class InsuredPerson:
    # třída obsahuje konstruktor a textovou reprezentaci pro ukládání a výpis pojištěnců
    _name = str
    _surname = str
    _phone_number = int
    _age = int

    def __init__(self, _name="", _surname="", _phone_number="", _age=0):
        self._name = _name
        self._surname = _surname
        self._phone_number = _phone_number
        self._age = _age

    def __str__(self):
    # textová reprezentace pojištěnců
        self._phone_number = str(self._phone_number)
        self._age = str(self._age)
        return f"{self._name.ljust(20)}{self._surname.ljust(25)}{self._phone_number.ljust(20)}{self._age.ljust(7)}"


