#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from obd_conf import auth, obdsim_url

r_string = obdsim_url + "obdstate.json"


class OBDException(Exception):
    pass


class OBDConnection:

    def __init__(self):
        self.content = None
        self.status_code = None
        try:
            r = requests.get(r_string, auth=auth, timeout=0.5)
            self.status_code = r.status_code
            if r.status_code == 200:
                rj = r.json()
                self.content = rj["content"]
        except:
            pass

    def getState(self):
        self.status_code = None
        try:
            r = requests.get(r_string, auth=auth)
            self.status_code = r.status_code
            if r.status_code == 200:
                rj = r.json()
                content = rj["content"]
                self.content = content
                result = {}
                for item in content:
                    name = item["name"]
                    val = item["val"]
                    result[name] = val
                return result
            else:
                return None
        except:
            return None
