square = list(map(lambda x: x*x, numbers))
print("Squares:", square)

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even)

total = reduce(lambda x, y: x+y, numbers)
print("Sum:", total)