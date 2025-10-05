import re

# Pomocné funkce
def escape_sql(value: str) -> str:
    """
    Escapuje jednoduché uvozovky pro bezpečné vložení do SQL literálu.
    MySQL/SQL standard: ' -> ''
    """
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
    """Základní kontrola e-mailu (není plně RFC-kompatibilní, ale postačí pro validaci vstupu)."""
    if not isinstance(email, str):
        return False
    # velmi jednoduchý regex: něco@něco.domena
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))


# Opravené funkce
def build_sql_update_user_jmeno_by_id(name, id):
    """
    Bezpečné vytvoření UPDATE příkazu. Escapuje jméno a validuje id jako integer.
    """
    id_int = int(id)  # pokud není možné převést, vyhodí ValueError
    name_esc = escape_sql(str(name))
    # používáme jednoduché backticky kolem identifikátorů pro MySQL
    return f"UPDATE `uzivatel` SET `jmeno` = '{name_esc}' WHERE `id` = {id_int};"

def build_sql_delete_by_table_and_id(table_name, id):
    """
    Bezpečné vytvoření DELETE příkazu. Validuje název tabulky a id.
    """
    table = validate_table_name(table_name)
    id_int = int(id)
    return f"DELETE FROM `{table}` WHERE `id` = {id_int};"

def build_sql_insert_users(users):
    """
    Bezpečné sestavení INSERT příkazů pro seznam uživatelů.
    Každý user musí být dict s klíči 'email' a 'jmeno'.
    E-mail je ověřen základním regexem.
    """
    if not isinstance(users, (list, tuple)):
        raise ValueError("users musí být seznam/datum")

    sql_parts = []
    for user in users:
        if not isinstance(user, dict):
            raise ValueError("Každý uživatel musí být slovník s klíči 'email' a 'jmeno'")
        if 'email' not in user or 'jmeno' not in user:
            raise ValueError("Každý uživatel musí obsahovat 'email' a 'jmeno'")

        email = str(user['email'])
        jmeno = str(user['jmeno'])

        if not validate_email(email):
            raise ValueError(f"Neplatný email: {email}")

        email_esc = escape_sql(email)
        jmeno_esc = escape_sql(jmeno)

        sql_parts.append(f"INSERT INTO `uzivatel` (`email`, `jmeno`) VALUES ('{email_esc}', '{jmeno_esc}');")

    return "".join(sql_parts)


# Testovací výpisy
print(build_sql_update_user_jmeno_by_id("martin", 38))
print(build_sql_delete_by_table_and_id("uzivatel", 42))
print(build_sql_insert_users([
    {"jmeno":"ondra","email":"ondra@seznam.cz"},
    {"jmeno":"petr","email":"petr@seznam.cz"}
]))

''' ocekavame

UPDATE `uzivatel` SET `jmeno` = 'martin' WHERE `id` = 38;
DELETE FROM `uzivatel` WHERE `id` = 42;
INSERT INTO `uzivatel` (`email`, `jmeno`) VALUES ('ondra@seznam.cz', 'ondra');INSERT INTO `uzivatel` (`email`, `jmeno`) VALUES ('petr@seznam.cz', 'petr');

'''