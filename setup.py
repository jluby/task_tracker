import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="task_tracker",
    version="0.0.0a0",
    author="Jack Luby",
    author_email="jack.o.luby@gmail.com",
    description="Personal task tracking package providing CLI tools and automation to more consistently track to-do's.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
