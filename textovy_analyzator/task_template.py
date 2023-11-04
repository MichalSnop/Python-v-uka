hlavicka = '''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Michal Snopko
email: michalsnopko84@gmail.com
discord: michalsn.
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
print(hlavicka)
print('-' * 40)
# Vyžádání přihlašovacího jména a hesla
uzivatelske_jmeno = input("username: ")
heslo = input("password: ")
pocet_textu = len(TEXTS)
# Zkontrolujte, zda zadané údaje odpovídají registrovaným uživatelům
if uzivatelske_jmeno in registrovani_uzivatele and registrovani_uzivatele[uzivatelske_jmeno] == heslo:
    print(f"Welcome to the app, {uzivatelske_jmeno}! We have {pocet_textu} texts to be analyzed.")
    print('-' * 40)
    # Uživatel je přihlášen, umožníme mu vybrat text
    try:
        cislo_textu = int(input(f"Enter a number btw. 1 and {pocet_textu} to select: "))
        print('-' * 40)
        if cislo_textu < 1 or cislo_textu > 3:
            print("The entered number is not valid. The program will be terminated.")
            quit()
        else:
            text = TEXTS[cislo_textu - 1]
            # Analýza vybraného textu.
            import re
            def text_bar_chart(data):
                print("LEN|    OCCURRENCES    |NR.")
                print('-' * 40)
                for key, value in data.items():
                    bar = "*" * value
                    print(f'{key:3}| {bar: <18} |{value}')
            def analyze_text(text):
                text[0]  # Vyberte text ze vstupního seznamu
                words = re.findall(r'\b[^\d\W]+\b', text)
                num_words = len(words)

                title_words = [word for word in words if word.istitle()]
                num_title_words = len(title_words)

                uppercase_words = [word for word in words if word.isupper()]
                num_uppercase_words = len(uppercase_words)

                lowercase_words = [word for word in words if word.islower()]
                num_lowercase_words = len(lowercase_words)

                numbers = re.findall(r'\b\d+\b', text)
                num_numbers = len(numbers)
                total_sum = sum(map(int, numbers))

                # Výstup statistik
                print(f'There are {num_words} words in the selected text.')
                print(f'There are {num_title_words} titlecase words.')
                print(f'There are {num_uppercase_words} uppercase words.')
                print(f'There are {num_lowercase_words} lowercase words.')
                print(f'There are {num_numbers} numeric strings.')
                print(f'The sum of all the numbers {total_sum}')
                print('-' * 40)

                # Analýza délek slov a vytvoření histogramu
                word_lengths = [len(word) for word in words]
                
                if word_lengths:
                    length_histogram = {i: word_lengths.count(i) for i in range(1, max(word_lengths) + 1)}
                    text_bar_chart(length_histogram)
                else:
                    print("No words to analyze.")
            # Spuštění analýzy
            analyze_text(text)
    except ValueError:
        print(f"Invalid input. Enter text number (1 and {pocet_textu}). The program will be terminated.")
        quit()
else:
    print("unregistered user, terminating the program...")
    quit()