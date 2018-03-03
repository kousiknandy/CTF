from bottle import request, route, run, abort, response
import block, blockchain
import json

genesis_block = block.Block(data="Genesis Block for CTF contest, all block chains must "
                            "start with this block. This is equivalent to Big Bang, time "
                            "didn't exist before this", block_id="000102030405060708090A0B0C0D0E0F",
                            nonce=3754873684)

@route('/validate', method='POST')
def validate():
    blocks = request.json
    if not isinstance(blocks, list):
        abort(400, "Expecting a block chain array as data")
    chain = blockchain.Blockchain()
    difficulty = 4
    for idx, elem in enumerate(blocks):
        try:
            print(elem)
            one_block = block.Block(data=elem["data"], block_id=elem["identifier"],
                               previous_hash=elem["previous_hash"], nonce=elem["nonce"])
            print(one_block)
            difficulty += idx // 3
            if not one_block.acceptable(difficulty):
                abort(400, "Block {} wasn't mined with required difficulty {}".format(
                    elem["identifier"], difficulty))
            if (idx == 0 or not one_block.previous_hash) and \
               one_block.hash() != "00000000c55f6538ae0a9d1e094c41781f4d05d789ab435c5ec1d4b8bd8738ba":
                abort(400, "Only genesis block, obtained from /genesis can start a chain")

            chain.add_block(one_block, precomputed=True)
        except Exception as err:
            abort(400, "Malformed block in chain: {}".format(str(err)))
    print(chain)
    if len(chain) < 4:
        abort(400, "At least a chain of length 4 is required")
    if chain.broken:
        abort(400, "Block chain broken")
    response.content_type = 'text/plain'
    return "flag{Bl0CK_chaIn_Ea5Y_to_CreAte}\n"

@route('/genesis', method='GET')
def genesis():
    response.content_type = 'application/json'
    return json.dumps(genesis_block.__dict__)

@route('/hashfunction', method='GET')
def hashfunction():
    response.content_type = 'text/plain'
    return """
        import hashlib
        def hash(identifier, nonce, data, previous_hash):
          message = hashlib.sha256()
          message.update(str(identifier).encode('utf-8'))
          message.update(str(nonce).encode('utf-8'))
          message.update(str(data).encode('utf-8'))
          message.update(str(previous_hash).encode('utf-8'))
          return message.hexdigest()
"""

run(host='0.0.0.0', port=8880)

