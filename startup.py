import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


def Startup():
    win = tk.Tk()

    win.title('AstroCore Menu')
    win.iconbitmap('resources/title/icon.ico')
    win.geometry('600x400')

    canvas = tk.Canvas(win, width= 600, height= 400)
    canvas.pack()

    canvas.config(bg='black')

    img = Image.open("resources/title/title.png")
    img = img.resize((300, 80), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(300, 50, image=img)

    fullscreen = False
    nickname = "Hero"
    gender = "Male"
    sex = ('Kamarát', '(ky)')

    var3 = tk.StringVar(value=sex)
    var2 = tk.StringVar()
    var1 = tk.IntVar()

    style = ttk.Style()
    style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='1')
    style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('disabled', 'black')])

    def submit():
        global nickname
        global gender
        global fullscreen
        global player_info

        if var1.get() == 1:
            fullscreen = True
        else:
            fullscreen = False

        gender_select = gs.curselection()
        gender_select = ",".join([gs.get(i) for i in gender_select])
        if gender_select == "":
            gender = "Male"
        else:
            gender = gender_select

        if var2.get() == "":
            nickname = "Hero"
        else:
            nickname = var2.get()

        win.destroy()
        player_info = [True, f'{nickname}', f'{gender}']

    l_ns = tk.Label(win, text="Nickname:", bg='black', fg='white')
    l_ns.place(x=272, y=100)
    ns = tk.Entry(win, textvariable=var2, bg='gray',
                  fg='white', highlightthickness=0)
    ns.place(x=240, y=120)

    l_ns = tk.Label(win, text="Gender:", bg='black', fg='white')
    l_ns.place(x=279, y=150)
    gs = tk.Listbox(win, listvariable=var3, height=3, bg='gray',
                    fg='white', highlightthickness=0)
    gs.place(x=241, y=170)

    '''fs = tk.Checkbutton(win, text='Fullscreen', variable=var1, onvalue=1, offvalue=0,
                        bg='black', fg='white', selectcolor='gray',
                        activebackground='black', activeforeground='white', highlightcolor='black',
                        highlightthickness=0)
    fs.place(x=263, y=250)'''

    start = ttk.Button(text='Start', style='TButton', command=submit)
    start.place(x=220, y=300)

    canvas.mainloop()
    win.mainloop()
    return player_info
