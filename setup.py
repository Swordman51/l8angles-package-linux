from setuptools import setup
from setuptools.extension import Extension
import numpy
from Cython.Build import cythonize


NAME = "l8angles"
DESC = "Polymer atmospheric correction algorithm (http://dx.doi.org/10.1364/OE.19.009783)"
SRC_DIR = 'l8angles'
DEBUG=False
ANNOTATE=True


if DEBUG:
    compiler_directives = {
            'profile': True,
            'embedsignature': True,
            }
else:
    compiler_directives = {
            'boundscheck': False,
            'initializedcheck': False,
            'cdivision': True,
            'embedsignature': True,
            }

extensions = [
    Extension("l8angles", ["l8angles.pyx"],
              include_dirs= ["c_build", "src", "src/ias_lib", "build", numpy.get_include()],
              library_dirs= ['./c_build'],
              libraries=['l8_angles']
              )
]

EXTENSIONS = cythonize(
		       extensions,
		       #['l8angles.pyx'],
                       build_dir='build',
                       compiler_directives=compiler_directives,
                       annotate=ANNOTATE,
                         
                       )

setup(
    name = NAME,
    description = DESC,
    ext_modules = EXTENSIONS,
    #include_dirs = ["src", "src/ias_lib", "c_build", "build" ,numpy.get_include()],
    #package_dir={'c_build': './c_build'},
    #package_data={'c_build': ['*.so']},
    )

