def readinglineDataWIG20():
    with open("WIG20_notowania.txt", "r", encoding="UTF-8") as f:
        odczytywanie = True
        while odczytywanie == True:
            f.seek(0)
            print("Ktora linie chcesz odczytać?")
            print("Od 19.10.2022 to linia nr 3, z wczesniejszych dni sa dalej")

            a = int(input())
            i = 1
            while a > i:
                f.readline()
                i += 1
            print("Data       Zamkniecie  Otwarcie")
            print(f.readline())
            print("Czy chcesz odczytywać dalej? Wciśnij y na tak lub cokolwiek na nie")
            b = input()
            if b != "y":
                odczytywanie = False
        odczytywanie = True

def readingspecificDataWIG20():
        with open("WIG20_notowania.txt", "r", encoding="UTF-8") as f:
            plik = f.readlines()
        #readingspecificDataWIG20()
        KonkretneElementy = []
        for i in plik:
            temp = i.strip()
            KonkretneElementy.append(temp.split(" "))
        print("Wpisz Datę")
        data = input()
        sprawdzaniedaty = True
        for opcja in KonkretneElementy:
            for i in opcja:
                if data == i:
                    print("Otwarcie czy Zamkniecie? Wpisz o lub z")
                    wybór = input()
                    if wybór == "o":
                        print(opcja[5])
                        sprawdzaniedaty = False
                    if wybór == "z":
                        print(opcja[1])
                        sprawdzaniedaty = False
        if sprawdzaniedaty == True:
            print("Brak notowań w danym dniu")

turn_on = True
while turn_on == True:
    print("Notowania WIG20 od 19.09.2022 do 19.10.2022")
    print("Notowania prowadzone od poniedzialku do piatku")
    print("Proszę o wybranie opcji z poniższego menu","1 - Odczyt data + notowania z otwarcia i zamknięcia", "2 - Odczyt konkretnej wartosci z dnia", sep="\n")
    print("3 - Zakończenie działania programu")
    choice = int(input())
    if choice == 1:
        choice = 0
        readinglineDataWIG20()
    if choice == 2:
        readingspecificDataWIG20()
    if choice == 3:
        turn_on = False



