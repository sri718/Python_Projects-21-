from requests import get
from pprint import PrettyPrinter

BASE_URL = 'https://raw.githubusercontent.com'                                    # hosted in GITHUB
LINK =  '/sri718/Python_Projects-21-/refs/heads/main/Project_15_(API_JSON)/J1_P15.json'

p = PrettyPrinter()

def get_link():
    data1 = get(BASE_URL + LINK).json()
    url1 = data1['library']['related_books']
    name = data1['library']['name']
    print(name)
    return url1

def get_books_url():
    url2 = get_link()['books_url']
    
    #data2 = get(BASE_URL + url2).json()
    # p.pprint(data2.keys())
    #Output : dict_keys(['books'])
    # data2 = get(BASE_URL + url2).json()['books']
    # p.pprint(data2.keys())     
    # Output : dict_keys(['book1', 'book2'])

    data2 = get(BASE_URL + url2).json()['books']

    for i,v in enumerate(data2.values()):
        auth = v['author']
        tit = v['title']
        yr = v['year']
        det = v.get('details',{})                                                   # pass a dic called details, if not exist then an empty dic {}.
        d = list(filter(lambda x: x['genre'] != 'Fiction',[det]))                   # to filter,lambda is a anonymous fn.  ---> try.
        gen = det['genre']
        rate = det['rating']
        print('-------------------------------------------------------------------------')
        print(f"{i+1}. Author: {auth}, Title: {tit},Year: {yr}.")
        print(f"Genre: {gen}, Rating: {rate}.")
        if d:
            print(f"\nGenre:{d[0]['genre']}, Rating: {d[0]['rating']} --> By list(filter(lambda x: x['genre'] != 'Fiction',[det])).")
        print(f'\n{d}')
    
get_books_url()
