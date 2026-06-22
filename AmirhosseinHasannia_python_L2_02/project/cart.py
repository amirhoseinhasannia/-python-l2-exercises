from cart_item import CartItem


class Cart:
    """Manages the customer's items before checkout."""

    def __init__(self):
        """Start with an empty cart."""
        self.items = []

    def add_to_cart(self, product, quantity: int) -> None:
        """Add product or update quantity if it already exists."""
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                return

        new_item = CartItem(product, quantity)
        self.items.append(new_item)

    def remove_item(self, product_name: str) -> bool:
        """Remove an item from cart by name."""
        for item in self.items:
            if item.product.name.lower() == product_name.lower():
                self.items.remove(item)
                return True
        return False

    def get_grand_total(self) -> float:
        """Sum up all item prices."""
        total = 0
        for item in self.items:
            total += item.get_total_price()
        return total
