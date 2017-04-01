import os

from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from .main import *

__all__ = ['riotwatcher']

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ROOT_DIR, "riotwatcher.yml")) as f:
    API_KEY = load(f)['api-key'].strip()
    print("API KEY: %s" % API_KEY)