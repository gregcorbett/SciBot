from distutils.core import setup
import py2exe
 
setup(
	windows=['runSciBot.py'],
	options={
		"py2exe":{
			"bundle_files": 1
		}
	}
)