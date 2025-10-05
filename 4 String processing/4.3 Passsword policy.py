import re


def password_policy_check(username: str, password: str) -> bool:
    """
    Kontroluje, zda heslo splňuje požadavky na silné heslo.

    Parametry:
        username (str): Uživatelské jméno.
        password (str): Heslo, které chceme ověřit.

    Návratová hodnota:
        bool: True pokud heslo vyhovuje všem pravidlům, False jinak.
    """

    # 1) Heslo minimálně 10 znaků
    if len(password) < 10:
        print("Heslo musí mít minimálně 10 znaků.")
        return False

    # 2) Heslo musí obsahovat alespoň jedno číslo
    if not re.search(r'\d', password):
        print("Heslo musí obsahovat alespoň jedno číslo.")
        return False

    # 3) Heslo musí obsahovat malé i velké písmeno
    if not re.search(r'[a-z]', password):
        print("Heslo musí obsahovat alespoň jedno malé písmeno.")
        return False
    if not re.search(r'[A-Z]', password):
        print("Heslo musí obsahovat alespoň jedno velké písmeno.")
        return False

    # 4) Heslo musí obsahovat alespoň jeden nečíselný a nepísmený znak (special char)
    # tj. něco co není písmeno ani číslo - použijeme negaci \w (které odpovídá [a-zA-Z0-9_])
    if not re.search(r'[^a-zA-Z0-9]', password):
        print("Heslo musí obsahovat alespoň jeden speciální znak (ne číslo ani písmeno).")
        return False

    # 5) Heslo nesmí obsahovat username
    if username.lower() in password.lower():
        print("Heslo nesmí obsahovat uživatelské jméno.")
        return False

    # 6) Heslo nesmí obsahovat žádný podřetězec username delší než 3 znaky
    # Provedeme kontrolu všech podřetězců username délky >= 4
    username_lower = username.lower()
    password_lower = password.lower()

    for i in range(len(username_lower) - 3):
        substring = username_lower[i:i + 4]  # podřetězec délky 4
        if substring in password_lower:
            print(f"Heslo nesmí obsahovat podřetězec uživatelského jména delší než 3 znaky: '{substring}'")
            return False

    # Pokud jsme došli až sem, heslo vyhovuje všem pravidlům
    return True


# Testovací příklady

username = "Pepa123"
password_good = "Aa1!2345678"
password_bad1 = "Aa12345678"  # chybí speciální znak
password_bad2 = "aaaaAA11!!"  # obsahuje username "Pepa"?
password_bad3 = "Aa1!Pepa1234"  # obsahuje username

print(password_policy_check(username, password_good))  # True
print(password_policy_check(username, password_bad1))  # False
print(password_policy_check(username, password_bad3))  # False
