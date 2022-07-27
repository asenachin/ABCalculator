# А/В калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.geometry("300x300")
root.title("А/В калькулятор")

# Добавление метки заголовка
lblTitle = tk.Label(text="А/В калькулятор", font=('Helvetica', 16, 'bold'), fg='#0000cc')
lblTitle.place(x=55, y=20)

# Добавление метки заголовка контрольной группы
lblTitle1 = tk.Label(text="Посетители", font=('Helvetica', 12, 'bold'), fg='#0066ff')
lblTitle1.place(x=25, y=55)

# Добавление полей ввода контрольной группы
lblVisitors1 = tk.Label(text="Посетители:", font=('Helvetica', 10, 'bold'))
lblVisitors1.place(x=25, y=85)

lblVisitors1 = tk.Entry(font=('Helvetica', 10, 'bold'))
lblVisitors1.place(x=115, y=85, width=90, height=20)

lblConversions1 = tk.Label(text="Конверсии:", font=('Helvetica', 10, 'bold'))
lblConversions1.place(x=25, y=115)

lblConversions1 = tk.Entry(font=('Helvetica', 10, 'bold'))
lblConversions1.place(x=115, y=115, width=90, height=20) 

# Добавление метки заголовка тестовой группы
lblTitle2 = tk.Label(text="Посетители", font=('Helvetica', 12, 'bold'), fg='#008800')
lblTitle2.place(x=25, y=145)

# Добавление полей ввода тестовой группы
lblVisitors2 = tk.Label(text="Посетители:", font=('Helvetica', 10, 'bold'))
lblVisitors2.place(x=25, y=175)

lblVisitors2 = tk.Entry(font=('Helvetica', 10, 'bold'))
lblVisitors2.place(x=115, y=175, width=90, height=20)

lblConversions2 = tk.Label(text="Конверсии:", font=('Helvetica', 10, 'bold'))
lblConversions2.place(x=25, y=205)

lblConversions2 = tk.Entry(font=('Helvetica', 10, 'bold'))
lblConversions2.place(x=115, y=205, width=90, height=20)

# Добавление кнопки "Расчитать"
btnProcess = tk.Button(root, text="Расчитать", font=('Helvetica', 10, 'bold'))
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font=('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=180, y=250, width=90, height=30)

# Запуск цикла mainlop
root.mainloop()
