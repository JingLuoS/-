import rsa

class RSAKey:
    def __init__(self):

        self.n = None
        self.e = 0

    def setPublic(self, N, E):

        if N is not None and E is not None and len(N) > 0 and len(E) > 0:
            self.n = int(N, 16)
            self.e = int(E, 16)
        else:
            raise ValueError

    def encrypt(self, text):

        if text is None:
            return None
        pubkey = rsa.PublicKey(self.n, self.e)
        text = text.encode("utf8")
        entext = rsa.encrypt(text, pubkey)
        return ''.join([("%x" % x).zfill(2) for x in entext])
   

