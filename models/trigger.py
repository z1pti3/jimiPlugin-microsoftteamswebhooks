import secrets

import jimi

class _microsoftteamswebhooksResponse(jimi.trigger._trigger):
    token = str()
    securityToken = str()

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "token":
            self.token = secrets.token_hex(128)
            self.update(['token'])
            return True
        elif attr == "securityToken" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.securityToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_microsoftteamswebhooksResponse, self).setAttribute(attr,value,sessionData)