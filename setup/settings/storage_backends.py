from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = "e-commerce--assets"
    location = "media"
    custom_domain = "{}.s3.amazonaws.com".format(bucket_name)
    file_overwrite = False


class StaticStorage(S3Boto3Storage):
    bucket_name = "e-commerce-static"
    location = "static"
