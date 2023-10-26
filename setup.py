from setuptools import setup

setup(
    name="wkhtmltopdf-pack",
    version="0.12.3.0.post1",
    url="https://github.com/illarra/wkhtmltopdf-pack",
    author="illarra",
    author_email="team@illarra.com",
    license="MIT",
    data_files=[
        (
            "bin",
            [
                "bin/wkhtmltopdf-pack",
                # "bin/wkhtmltopdf-mod",
                "bin/wkhtmltopdf-centos",
                "lib/libwkhtmltox.so",
                "lib/libjpeg.so.62",
                "lib/libXrender.so.1",
                "lib/libXext.so.6",
                "lib/libX11.so.6",
                "lib/libxcb.so.1",
                "lib/libXau.so.6",
                # "lib/libwkhtmltox.so.0",
                # "lib/libwkhtmltox.so.0.12",
                # "lib/libwkhtmltox.so.0.12.6",
            ],
        )
    ],
    description="wkhtmltopdf 0.12.3.0 for Python on Heroku buildpacks",
    long_description=open("README.rst").read(),
    keywords="pdf wkhtmltopdf paas heroku cloudcontrol buildpack",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
