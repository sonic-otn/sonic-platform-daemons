from setuptools import setup

setup(
    name='sonic-pmond',
    version='1.0',
    description='PMON daemon for SONiC',
    license='Apache 2.0',
    author='SONiC-OTN Team',
    author_email='sonic-wg-otn@lists.sonicfoundation.dev',
    url='https://github.com/zhengweitang-zwt/sonic-otn-platform-common',
    maintainer='xin lei',
    packages=[
        'tests'
    ],
    scripts=[
        'scripts/pmond',
    ],
    setup_requires=[
        'pytest-runner',
        'wheel'
    ],
    tests_require=[
        'pytest',
        'mock>=2.0.0',
        'pytest-cov'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Hardware',
    ],
    keywords='sonic SONiC daemon pmond',
    test_suite='setup.get_test_suite'
)
