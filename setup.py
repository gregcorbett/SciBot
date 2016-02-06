from distutils.core import setup
import py2exe




setup(
    console=['runSciBot.py'],
    #windows=['runSciBot.py'],
    #data_files=[("fonts/","./fonts/freesansbold.tff")],
    options={
        "py2exe":{
            "bundle_files": 0,
            "dist_dir":"."
            },
        },
    zipfile=None,

)
