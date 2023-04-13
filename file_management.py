# basename function
import os
import stat
import subprocess
import shutil
import lorem
# from stat import 

class FileHandling: 
    def find_absolute_path(self, filename):
        out = os.path.abspath("{}".format(filename))
        return out
    # print(out)

    def list_directory_content(self):
        # absolute_path= find_absolute_path(filename)
        entries = os.listdir()
        for entry in entries:
            print(entry)

    # list_directory_content('/home/sujan/Desktop/MoneyHoney')
    # find_absolute_path("imposer.py")

    def rename_file(self, real_name, new_name):
        os.rename(real_name, new_name)

    def copy_file(self, filename):
        subprocess.call('cp {} {}'.format(filename, filename+'1'), shell=True)

    def copy_folder(self, src_path, dst_path):
        shutil.copy(src_path, dst_path)
        print('Copied')

    def move_folder(self, src_path, dst_path): 
        shutil.move(src_path, dst_path)
        print('Copied')

    def create_file(self, name):
        f = open("".format(name), "a+")

    # Create a text file with random text

    def create_file_with_random_text(self, name):
        f= open("".format(name),"a+")
        name.write(lorem.paragraph())

    # ● View contents of a file
    def view_file_only(self, name):
        a= open("".format(name),"r")
        print(a)

    # ● Delete file
    def delete_file(self, name):
        if os.path.exists(name):
            os.remove(name)
        else:
            print("The file does not exist")

    # ● Delete folder
    def delete_file(self, name):
        if os.path.exists("{}".format(name)):
            os.remove("{}".format(name))
        else:
            print("The file does not exist") 

    # ● Hide a folder
    def hide_file(self, name):
        new_name = '.'+ name
        os.rename (name , new_name)
        
    # ● Toggle viewing hidden folders
    def toggle_hidden_files(self):
        os.system('ls -a')

    # ● Make a file executable
    ''' stat.S_IXUSR= Owner has execute permission 
        && stat.S_IWUSR= Owner has write permission
        && stat.S_IRWXU= Owner has read permission.
        
        TO DO: 
        -This code Removes Group and Other's permission
        -Have to explicitly define those!'''
    def make_file_executable(self, name): 
        path = self.find_absolute_path(name)
        os.chmod(path,  stat.S_IXUSR| stat.S_IWUSR| stat.S_IRWXU )

    # ● Other operations you want to implement
        #so fun 

