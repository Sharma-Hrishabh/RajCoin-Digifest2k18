from .models import blockDB
from .models import testblockDB, userFile
from hashlib import sha256, md5
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
		chain = blockDB.objects.all().first()

		if not chain:
			self.createGenesis()

		self.difficulty = 2


	def createGenesis(self):
		point = block(0, "This is a Genesis Block", time.ctime(), 0, "GOVERNMENT", "GOVERNMENT" ,"000000")

		temp = blockDB(data = str(point.data), time = str(point.timestamp), previousHash = str(point.previousHash), hashe = point.hashe, senderKey = str(point.sender), receiverKey = str(point.receiver), amount = float(point.amount) )
		
		temp.save()
	

	
	def returnDbCopy(self):
		
		tempData = blockDB.objects.all()
		testblockDB.objects.all().delete()
		
		for temp in tempData:
			node = testblockDB()
			
			node.data = temp.data
			node.time = temp.time
			node.previousHash = temp.previousHash
			node.hashe = temp.hashe
			node.senderKey = temp.senderKey
			node.receiverKey = temp.receiverKey
			node.amount = temp.amount
			node.save()
		
		return testblockDB
		
	def addNewNode(self, temp):
		node = blockDB()
		node.data = temp.data
		node.time = temp.time
		node.previousHash = temp.previousHash
		node.hashe = temp.hashe
		node.senderKey = temp.senderKey
		node.receiverKey = temp.receiverKey
		node.amount = temp.amount
		print("node : " , node)
		node.save()


# making a copy of blockchain data
# blockChain = blockDB.objects.all()

# ------------------------------------------------checking validity function -----------------------------------------
def checkValidity(tempHashes, hashe):
	
	
	for i in range(1, len(tempHashes)):
		previousNodeHash = tempHashes[i-1]['hashe']
		currentNodePrevHash  = tempHashes[i]['previousHash']
		currentNodeHash = tempHashes[i]['hashe']
		
		# print("Checkvalidity currentnodeHash: ", currentNodeHash)
		# print("checkvalidity currentnodePrevHash: ", currentNodePrevHash)
		# print("checkvalidity PrevnodeHash: ", previousNodeHash)
		
		
		if not currentNodePrevHash == previousNodeHash:
			return False
		
	
	
	#if not currentNodeHash == hashe:
	#		return False

	return True



# ----------------------------------------------------New Node function -----------------------------------------------		
def newNode(dataList):
	
	RajCoins = blockchain()
	
	# making a temporary DB
	tempDB = RajCoins.returnDbCopy()                 # copying blockChain data to new temporary data temp = tempblockDB.objects,all()
	
	
	#  tempDB.latest().all().latest('vfb')
	lastBlock = tempDB.objects.latest('id')
	
	if not lastBlock:
		raise Exception('empty Empty!')
	else:
		prevHash = lastBlock.hashe
	
	# saving form Data to block object i.e. a new node
	point = block(3, dataList[0], time.ctime(), dataList[1], dataList[2], dataList[3], prevHash)  
	point.hashe = point.calculateHash()
	
	# print("point = " , dataList)
	
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
		
		
# -----------------------------------------------------------------add registration reward-----------------------------------------------------
def registrationReward(userid):
	person = userFile()
	person.userid = md5(str(userid).encode()).hexdigest()			# returning sha64 hashed userid
	
	data = ["This is a New register Mining Reward by Rajasthan Government!", "10", "Government", userid]
	
	# mining new user 
	newNode(data)
	
	person.balance = (person.balance + 10.0 )
	person.lastMod = time.ctime()
	
	
	# updating new user's record
	person.save()
