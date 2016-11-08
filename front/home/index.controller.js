(function () {
    'use strict';

    angular
        .module('app')
        .controller('Servers.IndexController', Controller);

    function Controller($scope, $rootScope, $location, $localStorage, ServerListByUserService, ServerSaveService) {
        $scope.serverslist = [];
        $rootScope.serverview = {};

        ServerListByUserService.get($localStorage.currentUser.email).then(function (data) {
            $scope.serverslist = data.results;
        });

        $scope.select = function (item) {
            $rootScope.serverview = item;
            $location.path('/server-view')
        };
    }

})();
