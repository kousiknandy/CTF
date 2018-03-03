import hashlib
import uuid


class Block(object):
    def __init__(self, data=None, block_id=None, previous_hash=None, nonce=None):
        self.identifier = block_id or uuid.uuid4().hex
        self.nonce = nonce
        self.data = data
        self.previous_hash = previous_hash

    def hash(self, nonce=None):
        nonce = nonce or self.nonce

        message = hashlib.sha256()
        message.update(self.identifier.encode('utf-8'))
        message.update(str(nonce).encode('utf-8'))
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.previous_hash).encode('utf-8'))

        return message.hexdigest()

    @staticmethod
    def hash_is_valid(the_hash, difficulty):
        return the_hash.startswith("".zfill(difficulty))

    @property
    def mined(self):
        return self.nonce is not None

    def mine(self, difficulty=4):
        the_nonce = self.nonce or 0

        while True:
            the_hash = self.hash(nonce=the_nonce)
            if self.hash_is_valid(the_hash, difficulty):
                self.nonce = the_nonce
                return
            else:
                the_nonce += 1

    def update_data(self, data):
        self.data = data
        self.nonce = None

    def acceptable(self, difficulty=4):
        the_hash = self.hash()
        return self.hash_is_valid(the_hash, difficulty)

    def __repr__(self):
        return 'Block<Hash: {}, Nonce: {}>'.format(self.hash(), self.nonce)
