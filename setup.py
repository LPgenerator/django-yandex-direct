from setuptools import setup, find_packages


setup(
    name='django-yandex-direct',
    version="1.0",
    description='Simple wrapper for the Yandex.Direct API',
    keywords="django yandex direct",
    long_description=open('README.rst').read(),
    author="GoTLiuM InSPiRiT",
    author_email='gotlium@gmail.com',
    url='https://github.com/LPgenerator/django-yandex-direct',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    zip_safe=False,
        install_requires=[
        'requests>=2.3.0',
        'simplejson>=2.2.1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
