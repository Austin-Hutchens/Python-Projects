class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name} Menu: Available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        total_price = 0  # Initialize total_price to 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]  # Add the price of the item
        return total_price

# Create instances of different menus
brunch = Menu(
  name = "Brunch",
  items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},
  start_time = "11:00",
  end_time = "16:00"
  )

early_bird  = Menu(
  name = "Early Bird",
  items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,},
  start_time = "15:00",
  end_time = "18:00"
  )

dinner = Menu(
  name = "Dinner",
  items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,},
  start_time = '17:00',
  end_time = '23:00'
  )

kids = Menu(
  name = "kids",
  items = { 'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00},
  start_time = '11:00',
  end_time = '21:00'
  )

# Print the brunch menu
print(brunch)

# Breakfast order: pancakes, home fries, and coffee
order = ['pancakes', 'home fries', 'coffee']

eb_order = {'salumeria plate', 'vegan mushroom ravioli'}

# Calculate the total bill for the order
total_bill = brunch.calculate_bill(order)
early_bird_purchase = early_bird.calculate_bill(order)

# Print out the total price
print(f"The total bill for the brunch order is: ${total_bill:.2f}")

print(f"The total bill for the brunch order is: ${early_bird_purchase:.2f}")


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __str__(self):
    return f"Franchise sis located at {self.address}"

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available.append(menu)
    return available

flagship_store = Franchise(
  address = '1232 West End Raod',
  menus = [brunch, early_bird, dinner, kids]
  )

new_installment = Franchise(
  address = '12 East Mulberry Street',
  menus = [brunch, early_bird, dinner, kids]
  )

noon = flagship_store.available_menus('12:00')

# Print the available menus at 12:00
print("Menus available at 12:00:")
for menu in noon:
    print(menu)
# Print out the available menus at noon

evening = flagship_store.available_menus('17:00')
print("Menus available at 5pm")
for menu in evening:
  print(menu)

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

first_business = Business(
  name = "Basta Fazoolin' with my Heart",
  franchises = [flagship_store, new_installment]
  )

arepas_menu = Menu(
  name = 'Take a\' Arepa',
  items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},
  start_time = '10:00',
  end_time = '20:00'
  )

arepas_place = Franchise(
  address = '189 Fitzgerald Avenue',
  menus = arepas_menu
  )

arepas_business = Business(
  name = 'Take a\' Arepa!',
  franchises = arepas_place
)
