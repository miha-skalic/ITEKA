# ITEKA


Description
-----------
"I"sothermal "T"ration calorimetry "E"nyzme "K"inetics "A"nalyzer -
ITEKA - software for data exploration and enzyme kinetics model 
fitting from Isothermal Tration calorimetry as well as classical 
kinetics assays.


Instalation
-----------
1. Windows
   Package containing all prerequisite can be downloaded at:
   http://systemsbiology.hi.is/ITEKA
   To install it correctly make sure you do not have Python3
   in you registry. Alternatively you can set up Python and 
   packages independently.

2. Unix (Mac and Linux)
   Ubuntu 14.04.2 install script is provided in at:
   http://systemsbiology.hi.is/ITEKA
   If using you are using different system you will have to 
   prepare python3 environment with packages listed in 
   Prerequisites.


Run
---
1. Windows
   Run "ITEKA.bat" file in install folder (if you used provided
   installer) or run ITEKA.py with your Python3 interpreter. 
   
2. Unix (Mac and Linux)
   Run ITEKA.py with your Python3 interpreter.


Prerequisites
-------------
* Python 3.(3.4.3)
* Numpy (1.8.2)
* Scipy (0.14.1)
* PyQt 4.(11.4)
* lmfit (0.8.3)
* Openpyxl (2.2.4)
* matplotlib (1.4.3)

Note: ITEKA was tested on specified package versions, but it 
      is possible to run it on different versions as well.


Removing Software
-----------------
If you used provided install package run python-3.4.3.msi and 
choose "Remove" option. After that Remove the whole install 
directory. If you are using your own interpreter omit first 
step.


Problems and Questions
----------------------
In case of technical problems (bugs etc.) or questions on the 
scientific aspects of ITEKA please contact Miha Skalic, 
miha.skalic@gmail.com


License
-------
ITEKA - software for enzyme kinetics data fitting
Copyright (C) 2015  Miha Skalic and Neha Rohatgi

This program is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, or (at your option) 
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/gpl
