from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A conversion package'
LONG_DESCRIPTION = 'A package that makes it easy to convert values between several units of measurement'

setup(
    name="conversn",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="amisha2515",
    author_email="amishanaik.te19@bmsce.ac.in",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
