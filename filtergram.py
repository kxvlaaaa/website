import filter

def main():
    img = filter.load_img("corgipy.jpg")
    # # filter.show_img(img)
    # filter.save_img(img,'corgipy.jpg')
    obama_img = filter.obamicon(img)
    filter.show_img_(obama_img)



if __name__== "__main__":
    main()
