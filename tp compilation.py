from distutils import text_file

from tkinter import *

from tkinter import filedialog

import tkinter

win = Tk()

win.geometry('700x500+350+150')

win.resizable(False,False)

win.title('Automate recognition')

win.config(background='silver')

menubar = Menu(win)

win.config(menu=menubar)

 
file_menu = Menu(

    menubar,

    tearoff=0

)

 
def new_file():    

    if not Text_box1.edit_modified():      

        Text_box1.delete('1.0', END)

    else:        

        save_as()

        Text_box1.delete('1.0', END)  

    win.title('Automate recognition new')    

 

def openfile():   

    text_file = filedialog.askopenfile(filetypes = (("Text files", ".txt"), ("All files", ".*"))).name

    text_file = open(text_file, 'r')              
    content = text_file.read()
    Text_box1.delete('1.0', END)
    Text_box1.insert(END, content)

    """ else:      
        save_as()      
        openfile()  """

def savefile():    

    try:

        path = win.title().split('-')[1][1:]  
    except:

        path = ''

    if path != '':

        with open(path, 'w') as f:

            content = Text_box1.get('1.0', END)

            f.write(content)
    else:

        save_as()    

    Text_box1.edit_modified(0)

def save_as():    

    try:
        path = filedialog.asksaveasfilename(defaultextension=".*",title="save file" ,filetypes = (("Text document", ".txt"), ("All files", ".*")))

    except:

        return  

    with open(path, 'w') as f:
        f.write(Text_box1.get('1.0', END))

 

# add menu items to the File menu

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_command(label="Save as...", command=save_as)
file_menu.add_separator()

# add Exit menu item

file_menu.add_command(label='Exit',command=win.destroy)

# add the File menu to the menubar

menubar.add_cascade(label="File",menu=file_menu)

########################################################

# create the analyse menu

analyse_menu = Menu(menubar,tearoff=0)

analyse_menu.add_command(label='Lexicale')
analyse_menu.add_command(label='Syntaxique')
analyse_menu.add_command(label='Sementique')

# add the analyse menu to the menubar

menubar.add_cascade(label="Analyse",menu=analyse_menu)

lbl1= Label(win,text='^^^chose the type of analysing^^^',fg='black',bg='white',font=('Bodoni Mt',16,'italic bold underline'))
lbl1.place(x=10,y=10)
 

fr1 = Frame(width='250',height='260',bg='blue')
fr1.place(x=50,y=120)

fr2 = Frame(width='250',height='260',bg='blue')
fr2.place(x=420,y=120)

Text_box1= Text(fr1,width=25,height=15)
Text_box1.pack(padx=5,pady=5)

Text_box2= Text(fr2,width=25,height=15)
Text_box2.pack(padx=5,pady=5)
bt1 = Button(win,text='Okey', fg="white",bg='blue',font=20,width=30,cursor='hand2',activebackground='red',activeforeground='white')

bt1.place(x=210,y=400)

win.mainloop()
