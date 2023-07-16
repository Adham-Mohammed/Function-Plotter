from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QMessageBox,
    QPushButton,
    QWidget,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QGridLayout
)
from PySide2.QtGui import QFont, QIcon
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import sys



accepted_symbols=['+', '- ','/', '*','^','x','X','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.','(',')']

def extract_function(string,x):
    if len(string)==0:
        return "Please, Enter the equation"
    else:
        notAccepted=[]
        for symbol in string:
            if(symbol not in accepted_symbols):
                notAccepted.append(symbol)
        if(notAccepted):
            return "You can't use: {}".format(", ".join(str(i) for i in notAccepted))
        else:
            if('x'  not in string):
                string=string+'+0*x'
            string=string.replace('^', '**')
            try:
                func=eval(string)
                return func
            except Exception as e:
                return str(e)



class Plotter:
    def __init__(self, figure):
        self.figure = figure
        self.axes = self.figure.subplots()

    def plot(self, x, y):
        self.axes.clear()
        self.axes.plot(x, y)
        self.figure.canvas.draw()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")
        self.setGeometry(700, 300, 1000, 500)

        # create the widgets
        self.view = FigureCanvas(Figure(figsize=(8, 8)))
        self.toolbar = NavigationToolbar(self.view, self)
        self.function_label = QLabel("Enter a function:")
        self.function = QLineEdit(self)
        self.plot_btn = QPushButton("Plot")
        self.xmin_label = QLabel("X min:")
        self.xmax_label = QLabel("X max:")
        self.xmin_spinbox = QSpinBox()
        self.xmax_spinbox = QSpinBox()
        
        # define error message
        self.Error_msg = QMessageBox()
        self.Error_msg.setWindowTitle("An error occurred")
        self.Error_msg.setWindowIcon(QIcon("images/Error.png"))

        # add style 
        self.function_label.setMaximumHeight(20)
        self.plot_btn.setStyleSheet(
            "QPushButton { width: 200px; padding: 5px; font-weight:bold }")
        self.xmin_label.setFixedWidth(40)
        self.xmax_label.setFixedWidth(40)
        self.xmax_spinbox.setValue(5)

        # set the range for the spinboxes
        self.xmin_spinbox.setRange(-1000, 1000)
        self.xmax_spinbox.setRange(-1000, 1000)

        # create the plotter
        self.plotter = Plotter(self.view.figure)

        # connect the plot button to the plotter
        self.plot_btn.clicked.connect(self.plot_function)

        # create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.view)
        layout.addWidget(self.function_label)
        layout.addWidget(self.function)

        # create the horizontal layout for the spinboxes
        spinbox_layout = QHBoxLayout()
        spinbox_layout.addWidget(self.xmin_label)
        spinbox_layout.addWidget(self.xmin_spinbox)
        spinbox_layout.addWidget(self.xmax_label)
        spinbox_layout.addWidget(self.xmax_spinbox)
        layout.addLayout(spinbox_layout)

        # create a horizontal layout for the plot button
        plot_layout = QHBoxLayout()
        plot_layout.addStretch(1)  # add a flexible space to center the button
        plot_layout.addWidget(self.plot_btn)
        plot_layout.addStretch(1)  # add a flexible space to center the button
        layout.addLayout(plot_layout)
        self.setLayout(layout)

        # set the application icon and center the window
        self.add_icon(path="images/pngwing.com (1).png")
        self.center_window()



    def plot_function(self):
        xmin_value = self.xmin_spinbox.value()
        xmax_value = self.xmax_spinbox.value()
        if(xmin_value>xmax_value):
            self.Error_msg.setText("X min cannot be smaller than X max")
            self.Error_msg.exec_()
        else:
            x = np.linspace(xmin_value, xmax_value, 1000)
            function_value=self.function.text()
            y=extract_function(function_value,x)
            #to check there are an error
            if isinstance(y,str):
                self.Error_msg.setText(y)
                self.Error_msg.exec_()
            else:
                #to remove any inf values 
                y = np.delete(y,np.where(np.isnan(y)|np.isinf(y)))
                x = np.delete(x,np.where(np.isnan(y)|np.isinf(y)))
                self.plotter.plot(x, y) 


    def add_icon(self,path):
        appIcon = QIcon(path)
        self.setWindowIcon(appIcon)

    def center_window(self):
        qRect = self.frameGeometry()
        centerPoint = QApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    Window = Window()
    Window.show()
    sys.exit(app.exec_())
