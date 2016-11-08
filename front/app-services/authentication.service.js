(function () {
    'use strict';

    angular
        .module('app')
        .factory('AuthenticationService', Service);

//    var API = "http://localhost:8000/api/"
    var API = "https://localhost/api/"

    function Service($http, $localStorage, $window) {
        var service = {};

        service.Login = Login;
        service.Logout = Logout;

        return service;

        function Login(username, password, callback) {
            $http.post(API + 'token-auth/', {email: username, password: password})
                .success(function (response) {
                    if (response.token) {
                        $localStorage.currentUser = {email: username, token: response.token};
                        $http.defaults.headers.common.Authorization = 'JWT ' + response.token;
                        callback(true);
                    }
                }).error(function () {
                callback(false)
            })
        }

        function Logout() {
            delete $localStorage.currentUser;
            $http.defaults.headers.common.Authorization = '';
        }
    }
})();