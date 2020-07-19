from setuptools import setup, find_packages

setup(
    name='dshortcuts',
    version='0.0.1',
    long_description='Data science shortcuts is a set of useful funcitons to save the time on opening files, cache, transforming data, etc',
    url='https://github.com/Codealist/dshortcuts',
    author='Dmytro Samchuk',
    author_email='dvsamchuk@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['pickle'],
    python_requires='>=3.5'
)
