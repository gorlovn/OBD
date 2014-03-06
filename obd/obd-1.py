#!/usr/bin/python
# -*- coding: utf-8 -*-
# obd-1.py - обращение к эмулятору OBD в виде web сервиса
#
import requests
from requests.auth import HTTPBasicAuth
payload = {'entry': 'New Entry'}
auth = HTTPBasicAuth('gnv@ctmed.ru', '10203040')
url = "http://127.0.0.1:8000/obdsim/default/api/obdstate.json"
r = requests.get(url, auth=auth)
print((r.status_code))
rj = r.json()
print(rj)

content = rj["content"]

for item in content:
    print(item)


