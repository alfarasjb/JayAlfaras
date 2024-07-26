import streamlit as st
import streamlit.components.v1 as components

from src.app.chat import Chat
from src.definitions import constants as c
from src.definitions.projects import PROJECTS


class PortfolioApp:
    def __init__(self):
        self.chat = Chat()
        self._initialize_app()

    def _initialize_app(self):
        st.set_page_config(page_title="Jay Alfaras", layout="centered", initial_sidebar_state="expanded")
        st.markdown("""
            <style>
                .main .block-container {
                    max-width: 60%;
                    padding-top: 2rem; 
                    padding-right: 2rem;
                    padding-left: 2rem; 
                    padding-bottom: 2rem; 
                }
            </style>
        """, unsafe_allow_html=True)
        with open("style/style.css") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        self._initialize_states()

    def _initialize_states(self):
        if "sidebar_open" not in st.session_state:
            st.session_state.sidebar_open = False

    def toggle_sidebar(self):
        st.session_state.sidebar_open = not st.session_state.sidebar_open

    def main(self):
        # Header content
        st.markdown(
            """
            <div class="header">
                <div class="header-left">
                    <div class="header-title">Jay Benedict Alfaras</div>
                    <div class="header-job-title">AI Engineer</div>
                </div>
                <div class="header-right">
                    <div class="header-link">
                        <img src={LINKEDIN_ICON} alt="LinkedIn">
                        <a href={LINKEDIN_LINK} target="_blank">linkedin.com/in/{LINKEDIN_USERNAME}</a>
                    </div>
                    <div class="header-link">
                        <img src={GITHUB_ICON} alt="GitHub">
                        <a href={GITHUB_LINK} target="_blank">github.com/{GIT_USERNAME}</a>
                    </div>
                    <div class="header-link">
                        <img src=https://cdn-icons-png.flaticon.com/512/561/561127.png alt="Email">
                        <a href="mailto:alfarasjb@gmail.com" target="_blank">alfarasjb@gmail.com</a>
                    </div>
                </div>
            </div>
            """.format(LINKEDIN_ICON=c.LINKEDIN_ICON,
                       GITHUB_ICON=c.GIT_ICON,
                       LINKEDIN_LINK=c.LINKEDIN_LINK,
                       GITHUB_LINK=c.GIT_LINK,
                       GIT_USERNAME="alfarasjb",
                       LINKEDIN_USERNAME="jay-alfaras"),
            unsafe_allow_html=True
        )


        st.write('---')
        description, projects = st.columns(2)

        description.subheader("About Me")
        description.write(
            """
            I am an AI Engineer from the Philippines. My work focuses on developing and deploying AI Applications for our clients. 
            
            I have worked on multiple projects ranging from Machine Learning, Natural Language Processing, and even integrating OpenAI into 
            applications to solve the various business requirements of our clients.  
            
            Aside from AI, I am also an experienced Algorithmic Trading Developer where I specialize in developing execution models for trading strategies
            primarily through the MetaTrader platform, with MQL4, MQL5, and Pinescript.
            """
        )
        projects.subheader("Project Gallery")
        for project in PROJECTS:
            with projects.expander(project['title'].upper()):
                self.show_project_details(project)

        st.write('---')
        st.subheader("Got any questions?")
        assistant, meeting, _ = st.columns([2, 2, 4])
        assistant.button(label="Talk to my assistant", use_container_width=True, on_click=self.toggle_sidebar)
        meeting.button(label="Book a meeting", use_container_width=True, on_click=self.book_a_meeting)

        # st.write("Or you can ask my assistant to book a meeting..")

        if st.session_state.sidebar_open:
            with st.sidebar:
                self.chat.chat_box()

    def show_project_details(self, project):
        link = project.get('link', '')
        title_string = project['title'] if link == '' else f"[{project['title']}]({link})"
        st.write(f"### {title_string}")
        st.write(project['details'])
        techs = ""
        for tech in project['technologies']:
            techs += f'`{tech}` '
        st.write(f"**Technologies Used:** {techs}")

    def book_a_meeting(self):
        js = """
            <script type="text/javascript">
                window.open("https://calendly.com/alfarasjb", "_blank");
            </script>
            """
        components.html(js)

