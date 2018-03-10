import os
import sys

path='Desktop/python/Test/sectionB/searchApp/searchApp'

if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'searchApp.settings'

