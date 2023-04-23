import json
import os
import platform
import time

import cv2
import threading


class Pipeline(object):

    def __init__(self):
        self.multi_camera = True
        # multi camera -> ids or paths
        self.input = [0, 1]

        if self.multi_camera:
            self.predictor = []
            for name in self.input:
                predictor_item = CameraThread() #is_video=True, multi_camera=True
                #predictor_item.set_file_name(name)
                self.predictor.append(predictor_item)


    def run_multithreads(self):
        import threading
        if self.multi_camera:
            multi_res = []
            threads = []
            for idx, (predictor, input) in enumerate(zip(self.predictor, self.input)):
                print(idx)
                thread = threading.Thread(
                    name=str(idx).zfill(3),
                    target=predictor.run,
                    args=(input, idx))
                threads.append(thread)

            for thread in threads:
                thread.start()

            for predictor, thread in zip(self.predictor, threads):
                thread.join()

                # results

        else:
            self.get_frame.run(self.input)


class CameraThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.source = 0  # file/dir/URL/glob, 0 for webcam
        #self.source = 'test_videos/4.mp4'
        self.cap = cv2.VideoCapture(self.source)


        self.stop_thread = False

    def run(self):
        while not self.stop_thread:
            ret, frame = self.cap.read()
            if ret:
                DetectionThread.frame = frame.copy()

    def stop(self):
        self.cap.release
        self.stop_thread = True

if __name__ == '__main__':
    main = Pipeline()
    main.run_multithreads()