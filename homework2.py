#homework2


name=input("Please enter your name: ")
surname=input("Please enter your surname: ")
age=int(input("Please enter your age: "))
birthdate=int(input("Please enter your date of birth: "))
userlist=[name,surname,age,birthdate]
for i in userlist:
    print(i)
if (age<=18):
    print("You can't go out because it's to dangerous.")
elif (age>18):
    print("You can go out to the street.")
else:
    print("error")
