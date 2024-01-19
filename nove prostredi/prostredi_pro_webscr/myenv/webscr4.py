"""
webscr3.py: third project to Engeto Online Python Academy
author: Michal Snopko
email: michalsnopko84@gmail.com
discord: michalsn.
"""

import requests
from bs4 import BeautifulSoup
import csv
import sys

MAIN_URL = "https://volby.cz/pls/ps2017nss/"
url, OUTPUT_FILE = "", ""