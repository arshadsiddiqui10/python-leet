from bs4 import BeautifulSoup
import requests
subject = input("Enter technology name:")
html_text = requests.get('https://stackoverflow.com/questions/tagged/'+subject).text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
questions = soup.find_all('div', class_='s-post-summary js-post-summary')
# print(questions)
for q in questions:
    # find with number of answers
    div_ans = q.find('div', class_='s-post-summary--stats-item')
    num_ans = div_ans.find('span','s-post-summary--stats-item-number').text
    q_header = q.find('div', class_='s-post-summary--content')
    q_text = (q_header.find('h3').find('a')['href'])
    q_text = q_text.split('/')[3]
    timeq = soup.find('span', class_='relativetime')
    print(f'Question: {q_text} raised at {timeq.text}  with {num_ans} answers')
