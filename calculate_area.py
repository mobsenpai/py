# def calcuate_area(l,b):
#     return l * b


# l = w 
def calculate_area(l, w=None):
    if not w:
        w = l
    return l * w
area1 = calculate_area(2,4)
area2 = calculate_area(2)
print(area1)
print(area2)
