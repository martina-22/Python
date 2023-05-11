import PySimpleGUI as sg
from PIL import Image
import json 
import io
import os
import menu_principal_ventana

current_dir = os.path.abspath(__file__)
relative_path = "icons"
imagen_lista = os.path.join('./', relative_path)

indice = 0
perfil_actual=None
class NuevoPerfil:
    def __init__(self):
        
        column1_layout = [
            [sg.Text("Nuevo Perfil", pad=((30, 0), (0, 50)), font=('Helvetica', 20),,background_color='white',text_color='black')],
            [sg.Text("Ingresa tu nombre:", pad=((80, 0), (20, 0)), font=('Helvetica', 15),,background_color='white',text_color='black')],
            [sg.InputText('', pad=((80, 0), (0, 10)), size=(20, 1), font=('Helvetica', 15))],
            [sg.Text("Ingresa tu nick o alias:", pad=((80, 0), (20, 0)), font=('Helvetica', 15),,background_color='white',text_color='black')],
            [sg.InputText('', pad=((80, 0), (0, 10)), size=(20, 1), font=('Helvetica', 15))],
            [sg.Text("Ingresa tu edad:", pad=((80, 0), (10, 0)), font=('Helvetica', 15),background_color='white',text_color='black')],
            [sg.InputText('', pad=((80, 0), (0, 10)), size=(20, 1), font=('Helvetica', 15))],
            [sg.Text('Género autopercibido:', pad=((80, 0), (10, 0)), font=('Helvetica', 15),background_color='white',text_color='black')],
            [sg.Combo(['Masculino', 'Femenino','Otro'], key='genero', pad=((80, 0), (10, 0)), font=('Helvetica', 15))],
        ]

        column2_layout = [
            [sg.Button("<   volver", font=('Helvetica', 12), pad=((300, 0), (0, 150)), size=(20, 2))],
            [sg.Image(imagen_lista[indice], key='image_perfil', pad=((150,0), (0,0)))],
            [sg.Button("Anterior", key="-ant-",pad=((140,0), (50,0))),
            sg.Button("Siguiente", key="-sig-", pad=((30,0), (50,0))),],
            [sg.Button("guardar", font=('Helvetica', 12), pad=((300, 0), (50, 0)), size=(20, 2))],
        ]

        column1 = sg.Column(column1_layout, background_color="white")
        column2 = sg.Column(column2_layout, background_color="white", key='-column2-')

        layout = [[column1, column2]]

        self.window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))
        
def mostrar_imagen(imagen,self,event):
    img = Image.open(imagen[indice])
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    if not event == sg.WINDOW_CLOSED:
        self["image_perfil"].update(data=bio.getvalue())
    else:
        pass
    
def validar_campos(values):
    campos_vacios = []
    if not values[0]: # Validar campo nick
        campos_vacios.append('nombre')
    if not values[1]: # Validar campo nick
        campos_vacios.append('Nick o alias')
    if not values[2].isdigit(): # Validar campo edad
        campos_vacios.append('Edad')
    if not values['genero']: # Validar campo género
        campos_vacios.append('Género autopercibido')
    if campos_vacios:
        campos = ', '.join(campos_vacios)
        mensaje = f"Los siguientes campos están vacíos: {campos}. Por favor, completa todos los campos antes de guardar."
        sg.popup_error(mensaje)
        return False
    return True
def iniciar_ventana(self):
    while True:
        event, values = self.read()
        if event == 'guardar':
            if validar_campos(values):
                data = {
                    "nombre": values[0],
                    "nick": values[1],
                    "edad": values[2],
                    "genero": values["genero"],
                    "imagen": imagen_lista[indice]
                }
                perfil_actual=values[1]
                if os.path.exists('perfiles.json'):
                    with open('perfiles.json', "r") as f:
                        perfiles = json.load(f)
                else:
                    perfiles = []
                perfiles.append(data)
                with open('perfiles.json', "w") as f:
                    json.dump(perfiles, f, indent=4)
                break
        elif event == "<    volver" or event == sg.WIN_CLOSED:
            inicio = menu_principal_ventana.VentanaMenu()
            inicio.iniciar_ventana()
        elif event == "-ant-":
            indice = (indice - 1) % len(imagen_lista)
            mostrar_imagen(imagen_lista)
        elif event == "-sig-":
            indice = (indice + 1) % len(imagen_lista)
            mostrar_imagen(imagen_lista)
    self.close()
    
