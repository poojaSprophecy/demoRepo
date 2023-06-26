from setuptools import setup, find_packages

setup(
    name='demoPip',
    version='1.0',
    packages=find_packages(include=['demopip*']),
    description='demoPip',
    install_requires=[
        'prophecy-libs==1.5.5'
    ],
    entry_points={
        'console_scripts': [
            'main = demopip.pipeline:main',
        ],
    },
    data_files=[(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require={
        'test': ['pytest', 'pytest-html'],
    }
)