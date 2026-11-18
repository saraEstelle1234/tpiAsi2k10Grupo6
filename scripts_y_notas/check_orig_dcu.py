# -*- coding: utf-8 -*-
from PIL import Image

im_orig = Image.open('media_presentacion/page_9_img_0_32.png')
print("page_9_img_0_32 size:", im_orig.size, im_orig.mode)
print("page_9_img_0_32 corner pixel:", im_orig.getpixel((0,0)))

im_pdf = Image.open('media_presentacion/rendered_page_9.png')
print("rendered_page_9 size:", im_pdf.size, im_pdf.mode)
print("rendered_page_9 corner pixel:", im_pdf.getpixel((0,0)))
