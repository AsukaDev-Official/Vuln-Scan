import tkinter, requests
from tkinter import *

root = Tk()
root.title("Vulnerability Scan")
root.config(background="#fff")

root.geometry("450x450")
root.columnconfigure(0, weight=1)

def Scan():
    url = entry_url.get()
    response = requests.get(url)
    if response.status_code == 200:
        response = requests.get(url + '/admin.php')
        if (response.status_code == 200):
            Result.config(text="Vulnerable",fg="green")
        else:
            Result.config(text="Non-vulnerable",fg="red")
    else:
        Result.config(text="Failure",fg="yellow")


# judul
judul = Label(root,
        text="Vulnerability Scan by Tegar",
        font=("Roboto", 18))
judul.grid(pady=1)

# lebel url
url_label = Label(root,
        text="Masukan URL:",
        bg="#fff",
        font=("Roboto", 16))
url_label.grid(pady=1)

# input url
entry_url_var = StringVar()
entry_url = Entry(root,
        width=50,
        textvariable = entry_url_var,
        font=("Roboto", 16),
        justify="center")
entry_url.grid(pady=1)

# cek URL
url_cek = Button(root,
        width=10,
        text="Cek URL",
        bg="#ef5350",
        fg="white",
        font=("Roboto", 16),
        command=Scan)
url_cek.grid(pady=1)

# error result
Result = Label(root,
        text="Belum ada url yang di scan",
        bg="#fff",
        fg="red",
        font=("Roboto", 16))
Result.grid(pady=1)

root.mainloop()