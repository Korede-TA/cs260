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
		print(len(self.ht))
		return ord(key[0])%len(self.ht)

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

	def printAll(self):
		for i in range(0, len(self.ht)):
			hash = self.ht[i]
			if len(hash)>0:
				print("index is: "+str(i)+" key is: \""+hash[0]+"\" hash is: \""+hash[1]+"\"")


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
	dict = OpenHash(25)

	print('Vals Instertion')
	dict.printAll()
	dict.insert('Key','Val')
	dict.printAll()
	dict.insert('other','other val')
	dict.printAll()
	print('\nThe values of \'key\' is :', dict['Key'])

	print('Deleting \'key\' from dictonary')
	dict.printAll()
	dict.delete('Key')
	dict.printAll()


	try:
		print('The value of \'Key\' is :', dict['Key'])
	except:
		print('Unable to find node; deletion successful.')


	print("Shit done")