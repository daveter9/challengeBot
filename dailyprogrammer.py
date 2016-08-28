import re
import praw



class Scraper:
    user_agent = 'daily programmer test scrapper'
    thing_limit=10

    already_done_easy=[]

    def __init__(self):
        self.r= praw.Reddit(self.user_agent)


    def get_newest_easy(self):
        subreddit = self.r.get_subreddit('dailyprogrammer')
        for submission in subreddit.get_hot(limit=10):
            if submission.id not in self.already_done_easy and self._check_easy(submission.title):
                print(submission.title)
                self.already_done_easy.append(submission.id)


    def _check_easy(self,title):
        regex_easy = '.*?\[.*?(\[)(Easy).*?..*?..*?..*?..*?(.)'
        rg = re.compile(regex_easy,re.IGNORECASE | re.DOTALL)
        return rg.search(title)

a=  Scraper()
a.get_newest_easy()









