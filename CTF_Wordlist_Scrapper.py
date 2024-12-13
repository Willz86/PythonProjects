import requests
from bs4 import BeautifulSoup
import re

def scrape_site(url):
	"""Funtion to scrape the website and return a list of words."""
	# Send a request to the website
	try:
	    response = requests.get(url)
	    response.raise_for_status()
	except request.RequestException as e:
	    print(f"Error accessing {url}: {str(e)}")
	    return []
	    
	# Parse the content with BeautifulSoup
	soup = BeautifulSoup(response.text, 'html.parser')
	
	# Extract text from the webpage
	text = soup.get_text()
	
	# Use regular expression to extract words
	words = re.findall(r'\w+', text)
	
	return words
	
def main():
	# Ask the user for the website URL
	website = input("Enter the website URL: ")
	
	# Scrape the website
	words = scrape_site(website)
	
	# Remove duplicates and sorts words
	unique_words = sorted(set(words), key=str.lower)
	
	# Optionally, save the word list to a file
	if words:
	   with open("wordlist.txt", "w") as file:
	    for word in unique_words:
	        file.write(word + "\n")
	   print("Wordlist has been saved to wordlist.txt.")
	else:
	   print("No words found or failed to scrape the website.")
	   
if __name__ == "__main__":

   main()
   
