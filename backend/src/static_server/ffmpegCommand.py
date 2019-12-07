import os

os.system(
    "ffmpeg -f dshow -i video=\"HD WebCam\":audio=\"Microphone Array (Realtek High Definition Audio)\" -vcodec libx264 -segment_time 2 -f rtsp rtsp://10.200.106.78:1935/rtmp/teststr.sdp")
