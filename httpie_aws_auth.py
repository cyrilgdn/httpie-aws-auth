"""
AWS auth plugin for HTTPie.

"""
import os

import boto3
from httpie.plugins import AuthPlugin
from requests_aws4auth import AWS4Auth

__version__ = "0.0.3"
__author__ = "Jakub Roztocil"
__licence__ = "BSD"


class BytesHeadersFriendlyS3Auth(AWS4Auth):
    def __call__(self, r):
        for k, v in r.headers.items():
            if isinstance(v, bytes):
                # HTTPie passes bytes but S3Auth excepts text, so unless we
                # decode it here, the signature will be incorrect:
                # https://github.com/tax/python-requests-aws/blob/46f2e90ea48e18d8f32c6473fecdf0da4ef04847/awsauth.py#L104
                r.headers[k] = v.decode("utf8")
        return super(BytesHeadersFriendlyS3Auth, self).__call__(r)


class AWSAuthPlugin(AuthPlugin):
    name = "AWS auth"
    auth_type = "aws"
    description = ""
    auth_require = False
    prompt_password = False

    def get_auth(self, *args, **kwargs):
        credentials = boto3.Session().get_credentials()
        if not credentials:
            return ""

        return BytesHeadersFriendlyS3Auth(
            credentials.access_key,
            credentials.secret_key,
            os.getenv("AWS_REGION", "eu-central-1"),
            os.getenv("AWS_SERVICE", "es"),
            session_token=credentials.token,
        )
