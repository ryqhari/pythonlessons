# data types
# integer -> int
# float 
# string -> str
# null -> None


# str, int, float,
x = 1
y = 2
word = "hello"
print(str(x) + str(y) + word)


class Cup:
    def __init__(self, lid, color):
        self.lid = lid
        self.color = color

my_cup = Cup(True, "green")
my_cup2 = Cup(True, "yellow")
print(my_cup)
print(type(my_cup))

