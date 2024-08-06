def cal_rectangle_perimeter(a,b):
    return 2*(a+b)

if __name__ == "__main__":
    f = int(input("Choose function: \n\
                  0. cal_rectangle_perimeter \n\
                  "))
    if f ==0:
        a = int(input("Input a:"))
        b = int(input("Input b:"))
        result = cal_rectangle_perimeter(a,b)
    else:
        result = "Wrong input"
    print(f"\n Result: {result}")