from datetime import date

class Invoice:
    """
Represents an invoice with customer details and discount calculation.
     """
    def __init__(
        self,
        invoice_id: int,
        customer_name: str,
        issue_date: date,
        quantity: int,
        unit_price: float,
        discount_percent: float,
    ):
        if invoice_id <= 0:
            raise ValueError("invoice_id must be positive")
        if not customer_name:
            raise ValueError("customer_name cannot be empty")
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if unit_price < 0:
            raise ValueError("unit_price cannot be negative")

        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.issue_date = issue_date
        self.quantity = quantity
        self.unit_price = unit_price

        self._discount_percent = 0.0
        self.discount_percent = discount_percent  # goes through setter

    @property
    def discount_percent(self) -> float:
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, value: float) -> None:
        if not (0.0 <= value <= 100.0):
            raise ValueError("discount_percent must be between 0 and 100")
        self._discount_percent = value

    def subtotal(self) -> float:
        return self.quantity * self.unit_price

    def total(self) -> float:
        return self.subtotal() * (1 - self.discount_percent / 100)

    def summary(self) -> str:
        return (
            f"Invoice #{self.invoice_id}\n"
            f"Customer: {self.customer_name}\n"
            f"Issue date: {self.issue_date.isoformat()}\n"
            f"Quantity: {self.quantity}\n"
            f"Unit price: {self.unit_price:.2f}\n"
            f"Discount: {self.discount_percent:.1f}%\n"
            f"Subtotal: {self.subtotal():.2f}\n"
            f"Total: {self.total():.2f}"
        )

# Helper functions for input
def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def read_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Value cannot be empty.")

def main() -> None:
    invoice_id = read_int("Invoice ID (positive integer): ")
    customer_name = read_non_empty("Customer name: ")
    quantity = read_int("Quantity (positive integer): ")
    unit_price = read_float("Unit price (>= 0): ")
    discount_percent = read_float("Discount percent (0-100): ")

    try:
        inv = Invoice(
            invoice_id=invoice_id,
            customer_name=customer_name,
            issue_date=date.today(),
            quantity=quantity,
            unit_price=unit_price,
            discount_percent=discount_percent,
        )
    except ValueError as e:
        print("Invalid input:", e)
        return

    print("\n--- Invoice Summary ---")
    print(inv.summary())
    print("\n--- Method Calls ---")
    print("Subtotal:", inv.subtotal())
    print("Total:", inv.total())

if __name__ == "__main__":
    main()
