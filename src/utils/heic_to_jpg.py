import os
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener

register_heif_opener()  # lets Pillow open .HEIC files


def convert_folder(src_dir, dst_dir):
    """Convert every .HEIC image in src_dir to an upright .jpg in dst_dir."""
    os.makedirs(dst_dir, exist_ok=True)
    for name in sorted(os.listdir(src_dir)):
        if name.lower().endswith(".heic"):
            img = ImageOps.exif_transpose(Image.open(os.path.join(src_dir, name)))
            out_name = os.path.splitext(name)[0] + ".jpg"
            img.convert("RGB").save(os.path.join(dst_dir, out_name), quality=95)


if __name__ == "__main__":
    convert_folder("data/joe_phone_raw_3_15", "data/joe_phone_jpgs_3_15")
