from product import Product


class CartItem:
    """Represents an item placed in the shopping cart."""

    def __init__(self, product: Product, quantity: int):
        """Initialize with a product and requested quantity."""
        self.product: Product = product
        self.quantity: int = quantity

    def get_total_price(self) -> float:
        """Calculate price for this specific item."""
        return self.product.price * self.quantity
