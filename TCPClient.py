import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from socket import *


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((800, 800))
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, file_path)


def send_request():
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    image_path = image_path_entry.get()

    clientSocket.send(image_path.encode())
    response = clientSocket.recv(1024).decode()

    result_label.config(text="Resposta do servidor:\n" + response)

    clientSocket.close()


# Configurar a janela principal
root = tk.Tk()
root.title("Carregar Imagem e Enviar para o Servidor")

# Botão para carregar uma imagem
load_button = tk.Button(root, text="Carregar Imagem", command=open_image)
load_button.pack()

# Entrada para inserir o caminho da imagem
image_path_entry = tk.Entry(root, width=40)
image_path_entry.pack()

# Botão para enviar a solicitação para o servidor
send_button = tk.Button(root, text="Enviar Solicitação", command=send_request)
send_button.pack()

# Rótulo para exibir a imagem carregada
label = tk.Label(root)
label.pack()

# Rótulo para exibir a resposta do servidor
result_label = tk.Label(root)
result_label.pack()

root.mainloop()
