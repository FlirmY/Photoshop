#создай тут фоторедактор Easy Editor!
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QListWidget, QPushButton, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
import os 
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtGui import QPixmap

workdir = ''


class ImageProcessor():
    def __init__ (self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'Modified/'

    def loadImage(self, filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)
    def show_image(self,path):
        pixmapimage = QPixmap(path)
        label_width, label_height = picture.width(), picture.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio) 
        picture.setPixmap(scaled_pixmap) 
        picture.setVisible(True)
    def save_image (self):
        path = os.path.join(workdir,self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path,self.filename)
        self.image.save(image_path)
    def do_bw(self):
        self.image = ImageOps.grayscale(self.image)
        self.save_image()
        image_path =os.path.join(workdir,self.save_dir,self.filename)
        self.show_image(image_path)
    def do_left(self):
        self.image = self.image.rotate(90)
        self.save_image()
        image_path =os.path.join(workdir,self.save_dir,self.filename)
        self.show_image(image_path)


    def do_right(self):
        self.image = self.image.rotate(270)
        self.save_image()
        image_path =os.path.join(workdir,self.save_dir,self.filename)
        self.show_image(image_path)

    def do_mirror(self):
        self.image = ImageOps.mirror(self.image)
        self.save_image()
        image_path =os.path.join(workdir,self.save_dir,self.filename)
        self.show_image(image_path)

    def do_sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path =os.path.join(workdir,self.save_dir,self.filename)
        self.show_image(image_path)


WorkImage = ImageProcessor()





def showChosenImage():
    if files_list.currentRow() >= 0:
        filename = files_list.currentItem().text()
        WorkImage.loadImage(filename)
        image_path = os.path.join(workdir,filename)
        WorkImage.show_image(image_path)






def choseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename) 
                # break
    return result


def ShowFilenameList():
    choseWorkdir()
    extensions = ['.png', '.jpg' ,'.jpeg','.gif','.bmp', '.jfif']
    files = os.listdir(workdir)
    files = filter(files,extensions)
    files_list.clear()
    files_list.addItems(files)


app = QApplication([])
window = QWidget()
window.resize(700,500)


line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QVBoxLayout()
line4 = QVBoxLayout()
left = QPushButton('Лево')
right = QPushButton('Право')
files_list = QListWidget()
folder = QPushButton('Папка')
mirror = QPushButton('зеркало')
sharpen = QPushButton('резкость')
BW = QPushButton('Ч/Б')
picture = QLabel('картинка')

line1.addLayout(line3)
line1.addLayout(line4)
line4.addWidget(picture)
line4.addLayout(line2)
line3.addWidget(folder)
line3.addWidget(files_list)
line2.addWidget(left)
line2.addWidget(right)
line2.addWidget(mirror)
line2.addWidget(sharpen)
line2.addWidget(BW)

window.setLayout(line1)








folder.clicked.connect(ShowFilenameList)

files_list.currentRowChanged.connect(showChosenImage)

BW.clicked.connect(WorkImage.do_bw)
sharpen.clicked.connect(WorkImage.do_sharpen)
mirror.clicked.connect(WorkImage.do_mirror)
left.clicked.connect(WorkImage.do_left)
right.clicked.connect(WorkImage.do_right)


window.show()
app.exec_()