"""
webscr4_2.py: third project to Engeto Online Python Academy
author: Michal Snopko
email: michalsnopko84@gmail.com
discord: michalsn.
"""

import csv
import sys
import requests
from bs4 import BeautifulSoup

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
        for code, city, envelope_info, party_number in zip(codes, cities, all_header_data, party_numbers):
            volic, envelope, vote = envelope_info
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
    volici_in_list, provide_envelopes, valid_votes = 0, 0, 0
    for web in middle_links:
        for web_page in web:
            url_arg = MAIN_URL + web_page
            soup_3 = get_html(url_arg)
            for tb in soup_3.find_all("table", {"id": "ps311_6_t1"}):
                tds = tb.find_all("td")
                vol_sez, vyd_ob, pl_hl = '', '', ''
                for char in tds[1].text:
                    if char.isnumeric() or char == ",":
                        vol_sez += str(char)
                for char in tds[3].text:
                    if char.isnumeric() or char == ",":
                        vyd_ob += str(char)
                for char in tds[4].text:
                    if char.isnumeric() or char == ",":
                        pl_hl += str(char)
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
    header_data = []
    volici_in_list, provide_envelopes, valid_votes = '', '', ''
    for tb in soup_2.find_all("table", {"id": "ps311_t1"}):
        tds = tb.find_all("td")
        for char in tds[3].text:
            if char.isnumeric() or char == ",":
                volici_in_list += str(char)
        for char in tds[4].text:
            if char.isnumeric() or char == ",":
                provide_envelopes += str(char)
        for char in tds[7].text:
            if char.isnumeric() or char == ",":
                valid_votes += str(char)
    return [volici_in_list, provide_envelopes, valid_votes]

#Tato funkce získává data z druhé úrovně stránek volebních obvodů, včetně informací o kandidujících stranách a počtu hlasů.
def get_second_data(links):
    all_header_data, middle_links, party_numbers = [], [], []
    for link in links:
        url_arg = MAIN_URL + link
        if "vyber" in link:
            soup_2 = get_html(url_arg)
            all_header_data.append(get_all_header_data(soup_2))
            cand_parties = get_cand_parties(soup_2)
            party_numbers.append(get_party_numbers(soup_2))
        else:
            soup_2 = get_html(url_arg)
            middle_links.append(get_middle_links(soup_2))
            all_header_data.append(sum_header_data(middle_links))
            party_numbers.append(sum_party_numbers(middle_links))
    return all_header_data, cand_parties, party_numbers

#Tato funkce získává kódy obcí, názvy měst a odkazy na další stránky s informacemi o volebních obvodech z hlavní stránky.
def get_first_columns(soup):
    tables = soup.find_all("div", {"class": "t3"})
    codes, cities, links = [], [], []
    
    for index, tr in enumerate(tables):
        code_cells = tr.find_all("td", {"headers": CODE.format(index + 1, index + 1)})
        city_cells = tr.find_all("td", {"headers": CITY.format(index + 1, index + 1)})
        link_cells = tr.find_all("td", {"headers": LINK.format(index + 1)})
        
        codes += [td.text for td in code_cells if not td.text == "-"]
        cities += [td.text for td in city_cells if not td.text == "-"]
        
        for td in link_cells:
            for link in td.find_all("a"):
                links.append(link.get("href"))
    
    return codes, cities, links

#Tato funkce získává HTML kód stránky pomocí knihovny requests a BeautifulSoup.
def get_html(url):
    r = requests.get(url)
    html = r.text
    return BeautifulSoup(html, "html.parser")

if len(sys.argv) != 3:
    print("Nespravny pocet zadanych argumentu. UKONCUJI election-scraper")
    exit()

url, OUTPUT_FILE = sys.argv[1:]
if not ".cz" in url and not ".csv" in OUTPUT_FILE:
    print("Spatne poradi argumentu. UKONCUJI election-scraper")
    exit()

print(f"STAHUJI DATA Z VYBRANEHO URL: {url}")
soup = get_html(url)
codes, cities, links = get_first_columns(soup)
all_header_data, cand_parties, party_numbers = get_second_data(links)
save_to_csv(codes, cities, all_header_data, cand_parties, party_numbers)
print("UKONCUJI election_scraper")