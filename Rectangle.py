##William Sutton CIS261 Rectangle
#



class Rectangle:
        def __init__(self, height, width):
            self.height = height
            self.width = width

        def getArea(self):
            return self.height * self.width

        def getPerimeter(self):
            return (2 * self.height) + (2 * self.width)

        def printRectangle(self):
            edge_row = "* " * self.width
            center_row = "*" + '  '*(self.width - 2) + " *"
            rectangle_rows = [edge_row] + [center_row]*(self.height - 2) + [edge_row]
            print('\n'.join(rectangle_rows))

def main():
    print("Rectangle Calculator\n")
    choice = "y"
    while choice.lower() == "y":
        height = int(input("Height:    "))
        width = int(input("Width:     "))
        userRectangle = Rectangle(height, width)
        print("Perimeter:", userRectangle.getPerimeter())
        print("Area:     ", userRectangle.getArea())
        userRectangle.printRectangle()
        print()
        choice = input("Continue? (y/n): ")
        print()

if __name__ == "__main__":
     main()

