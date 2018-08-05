import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import random
import pyperclip 




window = tk.Tk()
class App:
    ## the main Functions
    def about(self):
        messagebox.showinfo('About','The app is written by Soufiane\n Tkinter')
    def exit(self):
        window.quit()


    def copy_clipbaord(self):
        c = pyperclip.copy(self.text_field.get('1.0','end'))
        p = pyperclip.paste()
        messagebox.showinfo('info','Something is copied : ' + p)


    def generate(self,n=1,letters=None,numbers=None,symbols=None):

        LETTERS = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
        NUMBERS = '0123456789'
        SYMBOLS = '@-!#$%+*~&¿?;:/='

        try:
                n = int(n)
                if letters ==0:
                    LETTERS = ''
                if numbers ==0:
                    NUMBERS = ''
                if symbols == 0:
                    SYMBOLS = ''
                result =''
                for i in range(n):
                        result += random.choice(list(LETTERS)+list(NUMBERS)+list(SYMBOLS))
                self.text_field.delete('1.0','end')
                self.text_field.insert('1.0',result)

        except ValueError :
            messagebox.showinfo('Error','You can only use numbers')

    ## The layout of the App

    def __init__(self,root):
        root.title('Password generator')
        root.resizable(False,False)
        root.iconbitmap('lock.ico')
        self.the_menu(root)
        self.up_frame(root)
        self.middle_frame(root)
        self.bottom_frame(root)


    def the_menu(self,root):
        main_menu = tk.Menu(root)
        file_menu=tk.Menu(main_menu,tearoff = False)
        help_menu = tk.Menu(main_menu,tearoff = False)



        main_menu.add_cascade(menu = file_menu,label = 'File')
        file_menu.add_command(label = 'Exit',command = lambda : self.exit())
        main_menu.add_cascade(menu =help_menu ,label = 'Help')
        help_menu.add_command(label = 'Check my github ')
        help_menu.add_command(label = 'About',command = lambda : self.about())

        root.config(menu =main_menu)



    def up_frame(self,root):

        self.title_image = Image.open('Pass_gen_title.png')
        self.title_show = ImageTk.PhotoImage(self.title_image)
        image_1 = tk.Label(root,image = self.title_show)
        image_1.pack(fill = 'both',expand = 'yes')

    def middle_frame(self,root):

        mini_window = tk.LabelFrame(root,text ='Your Password Generator Options:' )

        ask_for_chr_label =tk.Label(mini_window,
            text = 'Enter the number of characters (between 8 and 500) for your password :')
        ask_for_chr_label.grid(row = 0,column = 0)
        num_var = tk.IntVar()
        num_entry = tk.Entry(mini_window,textvariable = num_var)
        num_entry.grid(row = 1,column = 0)
        
        i = 0
        self.letter_var = tk.IntVar()
        self.number_var = tk.IntVar()
        self.symbol_var = tk.IntVar()
        d = {'letter': self.letter_var,'numbers':self.number_var,'symbols':self.symbol_var}
        for name,var in d.items():
            check_box = tk.Checkbutton(mini_window,text ='Password has {}?'.format(name),variable = var,state = 'active')
            check_box.grid(row=i+2,column=0,sticky ='W')
            i+=1
        ## generate the password
        generate_button = ttk.Button(mini_window,text='Generate password!!',
            command =lambda : self.generate(num_entry.get(),self.letter_var.get(),self.number_var.get(),self.symbol_var.get()))
        generate_button.grid(row = 5,column = 0,padx =10,pady= 5)

        
        mini_window.pack(padx = 10,pady = 5)


    def bottom_frame(self,root):

        new_pass_window = tk.LabelFrame(root,text ='Your New Password: ')

        new_pass_label = tk.Label(new_pass_window,text = 'Edit your new password if needed. Try to keep as generated.')
        new_pass_label.grid(row = 0,column = 0)
        self.text_var = tk.StringVar()
        self.text_field =tk.Text(new_pass_window, width = 42, height = 5)
        self.text_field.grid(row = 1,padx = 10,pady = 5)

        copy_button = ttk.Button(new_pass_window,text = 'Copy to ClipBoard',command = lambda: self.copy_clipbaord())
        copy_button.grid(row = 2,column = 0)

        new_pass_window.pack()



app = App(window)



window.mainloop()