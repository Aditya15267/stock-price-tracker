import yfinance as yf
import argparse

def track_stock(stock_symbol):
    """
    Track the stock price of a given stock symbol.

    Args:
        stock_symbol (str): The stock symbol to track.

    Returns:
        None
    """
    try:
        # Fetch the stock data using yfinance
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period='1d')
        
        # Print the latest stock price
        if data.empty:
            print(f"No data available for {stock_symbol}.")
            return
        
        last_quote = data.iloc[-1]
        print(f"Stock information for {stock_symbol.upper()}:")
        print(f"Date: {last_quote.name.date()}")
        print(f"Open: ${last_quote['Open']:.2f}")
        print(f"Close: ${last_quote['Close']:.2f}")
        print(f"High: ${last_quote['High']:.2f}")
        print(f"Low: ${last_quote['Low']:.2f}")
        print(f"Volume: {last_quote['Volume']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Track stock prices for given stock symbols")
    parser.add_argument("stock_symbol", type=str, help="Stock symbol to track (e.g., AAPL, GOOGL).")
    args = parser.parse_args()

    track_stock(args.stock_symbol)