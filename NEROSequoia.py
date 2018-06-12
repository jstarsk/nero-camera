# !/usr/bin/env python
from ptpy import PTPy
from ptpy.transports.ip import IPTransport
from argparse import ArgumentParser
from time import time, sleep
import os
import shutil
import errno
import serial


class NEROSequoia:

    @staticmethod
    def trigger_camera():
        camera = PTPy()

        with camera.session():
            capture = camera.initiate_capture()
            print (capture)
            evt = camera.event()
            if evt:
                print(evt)
            print ("-------")

    @staticmethod
    def trigger_camera_wifi():
        # Default PTP/IP port assumed
        c = PTPy(transport=IPTransport, device='197.168.47.1')

        # Optionally:
        # c = PTPy(transport=IPTransport, device=('197.168.47.1', 15740))
        print (c)

    @staticmethod
    def time_lapse_sequoia(ms=6):

        parser = ArgumentParser()
        parser.add_argument(
            '-t',
            type=float,
            help='Time between captures in seconds. Default is 0.1 seconds.'
        )
        parser.add_argument(
            '-n',
            type=int,
            help='Number of captures. Negative numbers mean "forever" (default)'
        )
        args = parser.parse_args()

        camera = PTPy()
        with camera.session():
            successful = 0
            beginning = time()
            while True if args.n is None or args.n < 0 else successful < args.n:
                capture = camera.initiate_capture()
                if capture.ResponseCode == 'OK':
                    successful += 1
                    cumulative_rate = (time() - beginning) / (successful)
                    print('elapsed {:.2f}s cumulative rate {:.2f}s captured {}'.format(
                        time() - beginning,
                        cumulative_rate,
                        successful
                    ))
                    sleep(ms if args.t is None else args.t)

    @staticmethod
    def time_lapse_trigger_cameras(ms=1):
        parser = ArgumentParser()
        parser.add_argument(
            '-t',
            type=float,
            help='Time between captures in seconds. Default is 0.1 seconds.'
        )
        parser.add_argument(
            '-n',
            type=int,
            help='Number of captures. Negative numbers mean "forever" (default)'
        )
        args = parser.parse_args()

        camera = PTPy()
        with camera.session():
            successful = 0
            beginning = time()
            while True if args.n is None or args.n < 0 else successful < args.n:
                capture = camera.initiate_capture()
                if capture.ResponseCode == 'OK':
                    successful += 1
                    cumulative_rate = (time() - beginning) / (successful)
                    print('elapsed {:.2f}s cumulative rate {:.2f}s captured {}'.format(
                        time() - beginning,
                        cumulative_rate,
                        successful
                    ))
                    NEROSequoia.trigger_flirVuePro()
                    sleep(ms if args.t is None else args.t)

    @staticmethod
    def trigger_flirVuePro(counter=1, _port="/dev/ttyUSB0", _baudrate=9600, _timeout=1):

        ser = serial.Serial(_port, baudrate=_baudrate, timeout=_timeout)

        while 1:
            ser.write(b'1')
            serial_line = ser.readline().decode("ascii")
            if len(serial_line) > 0:
                try:
                    _capture = int(serial_line)
                    if _capture >= counter:
                        break
                except ValueError:
                    print(str.format("capturing | {0}", serial_line))
        return _capture

    @staticmethod
    def sort_folder_sequoia(source_path):

        save_path = "/SORT"
        file_extension_tiff_folder = "/TIF"
        file_extension_jpg_folder = "/JPG"

        directory = os.listdir(source_path)
        print (directory)
        pictures = []

        try:
            os.makedirs(os.path.join(source_path + save_path))
            os.makedirs(os.path.join(source_path + save_path + file_extension_tiff_folder))
            os.makedirs(os.path.join(source_path + save_path + file_extension_jpg_folder))

        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        for i in directory:

            i_path = source_path + "/" + i

            if os.path.isdir(i_path):

                i_dir = os.listdir(i_path)

                for j in i_dir:

                    j_path = i_path + "/" + j

                    if not os.path.isdir(j_path):

                        file_name = j_path.split("_")

                        for p in file_name:

                            if p == "GRE.TIF":
                                pictures.append(j_path)
                                folder_name = i_path.split("/")[-1]

                                gre_path = source_path + save_path + file_extension_tiff_folder + "/"

                                gre_path = gre_path + j
                                print gre_path

                                shutil.copy2(j_path, gre_path)

                            elif p == "NIR.TIF":
                                pictures.append(j_path)
                                folder_name = i_path.split("/")[-1]

                                nir_path = source_path + save_path + file_extension_tiff_folder + "/"
                                nir_path = nir_path + j
                                print nir_path

                                shutil.copy2(j_path, nir_path)

                            elif p == "RED.TIF":
                                pictures.append(j_path)
                                folder_name = i_path.split("/")[-1]

                                red_path = source_path + save_path + file_extension_tiff_folder + "/"
                                red_path = red_path + j
                                print red_path

                                shutil.copy2(j_path, red_path)

                            elif p == "RGB.JPG":
                                pictures.append(j_path)
                                folder_name = i_path.split("/")[-1]

                                rgb_path = source_path + save_path + file_extension_jpg_folder + "/"
                                rgb_path = rgb_path + j
                                print rgb_path

                                shutil.copy2(j_path, rgb_path)
