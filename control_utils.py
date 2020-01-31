
from Tkinter import *

App = Tk()

# Set the initial value required for each of the value
min_disparity = -64
num_disparity = 16
sad_window_size = 3
p1 = 400
p2 = 2000
disp12maxdiff = 0
block_size = 5
uniqueness_ratio= 1
speckle_window_size = 50
speckle_range = 1


def init():

    global min_disparity, num_disparity, sad_window_size, p1, p2, disp12maxdiff, \
        block_size, uniqueness_ratio, speckle_window_size, speckle_range
    global App
    create_gui(App)


# Def Init Function
def get_app_handle():
    global App
    return App


# Define Callbacks for Tkinter GUI Sliders
def min_disparity_cb(val):
    global min_disparity
    min_disparity = int(val)


def num_disparity_cb(val):
    global num_disparity
    num_disparity = int(val)


def sad_window_size_cb(val):
    global sad_window_size
    sad_window_size = int(val)


def p1_cb(val):
    global p1
    p1 = int(val)


def p2_cb(val):
    global p2
    p2 = int(val)


def disp12maxdiff_cb(val):
    global disp12maxdiff
    disp12maxdiff = int(val)


def block_size_cb(val):
    global block_size
    block_size = int(val)


def uniqueness_ratio_cb(val):
    global uniqueness_ratio
    uniqueness_ratio = int(val)


def speckle_window_size_cb(val):
    global speckle_window_size
    speckle_window_size = int(val)


def speckle_range_cb(val):
    global speckle_range
    speckle_range= int(val)


def create_gui(app):
    # Decide the resolution etc of the slider GUI
    _width = 20
    _length = 300
    _resolution = 1
    res_val = 1
    # Define Sliders and Labels
    min_disparity_slider = Scale(app, from_=-128, to=64, resolution=_resolution, width=_width, length=_length, orient=HORIZONTAL, command=min_disparity_cb)
    min_disparity_slider.pack(expand=YES, fill=Y)
    min_disparity_label = Label(app, text="min Disparity value")
    min_disparity_label.pack(expand=YES, fill=Y)

    num_disparity_slider = Scale(app, from_=16, to=320, resolution=16, width=_width, length=_length, orient=HORIZONTAL, command=num_disparity_cb)
    num_disparity_slider.pack(expand=YES, fill=Y)
    num_disparity_label = Label(app, text="numDisparities value")
    num_disparity_label.pack(expand=YES, fill=Y)

    sad_window_size_slider = Scale(app, from_=3, to=11, resolution=res_val, width=_width, length=_length, orient=HORIZONTAL, command=sad_window_size_cb)
    sad_window_size_slider.pack(expand=YES, fill=Y)
    sad_window_size_label = Label(app, text="SAD Window size value")
    sad_window_size_label.pack(expand=YES, fill=Y)
    #
    p1_slider = Scale(app, from_=400, to=1000, resolution=res_val, width=_width, length=_length, orient=HORIZONTAL, command=p1_cb)
    p1_slider.pack(expand=YES, fill=Y)
    p1_label = Label(app, text="P1 value")
    p1_label.pack(expand=YES, fill=Y)

    p2_slider = Scale(app, from_=2000, to=3000, resolution=res_val, width=_width, length=_length, orient=HORIZONTAL, command=p2_cb)
    p2_slider.pack(expand=YES, fill=Y)
    p2_label = Label(app, text="P2 value")
    p2_label.pack(expand=YES, fill=Y)

    disp12maxdiff_slider = Scale(app, from_=0, to=100, resolution=res_val, width=_width, length=_length, orient=HORIZONTAL, command=disp12maxdiff_cb)
    disp12maxdiff_slider.pack(expand=YES, fill=Y)
    disp12maxdiff_label = Label(app, text="disp12MaxDiff value")
    disp12maxdiff_label.pack(expand=YES, fill=Y)

    block_size_slider = Scale(app, from_=5, to=21, resolution=res_val, width=_width, length=_length, orient=HORIZONTAL, command=block_size_cb)
    block_size_slider.pack(expand=YES, fill=Y)
    block_size_label = Label(app, text="block size")
    block_size_label.pack(expand=YES, fill=Y)

    uniqueness_ratio_slider = Scale(app, from_=1, to=20, resolution=res_val, width=_width, length=_length, orient=HORIZONTAL, command=uniqueness_ratio_cb)
    uniqueness_ratio_slider.pack(expand=YES, fill=Y)
    uniqueness_ratio_label = Label(app, text="uniquenessRatio value")
    uniqueness_ratio_label.pack(expand=YES, fill=Y)

    speckle_window_size_slider = Scale(app, from_=50, to=200, resolution=res_val, width=_width, length=_length, orient=HORIZONTAL, command=speckle_window_size_cb)
    speckle_window_size_slider.pack(expand=YES, fill=Y)
    speckle_window_size_label = Label(app, text="speckleWindowSize value")
    speckle_window_size_label.pack(expand=YES, fill=Y)

    speckle_range_slider = Scale(app, from_=1, to=5, resolution=res_val, width=_width, length=_length, orient=HORIZONTAL, command=speckle_range_cb)
    speckle_range_slider.pack(expand=YES, fill=Y)
    speckle_range_label = Label(app, text="speckleRange value")
    speckle_range_label.pack(expand=YES, fill=Y)

