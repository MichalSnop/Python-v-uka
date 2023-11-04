jmeno_souboru = "novy_soubor.txt"
pozdrav = "Ahoj, toto je první zápis do textového souboru"

txt_soubor = open(jmeno_souboru, mode="w")
txt_soubor.write(pozdrav)
# řádné zavření souboru
txt_soubor.close()