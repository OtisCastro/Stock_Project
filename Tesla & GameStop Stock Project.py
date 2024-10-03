#!/usr/bin/env python
# coding: utf-8

# ## Question 1: Use yfinance to Extract Stock Data
# 

# In[1]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')


# In[ ]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')


# In[55]:


import yfinance as yf
import pandas as pd
import matplotlib_inline
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[ ]:





# ## Question 1: Use yfinance to Extract Stock Data
# 

# In[59]:


tesla = yf.Ticker("TSLA")


# In[60]:


tesla_data = tesla.history(period="max")


# In[61]:


tesla_data.reset_index(inplace=True)


# In[62]:


tesla_data.head()


# ## Question 2: Use Webscraping to Extract Tesla Revenue Data
# 

# In[63]:


tesla_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data  = requests.get(tesla_url)
soup = BeautifulSoup(html_data.content, 'html.parser')


# In[88]:


# Find the relevant tbody
tbody = soup.find_all("tbody")[1]  # Get the second tbody

# Initialize a list to hold the data
revenue_data = []

# Step 4: Loop through rows in the relevant tbody
for row in tbody.find_all('tr'):
    cols = row.find_all('td')
    if cols:  # Ensure cols are not empty
        date = cols[0].text.strip()  # Get the date
        revenue = cols[1].text.strip()  # Get the revenue

        # Step 5: Clean revenue data
        revenue = revenue.replace('$', '').replace(',', '').strip()

        # Step 6: Add rows to the data list
        revenue_data.append({"Date": date, "Revenue": revenue})

# Step 6: Create a DataFrame from the list
tesla_revenue = pd.DataFrame(revenue_data)

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"", regex=True)
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

tesla_revenue.tail()


# In[68]:


tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"", regex=True)
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[69]:


tesla_revenue.tail()


# ## Question 3: Use yfinance to Extract Stock Data
# 

# In[70]:


gme = yf.Ticker("GME")


# In[77]:


gme_data = tesla.history(period="max")


# In[78]:


gme_data.reset_index(inplace=True)
gme_data.head()


# ## Question 4: Use Webscraping to Extract GME Revenue Data
# 

# In[79]:


gme_url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2  = requests.get(gme_url)
soup = BeautifulSoup(html_data_2.content, 'html.parser')


# In[82]:


# Find the relevant tbody
tbody = soup.find_all("tbody")[1]  # Get the second tbody

# Initialize a list to hold the data
revenue_data = []

# Step 4: Loop through rows in the relevant tbody
for row in tbody.find_all('tr'):
    cols = row.find_all('td')
    if cols:  # Ensure cols are not empty
        date = cols[0].text.strip()  # Get the date
        revenue = cols[1].text.strip()  # Get the revenue

        # Step 5: Clean revenue data
        revenue = revenue.replace('$', '').replace(',', '').strip()

        # Step 6: Add rows to the data list
        revenue_data.append({"Date": date, "Revenue": revenue})

# Step 6: Create a DataFrame from the list
gme_revenue = pd.DataFrame(revenue_data)

gme_revenue.tail()


# In[91]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    
    fig.update_layout(showlegend=False,
                      height=900,
                      title=f"{stock} Stock Performance",  # Custom title
                      xaxis_rangeslider_visible=True)
    fig.show()


# ## Question 5: Plot Tesla Stock Graph
# 

# In[92]:


make_graph(tesla_data,tesla_revenue,"Tesla")


# ## Question 6: Plot GameStop Stock Graph
# 

# In[93]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




