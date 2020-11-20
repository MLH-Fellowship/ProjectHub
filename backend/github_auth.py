import requests
from github import Github as _Github
import re
from datetime import datetime, timedelta, timezone
from settings import GITHUB_CLIENT_ID, GITHUB_SECRET


def request_access_token(code):

    client_id = GITHUB_CLIENT_ID
    client_secret = GITHUB_SECRET

    url = "https://github.com/login/oauth/access_token"

    data = {"client_id": client_id,
            "client_secret": client_secret,
            "code": code}

    req = requests.post(url=url, data=data)
    content = req.content.decode("utf-8")
    token = re.findall(r"access_token=(.*)&scope", content)

    try:
        return token[0]
    except IndexError:
        return "Invalid Request"

class GitHub(object):

    @classmethod
    def from_code(cls, code: str):
        return cls(at=request_access_token(code))
    
    @classmethod
    def from_jwe(cls, jwe: str):
        #TODO: decode and grab access token from jwe
        pass

    def __init__(self, at=None):
        self.dt = None
        self.access_token = at
            

    def expire_token(self):
        """

        :return:
        """
        if self.dt is None:
            self.dt = datetime.now(tz=timezone.utc)
        elif self.dt + timedelta(hours=12) > datetime.now(tz=timezone.utc):
            self.access_token = request_access_token(self.code)

    def get_orgs(self):

        auth = _Github(self.access_token)
        user = auth.get_user()
        return [i.name for i in user.get_orgs()]

    def get_teams(self):

        # Authenticates the user with Github
        auth = _Github(self.access_token)

        # Creates an authenticated user object
        org = auth.get_user()

        # Gets the teams the authenticated user is in, in the form of a paginated list
        team_list = org.get_teams()
        """
        returns all the teams the user is in, with get_teams[0] being the pods the user is in, and get_teams[1] being
        all other teams
        """
        pods = [i.name for i in team_list if "pod" in i.name.lower()]
        # teams = [i.name for i in team_list if "pod" not in i.name.lower()]
        return {"pods": pods}

    def meta(self):
        auth = _Github(self.access_token)
        user = auth.get_user()
        login = user.login
        name = user.name
        avatar = user.avatar_url
        return {"login": login, "name": name, "avatar": avatar}

    def id(self):
        auth = _Github(self.access_token)
        user = auth.get_user()
        return user.id
