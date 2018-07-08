# Rajasthan-Hackathon
## Idea Description :
Developing RajCoins cryptocurrency system(block-chain) using Bhamashah API where users can transact each other with RajCoins. 

The backbone of successful cryptocurrency lies in its design of Blockchain.

A blockchain thrives through a combination of decentralized, encrypted, anonymous, immutable and Trustless (that means that everything is trustworthy).


## How will it function:
Our **"Bhamashah_API"** based Cryptocurrency lets user create an account using their Bamashah_ID , and on logging in it provides the user with 10 mining reward coins.

The integrity of the blockchain is maintained by its unique **algorithm** , which lets every user access the *copy* of the database but not actual database.
The blockchain contains the following fields:
- index
- data(transaction description)
- senderKey
- ReceiverKEY
- amount(transferred)
- **previousHash**       (storing *sha256* hash of the previous node)
- **hashe**       (storing hashe of self block in sha256 format)


last two lines are the **main crisps** and the thing that maintains the **integrity** of the blockchain and what gives the power to it to make it **non-temparable**.

##### following is the database created by adding of nodes of every trransaction in the the blockchain:

![alt text](https://github.com/Sharma-Hrishabh/digifest2k18/blob/master/dbsnap.jpeg)

it can be seen that **previoushash** field of every block contains **hashe** of another block.

'''CLASS BLOCKCHAIN

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


'''

A blockchain class makes it away from the users use... and its noticeable that how this class only returns a **copy of the blockDB** - our original data.


#### the users table contains md5() encrypted bhamashahid: hence making it anonymous
![alt text](https://github.com/Sharma-Hrishabh/digifest2k18/blob/master/1.png)


## Application Background
### Technical Details
## Attributes of a user:
- username(Bhamashah Id)
- Firstname(extracted using Bhamashah)
- Lastname(extracted using Bhamashah)
- Balance

## Setting up the development environment

Overview:
In order to run this project on your system, django-framework(ver-1.9) to be setup with python 2.7 

### Prerequisites
- Git Client
- Django - 1.9
- Python - 2.7
- Pip
- VirtualEnvironment

## Setting up virtual env:
The first thing you will need to do is install pip.
>sudo apt-get install python-pip    
If you have setuptools installed, which you most likely will with most modern platforms, you can install pip through easy_install:
>easy_install pip
Next, you'll need to install virtualenv with pip:
>pip install virtualenv
Finally, I would highly recommend installing virtualenvwrapper as it makes it much easier to create and start virtual environments:
>pip install virtualenvwrapper
As part of the install instructions for virtualenvwrapper, you need to add this to your .bash_profile"-
virtualenv
>export WORKON_HOME=$HOME/.virtualenvs
>source /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh
[Please note that this path may differ depending on what version of Python you have. 
Also, I like to keep all my virtualenvs in a directory called .virtualenvs in my home directory, 
but this may differ for you if you choose to keep your virtual environments in a different directory.]

Make sure you source your new '.bash_profile'

>source ~/.bash_profile

...and that's it! Now you're all set to start using virtual environments!

To create and start a new virtual environment with --no-site-packages, enter:
>virtualenv ~/name_of_folder_where_to_create_virtualenv/virtual_env_name

### Activation of virtualenv
>cd ~/name_of_folder_where_to_create_virtualenv/virtual_env_name/bin
>source activate


Now at this stage u can install packages like Django here

>cd ..
>pip install Django

After this clone repositery in current directory
>git clone https://github.com/Sharma-Hrishabh/digifest2k18

[for better working use 'digifest2k18' as virtualenv name]



# Current_Version_Bugs
- for making transaction,currently login is not necessary,[@login function can be used in future releases ]
- updation of amount of money that user has is not working
- in mobile view ,toggle button is not apperaing,but if we tap at rightmost uppercorner navigation bar slides from right
- after selling coins redirect function is not working





## Developed for Rajasthan Hackathon

