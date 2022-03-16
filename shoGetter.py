import requests
import urllib.request
import bs4 as bs

allShoPages = ["http://www.trngcmd.marines.mil/Units/Northeast/The-Basic-School/Academics/FY16-PHASE-0/",
               "http://www.trngcmd.marines.mil/Units/Northeast/The-Basic-School/Academics/FY16-PHASE-l/",
               "http://www.trngcmd.marines.mil/Units/Northeast/The-Basic-School/Academics/FY16-PHASE-ll/"]

for page in allShoPages:
    source = urllib.request.urlopen(page)
    # print(len(source.content))
    soup = bs.BeautifulSoup(source, "html.parser")
    num = soup.find_all['DownloadCell']
    print(str(num))
