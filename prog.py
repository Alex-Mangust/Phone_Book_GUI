from tkinter import *
import option
import sys
from  colors import *
# from tkinter import messagebox
root = Tk()

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as ph:
        for i in ph:
            values = i.strip().split(',')
            record = dict(zip(fields, values))
            phone_book.append(record)
    return phone_book

def btn_click():
    option.print_phone_book(read_txt("phonebook.csv"))

    # login = loginInput.get()
    # password = passField.get()
    # info_str = f'Данные: {str(login)}, {str(password)}'
    # messagebox.showinfo(title='Название', message=info_str)
def btn1_click():
    option.find_phone_family(read_txt("phonebook.csv"))

def btn2_click():
    option.find_subscriber_by_phone(read_txt("phonebook.csv"))

def btn3_click():
    option.add_subscriber_in_phonebook(read_txt("phonebook.csv"), "phonebook.csv")

def btn4_click():
    option.change(read_txt("phonebook.csv"), "phonebook.csv")

def btn5_click():
    option.delete_record(read_txt("phonebook.csv"), "phonebook.csv")

def btn6_click():
    sys.exit()


root['bg'] = '#ffe4b5'
root.title('Телефонная книга')
root.wm_attributes('-alpha', 1.0)
root.geometry('500x500')

# root.resizable(width=True, height=True)

canvas = Canvas(root,height=10,width = 10)
canvas.pack()

frame_baground = Frame(root, bg = 'green')
frame_baground.place(relx=0.11, rely=0.02, relwidth=0.8, relheight=0.2)

frame = Frame(root, bg = 'green')
frame.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.1)

frame1 = Frame(root, bg = 'green')
frame1.place(relx=0.11, rely=0.21, relwidth=0.8, relheight=0.1)

frame2 = Frame(root, bg = 'green')
frame2.place(relx=0.11, rely=0.31, relwidth=0.8, relheight=0.1)

frame3 = Frame(root, bg = 'green')
frame3.place(relx=0.11, rely=0.41, relwidth=0.8, relheight=0.1)

frame4 = Frame(root, bg = 'green')
frame4.place(relx=0.11, rely=0.51, relwidth=0.8, relheight=0.1)

frame5 = Frame(root, bg = 'green')
frame5.place(relx=0.11, rely=0.61, relwidth=0.8, relheight=0.1)

frame6 = Frame(root, bg = 'green')
frame6.place(relx=0.11, rely=0.71, relwidth=0.8, relheight=0.1)

frame_baground_end = Frame(root, bg = 'green')
frame_baground_end.place(relx=0.11, rely=0.81, relwidth=0.8, relheight=0.1)

# title = Label(frame, text='Выберите пункт меню', bg='purple', font=60)
# title.place()
# title.pack()
btn = Button (frame, text='Распечатать справочник', bg='orange', command=btn_click)
btn1 = Button(frame1, text='Найти телефон по фамилии', bg='orange', command=btn1_click)
btn2 = Button(frame2, text='Найти абонента по номеру телефона', bg='orange', command=btn2_click)
btn3 = Button(frame3, text='Добавить абонента в справочнике', bg='orange', command=btn3_click)
btn4 = Button(frame4, text='Изменить контакт', bg='orange', command=btn4_click)
btn5 = Button(frame5, text='Удалить контакт', bg='orange', command=btn5_click)
btn6 = Button(frame6, text='Завершить работу', bg='orange', command=btn6_click)


btn.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
# loginInput = Entry(frame, bg='white')
# loginInput.pack()

# passField = Entry(frame, bg='white', show='*')
# passField.pack()

root.mainloop()