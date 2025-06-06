# aufgaben wie konvertieren

import subprocess


def convert_480p(source):
    target = source + "_480.mp4"
    cmd = "{}{}".format(source, target)
    subprocess.run(cmd)
