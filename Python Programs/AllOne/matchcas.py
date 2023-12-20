age = int(input("Enter you age :: "))
match age:
    case 0:
        print("your age is too low")
    case _ if age < 18:  #this is default match case
        print("your age is too low")
    case _ if age >= 18 and age <= 60:  #this is default match case
        print("your age is perfect")
    case _ if age > 60:  #this is default match case
        print("your age is too high")
    case _ :  #this is default match case
        print("wrong input")
    
    
    
