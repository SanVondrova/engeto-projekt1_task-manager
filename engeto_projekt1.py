"""
Projekt: Task Manager

Autor: Sandra Vondrová
Popis: 
Jednoduchá konzolová aplikace pro správu úkolů.
Umožňuje:
- přidávat úkoly,
- zobrazovat seznam úkolů,
- odstraňovat úkoly,
- ukončit program.

Úkoly jsou ukládány do seznamu "ukoly".
"""

# Globální seznam pro ukládání úkolů
ukoly = []


def hlavni_menu():
    """
    Zobrazuje hlavní menu aplikace.

    Funkce běží ve smyčce, dokud uživatel nezvolí možnost 4.
    Podle zvolené možnosti volá příslušné funkce.
    """

    while True:
        print("\nSprávce úkolů – Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()

        elif volba == "2":
            zobrazit_ukoly()

        elif volba == "3":
            odstranit_ukol()

        elif volba == "4":
            print("\nKonec programu.")
            break

        else:
            print("Neplatná volba. Zadejte číslo 1 až 4.")


def pridat_ukol():
    """
    Přidá nový úkol do seznamu.

    Uživatel zadává:
    - název úkolu
    - popis úkolu

    Pokud některý údaj není vyplněn,
    funkce požádá o zadání znovu.
    """

    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        # Kontrola prázdných vstupů
        if not nazev or not popis:
            print("Název ani popis nesmí být prázdný. Zkuste to znovu.")
            continue

        # Uložení úkolu jako slovníku
        ukol = {
            "nazev": nazev,
            "popis": popis
        }

        ukoly.append(ukol)

        print(f"Úkol {len(ukoly)} '{nazev}' byl přidán.")
        break


def zobrazit_ukoly():
    """
    Vypíše všechny uložené úkoly.

    Pokud seznam neobsahuje žádný úkol,
    uživatel je na tuto skutečnost upozorněn.
    """

    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")

    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol['nazev']} – {ukol['popis']}")


def odstranit_ukol():
    """
    Odstraní vybraný úkol.

    Nejprve zobrazí všechny úkoly.
    Poté uživatel zadá číslo úkolu,
    který chce odstranit.

    Funkce ošetřuje:
    - prázdný seznam,
    - neplatné číslo úkolu,
    - nečíselný vstup.
    """

    if not ukoly:
        print("\nNení žádný úkol k odstranění.")
        return

    print("\nSeznam úkolů:")

    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol['nazev']} – {ukol['popis']}")

    try:
        cislo = int(input("\nZadejte číslo úkolu, který chcete odstranit: "))

        if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)

            print(
                f"Úkol {cislo} '{odstraneny['nazev']}' byl odstraněn."
            )

        else:
            print("Takový úkol neexistuje.")

    except ValueError:
        print("Musíte zadat platné číslo úkolu.")


# Spuštění programu
hlavni_menu()