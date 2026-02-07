import requests

import pandas as pd

import numpy as np

 

# Crypto list (CoinGecko IDs)

cryptos = ["bitcoin", "ethereum", "solana", "cardano", "dogecoin"]

 

days = 30

currency = "inr"

 

results = []

 

for coin in cryptos:

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {

        "vs_currency": currency,

        "days": days

    }

 

    response = requests.get(url, params=params)

    data = response.json()

 

    prices = data["prices"]

 

    # Create DataFrame

    df = pd.DataFrame(prices, columns=["timestamp", "price"])

    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")

    df = df[["date", "price"]]

 

    # Save daily data

    df.to_csv(f"{coin}_daily_prices.csv", index=False)

 

    # Volatility calculation

    volatility = np.std(df["price"])

 

    # Risk classification

    if volatility < 5000:

        risk = "Low Risk"

    elif volatility < 20000:

        risk = "Medium Risk"

    else:

        risk = "High Risk"

 

    results.append([coin.upper(), volatility, risk])

 

# Final result table

result_df = pd.DataFrame(results, columns=["Crypto", "Volatility", "Risk Level"])

print(result_df)

 

# Save summary

result_df.to_csv("crypto_volatility_risk_summary.csv", index=False)