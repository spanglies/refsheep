import os
import glob
import pathlib
import zipfile


def zipdir(path, zip_file_handle: zipfile.ZipFile, nsfw=False):
    root: str
    file: str
    for root, _, files in os.walk(path):
        for file in files:
            if file[-4:] not in [".jpg", ".png"]:
                continue

            if not nsfw:
                if "nsfw" in file.lower() or "nsfw" in root.lower():
                    continue
            zip_file_handle.write(os.path.join(root, file),
                                  os.path.relpath(os.path.join(root, file),
                                                  os.path.join(path, '..')))


def main():
    characters = glob.glob("content/*/")
    if characters:
        pathlib.Path("static/zips/").mkdir(parents=True, exist_ok=True)
    for character_path in characters:
        character_name = character_path.replace("content/", "").strip("/ ")
        if glob.glob(f"{character_path}*nsfw"):
            with zipfile.ZipFile(f"static/zips/{character_name}_nsfw.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipdir(path=character_path, zip_file_handle=zipf, nsfw=True)
        with zipfile.ZipFile(f"static/zips/{character_name}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipdir(path=character_path, zip_file_handle=zipf)


if __name__ == "__main__":
    main()
