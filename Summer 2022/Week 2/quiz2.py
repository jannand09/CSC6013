def my_func(a,b):
    Dic = {}
    for i in range(10):
        Dic.append({a[i]: b[i]})
    x = input("Enter your index: ") 
    v = Dic.get(a[x], "absent")
    print("Index:", x, "Value:", v[x])
