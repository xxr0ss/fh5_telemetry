import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtCore import QUrl, QObject, Signal, Slot, Property
from PySide6.QtQuickControls2 import QQuickStyle
from PySide6.QtQuick import QQuickItem
from utils import FH5_API, FH5_Data
from typing import Optional
from socket import socket, AF_INET, SOCK_DGRAM
import threading


class Backend(QQuickItem):
    dataUpdated = Signal()

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self._fh5_api = FH5_API()
        self.fh5_data = b'\x00' * 324

    @Property('QVariant', notify=dataUpdated)
    def fh5_data(self) -> FH5_Data:
        d = {}
        data = self._fh5_api.fh_data
        for f in data._fields_:
            d[f[0]] = getattr(data, f[0])
        return d
    
    @fh5_data.setter
    def fh5_data(self, data: bytes):
        if not isinstance(data, bytes):
            raise TypeError('Error data type, bytes needed')
        self._fh5_api.fh_data = data
        self.dataUpdated.emit()


class Listener(threading.Thread):
    def __init__(self, receiver: Backend):
        super().__init__()
        self.receiver: Backend = receiver
        self._running = True
        self.s: socket = None
        
    def run(self):
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.bind(('localhost', 8000))
        while self._running:
            self.receiver.fh5_data = (t := self.s.recv(324))
    
    def terminate(self):
        self._running = False
        self.s.close()



def main():
    app = QGuiApplication(sys.argv)
    app.setApplicationName('FH5 Telemetry')
    QQuickStyle.setStyle('Material')

    qmlRegisterType(Backend, 'BackendPlugin', 1, 0, 'Backend')
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile('main.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    obj = engine.rootObjects()[0]
    backend =  obj.findChild(Backend)


    
    listener = Listener(backend)
    listener.start()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()