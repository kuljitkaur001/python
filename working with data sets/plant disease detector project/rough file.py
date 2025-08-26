from fontTools.ttLib import TTFont

font = TTFont("C:\\Users\\hp\\OneDrive\\python\\python\\FONTS\\Raajaa-Black.ttf")

# Blank out dottedcircle if present
if "glyf" in font and "dottedcircle" in font["glyf"].glyphs:
    g = font["glyf"].glyphs["dottedcircle"]
    g.coordinates = []
    g.endPtsOfContours = []
    g.flags = []
    print("✔ dottedcircle glyph blanked")

font.save("Raajaa-Black_fixed.ttf")
print("✔ Font saved as Raajaa-Black_fixed.ttf")
