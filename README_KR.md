Digital Camera Monitoring System
-------------
Digital Camera Monitoring System(이하 DigiMon)은 카메라를 이용해 빔의 transverse profile을 측정하는 프로그램 입니다.

한국어 설명서: [Korean](https://github.com/Somhammer/DigiMon/blob/master/README_KR.md)

영어 설명서: [English](https://github.com/Somhammer/DigiMon/blob/master/README.md)

### 다운로드와 설치
최신 버전의 프로그램은 저장소의 [release](https://github.com/Somhammer/DigiMon/releases) 란에서 받을 수 있습니다.

만약 운영체제에 맞게 압축파일을 다운로드한 이용할 카메라 회사(Basler, Allied Vision)의 소프트웨어(Pylon, Vimba)를 설치하면 프로그램을 바로 이용할 수 있습니다. 

소스파일을 받은 경우에는 여러 라이브러리들이 추가로 필요합니다.

#### Pylon
DigiMon은 Pylon 6.2.0을 이용했으며 각자의 운영체제에 맞게 [다운로드](https://www.baslerweb.com/ko/sales-support/downloads/software-downloads/) 후 설치를 진행하면 됩니다.

그리고 리눅스의 경우 PYLON_ROOT 환경변수를 등록해야 합니다. 변수의 값은 Pylon이 설치된 경로입니다(예시: /home/seohyeon/pylon)
#### Vimba
DigiMon은 Vimba 5.0을 이용했으며 각자의 운영체제에 맞게 [다운로드](https://www.alliedvision.com/en/products/vimba-sdk/#c1497) 후 설치를 진행하면 됩니다.

그리고 윈도우의 경우 VIMBA_HOME 환경변수를 등록해야 합니다. 변수의 값은 Vimba가 설치된 경로입니다.(예시: C:\Program Files\Allied Vision\Vimba_5.0)


두 소프트웨어가 없어도 프로그램은 실행되지만 해당 회사의 GigE 카메라 연결이 되지 않습니다. 필요한 회사의 소프트웨어를 반드시 설치해주기 바랍니다.

#### 소스파일 설치
만약 소스파일을 다운로드 받아서 이용한다면 Python3.8 이상이 요구됩니다. 그리고 앞의 경우와 마찬가지로 pylon과 vimba가 필요합니다.
또한 다음과 같은 라이브러리들이 추가로 필요합니다.

- PySide6
- pyqtgraph
- colour
- matplotlib
- numpy
- scipy
- pyyaml
- cv2
- pypylon
- VimbaPython

위 라이브러리들을 pip을 이용해 설치한 뒤 python DigiMon.py를 이용해 실행할 수 있습니다.
