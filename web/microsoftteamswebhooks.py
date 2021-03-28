import json
import urllib
import requests
from flask import Blueprint, render_template, request

from plugins.microsoftteamswebhooks.models import trigger

import jimi

pluginPages = Blueprint('microsoftteamswebhooksPages', __name__)

@pluginPages.route("/microsoftteamswebhooks/<token>/",methods=["POST"])
def __PUBLIC__outboundWebHook(token):
    apiEndpoint = "microsoftteamswebhooks/{0}/".format(token)
    url = jimi.cluster.getMaster()
    headers = { "authorization" : jimi.api.request.headers.get('authorization') }
    response = requests.post("{0}/{1}/{2}".format(url,"plugin",apiEndpoint), headers=headers, data= jimi.api.request.data, timeout=60)
    if response.status_code == 200:
        return { "type" : "message", "text" : "One moment please..."  }, 200
