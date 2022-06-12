car = 'Audi'
year = 2007

if car.lower() == 'audi':
	print("This car is an " + car.title() + "!")
else:
	print("Not an Audi.")

if car.lower() != 'saab':
	print("Not a Saab.")
else:
	print("This car is a Saab!")


if year != 2007:
	print("This " + car.title() + " is not a model year 2007.")
else:
	print("This " + car.title() + " is a model year 2007!")

if year == 2007 and car.lower() == 'audi':
	print("It's a 2007 Audi, wowza!")
else:
	print("Well, it's no 2007 Audi.")