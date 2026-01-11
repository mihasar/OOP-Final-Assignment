from view import View
from model import Model

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self) -> None:
        while True:
            choice = self.view.show_menu()
            if choice == "1":
                name, address, phone = self.view.read_person_fields()
                self.model.add(name, address, phone)
                self.view.show_message("Person saved.")
            elif choice == "2":
                self.view.show_people(self.model.get_all())
            elif choice == "0":
                self.view.show_message("Bye!")
                break
            else:
                self.view.show_message("Invalid choice, try again.")
