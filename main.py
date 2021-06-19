import sys
import math
import psutil
import cpuinfo

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSlot, pyqtSignal
from uis.ui_main import Ui_MainWindow
import time

# pc task =======================================
# def convert_byte(size):
#     n_size = math.floor(size / (1024 ** 3))
#     if n_size > 1000:
#         n_size = str(size / (1024 ** 4))
#         pt_idx = n_size.find('.')
#         n_size = n_size[0:pt_idx + 3]
#         return {'size': n_size, 'unit': 'TB'}
#     else:
#         return {'size': n_size, 'unit': 'GB'}


def load_update_datas():
    cpu = {
        'freq': f'{str(psutil.cpu_freq().current / 1024)} GHz',
        'usage_per': psutil.cpu_percent(interval=0.5)
    }

    m = psutil.virtual_memory()

    memory = {
        'used': str(round(m.used / 1024 ** 3)) + ' GB',
        'free': str(round(m.free / 1024 ** 3)) + ' GB',
        'usage_per': str(m.percent) + ' %'
    }

    return cpu, memory


def load_init_datas():
    # cpu 사용율
    cpu = {
        'cpu_model': cpuinfo.cpu.info[0]['ProcessorNameString'],
        'freq': f'{str(psutil.cpu_freq().current/1024)} GHz',  # 수시로 변함
        'usage_per': psutil.cpu_percent(interval=0.1),  # 수시로 변함
        'core_count_phy': psutil.cpu_count(logical=False),
        'core_count_log': psutil.cpu_count(logical=True),
    }

    # 메모리
    m = psutil.virtual_memory()
    memory = {
        'total': str(round(m.total / 1024 ** 3)) + ' GB',
        'used': str(round(m.used / 1024 ** 3)) + ' GB',  # 수시로 변함
        'free': str(round(m.free / 1024 ** 3)) + ' GB',  # 수시로 변함
        'usage_per': str(m.percent) + ' %',  # 수시로 변함
    }
    return cpu, memory


# 디스크 목록
# for p in psutil.disk_partitions():
#     disk_info = psutil.disk_usage(p.mountpoint)
#
#     s_total = convert_byte(disk_info.total)
#     s_used = convert_byte(disk_info.used)
#     s_free = convert_byte(disk_info.free)
#
#     self.disks.append({
#         'mount': p.mountpoint,
#         'usage_per': disk_info.percent,  # 수시로 변함
#         'total': str(s_total['size']) + ' ' + s_total['unit'],
#         'used': str(s_used['size']) + ' ' + s_used['unit'],  # 수시로 변함
#         'free': str(s_free['size']) + ' ' + s_free['unit'],  # 수시로 변함
#     })
# pc task =======================================


class LoadThread(QThread):
    proc = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            cpu, memory = load_update_datas()
            self.proc.emit({'cpu': cpu, 'memory': memory})
            time.sleep(0.5)


class WindowClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(flags=Qt.Window)
        self.setupUi(self)

        cpu, memory = load_init_datas()
        # cpu
        self.label_cpu_usage_per.setText(str(cpu['usage_per']) + ' %')
        self.label_cpu_model.setText(cpu['cpu_model'])
        self.label_freq.setText(cpu['freq'])
        self.label_core_phy.setText(str(cpu['core_count_phy']))
        self.label_core_log.setText(str(cpu['core_count_log']))

        # memory
        self.label_memory_usage_per.setText(memory['usage_per'])
        self.label_memory_total.setText(memory['total'])
        self.label_memory_free.setText(memory['free'])
        self.label_memory_used.setText(memory['used'])
        self.pc_task = None

        self.load_thread = LoadThread()
        self.load_thread.start()
        self.load_thread.proc.connect(self.proc)

    @pyqtSlot(dict)
    def proc(self, result):

        self.label_cpu_usage_per.setText(str(result['cpu']['usage_per']) + ' %')
        self.label_freq.setText(result['cpu']['freq'])

        self.label_memory_usage_per.setText(result['memory']['usage_per'])
        self.label_memory_free.setText(result['memory']['free'])
        self.label_memory_used.setText(result['memory']['used'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()

    myWindow.show()
    sys.exit(app.exec_())
