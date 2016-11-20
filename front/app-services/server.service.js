(function () {
    'use strict';

    angular
        .module('app')
        .factory('ServerListByUserService', ServerListByUserService)
        .factory('ServerByIdService', ServerByIdService)
        .factory('ServerSaveService', ServerSaveService)
        .factory('ServerInfoService', ServerInfoService);

//    var API = "http://localhost:8000/api/"
    var API = "http://localhost/api/"

    function ServerListByUserService($http) {
        return {
            get: function (user) {
                return $http.get(API + 'monitor/servers/?user_login=' + user)
                    .then(function (resp) {
                        return resp.data;
                    });
            }
        }
    }

    function ServerSaveService($http) {
        return {
            post: function (order) {
                return $http.post(API + 'monitor/servers/', order)
                    .then(function (resp) {
                        return resp.data;
                    });
            }
        }
    }

    function ServerByIdService($http) {
        return {
            get: function (id) {
                return $http.get(API + 'monitor/servers/' + id + '/')
                    .then(function (resp) {
                        return resp.data;
                    });
            }
        }
    }

    function ServerInfoService($http) {
        return {
            get: function (user, host, port) {
                return $http.get(API + 'monitor/info/' + user + '/' + host + "/" + port + '/')
                    .then(function (resp) {
                        return resp.data;
                    });
            }
        }
    }
})();
