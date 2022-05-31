##importando librerias

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
##def registro_facial():
    ##para capturar el rostro
##    cap = cv2.VideoCapture(0)          #elegimos la camara con la que vamos a hacer la deteccion
##    while(True):
##        ret,frame = cap.read()         ##leemos el video
##        cv2.imshow('Registro facila',frame)     #mostramos el cideo en pantalla
##        if cv2.waitKey(1) == 27:        ##cuando oprimamos ESC corta el video
##            break
##    usuario_img = usuario.get()
##    cv2.imwrite(usuario_img+".jpg",frame)   ## guardamos la ultima captura del video como imagen y asignamos el nombre del usuario
##    cap.release()                           ##Cerramos
##    cv2.destroyAllWindows()

##    usuario_entrada.delete(0, END) #limpiamos los text variables
##    contra_entrada.delete(0,END)
##    Label(pantalla1,text = "Registro facial exitoso", fg = "green", font = ("Calibri",11)).pack()

    #detectamos el rostro y exportamos los pixeles.

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