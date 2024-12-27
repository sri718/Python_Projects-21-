# The code works only after you replace the API_KEY.

from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://v6.exchangerate-api.com/v6/"
API_KEY = "e8850f15a6708112ce45f3b7148183007"                       # replace your key
p = PrettyPrinter()

def cur():
    end = f"/codes"
    data = get(BASE_URL + API_KEY + end).json()
    data = data.get('supported_codes','')                           # check, if not exist return ''.
    data.sort()
    return data

def print_cur(currencies):
    for  i,(code ,currency) in enumerate(currencies):
        name = currency
        code = code        
        print(f"{i+1}. {name} - {code}.")
    print("-----------------------------------------------------------------")

def conversion_rate(cur1,cur2):
    try:
        end = f"/latest/{cur1}"
        data = get(BASE_URL + API_KEY + end).json()['conversion_rates']
        print(f"{cur1} --> {cur2} = {data[cur2]}.")
    except KeyError:
        print("Invalid Currency.")

def convert(cur1,cur2,amount):
    try:
        end = f"/pair/{cur1}/{cur2}/{amount}"
        data = get(BASE_URL + API_KEY + end).json()['conversion_result']
        print(f"{amount} {cur1} = {data} {cur2}.")
    except:
        print("Invalid Currency/Amount.")

def main():
    currencies = cur()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()
    
    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_cur(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency code: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency code to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency code: ").upper()
            currency2 = input("Enter a currency code to convert to: ").upper()
            conversion_rate(currency1, currency2)
        else:
            print("Unrecognized command!")

main()
