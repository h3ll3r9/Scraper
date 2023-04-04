# Scraper
Description:
This is a Python project that allows users to track the price of a specific product on a website. The program uses the Python requests library to fetch product details and the BeautifulSoup library to scrape the price from the website's HTML. The user can enter their email address and a target price, and the program will send an email alert using the SMTP library if the price drops below the target.

Dependencies:
This project requires the following dependencies to be installed:

Python 3.x
BeautifulSoup
Requests
smtplib
Usage:
Clone the project from GitHub to your local machine.
Install the required dependencies using pip.
Run the program from the command line using the command python price_tracker.py.
Enter the product URL, your email address, and the target price when prompted.
The program will fetch the product details, scrape the price from the website's HTML, and compare it to the target price.
If the price drops below the target, the program will send an email alert using the specified email account's SMTP server.
License:
This project is licensed under the MIT License. Feel free to use and modify the code as per your requirements.
