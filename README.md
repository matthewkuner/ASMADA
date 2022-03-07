# ASMADA
Automatic Shape Memory Alloy Data Analyzer (ASMADA) source code v 1.0 (last updated April 2021). 


## SUMMARY:
This project serves to automatically analyze isobaric thermal cycling tests of Shape Memory Alloys (SMAs) in accordance with ASTM standard E3097-17. This code accompanies a journal manuscript:\
Matthew C. Kuner, Anargyros A. Karakalas, and Dimitris C. Lagoudas, \
"ASMADA – A Tool for Automatic Analysis of Shape Memory Alloy Thermal Cycling Data under Constant Stress", \
Smart Materials and Structures (2021), DOI: [yet to be given]


## FUNCTIONALITY:
This software provides a Graphical User Interface (GUI) to allow users to easily input their own experimental data into the tool. This tool then performs the following functions:
1. identify thermal cycles from the raw data.
2. apply a pre-defined set of processes to determine twenty-three (23) material properties/parameters, including the four (4) transformation start/finish points. All but three of these properties are defined within the aforementioned ASTM standard.
3. create figures showing the evolution of key properties, alongside an animation showing the tangent line fitting used to determine the transformation start/finish points.
4. export the figures, animation, and a spreadsheet or txt document containing the numerical values for each of the properties obtained from each cycle.


## INSTALLATION:
This project was developed in Python 3.7.3. For users simply wishing to analyze their data, download the repository by clicking on "Code" --> "Download Zip". Then, navigate to the application format relevant to your operating system (.exe for Windows, .dmg for MacOS).

If you plan on using the source code, then you will need to download the same dependencies. All packages and versions used in developing this application can be found in the provided "requirements.txt" file. These packages can be easily downloaded by running the following in your command prompt (or Terminal, etc.): \
    ```$ pip install -r requirements.txt``` \
or running the equivalent within a virtual environment.


## LICENSE:
This project is distributed under the GNU General Public License version 3. See "LICENSE.txt" for more information.


## AUTHOR INFORMATION:
Matthew Kuner -- conctact at:
* matthewkuner@gatech.edu
* matthewkuner@gmail.com
* matthewkuner@yahoo.com
