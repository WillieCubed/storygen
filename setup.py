"""A setuptools script to install this project's CLI and environment."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-project-template",
    version="0.1.0",
    author="Willie Chalmers III",
    author_email="willie@williecubed.me",
    description="A really cool AI project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://williecubed.github.io/ai-project-template",
    project_urls={
        "Bug Tracker": "https://github.com/WillieCubed/ai-project-template/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "aicli=ai_project_template.utils:run_cli",
        ]
    },
    packages=find_packages(),
    python_requires=">=3.8",
)