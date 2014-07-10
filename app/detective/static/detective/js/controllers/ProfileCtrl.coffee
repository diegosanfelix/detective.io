class ProfileCtrl
    # Injects dependancies
    @$inject: ['$scope', '$routeParams', 'Common', 'Page', 'user']

    constructor: (@scope,  @routeParams, @Common, @Page, user)->
        @Page.title user.username
        @Page.loading yes
        # ──────────────────────────────────────────────────────────────────────
        # Scope attributes
        # ──────────────────────────────────────────────────────────────────────        
        # Get the user's topics
        @scope.userTopics = @Common.query type: "topic", author__id: user.id
        # Get the user
        @scope.user = @Common.get type: "user", id: user.id, =>
            @scope.user.contribution_groups = _.filter @scope.user.groups, (x) => x.topic.author.id isnt @scope.user.id

        # ──────────────────────────────────────────────────────────────────────
        # Scope watchers
        # ──────────────────────────────────────────────────────────────────────
        @scope.$watchCollection "[userTopics.$resolved, user.$resolved]", (resolved)=>      
            @Page.loading( angular.equals(resolved, [yes, yes]) ) if @Page.loading()
        , yes

        # ──────────────────────────────────────────────────────────────────────
        # Scope functions
        # ──────────────────────────────────────────────────────────────────────
        @scope.shouldShowTopics = @shouldShowTopics
        @scope.shouldShowContributions = @shouldShowContributions

    shouldShowTopics: =>
        @scope.userTopics.$resolved and @scope.userTopics.length

    shouldShowContributions: =>
        @scope.user.$resolved and @scope.user.contribution_groups.length

angular.module('detective.controller').controller 'profileCtrl', ProfileCtrl