print("hello world")
print(2)
print(4+4)
a = 5

print(a)


""" Multiline strings can be written
    using three "s, and are often used
    as comments
"""

# Everything is an object in Python
type(3)  #=>
type(3.0)  #=>
type("word") #=>
type(True) #=>
type(None)  #=>

# Math is what you would expect
print(1 + 1 )#=> 2
print(8 - 1 )#=> 7
print(10 * 2 )#=> 20
print(35 / 5 )#=> 7
print(2 ** 5 )#=> 32
print(5 % 3 )#=> 2 #mod

# Python automatically floors the results of Integer division (like Java)
5 / 2 #=> 2

# Use floats to fix this:
2.0     # This is a float
5.0 / 2.0 #=> 2.5

# Enforce precedence with parentheses
(1 + 3) * 2 #=> 8