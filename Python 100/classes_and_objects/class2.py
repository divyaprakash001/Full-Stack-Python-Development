class Users:
    # constructor
    def __init__(self,name,age,fname,mname,gender,address):
        print('you are in Users constructor')
        self.name=name
        self.age=age
        self.fname=fname
        self.mname=mname
        self.gender=gender
        self.address=address

    @property
    def getName(self):
        return self.name
    
    @getName.setter
    def setName(self,new_Name):
        self.name=new_Name
        
    
    def UserInfo(self):
        try:
            print(f'Hey {self.name} ! Welcome to my application.')
            print('1 : Details')
            print('2 : Exit')
            option = int(input('Enter you option here :: '))
            match option:
                case _ if option == 1:
                    print(f'Name :: {self.name}')
                    print(f'Age :: {self.age}')    
                    print(f'FName :: {self.fname}')
                    print(f'MName :: {self.mname}')
                    print(f'Gender :: {self.gender}')
                    print(f'Address :: {self.address}')
                case _ if option == 2:
                    print('Thanks for using this application')
                case _ :
                    print("sorry wrong input")

        except Exception as e:
            print('something went wrong',e) 

   
            

rohit = Users('Rohit',24,'Rohan','Mohani','Male','Behra')
rohit.UserInfo()
print("-------------------")
print(rohit.getName) #getting the name
rohit.setName='mohit' #setting the name
print(rohit.getName) #getting the name again
