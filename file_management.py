"""
    Class module for using os module to handle files
"""
# basename function
import os
import stat
import subprocess
import shutil
import lorem
# from stat import

class FileHandling:
    """Class to have methods for handling documents on a directory"""

    def find_absolute_path(self, filename):
        """Finds absolute path ie from home folder.

        Args:
            filename (string): Filename which path is to be found.

        Returns:
            out (string): Pathname of format /home/Desktop....

        Raises:
            ErrorType:

        """
        out = os.path.abspath(f"{filename}")
        return out

    def list_directory_content(self):
        """lists the current folder of the directory.
        Returns:
            Prints the list of directory content 
        Raises:
            ErrorType:
        """
        # absolute_path= find_absolute_path(filename)
        entries = os.listdir()
        for entry in entries:
            print(entry)
    # list_directory_content('/home/sujan/Desktop/MoneyHoney')
    # find_absolute_path("imposer.py")

    def rename_file(self, real_name, new_name):
        """Rename file in the current directory.
         Args:
            real_name (str): Used for getting real name of the file in the same directory.
            new_name (str): Used for getting new name of the file in the same directory.

        Returns:
           Renames the real_name as new_name 

        Raises:
            ErrorType:
            
        """
        os.rename(real_name, new_name)

    def copy_file(self, filename):
        """Copy file in the current directory and saves file to the same directory.

        Args:
            filename (str): Used for getting real name of the file in the same 
            directory that is copied.

        Returns:
           Nothing

        Raises:
            ErrorType:
            
        """
        subprocess.call(f"cp {filename} {filename+'1'}", shell=True)

    def copy_folder(self, src_path, dst_path):
        """Copy folder in the current directory and saves folder to the input directory.

        Args:
            src_path (str): Takes the folder name as input
            dst_path (str): Takes the folder path as input for where it is to be copied 

        Returns:
            Prints copied when done 

        Raises:
            ErrorType:
        """
        shutil.copy(src_path, dst_path)
        print('Copied')

    def move_folder(self, src_path, dst_path):
        """Move folder in the current directory and saves folder to the input directory.

        Args:
            src_path (str): Takes the folder name as input
            dst_path (str): Takes the folder path as input for where it is to be copied 

        Returns:
            Prints copied when done 

        Raises:
            ErrorType:
            
        """
        shutil.move(src_path, dst_path)
        print('Copied')

    def create_file(self, name):
        """Creates file in the current directory and saves the file without any text

        Args:
            name (str): Takes the name of the file to be made

        Raises:
            ErrorType:
            
        """
        # open(name, "a+")
        with open(f'{name}', "a+", encoding="utf8"):
            pass

    # Create a text file with random text

    def create_file_with_random_text(self, name):
        """Creates file in the current directory and saves the file with a paragraph of lorem text

        Args:
            name (str): Takes the name of the file to be made

        Raises:
            ErrorType:
            
        """
        # open(name, "a+")
        # name.write(lorem.paragraph())
        with open(f'{name}', "a+", encoding="utf8") as file:
            file.write(lorem.paragraph)

    # ● View contents of a file
    def view_file_only(self, name):
        """Views file in the current directory and prints their text

         Args:
            name (str): Takes the name of the file to be viewed

        Returns:
           all the text of the file name given

        Raises:
            ErrorType:
            
        """
        # a= open("".format(name),"r")
        # print(a)
        with open(f'{name}', "r", encoding="utf8") as file:
            file_data= file.read()
            print(file_data)

# ● Delete file
    def delete_file(self, name):
        """Delete file in the current directory 

        Args:
            name (str): Takes the name of the file to be deleted

        Returns:
           Deleted message if deleted. If file doesnt exist, sends a no file case

        Raises:
            ErrorType:
                -File doesnt exist: Whn file not found then raises this in print 
            
        """
        if os.path.exists(name):
            os.remove(name)
        else:
            print("The file does not exist")

    # ● Hide a folder
    def hide_file(self, name):
        """Hides a folder in the current directory by adding '.' infront of its name

        Args:
            name (str): Takes the name of the file to be hidden

        """
        new_name = '.'+ name
        os.rename (name , new_name)

    # ● Toggle viewing hidden folders
    def toggle_hidden_files(self):

        """Shows hidden folder in the current directory 

        Returns:
            List of directory of the current directory
        """
        os.system('ls -a')

    # ● Make a file executable
    def make_file_executable(self, name):
        ''' Make a file executable- only user!

        Args: 
        name= Name of the file to be changed
        stat.S_IXUSR= Owner has execute permission 
        && stat.S_IWUSR= Owner has write permission
        && stat.S_IRWXU= Owner has read permission.
        
        TO DO: 
        -This code Removes Group and Other's permission
        -Have to explicitly define those!
        '''

        path = self.find_absolute_path(name)
        os.chmod(path,  stat.S_IXUSR| stat.S_IWUSR| stat.S_IRWXU )
    # ● Other operations you want to implement
        #so fun
