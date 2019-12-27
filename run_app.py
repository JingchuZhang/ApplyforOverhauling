import sys
from app import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


class Form_Plus(Ui_Form):
    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)
        self.genOffSteps.clicked.connect(self.generateOff)
        self.getStatusByte()
        self.dispImages()
        self.makeConnections()

    def makeConnections(self):
        for side in ['l1', 'l2', 'r1', 'r2']:
            for ele in ['Switch', 'Left', 'Right', 'LeftOpen', 'RightOpen']:
                self.__dict__['{}_if{}'.format(side, ele)].stateChanged.connect(self.reLoad)

    def reLoad(self):
        self.getStatusByte()
        self.dispImages()

    def dispImage(self, side):
        status = self.__dict__[side + 'Status']
        for i in [0, 2]:
            if status[i] == '1':
                url = './image/daoza_he.jpg'
            if status[i] == '0':
                url = './image/daoza_kai.jpg'
            if status[i] == '2':
                url = './image/nothing.jpg'
            self.__dict__['{}{}Label'.format(side, i+1)].setPixmap(QPixmap(url))
        if status[1] == '1':
            url = './image/kaiguan_he.jpg'
        if status[1] == '0':
            url = './image/kaiguan_kai.jpg'
        if status[1] == '2':
            url = './image/nothing.jpg'
        self.__dict__['{}2Label'.format(side)].setPixmap(QPixmap(url))

    def dispImages(self):
        for side in ['l1', 'l2', 'r1', 'r2']:
            self.dispImage(side)

    def generateOff(self):
        self.getStatusByte()
        if self.l1Status == '222' or self.l2Status == '222' or self.r1Status == '222' or self.r2Status == '222':
            print('混合作业！不适用本软件')
        else:
            self.genOff_com()

    def getStatusBit(self, cb1, cb2):
        if not cb1.isChecked():
            bit = '2'
        elif cb2.isChecked():
            bit = '0'
        else:
            bit = '1'
        return bit

    def getStatusByte(self):
        self.l1Status = self.getStatusBit(self.l1_ifLeft, self.l1_ifLeftOpen) + \
                        ('1' if self.l1_ifSwitch.isChecked() else '2') + \
                        self.getStatusBit(self.l1_ifRight, self.l1_ifRightOpen)

        self.l2Status = self.getStatusBit(self.l2_ifLeft, self.l2_ifLeftOpen) + \
                        ('1' if self.l2_ifSwitch.isChecked() else '2') + \
                        self.getStatusBit(self.l2_ifRight, self.l2_ifRightOpen)

        self.r1Status = self.getStatusBit(self.r1_ifLeft, self.r1_ifLeftOpen) + '0' + \
                        self.getStatusBit(self.r2_ifRight, self.r1_ifRightOpen)

        self.r2Status = (self.getStatusBit(self.r2_ifLeft, self.r2_ifLeftOpen) + '0' +
                        self.getStatusBit(self.r2_ifRight, self.r2_ifRightOpen))

    def genOff_com(self):
        # 来电侧转备用
        if self.r1_if.isChecked():
            if self.r1_ifSwitch.isChecked():
                print('确认{}{}{}{}开关在分闸位置'.format(self.r1_station.text(), self.r1_line.text(), self.r1_loc.text(),
                                                 self.r1_switch.text()))
            if self.r1Status[0] == '0':
                print('确认{}{}{}{}刀闸在拉开位置'.format(self.r1_station.text(), self.r1_line.text(), self.r1_loc.text(),
                                                 self.r1_leftIsolator.text()))
            if self.r1Status[0] == '1':
                print('拉开{}{}{}{}刀闸'.format(self.r1_station.text(), self.r1_line.text(), self.r1_loc.text(),
                                            self.r1_leftIsolator.text()))
            if self.r1Status[2] == '0':
                print('确认{}{}{}{}刀闸在拉开位置'.format(self.r1_station.text(), self.r1_line.text(), self.r1_loc.text(),
                                                 self.r1_rightIsolator.text()))
            if self.r1Status[2] == '1':
                print('拉开{}{}{}{}刀闸'.format(self.r1_station.text(), self.r1_line.text(), self.r1_loc.text(),
                                            self.r1_rightIsolator.text()))
        # 来电侧转冷备用
        if self.r2_if.isChecked():
            if self.r2_ifSwitch.isChecked():
                print('确认{}{}{}{}开关在分闸位置'.format(self.r2_station.text(), self.r2_line.text(), self.r2_loc.text(),
                                                 self.r2_switch.text()))
            if self.r2Status[0] == '0':
                print('确认{}{}{}{}刀闸在拉开位置'.format(self.r2_station.text(), self.r2_line.text(), self.r2_loc.text(),
                                                 self.r2_leftIsolator.text()))
            if self.r2Status[0] == '1':
                print('拉开{}{}{}{}刀闸'.format(self.r2_station.text(), self.r2_line.text(), self.r2_loc.text(),
                                            self.r2_leftIsolator.text()))
            if self.r2Status[2] == '0':
                print('确认{}{}{}{}刀闸在拉开位置'.format(self.r2_station.text(), self.r2_line.text(), self.r2_loc.text(),
                                                 self.r2_rightIsolator.text()))
            if self.r2Status[2] == '1':
                print('拉开{}{}{}{}刀闸'.format(self.r2_station.text(), self.r2_line.text(), self.r2_loc.text(),
                                            self.r2_rightIsolator.text()))
        # 电源侧转备用 2019年12月28日00:45:37
        if self.l1_if.isChecked():
            if self.l1_switch_type.currentText() == '配电设备':
                if self.l1_ifSwitch.isChecked():
                    print('断开{}{}{}{}开关'.format(self.l1_station.text(), self.l1_line.text(), self.l1_loc.text(),
                                                self.l1_switch.text()))
                if self.l1Status[0] == '1':
                    print('拉开{}{}{}{}刀闸'.format(self.l1_station.text(), self.l1_line.text(), self.l1_loc.text(),
                                                self.l1_leftIsolator.text()))
                if self.l1Status[2] == '1':
                    print('拉开{}{}{}{}刀闸'.format(self.l1_station.text(), self.l1_line.text(), self.l1_loc.text(),
                                                self.l1_rightIsolator.text()))
            else:
                print('将{}{}线路由运行转冷备用'.format(self.l1_station.text(), self.l1_line.text()))

        # 电源侧转备用
        if self.l2_if.isChecked():
            if self.l2_switch_type.currentText() == '配电设备':
                if self.l2_ifSwitch.isChecked():
                    print('断开{}{}{}{}开关'.format(self.l2_station.text(), self.l2_line.text(), self.l2_loc.text(),
                                                    self.l2_switch.text()))
                if self.l2Status[0] == '1':
                    print('拉开{}{}{}{}刀闸'.format(self.l2_station.text(), self.l2_line.text(), self.l2_loc.text(),
                                                    self.l2_leftIsolator.text()))
                if self.l2Status[2] == '1':
                        print('拉开{}{}{}{}刀闸'.format(self.l2_station.text(), self.l2_line.text(), self.l2_loc.text(),
                                                    self.l2_rightIsolator.text()))
                else:
                    print('将{}{}线路由运行转冷备用'.format(self.l2_station.text(), self.l2_line.text()))

        # 电源侧转检修
        if self.l1_if.isChecked():
            if self.l1_switch_type.currentText() == '配电设备':
                if self.l1Status[2] != '2':
                    print('将{}{}{}{}刀闸{}由冷备用转检修'.format(
                        self.l1_station.text(), self.l1_line.text(), self.l1_loc.text(),
                        self.l1_rightIsolator.text(), self.l1_side.text()))
                elif self.l1Status[1] != '2':
                    print(('将{}{}{}{}开关{}由'+('热' if self.l1Status == '212' else '冷')+'备用转检修').format(
                        self.l1_station.text(), self.l1_line.text(), self.l1_loc.text(), self.l1_switch.text(),
                        self.l1_side.text()))
                elif self.l1Status[0] != '2':
                    print('将{}{}{}{}刀闸{}由冷备用转检修'.format(
                        self.l1_station.text(), self.l1_line.text(), self.l1_loc.text(),
                        self.l1_leftIsolator.text(), self.l1_side.text()))
            else:
                print('将{}{}{}{}开关{}由冷备用转检修'.format(self.l1_station.text(), self.l1_line.text(),
                     self.l1_loc.text(), self.l1_switch.text(), self.l1_side.text()))

        # 电源侧转检修
        if self.l2_if.isChecked():
            if self.l2_switch_type.currentText() == '配电设备':
                if self.l2Status[2] != '2':
                    print('将{}{}{}{}刀闸{}由冷备用转检修'.format(
                        self.l2_station.text(), self.l2_line.text(), self.l2_loc.text(),
                        self.l2_rightIsolator.text(), self.l2_side.text()))
                elif self.l2Status[1] != '2':
                    print(('将{}{}{}{}开关{}由'+('热' if self.l2Status == '212' else '冷')+'备用转检修').format(
                        self.l2_station.text(), self.l2_line.text(), self.l2_loc.text(), self.l2_switch.text(),
                        self.l2_side.text()))
                elif self.l2Status[0] != '2':
                    print('将{}{}{}{}刀闸{}由冷备用转检修'.format(
                        self.l2_station.text(), self.l2_line.text(), self.l2_loc.text(),
                        self.l2_leftIsolator.text(), self.l2_side.text()))
            else:
                print('将{}{}{}{}开关{}由冷备用转检修'.format(
                    self.l2_station.text(), self.l2_line.text(),
                    self.l2_loc.text(), self.l2_switch.text(), self.l2_side.text()))
        # 来电侧转检修
        if self.r1_if.isChecked():
            if self.r1Status[0] != '2':
                print('将{}{}{}{}刀闸{}由冷备用转检修'.format(
                        self.r1_station.text(), self.r1_line.text(), self.r1_loc.text(),
                        self.r1_rightIsolator.text(), self.r1_side.text()))
            elif self.r1Status[1] != '2':
                print(('将{}{}{}{}开关{}由' + ('热' if self.r1Status == '212' else '冷') + '备用转检修').format(
                    self.r1_station.text(), self.r1_line.text(), self.r1_loc.text(), self.r1_switch.text(),
                    self.r1_side.text()))
            elif self.r1Status[2] != '2':
                print('将{}{}{}{}刀闸{}由冷备用转检修'.format(
                    self.r1_station.text(), self.r1_line.text(), self.r1_loc.text(),
                    self.r1_leftIsolator.text(), self.r1_side.text()))

        # 来电侧转检修
        if self.r2_if.isChecked():
            if self.r2Status[0] != '2':
                print('将{}{}{}{}刀闸{}由冷备用转检修'.format(
                        self.r2_station.text(), self.r2_line.text(), self.r2_loc.text(),
                        self.r2_rightIsolator.text(), self.r2_side.text()))
            elif self.r2Status[1] != '2':
                print(('将{}{}{}{}开关{}由' + ('热' if self.r2Status == '212' else '冷') + '备用转检修').format(
                    self.r2_station.text(), self.r2_line.text(), self.r2_loc.text(), self.r2_switch.text(),
                    self.r2_side.text()))
            elif self.r2Status[2] != '2':
                print('将{}{}{}{}刀闸{}由冷备用转检修'.format(
                    self.r2_station.text(), self.r2_line.text(), self.r2_loc.text(),
                    self.r2_leftIsolator.text(), self.r2_side.text()))


    def generateOff_SubEquip(self):
        pass

    def generateOff_MixedOper(self):
        pass






if __name__ == '__main__':
    application = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Form_Plus()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(application.exec_())
