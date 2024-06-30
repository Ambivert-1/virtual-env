from setuptools import setup, find_packages

setup(
    name="Weather_app",
    version="0.1.0",  # Corrected 'verion' to 'version'
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'weatherfetcher=weather_app.weatherfetcher:fetch_weather',
        ],
    },
    author="Pratima Budha Magar",
    author_email="magarpratima61@gmail.com",
    description="A simple weather fetching app",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

