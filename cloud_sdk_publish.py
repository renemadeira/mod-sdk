#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import pycurl, random, shutil, json
from cStringIO import StringIO
from modsdk.crypto import NewKey
from modsdk.publisher import Publisher
from modsdk import settings

try:
    dirname = sys.argv[1]
    if dirname.endswith('/'):
        dirname = dirname[:-1]
except IndexError:
    print("usage: " + __file__.split('/')[-1] + ' path [url]')
    sys.exit(1)

try:
    url = sys.argv[2]
except IndexError:
    url = 'cloud.moddevices.com'

private_key = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')

result = Publisher(url, os.environ['USER'], private_key).publish(dirname)

if result['ok']:
    print("OK!")
else:
    print("ERRO: %s" % result['error'])

