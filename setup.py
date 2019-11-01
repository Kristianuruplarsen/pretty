from setuptools import setup

setup(name='pretty',
      version='0.1',
      description='Updates the default theme in matplotlib',
      url='http://github.com/KristianUrupLarsen/pretty',
      author='Kristian Urup Olesen Larsen',
      license='MIT',
      include_package_data=True,
      packages=['pretty'],
      install_requires=[
        'matplotlib'      
      ],
      zip_safe=False)
