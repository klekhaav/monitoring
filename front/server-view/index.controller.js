(function () {
    'use strict';

    angular
        .module('app')
        .controller('ServerView.IndexController', Controller);

    function Controller($scope, $rootScope, $localStorage, $window, $location, ServerInfoService ) {
        $rootScope.info = {};
        $scope.dataSource = {};
        $scope.dataSource.chart = {
            caption: "CPU load",
            subCaption: "per core",
            numberPrefix: "%",
            theme: "ocean"
        };
        $scope.showList = false
        $scope.dataSource.data = [];
        ServerInfoService.get($localStorage.currentUser.email,
                              $rootScope.serverview.address,
                              $rootScope.serverview.port).then(function (data) {
            $rootScope.info = data;
            for (var i = 0; i < $rootScope.info.cpu_load.length; i++) {
                $scope.dataSource.data.push({
                        label: "core#" + i,
                        value: $rootScope.info.cpu_load[i]
                    });
            }
        });


        $scope.updateMyChartData = function () {
            $scope.dataSource.data = [];
            ServerInfoService.get($localStorage.currentUser.email,
                                  $rootScope.serverview.address,
                                  $rootScope.serverview.port).then(function (data) {
                $rootScope.info = data;
                $scope.dataSource.chart= {
                    caption: "CPU load",
                    subCaption: "per core",
                    numberPrefix: "%",
                    theme: "ocean"
                };
                for (var i = 0; i < $rootScope.info.cpu_load.length; i++) {
                    $scope.dataSource.data.push({
                            label: "core#" + i,
                            value: $rootScope.info.cpu_load[i]
                        });
                }
            });
        };

        $scope.showProcessList = function () {
            $scope.showList = !$scope.showList
        }

        $scope.back = function () {
            $location.path('/home')
        };
    }

})();
