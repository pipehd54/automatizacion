import os
import shutil
from pathlib import Path

def mover_archivos(origen, destino, extension='.docx'):
    # Convertir a Path objects
    origen_path = Path(origen)
    destino_path = Path(destino)

    if not destino_path.is_absolute():
        destino_path = origen_path / destino

    # Crear carpeta destino si no existe
    destino_path.mkdir(parents=True, exist_ok=True)
    print(f'Carpeta destino: {destino_path}')

    # Verificar que la carpeta origen existe
    if not origen_path.exists():
        print(f'La carpeta de origen {origen} no existe.')
        return
    
    # Contador de archivos
    archivos_movidos = 0

    # Buscar y mover archivos
    for archivo in origen_path.glob(f'*{extension}'):
        try:
            destino_final = destino_path / archivo.name
            shutil.move(str(archivo), str(destino_final))
            print(f'Movido: {archivo.name}')
            archivos_movidos += 1

        except Exception as e:
            print(f'Error moviendo {archivo.name}: {e}')
    
    print(f'Se movieron {archivos_movidos} archivos extension {extension} a {destino}')

if __name__ == "__main__":
    descargas_path = Path.home() / 'Downloads'
    carpeta_destino = 'ArchivosWord'

    mover_archivos(descargas_path, carpeta_destino)
