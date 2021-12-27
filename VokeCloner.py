from urllib.error import URLError, HTTPError
import urllib.request
import datetime
import time
import string
import difflib
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sprint(str):

   for c in str + '\n':

     sys.stdout.write(c)

     sys.stdout.flush()

     time.sleep(3./90)


sprint (bcolors.OKCYAN + "გამარჯობათ. tool-ი შექმინლია ლევან ყიფიანი-DคᖙuvͥØkͣeͫ-ის მიერ @2021. აღნიშნული ხელაწყო შექმნილია მხოლოდ სასწავლო მიზნებისთვის. დაკოპირებული URL იქნება იმავე დირექტორიაში სადაც პროგრამაა შენახული" + bcolors.BOLD)

class WebsiteToMonitor:

    def __init__(self, url):
        self.filename = self.create_filename(url)
        self.url = url
        # არსებული საიტის კოპის შექმნა და მონიტორიგი.
        new_site = self.download_site(self.url)
        self.save_site(new_site, self.filename)

    def create_filename(self, url):
        filename = "".join([i.replace(i, "") if i not in string.ascii_letters else i for i in url])
        current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        filename = f"{filename}_{current_time}.html"
        return filename

    def download_site(self, url):
        try:
            response = urllib.request.urlopen(url)
            web_content = response.read().decode("utf-8")
            return web_content
        except HTTPError:
            return "HTTPError"
        except URLError:
            return "URLError"

    def save_site(self, content, filename):
        f = open(filename, mode="w", encoding="utf-8")
        f.write(content)
        f.close()
        pass

    def show_difference(self, old, new):
        s = difflib.SequenceMatcher(None, old, new)
        for block in s.get_matching_blocks():
            print(block)
        pass

    def compare_site(self):
        new_content = self.download_site(self.url)
        old_content = open(self.filename, mode="r", encoding="utf-8").read()
        try:
            if new_content.split("</head>")[1] != old_content.split("</head>")[1] or new_content.split("</HEAD>")[1] \
                    != old_content.split("</HEAD>")[1]:
                print("Tსაიტზე მოხდა განახლება")
                self.show_difference(old_content, new_content)
                self.filename = self.create_filename(self.url)
                self.save_site(new_content, self.filename)
                pass
        except IndexError:
            print("მოხდა შეცდომა")
            pass
sprint (bcolors.OKCYAN + "დარწმუნდით რომ შეცვალეთ URL" + bcolors.BOLD)

if __name__ == "__main__":
    test_monitor = WebsiteToMonitor("https://მაგალითი.com")
    while True:
        time.sleep(60)
        test_monitor.compare_site()
 