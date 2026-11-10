# Testovací případy projektu Task Manager

Autor: Sandra Vondrová

## Cíl testování

Cílem testování je ověřit správnou funkčnost aplikace Task Manager.

Testovací případy pokrývají:

- pozitivní scénáře
- negativní scénáře
- hraniční případy
- validaci vstupů
- chybové stavy

## Seznam požadavků

| ID | Požadavek |
|----|-----------|
| REQ-001 | Přidání nového úkolu |
| REQ-002 | Zobrazení seznamu úkolů |
| REQ-003 | Odstranění úkolu |
| REQ-004 | Ovládání aplikace pomocí menu |

---

# Souhrn testování

| Metrika | Hodnota |
|----------|----------|
| Počet testovacích případů | 34 |
| Provedeno | 34 |
| PASS | 34 |
| FAIL | 0 |
| Úspěšnost | 100 % |

## Závěr

Byly vytvořeny a provedeny testovací případy pro všechny funkce aplikace Task Manager.

Testování pokrylo:

- pozitivní scénáře
- negativní scénáře
- hraniční hodnoty
- validaci vstupů

V průběhu testování jsem nezjistila žádné chyby, které by bránily správné funkčnosti aplikace.

Všechny testovací případy byly vyhodnoceny jako PASS.


# Testovací případy – Funkce `hlavni_menu()`

## TM-HM-001 Výběr možnosti 1 – Přidat nový úkol

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-004

**Popis:** Ověření, že volba čísla 1 v hlavním menu správně spustí funkci `pridat_ukol()`.

**Vstupní podmínky:**
- Program je spuštěn.
- Zobrazuje se hlavní menu.

**Testovací data:** 1

**Kroky testu:**
1. Spusťte program.
2. Ověřte zobrazení hlavního menu.
3. Zadejte 1.
4. Stiskněte Enter.

**Očekávaný výsledek:** Program spustí funkci `pridat_ukol()`.

**Skutečný výsledek:** Program zobrazil výzvu „Zadejte název úkolu:“.

**Stav:** PASS

**Poznámky:** Ověřuje základní navigaci aplikace. Test končí zobrazením výzvy, samotné přidání úkolu ověřují scénáře TM-PU.

---

## TM-HM-002 Výběr možnosti 2 – Zobrazení úkolů

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-004

**Popis:** Ověření spuštění funkce `zobrazit_ukoly()`.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** 2

**Kroky testu:**
1. Zadejte 2.
2. Stiskněte Enter.

**Očekávaný výsledek:** Program spustí funkci `zobrazit_ukoly()` a zobrazí zprávu o prázdném seznamu.

**Skutečný výsledek:** Program zobrazil „Seznam úkolů je prázdný.“

**Stav:** PASS

**Poznámky:** Ověřuje přesměrování do funkce zobrazení.

---

## TM-HM-003 Výběr možnosti 3 – Odstranit úkol

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-004

**Popis:** Ověření spuštění funkce `odstranit_ukol()`.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Existuje alespoň jeden úkol.

**Testovací data:** 3

**Kroky testu:**
1. Zadejte 3.
2. Stiskněte Enter.

**Očekávaný výsledek:** Program zobrazí seznam úkolů a výzvu k odstranění.

**Skutečný výsledek:** Program zobrazil seznam úkolů a výzvu „Zadejte číslo úkolu, který chcete odstranit:“.

**Stav:** PASS

**Poznámky:** Ověřuje navigaci do funkce mazání. Test končí zobrazením výzvy, samotné odstranění úkolu ověřují scénáře TM-OU.

---

## TM-HM-004 Výběr možnosti 4 – Ukončení programu

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-004

**Popis:** Ověření korektního ukončení programu.

**Vstupní podmínky:** Program zobrazuje hlavní menu.

**Testovací data:** 4

**Kroky testu:**
1. Zadejte 4.
2. Stiskněte Enter.

**Očekávaný výsledek:** Program se ukončí.

**Skutečný výsledek:** Program zobrazil „Konec programu.“ a ukončil běh.

**Stav:** PASS

**Poznámky:** Kritický scénář aplikace.

---

## TM-HM-005 Neplatná číselná volba

**Priorita:** Medium

**Typ testu:** Negativní

**Požadavek:** REQ-004

**Popis:** Ověření zadání čísla mimo rozsah 1–4.

**Vstupní podmínky:** Program zobrazuje hlavní menu.

**Testovací data:** 5

**Kroky testu:**
1. Zadejte 5.
2. Stiskněte Enter.

**Očekávaný výsledek:** Program zobrazí hlášení o neplatné volbě a znovu nabídne hlavní menu.

**Skutečný výsledek:** Program zobrazil „Neplatná volba. Zadejte číslo 1 až 4.“ a znovu zobrazil hlavní menu.

**Stav:** PASS

**Poznámky:** Negativní test validace vstupu.

---

## TM-HM-006 Textový vstup v menu

**Priorita:** Medium

**Typ testu:** Negativní

**Požadavek:** REQ-004

**Popis:** Ověření zadání textu místo čísla.

**Vstupní podmínky:** Program zobrazuje hlavní menu.

**Testovací data:** abc

**Kroky testu:**
1. Zadejte abc.
2. Stiskněte Enter.

**Očekávaný výsledek:** Program zobrazí hlášení o neplatné volbě a znovu nabídne hlavní menu.

**Skutečný výsledek:** Program zobrazil „Neplatná volba. Zadejte číslo 1 až 4.“ a znovu zobrazil hlavní menu.

**Stav:** PASS

**Poznámky:** Ověřuje robustnost vstupní validace.

---

## TM-HM-007 Prázdný vstup v menu

**Priorita:** Medium

**Typ testu:** Hraniční případ

**Požadavek:** REQ-004

**Popis:** Ověření stisknutí Enter bez zadání hodnoty.

**Vstupní podmínky:** Program zobrazuje hlavní menu.

**Testovací data:** [Enter]

**Kroky testu:**
1. Do výzvy nic nepište.
2. Stiskněte pouze Enter.

**Očekávaný výsledek:** Program vyhodnotí vstup jako neplatný a znovu nabídne hlavní menu.

**Skutečný výsledek:** Program zobrazil „Neplatná volba. Zadejte číslo 1 až 4.“ a znovu zobrazil hlavní menu.

**Stav:** PASS

**Poznámky:** Hraniční test minimálního vstupu.

---

# Testovací případy – Funkce `pridat_ukol()`

## TM-PU-001 Přidání platného úkolu

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-001

**Popis:** Ověření úspěšného vytvoření úkolu.

**Vstupní podmínky:**
- Program je spuštěn.
- Zobrazuje se hlavní menu.

**Testovací data:** Název: Nákup, Popis: Koupit mléko

**Kroky testu:**
1. Zvolte možnost 1 (Přidat nový úkol).
2. Zadejte název Nákup a stiskněte Enter.
3. Zadejte popis Koupit mléko a stiskněte Enter.

**Očekávaný výsledek:** Úkol bude uložen, program zobrazí potvrzení a vrátí se do hlavního menu.

**Skutečný výsledek:** Program zobrazil „Úkol 'Nákup' byl přidán.“ a vrátil se do hlavního menu.

**Stav:** PASS

**Poznámky:** Základní scénář.

---

## TM-PU-002 Prázdný název

**Priorita:** High

**Typ testu:** Negativní

**Požadavek:** REQ-001

**Popis:** Ověření, že úkol s nevyplněným názvem nelze uložit a program nechá zadat údaje znovu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: [Enter], Popis: Test. Poté Název: Nákup, Popis: Koupit mléko

**Kroky testu:**
1. Zvolte možnost 1.
2. Na výzvu k zadání názvu stiskněte pouze Enter.
3. Zadejte popis Test.
4. Ověřte chybové hlášení a novou výzvu k zadání názvu.
5. Zadejte název Nákup a popis Koupit mléko.
6. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní na prázdný vstup, úkol neuloží a nechá zadat název i popis znovu. Po zadání platných údajů je v seznamu pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Název ani popis nesmí být prázdný. Zkuste to znovu.“ a znovu výzvu „Zadejte název úkolu:“. Po zadání platných údajů zobrazil „Úkol 'Nákup' byl přidán.“, seznam obsahoval pouze „1. Nákup - Koupit mléko“.

**Stav:** PASS

**Poznámky:** Povinné pole.

---

## TM-PU-003 Prázdný popis

**Priorita:** High

**Typ testu:** Negativní

**Požadavek:** REQ-001

**Popis:** Ověření, že úkol s nevyplněným popisem nelze uložit a program nechá zadat název i popis znovu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: Test, Popis: [Enter]. Poté Název: Nákup, Popis: Koupit mléko

**Kroky testu:**
1. Zvolte možnost 1.
2. Zadejte název Test.
3. Na výzvu k zadání popisu stiskněte pouze Enter.
4. Ověřte chybové hlášení a novou výzvu k zadání názvu.
5. Zadejte název Nákup a popis Koupit mléko.
6. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní na prázdný vstup, úkol neuloží a nechá zadat název i popis znovu. Po zadání platných údajů je v seznamu pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Název ani popis nesmí být prázdný. Zkuste to znovu.“ a znovu výzvu „Zadejte název úkolu:“. Po zadání platných údajů zobrazil „Úkol 'Nákup' byl přidán.“, seznam obsahoval pouze „1. Nákup - Koupit mléko“.

**Stav:** PASS

**Poznámky:** Povinné pole. Úkol s názvem Test se do seznamu neuložil.

---

## TM-PU-004 Prázdný název i popis

**Priorita:** Medium

**Typ testu:** Negativní

**Požadavek:** REQ-001

**Popis:** Ověření chování programu, když uživatel nevyplní název ani popis.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: [Enter], Popis: [Enter]. Poté Název: Nákup, Popis: Koupit mléko

**Kroky testu:**
1. Zvolte možnost 1.
2. Na výzvu k zadání názvu stiskněte pouze Enter.
3. Na výzvu k zadání popisu stiskněte pouze Enter.
4. Ověřte chybové hlášení a novou výzvu k zadání názvu.
5. Zadejte název Nákup a popis Koupit mléko.
6. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní na prázdný vstup, úkol neuloží a nechá zadat název i popis znovu. Po zadání platných údajů je v seznamu pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Název ani popis nesmí být prázdný. Zkuste to znovu.“ a znovu výzvu „Zadejte název úkolu:“. Po zadání platných údajů zobrazil „Úkol 'Nákup' byl přidán.“, seznam obsahoval pouze „1. Nákup - Koupit mléko“.

**Stav:** PASS

**Poznámky:** Kombinovaný negativní scénář.

---

## TM-PU-005 Pouze mezery

**Priorita:** Medium

**Typ testu:** Hraniční případ

**Požadavek:** REQ-001

**Popis:** Ověření, že vstup složený pouze z mezer program vyhodnotí jako prázdný.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: tři mezery, Popis: tři mezery. Poté Název: Nákup, Popis: Koupit mléko

**Kroky testu:**
1. Zvolte možnost 1.
2. Jako název zadejte tři mezery a stiskněte Enter.
3. Jako popis zadejte tři mezery a stiskněte Enter.
4. Ověřte chybové hlášení a novou výzvu k zadání názvu.
5. Zadejte název Nákup a popis Koupit mléko.
6. Zvolte možnost 2.

**Očekávaný výsledek:** Program vyhodnotí vstup jako prázdný, úkol neuloží a nechá zadat název i popis znovu. Po zadání platných údajů je v seznamu pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Název ani popis nesmí být prázdný. Zkuste to znovu.“ – vstup byl po `strip()` vyhodnocen jako prázdný. Po zadání platných údajů zobrazil „Úkol 'Nákup' byl přidán.“, seznam obsahoval pouze „1. Nákup - Koupit mléko“.

**Stav:** PASS

**Poznámky:** Hraniční případ. Bez odstranění mezer by vznikl úkol, který vypadá jako prázdný.

---

## TM-PU-006 Přidání prvního úkolu

**Priorita:** High

**Typ testu:** Hraniční případ

**Požadavek:** REQ-001

**Popis:** Ověření přidání úkolu do prázdného seznamu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: Test, Popis: První úkol

**Kroky testu:**
1. Zvolte možnost 1.
2. Zadejte název Test.
3. Zadejte popis První úkol.
4. Zvolte možnost 2.

**Očekávaný výsledek:** Úkol bude uložen jako první položka seznamu s pořadovým číslem 1.

**Skutečný výsledek:** Program zobrazil „Úkol 'Test' byl přidán.“, seznam obsahoval „1. Test - První úkol“.

**Stav:** PASS

**Poznámky:** První položka seznamu.

---

## TM-PU-007 Přidání dalšího úkolu

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-001

**Popis:** Ověření, že se další úkol přidá na konec seznamu a dříve uložený úkol zůstane beze změny.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu je jeden úkol: 1. Nákup - Koupit mléko.

**Testovací data:** Název: Úklid, Popis: Vysát obývák

**Kroky testu:**
1. Zvolte možnost 1.
2. Zadejte název Úklid.
3. Zadejte popis Vysát obývák.
4. Zvolte možnost 2.

**Očekávaný výsledek:** Nový úkol bude přidán na konec seznamu s pořadovým číslem 2, původní úkol zůstane na prvním místě.

**Skutečný výsledek:** Program zobrazil „Úkol 'Úklid' byl přidán.“, seznam obsahoval „1. Nákup - Koupit mléko“ a „2. Úklid - Vysát obývák“.

**Stav:** PASS

**Poznámky:** Ověření číslování.

---

## TM-PU-008 Velmi dlouhý název úkolu

**Priorita:** Low

**Typ testu:** Hraniční hodnota

**Požadavek:** REQ-001

**Popis:** Ověření, že program uloží úkol s neobvykle dlouhým názvem a nic z něj neořízne.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: 500× znak A, Popis: Test dlouhého názvu

**Kroky testu:**
1. Zvolte možnost 1.
2. Jako název vložte ze schránky text složený z 500 znaků A.
3. Zadejte popis Test dlouhého názvu.
4. Zvolte možnost 2.

**Očekávaný výsledek:** Úkol bude uložen s celým názvem a program neskončí chybou.

**Skutečný výsledek:** Úkol byl uložen i s názvem o délce 500 znaků, v seznamu se zobrazil celý název.

**Stav:** PASS

**Poznámky:** Hraniční test délky. Text lze připravit příkazem `python -c "print('A' * 500)"`.

---

## TM-PU-009 Velmi dlouhý popis úkolu

**Priorita:** Low

**Typ testu:** Hraniční hodnota

**Požadavek:** REQ-001

**Popis:** Ověření, že program uloží úkol s neobvykle dlouhým popisem a nic z něj neořízne.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: Test dlouhého popisu, Popis: 1000× znak B

**Kroky testu:**
1. Zvolte možnost 1.
2. Zadejte název Test dlouhého popisu.
3. Jako popis vložte ze schránky text složený z 1000 znaků B.
4. Zvolte možnost 2.

**Očekávaný výsledek:** Úkol bude uložen s celým popisem a program neskončí chybou.

**Skutečný výsledek:** Úkol byl uložen i s popisem o délce 1000 znaků, v seznamu se zobrazil celý popis.

**Stav:** PASS

**Poznámky:** Robustnost vstupu. Text lze připravit příkazem `python -c "print('B' * 1000)"`.

---

## TM-PU-010 Speciální znaky a diakritika

**Priorita:** Medium

**Typ testu:** Pozitivní

**Požadavek:** REQ-001

**Popis:** Ověření podpory české diakritiky a speciálních znaků.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: Žluťoučký kůň !@#$%, Popis: Příliš žluťoučký kůň neprošel při posouzení porotou.

**Kroky testu:**
1. Zvolte možnost 1.
2. Zadejte název z testovacích dat.
3. Zadejte popis z testovacích dat.
4. Zvolte možnost 2.

**Očekávaný výsledek:** Úkol bude uložen a zobrazen beze změny znaků.

**Skutečný výsledek:** Úkol byl uložen beze změny textu, seznam obsahoval „1. Žluťoučký kůň !@#$% - Příliš žluťoučký kůň neprošel při posouzení porotou.“

**Stav:** PASS

**Poznámky:** Test diakritiky a speciálních znaků.

---

# Testovací případy – Funkce `zobrazit_ukoly()`

## TM-ZU-001 Zobrazení prázdného seznamu úkolů

**Priorita:** High

**Typ testu:** Hraniční případ

**Požadavek:** REQ-002

**Popis:** Ověření správného zobrazení zprávy při pokusu zobrazit úkoly v prázdném seznamu.

**Vstupní podmínky:**
- Program je spuštěn.
- Seznam `ukoly` je prázdný.

**Testovací data:** Není vyžadováno.

**Kroky testu:**
1. Spusťte program.
2. V hlavním menu zvolte možnost 2.
3. Stiskněte Enter.

**Očekávaný výsledek:** Program oznámí, že v seznamu nejsou žádné úkoly.

**Skutečný výsledek:** Program zobrazil „Seznam úkolů je prázdný.“

**Stav:** PASS

**Poznámky:** Hraniční scénář ověřující práci s prázdným seznamem.

---

## TM-ZU-002 Zobrazení jednoho úkolu

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-002

**Popis:** Ověření správného výpisu jednoho uloženého úkolu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Název: Nákup, Popis: Koupit mléko

**Kroky testu:**
1. Přidejte úkol z testovacích dat (možnost 1).
2. Zvolte možnost 2.

**Očekávaný výsledek:** Program zobrazí jeden úkol s pořadovým číslem 1.

**Skutečný výsledek:** Program zobrazil „1. Nákup - Koupit mléko“.

**Stav:** PASS

**Poznámky:** Ověření výpisu jedné položky.

---

## TM-ZU-003 Zobrazení více úkolů

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-002

**Popis:** Ověření správného výpisu více uložených úkolů.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Nákup / Koupit mléko, Úklid / Vysát obývák, Sport / Běh 5 km (název / popis)

**Kroky testu:**
1. Přidejte tři úkoly z testovacích dat (možnost 1).
2. Zvolte možnost 2.

**Očekávaný výsledek:** Program zobrazí všechny úkoly ve správném pořadí.

**Skutečný výsledek:** Program zobrazil „1. Nákup - Koupit mléko“, „2. Úklid - Vysát obývák“ a „3. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Ověření enumerate(). Ověření správného číslování úkolů při jejich zobrazení.

---

## TM-ZU-004 Zachování pořadí úkolů

**Priorita:** Medium

**Typ testu:** Pozitivní

**Požadavek:** REQ-002

**Popis:** Ověření zachování pořadí vložených úkolů.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Úkol C / Třetí v abecedě, Úkol A / První v abecedě, Úkol B / Druhý v abecedě (název / popis), záměrně mimo abecední pořadí

**Kroky testu:**
1. Přidejte tři úkoly v pořadí uvedeném v testovacích datech (možnost 1).
2. Zvolte možnost 2.

**Očekávaný výsledek:** Pořadí výpisu odpovídá pořadí vložení, program úkoly neseřadí podle abecedy.

**Skutečný výsledek:** Pořadí výpisu odpovídalo pořadí vložení: „1. Úkol C - Třetí v abecedě“, „2. Úkol A - První v abecedě“, „3. Úkol B - Druhý v abecedě“.

**Stav:** PASS

**Poznámky:** Ověření integrity dat.

---

## TM-ZU-005 Zobrazení více než 10 úkolů

**Priorita:** Medium

**Typ testu:** Hraniční hodnota

**Požadavek:** REQ-002

**Popis:** Ověření správného číslování při větším počtu úkolů.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- Seznam úkolů je prázdný.

**Testovací data:** Úkol 1 až Úkol 11 s popisy Popis 1 až Popis 11

**Kroky testu:**
1. Přidejte 11 úkolů z testovacích dat (možnost 1).
2. Zvolte možnost 2.

**Očekávaný výsledek:** Všechny úkoly budou správně očíslovány.

**Skutečný výsledek:** Program zobrazil všech 11 úkolů, poslední dva řádky „10. Úkol 10 - Popis 10“ a „11. Úkol 11 - Popis 11“.

**Stav:** PASS

**Poznámky:** Hraniční test většího počtu položek.

---

# Testovací případy – Funkce `odstranit_ukol()`

## TM-OU-001 Odstranění existujícího úkolu

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-003

**Popis:** Ověření úspěšného odstranění existujícího úkolu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** 2

**Kroky testu:**
1. Zvolte možnost 3.
2. Ověřte, že program zobrazil seznam všech úkolů.
3. Zadejte číslo 2.
4. Zvolte možnost 2.

**Očekávaný výsledek:** Program zobrazí všechny úkoly, vybraný úkol odstraní a odstranění potvrdí. Ostatní úkoly zůstanou v seznamu.

**Skutečný výsledek:** Program zobrazil seznam tří úkolů a po zadání čísla 2 zprávu „Úkol 'Úklid' byl odstraněn.“ V seznamu zůstaly „1. Nákup - Koupit mléko“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Základní pozitivní scénář.

---

## TM-OU-002 Odstranění prvního úkolu

**Priorita:** High

**Typ testu:** Hraniční případ

**Požadavek:** REQ-003

**Popis:** Ověření odstranění první položky seznamu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** 1

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte číslo 1.
3. Zvolte možnost 2.

**Očekávaný výsledek:** Program odstraní první úkol. Zbývající úkoly zůstanou ve stejném pořadí a budou očíslovány od 1.

**Skutečný výsledek:** Program zobrazil „Úkol 'Nákup' byl odstraněn.“ V seznamu zůstaly „1. Úklid - Vysát obývák“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Dolní hranice platného rozsahu čísel úkolů.

---

## TM-OU-003 Odstranění posledního úkolu

**Priorita:** High

**Typ testu:** Hraniční případ

**Požadavek:** REQ-003

**Popis:** Ověření odstranění poslední položky seznamu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** 3

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte číslo 3.
3. Zvolte možnost 2.

**Očekávaný výsledek:** Program odstraní poslední úkol. První dva úkoly zůstanou beze změny.

**Skutečný výsledek:** Program zobrazil „Úkol 'Sport' byl odstraněn.“ V seznamu zůstaly „1. Nákup - Koupit mléko“ a „2. Úklid - Vysát obývák“.

**Stav:** PASS

**Poznámky:** Horní hranice platného rozsahu čísel úkolů.

---

## TM-OU-004 Odstranění jediného úkolu

**Priorita:** High

**Typ testu:** Hraniční případ

**Požadavek:** REQ-003

**Popis:** Ověření odstranění jediného úkolu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu je jeden úkol: 1. Nákup - Koupit mléko.

**Testovací data:** 1

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte číslo 1.
3. Zvolte možnost 2.

**Očekávaný výsledek:** Program úkol odstraní a seznam zůstane prázdný.

**Skutečný výsledek:** Program zobrazil „Úkol 'Nákup' byl odstraněn.“ Po volbě 2 zobrazil „Seznam úkolů je prázdný.“

**Stav:** PASS

**Poznámky:** Po odstranění posledního zbývajícího úkolu musí program dál správně pracovat s prázdným seznamem.

---

## TM-OU-005 Zadání čísla mimo rozsah

**Priorita:** Medium

**Typ testu:** Negativní

**Požadavek:** REQ-003

**Popis:** Ověření zadání čísla úkolu, který v seznamu neexistuje.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** 4, poté 1

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte číslo 4.
3. Ověřte hlášení a novou výzvu k zadání čísla.
4. Zadejte číslo 1.
5. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní, že úkol neexistuje, nic neodstraní a zeptá se na číslo znovu. Po zadání čísla 1 odstraní pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Takový úkol neexistuje.“ a znovu výzvu „Zadejte číslo úkolu, který chcete odstranit:“. Po zadání čísla 1 zobrazil „Úkol 'Nákup' byl odstraněn.“, v seznamu zůstaly „1. Úklid - Vysát obývák“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Číslo o 1 vyšší než počet úkolů, tedy hodnota těsně za horní hranicí.

---

## TM-OU-006 Zadání hodnoty 0

**Priorita:** Medium

**Typ testu:** Hraniční hodnota

**Požadavek:** REQ-003

**Popis:** Ověření zadání hodnoty 0, která je těsně pod nejnižším platným číslem úkolu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** 0, poté 1

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte číslo 0.
3. Ověřte hlášení a novou výzvu k zadání čísla.
4. Zadejte číslo 1.
5. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní, že úkol neexistuje, nic neodstraní a zeptá se na číslo znovu. Po zadání čísla 1 odstraní pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Takový úkol neexistuje.“ a znovu výzvu „Zadejte číslo úkolu, který chcete odstranit:“. Po zadání čísla 1 zobrazil „Úkol 'Nákup' byl odstraněn.“, v seznamu zůstaly „1. Úklid - Vysát obývák“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Hodnota 0 nesmí odstranit poslední úkol – v Pythonu by index -1 znamenal poslední položku seznamu.

---

## TM-OU-007 Zadání záporného čísla

**Priorita:** Medium

**Typ testu:** Negativní

**Požadavek:** REQ-003

**Popis:** Ověření zadání záporného čísla úkolu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** -1, poté 1

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte číslo -1.
3. Ověřte hlášení a novou výzvu k zadání čísla.
4. Zadejte číslo 1.
5. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní, že úkol neexistuje, nic neodstraní a zeptá se na číslo znovu. Po zadání čísla 1 odstraní pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Takový úkol neexistuje.“ a znovu výzvu „Zadejte číslo úkolu, který chcete odstranit:“. Po zadání čísla 1 zobrazil „Úkol 'Nákup' byl odstraněn.“, v seznamu zůstaly „1. Úklid - Vysát obývák“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Záporné číslo nesmí odstranit úkol počítaný od konce seznamu.

---

## TM-OU-008 Zadání textu místo čísla

**Priorita:** High

**Typ testu:** Negativní

**Požadavek:** REQ-003

**Popis:** Ověření zadání textu místo čísla úkolu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** abc, poté 1

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte text abc.
3. Ověřte hlášení a novou výzvu k zadání čísla.
4. Zadejte číslo 1.
5. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní na neplatný vstup, neskončí chybou, nic neodstraní a zeptá se na číslo znovu. Po zadání čísla 1 odstraní pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Musíte zadat platné číslo úkolu.“ a znovu výzvu „Zadejte číslo úkolu, který chcete odstranit:“. Po zadání čísla 1 zobrazil „Úkol 'Nákup' byl odstraněn.“, v seznamu zůstaly „1. Úklid - Vysát obývák“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Ověřuje ošetření výjimky `ValueError`.

---

## TM-OU-009 Prázdný seznam úkolů

**Priorita:** High

**Typ testu:** Hraniční případ

**Požadavek:** REQ-003

**Popis:** Ověření pokusu o odstranění úkolu, když v seznamu žádný úkol není.

**Vstupní podmínky:**
- Program je spuštěn.
- Seznam úkolů je prázdný.

**Testovací data:** Není vyžadováno.

**Kroky testu:**
1. Spusťte program.
2. V hlavním menu zvolte možnost 3.

**Očekávaný výsledek:** Program oznámí, že není co odstranit, na číslo úkolu se nezeptá a vrátí se do hlavního menu.

**Skutečný výsledek:** Program zobrazil „Není žádný úkol k odstranění.“ a vrátil se do hlavního menu.

**Stav:** PASS

**Poznámky:** Hraniční scénář ověřující práci s prázdným seznamem.

---

## TM-OU-010 Zadání desetinného čísla

**Priorita:** Medium

**Typ testu:** Negativní

**Požadavek:** REQ-003

**Popis:** Ověření zadání desetinného čísla místo celého čísla úkolu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** 1.5, poté 1

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte číslo 1.5.
3. Ověřte hlášení a novou výzvu k zadání čísla.
4. Zadejte číslo 1.
5. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní na neplatný vstup, nic neodstraní a zeptá se na číslo znovu. Po zadání čísla 1 odstraní pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Musíte zadat platné číslo úkolu.“ a znovu výzvu „Zadejte číslo úkolu, který chcete odstranit:“. Po zadání čísla 1 zobrazil „Úkol 'Nákup' byl odstraněn.“, v seznamu zůstaly „1. Úklid - Vysát obývák“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Číslo úkolu musí být celé číslo, hodnotu 1.5 program nezaokrouhluje.

---

## TM-OU-011 Prázdný vstup při odstraňování

**Priorita:** Medium

**Typ testu:** Hraniční případ

**Požadavek:** REQ-003

**Popis:** Ověření stisknutí Enter bez zadání čísla úkolu.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** [Enter], poté 1

**Kroky testu:**
1. Zvolte možnost 3.
2. Na výzvu k zadání čísla stiskněte pouze Enter.
3. Ověřte hlášení a novou výzvu k zadání čísla.
4. Zadejte číslo 1.
5. Zvolte možnost 2.

**Očekávaný výsledek:** Program upozorní na neplatný vstup, nic neodstraní a zeptá se na číslo znovu. Po zadání čísla 1 odstraní pouze úkol Nákup.

**Skutečný výsledek:** Program zobrazil „Musíte zadat platné číslo úkolu.“ a znovu výzvu „Zadejte číslo úkolu, který chcete odstranit:“. Po zadání čísla 1 zobrazil „Úkol 'Nákup' byl odstraněn.“, v seznamu zůstaly „1. Úklid - Vysát obývák“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Hraniční test minimálního vstupu.

---

## TM-OU-012 Opakované neplatné vstupy při odstraňování

**Priorita:** Medium

**Typ testu:** Negativní

**Požadavek:** REQ-003

**Popis:** Ověření, že se program při několika neplatných vstupech po sobě ptá na číslo úkolu stále znovu a do hlavního menu se vrátí až po zadání platného čísla.

**Vstupní podmínky:**
- Program zobrazuje hlavní menu.
- V seznamu jsou tři úkoly: 1. Nákup - Koupit mléko, 2. Úklid - Vysát obývák, 3. Sport - Běh 5 km.

**Testovací data:** abc, 0, 4, [Enter], poté 2

**Kroky testu:**
1. Zvolte možnost 3.
2. Zadejte postupně abc, 0, 4 a prázdný vstup (pouze Enter). Po každém vstupu ověřte hlášení a novou výzvu k zadání čísla.
3. Zadejte číslo 2.
4. Zvolte možnost 2.

**Očekávaný výsledek:** Po každém neplatném vstupu program zobrazí hlášení, nic neodstraní a zeptá se na číslo znovu. Po zadání čísla 2 odstraní pouze úkol Úklid a vrátí se do hlavního menu.

**Skutečný výsledek:** Program postupně zobrazil „Musíte zadat platné číslo úkolu.“, „Takový úkol neexistuje.“, „Takový úkol neexistuje.“ a „Musíte zadat platné číslo úkolu.“, pokaždé následovala nová výzva „Zadejte číslo úkolu, který chcete odstranit:“. Po zadání čísla 2 zobrazil „Úkol 'Úklid' byl odstraněn.“, v seznamu zůstaly „1. Nákup - Koupit mléko“ a „2. Sport - Běh 5 km“.

**Stav:** PASS

**Poznámky:** Ověřuje smyčku `while` ve funkci `odstranit_ukol()`. Po neplatném vstupu se program nevrací do hlavního menu.
