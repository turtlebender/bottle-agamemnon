from setuptools import setup

setup(
        name="bottle-agamemnon",
        version="0.1.0",
        url="http://github.com/turtlebender/bottle-agamemnon/",
        description="Agamemnon integration for bottle",
        author="Tom Howe",
        author_email = 'turtlebender@gmail.com',
        license="MIT",
        platforms="any",
        py_modules=["bottle_agamemnon"],
        install_requires= [
            'bottle>=0.9',
            'agamemnon>=0.4'
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
)
