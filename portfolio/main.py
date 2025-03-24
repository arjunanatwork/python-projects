import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Arjunan Ravi")
    content="""
    Versatile Full Stack Developer with 9+ years of experience in analysis, design, implementation and support in large scale high performance applications. Technically ambitious and always looking for new challenges. Highly Adaptable to change, always willing to explore, experiment newer domains & technologies. ❤️ building apps. I have few other passions: Video Games 🎮, Music 🎵 and Travel ✈️.
    """
    st.write(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)