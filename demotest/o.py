#!/usr/bin/env python

import os,sys
sys.path.insert(0, '/home/wyt/Desktop/demotest/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demotest.settings")
import django
django.setup()

from demo.models import JD
print 'aa'
print sys.argv
print JD.objects.all()
