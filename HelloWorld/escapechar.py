# \n to start new line, \t to tab, \' for single quote, \" for double quote
splitString = "This string has been \nsplit over \nseveral times"
print(splitString)
tabbedString = "1\t2\t3\t4\t5\t6\t7"
print(tabbedString)

# In IDEA, the Tab stops are 4 spaces, in terminal, it's 8 spaces
print('The pet shop owner said, "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said, \"No, no, 'e's uh,...he's resting\".")
# using 3 double quotes aka triple quotes, we don't need to do this.
print("""The pet shop owner said, "No, no, 'e's uh,...he's resting".""")

anotherSplitString = """This string has been \
split over 
several times"""
print(anotherSplitString)
# Adding \ at the end of a triple quote string ignores line breaks in output

# What if the \ needs to be printed?
print(r"C:\Users\alphadelta\Desktop\text.txt")
print("C:\\Users\\alphadelta\\Desktop\\text.txt")
