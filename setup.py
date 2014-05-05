"""Gridgen is a tool for creating curvilinear grids.

Requires:
    NumPy (http://numpy.scipy.org)
    matplotlib with the Basemap toolkit (http://matplotlib.sourceforge.net)
"""

classifiers = """\
Development Status :: beta
Environment :: Console
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: MIT
Operating System :: OS Independent
Programming Language :: Python
Topic :: Scientific/Engineering
Topic :: Software Development :: Libraries :: Python Modules
"""

from numpy.distutils.core import Extension

csa = Extension(name = '_csa',
                sources=["pygridgen/src/csa/csa.c",
                         "pygridgen/src/csa/svd.c"])

doclines = __doc__.split("\n")

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(name = "pygridgen",
          version = '0.1.0',
          description = doclines[0],
          long_description = "\n".join(doclines[2:]),
          author = "Robert Hetland",
          author_email = "hetland@tamu.edu",
          url = "http://pygridgen.googlecode.com/",
          packages = ['pygridgen'],
          license = 'BSD',
          platforms = ["any"],
          ext_package='pygridgen',
          ext_modules = [csa, ], 
          classifiers = filter(None, classifiers.split("\n")),
          )
    
