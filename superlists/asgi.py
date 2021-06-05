"""
ASGI config for superlists project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superlists.settings')

application = get_asgi_application()

# unix:/tmp/39.106.68.230.socket superlists.wsgi:application
#
# unix:/root/sites/120.53.108.140.socket

# [Unit]
# Description=Gunicorn server for 120.53.108.140
#
#
# [Service]
# Restart=on-failure
# User=wanglong
# WorkingDirectory=/root/sites/120.53.108.140/source
# ExecStart=/root/sites/120.53.108.140/virtualenv/bin/gunicorn --bind unix:/root/sites/120.53.108.140.socket superlists.wsgi:application
#
# [Install]
# WantedBy=multi-user.target

