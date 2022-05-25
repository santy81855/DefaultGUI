appName = "AppName"
logoName = "logo.ico"
# make the resolution global variables
screen_resolution = 0
width = 0
height = 0
key = ''
res = {}
res["1920x1080"] = [1920/2, 0] # full hd
res["2560x1440"] = [2560/2, 0] # wqhd
res["3440x1440"] = [3440/2, 0] # ultrawide
res["3840x2160"] = [3840/2, 0] # 4k
focused = False # variable to track if the gui is focused so it knows to track typing or not
opacity = 0.98

# variable to track the margins used on the main layout
MARGIN = 5
# variable to allow going back to previous size after maximizing
isMaximized = False

# variables to store the mainwindow and title bar
application = None
mainWin = None
titleBar = None

# variable to be able to snap to sides and corners
leftDown = False
upDown = False
downDown = False
rightDown = False
# variablee to track if the snap widget is up
isSnapWidget = False

# variables for color settings
backgroundColor = "#2E3440"
accentColor1 = "#8FBCBB"
accentColor2 = "#A3BE8C"

bracketColor = "#D08770"
keywordColor = "#81A1C1"
parenColor = "#EBCB8B"
braceColor = "#D08770"
functionColor = "#88C0D0"
commentColor = "#4C566A"
textColor = "#D8DEE9"
stringColor = "#8FBCBB"
numberColor = "#BF616A"
selectionColor = "#4C566A"
curLineColor = "#3B4252"
selectionTextColor = "#D8DEE9"
operatorColor = "#EBCB8B"
unclosedString = "#BF616A"