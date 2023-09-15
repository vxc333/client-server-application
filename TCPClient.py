import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from socket import *


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, file_path)


def send_request():
    serverName = ip_entry.get()
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    image_path = image_path_entry.get()

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    clientSocket.send(image_data)
    response = clientSocket.recv(1024).decode()

    result_label.config(text="Resposta do servidor:\n" + response)

    clientSocket.close()


root = tk.Tk()
root.title("Carregar Imagem e Enviar para o Servidor")

ip_label = tk.Label(root, text="Digite o Ip do Servidor ou o Nome")
ip_label.pack()
ip_entry = tk.Entry(root, width=40)
ip_entry.pack()

print(ip_entry.get())

load_button = tk.Button(root, text="Carregar Imagem", command=open_image)
load_button.pack()

image_path_entry = tk.Entry(root, width=40)
image_path_entry.pack()

send_button = tk.Button(root, text="Enviar Solicitação", command=send_request)
send_button.pack()

label = tk.Label(root)
label.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
