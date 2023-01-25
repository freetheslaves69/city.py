cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# Traverse the list and print each city name
for city in cities:
    print(city)

# Allow user to add a city to the list
new_city = input("Enter a city to add to the list: ")
cities.append(new_city)

# Allow user to delete a city from the list
delete_city = input("Enter a city to delete from the list: ")
cities.remove(delete_city)

# Print the updated list of cities
print("\nUpdated list of cities:")
for city in cities:
    print(city)
