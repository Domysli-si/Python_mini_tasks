import re

def create_censored_insert_sql(nickname: str, text: str) -> str:
    # Slovník variant jmen - klíč: oficiální jméno, hodnota: seznam variant k cenzuře
    censored_names = {
        "Ondřej Mandík": ["Ondřej Mandík", "Ondra Mandík", "Mandík"],
        "Alena Reichlová": ["Alena Reichlová", "Reichlová", "Alena"],
        "Jára Cimrman": ["Jaroslav Cimrman", "Jára Cimrman", "Cimrman", "Jaroslav", "Jára"]
    }

    # Funkce pro cenzuru textu
    def censor_text(text):
        # Pro každý jmenovaný výraz v seznamu provede nahrazení
        for full_name, variants in censored_names.items():
            for name_variant in variants:
                # regex pro whole word match, case insensitive
                # \b zajistí hranice slova, aby nezasahoval do jiných slov
                pattern = r'\b' + re.escape(name_variant) + r'\b'
                text = re.sub(pattern, '[AUTOMATICKY CENZUROVÁNO]', text, flags=re.IGNORECASE)
        return text

    # Nejprve cenzurujeme text
    censored_text = censor_text(text)

    # Funkce pro bezpečné vložení stringu do SQL (escapování apostrofů)
    def escape_sql_string(s):
        return s.replace("'", "''")

    # Escapujeme nickname i censored_text
    nickname_escaped = escape_sql_string(nickname)
    text_escaped = escape_sql_string(censored_text)

    # Sestavíme SQL příkaz
    sql = f"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ('{nickname_escaped}', '{text_escaped}');"
    return sql


# Příklad testů
nick = "Eva"
text1 = "Dobrý den všem! Ondřej Mandík je tu."
text2 = "Alena Reichlová a Jára Cimrman jsou legendy."
text3 = "Ondra a Jára jsou přátelé."
text4 = "Jaroslav Cimrman napsal mnoho her."

print(create_censored_insert_sql(nick, text1))
print(create_censored_insert_sql(nick, text2))
print(create_censored_insert_sql(nick, text3))
print(create_censored_insert_sql(nick, text4))
