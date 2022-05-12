
# COVID19 Dashboard

Analyse our country's Covid19 situation using python.


## Screenshots

![App Screenshot](https://raw.githubusercontent.com/shaurya121/Covid19-Dashboard/main/Screenshots/covid%20cases.png)

![App Screenshot](https://raw.githubusercontent.com/shaurya121/Covid19-Dashboard/main/Screenshots/covid%20deaths.png)

![App Screenshot](https://raw.githubusercontent.com/shaurya121/Covid19-Dashboard/main/Screenshots/positivity.png)


## Installation

Install required modules using:

```bash
pip install pandas
pip install numpy
pip install matplotlib
```
    
## Usage/Examples

Read the data from CSV file:
```python
df=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
```

Convert string Date time into Python Date time object.
```python
df['date']=pd.to_datetime(df['date'], errors='coerce')
```

Visualize covid19 cases in india:
```python
plt.plot(india_cov19.date, india_cov19.new_cases)
plt.xlabel('Date')
plt.ylabel('New cases')
plt.title("Covid-19 New cases in India")
plt.show()
```
