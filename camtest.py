# MIT License
# Copyright (c) 2019-2022 JetsonHacks

# Using a CSI camera (such as the Raspberry Pi Version 2) connected to a
# NVIDIA Jetson Nano Developer Kit using OpenCV
# Drivers for the camera and OpenCV are included in the base image

import cv2

# video/x-raw, format=YUY2, width=1280, height=720, framerate=30/1
"""
gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
Flip the image by setting the flip_method (most common values: 0 and 2)
display_width and display_height determine the size of each camera pane in the window on the screen
Default 1920x1080 displayd in a 1/4 size window
"""
def gstreamer_pipeline(
    sensor_id=2,
    capture_width=1920,
    capture_height=1080,
    display_width=320,
    display_height=180,
    framerate=30,
    flip_method=0,
):
    return (
            "v4l2src device=/dev/video%d ! "
            "video/x-raw, width=(int)1280, height=(int)720, framerate=(fraction)30/1 ! "
            "videoconvert ! "
            "videoscale ! video/x-raw, width=(int)320, height=(int)180 ! "
            "appsink"
        % (
            sensor_id,
        )
    )


def show_camera():
    window_title = "CSI Camera"

    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    print(gstreamer_pipeline(flip_method=0))
    video_capture = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
    if video_capture.isOpened():
        try:
            while True:
                ret_val, frame = video_capture.read()
                # Display the resulting frame
                cv2.imshow('frame', frame)
                #cv2.resizeWindow('frame', 100, 224)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")


if __name__ == "__main__":
    show_camera()
