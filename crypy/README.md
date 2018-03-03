# CryPy

There is a lot of buzz on ransomwares. Here I am attaching the real source of crypy [1]. This is modified a little to run on Linux (actually made it portable).
However I am introducing an weakness here. This guy chooses a random 128 bit key to encrypt each file (and throws the key away, it has no intention to give
the key back when paid). What I am planning to add a line random.seed(<timestamp>) at the beginning. This way, for every run, if the timestamp is different
it'll produce different pseudo random sequence, or if seed is made the same, the sequence it produces will be the same.

## Challenge creation

The challenge to be given is: first create a plaintext file having the flag. Then run crypy on it. Publish the encrypted file and crypy source as a tarball.

### How to solve

The contestant has to brute-force the seed (the timestamp of the encrypted file preserved by tar may help). And then follow the exact sequence to
random.choice() etc calls (because there are many more, e.g filename generation) to reproduce the key, and then call AES.decrypt() to check if the decrypted file has the flag.

This also teaches a lesson that security is as good as the weakest link. And this gives a first hand look at a real ransomware.


 1. https://github.com/roothaxor/Ransom/blob/master/CryPy_Source.py
 