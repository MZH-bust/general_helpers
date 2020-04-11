import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='genutil',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=['genutil'],
    include_package_data=True,
    url='https://github.com/MZH-bust/general_helpers',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    author='martin.zoeltsch',
    author_email='',
    description="Übergreifende Hilfsfunktionen",
    long_description=README,
    entry_points={
        "console_scripts": [
            "genutil=genutil.__main__:main",
        ]
    },
    install_requires=[]
)
