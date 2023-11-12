from tkinter import *
from tkinter import ttk

def input_family(last_name):
        def find_family():
            family = entry.get()
            result_var.set(family)
            last_name.set(result_var.get())
            win.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Поиск телефона по фамилии')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()

        title = Label(win, text='Введите фамилию абонента', bg='#ffe4b5', font=60)
        title.pack()

        result_var = StringVar()
        entry = Entry(win, bg='white')
        entry.pack()

        frame1 = Frame(win, bg='blue')
        frame1.place(relx=0.30, rely=0.21, relwidth=0.5, relheight=0.1)

        btn = Button(frame1, text="Выполнить поиск", command=find_family)
        btn.pack()
        win.wait_window(win)
        return last_name.get()


def input_phone(phone_number):
        def find_family():
            family = entry.get()
            result_var.set(family)
            phone_number.set(result_var.get())
            win.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Поиск абонента по номеру телефона')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()

        title = Label(win, text='Введите телефон абонента', bg='#ffe4b5', font=60)
        title.pack()

        result_var = StringVar()
        entry = Entry(win, bg='white')
        entry.pack()

        frame1 = Frame(win, bg='blue')
        frame1.place(relx=0.30, rely=0.21, relwidth=0.5, relheight=0.1)

        btn = Button(frame1, text="Выполнить поиск", command=find_family)
        btn.pack()
        win.wait_window(win)
        return phone_number.get()


def create_contact():
        def create_people(family, name, phone, info):
            family = family.get()
            name = name.get()
            phone = phone.get()
            info = info.get()
            line = family + "," + name + "," + phone + "," + info
            result_var.set(line)
            win.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Создание контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()

        title = Label(win, text='Введите данные абонента', bg='#ffe4b5', font=60)
        title.pack()

        result_var = StringVar()

        title = Label(win, text='Введите фамилию абонента', bg='#ffe4b5', font=70)
        title.pack()
        family = Entry(win, bg='white')
        family.pack()

        title = Label(win, text='Введите имя абонента', bg='#ffe4b5', font=60)
        title.pack()
        name = Entry(win, bg='white')
        name.pack()

        title = Label(win, text='Введите телефон абонента', bg='#ffe4b5', font=60)
        title.pack()
        phone = Entry(win, bg='white')
        phone.pack()

        title = Label(win, text='Введите описание', bg='#ffe4b5', font=60)
        title.pack()
        info = Entry(win, bg='white')
        info.pack()

        frame1 = Frame(win, bg='blue')
        frame1.place(relx=0.35, rely=0.48, relwidth=0.3, relheight=0.1)

        btn = Button(frame1, text="Создать", command=lambda: create_people(family, name, phone, info))
        btn.pack()
        win.wait_window(win)
        return result_var.get()



# family.set(result_var.get())
# name.set(result_var.get())
# phone.set(result_var.get())
# info.set(result_var.get())