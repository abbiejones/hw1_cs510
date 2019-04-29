import wave as wav
import sys
import math
import numpy as np

#referencing Bart Massey's code at https://github.com/BartMassey/pdx-cs-sound/blob/master/findpeak.py
def read_file():
  wavefile = wav.open(sys.argv[1], 'rb')
  channels = wavefile.getnchannels()
  width = wavefile.getnchannels()
  rate = wavefile.getframerate()
  frames = wavefile.getnframes()
  frame_width = width * channels

  max_sample = None
  min_sample = None

  wave_bytes = wavefile.readframes(frames)

  max_sample = None
  min_sample = None
  wave_bytes = wavefile.readframes(frames)
  # Iterate over frames.
  for f in range(0, len(wave_bytes), frame_width):
      frame = wave_bytes[f : f + frame_width]
      # Iterate over channels.
      for c in range(0, len(frame), width):
          # Build a sample.
          sample_bytes = frame[c : c + width]
          # XXX Eight-bit samples are unsigned
          sample = int.from_bytes(sample_bytes,
                                  byteorder='little',
                                  signed=(width>1))
          # Check extrema.
          if max_sample == None:
              max_sample = sample
          if min_sample == None:
              min_sample = sample
          if sample > max_sample:
              max_sample = sample
          if sample < min_sample:
              min_sample = sample

#taken from Bart Massey at https://moodle.cs.pdx.edu/mod/page/view.php?id=88
class Goertzel:
  def __init__(self, frequency, rate):
    self.norm = numpy.exp(1j * frequency * n)
    self.coeffs = numpy.array([-1j * frequency * k for k in range(n)])

  def target_frequency(frequency, sample_rate):
    return 2 * math.pi * frequency / sample_rate
    
  def calculate_i():
    return sqrt(-1)

  def filter(x,f):
    j = calculate_i()

    y = numpy.abs(norm * numpy.dot(coeffs, xs))


def main():
  sample, frequency = read_file()

  results = Goertzel(sample, frequency)