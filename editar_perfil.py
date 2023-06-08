import PySimpleGUI as sg
from PIL import Image
import json 
import io
import os  
import menu_principal_ventana
import inicio_ventana


class EditarPerfil():
    '''constructor'''
    def __init__(self, perfil_actual):
        perfil_encontrado=None
        self.indice=0    
        '''ruta absoluta del codigo'''
        current_dir = os.path.abspath(__file__)
        '''ruta relativa al directorio con imágenes.'''
        relative_path = 'C:\\Users\\marti\\Desktop\\proyecto\\ventanas\\icons/'
        self.dir_images = os.path.join('./', relative_path)
        
        self.imagen_lista=[]

        '''itera sobre las imagenes y las guarda en imagen_lista'''
        for elem in os.listdir(self.dir_images):
            self.imagen_lista.append(relative_path+elem)
        print(self.imagen_lista)

        '''guardo los perfiles en la variable datos '''
        with open('C:\\Users\\marti\\Desktop\\proyecto\\ventanas\\datos\\perfil.json', 'r') as archivo: 
            self.datos = json.load(archivo)
        '''busco el perfil actual'''
        self.perfil_encontrado=self.EncontrarPerfil(perfil_actual)

        '''interfaz'''
        column1_layout = [
        [sg.Text("Editar Perfil", pad=((30, 0), (0, 50)), font=('Helvetica', 20),background_color='white',text_color='black')],
            
        [sg.Text("Ingresa tu nick o alias:", pad=((30, 0), (20, 30)), font=('Helvetica', 15),background_color='white',text_color='black'),
         sg.Text(self.perfil_encontrado['nick'], pad=((10, 0), (20, 30)), font=('Helvetica', 15),background_color='white',text_color='black')],
            
        [sg.Text("Nombre:", pad=((30, 0), (20, 30)), font=('Helvetica', 15),background_color='white',text_color='black'),
         sg.Text(self.perfil_encontrado['nombre'], key='-nombre-',pad=((10, 0), (20, 30)), font=('Helvetica', 15),background_color='white',text_color='black'),
         sg.Button("editar", key='editarNombre',pad=((10, 0), (20, 30)))],
            
        [sg.Text("Ingresa tu edad:", pad=((30, 0), (10, 30)), font=('Helvetica', 15),background_color='white',text_color='black'),
         sg.Text(self.perfil_encontrado['edad'], key='-edad-', pad=((10, 0), (20, 30)), font=('Helvetica', 15),background_color='white',text_color='black'),
         sg.Button("editar", key='editarEdad',pad=((10, 0), (20, 30)))],
            
        [sg.Text('Género autopercibido:', pad=((30, 0), (10, 30)), font=('Helvetica', 15),background_color='white',text_color='black'),
         sg.Text(self.perfil_encontrado['genero'],key='-genero-', pad=((10, 0), (20, 30)), font=('Helvetica', 15),background_color='white',text_color='black'),
         sg.Button("editar", key='editarGenero',pad=((10, 0), (20, 30)))],]
        
        column2_layout = [
            [sg.Button("<   volver", font=('Helvetica', 12), pad=((200, 0), (0, 150)), size=(20, 2),enable_events=True,key='volver')],
            [sg.Image(self.perfil_encontrado['imagen'], key='image_perfil', pad=((150,0), (0,0)))],
            [sg.Button("Anterior", key="-ant-",pad=((140,0), (50,0))),
            sg.Button("Siguiente", key="-sig-", pad=((30,0), (50,0))),],
            [sg.Button("guardar", font=('Helvetica', 12), pad=((200, 0), (50, 0)), size=(20, 2))],]
        
        column1 = sg.Column(column1_layout, background_color="white")
        column2 = sg.Column(column2_layout, background_color="white", key='-column2-')
        layout = [[column1, column2]]
        self.window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))

        '''funcion que itera sobre los perfiles hasta encontrar el actual'''
    def EncontrarPerfil(self,perfil_actual):
        for perfil in self.datos:
            if (perfil['nick'] == perfil_actual):
                perfil_encontrado = perfil
                return perfil_encontrado
                
    '''muestro y guardo la imagen de la lista, a partir de un indice proporcionado como argumento '''           
    def mostrar_imagen(self,indice,event):
        img = Image.open(self.imagen_lista[indice])
        bio = io.BytesIO()
        '''guardo el formato png'''
        img.save(bio, format="PNG")
        if not event == sg.WINDOW_CLOSED:
            '''actualizo la imagen'''
            self.window['image_perfil'].update(data=bio.getvalue())
        else:
            pass

    def iniciar_ventana(self,perfil_actual):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'guardar': 
                '''actualizo los datos'''
                for perfil in self.datos:
                    if (perfil['nick'] == perfil_actual):
                        perfil.update(self.perfil_encontrado)
                        break 
                with open('datos/perfil.json', 'w') as f:
                    json.dump(self.datos, f, indent=4)
                self.window.close()
                inicio = inicio_ventana.VentanaPrincipal()
                inicio.iniciar_ventana()
            elif event == "volver":
                '''vuelvo al menu principal'''
                self.window.close()
                inicio = menu_principal_ventana.VentanaMenu(perfil_actual)
                inicio.iniciar_ventana()
            elif event== "editarNombre":
                new_nombre = sg.popup_get_text("Nuevo nombre")
            
                if new_nombre:
                    '''Actualiza la variable "nombre"'''
                    self.perfil_encontrado['nombre'] = new_nombre
                    self.window['-nombre-'].update(self.perfil_encontrado['nombre'])
                    
            elif event== "editarEdad":
                new_edad = sg.popup_get_text("Nueva edad")
            
                if new_edad:
                    '''Actualiza la variable `nick`'''
                    self.perfil_encontrado['edad'] = new_edad
                    self.window['-edad-'].update(self.perfil_encontrado['edad'])
            elif event== "editarGenero":
                    
                genero_opciones = ["Masculino", "Femenino", "Otro"]
                new_genero = sg.popup_get_text("Nuevo género")
                    
                if new_genero:
                    '''Validar la entrada del usuario'''
                    if new_genero.capitalize() in genero_opciones:
                        self.perfil_encontrado['genero'] = new_genero.capitalize()
                        self.window['-genero-'].update(self.perfil_encontrado['genero'])
                    else:
                        sg.popup("Opción no válida. Las opciones son: Masculino, Femenino, Otro")
            elif event == "-ant-":
                '''voy a la imagen con el indice anterior'''
                self.indice = (self.indice - 1) % len(self.imagen_lista)
                self.mostrar_imagen(self.indice,event)
                self.perfil_encontrado['imagen']=self.imagen_lista[self.indice]
            elif event == "-sig-":
                '''voy a la imagen con el siguiente indice'''
                self.indice = (self.indice + 1) % len(self.imagen_lista)
                self.mostrar_imagen(self.indice,event)
                self.perfil_encontrado['imagen']=self.imagen_lista[self.indice]
        self.window.close()