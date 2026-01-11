from Person import Person

class Model:
    def __init__(self):
        self.people: list[Person] = []

    def add(self, name: str, address: str, phone: str) -> None:
        person = Person(name=name, address=address, phone=phone)
        self.people.append(person)

    def get_all(self) -> list[Person]:
        return self.people
