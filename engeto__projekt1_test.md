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
| Počet testovacích případů | 33 |
| Provedeno | 33 |
| PASS | 33 |
| FAIL | 0 |
| Úspěšnost | 100 % |

## Závěr

Byly vytvořeny a provedeny testovací případy pro všechny funkce aplikace Task Manager.

Testování pokrylo:

- pozitivní scénáře
- negativní scénáře
- hraniční hodnoty
- validaci vstupů

V průběhu testování jsem nezjištila žádné chyby, které by bránily správné funkčnosti aplikace.

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

**Poznámky:** Ověřuje základní navigaci aplikace.

---

## TM-HM-002 Výběr možnosti 2 – Zobrazení úkolů

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-004

**Popis:** Ověření spuštění funkce `zobrazit_ukoly()`.

**Vstupní podmínky:** Program zobrazuje hlavní menu.

**Testovací data:** 2

**Kroky testu:**
1. Zadejte 2.
2. Stiskněte Enter.

**Očekávaný výsledek:** Program zobrazí seznam úkolů nebo zprávu o prázdném seznamu.

**Skutečný výsledek:** Při prázdném seznamu program zobrazil „Seznam úkolů je prázdný.“

**Stav:** PASS

**Poznámky:** Ověřuje přesměrování do funkce zobrazení.

---

## TM-HM-003 Výběr možnosti 3 – Odstranit úkol

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-004

**Popis:** Ověření spuštění funkce `odstranit_ukol()`.

**Vstupní podmínky:** Existuje alespoň jeden úkol.

**Testovací data:** 3

**Kroky testu:**
1. Zadejte 3.
2. Stiskněte Enter.

**Očekávaný výsledek:** Program zobrazí seznam úkolů a výzvu k odstranění.

**Skutečný výsledek:** Program zobrazil seznam úkolů a výzvu k zadání čísla úkolu.

**Stav:** PASS

**Poznámky:** Ověřuje navigaci do funkce mazání.

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

**Očekávaný výsledek:** Program zobrazí hlášení o neplatné volbě.

**Skutečný výsledek:** Program zobrazil „Neplatná volba. Zadejte číslo 1 až 4.“

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

**Očekávaný výsledek:** Program zobrazí hlášení o neplatné volbě.

**Skutečný výsledek:** Program zobrazil „Neplatná volba. Zadejte číslo 1 až 4.“

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
1. Nestiskněte žádnou klávesu.
2. Stiskněte pouze Enter.

**Očekávaný výsledek:** Program vyhodnotí vstup jako neplatný.

**Skutečný výsledek:** Program zobrazil „Neplatná volba. Zadejte číslo 1 až 4.“

**Stav:** PASS

**Poznámky:** Hraniční test minimálního vstupu.

# Testovací případy – Funkce `pridat_ukol()`

## TM-PU-001 Přidání platného úkolu
**Priorita:** High
**Typ testu:** Pozitivní
**Požadavek:** REQ-001
**Popis:** Ověření úspěšného vytvoření úkolu.
**Vstupní podmínky:** Program běží.
**Testovací data:** Název=Nákup, Popis=Koupit mléko
**Kroky testu:** 1. Zvolte Přidat nový úkol. 2. Zadejte název. 3. Zadejte popis.
**Očekávaný výsledek:** Úkol bude uložen.
**Skutečný výsledek:** Program zobrazil „Úkol 1 'Nákup' byl přidán.“
**Stav:** PASS
**Poznámky:** Základní scénář.

## TM-PU-002 Prázdný název
**Priorita:** High
**Typ testu:** Negativní
**Požadavek:** REQ-001
**Popis:** Název není vyplněn.
**Vstupní podmínky:** Funkce spuštěna.
**Testovací data:** Název='', Popis='Test'
**Kroky testu:** Nechte název prázdný.
**Očekávaný výsledek:** Chybová zpráva.
**Skutečný výsledek:** „Název ani popis nesmí být prázdný. Zkuste to znovu.“
**Stav:** PASS
**Poznámky:** Povinné pole.

## TM-PU-003 Prázdný popis
**Priorita:** High
**Typ testu:** Negativní
**Požadavek:** REQ-001
**Skutečný výsledek:** „Název ani popis nesmí být prázdný. Zkuste to znovu.“
**Stav:** PASS
**Poznámky:** Povinné pole.

## TM-PU-004 Prázdný název i popis
**Skutečný výsledek:** „Název ani popis nesmí být prázdný. Zkuste to znovu.“
**Stav:** PASS
**Poznámky:** Kombinovaný negativní scénář.

## TM-PU-005 Pouze mezery
**Skutečný výsledek:** Vstup byl po strip() vyhodnocen jako prázdný.
**Stav:** PASS
**Poznámky:** Hraniční případ.

## TM-PU-006 Přidání prvního úkolu
**Skutečný výsledek:** „Úkol 1 'Test' byl přidán.“
**Stav:** PASS
**Poznámky:** První položka seznamu.

## TM-PU-007 Přidání dalšího úkolu
**Skutečný výsledek:** Úkol byl přidán na konec seznamu.
**Stav:** PASS
**Poznámky:** Ověření číslování.

## TM-PU-008 Velmi dlouhý název úkolu
**Skutečný výsledek:** Úkol byl uložen i s názvem o délce 500 znaků.
**Stav:** PASS
**Poznámky:** Hraniční test délky.

## TM-PU-009 Velmi dlouhý popis úkolu
**Skutečný výsledek:** Úkol byl uložen i s velmi dlouhým popisem.
**Stav:** PASS
**Poznámky:** Robustnost vstupu.

## TM-PU-010 Speciální znaky a diakritika
**Priorita:** Medium
**Typ testu:** Pozitivní
**Požadavek:** REQ-001
**Popis:** Ověření podpory české diakritiky a speciálních znaků.
**Vstupní podmínky:** Program je spuštěn.
**Testovací data:** Název: Žluťoučky kůň !@#$%
Popis: Příliš žluťoučký kůň neprošel při posouzení porotou.
**Kroky testu:** Zadat data a potvrdit.
**Očekávaný výsledek:** Úkol bude uložen.
**Skutečný výsledek:** Úkol byl uložen beze změny textu.
**Stav:** PASS
**Poznámky:** Test diakritiky a speciálních znaků.


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

**Skutečný výsledek:** Program zobrazil: Seznam úkolů je prázdný.

**Stav:** PASS

**Poznámky:** Hraniční scénář ověřující práci s prázdným seznamem.

---

## TM-ZU-002 Zobrazení jednoho úkolu

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-002

**Popis:** Ověření správného výpisu jednoho uloženého úkolu.

**Vstupní podmínky:**
- Seznam obsahuje jeden úkol.

**Testovací data:** Nákup – Koupit mléko

**Kroky testu:**
1. Přidejte jeden úkol.
2. Zvolte možnost 2.

**Očekávaný výsledek:** Program zobrazí jeden úkol s pořadovým číslem 1.

**Skutečný výsledek:** Program zobrazil: 1. Nákup – Koupit mléko

**Stav:** PASS

**Poznámky:** Ověření výpisu jedné položky.

---

## TM-ZU-003 Zobrazení více úkolů

**Priorita:** High

**Typ testu:** Pozitivní

**Požadavek:** REQ-002

**Popis:** Ověření správného výpisu více uložených úkolů.

**Vstupní podmínky:** Seznam obsahuje minimálně tři úkoly.

**Testovací data:** 3 uložené úkoly.

**Kroky testu:**
1. Přidejte alespoň 3 úkoly.
2. Zobrazte seznam.

**Očekávaný výsledek:** Program zobrazí všechny úkoly ve správném pořadí.

**Skutečný výsledek:** Všechny úkoly byly zobrazeny ve správném pořadí.

**Stav:** PASS

**Poznámky:** Ověření enumerate(). Ověření správného číslování úkolů při jejich zobrazení.

---

## TM-ZU-004 Zachování pořadí úkolů

**Priorita:** Medium

**Typ testu:** Pozitivní

**Požadavek:** REQ-002

**Popis:** Ověření zachování pořadí vložených úkolů.

**Vstupní podmínky:** V seznamu jsou minimálně tři úkoly.

**Kroky testu:**
1. Přidejte tři úkoly.
2. Zobrazte seznam.

**Očekávaný výsledek:** Pořadí výpisu odpovídá pořadí vložení.

**Skutečný výsledek:** Pořadí výpisu odpovídalo pořadí vložení.

**Stav:** PASS

**Poznámky:** Ověření integrity dat.

---

## TM-ZU-005 Zobrazení více než 10 úkolů

**Priorita:** Medium

**Typ testu:** Hraniční hodnota

**Požadavek:** REQ-002

**Popis:** Ověření správného číslování při větším počtu úkolů.

**Vstupní podmínky:** V seznamu je 11 úkolů.

**Kroky testu:**
1. Přidejte 11 úkolů.
2. Zobrazte seznam.

**Očekávaný výsledek:** Všechny úkoly budou správně očíslovány.

**Skutečný výsledek:** Program správně zobrazil položky 10 a 11.

**Stav:** PASS

**Poznámky:** Hraniční test většího počtu položek.

# Testovací případy – Funkce `odstranit_ukol()`

## TM-OU-001 Odstranění existujícího úkolu
**Priorita:** High
**Typ testu:** Pozitivní
**Požadavek:** REQ-003
**Popis:** Ověření úspěšného odstranění existujícího úkolu.
**Vstupní podmínky:** Program je spuštěn a existuje alespoň jeden úkol.
**Testovací data:** 1
**Kroky testu:** Spusťte odstranění úkolu a zadejte číslo existujícího úkolu.
**Očekávaný výsledek:** Vybraný úkol bude odstraněn.
**Skutečný výsledek:** Program zobrazil zprávu o odstranění úkolu.
**Stav:** PASS
**Poznámky:** Základní pozitivní scénář.

## TM-OU-002 Odstranění prvního úkolu
**Priorita:** High
**Typ testu:** Hraniční případ
**Požadavek:** REQ-003
**Popis:** Ověření odstranění první položky seznamu.
**Stav:** PASS

## TM-OU-003 Odstranění posledního úkolu
**Priorita:** High
**Typ testu:** Hraniční případ
**Požadavek:** REQ-003
**Popis:** Ověření odstranění poslední položky seznamu.
**Stav:** PASS

## TM-OU-004 Odstranění jediného úkolu
**Priorita:** High
**Typ testu:** Hraniční případ
**Požadavek:** REQ-003
**Popis:** Ověření odstranění jediného úkolu.
**Stav:** PASS

## TM-OU-005 Zadání čísla mimo rozsah
**Priorita:** Medium
**Typ testu:** Negativní
**Požadavek:** REQ-003
**Skutečný výsledek:** Takový úkol neexistuje.
**Stav:** PASS

## TM-OU-006 Zadání hodnoty 0
**Priorita:** Medium
**Typ testu:** Hraniční hodnota
**Požadavek:** REQ-003
**Skutečný výsledek:** Takový úkol neexistuje.
**Stav:** PASS

## TM-OU-007 Zadání záporného čísla
**Priorita:** Medium
**Typ testu:** Negativní
**Požadavek:** REQ-003
**Skutečný výsledek:** Takový úkol neexistuje.
**Stav:** PASS

## TM-OU-008 Zadání textu místo čísla
**Priorita:** High
**Typ testu:** Negativní
**Požadavek:** REQ-003
**Skutečný výsledek:** Musíte zadat platné číslo úkolu.
**Stav:** PASS

## TM-OU-009 Prázdný seznam úkolů
**Priorita:** High
**Typ testu:** Hraniční případ
**Požadavek:** REQ-003
**Skutečný výsledek:** Není žádný úkol k odstranění.
**Stav:** PASS

## TM-OU-010 Zadání desetinného čísla
**Priorita:** Medium
**Typ testu:** Negativní
**Požadavek:** REQ-003
**Skutečný výsledek:** Musíte zadat platné číslo úkolu.
**Stav:** PASS

## TM-OU-011 Prázdný vstup při odstraňování
**Priorita:** Medium
**Typ testu:** Hraniční případ
**Požadavek:** REQ-003
**Skutečný výsledek:** Musíte zadat platné číslo úkolu.
**Stav:** PASS

