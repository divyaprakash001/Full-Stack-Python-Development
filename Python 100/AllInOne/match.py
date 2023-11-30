age=int(input("Enter your age to check your eligibility :: "))

match age:
    case 0 :
        print("Sorry, You are zero")
    case _ if age<18:
        print("Oh! You are not eligible for voting")
    case _ if age>=18 and age <=60:
        print("Yeah! You are eligible for voting")
    case _ if age > 60:
        print("Oh! You are too old to vote.")