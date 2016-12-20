from setuptools import setup, find_packages
import os

setup(name='cvc',
      version="0.1.0",
      description='Control Cozmo with your voice',
      url='https://github.com/rizal72/Cozmo-Apps',
      author='Riccardo Sallusti',
      author_email='riccardo.sallusti@gmail.com',
      license='GNU',
      packages=find_packages(),
      entry_points={
              'console_scripts': [
                  'cvc = cvc.cozmo_voice_commands:main',
              ]
          },
      include_package_data = True,
      install_requires=[
          "termcolor",
          "cozmo[camera]",
          "SpeechRecognition",
          "PyAudio",
      ],
      zip_safe=False)