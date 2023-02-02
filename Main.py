# importing matplot lib
import matplotlib.pyplot as plt
import numpy as np

# importing movie py libraries
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# numpy array
x = np.linspace(-5, 5, 100)

# duration of the video
duration = 2

# matplot subplot
fig, ax = plt.subplots()

# method to get frames
def make_frame(t):
	
	# clear
	ax.clear()
	
	# plotting line
	ax.plot(x, np.sinc(x**2) + np.cos(x + 10 * np.pi / duration * t), lw = 3)
	ax.set_ylim(-1.5, 2.5)
	
	# returning numpy image
	return mplfig_to_npimage(fig)

# creating animation
animation = VideoClip(make_frame, duration = duration)

# displaying animation with auto play and looping
animation.ipython_display(fps = 20, loop = True, autoplay = True)
