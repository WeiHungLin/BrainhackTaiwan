def generatekey(message, key):
    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encrypt_letter(string, key):
    encrypt_text = []
    for i in range(len(string)):
        encrypted_index = (ord(string[i])+ord(key[i]))% 1114112
        encrypt_text.append(chr(encrypted_index))
    return("".join(encrypt_text))

def decrypt_letter(string, key):
    decrypt_text = []
    for i in range(len(string)):
        decrypt_index = (ord(string[i])-ord(key[i])) % 1114112
        decrypt_text.append(chr(decrypt_index))
    return("".join(decrypt_text))

def process_message(message, key, encrypt):
    if encrypt == "True":
        keyword = generatekey(message,key)
        ans = encrypt_letter(message, keyword)
        return ans
    else:
        keyword = generatekey(message,key)
        ans = decrypt_letter(message, keyword)
    return ans

if __name__ == "__main__":
   a = input("Please enter your message: ")
   b = input("Please enter your key: ")
   c = input("Whether this is an encrypt: ")
   x = process_message(a,b,c)
   print(x)