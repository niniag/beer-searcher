# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_BeerApp(object):
    def setupUi(self, BeerApp):
        BeerApp.setObjectName("BeerApp")
        BeerApp.resize(300, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(BeerApp)
        self.verticalLayout.setObjectName("verticalLayout")

        self.labelIntro = QtWidgets.QLabel(BeerApp)
        self.labelIntro.setObjectName("labelIntro")
        self.verticalLayout.addWidget(self.labelIntro)

        self.labelCountry = QtWidgets.QLabel(BeerApp)
        self.labelCountry.setObjectName("labelCountry")
        self.verticalLayout.addWidget(self.labelCountry)

        self.countryComboBox = QtWidgets.QComboBox(BeerApp)
        self.countryComboBox.setObjectName("countryComboBox")
        self.verticalLayout.addWidget(self.countryComboBox)

        self.labelColor = QtWidgets.QLabel(BeerApp)
        self.labelColor.setObjectName("labelColor")
        self.verticalLayout.addWidget(self.labelColor)

        self.colorComboBox = QtWidgets.QComboBox(BeerApp)
        self.colorComboBox.setObjectName("colorComboBox")
        self.verticalLayout.addWidget(self.colorComboBox)

        self.labelTaste = QtWidgets.QLabel(BeerApp)
        self.labelTaste.setObjectName("labelTaste")
        self.verticalLayout.addWidget(self.labelTaste)

        self.tasteComboBox = QtWidgets.QComboBox(BeerApp)
        self.tasteComboBox.setObjectName("tasteComboBox")
        self.verticalLayout.addWidget(self.tasteComboBox)

        self.labelFiltered = QtWidgets.QLabel(BeerApp)
        self.labelFiltered.setObjectName("labelFiltered")
        self.verticalLayout.addWidget(self.labelFiltered)

        self.filteredComboBox = QtWidgets.QComboBox(BeerApp)
        self.filteredComboBox.setObjectName("filteredComboBox")
        self.verticalLayout.addWidget(self.filteredComboBox)

        self.labelFoam = QtWidgets.QLabel(BeerApp)
        self.labelFoam.setObjectName("labelFoam")
        self.verticalLayout.addWidget(self.labelFoam)

        self.foamComboBox = QtWidgets.QComboBox(BeerApp)
        self.foamComboBox.setObjectName("foamComboBox")
        self.verticalLayout.addWidget(self.foamComboBox)

        self.findButton = QtWidgets.QPushButton(BeerApp)
        self.findButton.setObjectName("findButton")
        self.verticalLayout.addWidget(self.findButton)

        self.retranslateUi(BeerApp)
        QtCore.QMetaObject.connectSlotsByName(BeerApp)

    def retranslateUi(self, BeerApp):
        _translate = QtCore.QCoreApplication.translate
        BeerApp.setWindowTitle(_translate("BeerApp", "ლუდის ამომრჩევი"))
        BeerApp.setStyleSheet(_translate("BeerApp", """
            QWidget {
                background-color: black;
                color: yellow;
                font: 12pt "Arial";
            }
            QLabel {
                color: yellow;
                font-weight: bold;
            }
            QComboBox {
                background-color: #333300;
                color: yellow;
                selection-background-color: yellow;
                selection-color: black;
            }
            QPushButton {
                background-color: yellow;
                color: black;
                font-weight: bold;
                border-radius: 5px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #ffff66;
            }
        """))
        self.labelIntro.setText(_translate("BeerApp", "აირჩიე ლუდის მახასიათებლები:"))
        self.labelCountry.setText(_translate("BeerApp", "ქვეყანა:"))
        self.labelColor.setText(_translate("BeerApp", "ფერი:"))
        self.labelTaste.setText(_translate("BeerApp", "გემო:"))
        self.labelFiltered.setText(_translate("BeerApp", "გაფილტვრა:"))
        self.labelFoam.setText(_translate("BeerApp", "ქაფის რაოდენობა:"))
        self.findButton.setText(_translate("BeerApp", "იპოვე ლუდი"))



beers = [
    {"name": "Weihenstephaner", "country": "გერმანია", "color": "ღია", "taste": "დაბალგრადუსიანი", "filtered": "გაფილტრული", "foam": "საშუალო", "price": 7.5},
    {"name": "Duvel", "country": "ბელგია", "color": "ღია", "taste": "მაღალგრადუსიანი", "filtered": "გაფილტრული", "foam": "დიდი", "price": 9.0},
    {"name": "Pilsner Urquell", "country": "ჩეხეთი", "color": "ღია", "taste": "დაბალგრადუსიანი", "filtered": "გაფილტრული", "foam": "საშუალო", "price": 6.5},
    {"name": "Guinness", "country": "ირლანდია", "color": "მუქი", "taste": "მაღალგრადუსიანი", "filtered": "გაფილტრული", "foam": "დიდი", "price": 8.0},
    {"name": "Hoegaarden", "country": "ბელგია", "color": "ღია", "taste": "მჟავე", "filtered": "გაუფილტრავი", "foam": "ცოტა", "price": 7.0},
    {"name": "Leffe Brune", "country": "ბელგია", "color": "მუქი", "taste": "ტკბილი", "filtered": "გაფილტრული", "foam": "საშუალო", "price": 8.5},
    {"name": "Erdinger Weissbier", "country": "გერმანია", "color": "ღია", "taste": "მჟავე", "filtered": "გაუფილტრავი", "foam": "ცოტა", "price": 7.2},
    {"name": "Kozel Dark", "country": "ჩეხეთი", "color": "მუქი", "taste": "დაბალგრადუსიანი", "filtered": "გაფილტრული", "foam": "საშუალო", "price": 6.0},
    {"name": "Peroni Nastro Azzurro", "country": "იტალია", "color": "ღია", "taste": "დაბალგრადუსიანი", "filtered": "გაფილტრული", "foam": "ცოტა", "price": 6.3},
    {"name": "Chimay Blue", "country": "ბელგია", "color": "მუქი", "taste": "მაღალგრადუსიანი", "filtered": "გაფილტრული", "foam": "დიდი", "price": 10.0},
    {"name": "Baltika 7", "country": "რუსეთი", "color": "ღია", "taste": "დაბალგრადუსიანი", "filtered": "გაფილტრული", "foam": "საშუალო", "price": 5.5},
    {"name": "Mythos", "country": "საბერძნეთი", "color": "ღია", "taste": "დაბალგრადუსიანი", "filtered": "გაფილტრული", "foam": "ცოტა", "price": 6.0},
    {"name": "Budweiser Budvar", "country": "ჩეხეთი", "color": "ღია", "taste": "მაღალგრადუსიანი", "filtered": "გაფილტრული", "foam": "დიდი", "price": 7.8},
    {"name": "Zywiec Porter", "country": "პოლონეთი", "color": "მუქი", "taste": "მაღალგრადუსიანი", "filtered": "გაფილტრული", "foam": "საშუალო", "price": 7.5},
    {"name": "Affligem Blonde", "country": "ბელგია", "color": "ღია", "taste": "ტკბილი", "filtered": "გაფილტრული", "foam": "დიდი", "price": 9.2},
]



class BeerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BeerApp()
        self.ui.setupUi(self)


        self.ui.countryComboBox.addItems(["გერმანია", "ბელგია", "ჩეხეთი", "ირლანდია", "იტალია", "რუსეთი", "საბერძნეთი", "პოლონეთი"])
        self.ui.colorComboBox.addItems(["ღია", "მუქი"])
        self.ui.tasteComboBox.addItems(["მწარე", "მჟავე", "ტკბილი", "დაბალგრადუსიანი", "მაღალგრადუსიანი"])
        self.ui.filteredComboBox.addItems(["გაფილტრული", "გაუფილტრავი"])
        self.ui.foamComboBox.addItems(["ცოტა", "საშუალო", "დიდი"])


        self.ui.findButton.clicked.connect(self.find_beer)

    def find_beer(self):
        country = self.ui.countryComboBox.currentText()
        color = self.ui.colorComboBox.currentText()
        taste = self.ui.tasteComboBox.currentText()
        filtered = self.ui.filteredComboBox.currentText()
        foam = self.ui.foamComboBox.currentText()

        matches = [
            beer for beer in beers
            if beer["country"] == country and
               beer["color"] == color and
               beer["taste"] == taste and
               beer["filtered"] == filtered and
               beer["foam"] == foam
        ]

        if matches:
            result = matches[0]
            name = result["name"]
            price = result["price"]
            QMessageBox.information(self, "შედეგი", f"შესაფერისი ლუდი: {name}\nფასი: {price}₾")
        else:
            QMessageBox.warning(self, "შედეგი", "ასეთი ლუდი ვერ მოიძებნა.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BeerApp()
    window.show()
    sys.exit(app.exec_())



#
#
#
#
# PyQt5-ით შექმნილი მარტივი გრაფიკული აპლიკაცია, რომელიც მომხმარებელს საშუალებას აძლევს აირჩიოს ლუდის მახასიათებლები
# (ქვეყანა, ფერი, გემო, გაფილტვრა, ქაფის რაოდენობა) და მოძებნოს შესაბამისი ლუდი წინასწარ განსაზღვრული მონაცემთა ბაზიდან.
# აპლიკაცია იყენებს Python-ს და PyQt5-ს ინტერფეისის შექმნისთვის და ლუდების ფილტრაციის ლოგიკას.
#
#
# ლუდის ამომრჩევი არის მარტივი გრაფიკული აპლიკაცია, რომელიც შექმნილია Python და PyQt5 გამოყენებით.
# აპლიკაცია საშუალებას აძლევს მომხმარებელს აირჩიოს ლუდის მახასიათებლები, როგორიცაა ქვეყანა, ფერი, გემო, გაფილტვრა და
# ქაფის რაოდენობა, და მოძებნოს შესაბამისი ლუდი წინასწარ განსაზღვრული ბაზიდან. შედეგი გამოისახება შეტყობინების ფანჯარაში,
# სადაც ჩანს ლუდის სახელი და ფასი, ან გაფრთხილება, თუ მსგავსი ლუდი ვერ მოიძებნა. პროგრამა იყენებს PyQt5-ის UI კომპონენტებს,
# როგორიცაა QComboBox, QLabel, QPushButton და QMessageBox, რომ უზრუნველყოს მარტივი და ინტუიტიური ინტერფეისი.
# პროექტის მიზანია მომხმარებლისთვის მხარი დაუჭიროს მის გემოვნებასთან და მოთხოვნებთან შესაბამისი ლუდის სწრაფად მოძებნაში.