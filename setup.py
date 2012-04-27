from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
        name="bottle-agamemnon",
        version="0.0.1",
        url="http://github.com/turtlebender/bottle-agamemnon/",
        description="Agamemnon integration for bottle",
        author="Tom Howe",
        author_email = 'turtlebender@gmail.com',
        license="MIT",
        platforms="any",
        py_modules=["bottle_agamemnon"],
        requires= [
            'bottle (>=0.9)',
            'agamemnon (>=0.4)'
            ],
        classifiers = [
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        cmdclass = {'build_py': build_py}
)
