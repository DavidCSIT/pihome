#!/usr/bin/env python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pi/pihome')
from webapp import app as application
application.secret_key = 'pihome'
