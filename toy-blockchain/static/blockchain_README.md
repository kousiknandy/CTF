# Implement Python Blockchain 

## Create a Python based Block Chain to reveal the flag

### Summary

The contestant has to submit a block chain (in JSON format) which is rooted
at a genesis block the challenge provides. The block chain length should be
at least 4. The hash difficulty is increased 16 fold for 4th block, 256 fold
for the fifth, 4096 fold for the sixth and so on, with initial difficulty
set to first 2^16 bits to be zero.

### Block

Each block consists of 4 elements. An "identifier" which is a string of length
1-32 characters, and needs to be unique in the chain. A "data" which is a string
of 1-256 characters and can contain any arbitrary string. A "previous_hash" which
is 64 characters, contains hex encoding of SHA256 hash of the previous block (an
implementation is provided). A "nonce", which is a positive integer. Example of
a block would be (JSON encoded)
```
    {
     "identifier": "4b9af129de354a5393670452f6689374",
     "data": "Third", 
     "previous_hash": "0000902865f7d72aeae49473fab6f1898017f4480cb3fff0f9c9590ee91e9277",
     "nonce": 37787
    }
```

### Hashing

Implementation of the hash is given as:
```
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
```

Also can be retrieved at `/hashfunction` URL.

### Genesis Block

The first block of a blockchain must start with the genesis block provided by the system.
The definition of genesis block is (JSON encoded):
```
    {
     "identifier": "000102030405060708090A0B0C0D0E0F",
     "nonce": 3754873684,
     "data": "Genesis Block for CTF contest, all block chains must start with this block. This is equivalent to Big Bang, time didn't exist before this",
     "previous_hash": null
    }
```

Notice the `previous_hash` is null as expected. To validate the implementation, if the hash
of the genesis block is taken, it should be `00000000c55f6538ae0a9d1e094c41781f4d05d789ab435c5ec1d4b8bd8738ba`.

The genesis block definition is available at `/genesis` URI.

### Proof of Work

For a block to appear as valid, the `nonce` should be chosen so that the computed `hash`
is less than a certain number (also known as difficulty). In our simple system, we'll define
difficulty as number of leading `0` in the hex representation of the hash. So if we have
to generate a block of difficulty `4`, the hash should read as `0000...` in hex. Notice
that the genesis block has a difficulty of 8.

### Block Chain and Validation API

A chain is an array of blocks, each referring to the previous block by its hash (in the field
`previous_hash`). The first block in the chain MUST always be the genesis block, and that
fixes `previous_hash` of the first block to `00000000c55f6538ae0a9d1e094c41781f4d05d789ab435c5ec1d4b8bd8738ba`.

An example of a chain would look like:
```
[
  {
    "identifier": "000102030405060708090A0B0C0D0E0F",
    "nonce": 3754873684,
    "data": "Genesis Block for CTF contest, all block chains must start with this block. This is equivalent to Big Bang, time didn't exist before this",
    "previous_hash": null
  },
  {
    "nonce": 37947,
    "previous_hash": "00000000c55f6538ae0a9d1e094c41781f4d05d789ab435c5ec1d4b8bd8738ba",
    "data": "first",
    "identifier": "d056b19d92e14b018482371f46f8ebc5"
  }
]
```

## CTF Contest

Given the above definitions, post a valid block chain of length at least 4 to URL `/validate` to expose the flag.

The difficulty of the respective blocks in the array is 8 (genesis block), 4, 4, 5, 6, 7, 9, 11, 13, 16.

#### Example Solution

```
$ cat chain.json
[ { "identifier": "000102030405060708090A0B0C0D0E0F", "nonce": 3754873684, ... },
  { "identifier": "1f4d05d789a4bc5ec41781", "nonce": 4653, ...},
  { "identifier": "41781f4d0500c55f6538ae0a9d", "nonce": ... },
  { "identifier": "55f6538ae0a9d1e094c41", "nonce": ... }
]

$ curl http://ctf-2017.captchaflag.com:9008/validate -d@chain.json -H "Content-type: application/json"
flag{...}
```
