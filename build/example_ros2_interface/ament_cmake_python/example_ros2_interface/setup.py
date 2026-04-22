from setuptools import find_packages
from setuptools import setup

setup(
    name='example_ros2_interface',
    version='0.0.0',
    packages=find_packages(
        include=('example_ros2_interface', 'example_ros2_interface.*')),
)
