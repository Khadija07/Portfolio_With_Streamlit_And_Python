import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(
    page_title="Personal Webpage", page_icon=":sparkles:", layout="wide"
)

def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
        
local_css("styles/style.css")

def load_lottie(url):             #to load the animation
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottie("https://lottie.host/c9a9be74-026e-447f-b824-47bc2930b95f/qV4r0qmRKR.json")
img_project1 = Image.open("images/movie.png")
#header_section

with st.container():
    st.subheader("Moi, I am Khadija :wave: ")
    st.title("Software Developer in Finland")
    st.write("I am passionate about learning and working with technologies.")
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            I am an experienced individual with proficiency in
            Python, along with a background in Computer Science. I am a final year Master's student at University of Helsinki.
            I have a strong passion for technology and have actively pursued several projects to enhance my skills and expand my
            knowledge with Python, REACTJS, HTML, CSS, and JavaScript.
            """
            
        )
    
    with right_column:
        st_lottie(lottie_animation, height=350, key="codingAnimation")
        
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        st.image(img_project1)
        
        
    with text_column:
        st.subheader("Movie Application Using ReactJS")
        st.write("""
                 Built a movie application that enables users to search and browse a vast movie library. Utilized JavaScript, 
                 React, and Node.js to build a dynamic and user-friendly movie catalog.
                 Emphasized front-end and back-end development skills while delivering an engaging user experience
        """
        )
        st.markdown("[Link to Github](https://github.com/Khadija07/Movie_App)")
        
        

        
    
#contact information

with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")
    
    contact_info = """
    <form action="https://formsubmit.co/ktk_01@outlook.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message" required></textarea>
     <button type="submit">Send</button>
     </form>
    """
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.markdown(contact_info, unsafe_allow_html= True)
    with right_column:
        st.empty()
    