a = 1
b = 2
if a < b:
    print("a is less than b ")
    print("a is defintely less than b ")
print("not sure if a is less than b ")

b = 1
if a == b :
    print("both are equal")


x = 1
y = 2

if x == y :
    print("x and y are equal")
else:
    print("x and y are not equal")


x = 2
y = 1


if x < y :
    print("x is less than y")
elif x ==  y:
    print("x is equal to y")
else:
    print("x is greter than y")

g = 7
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")


name = "muni"
height_m = 2
weight_g = 90

bmi = weight_g / (height_m ** 2)

print("bmi")

if bmi < 25 :
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is  overweight")