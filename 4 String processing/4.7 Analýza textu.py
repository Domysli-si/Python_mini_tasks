import re

def count_words(text: str) -> int:
    # Definice seznamů slov (všechna malá písmena, porovnáváme case-insensitive)
    predlozky = {"in", "from", "to", "on", "out", "at"}
    spojky = {"but", "because", "although", "so", "and"}
    zajmena = {"you", "i", "me", "he", "him", "himself", "ourselves", "mine", "hers"}
    cleny = {"a", "an", "the"}
    citoslovce = {"yipe", "yum", "yak", "ugh", "huh"}

    # Funkce pro rozpoznání řadových číslovek (např. 1st, 2nd, 3rd, 4th, 10th)
    def is_ordinal(word):
        return bool(re.fullmatch(r'\d+(st|nd|rd|th)', word.lower()))

    # Funkce na rozpoznání číslic (čísla samotná nepočítáme)
    def is_number(word):
        return bool(re.fullmatch(r'\d+', word))

    # Funkce na rozpoznání složenin, které se počítají jako 2 slova (It’s, I’ll, mustn’t, haven’t)
    # Vyjímka: cannot a can't jsou 1 slovo
    def count_contraction(word):
        word_lower = word.lower()
        # cannot a can't jsou 1 slovo
        if word_lower in {"cannot", "can't"}:
            return 1
        # ostatní s apostrofem a ukončené na -t, -ll, -ve, -d, -re apod. = 2 slova
        if re.fullmatch(r"[a-zA-Z]+('[a-z]{1,3})", word_lower):
            return 2
        return 1

    # Tokenizace textu: rozdělíme na slova + čárky, tečky atd. odstraníme
    # Pro správné rozpoznání adres a dat budeme potřebovat pokročilejší přístup

    # Nejprve nahradíme čárky za čárky + mezera (pro rozdělení)
    text = text.replace(",", ", ")

    # rozdělíme text podle mezer
    tokens = text.split()

    word_count = 0
    skip_indices = set()  # indexy slov, které už jsme zahrnuli jako část "jednoho slova" (adresy, datum)

    i = 0
    while i < len(tokens):
        if i in skip_indices:
            i += 1
            continue

        token = tokens[i]
        token_clean = token.lower().strip(".,!?")

        # 7) Datum rozepsané (např. September 11th 2014 = 3 tokeny)
        # Zkusíme detekovat vzor: <měsíc> <číslo + pořadová přípona> <rok>
        # Pro jednoduchost: měsíc začíná velkým písmenem, číslo řadové, rok 4 číslice
        if i + 2 < len(tokens):
            month = tokens[i]
            day = tokens[i+1]
            year = tokens[i+2]
            if (month[0].isupper() and
                is_ordinal(day.lower().strip(".,!?")) and
                re.fullmatch(r'\d{4}', year)):
                word_count += 1
                skip_indices.update({i, i+1, i+2})
                i += 3
                continue

        # 8) Adresa (např. "25 Londýnská, Praha" nebo "10 Broadway, New York City")
        # Přiblížíme detekci: číslo + slovo + (volitelně další slova oddělené čárkou)
        # Zkusíme vzít dva nebo více tokenů pokud první je číslo, druhý slovo a/nebo více slov
        # Není to úplně dokonalé, ale pro ilustraci:

        if i + 1 < len(tokens):
            first = tokens[i]
            second = tokens[i+1]
            # číslo + slovo
            if is_number(first.strip(".,!?")) and second[0].isalpha():
                # budeme hledat kolik tokenů patří k adrese, až do dalšího tokenu, který není slovo (nepočítáme čárky, tečky)
                j = i + 2
                while j < len(tokens) and tokens[j][0].isalpha():
                    j += 1
                # všechny tokeny od i do j-1 jsou adresa
                word_count += 1
                skip_indices.update(range(i, j))
                i = j
                continue

        # 9) Číslovky psány jako číslice (2, 2013) nepočítáme
        if is_number(token_clean):
            i += 1
            continue

        # 10) Složeniny
        # počítáme podle funkce count_contraction
        contraction_count = count_contraction(token_clean)
        if contraction_count == 2:
            word_count += 2
            i += 1
            continue

        # 1-5) Slova z daných kategorií počítáme jako 1 slovo
        if (token_clean in predlozky or
            token_clean in spojky or
            token_clean in zajmena or
            token_clean in cleny or
            token_clean in citoslovce):
            word_count += 1
            i += 1
            continue

        # Jinak slovo počítáme jako 1 slovo
        word_count += 1
        i += 1

    return word_count


# Testy
text1 = "I can’t believe it’s September 11th 2014, but I’ll try."
text2 = "25 Londýnská, Praha is my address."
text3 = "You and I are going to the park."
text4 = "2 2013 777 should not be counted."
text5 = "He said yipe and yum, but I’m not sure."

print(count_words(text1))  # Očekáváme: (I=1, can’t=1, believe=1, it’s=2, September 11th 2014=1, but=1, I’ll=2, try=1) = 10
print(count_words(text2))  # Očekáváme: 1 (adresa)
print(count_words(text3))  # Očekáváme: you=1, and=1, i=1, going=1, to=1, the=1, park=1 => 7
print(count_words(text4))  # Očekáváme: 0, 0, 0, ostatní slova bychom nepočítali
print(count_words(text5))  # yipe=1, yum=1, but=1, I’m=2, not=1, sure=1 => 7
