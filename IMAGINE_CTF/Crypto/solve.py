import rsa

def decrypt_rsa_file(encrypted_file_path, private_key_path, output_file_path):
    # Đọc dữ liệu được mã hóa từ file flag.enc
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Đọc khóa riêng từ file private.pem
    with open(private_key_path, 'rb') as private_key_file:
        private_key_data = private_key_file.read()
        private_key = rsa.PrivateKey.load_pkcs1(private_key_data)

    # Giải mã dữ liệu
    decrypted_data = rsa.decrypt(encrypted_data, private_key)

    # Lưu dữ liệu đã giải mã vào một file mới
    with open(output_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

# Sử dụng hàm để giải mã và lưu vào file mới
decrypt_rsa_file('flag.enc', 'private.pem', 'decrypted_flag.txt')
