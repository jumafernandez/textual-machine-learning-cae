# para usar este codigo debe tener instalado las siguientes librerias
# pip install qrcode
# pip install Pillow
# #######################################################################
import qrcode
from PIL import Image

# Datos que deseas codificar en el QR
data = "https://jumafernandez.github.io/textual-machine-learning-cae"

# Crea un objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Tamaño del código QR (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores (L, M, Q, H)
    box_size=30,  # Tamaño de cada "celda" del código QR
    border=4,  # Tamaño del borde
)

# Agrega los datos al código QR
qr.add_data(data)
qr.make(fit=True)

# Crea una imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guarda la imagen en un archivo PNG
img.save("C:/Users/jumaf/Documents/GitHub/textual-machine-learning-cae/web/imgs/qr-materiales.png")
