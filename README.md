# PyQt5 - Simple PC task monitor
## 1. What is this
<img src="./img.jpg"></img><br/><br/>
This program reads and displays CPU and RAM information of Windows PC in real time using QThread.
<br>This program was written using Pyqt5 and Python 3.8.
<br><br>
To get the name of the cpu, I used the cpuinfo.py script written by Pearu Peterson.<br>
https://github.com/pydata/numexpr/blob/master/numexpr/cpuinfo.py
<br>
## 2. Install required packages
- Python3+ (The version of Python used when making this program is 3.8)
- PyQt (PyQt5)
- Pyinstaller

If you want to build this source, run this command in your project's directory.
<pre><code>pyinstaller --onefile --windowed main.py</code></pre>

