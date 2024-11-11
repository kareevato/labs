class Flower:
    def __init__(self, height, size, color, price, quantity, deliveryRate):
        self.height = height
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.deliveryRate = deliveryRate

    def __str__(self):
        return f"Flower(height={self.height}, size={self.size}, color='{self.color}', price={self.price}, quantity={self.quantity}, deliveryRate={self.deliveryRate})"

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def calculate_delivery_price(self):
        return self.price + self.deliveryRate


class FlowerShop:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def remove_flower(self, flower):
        if flower in self.flowers:
            self.flowers.remove(flower)

    def get_top_expensive_flowers(self, top_n=5):
        sorted_flowers = sorted(self.flowers, key=lambda x: x.price, reverse=True)
        return sorted_flowers[:top_n]

    def __str__(self):
        return f"FlowerShop with {len(self.flowers)} flowers"


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower, quantity):
        if flower.quantity >= quantity:
            self.flowers.append((flower, quantity))
            flower.set_quantity(flower.quantity - quantity)
        else:
            print(f"Not enough {flower.color} flowers in stock.")

    def calculate_total_price(self):
        total_price = sum(flower.get_price() * quantity for flower, quantity in self.flowers)
        return total_price

    def __str__(self):
        return f"Bouquet with {len(self.flowers)} flowers"

def main():
    
    rose = Flower(30, 'large', 'red', 10.0, 100, 2.5)
    tulip = Flower(20, 'medium', 'yellow', 7.0, 50, 1.0)
    lily = Flower(25, 'large', 'white', 15.0, 30, 3.0)
    daisy = Flower(15, 'small', 'pink', 5.0, 80, 0.5)
    
    shop = FlowerShop()
    shop.add_flower(rose)
    shop.add_flower(tulip)
    shop.add_flower(lily)
    shop.add_flower(daisy)

    print("Top expensive flowers in the shop:")
    for flower in shop.get_top_expensive_flowers(3):
        print(flower)

    bouquet = Bouquet()
    bouquet.add_flower(rose, 5)
    bouquet.add_flower(tulip, 3)

    print(f"Bouquet total price: {bouquet.calculate_total_price()}")

    shop.remove_flower(daisy)
    print(f"Shop after removing daisy: {shop}")

if __name__== "__main__":
    main()