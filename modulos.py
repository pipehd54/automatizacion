import os
from pathlib import Path, PurePath

# Nombre de ruta de script de Python
print(os.getcwd())
print(Path.cwd())

# Listar archivos
print(os.listdir())
# print(os.listdir('nombre_carpeta')) # Acceder a una carpeta
print(list(Path().iterdir()))  # Iterar en los archivos de la carpeta actual
# print(list(Path('nombre_carpeta').iterdir())) # Acceder a una carpeta con Path

# Juntar rutas o Path
print(os.path.join(os.getcwd(), 'NuevaCarpeta'))
print(PurePath.joinpath(Path.cwd(), 'NuevaCarpeta'))

# Crear carpetas con Python
os.makedirs('Carpeta_Python', exist_ok=True)  # exist_ok evita error si ya existe
Path('Nueva_Python').mkdir(exist_ok=True)

os.makedirs(os.path.join('NuevaCarpeta', 'Scripts'), exist_ok=True)
PurePath.joinpath(Path.cwd(), 'NuevaCarpeta1', 'Scripts').mkdir(parents=True, exist_ok=True)

# Renombrar carpetas 
# os.rename('NuevaCarpeta1', 'CarpetaRenombrada')

# path_actual = Path('CarpetaRenombrada')
# path_objetivo = Path('Renombrada')

# Path.rename(path_actual, path_objetivo)

# Renombrar archivos
# for file in os.listdir():
#    if file.endswith('csv'):
#        os.rename(file, f'2025_{file}')

# Metadata
print(os.path.abspath('Scripts'))

script = Path('api.py')
print(script.resolve())
print(script.stem)  # Nombre sin extension
print(script.suffix)  # Extension
print(script.stat().st_size)  # Tamaño en bytes
