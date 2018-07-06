from models.py import
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
		self.hash = ''
		self.nonce = 0

	def calculateHash(self):
		# returning hash for a set of data
		return sha256((str(self.index) + str(self.data) + str(self.amount) + str(self.sender) + str(self.receiver) + str(self.timestamp) + str(self.nonce) + str(self.previousHash)).encode())

	def mineBlock(self, difficulty):
		while not (sha256(self.hash)).hexdigest()[0:difficulty] == "0"*difficulty:
			self.nonce += 1 


class blockchain:
	def __init__(self):
		self.chain = [self.createGenesis()]
		self.difficulty = 2

	def createGenesis(self):
		return block(0 , "Created a genesis Block", time.ctime(), 10 , 'Govenment', 'Govenment', "0")

	def getLatestBlock(self):
		return self.chain[-1]

	def addBlock(self, newBlock):
		newBlock.previousHash = self.getLatestBlock().hash
		newBlock.mineBlock(self.difficulty)
		self.chain.append(newBlock)

	def isChainValid(self):
		for i in range(1, len(self.chain) - 1):
			previousNode = self.chain[i-1]
			currentNode = self.chain[i]

		if not currentNode.hash == currentNode.calculateHash():
			return False

		if not previousNode.hash == currentNode.previousHash:
			return False

		return True


crypto = blockchain()

# mining and printing JSON for block 1
crypto.addBlock(block(1, "First User added", time.ctime(), 10, "GOVERMENT", "first_user" ) )
lastNode = crypto.getLatestBlock()

print("-------> Block 1 Mined.......")

data = {
	'index'	: lastNode.index,
	'data'	: lastNode.data,
	'previousHash' : lastNode.previousHash.hexdigest(),
	'currentBlock' : lastNode.hash.hexdigest(),
	
	'sender'	:	lastNode.sender,
	'receiver'	:	lastNode.receiver,
	'time'		: 	lastNode.timestamp,
}

print(json.dumps(data))


# mining and printing JSON for block 1
crypto.addBlock(block(2, "Second User added", time.ctime(), 5, "GOVERMENT", "second_user") )
lastNode = crypto.getLatestBlock()

print("-------> Block 1 Mined.......")

data = {
	'index'	: lastNode.index,
	'data'	: lastNode.data,
	'previousHash' : lastNode.previousHash.hexdigest(),
	'currentBlock' : lastNode.hash.hexdigest(),
	
	'sender'	:	lastNode.sender,
	'receiver'	:	lastNode.receiver,
	'time'		: 	lastNode.timestamp,
}

print(json.dumps(data))