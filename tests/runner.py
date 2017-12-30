#!/usr/bin/python
import unittest2, os, sys

if __name__ == '__main__':

	testspath = os.path.realpath(os.path.dirname(__file__))
	basepath = os.path.realpath(testspath + '/../..')
	sys.path.append(basepath)

	print testspath, basepath
	import unittest2
	loader = unittest2.TestLoader()
	tests = unittest2.defaultTestLoader.discover(testspath)
	testRunner = unittest2.runner.TextTestRunner()
	testRunner.run(tests)
