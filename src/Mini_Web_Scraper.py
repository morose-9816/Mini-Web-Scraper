import bs4 as bs
from urllib.request import Request, urlopen
import json
import csv

#Converting INPUT JSON to DICT
with open('scraper-config.json', 'rb') as f:
  input_config = json.load(f)

#Function to read the input config file and scrap data as per the css selectors mentioned
def scraped(input_config2, soup):
    if(input_config2["entity_type"]!="entity"):
        if(input_config2["config"]=="img.img_delete_bg_noshow::attr(src)"): ##Handling one exception case of attr::(src)
            input_config2["entity"] = soup.select("img.img_delete_bg_noshow")[0]["src"]
        else:
            if not (soup.select(input_config2["config"][:-6])):
                input_config2["entity"] = "Not Found"
            else:
                input_config2["entity"] = soup.select(input_config2["config"][:-6])[0].text
        
    else:
        for nested_entity in input_config2["entity_scrapers"]:
            scraped(nested_entity, soup) ## To handle nested entities
    


#Empty list of dict which will be exported as JSON
final_output = []

##Readind the INPUT CSV File
content = []
with open('urls-100.csv', 'r') as file:
    reader = csv.reader(file)
    for url in reader:
        content.append(url)
content.pop(0) ##Removing the first row which is not a url


for url in content:
    req = Request(url[0]+'/', headers={'User-Agent': 'Mozilla/5.0'})
    sauce = urlopen(req).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    print(soup.title.text)
    output = input_config.copy()
    scraped(output,soup) ## Passing the url to custom function
    print(output) ## The output consists of scraped data for every different url
    final_output.append(output.copy()) ## Appending the dict to final list
    ## --------PROBLEM(pending) - The respective output with iteration over urls in console is correct, but when we look at final_output, it contains 100 dicts of last output only
    
    
    
## Exporting to JSON Object
final_output_json = json.dumps(final_output)
with open("output.json", "w") as outfile: 
    outfile.write(final_output_json) 
    

