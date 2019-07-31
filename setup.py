import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="graphenex",
    version="1.1.1",
    description="Automated System Hardening Framework for Linux & Windows",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/grapheneX/grapheneX",
    author="Graphenex Team",
    author_email="graphenex.project@protonmail.com",
    license="GPLv3",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    packages=[
        "graphenex", 
        "graphenex.core", 
        "graphenex.core.web", 
        "graphenex.core.cli", 
        "graphenex.core.hrd", 
        "graphenex.core.utils"
    ],
    include_package_data=True,
    install_requires=["flask-socketio", "coloredlogs", "colorama", "terminaltables", "pyinquirer"],
    entry_points={
        "console_scripts": [
            "grapheneX=graphenex.__main__:main",
        ]
    },
)
