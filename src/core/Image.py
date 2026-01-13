import base64
from PIL import Image


def encode_64(img_path):
    with open(img_path, 'rb') as image_file:
        data = base64.b64encode(image_file.read()).decode('utf_8')

    return data


def fill(img_path, container_res):
    image = Image.open(img_path)
    new_image = Image.new('RGBA', (container_res, container_res), (0, 0, 0, 0))

    if not image.size[0] > container_res and not image.size[1] > container_res:
        top = (container_res - image.size[1]) // 2
        left = (container_res - image.size[0]) // 2
    else:
        y_crop = (image.size[1] - container_res) // 2
        x_crop = (image.size[0] - container_res) // 2
        image = image.crop((x_crop, y_crop, x_crop + container_res, y_crop + container_res))
        top = 0
        left = 0

    new_image.paste(image, (left, top))

    return new_image


def fill_with_bg(img_path, bg_img_path, container_res):
    image = Image.open(img_path)
    image_bg = Image.open(bg_img_path)

    new_image = Image.new('RGBA', (container_res, container_res), (0, 0, 0, 0))

    new_width = int(container_res / 2)
    new_height = new_width * image_bg.size[1] // image_bg.size[0]

    image = image.resize((new_width, new_height), resample=Image.ANTIALIAS)

    top = (container_res - image.size[1]) // 2
    left = (container_res - image.size[0]) // 2

    if not image_bg.size[0] > container_res and not image_bg.size[1] > container_res:
        top_bg = (container_res - image_bg.size[1]) // 2
        left_bg = (container_res - image_bg.size[0]) // 2
    else:
        y_crop_bg = (image_bg.size[1] - container_res) // 2
        x_crop_bg = (image_bg.size[0] - container_res) // 2
        image_bg = image_bg.crop((x_crop_bg, y_crop_bg, x_crop_bg + container_res, y_crop_bg + container_res))
        top_bg = 0
        left_bg = 0

    image_bg.paste(image, (left, top), image)
    new_image.paste(image_bg, (left_bg, top_bg))
    # new_image.paste(image, (left, top))

    return new_image


def adjust(img_path, container_res, img_res):
    image = Image.open(img_path)
    image = image.convert('RGBA')
    width, height = image.size

    new_width = img_res
    new_height = new_width * height // width

    image = image.resize((new_width, new_height), resample=Image.ANTIALIAS)

    new_image = Image.new('RGBA', (container_res, container_res), (0, 0, 0, 0))

    top = (container_res - image.size[1]) // 2
    left = (container_res - image.size[0]) // 2

    new_image.paste(image, (left, top))

    return new_image


def adjust_with_bg(img_path, bg_img_path, container_res, img_res):
    image = Image.open(img_path)
    image = image.convert('RGBA')

    bg_image = Image.open(bg_img_path)
    bg_image = bg_image.convert('RGBA')

    image_width, image_height = image.size
    bg_image_width, bg_image_height = bg_image.size

    new_width = img_res
    new_height = new_width * image_height // image_width
    new_bg_image_width = int(container_res)
    new_bg_image_height = int(new_bg_image_width * bg_image_height // bg_image_width)

    image = image.resize((new_width, new_height), resample=Image.ANTIALIAS)
    bg_image = bg_image.resize((new_bg_image_width, new_bg_image_height), resample=Image.ANTIALIAS)

    new_image = Image.new('RGBA', (container_res, container_res), (0, 0, 0, 0))

    top = (container_res - image.size[1]) // 2
    left = (container_res - image.size[0]) // 2
    bg_top = (container_res - bg_image.size[1]) // 2
    bg_left = (container_res - bg_image.size[0]) // 2

    new_image.paste(bg_image, (bg_left, bg_top))
    new_image.paste(image, (left, top))

    return new_image


def save(path, image):
    image.save(path)


def close(image: Image):
    image.close()


def color_image(image, img_path):
    pixdata = image.load()

    width, height = image.size
    for y in range(height):
        for x in range(width):
            if int(pixdata[x, y][3]) == 0:
                pixdata[x, y] = (20, 221, 177, 255)
    image.save(img_path, "PNG")
    image = Image.open(img_path)
    image = image.convert('RGBA')
