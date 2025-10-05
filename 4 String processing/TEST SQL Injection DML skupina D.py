import re

# Pomocné funkce
def escape_sql(value: str) -> str:
    """Escapuje jednoduché uvozovky pro bezpečné vložení do SQL literálu."""
    if not isinstance(value, str):
        raise ValueError("Očekáván řetězec")
    return value.replace("'", "''")

def validate_table_name(name: str) -> str:
    """
    Validace názvu tabulky - pouze A-Z, a-z, 0-9 a podtržítko.
    Musí začínat písmenem nebo podtržítkem.
    """
    if not isinstance(name, str):
        raise ValueError("Název tabulky musí být řetězec")
    if not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', name):
        raise ValueError("Neplatný název tabulky")
    return name

def validate_email(email: str) -> bool:
    """Základní kontrola e-mailu (neplně RFC, dostačuje pro validaci vstupu)."""
    if not isinstance(email, str):
        return False
    # jednoduchý regex pro "něco@něco.domena"
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))

# Opravené funkce
def build_sql_update_email_by_id(email, id):
    """
    Bezpečné vytvoření UPDATE příkazu pro změnu emailu podle id.
    """
    # validace a převod id na int
    id_int = int(id)
    # validace emailu
    email_str = str(email)
    if not validate_email(email_str):
        raise ValueError(f"Neplatný email: {email_str}")
    email_esc = escape_sql(email_str)
    return f"UPDATE `uzivatel` SET `email` = '{email_esc}' WHERE `id` = {id_int};"

def build_sql_delete_all_by_table(table_name):
    """
    Bezpečné vytvoření DELETE FROM <table> WHERE 1=1 (vymaže vše z tabulky).
    Název tabulky musí projít validací.
    """
    table = validate_table_name(table_name)
    return f"DELETE FROM `{table}` WHERE 1=1;"

def build_sql_update_users(users):
    """
    Bezpečné sestavení UPDATE příkazů pro seznam uživatelů.
    Každý uživatel: dict s klíči 'id', 'jmeno', 'email'.
    """
    if not isinstance(users, (list, tuple)):
        raise ValueError("users musí být seznam nebo n-tice")

    sql_parts = []
    for user in users:
        if not isinstance(user, dict):
            raise ValueError("Každý uživatel musí být slovník")
        if 'id' not in user or 'email' not in user or 'jmeno' not in user:
            raise ValueError("Každý uživatel musí obsahovat 'id', 'email' a 'jmeno'")

        # validace a převody
        id_int = int(user['id'])
        email_str = str(user['email'])
        jmeno_str = str(user['jmeno'])

        if not validate_email(email_str):
            raise ValueError(f"Neplatný email: {email_str}")

        email_esc = escape_sql(email_str)
        jmeno_esc = escape_sql(jmeno_str)

        sql_parts.append(
            f"UPDATE `uzivatel` SET `email` = '{email_esc}', `jmeno` = '{jmeno_esc}' WHERE `id` = {id_int};"
        )

    return "".join(sql_parts)

# Testovací výpisy
print(build_sql_update_email_by_id("ondra@seznam.cz", 23))
print(build_sql_delete_all_by_table("uzivatel"))
print(build_sql_update_users([
    {"id":11,"jmeno":"ondra","email":"ondra@seznam.cz"},
    {"id":12,"jmeno":"petr","email":"petr@seznam.cz"}
]))


"""
UPDATE `uzivatel` SET `email` = 'ondra@seznam.cz' WHERE `id` = 23;
DELETE FROM `uzivatel` WHERE 1=1;
UPDATE `uzivatel` SET `email` = 'ondra@seznam.cz', `jmeno` = 'ondra' WHERE `id` = 11;UPDATE `uzivatel` SET `email` = 'petr@seznam.cz', `jmeno` = 'petr' WHERE `id` = 12;

"""
