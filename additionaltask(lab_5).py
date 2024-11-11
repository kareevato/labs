class Flower:
    def __init__(self, name, height, size, color, price, quantity, deliveryRate):
        self.name = name
        self.height = height
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.deliveryRate = deliveryRate

    def __str__(self):
        return f"Flower(name='{self.name}', height={self.height}, size={self.size}, color='{self.color}', price={self.price}, quantity={self.quantity}, deliveryRate={self.deliveryRate})"

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
            print(f"Not enough {flower.name} flowers in stock.")

    def calculate_total_price(self):
        total_price = sum(flower.get_price() * quantity for flower, quantity in self.flowers)
        return total_price

    def __str__(self):
        bouquet_details = "\n".join([f"{flower.name} ({quantity} шт.) - {flower.price * quantity} грн" for flower, quantity in self.flowers])
        return f"Bouquet:\n{bouquet_details}"

    def create_fixed_price_bouquet(self, shop, target_price):
        
        sorted_flowers = sorted(shop.flowers, key=lambda x: x.price, reverse=True)
        self.flowers = []
        
        remaining_price = target_price

        for flower in sorted_flowers:
    
            if remaining_price <= 0:
                break
            max_quantity = min(flower.get_quantity(), remaining_price // flower.get_price())
            if max_quantity > 0:
        
                self.add_flower(flower, int(max_quantity))
                remaining_price -= flower.get_price() * max_quantity

        
        if remaining_price > 0:
            print("Не вдалося досягти точної суми з наявними квітами.")
        else:
            print(f"Букет зібрано на суму {target_price} грн.")

def main():
    
    rose = Flower("Троянда", 30, 'large', 'red', 90.0, 100, 2.5)
    daisy = Flower("Ромашка", 15, 'small', 'pink', 10.0, 80, 0.5)
    tulip = Flower("Тюльпан", 20, 'medium', 'yellow', 50.0, 60, 1.0)
    lily = Flower("Лілія", 25, 'large', 'white', 70.0, 40, 1.5)
    orchid = Flower("Орхідея", 35, 'large', 'purple', 120.0, 30, 3.0)
    

    shop = FlowerShop()
    shop.add_flower(rose)
    shop.add_flower(daisy)
    shop.add_flower(tulip)
    shop.add_flower(lily)
    shop.add_flower(orchid)

    bouquet = Bouquet()
    target_price = float(input("Введіть цільову суму для букета: "))
    bouquet.create_fixed_price_bouquet(shop, target_price)

    print(bouquet)
    print(f"Загальна вартість букета: {bouquet.calculate_total_price()} грн.")

if __name__ == "__main__":
    main()