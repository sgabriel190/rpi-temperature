import os

# Navigating os functions
def cdToRoot():
    try:
        os.chdir("/")
    except:
        print("Log: Error changing current directory to root.")

def cdToPath(path):
    try:
        cdToRoot()
        os.chdir(path)
    except:
        print("Log: Error changing currect directory to a specific path.")