# Making a list with cities
lijstMetSteden = ["Brussel", "Antwerpen", "Bonn", "Berlijn", "Hamburg"]

# Asking the user for string input
target = input(str("Type een naam van een stad: "))

# Check if the input can be found in the list
# Using capitalize to make the first character of the string input a uppercase
if target.capitalize() in lijstMetSteden:

    # Find the index of the value in the list
    position = lijstMetSteden.index(target.capitalize())
    # Using len to find the length of the user input string
    print(target, "staat op positie", position + 1, "en telt", len(target), "letters.")

else:
    print(target, "komt niet in de lijst voor.")