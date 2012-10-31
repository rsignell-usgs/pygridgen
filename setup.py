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

gridgen = Extension(name = '_gridgen',
                    extra_compile_args=['-O2', ],
                    sources=["pygridgen/src/csa.c",
                             "pygridgen/src/svd.c",
                             "pygridgen/src/delaunay.c",
                             "pygridgen/src/hash.c",
                             "pygridgen/src/istack.c",
                             "pygridgen/src/lpi.c",
                             "pygridgen/src/minell.c",
                             "pygridgen/src/nnai.c",
                             "pygridgen/src/nnbathy.c",
                             "pygridgen/src/nncommon.c",
                             "pygridgen/src/nncommon-vulnerable.c",
                             "pygridgen/src/nnpi.c",
                             "pygridgen/src/preader.c",
                             "pygridgen/src/triangle.c",
                             "pygridgen/src/gridmap.c",
                             "pygridgen/src/gucommon.c",
                             "pygridgen/src/poly.c",
                             "pygridgen/src/broyden.c",
                             "pygridgen/src/geom.c",
                             "pygridgen/src/gridgen.c",
                             "pygridgen/src/gridnodes.c",
                             "pygridgen/src/issimplepoly.c",
                             "pygridgen/src/ode.c",
                             "pygridgen/src/swcr.c",
                             "pygridgen/src/vertlist.c",
                             "pygridgen/src/zode.c",])

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
          # ext_modules = [gridgen],
          ext_modules = [csa], 
          classifiers = filter(None, classifiers.split("\n")),
          )
    
