import numpy as np
import time

from easyrobot.encoder.Unitree_encoder import UnitreeEncoder
from easyrobot.encoder.Cybergear_encoder import CybergearEncoder
from easyrobot.encoder.End_effector import EndEffectorEncoder

Unitree_encoder = UnitreeEncoder(ids = [0, 1, 2], port = '/dev/ttyUSB0', baudrate = 4000000)
Cybergear_encoder = CybergearEncoder(ids = [1, 2], port = '/dev/ttyUSB1', baudrate = 921600)
effector_encoder = EndEffectorEncoder(ids = [1, 2], port = '/dev/ttyUSB2', baudrate = 115200)

while True:
    Unitree_e = Unitree_encoder.fetch_info()
    print(Unitree_e)
    Cybergear_e = Cybergear_encoder.fetch_info()
    print(Cybergear_e)
    EndEffector_e = effector_encoder.fetch_info()
    print(EndEffector_e)
    time.sleep(0.1)