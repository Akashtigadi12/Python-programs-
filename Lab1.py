a) Develop a python program to read student details Name, USN and Marks in the three subjects. # Display the student details , total marks and percentage with suitable messages
name = input("Enter the student name: ")
usn = input("Enter the student USN: ")
phy = int(input("Enter the marks obtained in Physics: ")) che = int(input("Enter the marks obtained in Chemistry: ")) mat = int(input("Enter the marks obtained in Mathematics: ")) max_marks = 300
print(30 * "*")
# Display the student details print("Name of the Student:", name) print("Student USN:", usn) print(30 * "*")
# Calculate the total marks total=phy +che+mat
print("The total marks scored by the student in Physics", phy, "Chemistry", che, "Mathematics", mat, "is", total) print(30 * "*")
# Calculate percentage
percent = (total/max_marks) * 100
print("Percentage of the Student:", round(percent))
Enter the student name: Amit
Enter the student USN: 2JI22CS001
Enter the marks obtained in Physics: 84
Enter the marks obtained in Chemistry: 65
Enter the marks obtained in Mathematics: 73
******************************
Name of the Student: Amit
Student USN: 2JI22CS001
******************************
The total marks scored by the student in Physics 84 Chemistry 65 Mathematics 73 is 222 ******************************
Percentage of the Student: 74
# (b) Develop a program to reas the name and year of birth of a person. Display whether the person is a senior citizen or not. import datetime
name = input("Enter the name of the person: ")
birth_year = int(input("Enter the year of birth of the person: "))
today = datetime.date.today() year = today.year
age = year - birth_year
if age >= 60:
print(name + "is a senior citizen")
else:
print(name + "is not a senior citizen")
Enter the name of the person: Rohit
Enter the year of birth of the person: 1955 Rohitis a senior citizen
 
