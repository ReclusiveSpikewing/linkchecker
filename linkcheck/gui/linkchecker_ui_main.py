# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Thu Dec 16 21:50:10 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 664)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(4, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.urlinput = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlinput.sizePolicy().hasHeightForWidth())
        self.urlinput.setSizePolicy(sizePolicy)
        self.urlinput.setMaxLength(2048)
        self.urlinput.setObjectName("urlinput")
        self.horizontalLayout_3.addWidget(self.urlinput)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.controlButton = QtGui.QPushButton(self.centralwidget)
        self.controlButton.setStatusTip("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.controlButton.setIcon(icon1)
        self.controlButton.setDefault(True)
        self.controlButton.setObjectName("controlButton")
        self.horizontalLayout_3.addWidget(self.controlButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setRootIsDecorated(False)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setItemsExpandable(False)
        self.treeView.setSortingEnabled(False)
        self.treeView.setAllColumnsShowFocus(True)
        self.treeView.setExpandsOnDoubleClick(False)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.url_properties = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.url_properties.sizePolicy().hasHeightForWidth())
        self.url_properties.setSizePolicy(sizePolicy)
        self.url_properties.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.url_properties.setObjectName("url_properties")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.url_properties)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtGui.QFrame(self.url_properties)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.prop_url = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_url.sizePolicy().hasHeightForWidth())
        self.prop_url.setSizePolicy(sizePolicy)
        self.prop_url.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_url.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_url.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_url.setText("")
        self.prop_url.setTextFormat(QtCore.Qt.RichText)
        self.prop_url.setOpenExternalLinks(True)
        self.prop_url.setObjectName("prop_url")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.prop_url)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.prop_name = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_name.sizePolicy().hasHeightForWidth())
        self.prop_name.setSizePolicy(sizePolicy)
        self.prop_name.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_name.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_name.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_name.setText("")
        self.prop_name.setTextFormat(QtCore.Qt.PlainText)
        self.prop_name.setObjectName("prop_name")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.prop_name)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.prop_parenturl = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_parenturl.sizePolicy().hasHeightForWidth())
        self.prop_parenturl.setSizePolicy(sizePolicy)
        self.prop_parenturl.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_parenturl.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_parenturl.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_parenturl.setText("")
        self.prop_parenturl.setTextFormat(QtCore.Qt.RichText)
        self.prop_parenturl.setOpenExternalLinks(True)
        self.prop_parenturl.setObjectName("prop_parenturl")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.prop_parenturl)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.prop_base = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_base.sizePolicy().hasHeightForWidth())
        self.prop_base.setSizePolicy(sizePolicy)
        self.prop_base.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_base.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_base.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_base.setText("")
        self.prop_base.setTextFormat(QtCore.Qt.RichText)
        self.prop_base.setOpenExternalLinks(False)
        self.prop_base.setObjectName("prop_base")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.prop_base)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.prop_checktime = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_checktime.sizePolicy().hasHeightForWidth())
        self.prop_checktime.setSizePolicy(sizePolicy)
        self.prop_checktime.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_checktime.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_checktime.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_checktime.setText("")
        self.prop_checktime.setTextFormat(QtCore.Qt.PlainText)
        self.prop_checktime.setObjectName("prop_checktime")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.prop_checktime)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.prop_dltime = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_dltime.sizePolicy().hasHeightForWidth())
        self.prop_dltime.setSizePolicy(sizePolicy)
        self.prop_dltime.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_dltime.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_dltime.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_dltime.setText("")
        self.prop_dltime.setTextFormat(QtCore.Qt.PlainText)
        self.prop_dltime.setObjectName("prop_dltime")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.prop_dltime)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_9)
        self.prop_size = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_size.sizePolicy().hasHeightForWidth())
        self.prop_size.setSizePolicy(sizePolicy)
        self.prop_size.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_size.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_size.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_size.setText("")
        self.prop_size.setTextFormat(QtCore.Qt.PlainText)
        self.prop_size.setObjectName("prop_size")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.prop_size)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_10)
        self.prop_info = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_info.sizePolicy().hasHeightForWidth())
        self.prop_info.setSizePolicy(sizePolicy)
        self.prop_info.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_info.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_info.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_info.setText("")
        self.prop_info.setTextFormat(QtCore.Qt.PlainText)
        self.prop_info.setWordWrap(True)
        self.prop_info.setObjectName("prop_info")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.prop_info)
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_11)
        self.prop_warning = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_warning.sizePolicy().hasHeightForWidth())
        self.prop_warning.setSizePolicy(sizePolicy)
        self.prop_warning.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_warning.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_warning.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_warning.setText("")
        self.prop_warning.setTextFormat(QtCore.Qt.PlainText)
        self.prop_warning.setScaledContents(True)
        self.prop_warning.setWordWrap(True)
        self.prop_warning.setObjectName("prop_warning")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.prop_warning)
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_12)
        self.prop_result = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop_result.sizePolicy().hasHeightForWidth())
        self.prop_result.setSizePolicy(sizePolicy)
        self.prop_result.setMinimumSize(QtCore.QSize(300, 0))
        self.prop_result.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prop_result.setFrameShadow(QtGui.QFrame.Sunken)
        self.prop_result.setText("")
        self.prop_result.setTextFormat(QtCore.Qt.PlainText)
        self.prop_result.setObjectName("prop_result")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.prop_result)
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.url_properties)
        self.statistics = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statistics.sizePolicy().hasHeightForWidth())
        self.statistics.setSizePolicy(sizePolicy)
        self.statistics.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statistics.setObjectName("statistics")
        self.label_14 = QtGui.QLabel(self.statistics)
        self.label_14.setGeometry(QtCore.QRect(190, 60, 57, 15))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtGui.QLabel(self.statistics)
        self.label_15.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtGui.QLabel(self.statistics)
        self.label_16.setGeometry(QtCore.QRect(20, 230, 101, 16))
        self.label_16.setObjectName("label_16")
        self.label_18 = QtGui.QLabel(self.statistics)
        self.label_18.setGeometry(QtCore.QRect(20, 250, 31, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtGui.QLabel(self.statistics)
        self.label_19.setGeometry(QtCore.QRect(90, 250, 31, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtGui.QLabel(self.statistics)
        self.label_20.setGeometry(QtCore.QRect(170, 250, 57, 15))
        self.label_20.setObjectName("label_20")
        self.stats_domains = QtGui.QLabel(self.statistics)
        self.stats_domains.setGeometry(QtCore.QRect(260, 60, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_domains.sizePolicy().hasHeightForWidth())
        self.stats_domains.setSizePolicy(sizePolicy)
        self.stats_domains.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_domains.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_domains.setText("")
        self.stats_domains.setTextFormat(QtCore.Qt.RichText)
        self.stats_domains.setOpenExternalLinks(True)
        self.stats_domains.setObjectName("stats_domains")
        self.stats_url_avglen = QtGui.QLabel(self.statistics)
        self.stats_url_avglen.setGeometry(QtCore.QRect(230, 250, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_url_avglen.sizePolicy().hasHeightForWidth())
        self.stats_url_avglen.setSizePolicy(sizePolicy)
        self.stats_url_avglen.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_url_avglen.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_url_avglen.setText("")
        self.stats_url_avglen.setTextFormat(QtCore.Qt.RichText)
        self.stats_url_avglen.setOpenExternalLinks(True)
        self.stats_url_avglen.setObjectName("stats_url_avglen")
        self.stats_url_maxlen = QtGui.QLabel(self.statistics)
        self.stats_url_maxlen.setGeometry(QtCore.QRect(120, 250, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_url_maxlen.sizePolicy().hasHeightForWidth())
        self.stats_url_maxlen.setSizePolicy(sizePolicy)
        self.stats_url_maxlen.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_url_maxlen.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_url_maxlen.setText("")
        self.stats_url_maxlen.setTextFormat(QtCore.Qt.RichText)
        self.stats_url_maxlen.setOpenExternalLinks(True)
        self.stats_url_maxlen.setObjectName("stats_url_maxlen")
        self.stats_url_minlen = QtGui.QLabel(self.statistics)
        self.stats_url_minlen.setGeometry(QtCore.QRect(40, 250, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_url_minlen.sizePolicy().hasHeightForWidth())
        self.stats_url_minlen.setSizePolicy(sizePolicy)
        self.stats_url_minlen.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_url_minlen.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_url_minlen.setText("")
        self.stats_url_minlen.setTextFormat(QtCore.Qt.RichText)
        self.stats_url_minlen.setOpenExternalLinks(True)
        self.stats_url_minlen.setObjectName("stats_url_minlen")
        self.label_6 = QtGui.QLabel(self.statistics)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 57, 15))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtGui.QLabel(self.statistics)
        self.label_13.setGeometry(QtCore.QRect(130, 150, 57, 15))
        self.label_13.setObjectName("label_13")
        self.label_17 = QtGui.QLabel(self.statistics)
        self.label_17.setGeometry(QtCore.QRect(20, 170, 57, 15))
        self.label_17.setObjectName("label_17")
        self.label_21 = QtGui.QLabel(self.statistics)
        self.label_21.setGeometry(QtCore.QRect(130, 170, 57, 15))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtGui.QLabel(self.statistics)
        self.label_22.setGeometry(QtCore.QRect(20, 190, 57, 15))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtGui.QLabel(self.statistics)
        self.label_23.setGeometry(QtCore.QRect(130, 190, 57, 15))
        self.label_23.setObjectName("label_23")
        self.stats_content_text = QtGui.QLabel(self.statistics)
        self.stats_content_text.setGeometry(QtCore.QRect(180, 150, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_content_text.sizePolicy().hasHeightForWidth())
        self.stats_content_text.setSizePolicy(sizePolicy)
        self.stats_content_text.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_content_text.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_content_text.setText("")
        self.stats_content_text.setTextFormat(QtCore.Qt.RichText)
        self.stats_content_text.setOpenExternalLinks(True)
        self.stats_content_text.setObjectName("stats_content_text")
        self.stats_content_video = QtGui.QLabel(self.statistics)
        self.stats_content_video.setGeometry(QtCore.QRect(180, 170, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_content_video.sizePolicy().hasHeightForWidth())
        self.stats_content_video.setSizePolicy(sizePolicy)
        self.stats_content_video.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_content_video.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_content_video.setText("")
        self.stats_content_video.setTextFormat(QtCore.Qt.RichText)
        self.stats_content_video.setOpenExternalLinks(True)
        self.stats_content_video.setObjectName("stats_content_video")
        self.stats_content_other = QtGui.QLabel(self.statistics)
        self.stats_content_other.setGeometry(QtCore.QRect(180, 190, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_content_other.sizePolicy().hasHeightForWidth())
        self.stats_content_other.setSizePolicy(sizePolicy)
        self.stats_content_other.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_content_other.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_content_other.setText("")
        self.stats_content_other.setTextFormat(QtCore.Qt.RichText)
        self.stats_content_other.setOpenExternalLinks(True)
        self.stats_content_other.setObjectName("stats_content_other")
        self.stats_content_image = QtGui.QLabel(self.statistics)
        self.stats_content_image.setGeometry(QtCore.QRect(70, 150, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_content_image.sizePolicy().hasHeightForWidth())
        self.stats_content_image.setSizePolicy(sizePolicy)
        self.stats_content_image.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_content_image.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_content_image.setText("")
        self.stats_content_image.setTextFormat(QtCore.Qt.RichText)
        self.stats_content_image.setOpenExternalLinks(True)
        self.stats_content_image.setObjectName("stats_content_image")
        self.stats_content_audio = QtGui.QLabel(self.statistics)
        self.stats_content_audio.setGeometry(QtCore.QRect(70, 170, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_content_audio.sizePolicy().hasHeightForWidth())
        self.stats_content_audio.setSizePolicy(sizePolicy)
        self.stats_content_audio.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_content_audio.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_content_audio.setText("")
        self.stats_content_audio.setTextFormat(QtCore.Qt.RichText)
        self.stats_content_audio.setOpenExternalLinks(True)
        self.stats_content_audio.setObjectName("stats_content_audio")
        self.stats_content_mail = QtGui.QLabel(self.statistics)
        self.stats_content_mail.setGeometry(QtCore.QRect(70, 190, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_content_mail.sizePolicy().hasHeightForWidth())
        self.stats_content_mail.setSizePolicy(sizePolicy)
        self.stats_content_mail.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_content_mail.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_content_mail.setText("")
        self.stats_content_mail.setTextFormat(QtCore.Qt.RichText)
        self.stats_content_mail.setOpenExternalLinks(True)
        self.stats_content_mail.setObjectName("stats_content_mail")
        self.label_24 = QtGui.QLabel(self.statistics)
        self.label_24.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtGui.QLabel(self.statistics)
        self.label_25.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtGui.QLabel(self.statistics)
        self.label_26.setGeometry(QtCore.QRect(190, 30, 61, 16))
        self.label_26.setObjectName("label_26")
        self.stats_valid_urls = QtGui.QLabel(self.statistics)
        self.stats_valid_urls.setGeometry(QtCore.QRect(100, 30, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_valid_urls.sizePolicy().hasHeightForWidth())
        self.stats_valid_urls.setSizePolicy(sizePolicy)
        self.stats_valid_urls.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_valid_urls.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_valid_urls.setText("")
        self.stats_valid_urls.setTextFormat(QtCore.Qt.RichText)
        self.stats_valid_urls.setOpenExternalLinks(True)
        self.stats_valid_urls.setObjectName("stats_valid_urls")
        self.stats_invalid_urls = QtGui.QLabel(self.statistics)
        self.stats_invalid_urls.setGeometry(QtCore.QRect(100, 60, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_invalid_urls.sizePolicy().hasHeightForWidth())
        self.stats_invalid_urls.setSizePolicy(sizePolicy)
        self.stats_invalid_urls.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_invalid_urls.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_invalid_urls.setText("")
        self.stats_invalid_urls.setTextFormat(QtCore.Qt.RichText)
        self.stats_invalid_urls.setOpenExternalLinks(True)
        self.stats_invalid_urls.setObjectName("stats_invalid_urls")
        self.stats_warnings = QtGui.QLabel(self.statistics)
        self.stats_warnings.setGeometry(QtCore.QRect(260, 30, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_warnings.sizePolicy().hasHeightForWidth())
        self.stats_warnings.setSizePolicy(sizePolicy)
        self.stats_warnings.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_warnings.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_warnings.setText("")
        self.stats_warnings.setTextFormat(QtCore.Qt.RichText)
        self.stats_warnings.setOpenExternalLinks(True)
        self.stats_warnings.setObjectName("stats_warnings")
        self.label_27 = QtGui.QLabel(self.statistics)
        self.label_27.setGeometry(QtCore.QRect(230, 150, 71, 16))
        self.label_27.setObjectName("label_27")
        self.stats_content_application = QtGui.QLabel(self.statistics)
        self.stats_content_application.setGeometry(QtCore.QRect(300, 150, 31, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_content_application.sizePolicy().hasHeightForWidth())
        self.stats_content_application.setSizePolicy(sizePolicy)
        self.stats_content_application.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stats_content_application.setFrameShadow(QtGui.QFrame.Sunken)
        self.stats_content_application.setText("")
        self.stats_content_application.setTextFormat(QtCore.Qt.RichText)
        self.stats_content_application.setOpenExternalLinks(True)
        self.stats_content_application.setObjectName("stats_content_application")
        self.horizontalLayout.addWidget(self.statistics)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 21))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuLinkChecka = QtGui.QMenu(self.menubar)
        self.menuLinkChecka.setObjectName("menuLinkChecka")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon3)
        self.actionHelp.setObjectName("actionHelp")
        self.actionViewOnline = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/online.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewOnline.setIcon(icon4)
        self.actionViewOnline.setObjectName("actionViewOnline")
        self.actionOptions = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon5)
        self.actionOptions.setObjectName("actionOptions")
        self.actionCopyToClipboard = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopyToClipboard.setIcon(icon6)
        self.actionCopyToClipboard.setObjectName("actionCopyToClipboard")
        self.actionViewParentOnline = QtGui.QAction(MainWindow)
        self.actionViewParentOnline.setIcon(icon4)
        self.actionViewParentOnline.setObjectName("actionViewParentOnline")
        self.actionViewParentSource = QtGui.QAction(MainWindow)
        self.actionViewParentSource.setIcon(icon4)
        self.actionViewParentSource.setObjectName("actionViewParentSource")
        self.actionDebug = QtGui.QAction(MainWindow)
        self.actionDebug.setObjectName("actionDebug")
        self.actionViewProperties = QtGui.QAction(MainWindow)
        self.actionViewProperties.setObjectName("actionViewProperties")
        self.actionSave = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon7)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon8)
        self.actionQuit.setObjectName("actionQuit")
        self.menuEdit.addAction(self.actionOptions)
        self.menuLinkChecka.addAction(self.actionSave)
        self.menuLinkChecka.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionDebug)
        self.menubar.addAction(self.menuLinkChecka.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label.setBuddy(self.urlinput)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_("LinkChecker"))
        self.label.setText(_("URL"))
        self.controlButton.setToolTip(_("Start checking the given URL."))
        self.controlButton.setText(_("Start"))
        self.url_properties.setTitle(_("URL properties"))
        self.label_2.setText(_("URL"))
        self.label_3.setText(_("Name"))
        self.label_4.setText(_("Parent URL"))
        self.label_5.setText(_("Base"))
        self.label_7.setText(_("Check time"))
        self.label_8.setText(_("D/L time"))
        self.label_9.setText(_("Size"))
        self.label_10.setText(_("Info"))
        self.label_11.setText(_("Warning"))
        self.label_12.setText(_("Result"))
        self.statistics.setTitle(_("Check statistics"))
        self.label_14.setText(_("Domains"))
        self.label_15.setText(_("Content types"))
        self.label_16.setText(_("URL lengths"))
        self.label_18.setText(_("Min"))
        self.label_19.setText(_("Max"))
        self.label_20.setText(_("Average"))
        self.label_6.setText(_("Image"))
        self.label_13.setText(_("Text"))
        self.label_17.setText(_("Audio"))
        self.label_21.setText(_("Video"))
        self.label_22.setText(_("Mail"))
        self.label_23.setText(_("Other"))
        self.label_24.setText(_("Valid URLs"))
        self.label_25.setText(_("Invalid URLs"))
        self.label_26.setText(_("Warnings"))
        self.label_27.setText(_("Application"))
        self.menuEdit.setTitle(_("Edit"))
        self.menuLinkChecka.setTitle(_("File"))
        self.menuHelp.setTitle(_("Help"))
        self.actionAbout.setText(_("About"))
        self.actionHelp.setText(_("Help"))
        self.actionViewOnline.setText(_("View online"))
        self.actionViewOnline.setToolTip(_("View URL online"))
        self.actionOptions.setText(_("Options"))
        self.actionCopyToClipboard.setText(_("Copy to clipboard"))
        self.actionCopyToClipboard.setToolTip(_("Copy URL to clipboard"))
        self.actionCopyToClipboard.setShortcut(_("Ctrl+C"))
        self.actionViewParentOnline.setText(_("View parent online"))
        self.actionViewParentOnline.setToolTip(_("View parent URL online"))
        self.actionViewParentSource.setText(_("View parent source"))
        self.actionViewParentSource.setToolTip(_("View parent URL source"))
        self.actionDebug.setText(_("Show debug"))
        self.actionViewProperties.setText(_("View properties"))
        self.actionViewProperties.setToolTip(_("View URL properties"))
        self.actionSave.setText(_("Save results..."))
        self.actionSave.setShortcut(_("Ctrl+S"))
        self.actionQuit.setText(_("Quit"))
        self.actionQuit.setShortcut(_("Ctrl+Q"))

import linkchecker_rc
