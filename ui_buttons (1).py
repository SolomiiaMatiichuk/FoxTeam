import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Encrypt/decrypt program")
root.geometry("600x400")
root.configure(bg='#FF904F')

# First Column (Buttons)

frame1 = tk.Frame(root, bg='#FF904F')
frame1.grid(row=0, column=0, padx=10, pady=10, sticky='n')


def on_button1_clicked():
    pass


def on_button2_clicked():
    pass


def on_button3_clicked():
    pass


def on_button4_clicked():
    pass


def on_button5_clicked():
    pass


button1 = tk.Button(frame1, text='Is device connected?', command=on_button1_clicked, height=2, width=20)
button1.pack(pady=5)

button2 = tk.Button(frame1, text='Can you generation key?', command=on_button2_clicked, height=2, width=20)
button2.pack(pady=5)

button3 = tk.Button(frame1, text="Generate key", command=on_button3_clicked, height=2, width=20)
button3.pack(pady=5)

button4 = tk.Button(frame1, text='Encrypt data', command=on_button4_clicked, height=2, width=20)
button4.pack(pady=5)

button4 = tk.Button(frame1, text='Decrypt data', command=on_button5_clicked, height=2, width=20)
button4.pack(pady=5)

# Second Column (Upload Button)

frame2 = tk.Frame(root, bg='#FF904F')
frame2.grid(row=0, column=1, padx=10, pady=10, sticky='n')


def on_upload_button_clicked():
    file_path = filedialog.askopenfilename()
    print(file_path)
    with open(file_path, "r") as file:
        content = file.read()
        print(content)


upload_button = tk.Button(frame2, text='Загрузити файл', command=on_upload_button_clicked, height=2, width=20)
upload_button.pack(pady=5)


def on_download_button_clicked():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    content = "This is the content of the file"
    with open(file_path, "w") as file:
        file.write(content)


download_button = tk.Button(frame2, text='Зберегти файл', command=on_download_button_clicked, height=2, width=20)
download_button.pack(pady=5)

frame_free = tk.Frame(root, bg='#FF904F')
frame_free.grid(row=0, column=2, padx=10, pady=10, sticky='n')

# Third Column (Output Field)

frame3 = tk.Frame(root, bg='#FF904F')
frame3.grid(row=1, column=3, columnspan=2, rowspan=2, padx=10, pady=30, sticky='se')

output_label = tk.Label(frame3, text='Відповідь:', bg='#FF904F', font=("Helvetica", 14))
output_label.pack(pady=5)

output = tk.Text(frame3, height=2, width=20, font=("Helvetica", 14))
output.pack()

root.mainloop()
