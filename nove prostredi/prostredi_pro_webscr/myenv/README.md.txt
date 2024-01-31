Projekt Scrapování Volebních Výsledků 2017
Popis projektu

Tento projekt je navržen k scrapování volebních výsledků z roku 2017 přímo z oficiálních webových stránek. Skript vytahuje data o hlasování pro jednotlivé obce a vytváří výstupní soubor ve formátu CSV.

Obsah Výstupního Souboru
Výstupní soubor vysledky.csv obsahuje informace pro každou obec, včetně:
Kód obce
Název obce
Počet registrovaných voličů
Počet vydaných obálek
Počet platných hlasů
Počet hlasů pro jednotlivé politické strany

Spuštění Skriptu:
Potřebné knihovny se nainstalují příkazem...pip install <jmeno_knihovny>
Jako první krok přejděte do virtuálního prostředí. příkazem CD 'umístění souboru'
Spusťte skript s dvěma argumenty (odkaz a název výstupního souboru): např... python webscr4.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106' 'vysledky_rychnovnk.csv'
odkaz: Odkaz na konkrétní územní celek na stránce voleb z roku 2017.
vysledky.csv: Název výstupního souboru ve formátu CSV.