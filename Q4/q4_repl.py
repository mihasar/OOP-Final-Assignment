def is_multiple(n1: int, n2: int) -> bool:
    """Return True if one number is a multiple of the other."""
    # Keep it simple (avoid division by zero edge cases)
    if n1 == 0 or n2 == 0:
        return False
    return (n1 % n2 == 0) or (n2 % n1 == 0)


def main() -> None:
    print("Section 4 - REPL (enter -1 to exit)")

    while True:
        try:
            x_raw = input("Enter first number (-1 to exit): ").strip()
            if x_raw == "-1":
                break
            x = int(x_raw)

            y_raw = input("Enter second number (-1 to exit): ").strip()
            if y_raw == "-1":
                break
            y = int(y_raw)

            if is_multiple(x, y):
                print("Yes, one is a multiple of the other.\n")
            else:
                print("No, one is not a multiple of the other.\n")

        except ValueError:
            print("Invalid input. Please enter integers only.\n")

    print("Bye!")


if __name__ == "__main__":
    main()
