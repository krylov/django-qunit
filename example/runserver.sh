#!/bin/sh

export PYTHONPATH=`pwd`:`pwd`/..:$PYTHONPATH
django-admin.py runserver --settings=settings 8080
