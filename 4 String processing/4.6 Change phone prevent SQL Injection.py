import re

def uprav_telefon_bezpecne(username: str, phone: str) -> str:
    """
    Vytvoří bezpečný SQL příkaz pro aktualizaci telefonního čísla uživatele v tabulce USER.
    Ošetřuje vstupy proti SQL Injection.

    Args:
        username (str): Uživatelské jméno.
        phone (str): Nové telefonní číslo (9 znaků).

    Returns:
        str: SQL příkaz jako textový řetězec.
    """

    def escape_sql(value: str) -> str:
        """Escapuje apostrofy pro bezpečnost."""
        return value.replace("'", "''")

    # Validace telefonu: pouze číslice, délka přesně 9 (jak je ve schématu)
    if not re.fullmatch(r'\d{9}', phone):
        raise ValueError("Telefon musí obsahovat přesně 9 číslic.")

    # Validace username: povolíme jen alfanumerické znaky + podtržítko (pro jednoduchost)
    if not re.fullmatch(r'\w{1,100}', username):
        raise ValueError("Uživatelské jméno obsahuje nepovolené znaky nebo je příliš dlouhé.")

    username_esc = escape_sql(username)
    phone_esc = escape_sql(phone)

    sql = f"UPDATE USER SET PHONE = '{phone_esc}' WHERE USERNAME = '{username_esc}';"
    return sql


# Testovací příklad
username = "Pepa_123"
phone = "123456789"

print(uprav_telefon_bezpecne(username, phone))
