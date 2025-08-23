# if no width provided then w=l
def area(l,w = -1):
    if w == -1:
        w=l
    return l * w

print("AREA: ", area(5,2))
print("AREA: ", area(5))
