from setuptools import setup


def read_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f.readlines()]


def read_readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='openPMD-updater',
    version='1.0.0',
    url='https://github.com/openPMD/openPMD-updater',
    # author=...,  # TODO
    # author_email=...,  # TODO
    # maintainer=...,  # TODO
    # maintainer_email=...,  # TODO
    license='ISC',
    install_requires=read_requirements(),
    description='updater ',
    long_description=read_readme(),
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    packages=['openpmd_updater'],
    entry_points={
        'console_scripts': [
            'openPMD_updater_h5 = openpmd_updater.cli:main'
        ]
    },
)
