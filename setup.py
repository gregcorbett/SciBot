from distutils.core import setup
import py2exe
 
setup(
	windows=['runSciBot.py'],
	options={
		"py2exe":{
			"bundle_files": 0,
			"dist_dir":"."
		},
	},
	zipfile=None,
	
)