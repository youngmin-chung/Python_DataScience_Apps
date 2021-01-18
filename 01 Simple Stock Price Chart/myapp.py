import yfinance as yfinance
import streamlit as streamlit
import pandas as pd

streamlit.write("""

# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL'

tickerData = yfinance.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2021-1-15')

streamlit.line_chart(tickerDf.Close)
streamlit.line_chart(tickerDf.Volume)