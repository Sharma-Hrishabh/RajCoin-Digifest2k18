# from . import models
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
		# self.hashe = ''
		self.nonce = 0
		self.hashe = calculatehash()

	def calculateHash(self):
		# returning hash for a set of data
		return sha256((str(self.index) + str(self.data) + str(self.amount) + str(self.sender) + str(self.receiver) 
					+ str(self.timestamp) + str(self.nonce) + str(self.previousHash)).encode()).hexstring()

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
crypto.addBlock(block(1, "First User added", time.ctime(), 10, "GOVERNMENT", "first_user" ) )
lastNode = crypto.getLatestBlock()

print("-------> Block 1 Mined.......")

print(lastNode.hashe.hexdigest())


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

def newNode(dataList):
	lastBlock = blockDB.objects.order_by('-time')[0]
	prevHash = lastBlock.hashe
	point = block(index=3, dataList[0], time.ctime(), dataList[1], dataList[2], dataList[3], prevHash)  
	point.calculateHash()
	
	# put "point" into transactions database
	b = blockDB(data = str(point.data), time = str(point.timestamp), previousHash = str(point.prevHash), hashe = point.hashe.hexstring(), senderKey = str(point.sender), recieverKey = str(point.receiver), amount = float(point.amount) )
	b.save()
	#take data from point and assign to each column of object of class blockDB
	#and save this data in db
	
   
	"""
    
    if checkValidity() == True:
    	return True
    else:
    	return False
    
    
    
def checkValidity():
	