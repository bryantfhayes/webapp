from setuptools import setup

setup(name='webapp',
      version='1.0.0',
      description='A python webapp template',
      url='http://github.com/bryantfhayes/webapp',
      author='Bryant Hayes',
      author_email='bryantfhayes@gmail.com',
      license='MIT',
      packages=['webapp'],
      dependency_links=[],
      install_requires=['flask'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)