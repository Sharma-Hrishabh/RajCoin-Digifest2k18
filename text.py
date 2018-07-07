{
    "hof_Details": {
        "AADHAR_ID": "734094301964",
        "STATE": "Rajasthan",
        "MOTHER_NAME_ENG": "ratna devi",
        "DOB": "01-JAN-88",
        "BHAMASHAH_ID": "1067-7PVQ-28383",
        "VILLAGE_CODE": "078167",
        "RSBY_STATUS": "N",
        "STREET": "ward 5",
        "M_ID": "0",
        "FAMILYIDNO": "WDDQMOW",
        "FATHER_NAME_HND": "प्यारेलाल ",
        "PIN_CODE": "321608",
        "GP_WARD": "0810905420",
        "DISTRICT_CODE": "109",
        "SPOUCE_NAME_ENG": "dhoojiram gurjar",
        "IS_RURAL": "Y",
        "HOUSE_NUMBER": null,
        "SPOUCE_NAME_HND": "धूजीराम गुर्जर ",
        "RSBY_URN_NUMBER": null,
        "NFSA_STATUS": "Y",
        "NFSA_BPL_NUMBER": null,
        "RATION_CARD_NO": "007816701259",
        "NAME_ENG": "mundar devi gurjar",
        "GENDER": "Female",
        "FATHER_NAME_ENG": "pyarelal",
        "NAME_HND": "मुन्दर देवी गुर्जर ",
        "MOTHER_NAME_HND": "रत्ना देवी ",
        "BLOCK_CITY": "0810905"
    },
    "family_Details": [
        {
            "AADHAR_ID": "766565486298",
            "M_ID": "4878417",
            "MOTHER_NAME_ENG": "mundar devi gurjar",
            "FATHER_NAME_HND": "धूजीराम गुर्जर ",
            "DOB": "01-JUN-06",
            "NAME_ENG": "vedprakash rawat",
            "GENDER": "Male",
            "FATHER_NAME_ENG": "dhoojiram gurjar",
            "SPOUCE_NAME_ENG": " ",
            "NAME_HND": "वेदप्रकाश रावत ",
            "SPOUCE_NAME_HND": " ",
            "MOTHER_NAME_HND": "मुन्दर देवी गुर्जर "
        },
        {
            "AADHAR_ID": "796668014335",
            "M_ID": "4878418",
            "MOTHER_NAME_ENG": "mundar devi gurjar",
            "FATHER_NAME_HND": "धूजीराम गुर्जर ",
            "DOB": "03-JUL-08",
            "NAME_ENG": "madanmohan rawat",
            "GENDER": "Male",
            "FATHER_NAME_ENG": "dhoojiram gurjar",
            "SPOUCE_NAME_ENG": " ",
            "NAME_HND": "मदनमोहन रावत ",
            "SPOUCE_NAME_HND": " ",
            "MOTHER_NAME_HND": "मुन्दर देवी गुर्जर "
        },
        {
            "AADHAR_ID": "388038964343",
            "M_ID": "4878416",
            "MOTHER_NAME_ENG": "suaa devi",
            "FATHER_NAME_HND": "हरीसिंह गुर्जर ",
            "DOB": "02-JUL-83",
            "NAME_ENG": "dhoojiram gurjar",
            "GENDER": "Male",
            "FATHER_NAME_ENG": "harisingh gurjar",
            "SPOUCE_NAME_ENG": "mundar devi gurjar",
            "NAME_HND": "धूजीराम गुर्जर  ",
            "SPOUCE_NAME_HND": "मुन्दर देवी गुर्जर ",
            "MOTHER_NAME_HND": "सुआ देवी "
        },
        {
            "AADHAR_ID": "447306886787",
            "M_ID": "4878419",
            "MOTHER_NAME_ENG": "jhuniya",
            "FATHER_NAME_HND": "कजोड़या",
            "DOB": "01-JAN-52",
            "NAME_ENG": "harisingh gurjar",
            "GENDER": "Male",
            "FATHER_NAME_ENG": "kajodya",
            "SPOUCE_NAME_ENG": "suaa devi",
            "NAME_HND": "हरीसिंह गुर्जर ",
            "SPOUCE_NAME_HND": "सुआ देवी",
            "MOTHER_NAME_HND": "झुनिया"
        }
    ]
}






https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/family/details/1067-7PVQ-28383?client_id=ad7288a4-7764-436d-a727-783a977f1fe1



#for python3
import requests
import json

def main():
    r=requests.get("https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/family/details/1067-7PVQ-28383?client_id=ad7288a4-7764-436d-a727-783a977f1fe1")
    if r.status_code != 200:
        raise Exception("ERROR")
data =r.json()
print(data)

if __name__ == "__main__":
    main()

#for python2
import urllib.request, json
with urllib.request.urlopen("") as url:
    data = json.loads(url.read().decode())
    print(data)








# 1207-CN0V-24567
# 1207-HOTX-20756