age = 18
print("My age is " + str(age) + " years")

age = 18
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "January", "March", "May", "July", "August", "October", "December"))
print("There are {0} days in January, March, May, July, August, October and December".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sept: {1},"
      " Oct: {2}, Nov: {1}, Dec: {1}".format(28, 30, 31))
print()

print("""Jan: {2},
Feb: {0}, 
Mar: {2}, 
Apr: {1}, 
May: {2}, 
Jun: {1},
Jul: {2}, 
Aug: {2}, 
Sept: {1}, 
Oct: {2}, 
Nov: {1}, 
Dec: {1}""".format(28, 30, 31))
