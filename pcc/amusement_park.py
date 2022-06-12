age = 5
print(f"Your age is: {age}.")

if age < 4:
	print("Your admission price is: $0")
elif age < 18:
	print("Your admission price is: $25")
else:
	print("Your admission price is: 40")

agey = 18

if agey < 4:
	price = 0
elif agey < 18:
	price = 25
else:
	price = 40

print(f"Your age is: {agey}.")
print(f"Your admission price is: ${price}")