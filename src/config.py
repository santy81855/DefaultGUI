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

# variable for the minimum resolution (minSize x minSize)
minSize = 500
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

# some sample colors
salmon = "#D08770"
lightBlue = "#81A1C1"
beige = "#EBCB8B"
skyBlue = "#88C0D0"
lightGrey = "#E5E9F0"
mediumGrey = "#4C566A"
blueGrey = "#D8DEE9"
pastelRed = "#BF616A"
darkGrey = "#3B4252"
seaFoamGreen = "#8FBCBB"
oliveGreen = "#A3BE8C"
darkestGrey = "#3B4252"
darkRed = "#990000"

# variables for color settings
backgroundColor = lightGrey
accentColor1 = darkestGrey
accentColor2 = lightGrey

closeButtonHover = darkRed