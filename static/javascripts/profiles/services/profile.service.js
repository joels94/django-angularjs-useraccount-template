/**
* Profile
* @namespace app.profiles.services
*/
(function () {
  'use strict';

  angular
    .module('app.profiles.services')
    .factory('Profile', Profile);

  Profile.$inject = ['$http'];

  /**
  * @namespace Profile
  */
  function Profile($http) {
    /**
    * @name Profile
    * @desc The factory to be returned
    * @memberOf app.profiles.services.Profile
    */
    var Aparam={};
    Aparam;
    var Profile = {
      destroy: destroy,
      get: get,
      update: update
    };

    return Profile;

    /////////////////////

    /**
    * @name destroy
    * @desc Destroys the given profile
    * @param {Object} profile The profile to be destroyed
    * @returns {Promise}
    * @memberOf app.profiles.services.Profile
    */
    function destroy(id) {
      console.log("Hello " + id);
      return $http.delete('/api/v1/profile/'+id+'/');
    }


    /**
    * @name get
    * @desc Gets the profile for user with username `username`
    * @param {string} username The username of the user to fetch
    * @returns {Promise}
    * @memberOf app.profiles.services.Profile
    */
    function get(uid) {
      return $http.get('/api/v1/profile/'+uid+'/');
    }


    /**
    * @name update
    * @desc Update the given profile
    * @param {Object} profile The profile to be updated
    * @returns {Promise}
    * @memberOf app.profiles.services.Profile
    */
    function update(p) {
      return $http.put('/api/v1/profile/'+p.id+'/', p);
    }
  }
})();
