from setuptools import setup

with open("requirements.txt") as req_file:
    requirements: list = req_file.readlines()

setup(
    name='nightwatch',
    version='0.0.1',
    packages=['nightwatch'],
    author="Michal Polovka",
    author_email="mpolovka@redhat.com",
    description="Helper tool for checking and reporting PR-CI nightly runs",
    platforms=["linux"],
    license="GPL",
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'nightwatch = nightwatch.__main__:main'
        ]
    }
)
