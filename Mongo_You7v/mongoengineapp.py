import email
from mongoengine import connect
from mongoenginemodel import User

# connect to mongo db
connect(db="mongoengine", host="localhost", port=27017)

#add signle user to mongo databases
user=User(email="mak@gmail.com",
        first_name="Mahabub",
        last_name="Rahman",
        age=25)
user.save()

# Inset multiple user into the database
User.objects.insert([User(email="maka@gmail.com",
        first_name="Mahabub",
        last_name="Rahman",
        age=25),
        User(email="maks@gmail.com",
        first_name="Mahabub",
        last_name="Rahman",
        age=25)])

# update user with email
update_user=User.objects(email="maks@gmail.com").update(age=26)

# delete user exsisting data
delete_user=User.objects(email="maks@gmail.com").delete()


# fetch data one

user=User.objects.get(email="maks@gmail.com")

#fetch all documents

user=User.objects()
for u in user:
        print(u.email)

# fetch by feltiring
user=User.objects(age__lte=30)

for u in user:
        print(u.age)

user=User.objects(first_name__exact='mak')

for u in user:
        print(u.first_name)
