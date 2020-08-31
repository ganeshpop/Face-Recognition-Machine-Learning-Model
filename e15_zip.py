#Join two tuples together:

a = ("One", "Two", "Three")
b = ("1", "2", "3")

x = zip(a, b)
print(tuple(x))

for (word, digit) in zip(a,b):
    print("{} {}".format(word, digit))