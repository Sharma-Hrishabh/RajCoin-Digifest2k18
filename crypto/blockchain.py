from .models import blockDB
from hashlib import sha256
import time
import json



class block:
	def __init__(self, index, data, timestamp, amount, sender, receiver ,previousHash = ''):
		self.index = index
		self.data  = data
		self.previousHash = previousHash
		self.amount = amount
		self.sender = sender
		self.receiver = receiver
		self.timestamp = timestamp
		self.nonce = 0
		self.hashe = self.calculateHash()
		
		
	def calculateHash(self):
		# returning hash for a set of data
		return sha256((str(self.index) + str(self.data) + str(self.amount) + str(self.sender) + str(self.receiver) 
					+ str(self.timestamp) + str(self.nonce) + str(self.previousHash)).encode()).hexdigest()

	#def mineBlock(self, difficulty):
	#	codeHash = str(self.hashe)[0:difficulty]
	#	while not codeHash == "0"*difficulty:
	#		self.nonce += 1 


class blockchain:
	def __init__(self):
		chain = blockDB.objects[0]

		if not chain:
			self.createGenesis(self)

		self.difficulty = 2


	def createGenesis(self):
		point = block(0, "This is a Genesis Block", time.ctime(), 0, "GOVERNMENT", "GOVERNMENT" , sha256(a.encode()).hexdigest())

		temp = blockDB(data = str(point.data), time = str(point.timestamp), previousHash = str(point.previousHash), hashe = point.hashe, senderKey = str(point.sender), receiverKey = str(point.receiver), amount = float(point.amount) )
		
		temp.save()
	
	def returnDbCopy(self):
		originalDB = blockDB.objects.all()
		return  originalDB
		
	def addNewNode(self, temp):
		node = blockDB()
		node = temp
		node.save()

		

# making a copy of blockchain data
#blockChain = blockDB.objects.all()


def checkValidity(tempHashes, point.hashe):
	
	for i in range(1, len(tempHashes)):
		previousNodeHash = tempHashes[i-1].hashe
		currentNodePrevHash  = tempHashes[i].previousHash
		currentNodeHash = tempHashes[i].hashe
		
		
		if not currentNodePrevHash == previousNodeHash:
			return False

	if not currentNodeHash == point.hashe:
			return False

	return True

		
def newNode(dataList):
	
	RajCoins = blockChain()

	# making a temporary DB
	tempDB = testblockDB()
	tempDB = RajCoins.returnDbCopy()                 # copying blockChain data to new temporary data
	tempDB.save()
	
	
	lastBlock = testblockDB.objects.order_by('-time')[0]
	prevHash = lastBlock.hashe
	
	# saving form Data to block object i.e. a new node
	point = block(3, dataList[0], time.ctime(), dataList[1], dataList[2], dataList[3], prevHash)  
	point.hashe = point.calculateHash()
	
	# put "point" into testing database
	temp = testblockDB(data = str(point.data), time = str(point.timestamp), previousHash = str(point.previousHash), hashe = point.hashe, senderKey = str(point.sender), receiverKey = str(point.receiver), amount = float(point.amount) )
	
	temp.save()

	# putting previous and current node hashes of all rows in testblockDB into a list
	temp = testblockDB.objects.values('previousHash', 'hashe')

	if checkValidity(temp, point.hashe):
		# add data to original DB
		tempo = testblockDB(data = str(point.data), time = str(point.timestamp), previousHash = str(point.previousHash), hashe = point.hashe, senderKey = str(point.sender), receiverKey = str(point.receiver), amount = float(point.amount) )
		RajCoins.addNewNode(tempo)
		return True, ""

	else:
		#exception
		#redirect to error.html
		
		return False, "Invalid Transaction"