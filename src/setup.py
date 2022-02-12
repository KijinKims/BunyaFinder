import setuptools

setuptools.setup(
    name='bunyafinder',
    version='1.0',
    scripts=['./scripts/bunyafinder'],
    author='Kijin Kim',
    description='BunyaFinder',
    packages=['bunyafinder'],
    install_requires=[
        'setuptools',
        'requests',
        'biopython',
        'wget',
    ],
    include_package_data=True
)
