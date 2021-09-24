Digital Camera Monitoring System
-------------

Digital Camera Monitoring System(DigiMon) is a program that measures the transverse profile of a beam using the camera.

Korean manual: [Korean](https://github.com/Somhammer/DigiMon/blob/master/README_KR.md)

English manual: [English](https://github.com/Somhammer/DigiMon/blob/master/README.md)

### Download and Installation

The newest program can be downloaded in the [release](https://github.com/Somhammer/DigiMon/releases) section of the repository.
Download it for your operating system and install software of the camera corporations like Basler and Allied Vision then you can use the program. 
If you download a source file, many libraries should be needed additionally.

#### Pylon

DigiMon uses Pylon 6.2.0. [Download](https://www.baslerweb.com/en/sales-support/downloads/software-downloads/) and install it for your operating system.
If your operating system is Linux, add the PYLON_ROOT environment parameter. The value of the parameter is the location of installation(ex: /home/seohyeon/pylon).

#### Vimba

DigiMon uses Vimba 5.0. [Download](https://www.alliedvision.com/en/products/vimba-sdk/#c1497) and install it for your operating system.
If your operating system is Window, add the VIMBA_HOME environment parameter. The value of the parameter is the location of installation(ex: C:\Program Files\Allied Vision\Vimba_5.0).

The DigiMon can be operated neither two software are installed, but GigE camera of each corporation cannot be connected. Please install the software that you need.

#### Source file installation
