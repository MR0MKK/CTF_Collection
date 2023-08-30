# v9 = 0x560561C05000
# v7 = 5

# result = "usN1hAlgXFwzhN8d"

import hashlib

def md5_update(data, md5_hash):
    if not isinstance(data, bytes):
        data = data.encode()

    md5_hash.update(data)

if __name__ == "__main__":
    md5_hash = hashlib.md5()

    # Dữ liệu đầu vào
    data1 = "minhkingkong123456789123"
    data2 = "0123456789ABCDEFFEDCBA9876543210"

    md5_update(data1, md5_hash)
    md5_update(data2, md5_hash)

    result = md5_hash.hexdigest()
    print("MD5 hash:", result)
