import xml.etree.ElementTree as ET

def person_search(xml_string):
    """
    Na vstupu má XML string z ARES a vypíše všechny fyzické osoby ve firmě.
    """
    try:
        # Načteme XML
        root = ET.fromstring(xml_string)

        # Namespace v XML ARES (nutné pro správné hledání elementů)
        ns = {'are': 'http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_answer/v_1.0.3'}

        # Najdeme všechny osoby fyzické - tag PF (Person Fyzická)
        persons = root.findall('.//are:PF', namespaces=ns)

        if not persons:
            print("Ve firmě nebyly nalezeny žádné fyzické osoby.")
            return

        print("Fyzické osoby uvedené ve firmě:")

        for pf in persons:
            # Zkusíme získat křestní jméno a příjmení
            first_name = pf.find('are:OF', namespaces=ns)  # OF = osobní jméno
            last_name = pf.find('are:NN', namespaces=ns)   # NN = příjmení

            # Některé uzly mohou být None, tak ošetříme
            first_name_text = first_name.text if first_name is not None else ""
            last_name_text = last_name.text if last_name is not None else ""

            full_name = f"{first_name_text} {last_name_text}".strip()
            print(full_name)

    except ET.ParseError as e:
        print("Chyba při parsování XML:", e)
