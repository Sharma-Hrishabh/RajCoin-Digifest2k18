# Rajasthan-Hackathon
## Idea Description :
Developing RajCoins cryptocurrency system(block-chain) using Bhamashah API where users can transact each other with RajCoins. 
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
- Python - 2.7 or later
- Pip
- VirtualEnvironment

## Setting up virtual env:
The first thing you will need to do is install pip. If you have setuptools installed, which you most likely will with most modern platforms, you can install pip through easy_install:
easy_install pip
Next, you'll need to install virtualenv with pip:
pip install virtualenv
Finally, I would highly recommend installing virtualenvwrapper as it makes it much easier to create and start virtual environments:
pip install virtualenvwrapper
As part of the install instructions for virtualenvwrapper, you need to add this to your .bash_profile"-
 # virtualenv
export WORKON_HOME=$HOME/.virtualenvs
source /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh
[Please note that this path may differ depending on what version of Python you have. 
Also, I like to keep all my virtualenvs in a directory called .virtualenvs in my home directory, 
but this may differ for you if you choose to keep your virtual environments in a different directory.]

Make sure you source your new .bash_profile

source ~/.bash_profile

...and that's it! Now you're all set to start using virtual environments!

To create and start a new virtual environment with --no-site-packages, enter:
virtualenv ~/name_of_folder_where_to_create_virtualenv/virtual_env_name

### Activation of virtualenv
cd ~/name_of_folder_where_to_create_virtualenv/virtual_env_name/bin
source activate


now at this stage u can install packages like Django here

cd ..
pip install Django

after this clone repositery in current directory
git clone https://github.com/Sharma-Hrishabh/digifest2k18

[for better working use 'digifest2k18' as virtualenv name]


## Screenshot of app:







## Understanding Block-Chain:
![alt text](https://github.com/Sharma-Hrishabh/digifest2k18/blob/master/dbsnap.jpeg)
