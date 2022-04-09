# from pathlib import Path
# from PIL import Image
# path = input("enter a path of images")

# images = [
#     Image.open(path+"/" + f)
#     for f in ["Aclonica.png", "Amatic sc.png", "Arial.png"]
# ]

# pdf_path = input("enter a pdf path")

# images[0].save(
#     pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
# )

# from PIL import Image

# png = Image.open(object.logo.path)
# png.load() # required for png.split()

# background = Image.new("RGB", png.size, (25, 25, 25))
# background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
# from PIL import Image

# im1 = Image.open('/home/jija/Desktop/imagesononepagepdf/images/Aclonica.png')
# im2 = Image.open('/home/jija/Desktop/imagesononepagepdf/images/Aclonica.png')

# def get_concat_h_repeat(im, column):
#     dst = Image.new('RGB', (im.width * column, im.height))
#     for x in range(column):
#         dst.paste(im, (x * im.width, 0))
#     return dst

# def get_concat_v_repeat(im, row):
#     dst = Image.new('RGB', (im.width, im.height * row))
#     for y in range(row):
#         dst.paste(im, (0, y * im.height))
#     return dst

# def get_concat_tile_repeat(im, row, column):
#     dst_h = get_concat_h_repeat(im, column)
#     return get_concat_v_repeat(dst_h, row)

# im_s = im1.resize((im1.width // 2, im2.height // 2))
# get_concat_tile_repeat(im_s, 4, 2).save('/home/jija/Desktop/imagesononepagepdf/images/pillow_concat_tile_repeat.pdf')