user = {"id": 1234, "first_name": "john", "last_name":"williams", "phone": "867-5309"}
print(user)
print(user['id'])

name = user.get('first_name') + " " + user['last_name']
print(name)

for key in user:
    print(key)

for key in user:
    print(user[key])

print(len(user))

user['email'] = "johnwilliams@gmail.com"
print(user)

phone = user.pop('phone')
print(user)

last_item = user.popitem()
print(last_item)

print(user)

user.clear()

print(user)