from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

#with open('LICENSE') as license_file:
    #license = license_file.read()

setup(name='email-forwarder',
      version='0.1.0',
      description='High level email forwarding in Python.',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/wesinator/email-forwarder-python',
      author='wesinator',
      keywords='spam',
      packages=['email-forwarder'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
      ],
      zip_safe=True)
