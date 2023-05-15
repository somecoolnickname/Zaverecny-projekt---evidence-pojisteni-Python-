from insured_person import InsuredPerson
evidence = []

class Evidence:
# třída obsahuje metody pro práci s evidencí pojištěnců
    def __init__(self):
        self.evidence = evidence

    def display_possible_actions(self):
    # metoda zobrazí možné akce v rámci evidence pojištěnců
        print("\nVyberte si akci:"
              "\n1 - Přidat nového pojištěného"
              "\n2 - Vypsat všechny pojištěné"
              "\n3 - Vyhledat pojištěného"
              "\n4 - Konec")

    def display_search_header(self):
    # metoda u výpisu všech pojištěnců a u vyhledávání zobrazuje hlavičku tabulky (estetická záležitost)
        str_name = "JMÉNO"
        str_surname = "PŘÍJMENÍ"
        str_phone_number = "TELEFONNÍ ČÍSLO"
        str_age = "VĚK"
        str_underline = ""
        print(f"\n{str_name.ljust(20)}{str_surname.ljust(25)}{str_phone_number.ljust(20)}{str_age.ljust(7)}")
        print(str_underline.ljust(72, "-"))

    def add_new_person_to_evidence(self, name, surname, phone_number, age):
    # metoda přijímá data z mainu a vytváří instanci osoby, kterou následně přidává do kolekce evidence
        new_person = InsuredPerson(name, surname, phone_number, age)
        # instance objektu InsuredPerson (osoba, která se má nově přidat do evidence)
        person_exists = 0
        for person in self.evidence:
            if (
                (person._name == new_person._name) and
                (person._surname == new_person._surname) and
                (person._phone_number == new_person._phone_number) and
                (person._age == new_person._age)):
                    person_exists += 1
        if person_exists > 0:
            print("Osoba již je v evidenci.")
        else:
            self.evidence.append(new_person)
            print("\nData byla uložena.")

    def display_all_people_in_evidence(self):
        # metoda vypíše kompletní seznam pojištěnců, řazení je chronologické
        if len(evidence) > 0:
            self.display_search_header()
            for person in self.evidence:
                print(person)
        else:
            print("\nEvidence je prázdná.")

    def find_person_in_evidence(self, search_by, search_parameter):
        # metoda umožní vyhledat uživateli pojištěného podle parametru zadaného v mainu.
        # Pokud osobu nenalezne, vrátí zprávu. Pokud je evidence prázdná, informuje uživatele.
        counter = 0

        if len(self.evidence) != 0:
            self.display_search_header()
            for person in self.evidence:
                if (
                        (search_by == "1" and search_parameter.lower().strip() in person._name.lower()) or
                        (search_by == "2" and search_parameter.lower().strip() in person._surname.lower()) or
                        (search_by == "3" and search_parameter.strip() in person._phone_number) or
                        (search_by == "4" and search_parameter.strip() in person._age)):
                    counter += 1
                    print(person)
        else:
            print("\nEvidence je prázdná.")

        if counter == 0 and search_by != "5":
            print("\nŽádný záznam neexistuje")

