country = input("Where do you live :")

munster = ('cork','kerry', 'limerik', 'clare', 'waterford', 'tipperary',5,6,7)
print(type(munster))

if country in munster:
    print("You live in Munster")
else:
    print("You live outside Munster")