import hashlib, json, sys

def hash(identifier, nonce, data, previous_hash):
          message = hashlib.sha256()
          message.update(str(identifier).encode('utf-8'))
          message.update(str(nonce).encode('utf-8'))
          message.update(str(data).encode('utf-8'))
          message.update(str(previous_hash).encode('utf-8'))
          return message.hexdigest()

block = json.load(sys.stdin)
print hash(block["identifier"], block["nonce"], block["data"], block["previous_hash"])
