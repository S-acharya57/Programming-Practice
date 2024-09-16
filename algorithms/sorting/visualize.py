import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import rc
from PIL import Image
import time 


def sort(arr, sort_function, speed = 0.003, gif_name="sort"):
    # Ensure that GIF output is enabled
    rc('animation', html='html5')

    def update_plot(frame, bars, speed):
        arr, current_index = frame  
        for i, (bar, val) in enumerate(zip(bars, arr)):
            bar.set_height(val)
            # Highlight the current index in red, others in blue
            if i == current_index:
                bar.set_color('red')
            else:
                bar.set_color('blue')

        time.sleep(speed) # seconds

    
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title('Insertion Sort Visualization')
    speed = speed

    # Create the animation by calling the update function at each step
    ani = animation.FuncAnimation(fig, update_plot, frames=sort_function(arr.copy()),
                                fargs=(bars, speed), repeat=False)


    gif_path = gif_name
    ani.save(gif_path, writer='pillow')

    
    from IPython.display import Image as IPImage
    IPImage(filename=gif_path)