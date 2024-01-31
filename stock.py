'''

DS20001 Spring 2022 Final Project
Benjamin Teixeira, Yi Chen Wu, Alyssa Benjamin
    
Filename: stock.py
    
Description: analyzing big tech stock market trends 
            from Jan 2020 to Apr 2022 of 52-Week High Prices
            
4 major events:
    March 11th, 2020: COVID-19 Pandemic Begins
    January 6th, 2021: U.S. Capitol Riot
    January 26th, 2021: Gamestop Short Squeeze
    February 24th, 2022: Russian Invasion of Ukraine
    
Sources:
    stackoverflow (plt.rcParams)
    GeeksforGeeks (boxplot color labeling)
    Yahoo! Finance (Stock Market Data)
    Investopedia (52-Week High, General Stock Information)
    Washington Post (Facebook's Russia Misinformation)
    
'''
# importing libraries here
import matplotlib.pyplot as plt
import csv

# identifying big tech companies here
APPLE = "AAPL.csv"
IBM = "IBM.csv"
META = "FB.csv"
MICROSOFT = "MSFT.csv"
TWITTER = "TWTR.csv"

def read_data(filename):
    """name: read_data
        input: Yahoo! stock market files
        result: Historical stock market data and categories"""
    
    # reading in data, appending to list
    stock_data = []
    with open (filename, "r") as file:
        csv_file = csv.reader(file, delimiter = ",")
        
        for row in csv_file:
            stock_data.append(row)
            
    # separate header from data for indexing
    header = stock_data[0]
    data = stock_data[1:]
    
    return header, data

def get_high_date(header, data):
    """name: retrieve_min_max
        input: historical stock market data (lists)
        result: List of 52-week highs (floats) with dates"""
    
    # labeling high index's for 52-Week High Prices with dates
    date = []
    max_price = []
    date_index = header.index("Date")
    max_index = header.index("High")
    
    # appending index data to lists
    for row in data:
        date.append(row[date_index])
        max_price.append(row[max_index])
        
    return max_price, date
            
def report_prices(max_price):
    """name: calc_average
        input: 52 week high (lists of strings)
        result: list of floats, prices of 52-Week Highs"""
    
    high_price = []
    
    # converting data to floats, appending to new list
    for num in range(len(max_price)):
        max_price[num] = float(max_price[num])
        high_price.append(max_price[num])
        
    return high_price

def plot(date, high_price, colors, labels):
    """name: plot
        input: date, avg_lst
        result: visualization of daily 52-Week Highs,
        highlighting dates of major events"""
    
    # visualizing and fine-tuning data
    plt.plot(date, high_price, color = colors, label = labels)
    plt.xlim(0,569)
    plt.ylim(0,400)
    plt.grid()
    
    plt.xticks([0,62,125,189,253,314,377,441,505,568],["Jan '20","Apr '20",
    "Jul '20", "Oct '20","Jan '21","Apr '21", 
    "Jul '21", "Oct '21", "Jan '22", "Apr '22"])
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams["figure.figsize"] = (6,5)
    
    # labeling important dates
    plt.text(47,255, "X")
    plt.text(3,270,"3/11/20: COVID")
    plt.text(248,320, "X")
    plt.text(185,335, "1/6/21: Capitol Riot")
    
    plt.text(268, 170, "X")
    plt.text(180, 185, "1/26/21: GameStop Squeeze")
    plt.text(541, 70, "X")
    plt.text(340, 85, "2/24/22: Russian Invasion")
    
    plt.text(130, 385, "X = Exact Date")

    # labeling visualizations
    plt.title("52-Week High Stock Prices in Relation to Global Events")
    plt.xlabel("Date")
    plt.ylabel("High Price ($)")
    plt.legend(facecolor = "lightgrey", edgecolor = "black", 
               loc = "upper left", fontsize = 8)
    plt.savefig("stock.png")
     
def compressed(file, color, company):
    """name: compressed
        input: csv_file, color-identifier, company
        result: visualization (line graph) combining the data 
        to plot each company's 52-Week High price, 
        and return the prices for plotting distribution through boxplots"""
    
    header, data = read_data(file)
    high_price, date = get_high_date(header, data)
    prices = report_prices(high_price)
    plot(date, prices, color, company)
    
    return prices
    
def main():
    
    # reading company data
    ibm = compressed(IBM, "red", "IBM")
    facebook = compressed(META, "dodgerblue", "Facebook")
    twitter = compressed(TWITTER, "orange", "Twitter")
    microsoft = compressed(MICROSOFT, "green", "Microsoft")
    apple = compressed(APPLE, "magenta", "Apple")
    
    # data distribution, report skews, outliers, ranges
    plt.figure(figsize = (6,5), dpi = 500)
    firms = [ibm, facebook, twitter, microsoft, apple]
    bp = plt.boxplot(firms, vert = False, patch_artist = True, notch = True)
    plt.grid()
    
    # labeling and fine-tuning distribution visualizations
    colors = ["red", "dodgerblue", "orange", "green", "magenta"]
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
    
    plt.yticks([1,2,3,4,5], ["IBM", "Facebook", 
                             "Twitter", "Microsoft", "Apple"])
    plt.title("52-Week High Stock Price Distribution")
    plt.xlabel("Price Distribution ($)")
    plt.ylabel("Big Tech Company")
    plt.savefig("stock_distribution.png")
    
main()

# written analysis introduction
"""For our Data Science Practicum project, we decided to analyze a problem 
that involved  the often uncertain times we are currently living in and the 
consequential global business and financial implications. In short, our team 
looked to provide insights into the issue of turbulent 52-Week stock prices 
due to major world events from 2020-2022. Our specific questions were: How 
did major world events affect five of the biggest technology companies in the 
world? How volatile have tech stocks been since the outbreak of COVID-19? And 
most importantly, how should shareholders react to this information? While the 
COVID-19 pandemic and its initial outbreak in the U.S. was the largest event, 
other occurrences such as the Capital Riot of January 2021 and Russia’s 
invasion of Ukraine in 2022 are just two other examples. This trend of 
turbulent stock prices is highly important for several reasons. The most 
evident reason is that distressing events that involve political unrest or 
risk the safety of global citizens impacts how people live their daily lives. 
Furthermore, economic instability causes issues for nations as a whole. The 
reality is that when an economy takes a turn for the worse, or is 
unpredictable over short periods of time, regular citizens are usually the 
ones who are the most financially impacted. For example, this is noted with 
the drastic rise in gasoline prices for American citizens. Furthermore, 
shareholders of Big Tech companies are evidently affected by turbulent stock 
prices. The specific metric we decided to analyze was the 52-Week High Stock 
Price, which is the highest price a stock has traded for over the last 52 
weeks daily. For example, if a company had a 52-Week High price of $100 on 
April 1st, 2022, then it would’ve been the highest price the stock traded for 
since April 1st, 2021. The reason why this is important is because it’s based 
on the daily closing price of a stock, an important metric for stock traders 
and investors to consider when assessing changes in stock prices over time. 
Given how these prices change, it’s often important for investors to consider 
investing in a stock or not if it’s near its 52-Week High and why. For 
example, if a stock reaches its high it could be a sign of strength, but
if it quickly drops after it could be a sign of persistent weakness. Overall, 
52-Week Highs represent positive attitudes in the market and may signify 
investors partially or fully cashing in on their investments, given that 
trading often rises when a stock crosses a 52-Week barrier.""" 

# introduction & description of data
"""Our group had an easy time gathering our data, as the stock prices of 
publicly traded companies are easily accessible through several highly 
reliable websites. We were able to cross-reference the stock prices among 
multiple websites to ensure the data was accurate. We ultimately gathered 
our daily stock price data via Yahoo Finance of five of the biggest tech 
companies: Apple, Facebook/Meta, IBM, Microsoft, and Twitter. Yahoo Finance 
allows for two specific features that were highly useful for our purposes: 1) 
the exportation of the files as csv files, and 2) the selection of specific 
start and end dates for our data. We chose stock prices for the respective 
companies starting on January 1st of 2020 and ending on April 1st of 2022. 
This was strategic, because the year 2020 was when the COVID-19 pandemic broke 
out. Within each individual csv file, there were 7 column headers. At position 
0 is the data of the date (m/d/yyyy, string), at position 1 is the opening 
price of the stock that day (float), at position 2 is the 52-Week high price 
of the stock that day (float), at position 3 is the 52-Week low price of the 
stock that day (float), at position 4 is the closing price of the stock that 
day (float), at position 5 is the adjusted closing price of the stock that 
date (float), and at position 6 is the volume for that day (int). The relevant 
variables for our code were the date (pos 0), and the high price (pos 2)."""

# methods
"""When conducting our analysis via Python, our group members wanted to keep our 
code as concise and straightforward as possible. Our first function called 
“read_data” read in the csv files, and appended the rows of data into a list. 
Two separate lists were then created via slicing, one containing only the 
headers, and the rest containing the bulk of the data. Our next function 
called “get_high_date” used the index function to find the column that 
contained the high stock price and date of each respective day. Using a 
“for loop”, the high and low prices were appended to 2 respective lists (one 
for the high price and one for the date). The next function called 
“report_prices” used a for loop to convert the high prices from strings to 
ints and append it to a list. The next function called “plot” used basic 
matplotlib functions to plot the average prices of the stock using a line 
graph. We thought this would be best to show a trend over time. Dates (x 
label) were determined by the fiscal year timeline, and y axis will be the 
stock price.  The last function, “compressed”, looked to plot all of the 
company’s data in one graph (a function that calls all the previous ones into 
a final function). In the main function, each company was called, meaning each 
of the 5 company’s data will be run through the functions and plotted. For the 
box plot, we utilized the same functions for the line graph, but we returned 
the necessary information needed, such as the returning stock prices from the 
“compressed” function. Later we used the data we found and plot box plot in 
our main function, which were useful to display the variability and 
distribution of data ranges, and insightful in identifying statistical values, 
skews, and potential outliers. Our biggest use for the boxplots was pairing 
it with the scatter plots to determine comparisons of variety and which 
variation is better.""" 

# results & conclusion
"""Each of the 5 companies we analyzed sustained price drops around the 
occurrence of the major global events, but certain companies had higher 
sustained performances afterwards and others had steeper drops that led to 
consistent negative performance. All 5 companies sustained significant price 
drops at the start of the COVID-19 Pandemic, with Facebook and IBM suffering 
the relatively steepest drops compared to competitors. Each company was able 
to recover past the pre-pandemic price drop except for IBM. While IBM’s price 
remained consistent over the time horizon and didn’t drop too significantly, 
including during the Capitol Riots and Gamestop Squeeze, it never got higher 
than it was before COVID. The two other lower priced firms, Twitter and Apple,
had varying performances. Apple was able to weather major events and their 
stock price consistently rose over time, whereas Twitter had periods of 
stagnant price levels and quick drops after peaks, followed by a consistent 
decline over the last half year. Of the three lower-priced companies, Apple is 
our choice for the best stock to invest in, particularly for risk-averse 
investors with less disposable income. In addition to their relative stock 
performance, they’re well-known and liked in both the B2B and B2C realms, 
something that they have advantages over Twitter and IBM for, respectively. 
Even though Twitter and IBM avoided drops amid major events, they didn’t see 
the progression Apple did. The relatively higher priced firms, Facebook and 
Microsoft, are popular stocks for risk-friendly investors with more disposable 
income available. While Facebook had the overall highest price and some of the 
strongest periods of progression, Microsoft is the better choice of the two 
higher-priced firms. Facebook’s drops were steeper than Microsoft, especially 
their drop at around the time of Russia’s invasion into Ukraine. This drop was
additionally fueled by Meta’s poor performance and reception, yet Microsoft 
and many other companies’ stocks dropped due to the global conflict, and if 
Facebook’s stock was stronger it would’ve weathered their issues better. 
Microsoft has had less relative volatility and more consistent gains since 
January 2020, while Facebook’s most recent price is closer to our starting 
price around early January 2020.""" 

# future work
"""One strength about our project is the data itself. The stock prices of 
big tech companies, and any publicly traded company for that matter, are 
easily accessible online. This means our data is highly reliable and reflects 
the insights we gathered from the “big events”. The data was easily 
downloadable as a CSV file from Yahoo Finance, and we could manually select 
the start and end dates that we wanted the data from. Additionally, we 
utilized 2 different types of matplotlib graphs (line graph and boxplot) 
that conveyed different insights from the same set of information. The line 
graph shows a broad trend of the stock prices over time, while the boxplot 
displays how volatile each company’s stock is (showing outliers, how 
consistent the stock holds, etc.). Conversely, this project did have some 
limitations. First off, we can’t predict the future, there is still 
uncertainty for internal and external issues. Secondly, we chose a specific 
sector (technology). Analyzing trends amongst other sectors is essential. 
Furthermore, Only analyzing trend patterns and if we had more time we will 
investigate deeper financial metrics such as EBIT, EBITDA, dividends paid, 
gross profit, net income, earnings per share, debt-to-liability ratio, 
asset-to-liability ratio, and more. Additionally, we studied stock market 
prices, but not the internal company performances that have the power to 
change stock prices and strength of company performance. This included 
performances reflected in a company’s balance sheet, income statement, 
statement of cash flows, and statement of retained earnings. One more 
limitation is analysis of the 52-Week Low, which is the lowest price a stock 
traded for during its 52-week period at that date. We had difficulties 
plotting the two metrics together given how our functions were structured, 
and we found that when we filtered for just the high or low, the 
visualizations were similar to each other in values given that our ranges 
for stock prices were in the 100s. Ultimately, our biggest reason for this 
issue was that we spent most of the time answering a different question that 
didn’t have as much feasibility as was answering questions on 52-Week Highs, 
and we wanted to stick with a coding option that we knew worked without trying 
to complicate things too quickly with too little time left."""

# sources
"""Investopedia: 52-Week and Closing Price Information
Yahoo! Finance: Stock Market Data (Apple, Facebook/Meta, IBM, Microsoft, 
                                   Twitter)
GeeksforGeeks: BoxPlot Information
StackOverflow: plt.rcParams Information
Washington Post: Facebook’s Misinformation Management"""