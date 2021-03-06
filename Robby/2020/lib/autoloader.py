import requests
import pickle
import json
from bs4 import BeautifulSoup

class Autoloader():
    def __init__(self, url=None):
        self.url = url
        config_file = open('.config', 'rb')
        self.config = pickle.load(config_file)

    def print_data(self):
        print(f"Url = {self.url}")

    def fetch(self, url=None):
        if url == None:
            url = self.url
        r = self.session.get(url)
        self.data = r.text
        return self.data
    
    def f_fetch(self, year, day):
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        in_filename = f'./inputs/y{year}d{day}'
        try:
            f = open(in_filename, 'r')
            s = load(f)
            f.close()
        except FileNotFoundError:
            s = self.fetch(url)
            f = open(in_filename, 'wb')
            pickle.dump(s, f)
            f.close()
        return s



    def connect(self):
        aocauthurl = 'https://adventofcode.com/auth/github'
        ghauthurl = 'https://github.com/session'
        payload = {'login':self.config['github_user'], 'password':self.config['github_pass'], 'commit':'Sign in', 'utf8':'%E2%9C%93'}
        session = requests.Session()
        ghresponse = session.get(ghauthurl)
        soup = BeautifulSoup(ghresponse.text, 'html5lib')
        payload['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']

        ghresponse = session.post(ghauthurl, data=payload)
        s = session.get(aocauthurl)
        self.session = session

    def aoc_parser(self, mode='Auto'):
        if mode == 'Auto':
            if len(self.data.splitlines()) > 1:
                mode = 'lines'
            else:
                mode = 'string'
        if mode == 'lines':
            return self.aoc_line_parse()
        elif mode == 'string':
            return self.aoc_str_parse()


