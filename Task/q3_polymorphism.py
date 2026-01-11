from abc import ABC, abstractmethod

# --- חלק א': Duck Typing ---
class Dog:
    def speak(self) -> str:
        return "Woof!"

class Cat:
    def speak(self) -> str:
        return "Meow!"

def part_a() -> None:
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())

# --- חלק ג': מחלקה אבסטרקטית + ירושה ---
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        raise NotImplementedError

class Dog2(Animal):
    def speak(self) -> str:
        return "Woof!"
class Cat2(Animal):
    def speak(self) -> str:
        return "Meow!"

def part_c() -> None:
    animals = [Dog2(), Cat2(), "not an animal"]
    for animal in animals:
        if isinstance(animal, Animal):
            print(animal.speak())
        else:
            print("Skipped non-animal:", animal)

if __name__ == "__main__":
    print("Part A output:")
    part_a()
    print("\nPart C output:")
    part_c()
