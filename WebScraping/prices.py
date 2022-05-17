from bs4 import BeautifulSoup
from sympy import content

with open("home.html", "r") as html_file:
    content = html_file.read()

    bs4 = BeautifulSoup(content, "lxml")

    course_cards = bs4.find_all("div", class_="card")

    for course in course_cards:
        courseName = course.h5.text
        coursePrice = course.a.text.split(" ")[-1]

        print(f"The course {courseName} costs {coursePrice}")
