"""
Website Scraping with BeautifulSoup 4 and Requests | CoreyMS
"""
from bs4 import BeautifulSoup
import requests
import csv

# A csv file to save the data
csv_file = open("cms_scrapper.csv","w")
csv_writer = csv.writer(csv_file)

csv_writer.writerow(["header","paragraph","video_link"])

# Requests for the html document of the target website
html_file = requests.get("https://coreyms.com").text

# Create a Soup
soup = BeautifulSoup(html_file,"lxml")
link_count = 0
article_count = 0
for article in soup.find_all("article"):
    try:
        header = article.header.h2.a.text

        paragraph = article.find("div", class_="entry-content").p.text

        video_src = article.find("iframe", class_="youtube-player")["src"]
        video_id = video_src.split("/")[4]
        video_id = video_id.split("?")[0]
        video_link = f"https://www.youtube.com/watch?v={video_id}"

        print(header)
        print("\n",paragraph)
        print("\n",video_link)
        print()
    except TypeError:
        video_link = None
    
    csv_writer.writerow([header,paragraph,video_link])

# Closing a file after writing into it.
csv_file.close()