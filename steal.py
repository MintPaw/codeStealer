def main():
    try:
        import Image
    except ImportError:
        from PIL import Image

    import pytesseract

    import urllib.request
    urllib.request.urlretrieve("https://i.imgur.com/GqvByp6.png", "local.png")

    img = Image.open('local.png')
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
    steamChunks = list()
    originChunks = list()

    for c in chunks:
        if c.count("-") == 2:
            steamChunks.append(c)
        if c.count("-") == 4:
            originChunks.append(c)

    print("Possible Steam Keys:")
    for c in steamChunks:
        print(c)

    print("Possible Origin Keys:")
    for c in originChunks:
        print(c)

if __name__ == "__main__":
    main()
