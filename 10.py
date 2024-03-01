python
def convert_meters_to_miles(meters):
    miles = meters / 1609.34
    return miles

distance_in_meters = 762
distance_in_miles = convert_meters_to_miles(distance_in_meters)

print(f"Фейт Коннорс пробежала {distance_in_miles} миль.")
