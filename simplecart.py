class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = {}
    
    def add_product(self, product, quantity):
        if product.name in self.cart:
            self.cart[product.name]['quantity'] += quantity
        else:
            self.cart[product.name] = {'product': product, 'quantity': quantity}
    
    def remove_product(self, product, quantity):
        if product.name in self.cart:
            if self.cart[product.name]['quantity'] > quantity:
                self.cart[product.name]['quantity'] -= quantity
            else:
                del self.cart[product.name]
    
    def calculate_total(self):
        total = 0.0
        for item in self.cart.values():
            total += item['product'].price * item['quantity']
        return total


if __name__ == "__main__":
   
    apple = Product('Apple', 0.5)
    banana = Product('Banana', 0.3)
    orange = Product('Orange', 0.8)


    cart = ShoppingCart()


    cart.add_product(apple, 3)
    cart.add_product(banana, 2)
    cart.add_product(orange, 1)

    print(f"Total cost: ${cart.calculate_total():.2f}")

    cart.remove_product(apple, 1)
    cart.remove_product(banana, 1)

    print(f"Total cost after removal: ${cart.calculate_total():.2f}")
