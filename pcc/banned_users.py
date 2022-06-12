banned_users = ['andrew','carolina','david']
user = 'david'

if user not in banned_users:
	print(f"{user.title()}, you can post!")
else:
	print(f"{user.title()}, you have been banned.")