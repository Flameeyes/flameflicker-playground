# SPDX-FileCopyrightText: 2020 Diego Elio Pettenò
#
# SPDX-License-Identifier: MIT

import pulseio
import board
import time

import waveform

pwm = pulseio.PWMOut(board.D5, frequency=152000)
while True:
    for i in range(1024):
        pwm.duty_cycle = waveform.WAVEFORM[i]
        time.sleep(0.004)
