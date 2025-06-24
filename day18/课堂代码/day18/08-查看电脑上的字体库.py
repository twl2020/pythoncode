from matplotlib.font_manager import FontManager

fm = FontManager()
my_fonts = set(f.name for f in fm.ttflist)
print(my_fonts)
