import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="escape_game"
    version="0.0.1",
    author="your name",
    author_email="your@email.com",
    url="https://github.com/yourusername/escape_game",
    description="what does escape_game do?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
