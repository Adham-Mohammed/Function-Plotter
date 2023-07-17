import pytest
from function_plotter import Window,extract_function

from PySide2.QtTest import QTest
from PySide2.QtCore import Qt

import numpy as np



@pytest.fixture
def window(qtbot):
    # create a Window instance and add it to the qtbot test harness
    win = Window()
    qtbot.add_widget(win)
    return win

def test_spinbox(window):
    # test xmin
    QTest.mouseClick(window.xmin_spinbox, Qt.LeftButton)
    QTest.keyClicks(window.xmin_spinbox, "10")
    # test xmax
    # clear the default value of xmax_spinbox
    window.xmax_spinbox.clear()

    QTest.mouseClick(window.xmax_spinbox, Qt.LeftButton)
    QTest.keyClicks(window.xmax_spinbox, "10")

    assert window.xmin_spinbox.value() == 10 and window.xmax_spinbox.value() == 10
    
# check plotting
class Test_plotting:
    # check that the plot is visible
    def test_plot_show(self,window):
        QTest.keyClicks(window.function, "x")
        window.xmin_spinbox.setValue(-5)
        window.xmax_spinbox.setValue(5)
        # click the plot button
        QTest.mouseClick(window.plot_btn, Qt.LeftButton)
        # check that a plot is displayed
        assert window.plotter.axes.lines != []

    # check that the plot is drawing correctly
    def test_plot_correctly(self,window):
        QTest.keyClicks(window.function, "(x^2)+1")
        window.xmin_spinbox.setValue(-5)
        window.xmax_spinbox.setValue(5)
        QTest.mouseClick(window.plot_btn, Qt.LeftButton)
        x, y = window.plotter.axes.lines[0].get_data()
        assert (y == (x**2)+1).all()

    # check extract_function
    def test_extract_function(self):
        x=x = np.linspace(-5, -5, 1000)
        string='(x^2)+1'
        y=extract_function(string,x)
        assert (y==(x**2)+1).all()

#errors 
class Test_errors:
    def test_empty_input(self,window):
        QTest.keyClicks(window.function, "")
        window.xmin_spinbox.setValue(-5)
        window.xmax_spinbox.setValue(5)
        QTest.mouseClick(window.plot_btn, Qt.LeftButton)

    #     # check if error message is error detected
        assert window.Error_msg.text() == "Please, Enter the equation"

    def test_invalid_symbols(self,window):
        QTest.keyClicks(window.function, "&#$")
        window.xmin_spinbox.setValue(-5)
        window.xmax_spinbox.setValue(5)
        QTest.mouseClick(window.plot_btn, Qt.LeftButton)

        # check if error message is error detected
        assert window.Error_msg.text() == "You can't use: &, #, $"

    def test_division_by_zero(self,window):
        QTest.keyClicks(window.function, "1/0")
        window.xmin_spinbox.setValue(-5)
        window.xmax_spinbox.setValue(5)
        QTest.mouseClick(window.plot_btn, Qt.LeftButton)

        # check if error message is error detected
        assert window.Error_msg.text() == "division by zero"

    def test_xmax_smaller_than_xmin(self,window):
        QTest.keyClicks(window.function, "x")
        window.xmin_spinbox.setValue(8)
        window.xmax_spinbox.setValue(5)
        QTest.mouseClick(window.plot_btn, Qt.LeftButton)

        # check if error message is error detected
        assert window.Error_msg.text() == "X max cannot be smaller than X min"


        
