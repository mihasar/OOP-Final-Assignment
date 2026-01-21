from __future__ import annotations


class Security:
    """Base class: Security (נייר ערך)"""

    def __init__(self, symbol: str, name: str, current_price: float):
        if not symbol.strip():
            raise ValueError("symbol cannot be empty")
        if not name.strip():
            raise ValueError("name cannot be empty")
        if current_price < 0:
            raise ValueError("current_price cannot be negative")

        # >= 3 attributes
        self.symbol = symbol
        self.name = name
        self.current_price = current_price

    # >= 1 function
    def base_info(self) -> str:
        return f"[{self.symbol}] {self.name} | Price: {self.current_price:.2f}"


class Stock(Security):
    """Stock (מניה)"""

    def __init__(self, symbol: str, name: str, current_price: float, dividend_yield: float):
        super().__init__(symbol, name, current_price)
        if dividend_yield < 0:
            raise ValueError("dividend_yield cannot be negative")
        # +1 attribute
        self.dividend_yield = dividend_yield

    # +1 method
    def estimated_annual_income(self) -> float:
        return self.current_price * (self.dividend_yield / 100)

    def info(self) -> str:
        return f"{self.base_info()} | DivYield: {self.dividend_yield:.2f}%"


class Bond(Security):
    """Bond (אג\"ח)"""

    def __init__(self, symbol: str, name: str, current_price: float, interest_rate: float):
        super().__init__(symbol, name, current_price)
        if interest_rate < 0:
            raise ValueError("interest_rate cannot be negative")
        self.interest_rate = interest_rate

    def annual_interest(self) -> float:
        return self.current_price * (self.interest_rate / 100)

    def info(self) -> str:
        return f"{self.base_info()} | Interest: {self.interest_rate:.2f}%"


class Option(Security):
    """Option (אופציה)"""

    def __init__(self, symbol: str, name: str, current_price: float, strike_price: float):
        super().__init__(symbol, name, current_price)
        if strike_price < 0:
            raise ValueError("strike_price cannot be negative")
        self.strike_price = strike_price

    def is_in_the_money(self) -> bool:
        return self.current_price > self.strike_price

    def info(self) -> str:
        status = "In the Money" if self.is_in_the_money() else "Out of Money"
        return f"{self.base_info()} | Strike: {self.strike_price:.2f} ({status})"


def read_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Value cannot be empty.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    print("Section 2 - Inheritance (Securities)\n")

    # Input (per requirement)
    print("Enter Stock details:")
    s_symbol = read_non_empty("Symbol: ")
    s_name = read_non_empty("Name: ")
    s_price = read_float("Current price: ")
    s_div = read_float("Dividend yield (%): ")

    print("\nEnter Bond details:")
    b_symbol = read_non_empty("Symbol: ")
    b_name = read_non_empty("Name: ")
    b_price = read_float("Current price: ")
    b_rate = read_float("Interest rate (%): ")

    print("\nEnter Option details:")
    o_symbol = read_non_empty("Symbol: ")
    o_name = read_non_empty("Name: ")
    o_price = read_float("Current price: ")
    o_strike = read_float("Strike price: ")

    try:
        stock = Stock(s_symbol, s_name, s_price, s_div)
        bond = Bond(b_symbol, b_name, b_price, b_rate)
        option = Option(o_symbol, o_name, o_price, o_strike)
    except ValueError as e:
        print("Invalid input:", e)
        return

    # Create instances + call methods (per requirement)
    print("\n--- Portfolio ---")
    print("Stock:", stock.info(), "| Est. annual income:", f"{stock.estimated_annual_income():.2f}")
    print("Bond: ", bond.info(),  "| Est. annual interest:", f"{bond.annual_interest():.2f}")
    print("Option:", option.info())


if __name__ == "__main__":
    main()
