#!/usr/bin/python
# -*- coding: utf-8 -*-
# obd-1.py - обращение к эмулятору OBD в виде web сервиса
#
import requests
from requests.auth import HTTPBasicAuth 
payload = {'entry': 'New Entry'}
auth=HTTPBasicAuth('gnv@ctmed.ru', '10203040')
#r = requests.post("http://127.0.0.1:8000/obdsim/default/api/entries.json", data=payload, auth=auth)
r = requests.get("http://127.0.0.1:8000/obdsim/default/api/entries.json", auth=auth)
print r.status_code
rj = r.json()
print rj

content = rj[u"content"]

for item in content:
    print item


