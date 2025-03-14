#Imports
import customtkinter
import functions
import ui

class myButton(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(fg_color="purple", text="")
        
        

# Tabs
class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # add widgets on tabs
        self.label.grid(row=0, column=0, padx=100, pady=100)

# Main        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # add tabs
        self.tab_view = MyTabView(self)
        self.tab_view.add("Bible")
        self.tab_view.add("Notes")
        self.tab_view.add("Settings")
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        
app = App()
app.mainloop()