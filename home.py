# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.firefox.options import Options

# specify the url
urlpage = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=STATION%5E3311&maxBedrooms=2&minBedrooms=1&radius=0.5&propertyTypes=&maxDaysSinceAdded=14&includeSSTC=false&mustHave=&dontShow=retirement%2CsharedOwnership&furnishTypes=&keywords='

print(urlpage)

# scrape the webpage using firefox webdriver
# run firefox webdriver from executable path of your choice
options = Options()
options.headless = True


# driver with Headless option:
# Specify the location of the driver: 
driver = webdriver.Firefox(firefox_options=options, executable_path = '/Users/YOUR-USER-NAME/Documents/YOUR-PROJECT/geckodriver')

# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for n-seconds
time.sleep(10)

# print(urlpage)

# === === === === === === 

# find elements by xpath
results = driver.find_elements_by_xpath('//*[@id="l-searchResults"]//*[contains(@class,"l-searchResult")]//*[@class="propertyCard"]//*[@class="propertyCard-wrapper"]')
print('Firefox Webdriver - Number of results', len(results))

# # create empty array to store data
data = []
# # loop over results
for result in results:
    # === === === === === 
    # Find the title name of the data entry 
    element_content = result.find_element_by_class_name('propertyCard-content')
    element_section = element_content.find_element_by_class_name('propertyCard-section')
    property_details = element_section.find_element_by_class_name('propertyCard-details')
    element_a = property_details.find_element_by_class_name('propertyCard-link')
    element_title = element_a.find_element_by_class_name('propertyCard-title').text
    # === === === === === 
    # Find the address 
    element_address = element_a.find_element_by_class_name('propertyCard-address').text
    # === === === === === 
    # Find the distance (from a nearest station)
    element_distance = property_details.find_element_by_class_name('propertyCard-distance').text
    distance_cleaned = element_distance.replace(' miles from station', '')
    # === === === === === 
    # Find the asking price
    element_header = result.find_element_by_class_name('propertyCard-header')
    element_price = element_header.find_element_by_class_name('propertyCard-priceValue').text
    price_cleaned = element_price.replace('£', '')
    # === === === === === 
    # Who's posted it? 
    # And when was it posted or updated??
    element_footer = element_content.find_element_by_class_name('propertyCard-detailsFooter')
    element_branch = element_footer.find_element_by_class_name('propertyCard-branchSummary')
    text_date = element_branch.find_element_by_class_name('propertyCard-branchSummary-addedOrReduced').text
    text_agent = element_branch.find_element_by_class_name('propertyCard-branchSummary-branchName').text
    text_agent_cleaned = (text_agent[3:])

    # append dict to array
    data.append({"01_title" : element_title, "02_location" : element_address, "03_distance (miles)" : distance_cleaned, "04_price" : price_cleaned, "05_date" : text_date, "06_by" : text_agent_cleaned })

# close driver 
driver.quit()

# save to pandas dataframe
df = pd.DataFrame(data)

# write to csv
df.to_csv('data_export.csv')

