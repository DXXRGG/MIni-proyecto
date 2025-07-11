import tkinter as tk 
from operations import crear_usuario
from tkinter import messagebox as mb 

main_window = tk.Tk()

main_window.geometry("700x700")

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1)
main_window.columnconfigure(2, weight=1)
for i in range (6):
    main_window.rowconfigure(i, pad=10)
#titulo
title = tk.Label(main_window, text="Vista para crear clientes", font=("Arial", 20), fg="red")
title.grid(column=0, row=0, columnspan=3, sticky="n")


tk.Label(main_window, text="Nombre:", font=("Arial", 15)).grid(column=0, row=1, sticky="en")
entry_name = tk.Entry(main_window, font=("Arial", 15))
entry_name.grid(column=1, row=1)

tk.Label(main_window, text="email:", font=("Arial", 15)).grid(column=0, row=2, sticky="en")
entry_email = tk.Entry(main_window, font=("Arial", 15))
entry_email.grid(column=1, row=2)

tk.Label(main_window, text="phone:", font=("Arial", 15)).grid(column=0, row=3, sticky="en")
entry_phone = tk.Entry(main_window, font=("Arial", 15))
entry_phone.grid(column=1, row=3)

tk.Label(main_window, text="adress:", font=("Arial", 15)).grid(column=0, row=4, sticky="en")
entry_address = tk.Entry(main_window, font=("Arial", 15))
entry_address.grid(column=1, row=4)

tk.Label(main_window, text="password:", font=("Arial", 15)).grid(column=0, row=5, sticky="en")
entry_password = tk.Entry(main_window, font=("Arial", 15))
entry_password.grid(column=1, row=5)

def enviar():
    data ={}
    data["name"] = entry_name.get()
    data["password"] = entry_password.get()
    data["email"] = entry_email.get()
    data["address"]= entry_address.get()
    data["phone"]= entry_phone.get()
    status, msg = crear_usuario(data)
    if not status: 
        mb.showerror("ocurrio un error:", msg)
        return
    mb.showinfo("usuatrio creado,", msg)



tk.Button(main_window, command=enviar, font=("Arial", 15), text="Guardar", fg="black", bg="white", relief="flat").grid(column=0, row=6, columnspan=3, sticky="n")