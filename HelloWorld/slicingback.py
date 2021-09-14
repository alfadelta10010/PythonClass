letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]  # zyxwvutsrqponmlkjihgfedcb
print(backwards)

# to include a, no stop value
backwards = letters[25::-1]  # zyxwvutsrqponmlkjihgfedcba
print(backwards)
# works

# to include a, use -1 stop value
backwards = letters[25:-1:-1]  # zyxwvutsrqponmlkjihgfedcb
print(backwards)
# doesn't work, cause it stops at 25 itself

backwards = letters[::-1]  # zyxwvutsrqponmlkjihgfedcba
print(backwards)
# python idiom

# Challenge!
# slice outputs "qpo"
out1 = letters[16:13:-1]
print(out1)  # qpo

# slice outputs "edcba"
out2 = letters[4::-1]
print(out2)  # edcba

# slice outputs last 8 characters, in reverse order
out3 = letters[:-9:-1]
print(out3)  # zyxwvuts

# python idioms
print(letters[-4:])  # Get last 4 items
print(letters[-1:])  # Get last item
print(letters[:1])  # Get first item
print(letters[0])  # Get first item
