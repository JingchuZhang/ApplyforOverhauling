# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(925, 697)
        Form.setAutoFillBackground(True)
        self.l1_switch_type = QtWidgets.QComboBox(Form)
        self.l1_switch_type.setGeometry(QtCore.QRect(120, 190, 71, 21))
        self.l1_switch_type.setObjectName("l1_switch_type")
        self.l1_switch_type.addItem("")
        self.l1_switch_type.addItem("")
        self.l1_switch_type.addItem("")
        self.genOffSteps = QtWidgets.QPushButton(Form)
        self.genOffSteps.setGeometry(QtCore.QRect(220, 660, 101, 23))
        self.genOffSteps.setObjectName("genOffSteps")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(550, 30, 253, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.r1_switch = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.r1_switch.setObjectName("r1_switch")
        self.gridLayout_2.addWidget(self.r1_switch, 3, 2, 1, 1)
        self.r1_loc = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.r1_loc.setObjectName("r1_loc")
        self.gridLayout_2.addWidget(self.r1_loc, 2, 2, 1, 1)
        self.r1_line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.r1_line.setObjectName("r1_line")
        self.gridLayout_2.addWidget(self.r1_line, 1, 2, 1, 1)
        self.r1_rightIsolator = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.r1_rightIsolator.setObjectName("r1_rightIsolator")
        self.gridLayout_2.addWidget(self.r1_rightIsolator, 5, 2, 1, 1)
        self.r1_ifRightOpen = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.r1_ifRightOpen.setCheckable(True)
        self.r1_ifRightOpen.setChecked(True)
        self.r1_ifRightOpen.setObjectName("r1_ifRightOpen")
        self.gridLayout_2.addWidget(self.r1_ifRightOpen, 5, 1, 1, 1)
        self.r1_ifRight = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.r1_ifRight.setChecked(True)
        self.r1_ifRight.setObjectName("r1_ifRight")
        self.gridLayout_2.addWidget(self.r1_ifRight, 5, 0, 1, 1)
        self.r1_station = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.r1_station.setObjectName("r1_station")
        self.gridLayout_2.addWidget(self.r1_station, 0, 2, 1, 1)
        self.r1_leftIsolator = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.r1_leftIsolator.setText("")
        self.r1_leftIsolator.setObjectName("r1_leftIsolator")
        self.gridLayout_2.addWidget(self.r1_leftIsolator, 4, 2, 1, 1)
        self.r1_if = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.r1_if.setChecked(True)
        self.r1_if.setObjectName("r1_if")
        self.gridLayout_2.addWidget(self.r1_if, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.r1_ifLeftOpen = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.r1_ifLeftOpen.setChecked(True)
        self.r1_ifLeftOpen.setObjectName("r1_ifLeftOpen")
        self.gridLayout_2.addWidget(self.r1_ifLeftOpen, 4, 1, 1, 1)
        self.r1_ifLeft = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.r1_ifLeft.setChecked(False)
        self.r1_ifLeft.setObjectName("r1_ifLeft")
        self.gridLayout_2.addWidget(self.r1_ifLeft, 4, 0, 1, 1)
        self.r1_ifSwitch = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.r1_ifSwitch.setChecked(True)
        self.r1_ifSwitch.setObjectName("r1_ifSwitch")
        self.gridLayout_2.addWidget(self.r1_ifSwitch, 3, 0, 1, 1)
        self.r1_ifRemote = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.r1_ifRemote.setObjectName("r1_ifRemote")
        self.gridLayout_2.addWidget(self.r1_ifRemote, 3, 1, 1, 1)
        self.l1_side = QtWidgets.QLineEdit(Form)
        self.l1_side.setGeometry(QtCore.QRect(370, 220, 51, 21))
        self.l1_side.setObjectName("l1_side")
        self.r1_side = QtWidgets.QLineEdit(Form)
        self.r1_side.setGeometry(QtCore.QRect(490, 270, 51, 21))
        self.r1_side.setObjectName("r1_side")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(550, 480, 253, 171))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.r2_loc = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.r2_loc.setObjectName("r2_loc")
        self.gridLayout_3.addWidget(self.r2_loc, 2, 2, 1, 1)
        self.r2_switch = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.r2_switch.setObjectName("r2_switch")
        self.gridLayout_3.addWidget(self.r2_switch, 3, 2, 1, 1)
        self.r2_ifRight = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.r2_ifRight.setChecked(True)
        self.r2_ifRight.setObjectName("r2_ifRight")
        self.gridLayout_3.addWidget(self.r2_ifRight, 5, 0, 1, 1)
        self.r2_ifLeft = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.r2_ifLeft.setChecked(False)
        self.r2_ifLeft.setObjectName("r2_ifLeft")
        self.gridLayout_3.addWidget(self.r2_ifLeft, 4, 0, 1, 1)
        self.r2_ifRightOpen = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.r2_ifRightOpen.setCheckable(True)
        self.r2_ifRightOpen.setChecked(True)
        self.r2_ifRightOpen.setObjectName("r2_ifRightOpen")
        self.gridLayout_3.addWidget(self.r2_ifRightOpen, 5, 1, 1, 1)
        self.r2_line = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.r2_line.setObjectName("r2_line")
        self.gridLayout_3.addWidget(self.r2_line, 1, 2, 1, 1)
        self.r2_rightIsolator = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.r2_rightIsolator.setObjectName("r2_rightIsolator")
        self.gridLayout_3.addWidget(self.r2_rightIsolator, 5, 2, 1, 1)
        self.r2_leftIsolator = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.r2_leftIsolator.setText("")
        self.r2_leftIsolator.setObjectName("r2_leftIsolator")
        self.gridLayout_3.addWidget(self.r2_leftIsolator, 4, 2, 1, 1)
        self.r2_station = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.r2_station.setObjectName("r2_station")
        self.gridLayout_3.addWidget(self.r2_station, 0, 2, 1, 1)
        self.r2_ifLeftOpen = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.r2_ifLeftOpen.setChecked(True)
        self.r2_ifLeftOpen.setObjectName("r2_ifLeftOpen")
        self.gridLayout_3.addWidget(self.r2_ifLeftOpen, 4, 1, 1, 1)
        self.r2_ifRemote = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.r2_ifRemote.setObjectName("r2_ifRemote")
        self.gridLayout_3.addWidget(self.r2_ifRemote, 3, 1, 1, 1)
        self.r2_ifSwitch = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.r2_ifSwitch.setChecked(True)
        self.r2_ifSwitch.setObjectName("r2_ifSwitch")
        self.gridLayout_3.addWidget(self.r2_ifSwitch, 3, 0, 1, 1)
        self.r2_if = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.r2_if.setChecked(True)
        self.r2_if.setObjectName("r2_if")
        self.gridLayout_3.addWidget(self.r2_if, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.r2_side = QtWidgets.QLineEdit(Form)
        self.r2_side.setGeometry(QtCore.QRect(490, 370, 51, 21))
        self.r2_side.setObjectName("r2_side")
        self.l2_side = QtWidgets.QLineEdit(Form)
        self.l2_side.setGeometry(QtCore.QRect(370, 370, 51, 21))
        self.l2_side.setObjectName("l2_side")
        self.l2_switch_type = QtWidgets.QComboBox(Form)
        self.l2_switch_type.setGeometry(QtCore.QRect(110, 340, 71, 21))
        self.l2_switch_type.setObjectName("l2_switch_type")
        self.l2_switch_type.addItem("")
        self.l2_switch_type.addItem("")
        self.l2_switch_type.addItem("")
        self.l22Label = QtWidgets.QLabel(Form)
        self.l22Label.setGeometry(QtCore.QRect(270, 380, 51, 31))
        self.l22Label.setStyleSheet("image: url(:/newPrefix/image/kaiguan_he.jpg);")
        self.l22Label.setText("")
        self.l22Label.setObjectName("l22Label")
        self.l23Label = QtWidgets.QLabel(Form)
        self.l23Label.setGeometry(QtCore.QRect(310, 380, 51, 31))
        self.l23Label.setStyleSheet("image: url(:/newPrefix/image/daoza_he.jpg);")
        self.l23Label.setText("")
        self.l23Label.setObjectName("l23Label")
        self.l21Label = QtWidgets.QLabel(Form)
        self.l21Label.setGeometry(QtCore.QRect(230, 380, 51, 31))
        self.l21Label.setStyleSheet("image: url(:/newPrefix/image/daoza_he.jpg);")
        self.l21Label.setText("")
        self.l21Label.setObjectName("l21Label")
        self.l13Label = QtWidgets.QLabel(Form)
        self.l13Label.setGeometry(QtCore.QRect(310, 240, 51, 31))
        self.l13Label.setStyleSheet("image: url(:/newPrefix/image/daoza_he.jpg);")
        self.l13Label.setText("")
        self.l13Label.setObjectName("l13Label")
        self.l12Label = QtWidgets.QLabel(Form)
        self.l12Label.setGeometry(QtCore.QRect(270, 240, 51, 31))
        self.l12Label.setStyleSheet("image: url(:/newPrefix/image/kaiguan_he.jpg);")
        self.l12Label.setText("")
        self.l12Label.setObjectName("l12Label")
        self.l11Label = QtWidgets.QLabel(Form)
        self.l11Label.setGeometry(QtCore.QRect(230, 240, 51, 31))
        self.l11Label.setStyleSheet("image: url(:/newPrefix/image/daoza_he.jpg);")
        self.l11Label.setText("")
        self.l11Label.setObjectName("l11Label")
        self.r12Label = QtWidgets.QLabel(Form)
        self.r12Label.setGeometry(QtCore.QRect(590, 290, 51, 31))
        self.r12Label.setStyleSheet("image: url(:/newPrefix/image/kaiguan_he.jpg);")
        self.r12Label.setText("")
        self.r12Label.setObjectName("r12Label")
        self.r11Label = QtWidgets.QLabel(Form)
        self.r11Label.setGeometry(QtCore.QRect(550, 290, 51, 31))
        self.r11Label.setStyleSheet("image: url(:/newPrefix/image/daoza_he.jpg);")
        self.r11Label.setText("")
        self.r11Label.setObjectName("r11Label")
        self.r13Label = QtWidgets.QLabel(Form)
        self.r13Label.setGeometry(QtCore.QRect(630, 290, 51, 31))
        self.r13Label.setStyleSheet("image: url(:/newPrefix/image/daoza_he.jpg);")
        self.r13Label.setText("")
        self.r13Label.setObjectName("r13Label")
        self.r23Label = QtWidgets.QLabel(Form)
        self.r23Label.setGeometry(QtCore.QRect(630, 380, 51, 31))
        self.r23Label.setStyleSheet("image: url(:/newPrefix/image/daoza_he.jpg);")
        self.r23Label.setText("")
        self.r23Label.setObjectName("r23Label")
        self.r22Label = QtWidgets.QLabel(Form)
        self.r22Label.setGeometry(QtCore.QRect(590, 380, 51, 31))
        self.r22Label.setStyleSheet("image: url(:/newPrefix/image/kaiguan_he.jpg);")
        self.r22Label.setText("")
        self.r22Label.setObjectName("r22Label")
        self.r21Label = QtWidgets.QLabel(Form)
        self.r21Label.setGeometry(QtCore.QRect(550, 380, 51, 31))
        self.r21Label.setStyleSheet("image: url(:/newPrefix/image/daoza_he.jpg);")
        self.r21Label.setText("")
        self.r21Label.setObjectName("r21Label")
        self.l2_switch = QtWidgets.QLineEdit(Form)
        self.l2_switch.setGeometry(QtCore.QRect(280, 360, 31, 20))
        self.l2_switch.setObjectName("l2_switch")
        self.l2_leftIsolator = QtWidgets.QLineEdit(Form)
        self.l2_leftIsolator.setGeometry(QtCore.QRect(230, 360, 41, 20))
        self.l2_leftIsolator.setObjectName("l2_leftIsolator")
        self.l2_rightIsolator = QtWidgets.QLineEdit(Form)
        self.l2_rightIsolator.setGeometry(QtCore.QRect(320, 360, 41, 20))
        self.l2_rightIsolator.setFrame(True)
        self.l2_rightIsolator.setObjectName("l2_rightIsolator")
        self.l2_station = QtWidgets.QLineEdit(Form)
        self.l2_station.setGeometry(QtCore.QRect(90, 410, 81, 20))
        self.l2_station.setObjectName("l2_station")
        self.l21Label_2 = QtWidgets.QLabel(Form)
        self.l21Label_2.setGeometry(QtCore.QRect(70, 360, 121, 81))
        self.l21Label_2.setStyleSheet("image: url(:/newPrefix/image/station.jpg);")
        self.l21Label_2.setText("")
        self.l21Label_2.setObjectName("l21Label_2")
        self.l2_line = QtWidgets.QLineEdit(Form)
        self.l2_line.setGeometry(QtCore.QRect(90, 370, 91, 20))
        self.l2_line.setObjectName("l2_line")
        self.l23Label_2 = QtWidgets.QLabel(Form)
        self.l23Label_2.setGeometry(QtCore.QRect(350, 380, 41, 31))
        self.l23Label_2.setStyleSheet("image: url(:/newPrefix/image/nothing.jpg);")
        self.l23Label_2.setText("")
        self.l23Label_2.setObjectName("l23Label_2")
        self.l23Label_3 = QtWidgets.QLabel(Form)
        self.l23Label_3.setGeometry(QtCore.QRect(190, 380, 51, 31))
        self.l23Label_3.setStyleSheet("image: url(:/newPrefix/image/nothing.jpg);")
        self.l23Label_3.setText("")
        self.l23Label_3.setObjectName("l23Label_3")
        self.l2_loc = QtWidgets.QLineEdit(Form)
        self.l2_loc.setGeometry(QtCore.QRect(220, 450, 171, 20))
        self.l2_loc.setObjectName("l2_loc")
        self.l2_ifSwitch = QtWidgets.QCheckBox(Form)
        self.l2_ifSwitch.setGeometry(QtCore.QRect(280, 410, 31, 16))
        self.l2_ifSwitch.setChecked(True)
        self.l2_ifSwitch.setObjectName("l2_ifSwitch")
        self.l2_ifLeft = QtWidgets.QCheckBox(Form)
        self.l2_ifLeft.setGeometry(QtCore.QRect(240, 410, 31, 16))
        self.l2_ifLeft.setChecked(True)
        self.l2_ifLeft.setObjectName("l2_ifLeft")
        self.l2_ifRight = QtWidgets.QCheckBox(Form)
        self.l2_ifRight.setGeometry(QtCore.QRect(320, 410, 31, 16))
        self.l2_ifRight.setChecked(True)
        self.l2_ifRight.setObjectName("l2_ifRight")
        self.l23Label_4 = QtWidgets.QLabel(Form)
        self.l23Label_4.setGeometry(QtCore.QRect(390, 240, 161, 191))
        self.l23Label_4.setStyleSheet("image: url(:/newPrefix/image/scope.jpg);")
        self.l23Label_4.setText("")
        self.l23Label_4.setObjectName("l23Label_4")
        self.l23Label_5 = QtWidgets.QLabel(Form)
        self.l23Label_5.setGeometry(QtCore.QRect(510, 380, 41, 31))
        self.l23Label_5.setStyleSheet("image: url(:/newPrefix/image/nothing.jpg);")
        self.l23Label_5.setText("")
        self.l23Label_5.setObjectName("l23Label_5")
        self.l23Label_6 = QtWidgets.QLabel(Form)
        self.l23Label_6.setGeometry(QtCore.QRect(510, 290, 41, 31))
        self.l23Label_6.setStyleSheet("image: url(:/newPrefix/image/nothing.jpg);")
        self.l23Label_6.setText("")
        self.l23Label_6.setObjectName("l23Label_6")
        self.l2_if = QtWidgets.QCheckBox(Form)
        self.l2_if.setGeometry(QtCore.QRect(70, 340, 31, 16))
        self.l2_if.setChecked(True)
        self.l2_if.setObjectName("l2_if")
        self.l2_ifLeftOpen = QtWidgets.QCheckBox(Form)
        self.l2_ifLeftOpen.setGeometry(QtCore.QRect(240, 430, 31, 16))
        self.l2_ifLeftOpen.setObjectName("l2_ifLeftOpen")
        self.l2_ifRightOpen = QtWidgets.QCheckBox(Form)
        self.l2_ifRightOpen.setGeometry(QtCore.QRect(320, 430, 31, 16))
        self.l2_ifRightOpen.setObjectName("l2_ifRightOpen")
        self.l21Label_3 = QtWidgets.QLabel(Form)
        self.l21Label_3.setGeometry(QtCore.QRect(70, 220, 121, 81))
        self.l21Label_3.setStyleSheet("image: url(:/newPrefix/image/station.jpg);")
        self.l21Label_3.setText("")
        self.l21Label_3.setObjectName("l21Label_3")
        self.l23Label_7 = QtWidgets.QLabel(Form)
        self.l23Label_7.setGeometry(QtCore.QRect(190, 240, 51, 31))
        self.l23Label_7.setStyleSheet("image: url(:/newPrefix/image/nothing.jpg);")
        self.l23Label_7.setText("")
        self.l23Label_7.setObjectName("l23Label_7")
        self.l1_ifSwitch = QtWidgets.QCheckBox(Form)
        self.l1_ifSwitch.setGeometry(QtCore.QRect(280, 270, 31, 16))
        self.l1_ifSwitch.setChecked(True)
        self.l1_ifSwitch.setObjectName("l1_ifSwitch")
        self.l1_ifLeft = QtWidgets.QCheckBox(Form)
        self.l1_ifLeft.setGeometry(QtCore.QRect(240, 270, 31, 16))
        self.l1_ifLeft.setChecked(True)
        self.l1_ifLeft.setObjectName("l1_ifLeft")
        self.l1_ifRight = QtWidgets.QCheckBox(Form)
        self.l1_ifRight.setGeometry(QtCore.QRect(320, 270, 31, 16))
        self.l1_ifRight.setChecked(True)
        self.l1_ifRight.setObjectName("l1_ifRight")
        self.l1_ifLeftOpen = QtWidgets.QCheckBox(Form)
        self.l1_ifLeftOpen.setGeometry(QtCore.QRect(240, 290, 31, 16))
        self.l1_ifLeftOpen.setObjectName("l1_ifLeftOpen")
        self.l1_ifRightOpen = QtWidgets.QCheckBox(Form)
        self.l1_ifRightOpen.setGeometry(QtCore.QRect(320, 290, 31, 16))
        self.l1_ifRightOpen.setObjectName("l1_ifRightOpen")
        self.l1_ifRemote = QtWidgets.QCheckBox(Form)
        self.l1_ifRemote.setGeometry(QtCore.QRect(280, 180, 47, 16))
        self.l1_ifRemote.setObjectName("l1_ifRemote")
        self.l1_rightIsolator = QtWidgets.QLineEdit(Form)
        self.l1_rightIsolator.setGeometry(QtCore.QRect(320, 220, 41, 20))
        self.l1_rightIsolator.setObjectName("l1_rightIsolator")
        self.l1_switch = QtWidgets.QLineEdit(Form)
        self.l1_switch.setGeometry(QtCore.QRect(280, 220, 31, 20))
        self.l1_switch.setObjectName("l1_switch")
        self.l1_leftIsolator = QtWidgets.QLineEdit(Form)
        self.l1_leftIsolator.setGeometry(QtCore.QRect(230, 220, 41, 20))
        self.l1_leftIsolator.setObjectName("l1_leftIsolator")
        self.l1_station = QtWidgets.QLineEdit(Form)
        self.l1_station.setGeometry(QtCore.QRect(90, 270, 81, 20))
        self.l1_station.setObjectName("l1_station")
        self.l1_line = QtWidgets.QLineEdit(Form)
        self.l1_line.setGeometry(QtCore.QRect(90, 230, 91, 20))
        self.l1_line.setObjectName("l1_line")
        self.l1_loc = QtWidgets.QLineEdit(Form)
        self.l1_loc.setGeometry(QtCore.QRect(220, 310, 166, 20))
        self.l1_loc.setObjectName("l1_loc")
        self.l1_if = QtWidgets.QCheckBox(Form)
        self.l1_if.setGeometry(QtCore.QRect(70, 190, 31, 16))
        self.l1_if.setChecked(True)
        self.l1_if.setObjectName("l1_if")
        self.l23Label_4.raise_()
        self.l21Label_2.raise_()
        self.l1_switch_type.raise_()
        self.genOffSteps.raise_()
        self.gridLayoutWidget_2.raise_()
        self.l1_side.raise_()
        self.gridLayoutWidget_3.raise_()
        self.l2_switch_type.raise_()
        self.l22Label.raise_()
        self.l23Label.raise_()
        self.l21Label.raise_()
        self.l13Label.raise_()
        self.l12Label.raise_()
        self.l11Label.raise_()
        self.r12Label.raise_()
        self.r11Label.raise_()
        self.r13Label.raise_()
        self.r23Label.raise_()
        self.r22Label.raise_()
        self.r21Label.raise_()
        self.l2_switch.raise_()
        self.l2_leftIsolator.raise_()
        self.l2_rightIsolator.raise_()
        self.l2_station.raise_()
        self.l2_line.raise_()
        self.l23Label_2.raise_()
        self.l23Label_3.raise_()
        self.l2_loc.raise_()
        self.l2_ifSwitch.raise_()
        self.l2_ifLeft.raise_()
        self.l2_ifRight.raise_()
        self.l2_side.raise_()
        self.l23Label_5.raise_()
        self.r2_side.raise_()
        self.l23Label_6.raise_()
        self.r1_side.raise_()
        self.l2_if.raise_()
        self.l2_ifLeftOpen.raise_()
        self.l2_ifRightOpen.raise_()
        self.l21Label_3.raise_()
        self.l23Label_7.raise_()
        self.l1_ifSwitch.raise_()
        self.l1_ifLeft.raise_()
        self.l1_ifRight.raise_()
        self.l1_ifLeftOpen.raise_()
        self.l1_ifRightOpen.raise_()
        self.l1_ifRemote.raise_()
        self.l1_rightIsolator.raise_()
        self.l1_switch.raise_()
        self.l1_leftIsolator.raise_()
        self.l1_station.raise_()
        self.l1_line.raise_()
        self.l1_loc.raise_()
        self.l1_if.raise_()

        self.retranslateUi(Form)
        self.l1_ifLeft.toggled['bool'].connect(self.l1_leftIsolator.setEnabled)
        self.r1_ifLeft.toggled['bool'].connect(self.r1_leftIsolator.setEnabled)
        self.r1_ifRight.toggled['bool'].connect(self.r1_rightIsolator.setEnabled)
        self.l1_ifRight.toggled['bool'].connect(self.l1_rightIsolator.setEnabled)
        self.l1_ifSwitch.toggled['bool'].connect(self.l1_switch.setEnabled)
        self.l1_ifSwitch.toggled['bool'].connect(self.l1_ifRemote.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.l1_switch_type, self.r1_loc)
        Form.setTabOrder(self.r1_loc, self.r1_ifLeft)
        Form.setTabOrder(self.r1_ifLeft, self.r1_switch)
        Form.setTabOrder(self.r1_switch, self.r1_ifRight)
        Form.setTabOrder(self.r1_ifRight, self.r1_rightIsolator)
        Form.setTabOrder(self.r1_rightIsolator, self.r1_ifRemote)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.l1_switch_type.setItemText(0, _translate("Form", "配电设备"))
        self.l1_switch_type.setItemText(1, _translate("Form", "变电设备"))
        self.l1_switch_type.setItemText(2, _translate("Form", "带电解口"))
        self.genOffSteps.setText(_translate("Form", "生成停电步骤单"))
        self.r1_switch.setText(_translate("Form", "61T2"))
        self.r1_loc.setText(_translate("Form", "#61塔"))
        self.r1_line.setText(_translate("Form", "10kV702中安线"))
        self.r1_rightIsolator.setText(_translate("Form", "61T22"))
        self.r1_ifRightOpen.setText(_translate("Form", "常开"))
        self.r1_ifRight.setText(_translate("Form", "有右刀"))
        self.r1_station.setText(_translate("Form", "110kV箩行站"))
        self.r1_if.setText(_translate("Form", "有"))
        self.label_10.setText(_translate("Form", "线路"))
        self.label_4.setText(_translate("Form", "位置"))
        self.label_7.setText(_translate("Form", "变电站"))
        self.r1_ifLeftOpen.setText(_translate("Form", "常开"))
        self.r1_ifLeft.setText(_translate("Form", "有左刀"))
        self.r1_ifSwitch.setText(_translate("Form", "有开关"))
        self.r1_ifRemote.setText(_translate("Form", "遥控"))
        self.l1_side.setText(_translate("Form", "线路侧"))
        self.r1_side.setText(_translate("Form", "线路侧"))
        self.r2_loc.setText(_translate("Form", "#61塔"))
        self.r2_switch.setText(_translate("Form", "61T1"))
        self.r2_ifRight.setText(_translate("Form", "有右刀"))
        self.r2_ifLeft.setText(_translate("Form", "有左刀"))
        self.r2_ifRightOpen.setText(_translate("Form", "常开"))
        self.r2_line.setText(_translate("Form", "10kV716东沥线"))
        self.r2_rightIsolator.setText(_translate("Form", "61T12"))
        self.r2_station.setText(_translate("Form", "110kV箩行站"))
        self.r2_ifLeftOpen.setText(_translate("Form", "常开"))
        self.r2_ifRemote.setText(_translate("Form", "遥控"))
        self.r2_ifSwitch.setText(_translate("Form", "有开关"))
        self.r2_if.setText(_translate("Form", "有"))
        self.label_8.setText(_translate("Form", "变电站"))
        self.label_5.setText(_translate("Form", "位置"))
        self.label_12.setText(_translate("Form", "线路"))
        self.r2_side.setText(_translate("Form", "线路侧"))
        self.l2_side.setText(_translate("Form", "线路侧"))
        self.l2_switch_type.setItemText(0, _translate("Form", "配电设备"))
        self.l2_switch_type.setItemText(1, _translate("Form", "变电设备"))
        self.l2_switch_type.setItemText(2, _translate("Form", "带电解口"))
        self.l2_switch.setText(_translate("Form", "26T1"))
        self.l2_leftIsolator.setText(_translate("Form", "26T11"))
        self.l2_rightIsolator.setText(_translate("Form", "26T12"))
        self.l2_station.setText(_translate("Form", "110kV箩行站"))
        self.l2_line.setText(_translate("Form", "10kV716东沥线"))
        self.l2_loc.setText(_translate("Form", "#26塔"))
        self.l2_ifSwitch.setText(_translate("Form", "有开关"))
        self.l2_ifLeft.setText(_translate("Form", "有左刀"))
        self.l2_ifRight.setText(_translate("Form", "有右刀"))
        self.l2_if.setText(_translate("Form", "有"))
        self.l2_ifLeftOpen.setText(_translate("Form", "开"))
        self.l2_ifRightOpen.setText(_translate("Form", "开"))
        self.l1_ifSwitch.setText(_translate("Form", "有开关"))
        self.l1_ifLeft.setText(_translate("Form", "有左刀"))
        self.l1_ifRight.setText(_translate("Form", "有右刀"))
        self.l1_ifLeftOpen.setText(_translate("Form", "开"))
        self.l1_ifRightOpen.setText(_translate("Form", "开"))
        self.l1_ifRemote.setText(_translate("Form", "遥控"))
        self.l1_rightIsolator.setText(_translate("Form", "26T22"))
        self.l1_switch.setText(_translate("Form", "26T2"))
        self.l1_leftIsolator.setText(_translate("Form", "26T21"))
        self.l1_station.setText(_translate("Form", "110kV箩行站"))
        self.l1_line.setText(_translate("Form", "10kV702中安线"))
        self.l1_loc.setText(_translate("Form", "#26塔"))
        self.l1_if.setText(_translate("Form", "有"))
import pictures_rc