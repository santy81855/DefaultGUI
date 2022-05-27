# The name that appears at the top of the title bar
appName = "AppName"
# The logo for the taskbar
logoName = "logo.ico"
# Toggle the bar at the bottom with the snap features
infoBar = True
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
# make the close button red when you hover over it
darkRed = "#990000"
closeButtonHover = darkRed

# color schemes - uncomment one at a time to try them out

# 1 - Nord
salmon = "#D08770"
lightBlue = "#81A1C1"
skyBlue = "#88C0D0"
lightGrey = "#E5E9F0"
mediumGrey = "#4C566A"
blueGrey = "#D8DEE9"
pastelRed = "#BF616A"
darkGrey = "#3B4252"
seaFoamGreen = "#8FBCBB"
oliveGreen = "#A3BE8C"
darkestGrey = "#3B4252"

backgroundColor = darkestGrey
accentColor1 = seaFoamGreen
'''
# 2 - Forest
almostBlack = "#121e26"
deepForestGreen = "#283635"
lightBeige = "#f4efeb"
beige = "#d2c0b2"
clay = "#9d6556"

backgroundColor = almostBlack
accentColor1 = lightBeige
'''
'''
# 3 - Blue
purple = "#9674d4"
midnightBlue = "#101356"
offWhite = "#fbfdf6"
brightBlue = "#81ffff"
grey = "#e8e8e8"

backgroundColor = midnightBlue
accentColor1 = grey
'''
'''
# 4 - Soft beach colors
brightBlue = "#51e2f5"
blueGreen = "#9df9ef"
dustyWhite = "#edf756"
pinkSand = "#ffa8B6"
darkSand = "#a28089"

backgroundColor = midnightBlue
accentColor1 = grey
'''
'''
# 5 - Purple color scheme
iceCold = "#a0d2eb"
freezePurple = "#e5eaf5"
mediumPurple = "#d0bdf4"
purplePain = "#8458B3"
heavyPurple = "#494D5F"

backgroundColor = heavyPurple
accentColor1 = freezePurple
'''
'''
# 6 - Deep blue and tan
sandTan = "#e1b382"
sandTanShadow = "#c89666"
nightBlue = "#2d545e"
nightBlueShadow = "#12343b"

backgroundColor = nightBlue
accentColor1 = sandTan
'''