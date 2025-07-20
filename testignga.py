import requests
import json
import os

def parameter(name):
    return {
        'ids': ','.join(name),
        'vs_currency': 'usd',
        'include_market_cap':True
    }

def get_info( name=""):
    base_url="https://api.coingecko.com/api/v3/coins/markets"
    response = requests.get(base_url, params=parameter(name))
    try:
        data = response.json()
        if data:
            return data
    except Exception as e:
        print(" Error while fetching data:", e)
    return 0

def market_cap_change():
    market_cap_url = "https://api.coingecko.com/api/v3/global"
    try:
        response = requests.get(market_cap_url)
        data = response.json()
        percent = data['data']['market_cap_change_percentage_24h_usd']
        print(f"{percent:.4f}%")
    except:
        print(" Couldn't fetch market cap data.")

def add_fav(name_list, filename='favourites_coins.txt'):
    existing = set()
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            existing = set(f.read().split())
    with open(filename, 'w') as f:
        all_favs = existing.union(set(name_list))
        f.write(' '.join(all_favs))
        print("Favourites updated.")

def load_favs(filename='favourites_coins.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read().split()
    else:
        print(" No favourites found.")
        return []

def alerts():
    pass

def extract_info():
    name = input("Enter coins to extract info on (space-separated): ").split()
    data = get_info(name)
    if data:
        with open("extracted_data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data extracted to 'extracted_data.json'")
    else:
        print("Failed to extract info. Check the coin names.")

def main():
    choice = 1
    while choice:
        print('\n*-- Crypto Tracker --*')
        print("Today's market cap change:", end=" ")
        market_cap_change()
        print('\nWhat would you like to do today:')
        print('1. Check new coin')
        print('2. Track favourites')
        print('3. Extract Data')
        print('4. Exit')

        try:
            choice = int(input('\nEnter your choice: '))
        except ValueError:
            print(" Enter a valid number.")
            continue

        if choice == 1:
            name = input('Enter crypto coins (space-separated): ').split()
            data = get_info(name)
            if data:
                print(data)
                for coin in data:
                      mar=format(coin['market_cap'],',')
                      print(f"{coin['id'].capitalize()} → ₹{coin['current_price']} .Market cap →{mar}")
                fav_choice = input('Add these as favourites? (y/n): ').strip().lower()
                if fav_choice == 'y':
                     add_fav(name)
            else:
                print(' No data found. Are the spellings correct?')

        elif choice == 2:
            favs = load_favs()
            if favs:
                data = get_info(favs)
                if data:
                    for coin in data:
                      mar=format(coin['market_cap'],',')
                      print(f"{coin['id'].capitalize()} → ₹{coin['current_price']} .Market cap →{mar}")
                else:
                    print("Couldn't fetch data for favorites.")

        elif choice == 3:
            extract_info()

        elif choice == 4:
            print(' Have a great day!')
            break
        else:
            print(' Invalid choice. Please select between 1–4.')

main()
