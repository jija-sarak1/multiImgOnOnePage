
# from PIL import Image

# im1 = Image.open('/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home1.jpg')
# im3 = Image.open('/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home3.jpg')
# im5 = Image.open('/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home5.jpg')
# im7 = Image.open('/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home7.jpg')
# im16 = Image.open('/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home16.jpg')
# im14 = Image.open('/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home14.jpg')
# im12 = Image.open('/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home12.jpg')
# im10 = Image.open('/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home10.jpg')


# def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
#     min_height = min(im.height for im in im_list)
#     im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height),resample=resample)
#                       for im in im_list]
#     total_width = sum(im.width for im in im_list_resize)
#     dst = Image.new('RGB', (total_width, min_height))
#     pos_x = 0
#     for im in im_list_resize:
#         dst.paste(im, (pos_x, 0))
#         pos_x += im.width
#     return dst

# def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
#     min_width = min(im.width for im in im_list)
#     im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)),resample=resample)
#                       for im in im_list]
#     total_height = sum(im.height for im in im_list_resize)
#     dst = Image.new('RGB', (min_width, total_height))
#     pos_y = 0
#     for im in im_list_resize:
#         dst.paste(im, (0, pos_y))
#         pos_y += im.height
#     return dst

# def get_concat_tile_resize(im_list_2d, resample=Image.BICUBIC):
#     im_list_v = [get_concat_h_multi_resize(im_list_h, resample=resample) for im_list_h in im_list_2d]
#     return get_concat_v_multi_resize(im_list_v, resample=resample)

# get_concat_tile_resize([[im16, im1],
#                         [im14, im3],
#                         [im12, im5],
#                         [im10, im7]]).save('/home/jija/Desktop/imagesInApdf/outputPDF/pillow_concat_tile_resize.png')

from PIL import Image

image_1 = Image.open(r'/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home3.pdf')
image_2 = Image.open(r'/home/jija/Desktop/imagesInApdf/pdf2img/288-my-home2.pdf')

im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')

image_list = [im_2]

im_1.save(r'/home/jija/Desktop/imagesInApdf/outputPDF/288-my-home1.pdf', save_all=True, append_images=image_list)