with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_s12 = text.find('id="slide-12"')
pos_s13 = text.find('id="slide-13"')
s12 = text[pos_s12:pos_s13]
idx_img = s12.find('<img')
while idx_img != -1:
    print(s12[idx_img:idx_img+200])
    idx_img = s12.find('<img', idx_img+1)
