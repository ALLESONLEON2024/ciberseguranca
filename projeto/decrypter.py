import os
import pyaes

def decrypt_file(encrypted_file, key):
    if not os.path.exists(encrypted_file):
        print(f"Erro: Arquivo {encrypted_file} não encontrado.")
        return
    
    with open(encrypted_file, "rb") as file:
        encrypted_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)

    original_file = encrypted_file.replace(".ransomwaretroll", "")
    with open(original_file, "wb") as file:
        file.write(decrypted_data)

    os.remove(encrypted_file)
    print(f"Arquivo {original_file} descriptografado com sucesso!")

# Chave segura 
key = b"testeransomwares"
decrypt_file("teste.txt.ransomwaretroll", key)
