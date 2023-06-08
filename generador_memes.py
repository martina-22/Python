import PySimpleGUI as sg
import configuracion
import menu_principal_ventana
import json
import os
from PIL import Image


class GeneradorMemes:
    def __init__(self):
        '''
        Inicializa la clase GeneradorMemes.

        Lee los datos de configuración del archivo data.json y configura la ventana de la aplicación.
        '''

        with open('datos/data.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            self.dir_imagenes = datos['Repositorio de imagenes']
            self.archivos_imagenes = self.obtener_imagenes()
            self.elegir_imagen = [
                [sg.Text('Selecciona una imagen'),
                 sg.Listbox(
                     select_mode='extended',
                     enable_events=True,
                     values=self.archivos_imagenes,
                     size=(30, 5),
                     key='imagenes'),
                 sg.Button('Aceptar', key='listo', enable_events=True)]
            ]

            self.image_viewer_column = [
                [sg.Image(key="-IMAGE-", size=(300, 300))],
            ]

            relative_path = "C:\\Users\\marti\\Desktop\\proyecto\\ventanas\\botones\\botonVolver2.png"
            boton_volver = os.path.join('./', relative_path)
            boton_volver = [
                sg.Button(
                    enable_events=True,
                    image_subsample=(10),
                    button_color='white',
                    border_width=0,
                    image_size=(50, 50),
                    image_filename=boton_volver,
                    key='VOLVER'
                )
            ]

            self.layout1 = [
                [
                    sg.Column(self.elegir_imagen, background_color='white'),
                    sg.Column(self.image_viewer_column),
                    boton_volver
                ]
            ]
            self.window = sg.Window(
                'UNLPImage',
                self.layout1,
                size=(800, 600),
                background_color='white'
            )

    def obtener_imagenes(self):
        '''
        Obtiene la lista de archivos de imagen en el directorio especificado.

        Devuelve: una lista de nombres de archivos de imagen.
        '''
        return [
            archivo
            for archivo in os.listdir(self.dir_imagenes)
            if os.path.isfile(os.path.join(self.dir_imagenes, archivo))
            and archivo.lower().endswith((".png", ".gif"))
        ]

    def abrir_ventana(self, perfil_act):
        '''Abre la ventana principal de la aplicación y maneja los eventos.

        Recibe: perfil_act: El perfil de usuario activo.'''

        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'imagenes':
                self.window['imagenes'].update(values=self.obtener_imagenes())
            elif event == 'listo':
                selected_files = values['imagenes']
                if selected_files:
                    filename = os.path.join(self.dir_imagenes, selected_files[0])
                    image = Image.open(filename)
                    image.thumbnail((300, 300))
                    image_data = image.tobytes()
                    self.window["-IMAGE-"].update(data=image_data, size=(300, 300))
            elif event == 'VOLVER':
                self.window.close()
                menu_ventana = menu_principal_ventana.VentanaMenu(perfil_act)
                menu_ventana.iniciar_ventana()
        self.window.close()