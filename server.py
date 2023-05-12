import socket 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8888))

servidor.listen()
cliente, end = servidor.accept()

terminado = False

while not terminado:
    mensagem = cliente.recv(1024).decode('utf-8')
    if mensagem == 'tt':
        terminado = True
    else:
        print("Mensagem do cliente: ", mensagem)
    cliente.send(input('Mensagem do servidor: ').encode('utf-8'))

cliente.close()
servidor.close()
