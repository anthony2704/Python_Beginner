def ref_demo(x):
    print ("x= ", x) 
    print ("id= ", id(x))
    x=100
    print ("x= ", x)
    print ("id= ", id(x))

var = 20
print ("id(var)= ", id(var))
ref_demo(var)
print ("var= ", var)

# id(var)=  140717890472208
# x=  20
# id=  140717890472208
# x=  100
# id=  140717890474768
# var=  20