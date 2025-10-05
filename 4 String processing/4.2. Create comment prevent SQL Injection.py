def vytvor_sql_vlozeni_bezpecne(nickname: str, text: str) -> str:
    """
    Vytvoří SQL příkaz pro vložení příspěvku do tabulky PRISPEVEK.
    Escapuje apostrofy tak, aby nebylo možné provést SQL Injection.

    Args:
        nickname (str): Autor příspěvku.
        text (str): Text příspěvku.

    Returns:
        str: Bezpečný SQL příkaz jako textový řetězec.
    """

    # Escapování apostrofů (') nahrazením za dva apostrofy ('')
    def escape_sql(value: str) -> str:
        return value.replace("'", "''")

    nickname_esc = escape_sql(nickname)
    text_esc = escape_sql(text)

    sql = f"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ('{nickname_esc}', '{text_esc}');"
    return sql


# Testování proti pokusu o SQL Injection
nickname = r"""\", ""); DROP TABLE PRISPEVEK; --"""
text = "Zdravím!"

print(vytvor_sql_vlozeni_bezpecne(nickname, text))
