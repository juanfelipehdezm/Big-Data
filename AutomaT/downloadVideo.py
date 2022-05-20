import requests
from bs4 import BeautifulSoup
import sys
import json

# https://www.ted.com/talks/elizabeth_strickler_nfts_the_metaverse_and_the_future_of_digital_art

# getting url from user in argvs
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter a TED talk url...")


def connectAndParse(url):
    connection = requests.get(url)
    print(f"Download about to start, status = {connection}")
    return BeautifulSoup(connection.text, "lxml")


bs4 = connectAndParse(url)

nextDataScript = bs4.find(id="__NEXT_DATA__")

jsonObject_nextData = json.loads(nextDataScript.string)


def formatJsonObject(jsonObject):
    return json.dumps(jsonObject, indent=4)


formatJsonNextData = formatJsonObject(jsonObject_nextData)

# print(formatJsonObject)

# We need to get until player data
playerData = jsonObject_nextData["props"]["pageProps"]["videoData"]["playerData"]

# print(playerData) again to json
url_content = json.loads(playerData)

formatUrlContent = formatJsonObject(url_content)

# print(formatUrlContent)
# we need to get to the url
url_mp4 = url_content["resources"]["h264"][0]["file"]

video = requests.get(url_mp4)

print(url_mp4)

with open("ted_talk_video.mp4", "wb") as mp4File:
    mp4File.write(video.content)

    print("Video succesfully download")
