
import boto3
import os
import io


def main(from_dir=None, to_dir=None):
    if from_dir is None:
        from_dir = "public/zips"
    if to_dir is None:
        to_dir = "zips"

    s3_token = os.getenv("CLOUDFLARE_S3_token_id")
    s3_secret = os.getenv("cloudflare_s3_token_secret")
    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
    bucket_id = os.getenv("s3_bucket_id")
    s3 = boto3.resource(service_name="s3",
                        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com/",
                        aws_access_key_id=s3_token,
                        aws_secret_access_key=s3_secret
                        )
    for item in os.listdir(from_dir):
        with io.FileIO(f"{from_dir}/{item}") as file:
            s3.ObjectSummary(bucket_name=bucket_id, key=f'{to_dir}/{item}').put(Body=file)


if __name__ == "__main__":
    cf_pages_branch = os.getenv("CF_PAGES_BRANCH")
    env_from_dir = os.getenv("local_static_src_dir")
    env_to_dir = os.getenv("cloudflare_target_dir")
    if cf_pages_branch == "master":
        print("uploading zips of references")
        main()
    elif env_from_dir and env_to_dir:
        print("uploading static references")
        main(from_dir=env_from_dir, to_dir=env_to_dir)
    else:
        print(f"Skipping uploads (CF_PAGES_BRANCH={cf_pages_branch})")
