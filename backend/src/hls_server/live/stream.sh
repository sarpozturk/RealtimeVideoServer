#!/bin/bash
VIDSOURCE="http://127.0.0.1:8081/live"
VIDEO_OPTS="-s 640x480 -c:v libx264 -b:v 800000"
OUTPUT_HLS="-hls_time 10 -hls_list_size 10 -start_number 1"
ffmpeg -i "$VIDSOURCE" -y $VIDEO_OPTS $OUTPUT_HLS stream.m3u8