
def vote():
    age=int(input("Enter Age: "))
    nationality=input("Enter Nationality: ")
    
    if age>17 and nationality =="Ghanaian":
        return print("Eligible")
    else:
        return print("Not Eligible")
    
    
vote()