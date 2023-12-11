import os

print('current working directory :: ',os.getcwd())

# os.chdir('E:\\Python Full Stack Development\\Python Programs')
# print('current working directory :: ',os.getcwd())

# os.chdir('../')
# print('current working directory :: ',os.getcwd())

# creating a directory
# os.mkdir(os.getcwd()+'\\OsModuleExample')  #create a directory and if the directory already exists, then it gives FileExistError

if not os.path.exists('OsModuleExample'):
    os.mkdir(os.getcwd()+'\\OsModuleExample')  

# directory = 'bihar'
# parent_dir = os.getcwd()
# # path = os.path.join(parent_dir,directory)
# path = parent_dir + '\\Bihar\\Ara\\Milki'
# os.makedirs(path)

# for dir in os.listdir():
#     print(dir)
#     print(os.getcwd())

# deleting directories


# os.remove('info.txt')
# os.rmdir('Bihar')  #delete dir if empty directory

# print(os.name)  #nt means window

# os.rename('old','new')
# os.rename('OsModuleExample','oskaexamplehai')

