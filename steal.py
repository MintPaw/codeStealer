def main(argv):
    import getopt
    url = ""

    try:
        opts, args = getopt.getopt(argv, "", ["url="])
    except getopt.GetoptError:
        print("Run with --url=http://mysite.com/myImage.png")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--url":
            url = arg

    import PIL
    from PIL import Image
    from PIL import ImageOps

    import pytesseract

    import urllib.request
    urllib.request.urlretrieve(url, "local.png")

    img = Image.open("local.png")
    img = ImageOps.grayscale(img)
    img = img.resize((img.width * 2, img.height * 2))
    text = pytesseract.image_to_string(
        img,
        None,
        False,
        "-c tessedit_char_whitelist=0123456789-ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    text += " "

    text += pytesseract.image_to_string(
        img,
        None,
        False,
        "-c tessedit_char_whitelist=0123456789-abcdefghijklmnopqrstuvqxyz")

    chunks = text.split()
    validChunks = list()

    for c in chunks:
        if c.count("-") == 2:
            validChunks.append(c)
        if c.count("-") == 4:
            validChunks.append(c)

    print("Possible keys:")
    for c in validChunks:
        print(c)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
