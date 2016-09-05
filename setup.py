from setuptools import setup, find_packages

vftools_description = (
    u'A set of forensics tools for analyzing evidence files or devices using dfVFS.'
)

setup(
    name=u'vftools',
    version=u'0.1 Beta',
    descript=vftools_description,
    packages=find_packages(),
    include_package_data=True,
    url=u'https://github.com/maurermj08/vftools',
    license=u'Apache License Version 2.0',
    author=u'Michael Maurer',
    classifiers=[
        u'Development Status :: 4 - Beta',
        u'Environment :: Web Environment',
        u'Operating System :: OS Independent',
        u'Programming Language :: Python',
    ],
    scripts=[u'efetch'],
    zip_safe=False,
    install_requires=frozenset([u'argparse>=1.2.1',
                      u'dfvfs>=20150708',
                      u'elasticsearch>=2.1.0',
                      u'Jinja2>=2.1']),
    author_email=u'maurermj08@gmail.com',
)
