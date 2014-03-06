#!/usr/bin/python
# -*- coding: utf-8 -*-
# obd-2.py - обращение к OBD сервису с использованием
#            OBDConnection class
#
import logging
import sys
import codecs
from obd2 import OBDConnection

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

LOG_FILENAME = '_obd2.out'
logging.basicConfig(filename = LOG_FILENAME, level = logging.INFO,)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

log = logging.getLogger(__name__)


if __name__ == "__main__":

    obdLink = OBDConnection()
    state = obdLink.getState()
    for name in state:
        sout = "{0}: {1}".format(name, state[name])
        log.info(sout)

    sys.exit(0)
