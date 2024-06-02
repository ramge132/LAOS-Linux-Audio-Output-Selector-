#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import pulsectl

def switch_output_device():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Switch Audio Output')
    layout = QVBoxLayout()

    with pulsectl.Pulse('audio-switcher') as pulse:
        for sink in pulse.sink_list():
            btn = QPushButton(sink.description)
            btn.clicked.connect(lambda _, sink=sink: pulse.sink_default_set(sink))
            layout.addWidget(btn)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    switch_output_device()


