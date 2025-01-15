

import os.path
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
        self.lb_image = None

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)

    def showImage(self, path, lb_image):
        self.lb_image = lb_image
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path,self.lb_image)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path,self.lb_image)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path,self.lb_image)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path,self.lb_image)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.GaussianBlur(10))
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path,self.lb_image)

    def do_del(self):
        self.image = self.image.filter(ImageFilter.MedianFilter(5))
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path,self.lb_image)

    def do_func1(self):
        kernel = ImageFilter.Kernel(
            size=(3,3),
            kernel = [1,0,2,
                     -1,5,-3,
                      0,-1,5],
            scale = None,
            offset=0

        )

        self.image = self.image.filter(kernel)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path,self.lb_image)
