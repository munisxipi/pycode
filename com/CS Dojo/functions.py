def function1():
    print("test function")
    print("testing function 2")
print("this is outside function")

function1()

def function2(x):
    return 2*x

print(function2(3))
print(function2(20))
#print(function2())


def function3(x, y):
    return x + y

print(function3(2, 6))

name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70


name3 = "YK"
height_m3 = 2.5
weight_kg3 = 160


def bmi_calculator(name, height_m, weight_kg) :
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name+ "is overweight"
    
result1= bmi_calculator(name1,height_m1, weight_kg1)

result2 = bmi_calculator(name2, height_m2, weight_kg2)

result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print( result2)
print(result3)