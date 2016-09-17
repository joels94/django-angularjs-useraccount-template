
(function () {
  'use strict';

  angular
    .module('app.authentication.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location','Authentication'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, Authentication) {
    var vm = this;

    vm.register = register;

    /**
    * @name register
    * @desc Register a new user
    * @memberOf app.authentication.controllers.RegisterController
    */
    function register() {
      Authentication.register(vm.email, vm.password, vm.username);
    }
    
    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf app.authentication.controllers.RegisterController
     */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }

  }
})();