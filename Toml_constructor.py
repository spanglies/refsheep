import os
branch = os.getenv("CF_PAGES_BRANCH")
page_url = os.getenv("CF_PAGES_URL")

if __name__ == "__main__":
    with open("config.base.toml") as base:
        with open("config.toml", "w") as newconfig:
            if page_url is None or branch == "master":
                with open("base_url") as base_url_file:
                    newconfig.writelines(base_url_file.readlines())
            else:
                newconfig.write(f"base_url = \"{page_url}\"\n")

            newconfig.writelines(base.readlines())
