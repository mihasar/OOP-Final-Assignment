from typing import Iterable
from Person import Person

class View:
    def show_menu(self) -> str:
        print("\n--- MENU ---")
        print("1) Add person")
        print("2) Show all people")
        print("0) Exit")
        return input("Choose: ").strip()

    def read_person_fields(self) -> tuple[str, str, str]:
        while True:
            name = input("Name: ").strip()
            if name:
                break
            print("Name cannot be empty.")
        
        address = input("Address: ").strip()
        
        while True:
            phone = input("Phone: ").strip()
            if phone:
                break
            print("Phone cannot be empty.")
            
        return name, address, phone

    def show_people(self, people: Iterable[Person]) -> None:
        people = list(people)
        if not people:
            print("No people saved yet.")
            return
        print("\n--- PEOPLE LIST ---")
        for i, p in enumerate(people, start=1):
            print(f"{i}. {p.name} | {p.address} | {p.phone}")

    def show_message(self, msg: str) -> None:
        print(msg)
