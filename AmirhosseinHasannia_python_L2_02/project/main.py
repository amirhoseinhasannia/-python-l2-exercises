from store import Store
from cart import Cart

# Initializing the global store
store = Store()


def manager_flow() -> None:
    """Manager process for adding products with error handling."""
    print("\n-------------------------------")
    print("📦  Add Products")
    print("-------------------------------")

    while True:
        name = input("Enter product name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            print("Returning to main menu...")
            break
        if not name:
            print("❌ Name cannot be empty.")
            continue

        try:
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock quantity: "))

            if price < 0 or stock < 0:
                print("❌ Price and stock cannot be negative.")
                continue

            store.add_product(name, price, stock)
            print(f"✅ Product added: {name} - ${price:.2f} (Stock: {stock})\n")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number for price and stock.")


def customer_flow() -> None:
    """Customer portal with product listing and shopping logic."""
    cart = Cart()

    while True:
        print("\n-----------------")
        print("🛍️  CUSTOMER PORTAL")
        print("-----------------")
        print("👋 Hello, dear customer!")
        store.list_products()

        print("\nWhat would you like to do?")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Return to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            p_name = input("Enter product name to add: ").strip()
            product = store.find_product(p_name)
            if product:
                try:
                    qty = int(input("Enter quantity: "))
                    if qty <= 0:
                        print("❌ Quantity must be more than 0.")
                    elif qty <= product.stock:
                        cart.add_to_cart(product, qty)
                        product.stock -= qty
                        print(f"✅ Added {qty} x {product.name} to cart.")
                    else:
                        print(f"❌ Not enough stock! (Available: {product.stock})")
                except ValueError:
                    print("❌ Invalid input! Quantity must be a whole number.")
            else:
                print("❌ Product not found.")

        elif choice == "2":
            p_name = input("Enter product name to remove: ").strip()
            # Find the item in the cart first
            removed_item = None
            for item in cart.items:
                if item.product.name.lower() == p_name.lower():
                    removed_item = item
                    break

            if removed_item:
                # Restore the quantity back to store stock
                removed_item.product.stock += removed_item.quantity
                cart.remove_item(p_name)
                print(f"🗑️  Removed {p_name} from cart.")
                print(
                    f"🔁 Restocked {removed_item.quantity} item(s). New stock: {removed_item.product.stock}"
                )
            else:
                print("❌ Item not found in cart.")

        elif choice == "3":
            print("\n🛒 Your cart:")
            if not cart.items:
                print("Your cart is empty.")
            else:
                for item in cart.items:
                    print(
                        f"- {item.product.name} x{item.quantity} - ${item.get_total_price():.2f}"
                    )
                print(f"💰 Total: ${cart.get_grand_total():.2f}")

        elif choice == "4":
            if not cart.items:
                print("❌ Your cart is empty.")
            else:
                print("\n🧾 Final Checkout:")
                for item in cart.items:
                    print(
                        f"- {item.product.name} x{item.quantity} - ${item.get_total_price():.2f}"
                    )
                print(f"💳 Total amount due: ${cart.get_grand_total():.2f}")
                print("🌿 Thank you for shopping with us!")
                cart.items = []

        elif choice == "5":
            break


def main() -> None:
    """Main entry point with the correct store emoji."""
    print("==========================================")
    print("     🛍️  MINI STORE MANAGEMENT SYSTEM")
    print("==========================================")

    while True:
        print("\n👋 Welcome! Please select your role:")
        print("1. Store Manager")
        print("2. Customer")
        print("3. Exit Program")

        choice = input("Enter choice: ")

        if choice == "1":
            print(
                "\n-------------------------------\n🔐 Store Manager Login\n-------------------------------"
            )
            user = input("Username: ")
            pw = input("Password: ")
            if user == "admin" and pw == "1234":
                print("\n✅ Login successful! Welcome, Manager.")
                manager_flow()
            else:
                print("\n❌ Login failed!")

        elif choice == "2":
            customer_flow()

        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
