import shutil, os, sys

#For Ubuntu

def get_subdir():
   return [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

def get_files():
    return [e for e in os.listdir(os.getcwd()) if os.path.isfile(e)]

def sort_files():
    for filename in get_files():
        find = False
        #print(filename)
        for foldername in get_subdir():
            #print(foldername)
            if foldername in filename:
                #print('success')
                shutil.move(os.getcwd()+'/'+filename, os.getcwd()+'/'+foldername)
                find = True
                break
        if find == False:
            user_input = input(filename+' does not match with any existing folder. Do you want to create a new folder? (y/n/end)\n')
            if user_input == 'y':
                user_folder = input('Name your new folder: ')
                os.makedirs(os.getcwd()+'/'+user_folder)
                shutil.move(os.getcwd()+'/'+filename, os.getcwd()+'/'+user_folder)
            elif user_input == 'n':
                pass
            elif user_input == 'end':
                sys.exit()
            else:
                print('Command not recognized')

sort_files()
