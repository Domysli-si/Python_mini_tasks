def uprav_telefon(username: str, phone: str) -> str:
    """
    Vytvoří SQL příkaz pro aktualizaci telefonního čísla uživatele v tabulce USER.

    Args:
        username (str): Uživatelské jméno.
        phone (str): Nové telefonní číslo (9 znaků).

    Returns:
        str: SQL příkaz jako textový řetězec.
    """

    # Escapování apostrofů pro bezpečnost (nahradí ' za '')
    def escape_sql(value: str) -> str:
        return value.replace("'", "''")

    username_esc = escape_sql(username)
    phone_esc = escape_sql(phone)

    sql = f"UPDATE USER SET PHONE = '{phone_esc}' WHERE USERNAME = '{username_esc}';"
    return sql


# Testovací příklad
username = "Pepa"
phone = "123456789"

print(uprav_telefon(username, phone))
