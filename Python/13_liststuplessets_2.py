# Tuples
# sorting and reversing etc are not allowed in tuple, hence tuple is immutable
prices = (29.5, 12, 45.33)
print(prices)
print(len(prices))
print(prices.count(45.33))
print(4.5 in prices)        # returns boolean value
print(4.5 not in prices)    # returns boolean value

# looping
for x in prices:
    print(x)
print(prices[0])

# Sets
prices = {29.95, 4.5, 15.5, 4.5}    # duplicate elements are removed automatically when you print
print(prices)
prices.add(20)  # added at the 0th index
print(prices)
prices.update({10, 25, 25})     # answer is different
print(prices)
prices.update([10, 15, 25])     # answer is different
print(prices)