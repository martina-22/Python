import PySimpleGUI as sg
import os
import json
import inicio_ventana
import configuracion
import generador_memes
import editar_perfil
import creador_de_collage
import etiquetar_imagenes

class GenerarMeme:

    '''Metodo que se encarga de preparar la ventana previamente a ser iniciada, recibe un parametro que nos indica que perfil mostrar en pantalla'''
    def __init__(self):
        '''Nos preparamos todas las rutas que vamos a usar en la ventana'''
        current_dir = os.path.abspath(__file__)

        columna_vacia = [sg.Column([], background_color='white', size=(200,115))]
        titulo = [sg.Text('Generar Meme:')]
        output_1 = [sg.Output(size=(40, 10), key='-OUTPUT-')]

        texto_1 = [sg.Text('Texto 1:')]
        texto_2 = [sg.Text('Texto 2:')]

        opciones = ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']
        option_menu = [sg.OptionMenu(opciones, default_value=opciones[0])]
        multi_texto_1 = [sg.Multiline(default_text='', size=(40, 5), key ='-INPUT-')]      
        multi_texto_2 = [sg.Multiline(default_text='', size=(40, 5), key ='-INPUT2-')]
        mostrar_texto= [sg.Button('Mostrar: ', key='-MOSTRAR-')]




        column1_layout = [titulo, columna_vacia, option_menu, texto_1, multi_texto_1, mostrar_texto, texto_2, multi_texto_2]
        

        column2_layout = [output_1]
        column3_layout = []
        column4_layout = []

        column1 = sg.Column(column1_layout, size=(300, 600), background_color="white")
        column2 = sg.Column(column2_layout, size=(250, 600), background_color="white")
        column3 = sg.Column(column3_layout, size=(82, 600), background_color="white")
        column4 = sg.Column(column4_layout, size=(82, 600), background_color="white")

        layout = [[column1, column2, column3, column4]]
        self.window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))
    
    '''Metodo que se encarga de iniciar la ventana'''
    def iniciar_ventana(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == '-MOSTRAR-':
                texto_ingresado = values['-INPUT-'] + '\n' + values['-INPUT2-']
                print(texto_ingresado)
        self.window.close()
