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
                    sources=["octant/src/gridgen/csa.c",
                             "octant/src/gridgen/svd.c",
                             "octant/src/gridgen/delaunay.c",
                             "octant/src/gridgen/hash.c",
                             "octant/src/gridgen/istack.c",
                             "octant/src/gridgen/lpi.c",
                             "octant/src/gridgen/minell.c",
                             "octant/src/gridgen/nnai.c",
                             "octant/src/gridgen/nnbathy.c",
                             "octant/src/gridgen/nncommon.c",
                             "octant/src/gridgen/nncommon-vulnerable.c",
                             "octant/src/gridgen/nnpi.c",
                             "octant/src/gridgen/preader.c",
                             "octant/src/gridgen/triangle.c",
                             "octant/src/gridgen/gridmap.c",
                             "octant/src/gridgen/gucommon.c",
                             "octant/src/gridgen/poly.c",
                             "octant/src/gridgen/broyden.c",
                             "octant/src/gridgen/geom.c",
                             "octant/src/gridgen/gridgen.c",
                             "octant/src/gridgen/gridnodes.c",
                             "octant/src/gridgen/issimplepoly.c",
                             "octant/src/gridgen/ode.c",
                             "octant/src/gridgen/swcr.c",
                             "octant/src/gridgen/vertlist.c",
                             "octant/src/gridgen/zode.c",])

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
          ext_modules = [gridgen],
          classifiers = filter(None, classifiers.split("\n")),
          )
    
