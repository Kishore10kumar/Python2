
days = int(input("Enter the number of days late: "))

if days < 0:
    print("Invalid number of days!")

elif days == 0:
    fine = 0
    print("No fine. Book returned on time.")

elif days <= 5:
    fine = days * 0.50
    print("Fine: Rs.", fine)

elif days <= 10:
    fine = days * 1
    print("Fine: Rs.", fine)

elif days <= 30:
    fine = days * 5
    print("Fine: Rs.", fine)

else:
    print("Membership cancelled!")
