# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'samplestool.ui'
#
# Created: Sun Aug 24 09:13:40 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(689, 555)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.segstatEdit = QtGui.QTextEdit(Dialog)
        self.segstatEdit.setReadOnly(True)
        self.segstatEdit.setObjectName(_fromUtf8("segstatEdit"))
        self.gridLayout.addWidget(self.segstatEdit, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.startIndexEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startIndexEdit.sizePolicy().hasHeightForWidth())
        self.startIndexEdit.setSizePolicy(sizePolicy)
        self.startIndexEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.startIndexEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.startIndexEdit.setObjectName(_fromUtf8("startIndexEdit"))
        self.horizontalLayout_4.addWidget(self.startIndexEdit)
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_4.addWidget(self.label_13)
        self.endIndexEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endIndexEdit.sizePolicy().hasHeightForWidth())
        self.endIndexEdit.setSizePolicy(sizePolicy)
        self.endIndexEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.endIndexEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.endIndexEdit.setObjectName(_fromUtf8("endIndexEdit"))
        self.horizontalLayout_4.addWidget(self.endIndexEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.directoryEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directoryEdit.sizePolicy().hasHeightForWidth())
        self.directoryEdit.setSizePolicy(sizePolicy)
        self.directoryEdit.setObjectName(_fromUtf8("directoryEdit"))
        self.horizontalLayout_2.addWidget(self.directoryEdit)
        self.browseDirButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseDirButton.sizePolicy().hasHeightForWidth())
        self.browseDirButton.setSizePolicy(sizePolicy)
        self.browseDirButton.setMinimumSize(QtCore.QSize(50, 28))
        self.browseDirButton.setAutoDefault(False)
        self.browseDirButton.setObjectName(_fromUtf8("browseDirButton"))
        self.horizontalLayout_2.addWidget(self.browseDirButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.currentEdit = QtGui.QLineEdit(Dialog)
        self.currentEdit.setEnabled(False)
        self.currentEdit.setObjectName(_fromUtf8("currentEdit"))
        self.gridLayout.addWidget(self.currentEdit, 9, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 15, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.transcribeEdit = QtGui.QLineEdit(Dialog)
        self.transcribeEdit.setObjectName(_fromUtf8("transcribeEdit"))
        self.gridLayout.addWidget(self.transcribeEdit, 10, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playButton = QtGui.QPushButton(Dialog)
        self.playButton.setAutoDefault(False)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        self.waveButton = QtGui.QPushButton(Dialog)
        self.waveButton.setAutoDefault(False)
        self.waveButton.setObjectName(_fromUtf8("waveButton"))
        self.horizontalLayout.addWidget(self.waveButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.nextButton = QtGui.QPushButton(Dialog)
        self.nextButton.setAutoDefault(False)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.gridLayout.addLayout(self.horizontalLayout, 14, 1, 1, 1)
        self.imageLabel = QtGui.QLabel(Dialog)
        self.imageLabel.setText(_fromUtf8(""))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.gridLayout.addWidget(self.imageLabel, 11, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 11, 0, 1, 1)
        self.sizeMinEdit = QtGui.QLineEdit(Dialog)
        self.sizeMinEdit.setObjectName(_fromUtf8("sizeMinEdit"))
        self.gridLayout.addWidget(self.sizeMinEdit, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.analyzeCheckBox = QtGui.QCheckBox(Dialog)
        self.analyzeCheckBox.setObjectName(_fromUtf8("analyzeCheckBox"))
        self.gridLayout.addWidget(self.analyzeCheckBox, 1, 0, 1, 2)
        self.autoplayCheckBox = QtGui.QCheckBox(Dialog)
        self.autoplayCheckBox.setObjectName(_fromUtf8("autoplayCheckBox"))
        self.gridLayout.addWidget(self.autoplayCheckBox, 12, 0, 1, 2)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)
        self.numberSpinBox = QtGui.QSpinBox(Dialog)
        self.numberSpinBox.setObjectName(_fromUtf8("numberSpinBox"))
        self.gridLayout.addWidget(self.numberSpinBox, 13, 1, 1, 1)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 14, 0, 1, 1)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.silenceEdit = QtGui.QLineEdit(Dialog)
        self.silenceEdit.setObjectName(_fromUtf8("silenceEdit"))
        self.gridLayout.addWidget(self.silenceEdit, 5, 1, 1, 1)
        self.tresholdEdit = QtGui.QLineEdit(Dialog)
        self.tresholdEdit.setObjectName(_fromUtf8("tresholdEdit"))
        self.gridLayout.addWidget(self.tresholdEdit, 7, 1, 1, 1)
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)
        self.sizeEdit = QtGui.QLineEdit(Dialog)
        self.sizeEdit.setText(_fromUtf8(""))
        self.sizeEdit.setObjectName(_fromUtf8("sizeEdit"))
        self.gridLayout.addWidget(self.sizeEdit, 6, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.generateButton = QtGui.QPushButton(Dialog)
        self.generateButton.setAutoDefault(False)
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.horizontalLayout_3.addWidget(self.generateButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.closeButton = QtGui.QPushButton(Dialog)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label.setBuddy(self.directoryEdit)
        self.label_4.setBuddy(self.transcribeEdit)
        self.label_6.setBuddy(self.tresholdEdit)
        self.label_10.setBuddy(self.silenceEdit)
        self.label_14.setBuddy(self.sizeEdit)
        self.label_5.setBuddy(self.sizeMinEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Describe samples", None))
        self.label_11.setText(_translate("Dialog", "Use this subset of segments", None))
        self.label_12.setText(_translate("Dialog", "from index", None))
        self.label_13.setText(_translate("Dialog", "to index", None))
        self.label.setText(_translate("Dialog", "&Directory with samples", None))
        self.browseDirButton.setText(_translate("Dialog", "...", None))
        self.label_3.setText(_translate("Dialog", "Current file", None))
        self.label_4.setText(_translate("Dialog", "&Transcibe letters", None))
        self.playButton.setText(_translate("Dialog", "&Play", None))
        self.waveButton.setText(_translate("Dialog", "Show Energy &Envelope", None))
        self.nextButton.setText(_translate("Dialog", "&Next", None))
        self.label_2.setText(_translate("Dialog", "CAPTCHA image", None))
        self.sizeMinEdit.setText(_translate("Dialog", "0.35", None))
        self.label_6.setText(_translate("Dialog", "Treshold for &segmentation", None))
        self.label_7.setText(_translate("Dialog", "Segmentation stats", None))
        self.analyzeCheckBox.setText(_translate("Dialog", "Analyze segmentation initially (could take a while)", None))
        self.autoplayCheckBox.setText(_translate("Dialog", "Play sound when move to next item", None))
        self.label_8.setText(_translate("Dialog", "Sample number", None))
        self.label_9.setText(_translate("Dialog", "Current Sample:", None))
        self.label_10.setText(_translate("Dialog", "Sil&ence min length(s)", None))
        self.silenceEdit.setText(_translate("Dialog", "0.03", None))
        self.tresholdEdit.setText(_translate("Dialog", "470", None))
        self.label_14.setText(_translate("Dialog", "Number of freq. bins", None))
        self.label_5.setText(_translate("Dialog", "Segment min &length (s)", None))
        self.generateButton.setText(_translate("Dialog", "Generate Training Data", None))
        self.closeButton.setText(_translate("Dialog", "Close", None))

