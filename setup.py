from setuptools import setup, find_packages

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except FileNotFoundError:
        return 'DomainIntel is a tool for gathering various types of information about domains.'

setup(
    name='domainintel',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'whois',
        'pyopenssl',
        'dnspython',
        'tldextract',
        # add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'domainintel=domainintel.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool for gathering domain information',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/domainintel',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
