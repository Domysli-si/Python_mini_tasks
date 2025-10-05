def uprav_email(username: str, email: str) -> str:
    """
    Vytvoří SQL příkaz pro aktualizaci emailu uživatele v tabulce ACCOUNT.

    Args:
        username (str): Uživatelské jméno.
        email (str): Nový email uživatele.

    Returns:
        str: SQL příkaz jako textový řetězec.
    """

    # Funkce pro escapování apostrofů (') -> dvojité apostrofy ('')
    def escape_sql(value: str) -> str:
        return value.replace("'", "''")

    username_esc = escape_sql(username)
    email_esc = escape_sql(email)

    sql = f"UPDATE ACCOUNT SET EMAIL = '{email_esc}' WHERE USERNAME = '{username_esc}';"
    return sql

# Testovací příklad
username = "Pepa"
email = "pepa@example.com"

print(uprav_email(username, email))
