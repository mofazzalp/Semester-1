#\033[  Escape code, this is always the same
#1 = Style
#32 = Text colour, 32 for bright green.
#40m = Background colour, 40 is for black.
# changing the style (bold, normal, italics, underlined)
for style in (1,2,3,4):
    print(f"\033[{style};37;40m style = {style}")
# reset the colours
print("\033[0m")
# changing the font colour
for text in range(30, 38):
    print(f"\033[1;{text};48m style = {text}")
print("\033[0m")
# changing the background
for background in range(40, 49):
    print(f"\033[1;30;{background}m style = {background}")

print(f"\033[1;31;48mThe input is not correct.")
print("\033[0m")