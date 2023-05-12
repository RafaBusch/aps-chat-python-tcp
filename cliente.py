import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 8888))

terminado = False
print('Digite tt para terminar o chat')

while not terminado:
    cliente.send(input('Mensagem do cliente: ').encode('utf-8'))
    mensagem = cliente.recv(1024).decode('utf-8')
    if mensagem == 'tt':
        terminado = True
    else:
        print("Mensagem do cliente: ", mensagem)

cliente.close()