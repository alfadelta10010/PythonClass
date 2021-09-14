# for i in range(1, 13):
#    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
#    print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}?: ".format(name)))
print(age)

# if age >= 18:
#     print("Register to vote, {}!".format(name))
#     print("Please follow the instructions")
# else:
#     print("Tell the adults to vote! Come back in {0} years, {1}".format(18 - age, name))

if age < 18:
    print("Tell the adults to vote! Come back in {0} years, {1}".format(18 - age, name))
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi")
else:
    print("Register to vote, {}!".format(name))
    print("Please follow the instructions")
