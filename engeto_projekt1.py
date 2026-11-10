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

Úkoly jsou ukládány do seznamu "ukoly". Seznam vzniká ve funkci
hlavni_menu() a ostatním funkcím se předává jako parametr.

Spuštění: python engeto_projekt1.py (Python 3.9 nebo novější)
"""


def hlavni_menu() -> None:
    """
    Zobrazuje hlavní menu aplikace.

    Funkce běží ve smyčce, dokud uživatel nezvolí možnost 4.
    Podle zvolené možnosti volá příslušné funkce
    a předává jim seznam úkolů.
    """

    # Seznam pro ukládání úkolů – ostatním funkcím se předává jako parametr
    ukoly: list[dict[str, str]] = []

    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol(ukoly)

        elif volba == "2":
            zobrazit_ukoly(ukoly)

        elif volba == "3":
            odstranit_ukol(ukoly)

        elif volba == "4":
            print("\nKonec programu.")
            break

        else:
            print("Neplatná volba. Zadejte číslo 1 až 4.")


def pridat_ukol(ukoly: list[dict[str, str]]) -> None:
    """
    Přidá nový úkol do seznamu.

    Parametr:
    - ukoly: seznam úkolů, do kterého se nový úkol uloží

    Uživatel zadává:
    - název úkolu
    - popis úkolu

    Pokud některý údaj není vyplněn,
    funkce požádá o zadání názvu i popisu znovu.
    """

    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
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

        print(f"Úkol '{nazev}' byl přidán.")
        break


def zobrazit_ukoly(ukoly: list[dict[str, str]]) -> None:
    """
    Vypíše všechny uložené úkoly.

    Parametr:
    - ukoly: seznam úkolů, který se má vypsat

    Pokud seznam neobsahuje žádný úkol,
    uživatel je na tuto skutečnost upozorněn.
    """

    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")

    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol(ukoly: list[dict[str, str]]) -> None:
    """
    Odstraní vybraný úkol.

    Parametr:
    - ukoly: seznam úkolů, ze kterého se úkol odstraní

    Nejprve zobrazí všechny úkoly.
    Poté uživatel zadá číslo úkolu,
    který chce odstranit.

    Funkce ošetřuje:
    - prázdný seznam,
    - neplatné číslo úkolu,
    - nečíselný vstup.

    Při neplatném vstupu se funkce zeptá znovu,
    dokud uživatel nezadá číslo existujícího úkolu.
    """

    if not ukoly:
        print("\nNení žádný úkol k odstranění.")
        return

    # Výpis úkolů – využití existující funkce místo opakování kódu
    zobrazit_ukoly(ukoly)

    while True:
        try:
            cislo = int(
                input("\nZadejte číslo úkolu, který chcete odstranit: ")
            )

        except ValueError:
            print("Musíte zadat platné číslo úkolu.")
            continue

        if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)

            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
            break

        print("Takový úkol neexistuje.")


# Spuštění programu – pouze při přímém spuštění souboru, ne při importu
if __name__ == "__main__":
    hlavni_menu()
