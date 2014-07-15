angular.module('detective.service').factory("Summary", [ '$resource', '$http', '$stateParams', ($resource, $http, $stateParams)->
    defaultsParams =
        # Use the current topic parameter as default topic
        topic: -> $stateParams.topic or "common"

    $resource '/api/:topic/v1/summary/:id/', defaultsParams, {
        get:
            method : 'GET'
            isArray: false
        cachedGet:
            method : 'GET'
            isArray: false
            cache  : yes
        export:
            isArray : false
            method : 'GET'
            url :'/api/:topic/v1/summary/export/'
            responseType : 'arraybuffer'
            transformResponse : (data, getHeaders) ->
                filename = 'export.zip'
                contentDisposition = (do getHeaders)['content-disposition'].split ';'
                if contentDisposition[1]?
                    contentDisposition = contentDisposition[1].split '='
                    if contentDisposition[1]?
                        filename = contentDisposition[1]
                { data : data , filename : filename }
    }
])