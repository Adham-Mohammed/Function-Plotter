<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src=".\images/icon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Function Plotter</h3>

  <p align="center">
    A simple python GUI program that plots an arbitrary user-entered function.!

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Projecth [screenShots](images/screenShots)

![Demo](https://github.com/Adham-Mohammed/Function-Plotter/assets/81479927/5488e7e4-f0ee-4e6c-a8ff-bb9803186be5)

This project is a function plotter that allows users to input a mathematical function and plot it on a graph. The GUI is created using PySide2 and includes a QLineEdit for user input, QSpinBox widgets for setting the x-axis range, and a QPushButton to initiate the plot. The function input is checked for errors and parsed into a mathematical expression using the extract_function function. The plot is created using the Plotter class, which takes a matplotlib Figure object and creates a plot using the plot method. The resulting plot is displayed in a FigureCanvas widget. The application also includes an error message box and methods for setting the application icon and centering the window on the screen.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

<img src="https://docs.pytest.org/en/7.4.x/_static/pytest_logo_curves.svg" width="50" height="50" alt="Pytest Logo">
<img src="https://qt-wiki-uploads.s3.amazonaws.com/images/d/db/PySideLogo2.png" width="60" height="60" alt="Pyside Logo">


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

 * pyside2
  ```sh
  pip install pyside2
  ```
  * pytest
  ```sh
   pip install pytest
  ```
  * numpy
  ```sh
   pip install numpy
  ```
  * matplotlib
  ```sh
   pip install matplotlib
  ```
  

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [GeeksforGeeks pyside2](https://www.geeksforgeeks.org/pyside2-how-to-create-window/)
* [Tutorialspoint pytest](https://www.tutorialspoint.com/pytest/pytest_quick_guide.htm)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



