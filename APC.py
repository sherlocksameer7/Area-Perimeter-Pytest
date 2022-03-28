def area_square(s):
    return s ** 2


def perimeter_rectangle(l, b):
    result = 2 * (l + b)
    return result


def area_rectangle(l, b):
    return l * b

if __name__ == "__main__":
    while True:

        print("select an option :")
        print("1. Area of square :")
        print("2. Perimeter of rectangle :")
        print("3. Area of rectangle :")
        print("4. Exit")

        Choice = int(input("Enter the option : "))

        if Choice == 1:
            s = int(input("Enter the Side of Square :"))

            Square_area = area_square(s)
            print("Area of Square: ", Square_area)


        elif Choice == 2:
            l = int(input("Enter the Length of Rectangle :"))
            b = int(input("Enter the Breadth of Rectangle :"))

            Rect_Peri = perimeter_rectangle(l, b)
            print("Perimeter of Rectangle: ", Rect_Peri)


        elif Choice == 3:
            l = int(input("Enter the Length of Rectangle :"))
            b = int(input("Enter the Breadth of Rectangle :"))

            Rect_Area = area_rectangle(l, b)
            print("Area of Rectangle: ", Rect_Area)


        elif Choice == 4:
            break


        else:
            print("Invalid Option !! ")
