#!/usr/bin/python
# -*- coding: utf-8 -*-

from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('gnv@ctmed.ru', '10203040')

obdsim_url = "http://bs.ctmed.ru/obdsim/default/api/"

GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
