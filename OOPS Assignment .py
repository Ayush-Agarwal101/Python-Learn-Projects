class Pizza:
    def __init__(self, size, crust, sauce):
        self.size = size
        self.crust = crust
        self.sauce = sauce
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def show_pizza(self):
        print("\nYour Pizza Order Summary:")
        print(f"Size: {self.size}")
        print(f"Crust: {self.crust}")
        print(f"Sauce: {self.sauce}")
        print(f"Toppings: {', '.join(self.toppings) if self.toppings else 'None'}")

s = input("Enter pizza size (Small, Medium, Large): ")
print("\n")

print("Available crust types: Thin Crust, Thick Crust, Cheese Burst, Stuffed Crust, Pan Crust")
c = input("Enter crust type: ")
print("\n")

print("Available sauce types: Tomato Basil, Marinara, Barbecue, Alfredo, Pesto, Buffalo")
s1 = input("Enter sauce type: ")
print("\n")

print("Available toppings: Mushrooms, Onions, Bell Peppers, Olives, Chicken Sausage, Pepperoni")
t = input("Enter toppings (comma separated): ")
print("\n")

p1 = Pizza(s, c, s1)

for topping in t.split(','):
    p1.add_topping(topping.strip())

p1.show_pizza()