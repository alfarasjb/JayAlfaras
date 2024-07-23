import webbrowser

import streamlit as st
import streamlit.components.v1 as components
from src.app.chat import Chat


class PortfolioApp:
    def __init__(self):
        self.chat = Chat()
        self._initialize_app()

    def _initialize_app(self):
        st.set_page_config(page_title="Jay Alfaras", layout="centered", initial_sidebar_state="expanded")
        self._initialize_states()

    def _initialize_states(self):
        if "sidebar_open" not in st.session_state:
            st.session_state.sidebar_open = False

    def toggle_sidebar(self):
        st.session_state.sidebar_open = not st.session_state.sidebar_open

    def main(self):
        st.title("Jay Benedict Alfaras")
        st.subheader("AI Engineer")

        st.write('---')
        st.write(
            """
            I am an AI Engineer from the Philippines. My work focuses on developing and deploying AI Applications for our clients. 
            
            I have worked on multiple projects ranging from Machine Learning, Natural Language Processing, and even integrating OpenAI into 
            applications to solve the various business requirements of our clients.  
            
            Aside from AI, I am also an experienced Algorithmic Trading Developer where I specialize in developing execution models for trading strategies
            primarily through the MetaTrader platform, with MQL4, MQL5, and Pinescript.
            """
        )
        st.write('---')
        st.subheader("Got any questions?")
        assistant, meeting, _ = st.columns([2, 2, 4])
        assistant.button(label="Talk to my assistant", use_container_width=True, on_click=self.toggle_sidebar)
        meeting.button(label="Book a meeting", use_container_width=True, on_click=self.book_a_meeting)

        if st.session_state.sidebar_open:
            with st.sidebar:
                self.chat.chat_box()

        st.write('---')
        st.subheader("Gallery")

    def book_a_meeting(self):
        # url = 'https://calendly.com/alfarasjb'
        # webbrowser.open(url)
        js = """
            <script type="text/javascript">
                window.open("https://calendly.com/alfarasjb", "_blank");
            </script>
            """
        components.html(js)

