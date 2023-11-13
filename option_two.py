from tkinter import *
from tkinter import ttk


# 2. Найти телефон по фамилии
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


# 3. Найти абонента по номеру телефона
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

# 4. Добавить абонента в справочник
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



# 5. Изменить контакт
def find_contact_to_change():
        def input_family():
            result_var.set(1)
            win.destroy()
        def input_name():
            result_var.set(2)
            win.destroy()
        def input_phone():
            result_var.set(3)
            win.destroy()
        def input_info():
            result_var.set(4)
            win.destroy()
        
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Изменение контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()

        result_var = IntVar()

        title = Label(win, text='По какому критерию хотите произвести поиск?', bg='#ffe4b5', font=60)
        title.pack()

        frame1 = Frame(win, bg='#ffe4b5')
        frame1.place(relx=0.35, rely=0.28, relwidth=0.3, relheight=0.2)
        btn = Button(frame1, text="По фамилии", command=lambda: input_family())
        btn.pack()
        frame2 = Frame(win, bg='#ffe4b5')
        frame2.place(relx=0.35, rely=0.38, relwidth=0.3, relheight=0.2)
        btn = Button(frame2, text="По имени", command=lambda: input_name())
        btn.pack()
        frame3 = Frame(win, bg='#ffe4b5')
        frame3.place(relx=0.35, rely=0.48, relwidth=0.3, relheight=0.2)
        btn = Button(frame3, text="По номеру телефона", command=lambda: input_phone())
        btn.pack()
        frame4 = Frame(win, bg='#ffe4b5')
        frame4.place(relx=0.35, rely=0.58, relwidth=0.3, relheight=0.2)
        btn = Button(frame4, text="По описанию", command=lambda: input_info())
        btn.pack()
        win.wait_window(win)
        return result_var.get()


def contact_change():
        def your_input():
            result_var.set(your_choice.get())
            win.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Изменение контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = StringVar()
        title = Label(win, text='Введите свой запрос', bg='#ffe4b5', font=60)
        title.pack()
        your_choice = Entry(win, bg='white')
        your_choice.pack()
        frame = Frame(win, bg='#ffe4b5')
        frame.place(relx=0.35, rely=0.28, relwidth=0.3, relheight=0.2)
        btn = Button(frame, text="Ввод", command=lambda: your_input())
        btn.pack()
        win.wait_window(win)
        return result_var.get()

def many_find(found_people):
        def choice():
            result_var.set(your_choice.get())
            win.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Найдено больше одного запроса!')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('800x800')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = IntVar()
        for i in range(len(found_people)):
            line = ', '.join('{} {}'.format(key, val) for key, val in sorted(found_people[i].items()))
            title = Label(win, text=f"{i+1}.  {line}", bg='#ffe4b5', font=60)
            title.pack()
        title = Label(win, text='Ввведите номер нужного вам контакта', bg='#ffe4b5', font=60)
        title.pack()
        your_choice = Entry(win, bg='white')
        your_choice.pack()
        frame = Frame(win, bg='#ffe4b5')
        frame.place(relx=0.35, rely=0.28, relwidth=0.3, relheight=0.2)
        btn = Button(frame, text="Ввод", command=lambda: choice())
        btn.pack()
        win.wait_window(win)
        return result_var.get()


def not_found():
        def yes_function(window):
            result_var.set(True)
            window.destroy()
        def no_function(window):
            result_var.set(False)
            window.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Поиск не дал результата!')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = BooleanVar()
        title = Label(win, text='Хотите попробовать снова?', bg='#ffe4b5', font=60)
        title.pack()
        frame = Frame(win, bg='white')
        frame.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1)
        btn = Button(frame, text="Да", command=lambda: yes_function(win))
        btn.pack()
        btn = Button(frame, text="Нет", command=lambda: no_function(win))
        btn.pack()
        win.wait_window(win)
        return result_var.get()


def choice_contact_to_change():
        def input_family():
            result_var.set(1)
            win.destroy()
        def input_name():
            result_var.set(2)
            win.destroy()
        def input_phone():
            result_var.set(3)
            win.destroy()
        def input_info():
            result_var.set(4)
            win.destroy()
        
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Изменение контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()

        result_var = IntVar()

        title = Label(win, text='Что вы хотите изменить?', bg='#ffe4b5', font=60)
        title.pack()

        frame1 = Frame(win, bg='#ffe4b5')
        frame1.place(relx=0.35, rely=0.28, relwidth=0.3, relheight=0.2)
        btn = Button(frame1, text="Фамилию", command=lambda: input_family())
        btn.pack()
        frame2 = Frame(win, bg='#ffe4b5')
        frame2.place(relx=0.35, rely=0.38, relwidth=0.3, relheight=0.2)
        btn = Button(frame2, text="Имя", command=lambda: input_name())
        btn.pack()
        frame3 = Frame(win, bg='#ffe4b5')
        frame3.place(relx=0.35, rely=0.48, relwidth=0.3, relheight=0.2)
        btn = Button(frame3, text="Номер телефона", command=lambda: input_phone())
        btn.pack()
        frame4 = Frame(win, bg='#ffe4b5')
        frame4.place(relx=0.35, rely=0.58, relwidth=0.3, relheight=0.2)
        btn = Button(frame4, text="Описание", command=lambda: input_info())
        btn.pack()
        win.wait_window(win)
        return result_var.get()


def contact_change_end():
        def your_input():
            result_var.set(your_choice.get())
            win.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Изменение контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = StringVar()
        title = Label(win, text='Введите новое значение', bg='#ffe4b5', font=60)
        title.pack()
        your_choice = Entry(win, bg='white')
        your_choice.pack()
        frame = Frame(win, bg='#ffe4b5')
        frame.place(relx=0.35, rely=0.28, relwidth=0.3, relheight=0.2)
        btn = Button(frame, text="Ввод", command=lambda: your_input())
        btn.pack()
        win.wait_window(win)
        return result_var.get()


def saved_change():
        def yes_function(window):
            result_var.set(True)
            window.destroy()
        def no_function(window):
            result_var.set(False)
            window.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Изменения сохранены!')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = BooleanVar()
        title = Label(win, text='Хотите поменять что-либо еще?', bg='#ffe4b5', font=60)
        title.pack()
        frame = Frame(win, bg='white')
        frame.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1)
        btn = Button(frame, text="Да", command=lambda: yes_function(win))
        btn.pack()
        btn = Button(frame, text="Нет", command=lambda: no_function(win))
        btn.pack()
        win.wait_window(win)
        return result_var.get()



# 6. Удалить запись
def find_contact_delete():
        def your_input():
            result_var.set(your_choice.get())
            win.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Удаление контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = StringVar()
        title = Label(win, text='Введите фамилию абонента, запись о котором вы хотите удалить', bg='#ffe4b5', font=60)
        title.pack()
        your_choice = Entry(win, bg='white')
        your_choice.pack()
        frame = Frame(win, bg='#ffe4b5')
        frame.place(relx=0.35, rely=0.28, relwidth=0.3, relheight=0.2)
        btn = Button(frame, text="Ввод", command=lambda: your_input())
        btn.pack()
        win.wait_window(win)
        return result_var.get()


def confirm(fio, info, found_phone_record, file_open):
        def yes_function(window):
            result_var.set(True)
            window.destroy()
        def no_function(window):
            window.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Удаление контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = BooleanVar()
        title = Label(win, text='Все верно?', bg='#ffe4b5', font=60)
        title.pack()
        for record in found_phone_record:
            line = f"Абонент - {fio}. Телефон - {record}. Описание - {info}"
            title = Label(win, text=line, bg='#ffe4b5', font=60)
            title.pack()
        frame = Frame(win, bg='white')
        frame.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1)
        btn = Button(frame, text="Да", command=lambda: yes_function(win))
        btn.pack()
        btn = Button(frame, text="Нет", command=lambda: no_function(win))
        btn.pack()
        win.wait_window(win)
        return result_var.get()

def succes():
        def ok_function(window):
            window.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Удаление контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = BooleanVar()
        title = Label(win, text='Операция выполнена успешно', bg='#ffe4b5', font=60)
        title.pack()
        frame = Frame(win, bg='white')
        frame.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1)
        btn = Button(frame, text="ОК", command=lambda: ok_function(win))
        btn.pack()
        win.wait_window(win)
        return result_var.get()

def another_try():
        def yes_function(window):
            result_var.set(True)
            window.destroy()
        def no_function(window):
            window.destroy()
        win = Tk()
        win['bg'] = '#ffe4b5'
        win.title('Удаление контакта')
        win.wm_attributes('-alpha', 1.0)
        win.geometry('500x500')
        canvas = Canvas(win, height=20, width=10)
        canvas.pack()
        result_var = BooleanVar()
        title = Label(win, text='Хотите ввести другое значение?', bg='#ffe4b5', font=60)
        title.pack()
        frame = Frame(win, bg='white')
        frame.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1)
        btn = Button(frame, text="Да", command=lambda: yes_function(win))
        btn.pack()
        btn = Button(frame, text="Нет", command=lambda: no_function(win))
        btn.pack()
        win.wait_window(win)
        return result_var.get()