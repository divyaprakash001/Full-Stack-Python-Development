import os
import pprint 
# # Get the filename corresponding  
# # to the controlling terminal 
# # of the process. 
# filename = os.ctermid() 
  
  
# # Print the filename corresponding  
# # to the controlling terminal 
# # of the process. 
# print(filename) 



# Python program to explain os.environ object  
  
# importing os module  
  
# Get the list of user's 
# environment variables 
env_var = os.environ 
  
# Print the list of user's 
# environment variables 
print("User's Environment variable:") 
pprint.pprint(dict(env_var), width = 1) 