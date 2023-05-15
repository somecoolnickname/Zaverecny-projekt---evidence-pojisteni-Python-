class Validations:

    @staticmethod
    def contains_numbers_only(parameter, parameter_name):
    # statická metoda ověřuje, jestli ověřovaný parametr obsahuje pouze číslice
        if parameter.isnumeric():
            return True
        else:
            print("Zadejte {0} pouze pomocí číslic.".format(parameter_name))
            return False

    @staticmethod
    def contains_letters_only(parameter, parameter_name):
    # statická metoda ověřuje, jestli se ověřovaný parametr skládá pouze z písmen
        if parameter.isalpha():
            return True
        else:
            print("Zadejte {0} pouze pomocí písmen.".format(parameter_name))
            return False

    @staticmethod
    def search_by_is_valid(parameter):
    # statická metoda ověřuje, že u volby parametru pro hledání bylo zadáno číslo od 1 do 5
        if parameter.isnumeric() and ((int(parameter) > 0) and (int(parameter) < 6)):
            return True
        else:
            print("\nZadejte volbu pomocí číslic 1-5.")
            return False
