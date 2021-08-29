from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
    packages=['da_tangible_tasks'],
    package_dir={'': 'src'}
)
setup(**d)
