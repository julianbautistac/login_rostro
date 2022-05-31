##importando librerias

from configparser import Interpolation
from io import UnsupportedOperation
from tkinter import*
import os
from mtcnn import MTCNN
from mtcnn import cv2
from matplotlib import pyplot

import numpy as np

## se crea una funcion para registrar al usuario
##def registrar_usuario():
##    usuario_info = usuario.get() #para obtener la informacion almacenada en usuario
 ##   contra_info = contra.get() #para obtener la informacion almacenada en contra

 ##   archivo = open(usuario_info, "w")#abrimos la informacion en modo escritura
 ##   archivo.write(usuario_info + "\n") #escribirmos la informacion
 ##   archivo.write(contra_info)
 ##   archivo.close()

    #limpiamos los tex variable
 ##   usuario_entrada.delete(0,END)
  ##  contra_entrada.delete(0,END)

    #ahora le diremos al usuario que su registro ha sido exitoso
##    Label(pantalla1, text="Registro convencional exitoso", fg="green", font=("Calibri",11)).pak()

    ##funcion para almacenar el registro facial
def registro_facial():
    ##para capturar el rostro
    cap = cv2.VideoCapture(0)          #elegimos la camara con la que vamos a hacer la deteccion
    while(True):
        ret,frame = cap.read()         ##leemos el video
        cv2.imshow('Registro facila',frame)     #mostramos el video en pantalla
        if cv2.waitKey(1) == 27:        ##cuando oprimamos ESC corta el video
            break
    usuario_img = usuario.get()
    cv2.imwrite(usuario_img+".jpg",frame)   ## guardamos la ultima captura del video como imagen y asignamos el nombre del usuario
    cap.release()                           ##Cerramos
    cv2.destroyAllWindows()

    usuario_entrada.delete(0, END) #limpiamos los text variables
    contra_entrada.delete(0,END)
    Label(pantalla1,text = "Registro facial exitoso", fg = "green", font = ("Calibri",11)).pack()

    #detectamos el rostro y exportamos los pixeles.

    def reg_rostro(img,lista_resultados):
        data=pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto=lista_resultados[i]['box']
            x2,y2=x1 + ancho, y1 +alto
            pyplot.subplot(1,len(lista_resultados),i+1)
            pyplot.axis('off')
            cara_reg=data[y1:y2,x1:x2]
            cara_reg=cv2.resize(cara_reg,(150,200),Interpolation=cv2.INTER_CUBIC)##Guardamos la imagen con un tamaño de 150*200
            cv2.imwrite(usuario_img+".jpg",cara_reg)
            pyplot.imshow(data[y1:y2,x1:x2])
        pyplot.show()


    img=usuario_img+".jpg"
    pixeles=pyplot.imread(img)
    detector=MTCNN()
    caras=detector.detect_faces(pixeles)
    reg_rostro(img,caras)




# funcion para asignar al boton registro
def registro():
    ##variables globales que usaremos en otras funciones
    global usuario
    global contra 
    global usuario_entrada
    global contra_entrada
    global pantalla1
    pantalla1 = Toplevel(pantalla)  #esta pantalla es de un nivel superior al principal
    pantalla1.title("Registro")
    pantalla1.geometry("300x250")   #asignamos el tamaño de la ventana

    ##Se crean las entradas

    usuario = StringVar()
    contra = StringVar()

    Label(pantalla1,text="Registro facil: debe de asignar un usuario:").pack()
    Label(pantalla1,text="Registro tradicional: debe de asignar un usuario y contraseña:").pack()
    Label(pantalla1,text="").pack()##solo es un espacio
    Label(pantalla1,text="Usuario * ").pack() #se muestra la pantalla 1 al usuario
    usuario_entrada=Entry(pantalla1,textvariable=usuario) ##Creamos un text variable para que el usuario ingrese la informacion
    usuario_entrada.pack()
    Label(pantalla1,text="Contraseña * ").pack() #mostramos en la pantalla 1 la contraseña
    contra_entrada=Entry(pantalla1,textvariable=contra) ##creamos un text variable para que el usuario ingrese la contraseña
    contra_entrada.pack()
    Label(pantalla1,text="").pack() #dejamos un espacio para la creacion del boton
    Button(pantalla1, text="Registro Tradicional", width=15,height=1,command=registrar_usuario).pack() #creamos el boton de registrar usuario
    
    ## boton para hacer el registro facial
    Label(pantalla1,text ="").pack()
    Button(pantalla1, text="Registro facial",width=15,height=1,command=registro_facial).pack()

##Funcion que se le asigna al boton del login
def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2

    pantalla2=Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry("300 x 250") ##se crea la ventana
    Label(pantalla2,text="Login facial: debe de asignar un usuario:").pack()
    Label(pantalla2,text="Login tradicional: debe de asignar un usuario y contraseña:").pack()
    Label(pantalla2,text="").pack() ##espacio interlineado

    verificacion_usuario=StringVar()
    verificacion_contra=StringVar()

    #Ingresamos los datos
    Label(pantalla2,text="Usuario * ").pack()
    usuario_entrada2 = Entry(pantalla2,textvariable=verificacion_usuario)
    usuario.entrada2.pack()
    Label(pantalla2,text="contraseña * ").pack()
    contra_entrada2=Entry(pantalla2,textvariable=verificacion_contra)
    contra_entrada2.pack()
    Label(pantalla2,text="").pack()
    Button(pantalla2,text="Inicio de sesion tradicional",width=20,height=1,command=verificacion_login).pack()


    #vamos a crear el boton para hacer el login facial
    Label(pantalla2,text="").pack()
    Button(pantalla2,text="Inicio de sesion facial",width=20,height=1,command=login_facial).pack()



    ##empezamos creando la funcion para la pantalla principal
def pantalla_principal():
    global pantalla         #es global porque se usaraá en otras funciones
    pantalla = Tk()
    pantalla.geometry("300x250")    ##asignamos el tamaño de la ventana
    pantalla.title("Proyecto de Inteligencia Artificial")   #asignamos el titulo de la pantalla
    Label(text="Login con el rostro",bg = "gray",width ="300", height="2", font=("Arial",13)).pack()    #caracteristicas de la ventana

# Se crean los botones
    Label(text="").pack()   #Creamos el espacio entre el titulo y el primer boton
    Button(text="Iniciar Sesion", height="2",width="30", command=login).pack()
    Label(text="").pack()   #creamos el espacio entre el primer boton y el segundo boton
    Button(text="Registro",height="2",width="30",command=registro).pack()

    pantalla.mainloop()
pantalla_principal()