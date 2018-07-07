import urllib2
import json


def soup(bhama):
    bhama = "https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/family/details/" + bhama + "?client_id=ad7288a4-7764-436d-a727-783a977f1fe1"
    
    page = urllib2.urlopen(bhama)
    
    from bs4 import BeautifulSoup
    
    
    soup = BeautifulSoup(page)
    
    return str(soup)



def returnBhama(bhama):
    data = soup(bhama)
    index = data.find("BHAMASHAH_ID")
    print(data[index+15:index+30])
    
def returnFirstLastName(bhama):
    data = soup(bhama)
    indexName = data.find('"NAME_ENG"')
    string = data[indexName + 12 :]
    indexQuote = string.find('"')
    name = data[indexName + 12 : indexName + indexQuote + 6] 
    
    print(name)
    
    nameComp = name.split()
    return nameComp[0] , nameComp[-1]           # firstName , lastName = returnFirstLastName()
    
    
print(returnFirstLastName("1207-HOTX-20756"))