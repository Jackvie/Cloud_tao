#! /bin/bash

cd ..
pwd
python3  manage.py collectstatic --noinput
rm -rf animate/static/images/*

