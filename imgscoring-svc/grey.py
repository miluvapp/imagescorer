from skimage import exposure
import numpy as np
import math

def grey_scale(moon: np.ndarray):

    hist_grey = exposure.histogram(moon)
    moon_r = moon[:,:,0]
    moon_g = moon[:,:,1]
    moon_b = moon[:,:,2]
    hist_r = exposure.histogram(moon_r)
    hist_g = exposure.histogram(moon_g)
    hist_b = exposure.histogram(moon_b)
    delta_r = np.linalg.norm(hist_r[0] - hist_grey[0])
    delta_g = np.linalg.norm(hist_g[0] - hist_grey[0])
    delta_b = np.linalg.norm(hist_b[0] - hist_grey[0])
    stdev = np.std([delta_r, delta_g, delta_b])
    saturation2 = stdev / math.sqrt(moon.shape[0] * moon.shape[1])
    return saturation2