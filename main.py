from bs4 import BeautifulSoup

with open('index.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    courses_cards = soup.find_all('div',class_ = "card")
    table= {}
    for course in courses_cards:
        course_name, course_price = course.h5.text,course.a.text.split()[-1]
        table[course_name]=course_price
    print(table)