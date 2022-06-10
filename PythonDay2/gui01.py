import tkinter as tk

mainFrm = tk.Tk()  # Creating instance of Tk class
mainFrm.title("Centering windows")
mainFrm.resizable(False, False)  # This code helps to disable # windows from resizing

window_height = 500
window_width = 900

screen_width = mainFrm.winfo_screenwidth()
screen_height = mainFrm.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

mainFrm.geometry("{}x{}+{}+{}".format(window_width,window_height, x_cordinate, y_cordinate))

mainFrm.mainloop()
