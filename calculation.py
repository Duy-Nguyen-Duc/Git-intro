import math

def cal_rectangle_perimeter(a,b):
    return 2*(a+b)
def cal_circle_area(r):
    return math.pi*r**2
if __name__ == "__main__":
    f = int(input("Choose function: \n\
                  0. cal_rectangle_perimeter \n\
                  1. cal_circle_area \nPlease enter an integer:"))
    mult = int(input("Add multiplier:"))
    if f ==0:
        a = int(input("Input a:"))
        b = int(input("Input b:"))
        result = cal_rectangle_perimeter(a,b)
    elif f==1:
        r = int(input("Input r:"))
        result = cal_circle_area(r)
    else:
        result = "Wrong input"
    print(f"\n Result: {result * mult}")