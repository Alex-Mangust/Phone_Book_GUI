from tkinter import *
from tkinter import ttk
import option_two
# 1. Распечатать справочник
def print_phone_book(file_open):
    keys_to_fio = ["Фамилия", "Имя"]
    keys_to_data = ["Телефон", "Описание"]
    win = Tk()
    win['bg'] = '#ffe4b5'
    win.title('Справочник')
    win.wm_attributes('-alpha', 1.0)
    win.geometry('500x500')
    canvas = Canvas(win,height=20,width = 10)
    canvas.pack()
    for i in range(len(file_open)):
        line = str(i+1) + ': '  
        entry = file_open[i]
        values = [entry[key] for key in keys_to_fio]
        line = line + ' '.join(values)
        values = [entry[key] for key in keys_to_data]
        line = line +', ' + ' '.join(values)
        title = Label(win, text=line, bg='#ffe4b5', font=60)
        title.pack()
    win.mainloop()



# 2. Найти телефон по фамилии
def find_phone_family(file_open):
    last_name = StringVar()
    family = option_two.input_family(last_name)
    family = Higher_order(family)
    found_phone_record = []
    found_fio_record = []
    for record in file_open:
        if record.get("Фамилия") == family:
            found_phone_record.append(record.get("Телефон"))
            found_fio_record.append(record.get("Фамилия"))
            found_fio_record.append(record.get("Имя"))
    fio = " ".join(found_fio_record)
    win = Tk()
    win['bg'] = '#ffe4b5'
    win.title('Результаты поиска')
    win.wm_attributes('-alpha', 1.0)
    win.geometry('500x500')
    canvas = Canvas(win,height=20,width = 10)
    canvas.pack()
    if found_phone_record:
        for record in found_phone_record:
            line = f"Телефон абонента {fio} - {record}"
            title = Label(win, text=line, bg='#ffe4b5', font=60)
            title.pack()
    else:
        title = Label(win, text= "Абонент не найден", bg = '#ffe4b5', font=60)
        title.pack()


# 3. Найти абонента по номеру телефона
def find_subscriber_by_phone(file_open):
    phone_number = StringVar()
    phone = option_two.input_phone(phone_number)
    found_phone_record = []
    found_fio_record = []
    found_info_record = []
    for record in file_open:
        if record.get("Телефон") == phone:
            found_phone_record.append(record.get("Телефон"))
            found_fio_record.append(record.get("Фамилия"))
            found_fio_record.append(record.get("Имя"))
            found_info_record.append(record.get("Описание"))
    fio = " ".join(found_fio_record)
    info = "".join(found_info_record)
    win = Tk()
    win['bg'] = '#ffe4b5'
    win.title('Результаты поиска')
    win.wm_attributes('-alpha', 1.0)
    win.geometry('500x500')
    canvas = Canvas(win,height=20,width = 10)
    canvas.pack()
    if found_phone_record:
        for record in found_phone_record:
            line = f"Абонент {fio}. Телефон - {record}. Описание - {info}"
            title = Label(win, text=line, bg='#ffe4b5', font=60)
            title.pack()
    else:
        title = Label(win, text= "Абонент не найден", bg = '#ffe4b5', font=60)
        title.pack()


# 4. Добавить абонента в справочник
def ok_function(window):
    window.destroy()

def add_subscriber_in_phonebook(file_open, filename):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    create = option_two.create_contact().split(',')
    new_subscriber = []
    for i in range(len(create)):
        new_subscriber.append(create[i])
    new_subscriber = dict(zip(fields, new_subscriber))
    file_open.append(new_subscriber)
    # print(file_open)
    with open(filename, 'w', encoding='utf-8') as ph:
        for record in file_open:
            line = ','.join(record[field] for field in fields)
            ph.write(line + "\n")
    win = Tk()
    win['bg'] = '#ffe4b5'
    win.title('Контакт создан')
    win.wm_attributes('-alpha', 1.0)
    win.geometry('500x500')
    canvas = Canvas(win,height=20,width = 10)
    canvas.pack()
    frame1 = Frame(win, bg='#ffe4b5')
    frame1.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1)
    btn = Button(frame1, text="ОК", command=lambda: ok_function(win))
    btn.pack()


# 5. Изменить контакт
def change(file_open, filename):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    field_in = fields[option_two.find_contact_to_change() - 1]
    family_found = option_two.contact_change(file_open, filename, field_in)
    if field_in == 1 or field_in == 2:
        family_found = Higher_order(family_found)
    found_people = []
    id = []
    for record in range(len(file_open)):
        if file_open[record].get(field_in) == family_found:
            found_people.append(file_open[record])
            id.append(record)
    
    if len(found_people) >= 2:
        choice = option_two.many_find(found_people) - 1
    elif len(found_people) == 0:
        if option_two.not_found() == True:
            change(file_open, filename)
        else:
            return 0
    if len(found_people) == 1:
        choice = 0
    your_change = fields[option_two.choice_contact_to_change() - 1]
    new_record = option_two.contact_change_end(file_open, filename, your_change)
    if your_change == 1 or your_change == 2:
        new_record = Higher_order(new_record)
    for record in file_open:
        if record == found_people[choice]:
            record[your_change] = new_record
        with open(filename, 'w', encoding='utf-8') as ph:
            for record in file_open:
                line = ','.join(record[field] for field in fields)
                ph.write(line + "\n")
    if option_two.saved_change() == True:
        change(file_open, filename)
    else:
        return 0

# 6. Удалить запись
def delete_record(file_open, filename):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    confirm_w = False
    while (confirm_w == False):
        family = input("Введите фамилию абонента, запись о котором вы хотите удалить: ")
        found_phone_record = []
        found_fio_record = []
        found_info_record = []
        for record in file_open:
            if record.get("Фамилия") == family:
                found_phone_record.append(record.get("Телефон"))
                found_fio_record.append(record.get("Фамилия"))
                found_fio_record.append(record.get("Имя"))
                found_info_record.append(record.get("Описание"))
        fio = " ".join(found_fio_record)
        info = "".join(found_info_record)
        if found_phone_record:
            for record in found_phone_record:
                print(f"Абонент - {fio}. Телефон - {record}. Описание - {info}")
                confirm = input("Все верно?\n1 - да   2 - нет\n")
                if confirm == "1":
                    confirm_w = True
                    record_delete = 0
                    for i in range(len(file_open)):
                        if file_open[i].get("Фамилия") == family:
                            record_delete = i
                    del file_open[record_delete]
                    with open(filename, 'w', encoding='utf-8') as ph:
                        for record in file_open:
                            line = ','.join(record[field] for field in fields)
                            ph.write(line + "\n")
                else:
                    next_input = input("Хотите ввести другое значение?\n1 - да   2 - нет\n")
                    if next_input == '2':
                        confirm_w = True
        else:
            print("Абонент не найден")
            next = int(input("Продолжить?\n1. Да    2. Нет\n"))
            if next == 2:
                return 0
                
# Функция верхнего регистра первой буквы
def Higher_order(input_user):
    input_user = input_user.lower()
    input_user = list(input_user)
    input_user[0] = input_user[0].upper()
    return ''.join(input_user)



























