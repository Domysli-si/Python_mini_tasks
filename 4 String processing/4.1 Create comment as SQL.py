def vytvor_sql_vlozeni(nickname: str, text: str) -> str:
    """
    Vytvoří SQL příkaz pro vložení příspěvku do tabulky PRISPEVEK.

    Args:
        nickname (str): Autor příspěvku.
        text (str): Text příspěvku.

    Returns:
        str: SQL příkaz jako textový řetězec.
    """
    # Ošetření apostrofů v textu (nahradíme ' za '')
    nickname_esc = nickname.replace("'", "''")
    text_esc = text.replace("'", "''")

    sql = f"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ('{nickname_esc}', '{text_esc}');"
    return sql


# Testovací příklad
nickname = "Eva"
text = "Dobrý den všem!"
print(vytvor_sql_vlozeni(nickname, text))
