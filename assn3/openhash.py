class OpenHash:
    """
    OpenHash-based implementation of DIctionary ADT
    """

    def __init__(self, buckets):
        self.ht = [[]] * buckets

    def __getitem__(self, key):
        i = self._getHash(key)
        while len(self.ht[i]) > 0:
            if self.ht[i][0] == key:
                return self.ht[i][1]
            else:
                i+=1

    def _getHash(self, key):
        return ord(key[0]) % len(self.ht)

    # @staticmethod
    def insert(self, x, h):
        i = self._getHash(x)
        c = 0
        while len(self.ht[1]) > 0:
            if c > len(self.ht):
                print('Full HashTable')
            i += 1 if i < (len(self.ht) -1) else 0
            c += 1
        self.ht[i] = [x, h]

    # @staticmethod
    def delete(self, x):
        i = self._getHash(x)
        while len(self.ht[1]) > 0:
            if self.ht[i][0] == x:
                self.table[i] = []
                return 1
            else:
                i += 1
        print('Key not in HashTable')


    # @staticmethod
    # def MEMBER(x, H):
    #
    #
    # @staticmethod
    # def MAKENULL(H):
    #    pass

def time(out):
    pass

if __name__ == "__main__":
    dict = OpenHash(250)

    print('Vals Instertion')
    dict.insert('Key','Val')
    dict.insert('other','other val')
    print('\nThe values of \'key\' is :', dict['Key'])

    print('Deleting \'key\' from dictonary')
    dict.delete('Key')


    try:
        print('The value of \'Key\' is :', dict['Key'])
    except:
        print('Unable to find node; deletion successful.')


    print("Shit done")
