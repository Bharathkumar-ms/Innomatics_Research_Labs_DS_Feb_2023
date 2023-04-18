import streamlit as st
from PIL import Image
from matplotlib import image
import os


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title(":green[Welcome to Homepage! 👋]")
st.snow()



st.title(":red[Innomatics Research Labs]")


#Title of the home page
st.header(":blue[Flipkart Laptop Price Prediction :desktop_computer]")
#Using subheader
st.write('By: :red[Bharathkumar M S]')

#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "image")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "lap1.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)


st.title(":violet[ Data science Internship]")



btn_click = st.button("Click me to Know Who I am")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()
    st.title("I am :red[Bharathkumar M S]")
    st.title("I am a  :violet[ Data Science Enthusiast]")
    st.write("## Connect me on Linkedin [link](https://www.linkedin.com/in/bharathkumar-m-s-1736221b0/)")