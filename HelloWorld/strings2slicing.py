# Mini Challenge
#                   11111
#         012345678901234
parrot = "Norwegian Blue"
# -       43210987654321
#             1

print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
print(parrot[:9])  # Norwegian
print(parrot[10:14])  # Blue
print(parrot[10:])  # Blue
print(parrot[:6])  # Norweg
print(parrot[6:])  # ian Blue

print(parrot[:6] + parrot[6:])  # Norwegian Blue

print(parrot[:])  # Norwegian Blue

letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[:9])  # abcdegfhi
print(letters[9:])  # jklmnopqrstuvwxyz
print(letters[:])  # abcdefghijklmnopqrstuvwxyz
print(letters[:10] + letters[10:])  # abcdefghijklmnopqrstuvwxyz


