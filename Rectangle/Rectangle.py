#Victor Cruzat CIS 261 Rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height
    
    def draw_rectangle(self):
        for _ in range(self.height):
            print("* " * self.width)

#Main Program
if __name__ == "__main__":
    while True:
        try:
            print("Rectangle Calculator")
        
            #Get user input for width and height
            width = int(input("Width:    "))
            height = int(input("Height:   "))
        
            #validate input
            if width <= 0 or height <= 0:
                print("Width and height must be positive integers.")
                continue
        
            #Create a rectangle Object
            rect = Rectangle(width, height)
            
            #Calculate and display perimeter and area
            print(f"Perimeter: {rect.calculate_perimeter()}")
            print(f"Area: {rect.calculate_area()}")
            
            #Draw the Rectangle
            rect.draw_rectangle()
            
            #Ask if the user wants to continue
            print("\nContinue? (y/n): ")
            continue_choice = input().strip().lower()
            if continue_choice != "y":
                print("Goodbye!")
                break
        
        except ValueError:
            print ("Please enter valid integers for width and height.")
        