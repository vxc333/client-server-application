from socket import *
from PIL import Image
import io


def process_image(image_data):
    try:
        image_buffer = io.BytesIO(image_data)
        img = Image.open(image_buffer)
        color_mode = img.mode
        image_format = img.format
        dimensions = img.size
        return color_mode, image_format, dimensions
    except Exception as e:
        return None, None, None


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    color_mode, image_format, dimensions = process_image(sentence)

    if color_mode and image_format and dimensions:
        response = f"Padrão de cor: {color_mode}, Formato: {image_format}, Dimensões: {dimensions[0]}x{dimensions[1]}"
    else:
        response = "Erro ao processar a imagem."

    connectionSocket.send(response.encode())
    connectionSocket.close()
