import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

#reading the data from CSV file
df=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
#print(df.info())


date=df.date
df['date']=pd.to_datetime(df['date'], errors='coerce')
#print(df)

country=df['location'].to_list()
set_country=set()
for i in country:
	set_country.add(i)
#print(set_country)	

country="India"
include_india=df[df['location'].values==country]
exclude_india=df[df['location'].values!=country]
india_cov19=include_india
#print(india_cov19)

# visualize covid19 cases in india
plt.plot(india_cov19.date, india_cov19.new_cases)
plt.xlabel('Date')
plt.ylabel('New cases')
plt.title("Covid-19 New cases in India")
plt.show()

# visualize covid19 deaths in India
plt.plot(india_cov19.date, india_cov19.new_deaths)
plt.xlabel('Date')
plt.ylabel('New deaths')
plt.title("Covid-19 deaths in India")
plt.show()

# visualize covid19 positivity in india
plt.plot(india_cov19.date, india_cov19.positive_rate)
plt.xlabel('Date')
plt.ylabel('Positivity rate')
plt.title("Covid-19 Positivity in India")
plt.show()
