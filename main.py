from tkinter import HORIZONTAL

import cv2
import os
import tkinter
from PIL import Image, ImageTk

#TODO:
# -add photo centering
# -add window resize to fit photo and screen (more resize or dynamic window size?)
# -refactor XD
# -file explorer
# -video compatibility (how to solve running video? Maybe run videos in different mode - i.e. conver and run on button - dynamic gui)
# -add more filters
# -change to pyqt?
class mainWindow():
    def __init__(self, path):
        self.window = tkinter.Tk()
        self.window.geometry("800x600")
        self.image = cv2.imread(path)
        self.image_path = path
        self.createGui()

    def saveImage(self):
        without_empty_strings = [string for string in self.image_path.split("\\") if string != ""]
        img_name = without_empty_strings[-1]
        base_path = "\\".join(without_empty_strings[:-1])
        base_path = base_path + "\\Canny_" + img_name.split('.')[0]
          
    def createGui(self):
        self.lower_limit = 0
        self.upper_limit = 40

        self.lower_slider = tkinter.Scale(self.window, from_=0, to=600, orient=HORIZONTAL, variable=self.lower_limit, length=1200,
                                          resolution=1, command=lambda value: self.sliderChange(value))
        self.lower_slider.pack()

        self.upper_slider = tkinter.Scale(self.window, from_=0, to=600, orient=HORIZONTAL, length=1200,
                                          variable=self.upper_limit, resolution=1, command=lambda value: self.sliderChange(value))
        self.upper_slider.pack()

        # self.button = tkinter.Button(self.window, text="Process photo!",
        #                         command=lambda: self.preparePhotos())
        # self.button.pack()

        # self.canvas = tkinter.Canvas(self.window, width=300, height=300)
        # self.canvas.pack()
        # self.canvas.create_image(20, 20, anchor=tkinter.NW, image=self.image)


        self.window.mainloop()

    def sliderChange(self, value):
        if self.upper_slider.get() <= self.lower_slider.get() <= 590:
            self.upper_slider.set(self.lower_slider.get() + 10)
        elif self.upper_slider.get() <= self.lower_slider.get() >= 590:
            self.upper_slider.set(600)
        self.convertPhoto()

    def savePhoto(self, base_path, img_name, ddd):
        print(base_path + "\\" + img_name.split('.')[0] + "1." + img_name.split('.')[1])
        cv2.imwrite(base_path + "\\" + img_name.split('.')[0] + "2." + img_name.split('.')[1], ddd)

    def convertPhoto(self):
        # show the output Canny edge maps
        height, width, _ = self.image.shape
        # image = cv2.resize(image,  [int(width / 4), int(height / 4)])
        canny_image = cv2.Canny(self.image, self.lower_slider.get(), self.upper_slider.get())
        print(self.lower_slider.get(), self.upper_slider.get())
        canny_image = cv2.resize(canny_image,  [int(width / 4), int(height / 4)])


        if len(canny_image.shape) > 2:
            b, g, r = cv2.split(canny_image)
            img = cv2.merge((r, g, b))
            im = Image.fromarray(img)
            test = ImageTk.PhotoImage(im)
        else:
            im = Image.fromarray(canny_image)
            test = ImageTk.PhotoImage(im)

        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.configure(image=test)
        label1.place(x=200, y=90)
        self.window.update_idletasks()


        # cv2.imshow("Canny image", canny_image)
        # cv2.waitKey(0)

# def cannyImage(path=None):
#     list = path.split("\\")
#
#     without_empty_strings = [string for string in list if string != ""]
#     img_name = without_empty_strings[-1]
#     base_path = "\\".join(without_empty_strings[:-1])
#     base_path = base_path + "\\Canny_" + img_name.split('.')[0]
#
#     print(img_name)
#     if not os.path.exists(base_path):
#         os.makedirs(base_path)
#
#     image = cv2.imread(path)
#     wide = cv2.Canny(image, 10, 200)
#     ddd = cv2.Canny(image, 80, 120)
#     mid = cv2.Canny(image, 30, 150)
#     tight = cv2.Canny(image, 240, 250)
#
#
#     # wide = cv2.resize(wide, [int(width / 4), int(height / 4)])
#     # mid = cv2.resize(mid,  [int(width / 4), int(height / 4)])
#     # tight = cv2.resize(tight, [int(width / 4), int(height / 4)])
#
#     cv2.imwrite(base_path + "\\" + img_name.split('.')[0] + "3." + img_name.split('.')[1], mid)
#     cv2.imwrite(base_path + "\\" + img_name.split('.')[0] + "4." + img_name.split('.')[1], tight)
#     cv2.imwrite(base_path + "\\" + img_name.split('.')[0] + "1." + img_name.split('.')[1], wide)
#
#
#
#     # cv2.imshow("Wide Edge Map", wide)
#     # cv2.imshow("Mid Edge Map", mid)
#     # cv2.imshow("Tight Edge Map", tight)
#     # cv2.imshow("ddd Edge Map", ddd)
#     cv2.waitKey(0)



if __name__ == '__main__':
    # pathh = r'C:\\Users\\gracj\\OneDrive\\Obrazy\\cot.jpg'
    pathh = r'C:\\Users\\gracj\\OneDrive\\Obrazy\\245124588_232126335616265_1191892014833421561_n.jpg'
    window = mainWindow(pathh)
    # cannyImage(pathh)
