from PyQt5 import QtCore, QtGui, QtWidgets
from os import name
import PyQt5
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import math
import time
import csv
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QHBoxLayout, QPushButton, QProgressBar, QWidget
from sort import Ui_sortWindow
from filter import Ui_filterWindow
stop_window = True
pause = False
real_button_name = ""
real_button_city = ""
real_button_services = ""
button_name = ""
button_price = ""
button_city = ""
button_ranking = ""
button_rating = ""
button_review = ""
button_services = ""

class hotel:
    array_list = []

    def __init__(self, name, price, city, rating, reviews, services, ranking):
        self.array_list = [name, price, city,
                           rating, reviews, services, ranking]


class WorkerThread(QThread):
    def run(self):
        value=0
        p_bar=Ui_MainWindow()
        QApplication.processEvents()
        #driver = webdriver.Chrome(executable_path='C:\\Users\\rizwa\\Downloads\\chromedriver_win32\\chromedriver.exe')
        driver = webdriver.Chrome(executable_path='D:\\Driver\\chromedriver.exe')
        driver.get("https://www.tripadvisor.com/Hotels")
        content = driver.page_source
        soup = BeautifulSoup(content)
        categories = []
        categories_2 = []
        categories_3 = []
        array_list = []
        counter = 0
        i = soup.find(
            'div', attrs={'class': 'ppr_rup ppr_priv_popular_hotels'})
        j = i.find('ul', attrs={'class': 'flexCols'})
        for k in j.findAll('li', attrs={'class': 'item'}):
            get_category = k.find('a', attrs={'class': 'ui_link'})
            if (get_category):
                get_href = get_category.get('href').replace("/Hotels-", "")
                get_href_1 = get_href.rsplit("-", 2)[0]
                get_href = get_href.replace(get_href_1, "")
                get_href_2 = get_category.get('href').replace("/Hotels-", "")
                get_href_2 = get_href_2.replace(get_href_1, "")
                get_href_2 = get_href_2.replace("-Hotels.html", "")
                get_href_2 = get_href_2.replace("-", "")
                categories.append(get_href_1)
                categories_2.append(get_href)
                categories_3.append(get_href_2)
        while stop_window != False:
            for j in range(0, len(categories)):
                k = 0
                for i in range(1, 11):
                    p_bar.prog_bar(value)
                    value= value+1.88
                    driver.get("https://www.tripadvisor.com/Hotels-" +
                               str(categories[j]) + "-oa" + str(k) + str(categories_2[j]))
                    k += 30
                    while pause == True:
                        counter += 1
                    city = categories_3[j]
                    content = driver.page_source
                    soup = BeautifulSoup(content)
                    for a in soup.findAll('div', attrs={'class': 'ui_column is-8 main_col allowEllipsis'}):
                        name = a.find(
                            'a', attrs={'class': 'property_title prominent'})
                        price = a.find(
                            'div', attrs={'class': 'price __resizeWatch'})
                        if price == None:
                            price = "PKR 22,000"
                        reviews = a.find('a', attrs={'class': 'review_count'})
                        if reviews == None:
                            reviews = "0"
                        rating = a.find(
                            'a', attrs={'class': 'ui_bubble_rating bubble_50'})
                        if rating == None:
                            rating = a.find(
                                'a', attrs={'class': 'ui_bubble_rating bubble_45'})
                            if rating == None:
                                rating = a.find(
                                    'a', attrs={'class': 'ui_bubble_rating bubble_40'})
                                if rating == None:
                                    rating = a.find(
                                        'a', attrs={'class': 'ui_bubble_rating bubble_35'})
                                    if rating == None:
                                        rating = a.find(
                                            'a', attrs={'class': 'ui_bubble_rating bubble_30'})
                                        if rating == None:
                                            rating = a.find(
                                                'a', attrs={'class': 'ui_bubble_rating bubble_25'})
                                            if rating == None:
                                                rating = a.find(
                                                    'a', attrs={'class': 'ui_bubble_rating bubble_20'})
                                                if rating == None:
                                                    rating = a.find(
                                                        'a', attrs={'class': 'ui_bubble_rating bubble_15'})
                                                    if rating == None:
                                                        rating = a.find(
                                                            'a', attrs={'class': 'ui_bubble_rating bubble_10'})
                        if rating == None:
                            rating = "0"
                        else:
                            rating = rating["alt"]
                            rating = rating.replace(' of 5 bubbles', '')
                        ranking = a.find('div', attrs={'class': 'popindex'})
                        if ranking == None:
                            ranking = "Not available"
                        services = a.find('div', attrs={'class': 'label'})
                        if services == None:
                            services = "Not available"
                        if hasattr(price, 'text'):
                            price = price.text
                        if hasattr(services, 'text'):
                            services = services.text
                        if hasattr(ranking, 'text'):
                            ranking = ranking.text
                        h = hotel(*name, price, city, rating,
                                  reviews.text, services, ranking)
                        array_list.append(h)
                    if stop_window == False:
                        break
                if stop_window == False:
                    break
class Ui_filterWindow(object):
    def setupUi(self, filterWindow,ui_window):
        self.ui_window = ui_window
        ui_window.set_filter_window(self)
        filterWindow.setObjectName("filterWindow")
        filterWindow.resize(260, 241)
        self.centralwidget = QtWidgets.QWidget(filterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 110, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        filterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(filterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
        self.menubar.setObjectName("menubar")
        filterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(filterWindow)
        self.statusbar.setObjectName("statusbar")
        filterWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.real_caller_name)
        self.retranslateUi(filterWindow)
        QtCore.QMetaObject.connectSlotsByName(filterWindow)

    def real_caller_name(self):
        if real_button_name == "pushButton_5":
            self.ui_window.real_name_column(0)
        elif real_button_city == "pushButton_6":
            self.ui_window.real_name_column(2)
        elif real_button_services == "pushButton_7":
            self.ui_window.real_name_column(5)
    def real_call_method(self):
        real_start = self.lineEdit.text()
        real_end = self.lineEdit_2.text()
        real_filter = get_filter() 
        arr_1 = self.ui_window.getClassicData()
        if real_button_name == "pushButtton_5":
            data_array = real_filter.filter_func(arr_1, 0,real_start,real_end)
        elif real_button_city == "pushButtton_6":
            data_array = real_filter.filter_func(arr_1, 2,real_start,real_end)
        elif real_button_services == "pushButtton_7":
            data_array = real_filter.filter_func(arr_1, 5,real_start,real_end)
        
        return data_array
    
    def retranslateUi(self, filterWindow):
        _translate = QtCore.QCoreApplication.translate
        filterWindow.setWindowTitle(_translate("filterWindow", "MainWindow"))
        self.label.setText(_translate("filterWindow", "Show items starting with:"))
        self.label_2.setText(_translate("filterWindow", "Show items ending  with:"))
        self.pushButton.setText(_translate("filterWindow", "Search"))



class Ui_sortWindow(object):
    def setupUi(self, sortWindow, ui_window):
        sortWindow.setObjectName("sortWindow")
        sortWindow.resize(308, 345)
        self.ui_window = ui_window
        ui_window.set_sort_window(self)
        self.centralwidget = QtWidgets.QWidget(sortWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sort_alogrithms = QtWidgets.QComboBox(self.centralwidget)
        self.sort_alogrithms.setGeometry(QtCore.QRect(70, 10, 141, 22))
        self.sort_alogrithms.setObjectName("sort_alogrithms")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.setItemText(0, "Sorting algorithms")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 40, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(90, 70, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 150, 111, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 190, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        sortWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sortWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 21))
        self.menubar.setObjectName("menubar")
        sortWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sortWindow)
        self.statusbar.setObjectName("statusbar")
        sortWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.caller_name)
        self.pushButton_2.clicked.connect(self.caller_name_1)

        self.retranslateUi(sortWindow)
        QtCore.QMetaObject.connectSlotsByName(sortWindow)

    def caller_name(self):
        if button_name == "ssButton":
            self.ui_window.name_column(0)
        elif button_price == "ssButton_2":
            self.ui_window.name_column(1)
        elif button_city == "ssButton_3":
            self.ui_window.name_column(2)
        elif button_rating == "ssButton_4":
            self.ui_window.name_column(3)
        elif button_review == "ssButton_5":
            self.ui_window.name_column(4)
        elif button_services == "ssButton_6":
            self.ui_window.name_column(5)
        elif button_ranking == "ssButton_7":
            self.ui_window.name_column(6)
    def caller_name_1(self):
        if button_name == "ssButton":
            self.ui_window.name_column_1(0)
        elif button_price == "ssButton_2":
            self.ui_window.name_column_1(1)
        elif button_city == "ssButton_3":
            self.ui_window.name_column_1(2)
        elif button_rating == "ssButton_4":
            self.ui_window.name_column_1(3)
        elif button_review == "ssButton_5":
            self.ui_window.name_column_1(4)
        elif button_services == "ssButton_6":
            self.ui_window.name_column_1(5)
        elif button_ranking == "ssButton_7":
            self.ui_window.name_column_1(6)
    def call_method_1(self):
        x_1 = self.comboBox_2.currentText()
        y_1 = self.lineEdit.text()
        search = searching()
        arr_1 = self.ui_window.getClassicData()
        q_1 = len(arr_1) - 1
        if button_name == "ssButton":
            if x_1 == "Linear Search":
                searched_array = search.linear_search(arr_1, 0, y_1)
            elif x_1 == "Binary Search":
                searched_array = search.binary_search(arr_1, 0, y_1,0,q_1)
        elif button_price == "ssButton_2":
            if x_1 == "Linear Search":
                searched_array = search.linear_search(arr_1, 1, y_1)
            elif x_1 == "Binary Search":
                searched_array = search.binary_search(arr_1, 1, y_1,0,q_1)
        elif button_city == "ssButton_3":
            if x_1 == "Linear Search":
                searched_array = search.linear_search(arr_1, 2, y_1)
            elif x_1 == "Binary Search":
                searched_array = search.binary_search(arr_1, 2, y_1,0,q_1)
        elif button_rating == "ssButton_4":
            if x_1 == "Linear Search":
                searched_array = search.linear_search(arr_1, 3, y_1)
            elif x_1 == "Binary Search":
                searched_array = search.binary_search(arr_1, 3, y_1,0,q_1)
        elif button_review == "ssButton_5":
            if x_1 == "Linear Search":
                searched_array = search.linear_search(arr_1, 4, y_1)
            elif x_1 == "Binary Search":
                searched_array = search.binary_search(arr_1, 4, y_1,0,q_1)        
        elif button_services == "ssButton_6":
            if x_1 == "Linear Search":
                searched_array = search.linear_search(arr_1, 5, y_1)
            elif x_1 == "Binary Search":
                searched_array = search.binary_search(arr_1, 5, y_1,0,q_1)
        elif button_ranking == "ssButton_7":
            if x_1 == "Linear Search":
                searched_array = search.linear_search(arr_1, 6, y_1)
            elif x_1 == "Binary Search":
                searched_array = search.binary_search(arr_1, 6, y_1,0,q_1)
        print("==")
        return searched_array
        
    def call_method(self):
        x = self.sort_alogrithms.currentText()
        y = self.comboBox.currentText()
        sort = sorting()
        arr = self.ui_window.getClassicData()
        q = len(arr) - 1
        if button_name == "ssButton":
            if x == "Insertion Sort":
                start = time.time()
                sorted_array = sort.insert_sort(arr, 0, y)
                end = time.time()
            elif x == "Selection Sort":
                start = time.time()
                sorted_array = sort.selection_sort(arr, 0, y)
                end = time.time()
            elif x == "Merge Sort":
                start = time.time()
                sorted_array = sort.merge_sort(arr, 0, y, 0, q)
                end = time.time()
            elif x == "Shell Sort":
                start = time.time()
                sorted_array = sort.shell_sort(arr, 0, y)
                end = time.time()
            elif x == "Bubble Sort":
                start = time.time()
                sorted_array = sort.bubble_sort(arr, 0, y)
                end = time.time()
            elif x == "Heap Sort":
                start = time.time()
                sorted_array = sort.heap_sort(arr, 0, y)
                end = time.time()
            elif x == "Cycle Sort":
                start = time.time()
                sorted_array = sort.cycle_sort(arr, 0, y)
                end = time.time()
            elif x == "Quick Sort":
                start = time.time()
                sorted_array = sort.quick_sort(arr, 0, y, 0, q)
                end = time.time()
        elif button_price == "ssButton_2":
            if x == "Insertion Sort":
                start = time.time()
                sorted_array = sort.insert_sort(arr, 1, y)
                end = time.time()
            elif x == "Cycle Sort":
                start = time.time()
                sorted_array = sort.cycle_sort(arr, 0, y)
                end = time.time()
            elif x == "Quick Sort":
                start = time.time()
                sorted_array = sort.quick_sort(arr, 1, y, 0, q)
                end = time.time()
            elif x == "Selection Sort":
                start = time.time()
                sorted_array = sort.selection_sort(arr, 1, y)
                end = time.time()
            elif x == "Merge Sort":
                start = time.time()
                sorted_array = sort.merge_sort(arr, 1, y, 0, q)
                end = time.time()
            elif x == "Shell Sort":
                start = time.time()
                sorted_array = sort.shell_sort(arr, 1, y)
                end = time.time()
            elif x == "Bubble Sort":
                start = time.time()
                sorted_array = sort.bubble_sort(arr, 1, y)
                end = time.time()
            elif x == "Heap Sort":
                start = time.time()
                sorted_array = sort.heap_sort(arr, 1, y)
                end = time.time()
        elif button_city == "ssButton_3":
            if x == "Insertion Sort":
                start = time.time()
                sorted_array = sort.insert_sort(arr, 2, y)
                end = time.time()
            elif x == "Quick Sort":
                start = time.time()
                sorted_array = sort.quick_sort(arr, 2, y, 0, q)
                end = time.time()
            elif x == "Selection Sort":
                start = time.time()
                sorted_array = sort.selection_sort(arr, 2, y)
                end = time.time()
            elif x == "Merge Sort":
                start = time.time()
                sorted_array = sort.merge_sort(arr, 2, y, 0, q)
                end = time.time()
            elif x == "Shell Sort":
                start = time.time()
                sorted_array = sort.shell_sort(arr, 2, y)
                end = time.time()
            elif x == "Bubble Sort":
                start = time.time()
                sorted_array = sort.bubble_sort(arr, 2, y)
                end = time.time()
            elif x == "Heap Sort":
                start = time.time()
                sorted_array = sort.heap_sort(arr, 2, y)
                end = time.time()
        elif button_rating == "ssButton_4":
            if x == "Insertion Sort":
                start = time.time()
                sorted_array = sort.insert_sort(arr, 3, y)
                end = time.time()
            elif x == "Quick Sort":
                start = time.time()
                sorted_array = sort.quick_sort(arr, 3, y, 0, q)
                end = time.time()
            elif x == "Selection Sort":
                start = time.time()
                sorted_array = sort.selection_sort(arr, 3, y)
                end = time.time()
            elif x == "Merge Sort":
                start = time.time()
                sorted_array = sort.merge_sort(arr, 3, y, 0, q)
                end = time.time()
            elif x == "Shell Sort":
                start = time.time()
                sorted_array = sort.shell_sort(arr, 3, y)
                end = time.time()
            elif x == "Bubble Sort":
                start = time.time()
                sorted_array = sort.bubble_sort(arr, 3, y)
                end = time.time()
            elif x == "Heap Sort":
                start = time.time()
                sorted_array = sort.heap_sort(arr, 3, y)
                end = time.time()
        elif button_review == "ssButton_5":
            if x == "Insertion Sort":
                start = time.time()
                sorted_array = sort.insert_sort(arr, 4, y)
                end = time.time()
            elif x == "Quick Sort":
                start = time.time()
                sorted_array = sort.quick_sort(arr, 4, y, 0, q)
                end = time.time()
            elif x == "Selection Sort":
                start = time.time()
                sorted_array = sort.selection_sort(arr, 4, y)
                end = time.time()
            elif x == "Merge Sort":
                start = time.time()
                sorted_array = sort.merge_sort(arr, 4, y, 0, q)
                end = time.time()
            elif x == "Shell Sort":
                start = time.time()
                sorted_array = sort.shell_sort(arr, 4, y)
                end = time.time()
            elif x == "Bubble Sort":
                start = time.time()
                sorted_array = sort.bubble_sort(arr, 4, y)
                end = time.time()
            elif x == "Heap Sort":
                start = time.time()
                sorted_array = sort.heap_sort(arr, 4, y)
                end = time.time()
        elif button_services == "ssButton_6":
            if x == "Insertion Sort":
                start = time.time()
                sorted_array = sort.insert_sort(arr, 5, y)
                end = time.time()
            elif x == "Quick Sort":
                start = time.time()
                sorted_array = sort.quick_sort(arr, 5, y, 0, q)
                end = time.time()
            elif x == "Selection Sort":
                start = time.time()
                sorted_array = sort.selection_sort(arr, 5, y)
                end = time.time()
            elif x == "Merge Sort":
                start = time.time()
                sorted_array = sort.merge_sort(arr, 5, y, 0, q)
                end = time.time()
            elif x == "Shell Sort":
                start = time.time()
                sorted_array = sort.shell_sort(arr, 5, y)
                end = time.time()
            elif x == "Bubble Sort":
                start = time.time()
                sorted_array = sort.bubble_sort(arr, 5, y)
                end = time.time()
            elif x == "Heap Sort":
                start = time.time()
                sorted_array = sort.heap_sort(arr, 5, y)
                end = time.time()
        elif button_ranking == "ssButton_7":
            if x == "Insertion Sort":
                start = time.time()
                sorted_array = sort.insert_sort(arr, 6, y)
                end = time.time()
            elif x == "Quick Sort":
                start = time.time()
                sorted_array = sort.quick_sort(arr, 6, y, 0, q)
                end = time.time()
            elif x == "Selection Sort":
                start = time.time()
                sorted_array = sort.selection_sort(arr, 6, y)
                end = time.time()
            elif x == "Merge Sort":
                start = time.time()
                sorted_array = sort.merge_sort(arr, 6, y, 0, q)
                end = time.time()
            elif x == "Shell Sort":
                start = time.time()
                sorted_array = sort.shell_sort(arr, 6, y)
                end = time.time()
            elif x == "Bubble Sort":
                start = time.time()
                sorted_array = sort.bubble_sort(arr, 6, y)
                end = time.time()
            elif x == "Heap Sort":
                start = time.time()
                sorted_array = sort.heap_sort(arr, 6, y)
                end = time.time()
        print("==")
        total = end - start
        print(str(total))
        return sorted_array

    def retranslateUi(self, sortWindow):
        _translate = QtCore.QCoreApplication.translate
        sortWindow.setWindowTitle(_translate("sortWindow", "MainWindow"))
        self.sort_alogrithms.setItemText(
            1, _translate("sortWindow", "Insertion Sort"))
        self.sort_alogrithms.setItemText(
            2, _translate("sortWindow", "Merge Sort"))
        self.sort_alogrithms.setItemText(
            3, _translate("sortWindow", "Selection Sort"))
        self.sort_alogrithms.setItemText(
            4, _translate("sortWindow", "Bubble Sort"))
        self.sort_alogrithms.setItemText(
            5, _translate("sortWindow", "Quick Sort"))
        self.sort_alogrithms.setItemText(
            6, _translate("sortWindow", "Counting Sort"))
        self.sort_alogrithms.setItemText(
            7, _translate("sortWindow", "Heap Sort"))
        self.sort_alogrithms.setItemText(
            8, _translate("sortWindow", "Cycle Sort"))
        self.sort_alogrithms.setItemText(
            9, _translate("sortWindow", "Radix Sort"))
        self.sort_alogrithms.setItemText(
            10, _translate("sortWindow", "Shell Sort"))
        self.sort_alogrithms.setItemText(
            11, _translate("sortWindow", "Bucket Sort"))
        self.comboBox.setItemText(0, _translate(
            "sortWindow", "Ascend / Descend"))
        self.comboBox.setItemText(1, _translate("sortWindow", "Ascending"))
        self.comboBox.setItemText(2, _translate("sortWindow", "Descending"))
        self.checkBox.setText(_translate("sortWindow", "Multi sort"))
        self.comboBox_2.setItemText(0, _translate(
            "sortWindow", "Searching algorithms"))
        self.comboBox_2.setItemText(
            1, _translate("sortWindow", "Linear Search"))
        self.comboBox_2.setItemText(
            2, _translate("sortWindow", "Binary Search"))
        self.comboBox_2.setItemText(3, _translate("sortWindow", "Jump Search"))
        self.pushButton.setText(_translate("sortWindow", "Sort"))
        self.pushButton_2.setText(_translate("sortWindow", "Search"))
class get_filter:
    def filter_func(self, arr, col,start,end):
        k=0
        arr2 = []
        real_arr = arr.array_list[col]
        len_start=len(start)
        for i in real_arr:
            i_len=len(i)
            for j in i:
                if k!=len(start):
                    if j==start[k] and start[0]==i[0]: 
                        k+=1
                    else:
                        k=0
                if k==len(start):
                    arr2.append(i)
                    k=0
        return arr2
class searching:
    def linear_search(self, arr, col,find_element):
        get_element = []
        for i in range(0,len(arr)):
            if arr[i].array_list[col] == find_element:
                element = arr[i]
                get_element.append(element)
        return get_element
    
    def binary_search(self, arr, col,find_element,left,right):
        get_element = []
        mid_1 = 0
        if right >= left:
            mid_1 = (right + left) // 2
        if arr[mid_1].array_list[col] == find_element:
            element = arr[mid_1]
            get_element.append(element)
        elif arr[mid_1].array_list[col] > find_element:
            return self.binary_search(arr,col,find_element,left, mid_1 - 1)
        else:
            return self.binary_search(arr,col,find_element,mid_1 + 1,right)
        return get_element
class sorting:
    def insert_sort(self, arr, col, type):
        if type == "Ascending":
            n = len(arr)
            for i in range(1, n):
                key = arr[i].array_list[col]
                keys = arr[i]
                j = i-1
                while j >= 0 and (arr[j].array_list[col]) > key:
                    arr[j+1] = arr[j]
                    j = j-1
                arr[j+1] = keys
        elif type=="Descending":
            n = len(arr)
            for i in range(1, n):
                key = arr[i].array_list[col]
                keys = arr[i]
                j = i-1
                while j >= 0 and key > (arr[j].array_list[col]):
                    arr[j+1] = arr[j]
                    j = j-1
                arr[j+1] = keys
        return arr

    def selection_sort(self, arr, col, type):
        if type == "Ascending":
            n = len(arr)
            for i in range(n-1):
                minValueIndex = i
                for j in range(i + 1, n):
                    if arr[j].array_list[col] < arr[minValueIndex].array_list[col]:
                        minValueIndex = j
                if minValueIndex != i:
                    temp = arr[i]
                    arr[i] = arr[minValueIndex]
                    arr[minValueIndex] = temp
        elif type=="Descending":
            n = len(arr)
            for i in range(n-1):
                minValueIndex = i
                for j in range(i + 1, n):
                    if arr[j].array_list[col] > arr[minValueIndex].array_list[col]:
                        minValueIndex = j
                if minValueIndex != i:
                    temp = arr[i]
                    arr[i] = arr[minValueIndex]
                    arr[minValueIndex] = temp
        return arr

    def merge_sort(self, arr, col, type, p, r):
        q = 0
        if p < r:
            q = p + (r-p) // 2
            self.merge_sort(arr, col, type, p, q)
            self.merge_sort(arr, col, type, q+1, r)
            self.merge(arr, col, type, p, q, r)
        # else:
        #     print(arr[col].array_list)
        #     return arr
        return arr

    def merge(self,arr,col, typee, p, q, r):
        L = []
        R = []
        L1 = []
        R1 = []
        if typee == "Ascending":
            for i in range(p,q+1):
                L.append(arr[i])
                L1.append(arr[i].array_list[col])
            for j in range(q+1,r+1):
                R.append(arr[j])
                R1.append(arr[j].array_list[col])
            m=hotel("zzzzzzzzzzzzzz","999999999","zzzzzzzzzz","99999","999999999","zzzzzzzzz","#99999999")
            L.append(m)
            R.append(m)
            L1.append(m.array_list[col])
            R1.append(m.array_list[col])
            i = 0
            j = 0
            for k in range(p, r+1):
                if L1[i] <= R1[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
        elif typee=="Descending":
            for i in range(p,q+1):
                L.append(arr[i])
                L1.append(arr[i].array_list[col])
            for j in range(q+1,r+1):
                R.append(arr[j])
                R1.append(arr[j].array_list[col])
            m=hotel("aaaaaaaaaaaaa","0","aaaaaaaaa","0","0","aaaaaaaaaa","#0")
            L.append(m)
            R.append(m)
            L1.append(m.array_list[col])
            R1.append(m.array_list[col])
            i = 0
            j = 0
            for k in range(p, r+1):
                if L1[i] >= R1[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1

    def quick_sort(self, arr, col, type,p,r):
        if p < r:
            pi = self.partition(arr, col, type,p,r)
            self.quick_sort(arr, col, type,p,pi-1)
            self.quick_sort(arr, col, type,pi+1,r)
        return arr
    def partition(self, arr, col, type,p,r):
        pivot = arr[r]
        pivot_1 = arr[r].array_list[col]
        i = p - 1
        if type== "Ascending":
            for j in range(p,r):
                if (arr[j].array_list[col] < pivot_1):  
                    i +=1
                    (arr[i], arr[j]) = (arr[j], arr[i])
            (arr[i+1], arr[r]) = (arr[r], arr[i+1])
        elif type=="Descending":
            for j in range(p,r):
                if (arr[j].array_list[col] > pivot_1):  
                    i +=1
                    (arr[i], arr[j]) = (arr[j], arr[i])
            (arr[i+1], arr[r]) = (arr[r], arr[i+1])
        return (i+1)

    def shell_sort(self, arr, col, type):
        n = len(arr)
        interval = n // 2
        if type == "Ascending":
            while interval > 0:
                for i in range(interval, n):
                    key = arr[i].array_list[col]
                    keys = arr[i]
                    j = i
                    while j >= interval and arr[j - interval].array_list[col] > key:
                        arr[j] = arr[j - interval]
                        j -= interval
                    arr[j] = keys
                interval //= 2
        elif type=="Descending":
            while interval > 0:
                for i in range(interval, n):
                    key = arr[i].array_list[col]
                    keys = arr[i]
                    j = i
                    while j >= interval and arr[j - interval].array_list[col] < key:
                        arr[j] = arr[j - interval]
                        j -= interval
                    arr[j] = keys
                interval //= 2
        return arr
    
    def bubble_sort(self, arr, col, type):
        if type == "Ascending":
            for i in range(len(arr)-1):
                for j in range(len(arr) - 1):
                    if arr[j].array_list[col] > arr[j+1].array_list[col]:
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
        elif type=="Descending":
            for i in range(len(arr)-1):
                for j in range(len(arr) - 1):
                    if arr[j].array_list[col] < arr[j+1].array_list[col]:
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
        return arr
    

    def heap_sort(self, arr, col, type):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, col, type, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, col, type, i, 0)
        return arr

    def heapify(self, arr, col, type, n, i):
        largest = i
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if type == "Ascending":
            if left < n and arr[i].array_list[col] < arr[left].array_list[col]:
                largest = left
            if right < n and arr[largest].array_list[col] < arr[right].array_list[col]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                self.heapify(arr, col, type, n, largest)
        elif type=="Descending":
            if left < n and arr[left].array_list[col] < arr[smallest].array_list[col]:
                smallest = left
            if right < n and arr[right].array_list[col] < arr[smallest].array_list[col]:
                smallest = right
            if smallest != i:
                (arr[i], arr[smallest]) = (arr[smallest], arr[i])
                self.heapify(arr, col, type, n, smallest)

    def cycle_sort(self, arr, col, type):
        cycle = 0
        if type == "Ascending":
            for k in range(0, len(arr) - 1):
                key = arr[k].array_list[col]
                keys = arr[k]
                idx = k
                for i in range(k + 1, len(arr)):
                    if arr[i].array_list[col] < key:
                        idx += 1
                if idx == k:
                    continue
                while key == arr[idx].array_list[col]:
                    idx += 1
                arr[idx], keys = keys, arr[idx]
                cycle += 1
                while idx != k:
                    idx = k
                    for i in range(k + 1, len(arr)):
                        if arr[i].array_list[col] < key:
                            idx += 1
                    while key == arr[idx].array_list[col]:
                        idx += 1
                    arr[idx], keys = keys, arr[idx]
        return arr


class Ui_MainWindow(object):
    def set_sort_window(self, sort_window):
        self.sort_window = sort_window
    def set_filter_window(self, filter_window):
        self.filter_window = filter_window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 741, 401))
        self.tableWidget.setMinimumSize(QtCore.QSize(711, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 0, 131, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QtCore.QRect(790, 340, 191, 23))
        self.progressBar.setProperty("value", 0)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(790, 410, 200, 16))
        
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 140, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 180, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 140, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 180, 61, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.ssButton = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton.setGeometry(QtCore.QRect(65, 36, 21, 21))
        self.ssButton.setObjectName("ssButton")
        self.ssButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_2.setGeometry(QtCore.QRect(175, 36, 21, 21))
        self.ssButton_2.setObjectName("ssButton_2")
        self.ssButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_3.setGeometry(QtCore.QRect(270, 36, 21, 20))
        self.ssButton_3.setObjectName("ssButton_3")
        self.ssButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_4.setGeometry(QtCore.QRect(370, 36, 20, 20))
        self.ssButton_4.setObjectName("ssButton_4")
        self.ssButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_5.setGeometry(QtCore.QRect(470, 36, 21, 21))
        self.ssButton_5.setObjectName("ssButton_5")
        self.ssButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_6.setGeometry(QtCore.QRect(580, 36, 21, 21))
        self.ssButton_6.setObjectName("ssButton_6")
        self.ssButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_7.setGeometry(QtCore.QRect(680, 36, 20, 20))
        self.ssButton_7.setObjectName("ssButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 36, 21, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 36, 21, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 36, 21, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.clicker)
        self.pushButton_3.clicked.connect(self.break_window)
        self.pushButton_2.clicked.connect(self.pause_window)
        self.pushButton_4.clicked.connect(self.resume_window)
        self.pushButton_5.clicked.connect(self.searchWindow_1)
        self.pushButton_6.clicked.connect(self.searchWindow_2)
        self.pushButton_7.clicked.connect(self.searchWindow_3)
        self.ssButton.clicked.connect(self.sortedWindow_1)
        self.ssButton_2.clicked.connect(self.sortedWindow_2)
        self.ssButton_3.clicked.connect(self.sortedWindow_3)
        self.ssButton_4.clicked.connect(self.sortedWindow_4)
        self.ssButton_5.clicked.connect(self.sortedWindow_5)
        self.ssButton_6.clicked.connect(self.sortedWindow_6)
        self.ssButton_7.clicked.connect(self.sortedWindow_7)
        # self.prog_bar(0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        data = self.getdata()
        self.loaddata(data)
    def prog_bar(self,value):
        print("======")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QtCore.QRect(790, 340, 191, 23))
        self.progressBar.setProperty("value", value)
        

    def name_column(self, col):
        row = 0
        arr = self.sort_window.call_method()
        self.tableWidget.setRowCount(len(arr))
        for i in arr:
            data = [{"Name": i.array_list[0], "Price":i.array_list[1], "City":i.array_list[2],
                     "Rating":i.array_list[3], "Reviews":i.array_list[4], "Services":i.array_list[5], "Ranking":i.array_list[6]}]
            for person in data:
                self.tableWidget.setItem(
                    row, 0, QtWidgets.QTableWidgetItem(person["Name"]))
                self.tableWidget.setItem(
                    row, 1, QtWidgets.QTableWidgetItem(person["Price"]))
                self.tableWidget.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(person["City"]))
                self.tableWidget.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(person["Rating"]))
                self.tableWidget.setItem(
                    row, 4, QtWidgets.QTableWidgetItem(person["Reviews"]))
                self.tableWidget.setItem(
                    row, 5, QtWidgets.QTableWidgetItem(person["Services"]))
                self.tableWidget.setItem(
                    row, 6, QtWidgets.QTableWidgetItem(person["Ranking"]))
            row += 1
    def name_column_1(self, col):
        row = 0
        arr_1 = self.sort_window.call_method_1()
        print(arr_1)
        self.tableWidget.setRowCount(len(arr_1))
        for i in arr_1:
            data = [{"Name": i.array_list[0], "Price":i.array_list[1], "City":i.array_list[2],
                     "Rating":i.array_list[3], "Reviews":i.array_list[4], "Services":i.array_list[5], "Ranking":i.array_list[6]}]
            for person in data:
                self.tableWidget.setItem(
                    row, 0, QtWidgets.QTableWidgetItem(person["Name"]))
                self.tableWidget.setItem(
                    row, 1, QtWidgets.QTableWidgetItem(person["Price"]))
                self.tableWidget.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(person["City"]))
                self.tableWidget.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(person["Rating"]))
                self.tableWidget.setItem(
                    row, 4, QtWidgets.QTableWidgetItem(person["Reviews"]))
                self.tableWidget.setItem(
                    row, 5, QtWidgets.QTableWidgetItem(person["Services"]))
                self.tableWidget.setItem(
                    row, 6, QtWidgets.QTableWidgetItem(person["Ranking"]))
            row += 1
    def real_name_column(self, col):
        row = 0
        arr_2 = self.filter_window.real_call_method()
        print(arr_2)
        self.tableWidget.setRowCount(len(arr_2))
        for i in arr_2:
            data = [{"Name": i.array_list[0], "Price":i.array_list[1], "City":i.array_list[2],
                    "Rating":i.array_list[3], "Reviews":i.array_list[4], "Services":i.array_list[5], "Ranking":i.array_list[6]}]
            for person in data:
                self.tableWidget.setItem(
                    row, 0, QtWidgets.QTableWidgetItem(person["Name"]))
                self.tableWidget.setItem(
                    row, 1, QtWidgets.QTableWidgetItem(person["Price"]))
                self.tableWidget.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(person["City"]))
                self.tableWidget.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(person["Rating"]))
                self.tableWidget.setItem(
                    row, 4, QtWidgets.QTableWidgetItem(person["Reviews"]))
                self.tableWidget.setItem(
                    row, 5, QtWidgets.QTableWidgetItem(person["Services"]))
                self.tableWidget.setItem(
                    row, 6, QtWidgets.QTableWidgetItem(person["Ranking"]))
            row += 1
            
    def clicker(self):
        global stop_window
        stop_window = True
        self.worker = WorkerThread()
        self.worker.start()

    def break_window(self):
        global stop_window
        stop_window = False

    def pause_window(self):
        global pause
        pause = True

    def resume_window(self):
        global pause
        pause = False

    def sortedWindow_1(self):
        self.sortWindow = QtWidgets.QMainWindow()
        global button_name
        button_name = self.ssButton.objectName()
        print(button_name)
        self.ui = Ui_sortWindow()
        self.ui.setupUi(self.sortWindow, self)
        self.sortWindow.show()

    def sortedWindow_2(self):
        self.sortWindow = QtWidgets.QMainWindow()
        global button_price
        button_price = self.ssButton_2.objectName()
        print(button_price)
        self.ui = Ui_sortWindow()
        self.ui.setupUi(self.sortWindow, self)
        self.sortWindow.show()

    def sortedWindow_3(self):
        self.sortWindow = QtWidgets.QMainWindow()
        global button_city
        button_city = self.ssButton_3.objectName()
        print(button_city)
        self.ui = Ui_sortWindow()
        self.ui.setupUi(self.sortWindow, self)
        self.sortWindow.show()

    def sortedWindow_4(self):
        self.sortWindow = QtWidgets.QMainWindow()
        global button_rating
        button_rating = self.ssButton_4.objectName()
        print(button_rating)
        self.ui = Ui_sortWindow()
        self.ui.setupUi(self.sortWindow, self)
        self.sortWindow.show()

    def sortedWindow_5(self):
        self.sortWindow = QtWidgets.QMainWindow()
        global button_review
        button_review = self.ssButton_5.objectName()
        print(button_review)
        self.ui = Ui_sortWindow()
        self.ui.setupUi(self.sortWindow, self)
        self.sortWindow.show()

    def sortedWindow_6(self):
        self.sortWindow = QtWidgets.QMainWindow()
        global button_services
        button_services = self.ssButton_6.objectName()
        print(button_services)
        self.ui = Ui_sortWindow()
        self.ui.setupUi(self.sortWindow, self)
        self.sortWindow.show()

    def sortedWindow_7(self):
        self.sortWindow = QtWidgets.QMainWindow()
        global button_ranking
        button_ranking = self.ssButton_7.objectName()
        print(button_ranking)
        self.ui = Ui_sortWindow()
        self.ui.setupUi(self.sortWindow, self)
        self.sortWindow.show()

    def searchWindow_1(self):
        self.filterWindow = QtWidgets.QMainWindow()
        global real_button_name
        real_button_name = self.pushButton_5.objectName()
        print(real_button_name)
        self.ui = Ui_filterWindow()
        self.ui.setupUi(self.filterWindow, self)
        self.filterWindow.show()
    def searchWindow_2(self):
        self.filterWindow = QtWidgets.QMainWindow()
        global real_button_city
        real_button_city = self.pushButton_6.objectName()
        print(real_button_city)
        self.ui = Ui_filterWindow()
        self.ui.setupUi(self.filterWindow, self)
        self.filterWindow.show()
    def searchWindow_3(self):
        self.filterWindow = QtWidgets.QMainWindow()
        global real_button_services
        real_button_services = self.pushButton_7.objectName()
        print(real_button_services)
        self.ui = Ui_filterWindow()
        self.ui.setupUi(self.filterWindow, self)
        self.filterWindow.show()    
    def getdata(self):
        data_array = []
        with open("C:\\Users\\Asad Mehmood\\Documents\\GitHub\\CS261F21PID20\\hotels.csv", "r") as file:
        #with open("C:\\Users\\rizwa\\Documents\\GitHub\\CS261F21PID20\\hotels.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data_array.append(row)
        return data_array

    def getClassicData(self):
        data_array = []
        with open("C:\\Users\\Asad Mehmood\\Documents\\GitHub\\CS261F21PID20\\hotels.csv", "r") as file:
        #with open("C:\\Users\\rizwa\\Documents\\GitHub\\CS261F21PID20\\hotels.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                c = hotel(row[0], row[1], row[2],
                          row[3], row[4], row[5], row[6])
                data_array.append(c)
        return data_array

    def loaddata(self, data_array):
        row = 0
        for i in data_array:
            data = [{"Name": i[0],
                     "Price":i[1],
                     "City":i[2],
                     "Rating":i[3],
                     "Reviews":i[4],
                     "Services":i[5],
                     "Ranking":i[6]}]
            self.tableWidget.setRowCount(len(data_array))
            for person in data:
                self.tableWidget.setItem(
                    row, 0, QtWidgets.QTableWidgetItem(person["Name"]))
                self.tableWidget.setItem(
                    row, 1, QtWidgets.QTableWidgetItem(person["Price"]))
                self.tableWidget.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(person["City"]))
                self.tableWidget.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(person["Rating"]))
                self.tableWidget.setItem(
                    row, 4, QtWidgets.QTableWidgetItem(person["Reviews"]))
                self.tableWidget.setItem(
                    row, 5, QtWidgets.QTableWidgetItem(person["Services"]))
                self.tableWidget.setItem(
                    row, 6, QtWidgets.QTableWidgetItem(person["Ranking"]))
            row += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Names"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Review"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Services"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ranking"))
        self.label.setText(_translate("MainWindow", "TripAdvisor"))
        self.label_2.setText(_translate("MainWindow", "Time Elapsed:"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Pause"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Resume"))
        self.ssButton.setText(_translate("MainWindow", "S"))
        self.ssButton_2.setText(_translate("MainWindow", "S"))
        self.ssButton_3.setText(_translate("MainWindow", "S"))
        self.ssButton_4.setText(_translate("MainWindow", "S"))
        self.ssButton_5.setText(_translate("MainWindow", "S"))
        self.ssButton_6.setText(_translate("MainWindow", "S"))
        self.ssButton_7.setText(_translate("MainWindow", "S"))
        self.pushButton_5.setText(_translate("MainWindow", "F"))
        self.pushButton_6.setText(_translate("MainWindow", "F"))
        self.pushButton_7.setText(_translate("MainWindow", "F"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
