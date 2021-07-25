# WRITE YOUR FUNCTIONS HERE

# test1 - get shop name
def get_pet_shop_name(shop_name):
    name_of_shop = shop_name["name"]
    return name_of_shop

# test2 - get total cash
def get_total_cash(float):
    holdings = float["admin"]["total_cash"]
    return int(holdings)

# test3 - add or remove cash
def add_or_remove_cash(shop, takings):
    holdings = shop["admin"]["total_cash"]
    new_balance = (holdings + takings)
    shop["admin"]["total_cash"] = new_balance

# test4 - get pets sold
def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

# test5 - increase pets sold
def increase_pets_sold(shop, pets_sold):
    sold = shop["admin"]["pets_sold"]
    sold = sold + pets_sold
    shop["admin"]["pets_sold"] = sold

# test6 - check stock count
def get_stock_count(shop):
    count = len(shop["pets"])
    return count

# test7 - get pets by breed
def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(breed)
    return pets

# test8 - checks fn in test7 for missing breeds 

# test9 - find pet by name
def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet

# test10 - remove pet by name
def remove_pet_by_name(shop, name):
    pets = shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            pets.remove(pet)

#  test11 - add pet to stock
def add_pet_to_stock(shop, name):
    shop["pets"].append(name)   

# test12 - get customer cash
def get_customer_cash(shop):
    cash = shop["cash"]
    return cash

# test13 - remove customer cash
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

# test14 - get customer pet count
def get_customer_pet_count(customers):
    count = customers["pets"]
    return len(count)               # not sure this is correct? 

# test15 - add pet to customer
def add_pet_to_customer(person, new_pet):
    person["pets"].append(new_pet)