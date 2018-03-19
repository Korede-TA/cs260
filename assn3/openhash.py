import time
class OpenHash:
	"""
	OpenHash-based implementation of DIctionary ADT
	"""

	def __init__(self, buckets):
		self.icount = 0
		self.dcount = 0
		self.ht = [[]] * buckets

	def __getitem__(self, key):
		i = self._getHash(key)
		while len(self.ht[i]) > 0:
			if self.ht[i][0] == key:
				return self.ht[i][1]
			else:
				i+=1

	def _getHash(self, key):
		return ord(key[0])%len(self.ht)

	# @staticmethod
	def insert(self, x, h):
		i = self._getHash(x)
		c = 0
		while len(self.ht[i]) > 0:
			if c > len(self.ht):
				print('Full HashTable')
			i += 1 if i < (len(self.ht) -1) else 0
			c += 1
		self.ht[i] = [x, h]
		self.icount += c
		# print(self.icount)

	# @staticmethod
	def delete(self, x):
		i = self._getHash(x)
		c = 0
		while len(self.ht[i]) > 0:
			if self.ht[i][0] == x:
				self.ht[i] = []
				# print("deletetime: ",self.dcount)
				return 1
			else:
				i += 1
				c += 1
				self.dcount += c
		print('Key not in HashTable')

	def printAll(self):
		for i in range(0, len(self.ht)):
			hash = self.ht[i]
			if len(hash)>0:
				print("index is: "+str(str(i))+" key is: \""+hash[0]+"\" hash is: \""+hash[1]+"\"")


	# @staticmethod
	# def MEMBER(x, H):
	#
	#
	# @staticmethod
	# def MAKENULL(H):
	#    pass


if __name__ == "__main__":
	dict = OpenHash(10)

	print('Values Instertion')
	insertTime=0
	start=time.perf_counter()
	dict.insert("Sree", "Kuttan")
	end=time.perf_counter()
	insertTime+=(end-start)*1000
	start=time.perf_counter()
	dict.insert('CS260','Knowak')
	end=time.perf_counter()
	insertTime+=(end-start)*1000
	start=time.perf_counter()
	dict.insert('cs260ta','Wei')
	end=time.perf_counter()
	insertTime+=(end-start)*1000
	start=time.perf_counter()
	dict.insert('Drexel',"University")
	end=time.perf_counter()
	insertTime+=(end-start)*1000
	dict.printAll()
	print("Average time(in seconds) took to insert 4 items to size 10 is: ",insertTime/4)

	print('Deleting the 4 items from OpenHash table')
	deleteTime=0
	start=time.perf_counter()
	dict.delete('Sree')
	end=time.perf_counter()
	deleteTime+=(end-start)*1000
	start=time.perf_counter()
	dict.delete('CS260')
	end=time.perf_counter()
	deleteTime+=(end-start)*1000
	start=time.perf_counter()
	dict.delete('cs260ta')
	end=time.perf_counter()
	deleteTime+=(end-start)*1000
	start=time.perf_counter()
	dict.delete('Drexel')
	end=time.perf_counter()
	deleteTime+=(end-start)*1000
	print("Average time(in seconds) took to delete 4 items to size 10 is: ",deleteTime/4)
	dict.printAll()

	dict = OpenHash(1000)

	print('Values Instertion')
	insertTime=0
	start=time.perf_counter()
	dict.insert("Sree", "Kuttan")
	end=time.perf_counter()
	insertTime+=(end-start)*1000
	start=time.perf_counter()
	dict.insert('CS260','Knowak')
	end=time.perf_counter()
	insertTime+=(end-start)*1000
	start=time.perf_counter()
	dict.insert('cs260ta','Wei')
	end=time.perf_counter()
	insertTime+=(end-start)*1000
	start=time.perf_counter()
	dict.insert('Drexel',"University")
	end=time.perf_counter()
	insertTime+=(end-start)*1000
	dict.printAll()
	print("Average time(in seconds) took to insert 4 items to size 1000 is: ",insertTime/4)

	print('Deleting the 4 items from OpenHash table')
	deleteTime=0
	start=time.perf_counter()
	dict.delete('Sree')
	end=time.perf_counter()
	deleteTime+=(end-start)*1000
	start=time.perf_counter()
	dict.delete('CS260')
	end=time.perf_counter()
	deleteTime+=(end-start)*1000
	start=time.perf_counter()
	dict.delete('cs260ta')
	end=time.perf_counter()
	deleteTime+=(end-start)*1000
	start=time.perf_counter()
	dict.delete('Drexel')
	end=time.perf_counter()
	deleteTime+=(end-start)*1000
	print("Average time(in seconds) took to delete 4 items to size 1000 is: ",deleteTime/4)
	dict.printAll()

	print("PA3 #1 Done")
