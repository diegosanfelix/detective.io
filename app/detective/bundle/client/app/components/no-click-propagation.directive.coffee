angular.module('detective').directive "noClickPropagation", ($document) ->
    restrict: "A"
    link: (scope, elem, attr, ctrl) ->
        elem.bind "click", (e) ->
            do e.preventDefault
            do e.stopPropagation
