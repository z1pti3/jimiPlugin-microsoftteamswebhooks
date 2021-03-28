from core.models import action
from core import auth, db, helpers

from plugins.microsoftteamswebhooks.includes import microsoftteamswebhooks

class _microsoftteamswebhooksPostMessage(action._action):
    url = str()
    message = str()

    def doAction(self,data):
        message = helpers.evalString(self.message,{"data" : data["flowData"]})
        url = auth.getPasswordFromENC(self.url)

        result = microsoftteamswebhooks._microsoftteamswebhooks(url).postMessage(message)

        if result:
            return {"result" : True, "rc" : 0, "msg" : "Message posted."}
        else:
            return {"result" : False, "rc" : 400, "msg" : "Invalid response from web service, check your url."}

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "url" and not value.startswith("ENC "):
            if db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.url = "ENC {0}".format(auth.getENCFromPassword(value))
                return True
            return False
        return super(_microsoftteamswebhooksPostMessage,self).setAttribute(attr,value,sessionData=sessionData)

