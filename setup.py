from setuptools import setup, find_packages

LONG_DESC = """
Data science shortcuts is a set of useful funcitons to save the time on opening files, cache, transforming data, etc
"""

setup(
    name='dshortcuts',
    version='0.0.2',
    long_description=LONG_DESC,
    url='https://github.com/Codealist/dshortcuts',
    author='Dmytro Samchuk',
    author_email='dvsamchuk@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['geopandas', 'scipy'],
    python_requires='>=3.5'
)
