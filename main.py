from src.products import Product
from src.cart import Cart
import time

def menu():
	print("\nSelecciona una opción:")
	print("1. Add Green Tea")
	print("2. Add Strawberries")
	print("3. Add Coffee")
	print("4. Show the cart")
	print("5. Exit program")
	print('------------------------------------------------')

def main():
	cart = Cart()

	products = {
		"1": Product("GR1", "Green Tea", 3.11),
		"2": Product("SR1", "Strawberries", 5.00),
		"3": Product("CF1", "Coffee", 11.23)
	}

	while True:
		menu()
		choice = input('Ingrese una opción: ')

		if choice in products:
			quantity_choice = int(input(f"How many {products[choice].name} you'd like to add? "))

			for _ in range(quantity_choice):
				cart.addProducts(products[choice])

			time.sleep(0.5)
			print('------------------------------------------------')
			print(f"{quantity_choice} {products[choice].name}(s) added to the cart.")
		elif choice == "4":
			print('\nCarrito:')
			if cart.items:
				product_counts = {}
				for item in cart.items:
					if item.name in product_counts:
						product_counts[item.name]["quantity"] += 1
					else:
						product_counts[item.name] = {"price": item.price, "quantity": 1}

				for name, data in product_counts.items():
					print(f"{data['quantity']} X {name} - {data['price']}€ each")
				print('************************************************')
				print(f'Total price: {cart.PrecioTotal()} €')
			else:
				print('The cart is empty, please add any product')
		elif choice == "5":
			print('Thank you! Have a nice day')
			break
		else:
				print('Wrong choice, try again!')

if __name__ == "__main__":
    main()
