from models.product import Product

class Cart:

    def __init__(self):
        self._product = [] #Lista produktów

    def add_product(self, product: Product):
        "Dodawanie produktów"
        if not isinstance(product, Product):
            raise TypeError("Można dodoawać tylko proodukty")
        self._product.append(product)

    def remove_product(self, product: Product):
        "Usuwanie produktu"
        if product in self._product:
            self._product.remove(product)
    
    def total_price(self) -> float:
        "łączna kowata za wszystkie produkty"
        return sum(product.price for product in self._product)
    
    def __len__(self):
        "Liczba produktów"
        return len(self._product)
    
    def __contains__(self, product: Product):
        "Obsługa operatpra 'in'"
        return product in self._product
    
    def __str__(self):
        "Ładny wydruk koszyka"
        if not self._product:
            return "Koszyk jest pusty"
        
        lines = ["Zawrtość koszyk:"]
        for i, prod in enumerate(self._product, 1):
            lines.append(f" {i}, {prod}")
        lines.append(f"\nRazem: {self.total_price():.2f} zł ({len(self)}) produktów)")
        return "\n".join(lines)
    
    