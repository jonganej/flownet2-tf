from setuptools import setup
from setuptools import find_packages

setup(name='flownet2',
      version='0.1',
      description='FlowNet2 for Tensorflow',
      license='MIT',
      packages=find_packages('src'),
      # package_dir={'tinkerflow', '.'},
			package_dir={'':'src'},
      install_requires=['numpy', 'scipy', 'pypng', 'image'],
      include_package_data=True,
      zip_safe=False)
