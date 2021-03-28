import hmac
import hashlib
import base64
import binascii
import urllib
import json
from flask import Blueprint, render_template, request

from plugins.microsoftteamswebhooks.models import trigger

import jimi

pluginPages = Blueprint('microsoftteamswebhooksPages', __name__)

@pluginPages.route("/microsoftteamswebhooks/<token>/",methods=["POST"])
def __PUBLIC__microsoftteamsRunWebhookTrigger(token):
    webhook = trigger._microsoftteamswebhooksResponse().getAsClass(query={ "token" : token })[0]
    if webhook.enabled:
        signature = jimi.api.request.headers.get('authorization').split(" ")[1]
        if validateMessage(jimi.api.request.data,jimi.auth.getPasswordFromENC(webhook.securityToken),signature):
            data = json.loads(jimi.api.request.data)
            events = []
            events.append(data)
            maxDuration = 0
            if webhook.maxDuration > 0:
                maxDuration = webhook.maxDuration
            jimi.workers.workers.new("microsoftteamswebhooks{0}".format(webhook._id),webhook.notify,(events,),maxDuration=maxDuration)
            return {}, 200
    return {}, 404

def validateMessage(message,key,signature):
    key = base64.b64decode(key)
    print(message)
    messageSignature = base64.b64encode(hmac.new(key, message, hashlib.sha256).digest()).decode()
    return signature ==  messageSignature
    