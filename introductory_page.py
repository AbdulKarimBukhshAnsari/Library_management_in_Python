from PIL import Image as Im , ImageTk
from tkinter import*
import os
# defining the function
def display_image(canvas,x,y,image_path,x_size,y_size):
    image =Im.open(image_path)
    resized_image = image.resize((x_size,y_size))
    photo =ImageTk.PhotoImage(resized_image)
    canvas.create_image(x, y, image=photo)
    canvas.image = photo


def image_path(directory_address):
    current_path=os.getcwd()
    image_path = os.path.join(current_path,directory_address)
    return image_path


def main():
    window =Tk()        
    #Setting the geometry 
    x = "130"  
    y = "30"
    width_window = "1000"
    height_window="600"
    window.geometry(f"{width_window}x{height_window}+{x}+{y}")
    window.resizable(False,False)
    #Set the colour
    bg_colour = "#EFDECD"
    window.configure(bg=bg_colour)
    #creating Canvas to show the widget
    canvas =Canvas(window,width=width_window,height=height_window,bg="#EFDECD") #make canva to display the image
    canvas.pack()
    #definig the position and size of logo 
    x_of_logo = "270"
    y_of_logo = "50"
    x_size_of_logo =130
    y_size_of_logo =120
    logo_address ="Library_management_in_Python\All_pictures\logo.png"
    real_address =image_path(logo_address)
    display_image(canvas,x_of_logo,y_of_logo,real_address,x_size_of_logo,y_size_of_logo)

    #label with text
    text_on_label = "Library  Management  System"
    x_label ="520"
    y_label ="55"
    canvas.create_text(x_label,y_label,text=text_on_label,font=("Cambria Math",24,"bold"),fill="black",anchor="center")   
    
    #book pictures on left side
    # x_of_book_left = "540" #coordinates
    # y_of_book_left = "540"  #coordinates
    # x_size_of_book_left =100 #size
    # y_size_of_book_left =100 #size
    # book_left_address ="Library_management_in_Python\All_pictures\left_book.png"
    # real_book_left_address =image_path(book_left_address)
    # display_image(canvas,x_of_book_left,y_of_book_left,real_book_left_address,x_size_of_book_left,y_size_of_book_left)



    window.mainloop()

main()