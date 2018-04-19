from setuptools import setup
from setuptools import find_packages

setup(name='flownets',
      version='0.1',
      description='FlowNet2 for Tensorflow',
      license='MIT',
			package_dir={'flownets':'src'},
			packages=['flownets', 'flownets.flownet2', 'flownets.flownet_c', 'flownets.flownet_cs', 'flownets.flownet_css', 'flownets.flownet_s', 'flownets.flownet_sd'],
      install_requires=['numpy', 'scipy', 'pypng', 'image'],
      include_package_data=True,
      zip_safe=False)
