from setuptools import setup, find_packages

setup(
    name='webhook',
    version='1.0',
    packages=find_packages(),
    description='A simple Python package to send webhooks using requests',
    author='Kevin Alexander Krefting',
    author_email='linuxandtermux@gmail.com.',
    url='https://github.com/termuxandlinux/webhook',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests',
    ],
)
