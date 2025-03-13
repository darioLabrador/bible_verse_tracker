#Imports
import main
import ui
import enum

# Functions
# TODO


# Switch Button to pick theme between Dark and Light    
def change_theme():
    
    if customtkinter.get_appearance_mode() == "dark":
        customtkinter.set_appearance_mode("light")
        
    else:
        customtkinter.set_appearance_mode("dark")
    
    

def create_list():
    pass

# TODO
def list_item():
    pass

# TODO
def delete_list():
    pass

# TODO
def delete_item():
    pass