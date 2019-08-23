"""
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
import setuptools

# Get the long description from the README file
with open('README.rst') as f:
    long_description = f.read()


setuptools.setup(
    name='dset',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Disjoint-Set implementation with heuristic optimizations (union-by-rank and path-compression)',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/Mr-Io/dset',
    author='Mr-Io',
    author_email='mrio.dev@gmail.com',
    py_modules=['dset',],
    python_requires='>=3.7',
    project_urls={
        'Bug Reports': 'https://github.com/Mr-Io/dset/issues',
        'Source':  'https://github.com/Mr-Io/dset',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
    ]
)
