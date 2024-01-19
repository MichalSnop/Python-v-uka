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

#Tato funkce ukládá data do CSV souboru. Přijímá data o kandidujících stranách a další relevantní informace pro jednotlivé obce. Vytváří CSV soubor se získanými daty.
def save_to_csv(*data):
    print(f"Ukladam do souboru {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, mode="w", newline="", encoding="Windows-1250") as file:
        f_writer = csv.writer(file)
        f_writer.writerow(FIRST_ROW + cand_parties)
        for index, (code, city, envelope_info, party_number) in enumerate(
                zip(codes, cities, all_header_data, party_numbers)):
            volic = envelope_info[0]
            envelope = envelope_info[1]
            vote = envelope_info[2]
            f_writer.writerow([code, city, volic, envelope, vote] + party_number)
