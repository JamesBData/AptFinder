def apt_search1(city, max_rent, min_beds, pets_allowed):

    if pets_allowed == True:
        print(f"Weclome to GC property management. Looking up listings in {city} for {min_beds} bed rentals that allow pets with a budget of ${max_rent} per month...")
    else:
        print(f"There are listings in {city} for {min_beds} bed rentals that don't allow pets in your budget of ${max_rent} per month...")

apt_search1("Detroit", 1500, 3, False)

def apt_search2(city, max_rent, min_beds = 2, pets_allowed = False):
    if pets_allowed == False:
        print(f"Looking up listings in {city} with a budget of ${max_rent} and {min_beds} rooms. ")
    else:
        print(f"Looking up listings in {city} with a budget of ${max_rent} and {min_beds} rooms that allows pets.")
apt_search2("Tampa", 1400)
apt_search2(city="any", min_beds=5, pets_allowed=True, max_rent="any")
apt_search2("Toronto", 2000, pets_allowed = True)
plus_one_hundred = lambda a: a + 100
square_num = lambda x: x ** 2
concatenate = lambda y: "- " + y
divide_by_3 = lambda b: b / 3
print(plus_one_hundred(20))
print(square_num(5))
print(concatenate("minus"))
print(divide_by_3(9))
