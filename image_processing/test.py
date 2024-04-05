import dependencies as d

if __name__ == '__main__':
    file = '..\..\imagem3.jpg'
    img = d.cv2.imread(file)
    print(type(img))
    test = d.Filter(img)

    gray_img = test.gray_scale()

    d.cv2.imshow("nome", gray_img)
    d.cv2.waitKey(0)