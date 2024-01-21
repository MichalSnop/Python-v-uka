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
#Tato funkce provádí součet čísel pro jednotlivé strany a obce, které mají více než jeden volební obvod.
def get_sum_numbers(middle_numbers):
    nums = []
    for index, row in enumerate(middle_numbers):
        for pos, num in enumerate(row):
            if index == 0:
                nums.append(int(num))
            else:
                nums[pos] += int(middle_numbers[index][pos])
    return nums
#Tato funkce provádí součet hlasů pro jednotlivé strany přes více volebních obvodů v rámci daného města nebo obce.
def sum_party_numbers(middle_links):
    all_numbers = []
    for web in middle_links:
        middle_numbers = []
        for web_page in web:
            url_arg = MAIN_URL + web_page
            soup_3 = get_html(url_arg)
            numbers = []
            for index, tb in enumerate(soup_3.find_all("div", {"class": "t2_470"})):
                for td in tb.find_all("td", {"headers": NUMBER.format(index + 1, index + 1)}):
                    if td.text == "-":
                        continue
                    else:
                        numbers.append(td.text)
            middle_numbers.append(numbers)
    sum_numbers = get_sum_numbers(middle_numbers)
    return sum_numbers

#Tato funkce získává počet hlasů pro jednotlivé politické strany.
def get_party_numbers(soup_2):
    numbers = []
    for index, tb in enumerate(soup_2.find_all("div", {"class": "t2_470"})):
        for number in tb.find_all("td", {"headers": NUMBER.format(index + 1, index + 1)}):
            if number.text == "-":
                continue
            else:
                numbers.append(number.text)
    return numbers

#Tato funkce spočítá informace jako počet registrovaných voličů, vydaných obálek a platných hlasů pro všechny volební obvody daného města nebo obce.
def sum_header_data(middle_links):
    for web in middle_links:
        volici_in_list, provide_envelopes, valid_votes = 0, 0, 0
        for web_page in web:
            url_arg = MAIN_URL + web_page
            soup_3 = get_html(url_arg)
            for tb in soup_3.find_all("table", {"id": "ps311_6_t1"}):
                vol_sez, vyd_ob, pl_hl = '', '', ''
                tds = tb.find_all("td")
                for char in tds[1].text:
                    if char.isnumeric() or char == ",":
                        vol_sez += str(char)
                    else:
                        continue
                for char in tds[3].text:
                    if char.isnumeric() or char == ",":
                        vyd_ob += str(char)
                    else:
                        continue
                for char in tds[4].text:
                    if char.isnumeric() or char == ",":
                        pl_hl += str(char)
                    else:
                        continue
                volici_in_list += int(vol_sez.replace(",", "."))
                provide_envelopes += int(vyd_ob.replace(",", "."))
                valid_votes += int(pl_hl.replace(",", "."))
        return [str(volici_in_list), str(provide_envelopes), str(valid_votes)]

#Tato funkce získává informace o kandidujících stranách.
def get_cand_parties(soup_2):
    cand_parties = []
    for index, tb in enumerate(soup_2.find_all("div", {"class": "t2_470"})):
        for party in tb.find_all("td", {"headers": CAND_PARTY.format(index + 1, index + 1)}):
            if party.text == '-':
                continue
            else:
                cand_parties.append(party.text)
    return cand_parties   

#Tato funkce získává odkazy na další stránky s dalšími informacemi pro všechny volební obvody daného města nebo obce.
def get_middle_links(soup_2):
    district_links = []
    for middle_table in soup_2.find_all("table", {"class": "table"}):
        for middle_td in middle_table.find_all("td", {"headers": "s1"}):
            for middle_link in middle_td.find_all("a"):
                district_links.append(middle_link.get("href"))
    return district_links
    
#Tato funkce získává informace jako počet registrovaných voličů, vydaných obálek a platných hlasů pro všechny volební obvody daného města nebo obce bez jejich součtu.
def get_all_header_data(soup_2):
    for tb in soup_2.find_all("table", {"id": "ps311_t1"}):
        header_data = []
        volici_in_list, provide_envelopes, valid_votes = '', '', ''
        tds = tb.find_all("td")
        for char in tds[3].text:
            if char.isnumeric() or char == ",":
                volici_in_list += str(char)
            else:
                continue
        for char in tds[4].text:
            if char.isnumeric() or char == ",":
                provide_envelopes += str(char)
            else:
                continue
        for char in tds[7].text:
            if char.isnumeric() or char == ",":
                valid_votes += str(char)
            else:
                continue
        return [volici_in_list, provide_envelopes, valid_votes]
