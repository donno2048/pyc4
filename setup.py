from setuptools import setup, Extension
setup(
    name='pyc4',
    version='1.0.0',
    license='GPL-2.0',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description='A Python extension to run C code in Python',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/pyc4',
    project_urls={
        'Documentation': 'https://github.com/donno2048/pyc4#readme',
        'Bug Reports': 'https://github.com/donno2048/pyc4/issues',
        'Source Code': 'https://github.com/donno2048/pyc4'
    },
    ext_modules=[Extension('c4', ['c4.c'])],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
    zip_safe = False,
)