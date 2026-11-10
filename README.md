# Task Manager

Jednoduchá konzolová aplikace pro správu úkolů. První projekt kurzu Engeto Testing Akademie.

Autor: Sandra Vondrová

## Co program umí

- přidat nový úkol (název a popis),
- zobrazit všechny uložené úkoly,
- odstranit úkol podle jeho čísla,
- ukončit program.

Úkoly se ukládají pouze do paměti. Po ukončení programu se neuchovávají.

## Požadavky

- **Python 3.9 nebo novější** (program používá zápis typů `list[dict[str, str]]`, který starší verze neznají)
- žádné další knihovny – program používá jen standardní knihovnu Pythonu

Nainstalovanou verzi Pythonu zjistíte příkazem:

```
python --version
```

V systémech Linux a macOS se místo `python` obvykle používá příkaz `python3`.

## Spuštění

1. Stáhněte si repozitář – buď jako ZIP (tlačítko **Code → Download ZIP**), nebo příkazem:

   ```
   git clone https://github.com/SanVondrova/engeto-projekt1_task-manager.git
   ```

2. V příkazovém řádku přejděte do složky projektu:

   ```
   cd engeto-projekt1_task-manager
   ```

   Po stažení jako ZIP se rozbalená složka jmenuje `engeto-projekt1_task-manager-main`.

3. Spusťte program:

   ```
   python engeto_projekt1.py
   ```

   V systémech Linux a macOS: `python3 engeto_projekt1.py`.

## Ovládání

Po spuštění se zobrazí hlavní menu. Zadejte číslo požadované možnosti a potvrďte klávesou Enter. Po dokončení každé akce se program vrátí do hlavního menu, volba 4 program ukončí.

```
Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4): 1

Zadejte název úkolu: Nákup
Zadejte popis úkolu: Koupit mléko a chléb
Úkol 'Nákup' byl přidán.

Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4): 2

Seznam úkolů:
1. Nákup - Koupit mléko a chléb
```

## Soubory projektu

| Soubor | Popis |
|--------|-------|
| `engeto_projekt1.py` | zdrojový kód aplikace |
| `engeto__projekt1_test.md` | testovací případy pro všechny funkce aplikace |
| `README.md` | popis projektu a návod ke spuštění |

## Testování

Testovací případy včetně kroků, očekávaných a skutečných výsledků jsou popsány v souboru [engeto__projekt1_test.md](engeto__projekt1_test.md).
