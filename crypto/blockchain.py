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
		return sha256((str(self.index) + str(self.data) + str(self.amount) + str(self.sender) + str(self.receiver) + str(self.timestamp) + str(self.previousHash)).encode())

class blockchain:
	def __init__(self):
		self.chain = [self.createGenesis()]

	def createGenesis(self):
		return block(0 , "Created a genesis Block", time.ctime(), 10 , 'Govenment', 'Govenment', "0")

	def getLatestBlock(self):
		return self.chain[-1]

	def addBlock(self, newBlock):
		newBlock.previousHash = self.getLatestBlock().hash
		newBlock.hash = newBlock.calculateHash()
		self.chain.append(newBlock)

	def isChainValid(self):
		for i in range(1, len(self.chain) - 1):
			previousNode = self.chain[i-1]
			currentNode = self.chain[i]

		if currentNode.hash != currentNode.calculateHash():
			return False

		if previousNode.hash != currentNode.previousHash:
			return False

		return True


crypto = blockchain()

crypto.addBlock(block(1, "First User added", time.ctime(), 10, "GOVERNMENT", "first_user" ) )
crypto.addBlock(block(2, "Second User added", time.ctime(), 5, "GOVERNMENT", "second_user") )

lastNode = crypto.getLatestBlock()

data = {
	'index'	: lastNode.index,
	'data'	: lastNode.data,
	'previousHash' : lastNode.previousHash.hexdigest(),
	'currentBlock' : lastNode.hash.hexdigest(),
	
	'sender'	:	lastNode.sender,
	'receiver'	:	lastNode.receiver,
	'time'		: 	lastNode.timestamp,
}

print(str(crypto.chain[1].amount) + "\n\n" + str(crypto.chain[2].amount))

print(json.dumps(data, indent=4))