# Importaciones
from tkinter import *
from tkinter import ttk
import sqlite3
import re
from datetime import date

################################################# Modelo

# Creo la conexion con la base de datos
con = sqlite3.connect("blog.db")
cursor = con.cursor()


# funcion para crear la tabla
def crear_tabla():
    # Creo las instrucciones para la tabla
    sql_table = "CREATE TABLE IF NOT EXISTS blogs (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL, email TEXT NOT NULL, creatd_date TEXT NOT NULL)"
    # Ejecuto la tabla
    cursor.execute(sql_table)
    # confirmo ejecucion
    con.commit()


# Funcion de alta
def alta(title, content, email, created_date, tree, message_label):
    # defino instrucciones de datos
    data = (title, content, email, created_date)
    sql = "INSERT INTO blogs(title, content, email, created_date) VALUES(?, ?, ?, ?)"
    # ejecuto y confirmo
    cursor.execute(sql, data)
    con.commit()

    # Actualizar###############################################################################
    actualizar_treeview(tree, message_label)


# Funcion modificar
def modificar(id, title, content, email, tree, message_label):
    # defino instrucciones de datos
    data = (title, content, email, id)
    sql = "UPDATE blogs SET title = ?, content = ?, email = ? WHERE id = ?"
    # ejecuto y confirmo
    cursor.execute(sql, data)
    con.commit()

    # Actualizar###############################################################################
    actualizar_treeview(tree, message_label)


# Funcion borrar
def borrar(tree, message_label):
    # seleciono valor a borrar
    selected = tree.selection()
    # Agrego condicional para verificar seleccion
    if selected:
        item = tree.item(selected)
        mi_id = item["text"]
        # defino instrucciones
        sql = "DELETE FROM blogs WHERE id = ?"
        data = (mi_id,)
        # ejecuto y confirmo
        cursor.execute(sql, data)
        tree.delete(selected)
        message_label.config(text="Entrada borrada con éxito.")
    else:
        message_label.config(text="Error: No se seleccionó ninguna entrada.")


# Funcion consultar
def consultar(tree, a_val, b_val, c_val):
    # Vuelvo a seleccionar
    selected = tree.selection()
    # Si el seleccionado existe
    if selected:
        item = tree.item(selected)
        # Lo meto en las 3 entradas
        a_val.set(item["values"][0])
        b_val.set(item["values"][1])
        c_val.set(item["values"][2])
        return item["text"]
    else:
        message_label.config(text="Error: No se seleccionó ninguna entrada.")


# Actualizar el tree(visto en ej en clase)
def actualizar_treeview(tree, message_label):
    records = tree.get_children()
    for element in records:
        tree.delete(element)

    # defino instrucciones
    sql = "SELECT * FROM blogs ORDER BY id ASC"
    # ejecuto y confirmo
    datos = cursor.execute(sql)
    # Traigo resultados con un fetch
    resultado = datos.fetchall()
    # Recorro como en ej clase
    for fila in resultado:
        tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))
    message_label.config(text="Base de datos actualizada con éxito.")


######################################## Vista

# Asigno Tk a varable
root = Tk()
# Doy titulo
root.title("Blog App")

root.config(bg="floral white")

root.geometry("1024x768")

titulo = Label(
    root,
    text="Crea Contenido Informativo",
    bg="gray10",
    fg="thistle1",
    height=1,
    width=60,
)
titulo.grid(row=0, column=1, columnspan=4, padx=1, pady=1, sticky=W + E)

titulo_blog = Label(root, text="Titulo del blog")
titulo_blog.grid(row=1, column=1, sticky=W + E)
cont_blog = Label(root, text="Contenido del Blog")
cont_blog.grid(row=2, column=1, sticky=W + E)
email_blog = Label(root, text="Email")
email_blog.grid(row=3, column=1, sticky=W + E)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val = StringVar(), StringVar(), StringVar()
w_ancho = 20

entrada1 = Entry(root, textvariable=a_val, width=100)
entrada1.grid(row=1, column=2)
entrada2 = Entry(root, textvariable=b_val, width=100)
entrada2.grid(row=2, column=2)
entrada3 = Entry(root, textvariable=c_val, width=100)
entrada3.grid(row=3, column=2)

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=150, anchor=W)
tree.column("col2", width=500, minwidth=150, anchor=W)
tree.column("col3", width=150, minwidth=120, anchor=W)
tree.column("col4", width=120, minwidth=120, anchor=W)

tree.heading("#0", text="ID")
tree.heading("col1", text="Titulo del Blog")
tree.heading("col2", text="Contenido")
tree.heading("col3", text="Email")
tree.heading("col4", text="Fecha")
tree.grid(row=9, column=1, columnspan=4)

# Mensajes

message_label = Label(root, text="", fg="red", bg="floral white")
message_label.grid(row=8, column=1, columnspan=2)


##################################### Controlador

# Doy la orden de crear la tabla o leerla
crear_tabla()


# Funcion para datos de entrda
def control_alta():
    # Tomo los datos de entrada con get
    title = a_val.get()
    content = b_val.get()
    email = c_val.get()
    # Uso regex para verificacion
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        alta(title, content, email, str(date.today()), tree, message_label)
        a_val.set("")
        b_val.set("")
        c_val.set("")
    else:
        message_label.config(text="Por favor, introduce un email válido.")


# Funcion para modificar


def control_modificar():
    # seleciono valor
    selected = tree.selection()
    # Si existe
    if selected:
        # hago como en consulta
        item = tree.item(selected)
        # seleciono id
        mi_id = item["text"]
        title = a_val.get()
        content = b_val.get()
        email = c_val.get()
        # Vuelvo a verificar como en alta
        if re.match(r"(<)?(\w+@\w+(?:\.[a-z]+)+)(?(1)>|$)", email):
            modificar(mi_id, title, content, email, tree, message_label)
            a_val.set("")
            b_val.set("")
            c_val.set("")
        else:
            message_label.config(text="Por favor, introduce un email válido.")
    else:
        message_label.config(
            text="Error: No se seleccionó ninguna entrada para modificar."
        )


# Botones

boton_alta = Button(root, text="Alta", command=control_alta)
boton_alta.grid(row=4, column=2)

boton_consulta = Button(
    root, text="Consultar", command=lambda: consultar(tree, a_val, b_val, c_val)
)
boton_consulta.grid(row=5, column=2)

boton_modificar = Button(root, text="Modificar", command=control_modificar)
boton_modificar.grid(row=6, column=2)

boton_borrar = Button(root, text="Borrar", command=lambda: borrar(tree, message_label))
boton_borrar.grid(row=7, column=2)

root.mainloop()

con.close()
