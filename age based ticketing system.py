'''
No Fare : for children under 6
Half Ticket : for individuals aged above 6 and less than 18
Full Ticket : for individuals aged above 18

Fare is 50 if age is above 6 and less than 18.
Fare is 75 if age is 60 or above.
Fare is 100 rupees if age is below 60.
'''

def determine_ticket_category_and_fare(age):

    if age <= 6:
        print("No Fare")
        print("Total Fare = 0")
    elif age > 6 and age < 18:
        print("Half Ticket")
        print("Total Fare = 50")
    else:
        print("Full Ticket")
        if age < 60:
            print("Total Fare = 100")
        else:
            print("Total Fare = 75")

if __name__ == "__main__":
    age = int(input())
    determine_ticket_category_and_fare(age)