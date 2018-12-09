#caeser cypher

class Cryption:
    
    def encryption(self,plaintext,key):
        alpha = [chr(i) for i in range(256)]
        ciphertext = ''
        for p in plaintext:
            ciphertext += alpha[(ord(p)+key)%256]
        return ciphertext
    
    def decrytion(self,ciphertext,key):
        alpha = [chr(i) for i in range(256)]
        plaintext = ''
        for p in ciphertext:
            plaintext += alpha[(ord(p)-key)%256]
        return plaintext
        
if __name__ == "__main__":
    a = Cryption()
    print(a.encryption('hello',2))
    print(a.decrytion('jgnnq',2))