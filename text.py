from .models import blockDB
from hashlib import sha256
import time
import json



class block:
	def __init__(self, index, data, timestamp, amount, sender, receiver ,previousHash = ''):
		selffrom .models import blockDB
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
		self.hashe = ''
		
		
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
		self.chain = [self.createGenesis()]
		self.difficulty = 2

	def createGenesis(self):
		return block(0 , "Created a genesis Block", time.ctime(), 10 , 'Govenment', 'Govenment', "0")

	def getLatestBlock(self):
		return self.chain[-1]

	def addBlock(self, newBlock):
		newBlock.previousHash = self.getLatestBlock().hashe
		newBlock.hashe = newBlock.calculateHash()
		self.chain.append(newBlock)

	def isChainValid(self):
		for i in range(1, len(self.chain) - 1):
			previousNode = self.chain[i-1]
			currentNode = self.chain[i]

		if not currentNode.hashe == currentNode.calculateHash():
			return False

		if not previousNode.hashe == currentNode.previousHash:
			return False

		return True


crypto = blockchain()

# mining and printing JSON for block 1
crypto.addBlock(block(1, "First User added", time.ctime(), 10, "GOVERNMENT", "first_user" ,) )
lastNode = crypto.getLatestBlock()



point = block(1, "First User added", time.ctime(), 10, "GOVERNMENT", "first_user" , sha256(a.encode()).hexdigest())


# code that copies original db into testdb
testblockDB.objects.all.delete()
tempDB = testblockDB()
tempDB = blockDB.objects.all()
tempDB.save()


b = testblockDB(data = str(point.data), time = str(point.timestamp), previousHash = str(point.previousHash), hashe = point.hashe, senderKey = str(point.sender), receiverKey = str(point.receiver), amount = float(point.amount) )
#b = blockDB.objects.create(data = "hdhfjf", time = "2018-11-01", previousHash = "baca", hashe = "hdfjf", senderKey = "hfhjg", receiverKey = "hfjjf", amount = 0.0 )

b.save()

if checkValidity(point):
	
	

print("-------> Block 1 Mined.......")

print(lastNode.hashe)


'''
data = {
	'index'	: lastNode.index,
	'data'	: lastNode.data,
	'previousHash' : lastNode.previousHash.hexdigest(),
	'currentBlock' : lastNode.hashe.hexdigest(),
	
	'sender'	:	lastNode.sender,
	'receiver'	:	lastNode.receiver,
	'time'		: 	lastNode.timestamp,
}

print(json.dumps(data))
'''


blockChain = testblockDB.objects.all()

def newNode(dataList):
	
	lastBlock = blockDB.objects.order_by('-time')[0]
	prevHash = lastBlock.hashe
	
	point = block(3, dataList[0], time.ctime(), dataList[1], dataList[2], dataList[3], prevHash)  
	point.calculateHash()
	
	# put "point" into transactions database
	b = blockDB(data = str(point.data), time = str(point.timestamp), previousHash = str(point.previousHash), hashe = point.hashe, senderKey = str(point.sender), receiverKey = str(point.receiver), amount = float(point.amount) )
	# b=blockDB(data = "hdhfjf", time = "2018-11-01 00:00:00", previousHash = "baca", hashe = "hdfjf", senderKey = "hfhjg", receiverKey = "str(point.receiver)", amount = 0.0 )
	re = b.save()
	print(re)
	# checking validity of the chain
	
	if checkValidity(point) == True:
		blockDB.objects.all.delete()
		tempDB = blockDB()
		tempDB = testblockDB.objects.all()
		tempDB.save()
		testblockDB.objects.all.delete()
		return True
	else:
		return False
    
    
    
def checkValidity(point):
	
	for i in range(1, len(blockChain)):
		previousNode = blockChain[i]
		currentNode = blockChain[i-1]
		
		if not currentNode == point.calculateHash():
			return False
		if currentBlock.previousHash == previousNode.hashe:
			return False  
			
	return True
	
	
	
	
	
	#blockDB.objects.all()
	##blockDB.objects.all()[0].hashe
	.index = index
		self.data  = data
		self.previousHash = previousHash
		self.amount = amount
		self.sender = sender
		self.receiver = receiver
		self.timestamp = timestamp
		self.nonce = 0
		self.hashe = ''
		
		
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
		self.chain = [self.createGenesis()]
		self.difficulty = 2

	def createGenesis(self):
		return block(0 , "Created a genesis Block", time.ctime(), 10 , 'Govenment', 'Govenment', "0")

	def getLatestBlock(self):
		return self.chain[-1]

	def addBlock(self, newBlock):
		newBlock.previousHash = self.getLatestBlock().hashe
		newBlock.hashe = newBlock.calculateHash()
		self.chain.append(newBlock)

	def isChainValid(self):
		for i in range(1, len(self.chain) - 1):
			previousNode = self.chain[i-1]
			currentNode = self.chain[i]

		if not currentNode.hashe == currentNode.calculateHash():
			return False

		if not previousNode.hashe == currentNode.previousHash:
			return False

		return True
		

# making a copy of blockchain data
#blockChain = blockDB.objects.all()

def checkValidity(point):
	
	checkDBlist = testblockDB.objects.all()
	
	for i in range(1, len(blockChain)):
		previousNode = blockChain[i]
		currentNode = blockChain[i-1]
		
		if not currentNode == point.calculateHash():
			return False
		if currentBlock.previousHash == previousNode.hashe:
			return False  
			
	return True
	
		
		
def newNode(dataList):
	
	# making a temporary DB
	tempDB = testblockDB()
	tempDB = blockDB.objects.all()                 # copying blockChain data to new temporary data
	tempDB.save()
	
	
	lastBlock = testblockDB.objects.order_by('-time')[0]
	prevHash = lastBlock.hashe
	
	# saving form Data to block object i.e. a new node
	point = block(3, dataList[0], time.ctime(), dataList[1], dataList[2], dataList[3], prevHash)  
	point.hashe = point.calculateHash()
	
	# put "point" into testing database
	b = testblockDB(data = str(point.data), time = str(point.timestamp), previousHash = str(point.previousHash), hashe = point.hashe, senderKey = str(point.sender), receiverKey = str(point.receiver), amount = float(point.amount) )
	b.save()        # adding block to temporary DB
	
	tempDB = testblockDB.objects.all()
	if checkValidity(tempDB) == True:
		return True
	else:
		return False
    