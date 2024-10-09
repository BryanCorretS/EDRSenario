import os

def xor_chiffre(chemin, key):
    """Chiffrer selon une porte XOR

    Args:
        chemin (str): Chemin du fichier à crypter
        key (int): Nombre représentant une clé
    """
    with open(chemin, 'rb') as file:
        data = file.read()

    encrypted_data = bytearray(data)
    
    for i in range(len(encrypted_data)):
        encrypted_data[i] ^= (key % 256)  # réduire la clé à une valeur de byte
    
    with open(chemin, 'wb') as file:
        file.write(encrypted_data)

# Créer le fichier avec le message


# Chiffrer le fichier
key = 15161895
if os.path.exists('test.txt'):
    xor_chiffre('test.txt', key)
    print("Le fichier test.txt a été chiffré.")
else:
    print("Le fichier test.txt n'existe pas.")

# if os.path.exists('test.txt'):
#     xor_chiffre('test.txt', key)
#     print("Le fichier test.txt a été déchiffré.")
# else:
#     print("Le fichier test.txt n'existe pas.")
