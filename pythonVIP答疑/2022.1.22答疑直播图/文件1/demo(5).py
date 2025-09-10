import numpy as np
import scipy.io.wavfile as swave

# 声音可以表示为某个振幅和频率的正弦波
# y=a*sin(b*x+phi)   a   振幅    phi   相位
# 假如把钢琴键编号1-88
# 那么其频率为440*2**（（n-49）/12）  n 钢琴键编号

# 采样频率
rate=44100
# print(np.random.random((3,6)))
def gen_wave(freq,amp,dur,phi):
    t=np.linspace(0,dur,int(dur*rate))
    # 周期函数：T=2*pi/|b|=1/f   b=2*pi*f
    # 波每一个时刻都有一个对应的能量值
    data=amp*np.sin(2*np.pi*freq*t+phi)
    # 通常使用16bit有符号整数存储，采样大小是16bit
    return data.astype(np.int16)

# 初始化
# 89键
ntones=89
# 振幅
amp=np.dot(2000,np.random.random(ntones,))+200
# 音频时长0.01-0.2s
dur=0.19*np.random.random((ntones,))+0.01
# key=np.random.random_integers(1,88,ntones)
key=np.array([x for x in range(0,ntones)])
freq=440*2**((key-49)/12)
# 初相0-2pi
phi=2*np.pi*np.random.random((ntones,))

tone=np.array([],dtype="int16")
for i in range(ntones):
    new_tone=gen_wave(freq[i],amp[i],dur[i],phi[i])
    tone=np.concatenate((tone,new_tone))

swave.write("wave.wav",rate,tone)
