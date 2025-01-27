# %%
import numpy as np
import cv2

# %%
# Load an image from a file
image = cv2.imread("./boston.jpg")

# %%
print(type(image))

# %%
# For color images, the decoded images will have the channels stored in B G R order.
print(image.shape)

# %%
def tintBlue(image):
    """
        Tint the input image blue

        :param image: input color image
        :type image: ndarray
        :rtype: ndarray
    """
    image[:,:,0] = 255

    # TODO: your implementation here

    return image

# %%
image = tintBlue(image)

# %%
# Display the image
cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Display window", image)
# Wait for a key event infinitely
cv2.waitKey(0)
i = 0
while i < 100000000:
    i += 1
# Close all open windows
cv2.destroyAllWindows()
# For mac users, uncomment the following line
cv2.waitKey(1)

# %%
frame = 0
def readVideo(video_path):
    """
        Read the video frames.

        :param video_path: path to input video
        :type video_path: str
        :rtype: ndarray
    """
    num_frames = 0
    cap = cv2.VideoCapture(video_path)
    num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    video_frames = []
    for i in range(int(num_frames)):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        res, frame = cap.read()
        video_frames.append(frame)
        
    video_frames = np.array(video_frames)
    

    # TODO: your implementation here - write a function to read video frames and combine them into a numpy array of size 'T x H x W x C'.
    # T, H, W and C denote the number of frames, height, width and number of channels, respectively.

    # video_frames = NotImplemented
    return video_frames

    # return video_frames

# %%
# reads a video file
video_frames = readVideo("./input_video.mp4")

# %%
print(video_frames.shape)

# %%



