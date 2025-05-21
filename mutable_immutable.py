# mutable data types:
#    1.list 
#    2.set
#    3.dictionary
#    4.bytearray
#    5.array


# immutable data types :
#     1.string
#     2.integers
#     3.tuples
#     4.frozen set
#     5.bytes
#     6.boolean -> bool
#     7.floating-point number


# integers:

a = 5
print(a)

b = 6
print(b)

print(b is a) #true
print(b == a) #true

a = 10
b = a
print(a)
print(b)
print(b is a) #true
print(b == a) #true


a = 11


print(b is a) #false
print(b == a) #false

print(a)
print(b)

now a = 11  but the value of b = 10 
python check the ref of value aand assign ref to value not to key 


# string :

a = "hassan"
print(a)

b = "hassan"
print(b)

print(a is b)
print(a == b)

a = "nadeem"
b = a
print(a)
print(b)

a = "Nadeem"

print(a)
print(b)
print(a is b)
print(a == b)


p = "openai"
print(p[3 : 5]) #na
q = "".join(["open", "ai"]) #openai
print(p)
print(q)
print(p is q)  # ?
print(p == q)  # ?

q = "  ".join(["open", "ai"]) #open  ai
print(q)

# Tuples:

