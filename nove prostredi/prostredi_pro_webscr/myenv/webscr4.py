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

#FIRST PAGE TABLE DATA (cities etc.)
CODE = "t{}sa1 t{}sb1"
CITY = "t{}sa1 t{}sb2"
LINK = "t{}sa2"

#SECOND PAGE TABLE DATA (candidate parties etc.)
CAND_PARTY = "t{}sa1 t{}sb2"
NUMBER = "t{}sa2 t{}sb3"

FIRST_ROW = ["Code", "City", "Registered", "Envelopes", "Votes"]
