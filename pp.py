import streamlit as st
# title
st.title("Hello suraj")
# header/subheader
st.header("wellcome to streamlit")
st.subheader("my project")
# text
st.text("this is my first project")

from PIL import Image

img = Image.open("1.jpg")

st.image(img)

# adding video
video_file = open("2.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

# ballon
st.balloons()

# sidbar
st.sidebar.header("about")
st.sidebar.text("this is my first project in streamlit")


st.markdown('[Go to Google](https://www.google.com)')
