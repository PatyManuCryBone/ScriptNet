import os
from PIL import Image
import piexif

def get_exif_data(image_path):
    # Apre l'immagine
    image = Image.open(image_path)
    
    # Estrae i metadati EXIF
    exif_data = piexif.load(image.info['exif'])
    
    return exif_data

def get_gps_info(exif_data):
    # Controlla se ci sono dati GPS
    gps_info = exif_data.get('GPS', {})
    if not gps_info:
        return None
    
    # Estrae le coordinate GPS
    lat_deg = gps_info.get(piexif.GPSIFD.GPSLatitude, None)
    lat_ref = gps_info.get(piexif.GPSIFD.GPSLatitudeRef, None)
    lon_deg = gps_info.get(piexif.GPSIFD.GPSLongitude, None)
    lon_ref = gps_info.get(piexif.GPSIFD.GPSLongitudeRef, None)

    if lat_deg and lon_deg:
        # Converti i gradi, minuti e secondi in decimale
        lat = convert_to_decimal(lat_deg, lat_ref)
        lon = convert_to_decimal(lon_deg, lon_ref)
        return lat, lon
    return None

def convert_to_decimal(degrees, ref):
    # Converti i dati GPS in formato decimale
    decimal = degrees[0][0] / degrees[0][1] + degrees[1][0] / degrees[1][1] / 60 + degrees[2][0] / degrees[2][1] / 3600
    if ref == 'S' or ref == 'W':
        decimal = -decimal
    return decimal

# Chiedi all'utente di inserire il percorso dell'immagine
image_path = input("Inserisci il percorso dell'immagine (es. /home/parrot/immagine.jpg): ")

# Verifica se il file esiste
if os.path.exists(image_path):
    exif_data = get_exif_data(image_path)
    gps_coordinates = get_gps_info(exif_data)

    if gps_coordinates:
        print(f"Coordinate GPS: {gps_coordinates}")
    else:
        print("Nessuna informazione GPS trovata.")
else:
    print(f"Il file {image_path} non esiste.")
