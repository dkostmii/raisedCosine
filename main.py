from matplotlib import pyplot
# from mpl_toolkits.mplot3d import Axes3D
from numpy import linspace
from numpy import array
from numpy import empty
from numpy import sinc
from math import sin
from math import pi
from numpy import meshgrid

# convert sinc to signal function representation
def sinct(t, f):
  return sinc(2 * pi * f * t)

def samplingfrequency(range, samples):
  return samples / range

def plot2D(samples, start, end, freq):
  sampling_freq = samplingfrequency(end - start, samples)
  domain_freq = freq
  amplitude = 1.2

  x = linspace(start, end, samples)

  print("Sampling frequency: " + str(sampling_freq))

  fun = (lambda t: amplitude * sinct(t, domain_freq))

  pyplot.plot(x, list(map(fun, x)))
  pyplot.axhline(y=amplitude, color='r', linestyle='-')
  pyplot.show()

def plot3D(samples, start, end, freq):
  sampling_freq = samplingfrequency(end - start, samples)
  domain_freq = freq
  amplitude = 4

  a = linspace(start, end, samples)
  b = linspace(start, end, samples)

  x, y = meshgrid(a, b)

  # Easy example of raised cosine 2D
  z = amplitude * sinct(x, domain_freq) * sinct(y, domain_freq)

  print("Sampling frequency: " + str(sampling_freq))

  fig = pyplot.figure(figsize=(4, 4))
  ax = fig.add_subplot(projection='3d')
  ax.set_xlim3d(start, end)
  ax.set_ylim3d(start, end)

  ax.plot_wireframe(x, y, z)
  pyplot.show()

def main():
  samples = 20
  start = -2
  end = 2

  plot3D(samples, start, end, 0.25)

if __name__ == "__main__":
  main()
