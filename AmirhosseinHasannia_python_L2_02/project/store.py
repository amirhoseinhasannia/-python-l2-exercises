from product import Product


class Store:
    """Manages a list of products."""

    def __init__(self):
        """Initialize with an empty list."""
        self.products = []

    def add_product(self, name: str, price: float, stock: int) -> None:
        """Create and add a new product to the list."""
        new_prod = Product(name, price, stock)
        self.products.append(new_prod)

    def find_product(self, name: str):
        """Search for a product by its name."""
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None

    def list_products(self) -> None:
        """Show all products with numbers like [1], [2]."""
        if not self.products:
            print("No products available.")
            return

        print("Available products:")
        for index, p in enumerate(self.products, start=1):
            print(f"[{index}] {p}")
