import sys
import time
import argparse
from socket_server_test.socket_server import Video_Server, VideoClient

if __name__ == '__main__':
    vclient = VideoClient("127.0.0.1", 8080)
    vserver = Video_Server(8080)
    # vclient.start()
    vserver.start()
    while True:
        time.sleep(1)
        # if not vserver.isAlive() or not vclient.isAlive():
        if not vserver.isAlive():
            print("Video connection lost...")
            sys.exit(0)
