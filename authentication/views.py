from django.http import Http404
from rest_framework import permissions, viewsets

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

from django.contrib.auth import logout

from rest_framework import permissions


from django.contrib.auth import authenticate, login

from rest_framework import status, views
from rest_framework.response import Response

class ProfileView(views.APIView):
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return permissions.AllowAny(),
        if self.request.method == 'DELETE':
            return permissions.AllowAny(), IsAccountOwner(),
        if self.request.method == 'POST':
            return permissions.AllowAny(),
        if self.request.method == 'PUT':
            return permissions.AllowAny(), IsAccountOwner(),

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        username = data.get('username',None)
        account=Account.objects.create_user(email,password,username=username)
        serializer=AccountSerializer(account)
        if account!=None:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        try:
            account = self.get_object(pk)
            data=request.data

            password = data.get('password', None)
            c_password=data.get('confirm_password',None)
            username = data.get('username', None)
            tagline = data.get('tagline',None)

            print(password,c_password,username,tagline)

            if password!="" and c_password!="" and password==c_password:
                account.set_password(raw_password=password)

            if username!=account.username:
                account.username=username

            if tagline!="" and tagline!=account.tagline:
                account.tagline=tagline

            account.save()

            serializer = AccountSerializer(account)

            return Response(serializer.data)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = request.data

        email = data.get('email', None)
        password = data.get('password', None)
        print(email,password)
        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)
