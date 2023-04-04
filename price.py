import requests
import re
from bs4 import BeautifulSoup
from alert import alert_mail
import json
import datetime

#Email addrees to sent email to.
email_address = input("Enter your Email Address:")

url = 'https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'
res = requests.get(url)
html_doc = res.content
soup = BeautifulSoup(html_doc, 'html.parser')

#Regex to find the price
regex = r'\£\s*[0-9,]+(?:\s*\.\s*\d{2})?'
text = soup.get_text()

#Finding the title 
result = soup.find_all("h1")
title = result[0].text

#Finding the price using regex
match = re.search(regex, text)
if match:
    match_str = match.group(0).replace(' ', '')
    price = match_str
    #print("Match found:", match_str)
price = price[1:]
price = float(price)
print("Today's Price is: ", price)

# get today's date
today = datetime.date.today()

# format the date as "YYYY-MM-DD"
formatted_date = today.strftime("%d-%m-%Y")

data = {
    "Date": formatted_date,
    "Price": price 
}

# open the file in write mode
filename = 'prices_data.json'
with open(filename, "w") as file:
    # use the json.dump() function to write the data to the file
    json.dump(data, file)




#if(price < 60):
 #   alert_mail()
  #  print('Mail Sent')