
#######################################################################################################################


cafes = [
    {"name": "Ali_Foots", "tea_price": 300, "meal": "Sandwich", "meal_price": 450},
    {"name": "Kubanych", "tea_price": 250, "meal": "Salad", "meal_price": 350},
    {"name": "PizzaBurg", "tea_price": 400, "meal": "Pizza", "meal_price": 700},
    {"name": "Jony_burger", "tea_price": 200, "meal": "Burger", "meal_price": 300},
    {"name": "Navat", "tea_price": 350, "meal": "Polow", "meal_price": 1000}
]

budget = int(input("Enter your budget for tea and a meal: "))

available_cafes = []

print("\nCafes within your budget:")
for cafe in cafes:
    total_price = cafe["tea_price"] + cafe["meal_price"]
    if total_price <= budget:
        available_cafes.append(cafe)
        print(f"{cafe['name']} - Total: {total_price} som (Tea: {cafe['tea_price']} som, Meal: {cafe['meal']} - {cafe['meal_price']} som)")

if not available_cafes:
    print("Unfortunately, there are no cafes within your budget.")



#######################################################################################################################