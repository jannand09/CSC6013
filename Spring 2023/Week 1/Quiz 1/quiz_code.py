#Question 3

x = 0
buf = "high hopes"

for c in buf:
    x = x + 1

print(x)

#Question 4

a = [[1,2,3],[4,5,6],[7,8,9]]

y = a[2][0]

print(y)

#Question 5

buf1 = "The quick brown fox"
s = buf1[3:5]+buf1[16:]
print(s)


#Question 7
def func(x):
    for i in range(x):
        print("good luck")


func(5-2)


#Question 9

def my_func(x, y1=5, z=7):
    return x+y1+z


x1=10
z=2
x1=my_func(x1)+my_func(x1,z)+my_func(3,4,5)

print(x1)