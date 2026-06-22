class Product:
    """Represents a single product in the store."""

    def __init__(self, name: str, price: float, stock: int):
        """Initialize product attributes."""
        self.name: str = name
        self.price: float = price
        self.stock: int = stock

    def __str__(self) -> str:
        """How the product looks when printed."""
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"
