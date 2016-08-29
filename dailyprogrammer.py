import re
import praw



class Scraper:
    user_agent = 'daily programmer test scrapper'
    thing_limit=10

    already_done=[]

    def __init__(self):
        self.r= praw.Reddit(self.user_agent)


    def get_newest(self,difficulty='Easy'):
        '''
        Gets newest submmisions from /r/ dailyprogrammer
        :param difficulty: Easy, Intermediate, Hard
        :return:
        '''
        submission_links=[]
        subreddit = self.r.get_subreddit('dailyprogrammer')
        for submission in subreddit.get_hot(limit=10):
            if submission.id not in self.already_done and self._check(difficulty,submission.title):
                submission_links.append(submission.permalink)
                self.already_done.append(submission.id)
        return submission_links


    def _check(self,difficulty,title):
        regex_easy = '.*?\[.*?(\[)('+difficulty+').*?..*?..*?..*?..*?(.)'
        rg = re.compile(regex_easy,re.IGNORECASE | re.DOTALL)
        return rg.search(title)

a=  Scraper()
submission_links= a.get_newest('Easy')











