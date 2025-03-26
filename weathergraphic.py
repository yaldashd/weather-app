# We want to show the weather information in an application not in console environment :
import tkinter as tk
from tkinter.constants import COMMAND
# Using the requests library for our weather system :
import requests
#Using the time library for sunrise and sunset and datetime for date
import datetime
import time
from PIL import ImageTk, Image

# Making the concept of url easier :  
API_code = 'ed27ccf551c24a3fb56ab4b9e2796630'
base_url = 'http://api.openweathermap.org/data/2.5/weather?q='

window = tk.Tk()# Make the gui window for showing weather information
window.title("Weather APP")# The name of our application

window.geometry("550x750")
window.resizable(False,False)
#background image 
background = ImageTk.PhotoImage(Image.open("view.jpg")) 
bg_label=tk.Label(master=window,image=background)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)


#window icon
window.iconbitmap('weatherappicon2.ico')#changing icon image 

label_city_not_found = tk.Label( master = window , bg = 'light blue',font='consolas 10')# Use the label here for prevent from repetition in the send function when we type an unknown city
label_l = tk.Label(master=window,font='Consolas 20 bold',bg= None)#label of the location
label_tc = tk.Label( master = window , font ='Consolas 20 bold ',bg= None)# Label of the temperature 
label_p_h = tk.Label( master = window, font ='Consolas 14 ',bg=None)# Label of the pressure and humidity
label_d = tk.Label( master = window , font ='Consolas 18 bold ' ,bg=None)# Label of the description
label_sr=tk.Label(master=window, font='consolas 14',bg= None)#label of the sunrise and sunset
label_mnx=tk.Label(master=window,font='Consolas 14',bg= None)#label of minimum and maximum temperature
label_tz=tk.Label(master=window,font='consolas 18',bg=None)#label of date


# Function for pressing the button and then see the information about the weather of the city :
def search():

    city_name = city_name_entry.get()# Recieve the name of the city and save it in the city_name variable when user enter the name of the city in the box
    url = base_url + city_name + '&appid=' + API_code

    result = requests.get(url)# Load the url and information to use it
    data = result.json()# Convert the information in the json format to a conceptable information such as dictionary in python


    # If we enter an unknown city we will see this in the json format : {"cod":"404","message":"city not found"} , so lets make conditional system for this situation
    if data['cod'] == '404' :
        
        label_city_not_found.config(text = 'CITY NOT FOUND !')# We use config function for widgets settings
        label_l.pack_forget()
        label_tz.pack_forget()
        label_tc.pack_forget()
        label_d.pack_forget()
        label_mnx.pack_forget()
        label_p_h.pack_forget()
        label_sr.pack_forget()
        label_city_not_found.pack()
        

    else :
        a = data["main"]

        t = a["temp"]
        tc = t - 273.15# Convert the temperature from Kelvin to Celsius

        p = a["pressure"]

        h = a["humidity"]

        w = data["weather"]
        d = w[0]["description"]

        s = data["sys"]
        l = s["country"]

        cn =data    
        c = cn["name"]

        sr=s['sunrise']
        ss=s['sunset']

        min=a['temp_min']-273.15
        max=a['temp_max']-273.15

        date_time=datetime.datetime.now()
        
        # We use config function for widgets settings :
        label_l.config(text= '📍 '+c +"," +l )
        label_tc.config( text = str(round(tc,2)) + " °c")# Attach the amount of temperature to it's measure that is a string
        label_p_h.config( text = "Pessure : " + str(p) + " hpa" + " " + " Humidity : " +str(h)+"%")
        label_d.config( text = d)
        label_sr.config(text= 'sunrise:'+time.strftime('%I:%M:%S %p',time.gmtime(sr+16222))+"  "+'sunset:'+time.strftime('%I:%M:%S %p',time.gmtime(ss+16222)))
        label_mnx.config(text= 'min:' +str(round(min,2))+'°c' +'  '+'max:'+ str(round(max,2))+'°c')
        label_tz.config(text=date_time.strftime('%A ')+ date_time.strftime('%d %B') )
        
        # Show the widgets in our window :
        label_city.pack_forget()
        city_name_entry.pack_forget()
        entry_button.pack_forget()
        label_city_not_found.pack_forget()
        return_button.pack(pady=10)
        label_l.pack(pady=30)
        label_tz.pack(pady=10)
        label_tc.pack(pady=10)
        label_d.pack( pady = 30)
        more_button.pack(pady=10)
        


#function for searching again
def back():
    
    return_button.pack_forget()
    label_l.pack_forget(),
    label_tz.pack_forget(),
    label_tc.pack_forget(),
    label_d.pack_forget(),
    label_mnx.pack_forget(),
    label_p_h.pack_forget(),
    label_sr.pack_forget(),
    more_button.pack_forget(),
    label_city.pack(pady=10),
    city_name_entry.pack(pady=10),
    entry_button.pack(pady=10)  

def more():
    label_mnx.pack(pady=20)
    label_p_h.pack(pady = 20)
    label_sr.pack(pady=20)

label_city = tk.Label(master = window , text = 'Please enter name of the city', font ='Consolas 14 bold')# Create a label for the name of the city that we want to see the information of it's weather
city_name_entry = tk.Entry(bg = 'white' , fg = 'midnight blue', font ='Consolas 14 bold')# Make a widget for entering the city name
entry_button = tk.Button(master = window , text = 'Search Weather' , command = search , bg = 'light yellow', font ='Consolas 14 bold' )# Make the button that we want to use as the entry for the city name
return_button=tk.Button(master=window,text='back to search',command=back,bg='pink',font='consolas 14')
more_button=tk.Button(master=window,bg='pink',text='More:',font='consolas 14',command=more)

# Widgets :
label_city.pack(pady = 10)# Show the label that we want for our widget
city_name_entry.pack()# Show the widget for entering the city name
entry_button.pack(pady = 10)# Show the button

window.mainloop()# Make the main window visible and waiting for any event from user on the main window