#Team: Nihil Rajendran
#course: CS 701/GB 735, Dr. Rajeev
#Date: 08/01/21
#Programming Assignment: 1
#Program Inputs: length, width, height
#Program Outputs: Total area in square feet, gallons of primer, and gallons of paint

#Asks user to input length
length = int(float(input("Enter length: ")))

#Asks user to input width
width = int(float(input("Enter width: ")))

#Asks user to input height
height = int(float(input("Enter height: ")))

#Calculates total area of room excluding floor
total_area = (length * width) + (2*(height * width)) + (2*(height * length))

#Prints total area of the room excluding floor for the user
print("Area is :", total_area, "square feet")

#Prints gallons of primer needed
primer = print((total_area//200) , "gallons of primer is needed ")

#Prints gallons of paint needed
paint = print(total_area//350 , "gallons of paint is needed")