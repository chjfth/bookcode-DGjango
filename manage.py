#!/usr/bin/env python2
import os
import sys

from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
