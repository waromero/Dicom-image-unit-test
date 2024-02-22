#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name        : test_DcmImage.py
# Description : DICOM Image Unit Test.  
# Authors     : William A. Romero R. <contact@waromero.com>                                
#-------------------------------------------------------------------------------
import unittest
from igpokt.dcm import DcmImage 


INPUT_DCM_FILE_PATH = "./data/SD033.dcm"
SLICE_LOCATION = 31.9425961863641


class TestDcmImage(unittest.TestCase):
    """
    Test case for DICOM Image class.
    """
    def setUp(self):
        """
        Input file path.
        """
        self.image_path = INPUT_DCM_FILE_PATH


    def test_slice_location(self):
        """
        SliceLocation (0020,1041)
        """
        dicomImage = DcmImage(self.image_path)
        self.assertEqual(dicomImage.SliceLocation, 31.9425961863641)


if __name__ == '__main__':
    """
    Main test
    $ python -v ./test_DcmImage.py
    """
    unittest.main()


