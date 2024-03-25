import boto3
import botocore.exceptions
import os
import io


def connect_s3():
    s3_token = os.getenv("CLOUDFLARE_S3_token_id")
    s3_secret = os.getenv("cloudflare_s3_token_secret")
    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
    bucket_id = os.getenv("s3_bucket_id")
    s3 = boto3.resource(service_name="s3",
                        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com/",
                        aws_access_key_id=s3_token,
                        aws_secret_access_key=s3_secret
                        )
    return bucket_id, s3


def upload_s3(from_dir=None, to_dir=None):
    if from_dir is None:
        from_dir = "public/zips"
    if to_dir is None:
        to_dir = "zips"

    bucket_id, s3 = connect_s3()

    for item in os.listdir(from_dir):
        with io.FileIO(f"{from_dir}/{item}") as file:
            remote_file = s3.ObjectSummary(bucket_name=bucket_id, key=f'{to_dir}/{item}').Object()
            try:
                remote_file.load()
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                    remote_file.put(Body=file)
                    print(f"uploaded {to_dir}/{item}")
                else:
                    raise e
            else:
                # TODO better check if file has changed and upload.
                if remote_file.content_length != os.stat(f"{from_dir}/{item}").st_size:
                    remote_file.put(Body=file)
                    print(f"uploaded {to_dir}/{item}")

                print(f"skipping {to_dir}/{item}")



def download_static_refs():
    bucket_id, s3 = connect_s3()
    for item in s3.Bucket(name=bucket_id).objects.all():
        if not f"{item.key}".startswith("content"):
            continue
        path = f"{item.key}"
        s3_file = item.get()["Body"]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with io.FileIO(path, "w") as local_file:
            for i in s3_file:
                local_file.write(i)
