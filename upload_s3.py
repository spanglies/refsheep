from common import *


if __name__ == "__main__":
    cf_pages_branch = os.getenv("CF_PAGES_BRANCH")
    env_from_dir = os.getenv("local_static_src_dir")
    env_to_dir = os.getenv("cloudflare_target_dir")
    if cf_pages_branch == "master":
        print("uploading zips of references")
        upload_s3()
    elif env_from_dir and env_to_dir:
        print("uploading static references")
        upload_s3(from_dir=env_from_dir, to_dir=env_to_dir)
    else:
        print(f"Skipping uploads (CF_PAGES_BRANCH={cf_pages_branch})")
