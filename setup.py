import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="escape_game"
    version="0.0.1",
    author="Julio Pochet Edmead",
    author_email="jpe3841@gmail.com",
    url="https://github.com/jpochetedmead/Flask-Adventure-Game",
    description="escape_game app configured to be deployed to Heroku",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
