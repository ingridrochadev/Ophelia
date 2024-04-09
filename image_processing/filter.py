import dependencies as d

class Filter:
    def __init__(self, image):
        self.img = image

    # Mostra
    def show_img(self, name: str = "") -> None:
        d.cv2.imshow(name, self.img)
        d.cv2.waitKey(0)
    
    # Salva
    def save_img(self, output_file: str = "img") -> None:
        d.cv2.imwrite(output_file, self.img)
        print("Processed image saved as:", output_file)

    # Cinza
    def gray_scale(self) -> None:
        gray_img = d.cv2.cvtColor(self.img, d.cv2.COLOR_BGR2GRAY)
        self.img = gray_img

    # Preto e branco
    def binarization(self, limiar: int = 115) -> None: #limiar é o "parâmetro para a binarização"
        _, binarized_image = d.cv2.threshold(self.img, limiar, 255, d.cv2.THRESH_BINARY)
        self.img = binarized_image

    # Nitidez
    def sharpness(self) -> None:
        pass

    # Ampliação / Enquadramento
    def enlargement(self) -> None:
        pass
        # pts1 = d.np.float32([[29,32],[194,25],[13,200],[207,202]])
        # pts2 = d.np.float32([[0,0],[300,0],[0,300],[300,300]])
        # M = d.cv2.getPerspectiveTransform(pts1,pts2)
        # dst = d.cv2.warpPerspective(self.img, M, (300,300))
        # self.img = dst
    
    # Gira
    def rotate(self) -> None:
        self.img = d.cv2.rotate(self.img, d.cv2.ROTATE_90_CLOCKWISE)
    
    # Inverte
    def flip(self) -> None:
        self.img = d.cv2.flip(self.img, 1)