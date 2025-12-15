class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name.strip()
        self.price = float(price)
        self.category = category.strip().lower()

    def __str__(self):
        "Czytelny opis dla użytkownika"
        return f"{self.name} ({self.category}) - {self.price:.2f} zl"
    
    def __repr__(self):
        "Jednoznaczna reprezentacja do debugowania"
        return f"Product ('{self.name}', {self.price}, {self.category})"
    
    def __eq__(self, other):
        "Porownanie dwóch dwóch produktów jesli taka sama nazwa i kategoria"
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.category == other.category
    
    def __lt__(self, other):
        "Sortowanie po cenie"
        if not isinstance(other, Product):
            raise TypeError("Nie moża porównać z innym typem")
        return self.price < other.price
    
    def __len__(self):
        "Długośc nazwy produktu"
        return len(self.name)
    

        