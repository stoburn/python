for value in range(1, 5):
	print(value)

even_numbers = list(range(2,102,2))
print(even_numbers)
print (min(even_numbers))
print (max(even_numbers))
print (sum(even_numbers))

squares = [value**2 for value in range(1,11)]
print(squares)