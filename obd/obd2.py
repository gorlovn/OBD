#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
from obd_conf import auth, obdsim_url
from obd_conf import GREEN, BLUE, PINK, YELLOW, RED, ENDC

import logging

log = logging.getLogger(__name__)
r_string = obdsim_url + "obdstate.json"

class OBDConnection:

    def __init__(self):
        self.content = None
        sout = "Opening connection on {0}".format(obdsim_url)
        log.info(sout)
        try:
            r = requests.get(r_string, auth=auth)
            if r.status_code == 200:
                sout = "Successfully connected to {0}".format(obdsim_url)
                log.info(sout)
                rj = r.json()
                self.content = rj["content"]
            else:
                s_code = "Connection Status Code: {0}".format(r.status_code)
                log.warn(s_code)
                sout = "Could not connect! Aborting!"
                log.warn(sout)
                exit()
        except OSError:
            sout = "Could not connect! Aborting!"
            log.warn(sout)
            exit()

    def getState(self):
        try:
            r = requests.get(r_string, auth=auth)
            if r.status_code == 200:
                rj = r.json()
                content = rj["content"]
                self.content = content
                result = {}
                for item in content:
                    name = item["name"]
                    val  = item["val"]
                    result[name] = val
                return result
            else:
                s_code = "Connection Status Code: {0}".format(r.status_code)
                log.warn(s_code)
                sout = "Could not connect!"
                log.warn(sout)
                return None
        except OSError:
            sout = "Could not connect! Aborting!"
            log.warn(sout)
            return None
