# Accept student details using input()
roll_no = int(input("Enter Roll Number: "))
name = input("Enter Student Name: ")

mark1 = int(input("Enter Mark 1: "))
mark2 = int(input("Enter Mark 2: "))
mark3 = int(input("Enter Mark 3: "))

# Store marks in a tuple
marks = (mark1, mark2, mark3)

# Store student record in dictionary
student = {
    "Roll No": roll_no,
    "Name": name,
    "Marks": marks
}

# Display student details
print("\nStudent Details")
print("----------------")
print("Roll No :", student["Roll No"])
print("Name    :", student["Name"])
print("Marks   :", student["Marks"])

# Set operations
subjects_sem1 = set(input("\nEnter subjects of Semester 1 (comma separated): ").split(","))
subjects_sem2 = set(input("Enter subjects of Semester 2 (comma separated): ").split(","))

print("\nSet Operations")
print("----------------")
print("Union:", subjects_sem1 | subjects_sem2)
print("Intersection:", subjects_sem1 & subjects_sem2)
print("Difference (Sem1 - Sem2):", subjects_sem1 - subjects_sem2)
