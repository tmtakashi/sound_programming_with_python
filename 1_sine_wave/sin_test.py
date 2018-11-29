import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# パラメータ設定
fs = 48000
f0 = 500
duration = 5

# 時間軸
t = np.linspace(0, 5, duration * fs, endpoint=False)
# サイン波
x = np.sin(2 * np.pi * f0 * t)

# グラフ
# plt.plot(t, x)
# plt.show()

# plt.plot(t, x)
# plt.xlim(0, 0.01)
# plt.show()

# wavファイル書き出し
sf.write('sine.wav', x, 48000)
