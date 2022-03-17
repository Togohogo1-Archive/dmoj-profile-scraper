import requests
from bs4 import BeautifulSoup

'''
reading and writing to txt to be implemented
'''
myVis = 0
images = []

link = requests.get("https://dmoj.ca/user/Togohogo1")
soup = BeautifulSoup(link.content, "html.parser")

spanContent = soup.findAll("div", {"class": "content-description"})
spanSidebar = soup.findAll("div", {"class": "user-sidebar"})
spanDiv = spanSidebar[0].findAll("div")

for div in spanDiv:
    # Solved, Rank by points, Rank by rating, Volatility
    if "solved" in div.text or "Rank" in div.text or "Rating" in div.text or "Volatility" in div.text:
        print(div.text)

    # Total points rounded to 2 decimal places
    for span in div.findAll("span"):
        try:
            print("Total points:", span["title"])
        except KeyError:
            pass

# Getting all image links (to be safe)
for div in spanContent:
    for img in div.findAll("img"):
        images.append(img["src"])

for link in images:
    try:
        # Every time the camo.algome.me link is requested, the counter goes up by 1
        # Saving the number of times this program runs to a .txt file and then subtracting it from the total
        imgLink = requests.get(link)
        soup = BeautifulSoup(imgLink.content, "html.parser")
        print("Total traffic:", soup.findAll("text")[-1].text)
    except:
        pass
