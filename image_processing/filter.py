import dependencies as d

class Filter:
    def __init__(self, image):
        self.img = image

    def gray_scale(self):
        gray_img = d.cv2.cvtColor(self.img, d.cv2.COLOR_BGR2GRAY)
        return gray_img

    def binarization(self):
        pass

    # def pass():

# # Converter para escala de cinza com ajuste de escala (0 = preto, 255 = branco)
# escala = 12  # Ajuste o valor conforme necessário
# imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# imagem_cinza_ajustada = cv2.convertScaleAbs(imagem_cinza, alpha=escala, beta=0)