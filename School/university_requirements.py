# University
# Entry requirements
# Age must be >= 18
# Average grade must be >= 8
# Must have a certificate
age = int(input("Enter your age:"))
average_grade = bool(input("Enter your average grade:"))
certificate = input("Do you have any certificate:")

if (age >= 18) and (average_grade >= 8) and (certificate.lower() == yes):
    print("You meet the requirements, to join the university.")

else:
    print("Rejected")