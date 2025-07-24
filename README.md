# 🪙 Crypto Tracker

A simple Python-based command-line tool to fetch real-time cryptocurrency data using the CoinGecko API. Track coins, view market cap changes, manage your favorites, and extract data to a JSON file—all from the terminal.

## 🚀 Features

- Track current prices and market caps of cryptocurrencies
- View global 24-hour market cap percentage change
- Save and view a list of favorite coins
- Export coin data into a JSON file for future use
- Error handling for invalid coin names and API issues

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crypto-tracker.git
   cd crypto-tracker

2. Install required dependencies (only `requests` needed):
   ```bash
   pip install requests
   ```

## ▶️ How to Run

```bash
python crypto_tracker.py
```

Follow the menu in the terminal to:

- Check coin prices and market caps
- Add coins to favorites
- View your favorites
- Export data to `extracted_data.json`

## 💾 Sample Output

```
*-- Crypto Tracker --*
Today's market cap change: 0.8734%

What would you like to do today:
1. Check new coin
2. Track favourites
3. Extract Data
4. Exit
```

## 📁 Data Output

If you use the "Extract Data" option, the info will be saved to:
```
extracted_data.json
```

Your favorite coins are stored in:
```
favourites_coins.txt
```

## 🧠 Built With

- Python 3
- [CoinGecko API](https://www.coingecko.com/en/api/documentation)

