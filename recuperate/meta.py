import subprocess

def run_mat2(image_path):
    """Esegui mat2 per ottenere i metadati dell'immagine."""
    try:
        result = subprocess.run(
            ['mat2', image_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout
    except FileNotFoundError:
        print("mat2 non è installato. Installa mat2 con 'sudo apt install mat2'.")
        return None

def run_exiftool(image_path):
    """Esegui ExifTool per ottenere i metadati EXIF."""
    try:
        result = subprocess.run(
            ['exiftool', image_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout
    except FileNotFoundError:
        print("ExifTool non è installato. Installa ExifTool con 'sudo apt install libimage-exiftool-perl'.")
        return None

# Chiedi all'utente di inserire il percorso dell'immagine
image_path = input("Inserisci il percorso dell'immagine (es. /home/parrot/immagine.jpg): ")

# Verifica se il file esiste
try:
    with open(image_path, 'rb') as f:
        pass
except FileNotFoundError:
    print(f"Il file {image_path} non esiste.")
    exit(1)

# Esegui mat2 per ottenere i metadati generali
print("\nMetadati generali (da mat2):")
mat2_output = run_mat2(image_path)
if mat2_output:
    print(mat2_output)
else:
    print("Non sono stati trovati metadati generali.")

# Esegui ExifTool per ottenere i metadati EXIF
print("\nMetadati EXIF (da ExifTool):")
exiftool_output = run_exiftool(image_path)
if exiftool_output:
    print(exiftool_output)
else:
    print("Non sono stati trovati metadati EXIF.")
