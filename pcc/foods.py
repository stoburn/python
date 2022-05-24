my_foods = ['pizza','falafel','funfetti cake']
friend_foods = my_foods[:]

my_foods.append('lasagna')
friend_foods.append('tofu')

print("My faves:")
for food in my_foods:
	print(food)


print("\nFriend faves:")
for ffood in friend_foods:
	print(ffood)
