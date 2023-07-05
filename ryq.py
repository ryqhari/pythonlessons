print("Hello, World!")
#this is a comment
print("Cheers Man!")
"""
this is a comment
so do not worry with
it cause you are free
"""

def myfunc():
    global x
    x = "all weather"
myfunc()

print("Today is", x)

fruit = ("apple", "gauva", "banana", "orange")
print(fruit)
if "mango" in fruit:
    print("Yes, that is correct")
else: print("not found")

txt ="hello, world"
print("hello" not in txt)

a=str("mango")
str.encode("no_use")
print(str.encode(a))

age = 35
town = "Mankoadze"
txt = "My name is Richie, and I am {} years old, and reside at {}"
print(txt.format(age,town))

drinks = ["coke", "fanta", "sprite"]
food = ("banku", "rice", "fufu")
drinks.pop()
print(drinks)

import platform
print(platform.version())

