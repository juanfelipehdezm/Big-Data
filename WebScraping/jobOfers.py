import time
from bs4 import BeautifulSoup
import requests

nonWantedSkill = input("Put some skills your are not familiar with: ")
print(f"filtering out {nonWantedSkill}")


def getJobsInfo():

    connection = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")

# print(connection)

    html_text = connection.text
    bs4 = BeautifulSoup(html_text, "lxml")
    # the job info is on the tag <li> of class = "clearfix job-bx wht-shd-btx"
    jobs_info = bs4.find_all("li", class_="clearfix job-bx wht-shd-bx")

    count = 0
    for index, job in enumerate(jobs_info):
        published_date = job.find("span", class_="sim-posted").span.text
        # filtering for published dates with FEW days differences
        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text
            skills = job.find("span", class_="srp-skills").text
            more_info = job.header.h2.a.get("href")

            # filtering the skill we are not good at

            if nonWantedSkill not in skills:
                with open(f"jobs posts/{index}post.txt", "w") as fileToWrite:

                    fileToWrite.write(
                        f"Company Name: {company_name.strip()} \n")
                    fileToWrite.write(f"Required Skills: {skills.strip()} \n")
                    fileToWrite.write(f"Apply here: {more_info} \n")
                    fileToWrite.write("----------------------")

                    print(f"File {index}.txt created")

                count += 1

    print(f"There where found {count} jobs")


if __name__ == '__main__':
    while True:
        getJobsInfo()
        print("This program will be excuted in 10 Minutes....")
        time.sleep(600)
