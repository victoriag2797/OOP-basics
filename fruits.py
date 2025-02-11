class Fruit:
    def __init__(self, name, color, taste, price):
        self.name = name
        self.color = color
        self.taste = taste
        self.price = float(price)
    
    def details(self):
        print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Fruit Type: {self.name}
            Fruit Color: {self.color}
            Fruit Taste: {self.taste}
            Fruit Price: {self.price}
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

    def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
        print(f"""
        ##################################
        Total Cost: {total}
        ##################################
        """)

apple = Fruit("Apple", "Red", "Sweet", "1.25")
orange = Fruit("Orange", "Orange", "Sweet", "2.67")
lemon = Fruit("Lemon", "Yellow", "Sour", "4.98")
lime = Fruit("Lime", "Green", "Bitter", "1.98")
blueberry = Fruit("Blueberry", "Blue", "Sweet", "3.98")
grape = Fruit("Grape", "Purple", "Sweet", "9.98")
rasberry = Fruit("Rasberry", "Pink", "Sweet", "4.53")

apple.details()
orange.details()
lemon.details()
lime.details()
blueberry.details()
grape.details()
rasberry.details()

apple.calc_sales_tax(0.4)
orange.calc_sales_tax(0.4)
lemon.calc_sales_tax(0.4)
lime.calc_sales_tax(0.4)
blueberry.calc_sales_tax(0.4)
grape.calc_sales_tax(0.4)
rasberry.calc_sales_tax(0.4)