from setuptools import setup

setup(
    name='off-your-rocker',
    version='0.1.0',
    packages=['off_your_rocker'],
    package_data={'off_your_rocker': ['templates/*.em']},
    author='Shane Loretz',
    author_email='shane.loretz@gmail.com',
    description='Plugins for rocker that I find useful',
    license='Apache 2.0',
    install_requires=[
        # 'git+https://github.com/tfoote/rocker.git',
    ],
    entry_points={
        'rocker.extensions': [
            'colcon = off_your_rocker.colcon:Colcon',
            'spacenav = off_your_rocker.spacenav:SpaceNav',
        ]
    }
)