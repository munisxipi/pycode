a = [1, 2, 3, 4]
print(a)

a.append(5)
print(a)
a.remove(1)
print(a)

# mixed type

a.append("hello")

print(a)

a.append([6, 7])
print(a)

a.pop()
print(a)

a.pop()
print(a)


print(a[0])

a[0] = 100

print(a)

b = [ "banana", "apple","ms"]
print(b)

temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

print("test")

