import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inkit", # Replace with your own username
    version="1.0.2",
    author="Inkit Inc",
    author_email="support@inkit.com",
    description="The world's leading Reach Enablement Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inkitio/inkit-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'inkit = inkit.main:main',
        ],
    },
    python_requires='>=3.6',
)