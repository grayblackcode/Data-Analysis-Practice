import yfinance as yf

# Apple Intrinsic value calculation
aapl = yf.Ticker("aapl")
outstandingshares = aapl.info["sharesOutstanding"]  # Fetch number of shares

# assumptions
required_rate = 0.07
perpetual_rate = 0.02
cashflowgrowthrate = 0.03

years = [1, 2, 3, 4]

freecashflow = [50803000, 64121000, 58896000, 73365000] # last 4yrs, in '000s of $

future_freecashflow = []
discount_factor = []
discounted_future_freecashflow = []

terminal_value = freecashflow[-1] * (1+perpetual_rate)/(required_rate - perpetual_rate)
# print(terminal_value)

for year in years:
    cashflow = freecashflow[-1] * (1+ cashflowgrowthrate) ** year
    future_freecashflow.append(cashflow)
    discount_factor.append((1+ required_rate)**year)  # discounted value denominator

# print(discount_factor)
# print(future_freecashflow)

for i in range(0, len(years)):
    discounted_future_freecashflow.append(future_freecashflow[i]/discount_factor[i])

# print(discounted_future_freecashflow)

discounted_terminalvalue = terminal_value/(1+ required_rate)**4  # discount value at year4
discounted_future_freecashflow.append(discounted_terminalvalue)

todays_value = sum(discounted_future_freecashflow)

fair_value = todays_value * 1000/outstandingshares

print("The fair value of AAPL is ${}".format(round(fair_value, 2)))