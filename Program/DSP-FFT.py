import numpy as np
import matplotlib.pyplot as plt

# Parameter Sinyal
A = 1 # Amplitudo
f0 = 100 # Frekuensi Natural
Fs = 2000 # Frekuensi Sampling
N = int(10*Fs/f0) # Jumlah Sampel
tStep = 1/Fs # Sampel Interval Waktu
fStep = Fs/N # Sampel Intervak Frekuensi
t = np.linspace(0, (N-1)*tStep, N) # Step Waktu
f = np.linspace(0, (N-1)*fStep, N) # Step Frekuensi

# Membuat Sinyal Diskrit
sn1 = A * np.sin(2*np.pi*f0*t)
sn2 = 4 * A * np.sin(2*np.pi*3*f0*t)
snt = sn1 + sn2

# Fast Fourier Transform
ft = np.fft.fft(snt)
ft_mag = np.abs(ft)
f_plot = f[0:int(N/2+1)]
ft_mag_plot = 2*ft_mag[0:int(N/2+1)]

#plot

plt.subplot(2,1,1)
plt.plot(t,snt)
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid()
plt.show()

plt.subplot(2,2,2)
plt.plot(f_plot,ft_mag_plot)
plt.xlabel("Frekuensi")
plt.ylabel("Intensitas (db)")
plt.grid()
plt.show()
