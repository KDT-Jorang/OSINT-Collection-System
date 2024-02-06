import requests
import os
from bs4 import BeautifulSoup


class more_information:
    def __init__(self):
        self.site_list = ["GitHub"]
        self.timeout = 60

    def __get_github(self, username):
        url = "https://www.github.com/" + username
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
        }
        resp = requests.get(url=url, headers=headers, timeout=self.timeout)

        if (
            resp.text.find('itemtype="http://schema.org/Organization"') == -1
        ):  # for users
            url = url + "?tab=repositories"

            # html to soup
            resp = requests.get(url=url, headers=headers, timeout=self.timeout)
            soup = BeautifulSoup(resp.text, "html.parser")

            # find profile image
            profile = soup.find(attrs={"alt": f"View {username}'s full-sized avatar"})
            profile = profile["src"]
        else:  # for Organizations
            # get profile image
            soup = BeautifulSoup(resp.text, "html.parser")
            soup = soup.find(
                attrs={"class": "avatar flex-shrink-0 mb-3 mr-3 mb-md-0 mr-md-4"}
            )
            profile = soup["src"]

            url = f"https://www.github.com/orgs/{username}/repositories"

            # html to soup
            resp = requests.get(url=url, headers=headers, timeout=self.timeout)
            soup = BeautifulSoup(resp.text, "html.parser")

        # parsing soup
        lis = soup.find_all(attrs={"itemprop": "name codeRepository"})

        git_info = []
        git_info.append({"repo_exist": False})
        git_info.append({"profile": profile})

        if lis == []:
            return git_info

        git_info[0]["repo_exist"] = True

        # get title & link
        for li in lis:
            title = li["href"].split("/")[2:][0]
            link = "https://github.com" + li["href"]
            git_info.append({"title": title, "link": link})

        return git_info

    def get_information(self, site, username, path="./"):
        if site == "GitHub":
            git_info = self.__get_github(username)

        path = path.replace("\\", "/")
        if path[-1] != "\\" or path[-1] != "/":
            path = path + "/"
        path = f"{path}{username}"

        if not os.path.exists(path):
            os.mkdir(path)

        # profile image save
        with open(f"{path}/GitHub_Profile.png", "wb") as f:
            resp = requests.get(git_info[1]["profile"])
            f.write(resp.content)
        # repo link save(.txt)
        if git_info[0]["repo_exist"]:
            with open(f"{path}/GitHub_Repo.txt", "w") as f:
                for s in git_info[2:]:
                    f.write(f'{s["link"]}\n')
