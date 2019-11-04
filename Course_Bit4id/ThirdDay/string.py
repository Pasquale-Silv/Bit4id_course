message = "I like dogs and cats... But i prefer cats"

print(message.find('cat'))
print(message.rfind('cat'))

print()

new_message = message.replace("cats", "snakes")
print(new_message)

number_of_snakes = new_message.count("snakes")
print(number_of_snakes)

words = message.split(" ")
print(words)

print("\nVediamo lo slicing:")
slice = words[0:3]
for word in slice:
    print(word)

