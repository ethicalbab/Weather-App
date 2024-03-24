from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests

# Function to get weather data
def get_weather(city):
    api_key = "cb34b0ebc7c412531aad850125c92a01"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp'] - 273.15
        humidity = data['main']['humidity']
        return weather, temp, humidity
    else:
        return None, None, None

# Function to display weather data
def display_weather():
    city = com.get()
    weather, temp, humidity = get_weather(city)
    if weather is not None:
        canvas.itemconfig(w_label1, text=weather)
        canvas.itemconfig(temp_label1, text=f'{temp:.2f}°C')
        canvas.itemconfig(per_label1, text=f'{humidity}%')
    else:
        canvas.itemconfig(w_label1, text='Error')
        canvas.itemconfig(temp_label1, text='Error')
        canvas.itemconfig(per_label1, text='Error')

# Driver Code
# create object
app = Tk()
# add title
app.title("Weather App")
# adjust window size
app.geometry("450x400")

# Set background image
bg_img = Image.open("862350.png")
bg_img = ImageTk.PhotoImage(bg_img)
canvas = Canvas(app, width=450, height=700)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, image=bg_img, anchor="nw")

# Load an image using PIL
app_icon = Image.open("icon.png")
app_icon = ImageTk.PhotoImage(app_icon)

# Set the icon of the app
app.iconphoto(False, app_icon)

name_label = canvas.create_text(225, 50, text="Weather App", font=("Times New Roman", 30, "bold"), fill="white")

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
             "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(app, values=list_name, font=("Times New Roman", 20))
canvas.create_window(225, 125, window=com)

display_button = Button(app, text="Display", font=("Times New Roman", 20, "bold"), command=display_weather)
canvas.create_window(225, 175, window=display_button)

# Position the text labels
left_col_x = 50
right_col_x = 250
line_spacing = 40

w_label = canvas.create_text(left_col_x, 250, text="Weather:", font=("Times New Roman", 20), fill="white", anchor="w")
w_label1 = canvas.create_text(right_col_x, 250, text=" ", font=("Times New Roman", 20), fill="white", anchor="w")

temp_label = canvas.create_text(left_col_x, 250 + line_spacing, text="Temperature:", font=("Times New Roman", 20), fill="white", anchor="w")
temp_label1 = canvas.create_text(right_col_x, 250 + line_spacing, text=" ", font=("Times New Roman", 20), fill="white", anchor="w")

per_label = canvas.create_text(left_col_x, 250 + line_spacing * 2, text="Humidity:", font=("Times New Roman", 20), fill="white", anchor="w")
per_label1 = canvas.create_text(right_col_x, 250 + line_spacing * 2, text=" ", font=("Times New Roman", 20), fill="white", anchor="w")

app.mainloop()
