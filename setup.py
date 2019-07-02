import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8")


# This call to setup() does all the work
setup(
    name="graphenex",
    version="1.0.0",
    description="Automated System Hardening Framework for Linux & Windows",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/grapheneX/grapheneX",
    author="Graphenex Team",
    author_email="graphenex.project@protonmail.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GPLv3 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["graphenex", "graphenex.core"],
    include_package_data=True,
    package_data={'',["modules.json"]},
    install_requires=["flask-socketio", "coloredlogs", "terminaltables", "pyinquirer"],
    entry_points={
        "console_scripts": [
            "graphenex=graphenex.__main__:main",
        ]
    },
)