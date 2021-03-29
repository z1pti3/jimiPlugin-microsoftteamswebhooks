from core import plugin, model

class _microsoftteamswebhooks(plugin._plugin):
    version = 0.31

    def install(self):
        # Register models
        model.registerModel("microsoftteamswebhooksPostMessage","_microsoftteamswebhooksPostMessage","_action","plugins.microsoftteamswebhooks.models.action")
        model.registerModel("microsoftteamswebhooksResponse","_microsoftteamswebhooksResponse","_trigger","plugins.microsoftteamswebhooks.models.trigger")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("microsoftteamswebhooksPostMessage","_microsoftteamswebhooksPostMessage","_action","plugins.microsoftteamswebhooks.models.action")
        model.deregisterModel("microsoftteamswebhooksResponse","_microsoftteamswebhooksResponse","_trigger","plugins.microsoftteamswebhooks.models.trigger")
        return True

    def upgrade(self,LatestPluginVersion):
        if self.version < 0.2:
            model.registerModel("microsoftteamswebhooksResponse","_microsoftteamswebhooksResponse","_trigger","plugins.microsoftteamswebhooks.models.trigger")
