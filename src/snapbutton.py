from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config

class SnapButton(QPushButton):
    def __init__(self, parent):
        super(SnapButton, self).__init__()
        self.parent = parent
        self.setText("snap")
        self.adjustSize()
        #self.setMaximumSize(100, 20)
        self.setStyleSheet("""
            QPushButton
            {
            background-color: """+config.backgroundColor+"""; 
            border:none;
            color:"""+config.accentColor1+""";
            font: 12pt "Consolas";
            padding-left: 5px;
            padding-right: 5px;
            padding-top: 5px;
            padding-bottom: 5px;
            }
                                """)
        self.setMouseTracking(True)
    
    def mousePressEvent(self, event):
        config.mainWin.snapWidget.hide()
    
    def mouseReleaseEvent(self, event):
        config.mainWin.snapWidget.show()

    # when we hover over this widget should show but disappear when we unhover
    def mouseMoveEvent(self, event):
        # first determine if we are using the height or the width to calculate the widget dimensions
        maxHeight = 295
        maxWidth = 600
        width = 0
        height = 0
        if self.parent.width() > self.parent.height():
            if int(self.parent.height() / 2.5) < maxHeight:
                height = int(self.parent.height() / 2.5)
                width = 2 * height
            else:
                height = maxHeight
                width = maxWidth
        else:
            if int(self.parent.width() / 2) < maxWidth:
                width = int(self.parent.width() / 2)
                height = int(width / 2)
            else:
                height = maxHeight
                width = maxWidth
        # now that we have the width and height of the widget we create the button sizes
        middleWidth = int(width / 5)
        middleHeight = int(height / 2 + 10) # the 10 accounts for the spacing of the vertical layouts
        cornerHeight = int(height / 4)
        cornerWidth = middleWidth
        longHeight = cornerHeight
        longWidth = int(middleWidth * 3 + 10) # the 10 accounts for the spacing of the layout

        # create the correct font for the size
        font = QFont()
        font.setFamily("Verdana")
        font.setFixedPitch( True )
        font.setPointSize(width / 50)

        # now set the buttons
        self.parent.snapWidget.max.setFixedSize(middleWidth, middleHeight)
        self.parent.snapWidget.max.setFont(font)
        self.parent.snapWidget.min.setFixedSize(middleWidth, middleHeight)
        self.parent.snapWidget.min.setFont(font)
        self.parent.snapWidget.left.setFixedSize(middleWidth, middleHeight)
        self.parent.snapWidget.left.setFont(font)
        self.parent.snapWidget.middle.setFixedSize(middleWidth, middleHeight)
        self.parent.snapWidget.middle.setFont(font)
        self.parent.snapWidget.right.setFixedSize(middleWidth, middleHeight)
        self.parent.snapWidget.right.setFont(font)
        self.parent.snapWidget.topleft.setFixedSize(cornerWidth, cornerHeight)
        self.parent.snapWidget.topleft.setFont(font)
        self.parent.snapWidget.topright.setFixedSize(cornerWidth, cornerHeight)
        self.parent.snapWidget.topright.setFont(font)
        self.parent.snapWidget.bottomleft.setFixedSize(cornerWidth, cornerHeight)
        self.parent.snapWidget.bottomleft.setFont(font)
        self.parent.snapWidget.bottomright.setFixedSize(cornerWidth, cornerHeight)
        self.parent.snapWidget.bottomright.setFont(font)
        self.parent.snapWidget.bottom.setFixedSize(longWidth, longHeight)
        self.parent.snapWidget.bottom.setFont(font)
        self.parent.snapWidget.top.setFixedSize(longWidth, longHeight)
        self.parent.snapWidget.top.setFont(font)

        QApplication.setOverrideCursor(Qt.PointingHandCursor)
        mainPosition = self.parent.mapToGlobal(QPoint(0,self.parent.height()))
        print(mainPosition.y())
        print(config.mainWin.height())
        print(height)
        self.parent.snapWidget.show()
        # the -50 in the y coordinate accounts for the padding and the spacing between layouts
        config.mainWin.snapWidget.setGeometry(mainPosition.x() + (config.mainWin.width() - self.parent.snapWidget.width()) / 2, mainPosition.y() - height - 50 - self.height(), width, height)
        config.isSnapWidget = True
        
