from tkinter import *

def Data_Gui():
    GUI_Background_Color = "#408EC6"
    GUI_Text_Color = "#FFE77A"
    
    # ReUsable Menu Button Configurations
    Menu_Button_Height = 3
    Menu_Button_Width = 15
    Menu_Button_Font = ('', 16)
    Menu_Button_Background_Color = "#234E70"
    Menu_Button_Text_Color = "#FBF8BE"
    
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
        Words_Gui_Window.geometry("1150x500")
        Words_Gui_Window.configure(background=GUI_Background_Color)
        Words_Gui_Window.title(''' Letter Data Window  ''')
        
        Main_Menu_Greeting_Part_1 = Label(Words_Gui_Window, text='''Enter Your Letter Data Here Below''', fg=GUI_Text_Color, bg=GUI_Background_Color, font=('', 30), anchor=N)
        Main_Menu_Greeting_Part_1.grid(row=0, column=0, padx=100, pady=10,)
        
        Data_Entry_Input = Entry(Words_Gui_Window)
        Data_Entry_Input.grid(row=1, column=0)

        Main_Menu_Greeting_Part_2 = Label(Words_Gui_Window, text='''Now Selecet A Letter Data Manipulation Function Below''', fg=GUI_Text_Color, bg=GUI_Background_Color, font=('', 30))
        Main_Menu_Greeting_Part_2.grid(row=2, column=0, padx=100, pady=10,)

        # To Return Word Data in ALL UPPERCASE
        def UpperCase():
            Data = str(Data_Entry_Input.get())
            Desired_Result =  Data.upper()
            All_Caps_Text = Text(Words_Gui_Window, height=50)
            # All_Caps_Text.insert(1.0, f'''All Uppercase Text Below:\n\n{Desired_Result}''')
            All_Caps_Text.insert(1.0, f'''Final Result:\n\n{Desired_Result}''')
            All_Caps_Text.grid(row=6, column=0)
        
        All_Caps_Button = Button(Words_Gui_Window, text="All Caps", command=lambda: UpperCase())
        All_Caps_Button.grid(row=3, column=0, columnspan=10, pady=5,)



        # To Return Word Data in ALL UPPERCASE
        def LowerCase():
            Data = str(Data_Entry_Input.get())
            Desired_Result =  Data.lower()
            All_Lower_Text = Text(Words_Gui_Window, height=50)
            # All_Lower_Text.insert(1.0, f'''All Lowercase Text Below:\n\n{Desired_Result}''')
            All_Lower_Text.insert(1.0, f'''Final Result:\n\n{Desired_Result}''')
            All_Lower_Text.grid(row=6, column=0)
        
        All_Lower_Button = Button(Words_Gui_Window, text="All Lower", command=lambda: LowerCase())
        All_Lower_Button.grid(row=4, column=0, columnspan=10, pady=5)
        
        # To Return Word Data in ALL Title
        def Title():
            Data = str(Data_Entry_Input.get())
            Desired_Result =  Data.title()
            All_Title_Text = Text(Words_Gui_Window, height=50)
            # All_Title_Text.insert(1.0, f'''All Title Text Below:\n\n{Desired_Result}''')
            All_Title_Text.insert(1.0, f'''Final Result:\n\n{Desired_Result}''')
            All_Title_Text.grid(row=6, column=0)

        Title_Button = Button(Words_Gui_Window, text="All Title:", command=lambda: Title())
        Title_Button.grid(row=5, column=0, columnspan=10, pady=5)


    # Window for Number Data Manipulation
    def Numbers_Data_Func():
        Numbers_Gui_Window = Toplevel()
        Numbers_Gui_Window.geometry("800x700")
        Numbers_Gui_Window.configure(background=GUI_Background_Color)
        Numbers_Gui_Window.title(''' Number Data Window ''')
        
        Main_Menu_Greeting = Label(Numbers_Gui_Window, text=''' Enter Your Data Here Below''', fg=GUI_Text_Color, bg=GUI_Background_Color, font=('', 30))
        Main_Menu_Greeting.grid(row=0, column=0, padx=100, pady=100,)
        
        Data_Entry_Input = Entry(Numbers_Gui_Window, text='')
        Data_Entry_Input.grid(row=1, column=0)
        Data = float(Data_Entry_Input.get())
    
    
    # Window for All Data Manipulation
    def All_Data_Func():
        All_Data_Window = Toplevel()
        All_Data_Window.geometry("800x700")
        All_Data_Window.configure(background=GUI_Background_Color)
        All_Data_Window.title(''' All Data Window ''')
        
        Main_Menu_Greeting = Label(All_Data_Window, text=''' Enter Your Data Here Below''', fg=GUI_Text_Color, bg=GUI_Background_Color, font=('', 30))
        Main_Menu_Greeting.grid(row=0, column=0, padx=100, pady=100,)
        
        Data_Entry_Input = Entry(All_Data_Window, text='')
        Data_Entry_Input.grid(row=1, column=0)
        Data = float(Data_Entry_Input.get())
        
    
    Words_Gui_Button = Button(root, text="Letter Data", command=Letter_Data_Func, font=Menu_Button_Font, height=Menu_Button_Height, width=Menu_Button_Width, fg=Menu_Button_Text_Color , bg=Menu_Button_Background_Color)
    Words_Gui_Button.grid(row=1, column=0, pady=25)
    
    
    Numbers_Gui_Button = Button(root, text="Number Data", command=Numbers_Data_Func, font=Menu_Button_Font, height=Menu_Button_Height, width=Menu_Button_Width, fg=Menu_Button_Text_Color , bg=Menu_Button_Background_Color)
    Numbers_Gui_Button.grid(row=2, column=0, pady=25)
    
    
    All_Data_Gui_Button = Button(root, text="All Data", command=All_Data_Func, font=Menu_Button_Font, height=Menu_Button_Height, width=Menu_Button_Width, fg=Menu_Button_Text_Color , bg=Menu_Button_Background_Color)
    All_Data_Gui_Button.grid(row=3, column=0, pady=25)
    
    root.mainloop()
    
Data_Gui()
