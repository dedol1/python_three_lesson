name = "Samuel Afotey Laryea"
age = 24
height = 5.8

#using string formatters

print(f"My name is {name}")
print(f"i am {age} years old")
print(f"i am {height} feet tall")

#different formating mode
print("Mary had a little lamp")
print("It was as white as {}".format('snow'))
print("And everywhere that {} went, the lamp was sure to go".format('Mary'))


#this is another formatting mode

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("try your ", "own here ", "maybe a poem ","or a song about fear"))

print("jan\nfeb\nmar\napril\nmay\njune\njuly\naug\nsep\noct\nnov\ndec")