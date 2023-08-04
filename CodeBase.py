from multiprocessing import Value
from tkinter import *
from Logical_Functions import *

def Data_Gui():
    GUI_Background_Color = "#386150"
    GUI_Text_Color = "#c5e384"
    
    # ReUsable Menu Button Configurations
    Menu_Button_Height = 3
    Menu_Button_Width = 15
    Menu_Button_Font = ('', 16)
    Menu_Button_Background_Color = "#679289"
    Menu_Button_Text_Color = "#fffaca"
    
    # Tkinter Setup
    root = Tk()
    root.geometry("1280x960")
    root.configure(background=GUI_Background_Color)
    root.title(''' SH Data Tool ''')
    
    # Initial Start Menu Message
    Main_Menu_Greeting = Label(root, text='''Welcome To Data Manipulation Tool\nPick the Data Type Below To Work With''', fg=GUI_Text_Color, bg=GUI_Background_Color, font=('', 30))
    Main_Menu_Greeting.grid(row=0, column=0, padx=320, pady=100,)
    
    
    # Window for Letter Data Manipulation
    def Letter_Data_Func():
        Words_Gui_Window = Toplevel()
        Words_Gui_Window.geometry("1280x960")
        Words_Gui_Window.configure(background=GUI_Background_Color)
        Words_Gui_Window.title(''' Letter Data Window  ''')
        
        Main_Menu_Greeting = Label(Words_Gui_Window, text=''' Enter Your Data Here Below''', fg=GUI_Text_Color, bg=GUI_Background_Color, font=('', 30))
        Main_Menu_Greeting.grid(row=0, column=0, padx=320, pady=100,)
        
        UpperCase_Button = Button(Words_Gui_Window, text= "All Uppercase", command=All_Upper_Func, font=Menu_Button_Font, height=Menu_Button_Height, width=Menu_Button_Width, fg=Menu_Button_Text_Color, bg=Menu_Button_Background_Color)
        UpperCase_Button.grid(row=1, column=0)
        
    
    # Window for Number Data Manipulation
    def Numbers_Data_Func():
        Numbers_Gui_Window = Toplevel()
        Numbers_Gui_Window.geometry("1280x960")
        Numbers_Gui_Window.configure(background=GUI_Background_Color)
        Numbers_Gui_Window.title(''' Number Data Window ''')
        
        Main_Menu_Greeting = Label(Numbers_Gui_Window, text=''' Enter Your Data Here Below''', fg=GUI_Text_Color, bg=GUI_Background_Color, font=('', 30))
        Main_Menu_Greeting.grid(row=0, column=0, padx=320, pady=100,)
        
        Input_Box = Entry(Numbers_Gui_Window)
    
    
    # Window for All Data Manipulation
    def All_Data_Func():
        All_Data_Window = Toplevel()
        All_Data_Window.geometry("1280x960")
        All_Data_Window.configure(background=GUI_Background_Color)
        All_Data_Window.title(''' All Data Window ''')
        
        Main_Menu_Greeting = Label(All_Data_Window, text=''' Enter Your Data Here Below''', fg=GUI_Text_Color, bg=GUI_Background_Color, font=('', 30))
        Main_Menu_Greeting.grid(row=0, column=0, padx=320, pady=100,)
        
    
    Words_Gui_Button = Button(root, text="Letter Data", command=Letter_Data_Func, font=Menu_Button_Font, height=Menu_Button_Height, width=Menu_Button_Width, fg=Menu_Button_Text_Color , bg=Menu_Button_Background_Color)
    Words_Gui_Button.grid(row=1, column=0, pady=25)
    
    
    Numbers_Gui_Button = Button(root, text="Number Data", command=Numbers_Data_Func, font=Menu_Button_Font, height=Menu_Button_Height, width=Menu_Button_Width, fg=Menu_Button_Text_Color , bg=Menu_Button_Background_Color)
    Numbers_Gui_Button.grid(row=2, column=0, pady=25)
    
    
    All_Data_Gui_Button = Button(root, text="All Data", command=All_Data_Func, font=Menu_Button_Font, height=Menu_Button_Height, width=Menu_Button_Width, fg=Menu_Button_Text_Color , bg=Menu_Button_Background_Color)
    All_Data_Gui_Button.grid(row=3, column=0, pady=25)
    
    root.mainloop()
    
Data_Gui()