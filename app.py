
import requests  
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
for question in questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(".s-post-summary--stats-item-number").getText())
    print(question.select_one(".s-post-summary--stats-item-unit").getText())

    # print(question.select_one(".s-post-summary--stats-item  ").getText())
    # print(question.select_one(".s-post-summary--stats-item-number").getText())
    # print(question.select_one(".s-post-summary--stats-item-unit").getText())


    #Extract values
    # votes = soup.find('div', class_='s-post-summary--stats-item__emphasized').find('span', class_='s-post-summary--stats-item-number').text
    # answers = soup.find('div', title='0 answers').find('span', class_='s-post-summary--stats-item-number').text
    # views = soup.find('div', title='2 views').find('span', class_='s-post-summary--stats-item-number').text

    # print("Votes:", votes)
    # print("Answers:", answers)
    # print("Views:", views)

