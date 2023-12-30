from DBHelper import DBHelper

def main():
    while(True):
        print('***********WELCOME*************\n')
        helper = DBHelper()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to fetch one user")
        print("PRESS 3 to fetch all user")
        print("PRESS 4 to delete user")
        print("PRESS 5 to update user")
        print("PRESS 6 to exit the program\n")

        try:
            choice = int(input('Enter your choice :: '))
            if choice==1:
                # insert user
                userid = int(input('Enter userId :: '))
                username = input('Enter userName :: ')
                userphone = input('Enter phone :: ')
                helper.insert_data(userid,username,userphone)

            elif choice == 2:
                # fetch one user
                userid = int(input('Enter userId :: '))
                helper.fetch_by_id(userid)

            elif choice == 3:
                # fetch all users
                helper.fetch_all()

            elif choice == 4:
                # delete user
                userid = int(input('Enter userId :: '))
                helper.delete_data(userid)
                pass
            elif choice == 5:
                # update user
                userid = int(input('Enter userId :: '))
                newname = (input('Enter new name :: '))
                newphone = (input('Enter new phone :: '))
                helper.updata_data(userid,newname, newphone)

            elif choice == 6:
                # exit
                print('----------Thanks for using my application------------')
                break
            else:
                print('Invalid input !! Try again !!')

        
        except Exception as e:
            print(e)
            print('Wrong input !!!')

if __name__ == '__main__':
    main()