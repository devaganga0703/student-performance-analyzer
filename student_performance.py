
name = input("Enter student name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

average = (mark1 + mark2 + mark3) / 3

print("\nStudent Performance Report")
print("Name:", name)
print("Average:", round(average, 2))

if average >= 90:
    print("Performance: Excellent")
elif average >= 75:
    print("Performance: Very Good")
elif average >= 50:
    print("Performance: Good")
else:
    print("Performance: Needs Improvement")
