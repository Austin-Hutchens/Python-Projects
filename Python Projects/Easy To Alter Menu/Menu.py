class Menu:
    def __init__(self, name, items, start_time, end_time):
        """Initialize the menu with name, items, start and end times."""
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        """Return a string representation of the menu."""
        return f"{self.name} Menu: Available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        """Calculate the total bill for the purchased items."""
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return total_price


# Create instances of different menus
brunch = Menu(
  name="Brunch",
  items={
      'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 
      'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  },
  start_time="11:00",
  end_time="16:00"
)

early_bird  = Menu(
  name="Early Bird",
  items={
      'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
      'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
      'coffee': 1.50, 'espresso': 3.00,
  },
  start_time="15:00",
  end_time="18:00"
)

dinner = Menu(
  name="Dinner",
  items={
      'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
      'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
  },
  start_time="17:00",
  end_time="23:00"
)

kids = Menu(
  name="Kids",
  items={
      'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
  },
  start_time="11:00",
  end_time="21:00"
)

# Print the brunch menu
print(brunch)

# Example orders and bill calculations
order = ['pancakes', 'home fries', 'coffee']
total_bill = brunch.calculate_bill(order)
print(f"The total bill for the brunch order is: ${total_bill:.2f}")

# Early bird example order
eb_order = ['salumeria plate', 'mushroom ravioli (vegan)']
early_bird_purchase = early_bird.calculate_bill(eb_order)
print(f"The total bill for the early bird order is: ${early_bird_purchase:.2f}")


class Franchise:
    def __init__(self, address, menus):
        """Initialize the franchise with an address and associated menus."""
        self.address = address
        self.menus = menus

    def __str__(self):
        """Return a string representation of the franchise."""
        return f"Franchise is located at {self.address}"

    def available_menus(self, time):
        """Return a list of menus available at a specific time."""
        available = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available.append(menu)
        return available


# Create franchises
flagship_store = Franchise(
  address='1232 West End Road',
  menus=[brunch, early_bird, dinner, kids]
)

new_installment = Franchise(
  address='12 East Mulberry Street',
  menus=[brunch, early_bird, dinner, kids]
)

# Check menus available at specific times
noon_menus = flagship_store.available_menus('12:00')
print("Menus available at 12:00:")
for menu in noon_menus:
    print(menu)

# Check menus available at 5:00 PM
evening_menus = flagship_store.available_menus('17:00')
print("Menus available at 5:00 PM:")
for menu in evening_menus:
    print(menu)


class Business:
    def __init__(self, name, franchises):
        """Initialize the business with a name and a list of franchises."""
        self.name = name
        self.franchises = franchises

# Example usage of the classes
first_business = Business(
  name="Basta Fazoolin' with my Heart",
  franchises=[flagship_store, new_installment]
)

# Add another franchise with a unique menu
arepas_menu = Menu(
  name="Take a' Arepa",
  items={
      'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
  },
  start_time="10:00",
  end_time="20:00"
)

arepas_place = Franchise(
  address="189 Fitzgerald Avenue",
  menus=[arepas_menu]
)

arepas_business = Business(
  name="Take a' Arepa!",
  franchises=[arepas_place]
)
