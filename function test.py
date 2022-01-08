import winapps
import subprocess


def getPossibleExePaths(appPath):
    if not appPath:
        raise Exception("App Path cannot be None")
    pattern = appPath + ":*exe"
    try:
        returned = subprocess.check_output(['where', pattern]).decode('utf-8')
        listOfPaths = filter(None, returned.split(os.linesep))
        return [i.strip() for i in list(listOfPaths)]
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error getting path for '{appPath}'")

def getAppPath(appName):
    for app in winapps.search_installed(appName):
        installPath = str(app.install_location)
        if installPath and installPath != "None":
            return installPath
    return None


#print(getPossibleExePaths(getAppPath('chrome')))
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
