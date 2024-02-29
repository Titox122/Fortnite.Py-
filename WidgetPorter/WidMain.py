import json
import tkinter as tk
from tkinter import filedialog

def convert_to_ue5_text(properties):
    ue5_text = ""
    for index, props in enumerate(properties):
        ue5_text += f"Begin Object Class=/Script/UMG.TextBlock Name=\"TextBlock_{index}\" ExportPath=\"/Script/UMG.TextBlock'/Game/Widgets/NewWidgetBlueprint.NewWidgetBlueprint:WidgetTree.TextBlock_{index}'\"\n"
        for key, value in props.items():
            if key == 'Text':
                ue5_text += f"   {key}=NSLOCTEXT(\"\", \"\", \"{value['LocalizedString']}\")\n"
            elif key == 'Font':
                font_object = value['FontObject']['ObjectPath']
                font_object = font_object[:-2] if font_object.endswith('.0') else font_object  # Eliminar ".0" al final si existe
                font_object = font_object.rstrip('.')  # Eliminar cualquier punto al final
                font_name = font_object.split('/')[-1]  # Extraer el nombre de la fuente
                font_resultado = f"font{font_name}"  # Construir el nombre de la fuente en el formato deseado
                typeface_font_name = value['TypefaceFontName']
                size = value.get('Size', 24.0)  # Default size if not present
                # Escape any quotation marks in the font object path
                font_object = font_object.replace("'", "\\'")
                ue5_text += f"   {key}=(FontObject=\"{font_object}\",TypefaceFontName=\"{font_resultado}\",Size={size},LetterSpacing={value.get('LetterSpacing', 1)})\n"
            elif isinstance(value, dict):
                ue5_text += f"   {key}=struct'{value}'\n"
            else:
                ue5_text += f"   {key}={value}\n"
        ue5_text += f"End Object\n"
    return ue5_text

def process_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        text_blocks = []
        for item in data:
            if item.get('Type') == 'CommonTextBlock':
                properties = item.get('Properties')
                text_blocks.append(properties)
        ue5_text = convert_to_ue5_text(text_blocks)
        print(ue5_text)

def select_json_file():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    json_file = filedialog.askopenfilename(
        title="Seleccione un archivo JSON",
        filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
    )

    if json_file:
        print("Archivo JSON seleccionado:", json_file)
        process_json(json_file)
    else:
        print("No se seleccionó ningún archivo JSON.")

# Llama a la función select_json_file para permitir al usuario seleccionar un archivo JSON
select_json_file()
