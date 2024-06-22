from PIL import Image, ImageDraw, ImageFont


image_path = "_.jpg"
image = Image.open(image_path)
bw_image = image.convert("RGBA")
width, height = bw_image.size
text_layer = Image.new("RGBA", (width, height), (255, 255, 255, 0))
text = ""
font_size = 600
font = ImageFont.truetype("arialbd.ttf", font_size)

draw = ImageDraw.Draw(text_layer)
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0, int(255 * 0.93)))
bw_image_with_alpha = bw_image.convert("RGBA")
final_image = Image.alpha_composite(bw_image_with_alpha, text_layer)
final_image_rgb = final_image.convert("RGB")
final_image_rgb.save("_.png")
final_image_rgb.show()
