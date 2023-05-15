from evidence import Evidence
from validations import Validations

print("_____________________\nEvidence pojištěných\n_____________________")
run = True
evidence = Evidence()

while run:

    evidence.display_possible_actions() # zobrazí dostupné akce v rámci evidence pojištěnců
    action = input().strip()
    match action:
        case "1":
            # zadání atributů pro novou osobu + volání validace pro jméno, příjmení a věk

            while True:
                new_name = input("\nZadejte jméno:\n").strip()
                if Validations.contains_letters_only(new_name, "jméno"):
                    break

            while True:
                new_surname = input("\nZadejte příjmení:\n").strip()
                if Validations.contains_letters_only(new_surname, "příjmení"):
                    break

            new_phone_number = input("\nZadejte telefonní číslo:\n").strip()

            while True:
                new_age = input("\nZadejte věk:\n").strip()
                if Validations.contains_numbers_only(new_age, "věk"):
                    break

            # přidání nové osoby do evidence
            evidence.add_new_person_to_evidence(new_name, new_surname, new_phone_number, new_age)

        case "2":
            evidence.display_all_people_in_evidence()

        case "3":
            search = True
            # uživatel si zvolí 1 parametr pro vyhledávání, vyhledávat může opakovaně, parametry lze střídat
            while search:
                print("\nPodle jakých parametrů chcete vyhledávat?")
                print(
                    "1 - Jméno\n"
                    "2 - Příjmení\n"
                    "3 - Telefonní číslo\n"
                    "4 - Věk\n"
                    "5 - Ukončit")
                search_by = input().strip()

                if not Validations.search_by_is_valid(search_by):
                    continue

                text = "\nZadejte"
                if search_by == "1":
                    search_parameter = input(f"{text} jméno: \n")
                elif search_by == "2":
                    search_parameter = input(f"{text} příjmení: \n")
                elif search_by == "3":
                    search_parameter = input(f"{text} telefonní číslo:\n")
                elif search_by == "4":
                    search_parameter = input(f"{text} věk:\n")
                elif search_by == "5":
                    break

                evidence.find_person_in_evidence(search_by, search_parameter)

        case "4":
            print("\nDěkujeme za použití programu.")
            break
        case _ :
            action = print("\nVyberte možnost ve tvaru 1, 2, 3, nebo 4.\n")

    input("\nPro pokračování stiskněte Enter...")