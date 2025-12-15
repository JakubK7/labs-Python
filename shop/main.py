from models.product import Product
from logic.cart import Cart

def main():
    print("Symulator skelpu internetowego")

    # Tworzenie produktów
    p1 = Product("Laptop Gamingowy", 3500, "electronics")
    p2 = Product("Myszka Gamingowa", 169.99, "electronics")
    p3 = Product("Banan", 3.50, "food")
    p4 = Product("Maliny", "5.30", "food")
    p5 = Product("Laptop Gamingowy", 3999, "electronics")

    print("Produkty:")
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print()

    # Porównanie
    print("Porównania:")
    print(f"p1 == p5: {p1 == p5}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"p1 < p2: {p1 < p2}")
    print(f"p3 < p4: {p3 < p4}")

    #Długośc nazw
    print("Długośc nazw:")
    print(f"len(p1): {len(p1)}")
    print(f"len(p3): {len(p3)}")
    print()

    # Sortowanie produktów po cenie 
    products = [p1, p2, p3, p4, p5]
    print("Produkty posortowane po cenie:")
    for prod in sorted(products):
        print(f" {prod}")
    print()

    # Koszyk
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p3)
    cart.add_product(p3)
    cart.add_product(p2)

    print(cart)
    print()

    print(f"Liczba produktw w koszyku: {len(cart)}")
    print(f"Czy Laptop jest w koszyku? {'Tak' if p1 in cart else 'Nie'}")
    print(f"Czy Banan jest w koszyku? {'Tak' if p4 in cart else 'Nie'}")

    cart.remove_product(p3)
    print("\n Po usuniiu malin:")
    print(cart)

if __name__ == "__main__":
    main()