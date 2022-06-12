requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nPizza has been assembled!\n")

# A more efficient way to display toppings.

requested_toppings = ['mushrooms','extra cheese', 'green peppers']

for requested_toppings in requested_toppings:
		print(f"Adding {requested_toppings}.")
print("\nPizza has been assembled, more efficiently!\n")

# What if we're out of ingredients?

requested_toppings = ['mushrooms','extra cheese', 'green peppers']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers.")
	else:
		print(f"Adding {requested_topping}.")

print("\nPizza has been assembled, but not with anything that's missing!\n")

# What if they don't want any toppings?

requested_toppings = []

if requested_toppings:
		for requested_topping in requested_toppings:
			print(f"Adding {requested_topping}.")
		print("\nFinished making pizza!")
else: 
	print("Plain pizza it is.\n")

# What if we have a list of available toppings, and let customers ask for anything?

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"We ain't got no {requested_topping}.")
print("\nDone making!\n")
















