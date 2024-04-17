import dependencies as d

if __name__ == '__main__':
    file = '..\..\imagem.jpeg'
    img = d.cv2.imread(file)
    print(type(img))
    test = d.Filter(img)

    test.show_img()
    test.gray_scale()
    test.binarization()
    test.flip()
    test.show_img()