# Multiple Return Values

def arithmetic_operations(a,b):
    sum = a+b
    diff =a-b
    prod = a*b
    quot = a/b
    return(sum,diff,prod,quot) #return as tupple

print(arithmetic_operations(2,4))

# return area of rectangle as tupple
def rectangle_properties(l,b):
    area = l*b
    peri = 2*(l+b)
    return(area,peri) #return as tupple

print(rectangle_properties(2,3))
