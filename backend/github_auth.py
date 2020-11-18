import requests
from github import Github
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

class GH(object):

    def __init__(self, username, code, at=None):
        self.username = username
        self.dt = None
        self.code = code

        if at is None:
            self.access_token = request_access_token(code)
        else:
            self.access_token = at

    def expire_token(self):
        """

        :return:
        """
        if self.dt is None:
            self.dt = datetime.now(tz=timezone.utc)
        else:
            if self.dt + timedelta(hours=12) > datetime.now(tz=timezone.utc):
                self.access_token = request_access_token(self.code)
            else:
                pass

    def get_orgs(self):

        auth = Github(self.access_token)
        user = auth.get_user(self.username)
        return [i.name for i in user.get_orgs()]

    def get_teams(self):

        # Authenticates the user with Github
        auth = Github(self.access_token)

        # Creates an authenticated user object
        org = auth.get_user()

        # Gets the teams the authenticated user is in, in the form of a paginated list
        team_list = org.get_teams()
        """
        returns all the teams the user is in, with get_teams[0] being the pods the user is in, and get_teams[1] being
        all other teams
        """
        pods = [i.name for i in team_list if "pod" in i.name.lower()]
        teams = [i.name for i in team_list if "pod" not in i.name.lower()]
        return {"pods": pods, "teams": teams}
