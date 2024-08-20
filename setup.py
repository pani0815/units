from distutils.core import setup
setup(
<<<<<<< HEAD
  name = 'units_pani',         # How you named your package folder (MyLib)
  packages = ['units_pani'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='GNU GENERAL PUBLIC LICENSE',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
=======
  name = 'units',         # How you named your package folder (MyLib)
  packages = ['units'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
>>>>>>> parent of 8be40d6 (changed name)
  description = 'units',   # Give a short description about your library
  author = 'Dominik Panstingl',                   # Type in your name
  author_email = 'dominik.panstingl@gmx.at',      # Type in your E-Mail
  url = 'https://github.com/pani0815/units',   # Provide either the link to your github or to your website
<<<<<<< HEAD
  download_url = 'https://github.com/pani0815/units/archive/refs/tags/0.2.tar.gz',    # I explain this later on
=======
  download_url = 'https://github.com/pani0815/units/archive/refs/tags/0.0.tar.gz',    # I explain this later on
>>>>>>> parent of 8be40d6 (changed name)
  keywords = ['units', 'physics'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License: GPL version 3, excluding DRM provisions',   # Again, pick a license

    'Programming Language :: Python :: 3.11',
  ],
)