from setuptools import setup

try:
    import multiprocessing
except ImportError:
    pass


setup(
    name="httpie-aws-auth",
    description="AWS/S3 auth plugin for HTTPie.",
    long_description=open("README.rst").read().strip(),
    version="0.0.3",
    author="Jakub Roztocil",
    author_email="jakub@roztocil.co",
    license="BSD",
    url="https://github.com/jkbrzt/httpie-aws-auth",
    download_url="https://github.com/jkbrzt/httpie-aws-auth",
    py_modules=["httpie_aws_auth"],
    zip_safe=False,
    entry_points={
        "httpie.plugins.auth.v1": ["httpie_aws_auth = httpie_aws_auth:AWSAuthPlugin"]
    },
    install_requires=["boto3>=1.17.0", "httpie>=2.4.0", "requests-aws4auth>=1.1.0"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Environment :: Plugins",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
    ],
)
