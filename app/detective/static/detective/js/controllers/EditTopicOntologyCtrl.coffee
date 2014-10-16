class window.EditTopicOntologyCtrl
    @$inject: ['$scope', 'Page', '$rootScope', 'topic']
    constructor: (@scope, @Page, @rootScope, @topic)->
        @Page.title "Ontology Editor", no
        return unless @topic.ontology_as_json?
        # actions
        @scope.addNewModel                = @addNewModel
        @scope.addNewRelationship         = @addNewRelationship
        @scope.editModel                  = @editModel
        @scope.saveModel                  = @saveModel
        @scope.cancelModel                = @cancelModel
        @scope.isModelUnchanged           = @isModelUnchanged
        @scope.removeField                = @removeField
        @scope.addField                   = @addField
        @scope.accordionShouldBeDisabled  = @accordionShouldBeDisabled
        # data
        @scope.models          = @topic.ontology_as_json
        @scope.relationships   = {}
        @scope.fieldTypes      = ["string", "url", "integer", "integerarray", "datetimestamp", "datetime", "date", "time", "boolean", "float"]
        @scope.newModel        = {}
        @scope.newRelationship = {}
        console.log "models", @scope.models
        for model in @scope.models
            for field in model.fields
                @scope.relationships[model.name] = [] unless @scope.relationships[model.name]?
                @scope.relationships[model.name].push field if field.type == "relationship"

    addNewModel: =>
        new_model =
            fields              : [{name:"name", verbose_name:"Name", type:"string"}]
            name                : @scope.newModel.Name # TODO: slugify
            verbose_name        : @scope.newModel.Name
            verbose_name_plural : @scope.newModel.NamePlural
            help_text           : @scope.newModel.HelpText
        @scope.models.push(new_model)
        @scope.newModel = {}

    addNewRelationship: =>
        new_relationship_field = {
            fields        : []
            help_text     : ""
            name          : @scope.newRelationship.Name # TODO: slugify
            verbose_name  : @scope.newRelationship.Name
            related_name  : @scope.newRelationship.ReverseName
            related_model : @scope.newRelationship.and
            rules         :  []
            type          : "relationship"

        }
        console.log new_relationship_field
        idx_model_to_update = @scope.models.indexOf(_.find(@scope.models, ((m) => @scope.newRelationship.between == m.name)))
        @scope.models[idx_model_to_update].fields.push(new_relationship_field)
        new_relationship_field = {}

    editModel: (model) =>
        @scope.editingModel = angular.copy(model)
        console.log "editModel", model

    saveModel:  =>
        model = @scope.editingModel
        # create the name from the verbose name if doesn't exist
        for field in model.fields
            if not field.name?
                # slugify
                field.name = field.verbose_name
                .toLowerCase()
                .replace(/\ /g, '-')
                .replace(/[^\w-]+/g, '')
                # TODO : check if doesn't exist
        idx_model_to_update = @scope.models.indexOf(_.find(@scope.models, ((m) -> model.name == m.name)))
        # update
        if idx_model_to_update > -1
            @scope.models[idx_model_to_update] = model
        @scope.editingModel = null
        console.log "model saved", @scope.models[idx_model_to_update]

    cancelModel: =>
        @scope.editingModel = null

    isModelUnchanged: =>
        idx_model_to_update = @scope.models.indexOf(_.find(@scope.models, ((m) => @scope.editingModel.name == m.name)))
        angular.equals(@scope.editingModel, @scope.models[idx_model_to_update])

    addField: =>
        @scope.editingModel.fields.push({})

    removeField: (field) =>
        index = @scope.editingModel.fields.indexOf(field)
        if index > -1
            @scope.editingModel.fields.splice(index, 1) if @scope.editingModel.fields[index]?

    accordionShouldBeDisabled: (accordion_name) =>
        if @scope.editingModel?
            return true

angular.module('detective.controller').controller 'EditTopicOntologyCtrl', EditTopicOntologyCtrl

# EOF