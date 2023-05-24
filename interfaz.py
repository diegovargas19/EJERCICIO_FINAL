from tkinter import *
from tkinter import ttk
import sqlite3

class Datos: 


    def __init__(self, raiz):
        frameTabla=ttk.Frame(raiz, padding="20 30 20 30", relief="raised")
        frameTabla.grid(column=0, row=10, columnspan=8)

        tv = ttk.Treeview(frameTabla, columns=("nombre","aPaterno", "aMaterno", "correo", "movil", "dedicacion", "lee", "estudiar" , "videojuegos", "estado"))
        tv.grid(column=2, row=0, padx=0, pady=0)
        tv.column("nombre",width=130, anchor=CENTER)
        tv.column("aPaterno",width=130, anchor=CENTER)
        tv.column("aMaterno",width=130, anchor=CENTER)
        tv.column("correo",width=130, anchor=CENTER)
        tv.column("movil",width=130, anchor=CENTER)
        tv.column("dedicacion",width=130, anchor=CENTER)
        tv.column("lee",width=130, anchor=CENTER)
        tv.column("estudiar",width=130, anchor=CENTER)
        tv.column("videojuegos",width=130, anchor=CENTER)
        tv.column("estado",width=130, anchor=CENTER)

        tv.heading("nombre", text="Nombre", anchor=CENTER)
        tv.heading("aPaterno", text="APaterno", anchor=CENTER)
        tv.heading("aMaterno", text="AMaterno", anchor=CENTER)
        tv.heading("correo", text="Correo", anchor=CENTER)
        tv.heading("movil", text="Movil", anchor=CENTER)
        tv.heading("dedicacion", text="Dedicacion", anchor=CENTER)
        tv.heading("estudiar", text="Estudiar", anchor=CENTER)
        tv.heading("lee", text="Lee", anchor=CENTER)
        tv.heading("videojuegos", text="Videojuegos", anchor=CENTER)
        tv.heading("estado", text="Estado", anchor=CENTER)


        with open('documentos.csv', 'r') as file:

            lineas = file.readlines()
            for i, linea in enumerate(lineas):
                lista = linea.strip().split(",")
                tv.insert(parent="", index="end", iid = i, text = i, values=(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9]))

            tv.pack()

        raiz.config(bd=25)

        self.nombre = StringVar()
        self.paterno=StringVar()
        self.materno = StringVar()
        self.correo=StringVar()
        self.movil=StringVar()

        '''radio_button'''
        self.estu_boolean=BooleanVar()
        self.estu_boolean.set(False)
        self.emple_boolean=BooleanVar()
        self.emple_boolean.set(False)
        self.des_boolean=BooleanVar()
        self.des_boolean.set(False)

        '''check_button'''
        self.estudiar_boolean=BooleanVar()
        self.estudiar_boolean.set(False)
        self.leer_boolean=BooleanVar()
        self.leer_boolean.set(False)
        self.juegos_boolean=BooleanVar()
        self.juegos_boolean.set(False)

        '''estado'''
        self.estado=StringVar()
        

        raiz.title("Resgistro")

        aficiones= ttk.Frame(raiz, padding="10 15 10 15", relief="raised")
        aficiones.grid(column=0, row=7, columnspan=1,pady=10)

        registro=ttk.Frame(raiz,padding="10 15 10 15", relief="raised")
        registro.grid(column=0, row=0, rowspan=6, columnspan=1,pady=10)

        oficios=ttk.Frame(raiz, padding="10 15 10 15")
        oficios.grid(column=2, row=0, rowspan=6,pady=10)


        '''datos'''
        nombreEntry=ttk.Entry(registro, width=20, textvariable=self.nombre)
        nombreEntry.grid(column=1,row=0,pady=10)

        paternoEntry=ttk.Entry(registro, width=20, textvariable=self.paterno)
        paternoEntry.grid(column=1,row=1,pady=10)

        maternoEntry=ttk.Entry(registro, width=20, textvariable=self.materno)
        maternoEntry.grid(column=1,row=2,pady=10)

        correoEntry=ttk.Entry(registro, width=20, textvariable=self.correo)
        correoEntry.grid(column=1,row=3,pady=10)

        movilEntry=ttk.Entry(registro, width=20, textvariable=self.movil)
        movilEntry.grid(column=1,row=4,pady=10)


        ttk.Label(registro, text="usuario:").grid(column=0, row=0, pady=10)
        ttk.Label(registro, text="A.paterno:").grid(column=0, row=1, pady=10)
        ttk.Label(registro, text="A.materno:").grid(column=0, row=2, pady=10)
        ttk.Label(registro, text="correo:").grid(column=0, row=3, pady=10)
        ttk.Label(registro, text="movil:").grid(column=0, row=4, pady=10)


        '''oficio'''
        estudiante=ttk.Radiobutton(oficios, text='estudiante', variable=self.estu_boolean)
        estudiante.grid(column=2,row=2,)

        empleado=ttk.Radiobutton(oficios, text='empleado', variable=self.emple_boolean)
        empleado.grid(column=2,row=3,pady=4, sticky=(N))

        desempleo=ttk.Radiobutton(oficios, text='desempleado', variable=self.des_boolean)
        desempleo.grid(column=2,row=4,pady=4, sticky=(N))


        '''aficiones'''

        ttk.Label(aficiones, text="aficiones").grid(column=0,row=0)

        leer=ttk.Checkbutton(aficiones,text="leer", variable=self.leer_boolean)
        leer.grid(column=0, row=1)

        estudiar=ttk.Checkbutton(aficiones,text="estudiar", variable=self.estudiar_boolean)
        estudiar.grid(column=1, row= 1)

        videojuegos=ttk.Checkbutton(aficiones,text="videojuegos",variable=self.juegos_boolean)
        videojuegos.grid(column=2, row= 1)

        '''estado'''
        estados=ttk.Combobox(raiz, text= "estados", textvariable=self.estado)
        estados.grid(column=2,row=7)
        estados['values']=("jalisco", "nayarit", "colima","michoacan" )

        '''guardar y cancelar'''

        ttk.Button(raiz, text="guardar", command=self.registrar).grid(column=0,row=8)
        ttk.Button(raiz, text="cancelar").grid(column=1,row=8)
        ttk.Button(raiz, text="Guardad bd ", command=self.baseDatos).grid(column=2,row=8)



    def registrar(self, *args):

    
        nombre=self.nombre.get()
        a_paterno=self.paterno.get()
        a_materno=self.materno.get()
        correo=self.correo.get()
        telefono=self.movil.get()

        oficio=StringVar()
        if self.estu_boolean.get()==TRUE:
             oficio="estudiante"
        elif self.emple_boolean.get()==TRUE:
           oficio="empleado"
        elif self.des_boolean.get()==TRUE:
            oficio="desempleaddo"
        
        

        leer=StringVar()
        if self.leer_boolean.get()==TRUE:
            leer="leer"
        else:
            leer=" "

        estudiar=StringVar()
        if self.estudiar_boolean.get()==TRUE:
            estudiar="estudiar"
        else:
            estudiar=" "

        jugar=StringVar()
        if self.juegos_boolean.get()==TRUE:
            jugar="videojuegos"
        else:
            jugar=" "

        estado=self.estado.get()

        lista=[nombre, a_paterno, a_materno, correo, telefono, oficio, leer, estudiar, jugar, estado]
        print(lista)

        with open("documentos.csv", "a") as file:
            for e in lista:
                file.writelines(e + ", ")
            file.write("\n")
        
                
        
        lista.clear()

    def baseDatos (self):
        conexion = sqlite3.connect('registro.db')
        c= conexion.cursor()
        
        nombre=self.nombre.get()
        a_paterno=self.paterno.get()
        a_materno=self.materno.get()
        correo=self.correo.get()
        telefono=self.movil.get()

        oficio=StringVar()
        if self.estu_boolean.get()==TRUE:
            oficio='estudiante'
        elif self.emple_boolean.get()==TRUE:
            oficio='empleado'
        elif self.des_boolean.get()==TRUE:
            oficio='desempleaddo'

        leer=StringVar()
        if self.leer_boolean.get()==TRUE:
            leer='leer'
        else:
            leer=' '

        estudiar=StringVar()
        if self.estudiar_boolean.get()==TRUE:
            estudiar='estudiar'
        else:
            estudiar=' '

        jugar=StringVar()
        if self.juegos_boolean.get()==TRUE:
            jugar='videojuegos'
        else:
            jugar=' '

        estado=self.estado.get()

        lista=[(nombre, a_paterno, a_materno, correo, telefono, oficio, leer, estudiar, jugar, estado)]   

        c.executemany('INSERT INTO logs VALUES (?,?,?,?,?,?,?,?,?,?)', lista)
        conexion.commit()
        for row in c.execute("SELECT * FROM logs"):
            print(row)

        conexion.close()

        


   
if __name__ == '__main__':
    root = Tk()
    ventana = Datos(root)
    root.mainloop()

    