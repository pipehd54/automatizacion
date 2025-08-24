import os

carpeta = "NuevaCarpeta"
if not os.path.exists(carpeta):
    os.mkdir(carpeta)
    print(f"Carpeta '{carpeta}' creada exitosamente.")
else:
    print(f"La carpeta '{carpeta}' ya existe.")