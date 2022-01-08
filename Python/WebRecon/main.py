# import sys
import ssl
import win32api
import requests
import argparse
from re import search
from time import sleep
from bs4 import BeautifulSoup as bs4
from selenium.webdriver.common.by import By

from Util.Utilities import Utilities
from WebDriver.webDriverConfig import webdriverCfg


class Recon:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='[+] This script automates the webRecon, that is, it searches for links on the site, performs a simple Google Hacking and finally a DNS Brute Force')
        parser.add_argument("-U", "--url", help="[+] Please enter the url", type=str, required=True)
        parser.add_argument("-ex", "--extension",
                            help="[+] Please enter the extension so that we can perform a Google hack.\n "
                                 "Default: 'txt', 'doc', 'php', 'csv', 'pdf', 'xls', 'xlsx', 'sh', 'js', 'sql', 'zip', 'gz', 'asp', 'hta',\
                                    'html', 'py'",
                            type=str, default="")
        self.args = parser.parse_args()

    headers = {
        'ccept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'pt-BR,pt;q=0.9',
        'Connection': 'keep-alive',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    server = ""
    context = ssl.SSLContext()

    def bootUp(self):
        self.webRecon()

    def webRecon(self):
        try:
            url = self.args.url
            url = url.split("/")
            if search("https", url[0]) or search("http", url[0]):
                userName = win32api.GetUserName()
                print(f"[+] Hello {userName}!")
                self.infoUrl(self.args.url)
                self.findCveServer()
                self.findItensUrl(self.args.url)
                self.findExtensions(self.args.url)
                self.findIndexOf(self.args.url)
                self.findRobots(self.args.url)
                self.whois(self.args.url)
                print("\n\n[+] Thanks for using the tool :)")
            else:
                print("[-] '-U' parameter argument is not a URL")
                exit()
        except Exception as err:
            err = str(err)
            print(f"[-] An error has occurred: {err}")
        finally:
            input("[+] Press enter to exit...")
            exit(0)

    def infoUrl(self, url):
        try:
            print("[+] Recovering Server and HTTP_VERBS_ACCEPT: ")
            head = requests.get(url, headers=self.headers)
            options = requests.options(url, headers=self.headers)
            if "X-Powered-By" in head.headers:
                print(f"    [+]  Language: {head.headers['X-Powered-By']}")
                if search("ASP", head.headers['X-Powered-By']):
                    print(f"    [+]  AspNet Version: {head.headers['X-AspNet-Version']}")
                    print(f"    [+]  AspNetMvc Version: {head.headers['X-AspNetMvc-Version']}")
            if "Server" in head.headers:
                print(f"    [+] Server: {head.headers['Server']}")
                self.server = head.headers['Server']
            if "allow" in options.headers:
                print(f"    [+]  HTTP_VERBS_ACCEPT: {options.headers['allow']}")
        except Exception as err:
            raise err

    def findCveServer(self):
        try:
            print("    [+] Searching CVE in Server:")
            gh = f"https://www.google.com/search?q=site%3Ahttps%3A%2F%2Fwww.cvedetails.com%2F+{self.server}"
            html = requests.get(gh, "html.parser")
            soupGh = bs4(html.content, 'html.parser')
            foundLink = []
            for href in soupGh.find_all('a', href=True):
                if search("/url", href['href']):
                    foundLink.append(href['href'])
            if len(foundLink) == 0:
                print("        [-] Could not find links directed to Server :/")
                return
            del foundLink[-2::]
            for link in foundLink:
                link = link.replace("/url?q=", "")
                linkSplit = link.split("&sa")
                if search("%3Fvendor_id%", linkSplit[0]):
                    linkSplit_2 = linkSplit[0].split("%3Fvendor_id%")
                    print(f"        [*] CVE found: {linkSplit_2[0]}")
                else:
                    print(f"        [*] CVE found: {linkSplit[0]}")
        except Exception as err:
            raise err

    def findItensUrl(self, url):
        try:
            res = requests.get(url, headers=self.headers, verify=self.context)
            soup = bs4(res.content, "html.parser")
            print("    [+] Searching links:")
            for href in soup.find_all('a', href=True):
                if not search("#", href['href']):
                    print(f"        [*] Links found: {href['href']}")
            print("    [+] Searching Directories:")
            for folder in soup.find_all('script'):
                try:
                    print(f"        [*] Links found: {folder['src']}")
                except KeyError:
                    pass
        except Exception as err:
            raise err

    @classmethod
    def findIndexOf(cls, url):
        try:
            urlSplit = url.split("/")
            print("    [+] Looking for possible IndexOf")
            indexOf = f"https://www.google.com/search?q=site%3A{urlSplit[2].replace('www.', '')}+indexOf"
            html = requests.get(indexOf, "html.parser")
            soupIndexOf = bs4(html.content, 'html.parser')
            foundIndexOf = []
            for href in soupIndexOf.find_all('a', href=True):
                if search("/url", href['href']):
                    foundIndexOf.append(href['href'])
            if len(foundIndexOf) <= 2:
                print("        [-] Could not find any IndexOf :/")
                return
            del foundIndexOf[-2::]
            for link in foundIndexOf:
                link = link.replace("/url?q=", "")
                if not search("/search", link) and not search("google", link):
                    linkSplit = link.split("&sa")
                    print(f"        [*] IndexOF found: {linkSplit[0]}")
        except Exception as err:
            raise err

    def findExtensions(self, url):
        try:
            paramEx = self.args.extension
            urlSplit = url.split("/")
            wasFound = False
            if paramEx == "":
                ext = ['txt', 'doc', 'php', 'csv', 'pdf', 'xls', 'xlsx', 'sh', 'js', 'sql', 'zip', 'gz', 'asp', 'hta',
                       'html', 'py']
                print("    [+] Looking for the following extensions: ")
                print(f"        [*] Extensions: {ext}")
                for i in ext:
                    lookingGoogle = f"https://www.google.com/search?q=site%3A{urlSplit[2].replace('www.', '')}+ext%3A{i}"
                    html = requests.get(lookingGoogle, "html.parser")
                    soupGh = bs4(html.content, 'html.parser')
                    foundLink = []
                    for href in soupGh.find_all('a', href=True):
                        if search("/url", href['href']):
                            foundLink.append(href['href'])
                    if len(foundLink) <= 2:
                        continue
                    del foundLink[-2::]
                    for link in foundLink:
                        link = link.replace("/url?q=", "")
                        if not search("/search", link):
                            linkSplit = link.split("&sa")
                            print(f"        [*] {i.upper()} found: {linkSplit[0]}")
                            wasFound = True
            else:
                print("    [+] Looking for the extension: ")
                print(f"        [*] Extensions: {paramEx}")
                lookingGoogle = f"https://www.google.com/search?q=site%3A{urlSplit[2].replace('www.', '')}+ext%3A{paramEx}"
                html = requests.get(lookingGoogle, "html.parser")
                soupGh = bs4(html.content, 'html.parser')
                foundLink = []
                for href in soupGh.find_all('a', href=True):
                    if search("/url", href['href']):
                        foundLink.append(href['href'])
                if len(foundLink) <= 2:
                    print("        [-] Could not find any file with the specified extension(s) :/")
                    return
                del foundLink[-2::]
                for link in foundLink:
                    link = link.replace("/url?q=", "")
                    if not search("/search", link):
                        linkSplit = link.split("&sa")
                        print(f"        [*] {paramEx.upper()} found: {linkSplit[0]}")
                        wasFound = True
            if not wasFound:
                print("        [-] Could not find any file with the specified extension(s) :/")
                return
        except Exception as err:
            raise err

    def findRobots(self, url):
        try:
            print("[+] Checking if the file \"robots.txt\" exists:")
            robots = requests.get(f"{url}/robots.txt", headers=self.headers, verify=self.context)
            if robots.status_code == 200:
                content = robots.content
                content = content.decode('utf-8').split("\n")
                for i in content:
                    print(f"    {i}")
            else:
                print("[+] Checking if the file \"robots.txt\" exists: not exists")
        except Exception as err:
            raise err

    @classmethod
    def whois(cls, url):
        driver = webdriverCfg()
        try:
            print("[+] Checking Whois:")
            print("     [+] Hold...")
            util = Utilities(driver)
            urlSplit = url.split("/")
            driver.get(f"https://registro.br/tecnologia/ferramentas/whois/?search={urlSplit[2].replace('www.', '')}")
            sleep(2)
            if not util.checkExistsXpath():
                driver.execute_script(
                    "document.querySelector('#app > main > section > div.whois-response.active > div.box-white > p > a').click()")
                sleep(2)
                info = driver.find_element(By.XPATH, "//html/body/div/main/section/div[2]/div[2]/pre").text
                print("     [+] Found this information about the host:")
                print(f"{info}")
            else:
                print("     [-] Sorry, unable to retrieve Whois information")
        except Exception as err:
            raise err
        finally:
            driver.close()
            driver.quit()


if __name__ == "__main__":
    Recon().bootUp()
