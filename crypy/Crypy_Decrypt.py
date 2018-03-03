import os, sys, random, string, struct
from Crypto.Cipher import AES

newextns = "decoded"

def text_generator(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join((random.choice(chars) for _ in range(size))) + '.' + newextns


def generate_file(filename):
    key = ''.join([ random.choice(string.ascii_letters + string.digits) for n in xrange(32) ])
    print("filename", filename, "key", key)
    decrypt_file(key, filename, filename + ".decoded")

def decrypt_file(key, filename, newfilename):
    with open(filename, 'rb') as infile:
        with open(newfilename, 'wb') as outfile:
            fsz = struct.unpack("<Q", infile.read(8))
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)
            while True:
                chunk = infile.read(16)
                if len(chunk) == 0:
                    outfile.truncate(fsz[0])
                    break
                outfile.write(decryptor.decrypt(chunk))

filename = sys.argv[1]
guesseed = int(sys.argv[2])
random.seed(guesseed)
generate_file(filename)
