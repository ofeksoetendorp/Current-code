import webbrowser
import os
try:
	import googlesearch
except ImportError:
    print("No module named 'google' found")


def search(search_value, do_open=True):
    url = 'https://www.google.com/search?q=' + search_value
    if do_open is True:
        webbrowser.open(url)
    return url


def open(site_name):
    val = open_app(site_name,apps)
    if val != None:
        os.startfile(val)
    else:
        for j in googlesearch.search(site_name, tld="co.in", num=1, stop=1):
            webbrowser.open(j)


def open_app(word,dict):
    for k in dict.keys():
        if k in word:
            return dict[k]
    return None


apps = {"word":"WINWORD.EXE","powerpoint":"POWERPNT.EXE","notepad":"notepad.exe","excel":"EXCEL.EXE","python":"python.exe","visual studio":"devenv.exe","steam":"C:\\Users\\gall_\\Desktop\\Steam\\steam.exe"}

#import subprocess
#cmd= '"C:\\Program Files\\Microsoft Office\\root\\\Office16\\POWERPNT.exe" %s'
#cmd = ""
#chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
#cmd = '"C:\\Program Files\\Microsoft Office\\root\\\Office16\\POWERPNT.exe"'
cmd = '"C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE"'
cmd = '"C:\\Users\\gall_\\Desktop\\Steam\\steam.exe"'
cmd = '"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"'
#subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
#open("steam")
