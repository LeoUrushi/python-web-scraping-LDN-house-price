# python-web-scraping-LDN-house-price

This is a working example of a python web scraper tool that scrapes Rightmove website and compiles properties near a given Tube station into a .csv file. From there, you can sort them by Tube lines or create data visualisation. 

## Basic technique: 

Below is an excellent introduction to web scraping by Dr. Parker. 
https://towardsdatascience.com/data-science-skills-web-scraping-using-python-d1a85ef607ed

However, in this case, the important information are hidden inside <script> tags. It requires a more advanced web scraping method. Dr. Parker’s tutorial vol.2 covers this topic. 

https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

## Preparation: 
Install flask to run python programmes from your terminal. 
https://flask.palletsprojects.com/en/1.1.x/installation/

Install the gecko driver to your project folder. And find the path of the gecko driver including all the parent folders. And copy and paste it into the “drive” section of the code. 

driver = webdriver.Firefox(firefox_options=options, executable_path = '/Users/YOUR-USER-NAME/Documents/PROJECTS/PROJECT-NAME/geckodriver’)

## Application

Go to Rightmove’s for-sale section of the website. 

https://www.rightmove.co.uk/property-for-sale

Type in the name of a station and specify other search criteria. 

For instance, “1 to 2 bed” properties within “1/2” mile from Euston Station that have been posted within the “last 14 days” returns 22 results as of this writing. Copy the URL of this result page and paste into the urlpage variable as below. 

````
# specify the url
urlpage = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=STATION%5E3311&maxBedrooms=2&minBedrooms=1&radius=0.5&propertyTypes=&maxDaysSinceAdded=14&includeSSTC=false&mustHave=&dontShow=retirement%2CsharedOwnership&furnishTypes=&keywords='
````

Find the information you need by combing through the website in the inspector mode. 

In this example, I selected title name, location, distance (from the station), asking price, listed date and the estate agent who posted the advertisement. 

````
data.append({"01_title" : element_title, "02_location" : element_address, "03_distance (miles)" : distance_cleaned, "04_price" : price_cleaned, "05_date" : text_date, "06_by" : text_agent_cleaned })
````


-Open the terminal and cd into the project folder where the home.py file is located 

-Set the FLASK to development mode by running this: 
export FLASK_ENV=development

-Run the programme by typing the following command: 
FLASK_APP=home.py flask run

-You will see the number of results being returned by the web scraper in the terminal screen. 

-After a few seconds, you will also see a new .csv file called ‘data_export.csv’ in the same folder. 



I used this web scraping method to generate a database of house prices per Tube station. The resulting data visualisation can be found below. 

Working example: 

http://whats-it-worth.net/


