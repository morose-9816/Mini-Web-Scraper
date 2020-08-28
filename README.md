A modular mini web scraper which can scrape data off any website which only
has static pages into a structured JSON output based on an input configuration.

Assumptions :
	- The input config file has all the tags/classes/id which are needed to be scraped
	- The config of every entity in input_config.json has either ::attr(src) or ::text in the end.
	- a:nth-child(2) is not supported in bs4. Modify it to a:nth-of-type(2).

Design :
	- Made a custom recursive function which reads the input config file and scraps data as per need
	- Used BeautifulSoup(Python) to scrape the webpages
	- Used .select() method to search particular class/id/tag/etc
	- Created an empty list and appended dict objects to it after scraping urls's given in the input csv sheet and later exported list to JSON onject

Drawbacks :
	- Not handling every kind of attribute associated with config(only ::attr(src) and ::text is being handled here)
	- BeautifulSoup has slower processing. Can use scrapy for complex projects 

Please see installation.txt to download dependecies required to run this code.
Output JSON will is named as output.json