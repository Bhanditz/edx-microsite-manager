import os
from setuptools import setup, find_packages


def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

setup(
    name='edx-microsite-manager',
    version='0.1',
    description='UI for configuring edX microsites',
    license='Affero GNU General Public License v3 (GPLv3)',
    url="https://github.com/jazkarta/edx-microsite-manager",
    author="David Glick, Jazkarta",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    package_data=package_data("edx_microsite_manager", ["static", "templates"]),
)
