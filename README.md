# Facemask Detection

This repository contains 1 Python file and 2 HAAR Cascade Classifiers stored as XML files.

## Python

The Python file opens up your webcam feed and detects masked and unmasked faces. It requires the [numpy](https://numpy.org/install/) and [OpenCV](https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html) libraries to be installed prior to running. 

## XML

The classifier for faces is from the widely available [OpenCV for Python project](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).

Whereas, the mask classifier was trained by me using [UCI's Maching Learning Repository](https://archive.ics.uci.edu/ml/datasets/CMU+Face+Images).

## Compatibility

This program has only been tried and tested on a Windows device. Be wary of possible issues when running on a different OS.

## Credits

Big shout out to [Harrison Kinsley](https://twitter.com/Sentdex?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) (sentdex) for the helpful [HAAR Cascade training tutorials](https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq)!
