import openai
import requests
from tkinter import *

# Set your OpenAI API key
api_key=  #'your API key'
openai.api_key = api_key

root = Tk()
root.geometry("400x400")  # size of the window by default
root.resizable(0, 0)  # to make the window size fixed
# title of our window
root.title("Weather Chatbot")

# Initialize weather data variable
weather_data = None


def fetch_weather_data(location):
    api_key = '02df194726903947c29ba241dc5f7d31'
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={location}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['current']
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response['choices'][0]['message']['content']


def show_weather():
    global weather_data

    location = CEntry.get()
    weather_data = fetch_weather_data(location)

    if weather_data:
        weather_message = f"The current temperature in {location} is {weather_data['temperature']} degrees Celsius."
        ai_response = chat_with_gpt(weather_message)

        # to show the conversation in the text field
        tfield.delete("1.0", END)
        tfield.insert(END, f"AI: {weather_message}\nAI: {ai_response}\n")
    else:
        tfield.delete("1.0", END)
        tfield.insert(END, "Error: Unable to fetch weather data.")


CLabel = Label(root, text='Enter country name', font='Arial 12 bold')
CLabel.pack(pady=10)  # to generate label heading

CEntry = Entry(root, width=24, font='Arial 14 bold')
CEntry.pack()

Button(root, command=show_weather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

# to show output

weather_now = Label(root, text="Chat with the Weather AI:", font='arial 12 bold')
weather_now.pack(pady=10)

tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()
