import PySimpleGUI as sg
from PIL import Image
import json 
import io
import os  
import inicio_ventana
#variables globales

perfil_encontrado=None
indice=0    
current_dir = os.path.abspath(__file__)
relative_path = "icons\\icon_add.png"
imagen_lista = os.path.join('./', relative_path)


if os.path.exists('perfil.json'):
    with open('perfil.json', 'r') as archivo: 
        datos = json.load(archivo)
        
class EditarPerfil():
    #constructor
    def __init__(self, perfil_actual):
        column1 = [
        [sg.Text("Editar Perfil", pad=((30, 0), (0, 50)), font=('Helvetica', 20))],
        [sg.Text("Ingresa tu nick o alias:", pad=((30, 0), (20, 30)), font=('Helvetica', 15)),sg.Text(perfil_encontrado['nick'], pad=((10, 0), (20, 30)), font=('Helvetica', 15))],
        [sg.Text("Nombre:", pad=((30, 0), (20, 30)), font=('Helvetica', 15)),sg.Text(perfil_encontrado['nombre'], key='-nombre-',pad=((10, 0), (20, 30)), font=('Helvetica', 15)),sg.Button("editar", key='editarNombre',pad=((10, 0), (20, 30)))],
        [sg.Text("Ingresa tu edad:", pad=((30, 0), (10, 30)), font=('Helvetica', 15)),sg.Text(perfil_encontrado['edad'], key='-edad-', pad=((10, 0), (20, 30)), font=('Helvetica', 15)),sg.Button("editar", key='editarEdad',pad=((10, 0), (20, 30)))],
        [sg.Text('Género autopercibido:', pad=((30, 0), (10, 30)), font=('Helvetica', 15)),sg.Text(perfil_encontrado['genero'],key='-genero-', pad=((10, 0), (20, 30)), font=('Helvetica', 15)),sg.Button("editar", key='editarGenero',pad=((10, 0), (20, 30)))],]
        column2 = [
            [sg.Button("<   volver", font=('Helvetica', 12), pad=((200, 0), (0, 150)), size=(20, 2))],
            [sg.Image(perfil_encontrado['imagen'], key='image_perfil', pad=((150,0), (0,0)))],
            [sg.Button("Anterior", key="-ant-",pad=((140,0), (50,0))),
            sg.Button("Siguiente", key="-sig-", pad=((30,0), (50,0))),],
            [sg.Text('', size=(30, 1), pad=((0, 0), 20))],
            [sg.Button("guardar", font=('Helvetica', 12), pad=((200, 0), (50, 0)), size=(20, 2))],]
        layout = [[sg.Column(column1), sg.Column(column2)],]
        self.window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))

def EncontrarPerfil(perfil_actual):
    for perfil in datos:
            if (perfil['nick'] == perfil_actual['nick']):
                perfil_encontrado = perfil
                break
def mostrar_imagen(imagen,self,event):
    img = Image.open(imagen[indice])
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    if not event == sg.WINDOW_CLOSED:
        self["image_perfil"].update(data=bio.getvalue())
    else:
        pass
def iniciar_ventana(self,perfil_actual):
    while True:
        event, values = self.read()
        
        if event == 'guardar':
            for i, perfil in enumerate(datos):
                if perfil['nick'] == perfil_actual['nick']:
                    datos[i] = perfil_encontrado
                    break
            with open('perfil.json', 'w') as f:
                json.dump(datos, f, indent=4 )
                print("se actualizo")
                break
        elif event == "<    volver" or event == sg.WIN_CLOSED:
            inicio = inicio_ventana.VentanaPrincipal()
            inicio.iniciar_ventana()
        elif event== "editarNombre":
            new_nombre = sg.popup_get_text("Nuevo nombre")
        
            if new_nombre:
            # Actualiza la variable `nombre`
                perfil_encontrado['nombre'] = new_nombre
                self['-nombre-'].update(perfil_encontrado['nombre'])
                
        elif event== "editarEdad":
            new_edad = sg.popup_get_text("Nueva edad")
        
            if new_edad:
            # Actualiza la variable `nick`
                perfil_encontrado['edad'] = new_edad
                self['-edad-'].update(perfil_encontrado['edad'])
        elif event== "editarGenero":
                
            genero_opciones = ["Masculino", "Femenino", "Otro"]
            new_genero = sg.popup_get_text("Nuevo género")
                
            if new_genero:
                # Validar la entrada del usuario
                if new_genero.capitalize() in genero_opciones:
                    perfil_encontrado['genero'] = new_genero.capitalize()
                    self['-genero-'].update(perfil_encontrado['genero'])
                else:
                    sg.popup("Opción no válida. Las opciones son: Masculino, Femenino, Otro")
        elif event == "-ant-":
            indice = (indice - 1) % len(imagen_lista)
            mostrar_imagen(imagen_lista)
            perfil_encontrado['imagen']=imagen_lista[indice]
        elif event == "-sig-":
            indice = (indice + 1) % len(imagen_lista)
            mostrar_imagen(imagen_lista)
            perfil_encontrado['imagen']=imagen_lista[indice]
    self.close()