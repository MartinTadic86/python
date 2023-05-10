import sys
from cryptography.fernet import Fernet

class FileEncryptorDecryptor:
    def __init__(self, action, file_path, key_file):
        self.action = action
        self.file_path = file_path
        self.key_file = key_file

    def load_key(self):
        with open(self.key_file, 'rb') as key_file:
            key = key_file.read()
        return key

    def encrypt_file(self):
        key = self.load_key()
        cipher_suite = Fernet(key)

        with open(self.file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)

        encrypted_file_path = self.file_path + '.cry'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f'File encrypted and saved as: {encrypted_file_path}')

    def decrypt_file(self):
        key = self.load_key()
        cipher_suite = Fernet(key)

        with open(self.file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        decrypted_file_path = self.file_path.replace('.cry', '')
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f'File decrypted and saved as: {decrypted_file_path}')

    def process_file(self):
        if self.action == '-e':
            self.encrypt_file()
        elif self.action == '-d':
            self.decrypt_file()
        else:
            print('Invalid action. Please use -e for encryption or -d for decryption.')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Invalid number of arguments.')
        print('Usage: python fernet.py <action> <file_path> <key_file>')
    else:
        action = sys.argv[1]
        file_path = sys.argv[2]
        key_file = sys.argv[3]

        file_encryptor_decryptor = FileEncryptorDecryptor(action, file_path, key_file)
        file_encryptor_decryptor.process_file()
