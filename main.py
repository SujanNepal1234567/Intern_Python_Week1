from file_management import *
# import keyboard

def on_hot_key_1(): 
    exit()


if __name__ == '__main__':
    file_object= FileHandling()
    # keyboard.add_hotkey('q', on_hot_key_1)
    # keyboard.wait()
    choices = {1: "Find Absolute Path", 2:"List Directory content",
               3: "Rename File", 4: "Rename Folder", 5:"Copy File",
               6: "move folder", 7: "Create File", 8: "Create file with random text", 
               9: "View File", 10: "Delete File", 11: "Hide file", 12: "toggle hideen file", 13: "Make File Executable"}
    
    for i in choices: 
        print ("{}".format(i)+ ". " + choices[i])
    
    user_choice= input("Enter the value of the task you want to perform. ")
    match user_choice:
        case "1":
            file_name = input("\n Input File name you want the path of the directory")
            absolute_path = file_object.find_absolute_path(file_name)
            print ("\n the Absolute path of {} is {}".format(file_name, absolute_path))

        case "2": 
            file_object.list_directory_content()

        case "3": 
            file_name = input("\n Input File name you want to Change: ")
            new_name = input("\n Input the new File name you want it to be: \n" )
            file_object.rename_file(file_name,new_name)

        case "4": 
            folder_name = input("\n Input File name you want to Change: ")
            new_name = input("\n Input the new File name you want it to be: \n" )
            file_object.rename_file(folder_name,new_name)

        case "5": 
            file_name = input("\n Input File name you want to Copy: ")
            file_object.copy_file(file_name)

        case "6": 
            folder_name = input("\n Input Folder name you want to Copy: ")
            folder_destination = input("\n Input Folder destination you want to Copy it \
                                       to eg: /home/Desktop/bin... : ")
            abs= file_object.find_absolute_path(folder_name)
            file_object.move_folder(folder_name,folder_destination)

        case "7": 
            name_of_new_file= input("Enter new file name with extension: ")
            file_object.create_file(name_of_new_file)

        case "8":
            name_of_new_file= input("Enter new filename with extension \
                                    to generate file with random text: ")
            file_object.create_file_with_random_text(name_of_new_file)

        case "9": 
            name_of_new_file= input("Enter file to be viewed: ")
            file_object.view_file_only(name_of_new_file)

        case "10": 
            name_of_file_to_be_deleted = input("Enter new file name with extension to \
                                               be deleted: ")
            file_object.delete_file(name_of_file_to_be_deleted)

        case "11": 
            name_of_file_to_be_hidden = input("Enter new file name with extension to be \
                                              hidden: ")
            file_object.hide_file(name_of_file_to_be_hidden)

        case "12": 
            file_object.toggle_hidden_files()
            
        case "13":
            name_of_file_to_be_made_executable = input("Enter new file name with extension \
                                                        tochange permission to executable: ")
            file_object.make_file_executable(name_of_file_to_be_made_executable)


