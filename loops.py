# loops/iterations
# for..in loop
# while loops

# Iterable
# lists, tuples

even_numbers = (2, 4, 6, 8)
# r_obj = range(10)
# print(type(r_obj))

for i in even_numbers:
    if i == 6:
        break
    print(i)

i = 0

while i < len(even_numbers):
    t = even_numbers[i]
    
    i = i + 1