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

        git_repo = f"[![repo]({c.GIT_ICON})]({c.GIT_LINK})"
        linkedin = f"[![linkedin]({c.LINKEDIN_ICON})]({c.LINKEDIN_LINK})"
        linkedin_col, git_col, _, _, _, _, _ = st.columns(7)
        linkedin_col.markdown(linkedin, unsafe_allow_html=True)
        git_col.markdown(git_repo, unsafe_allow_html=True)
        st.write('---')
        st.subheader("Got any questions?")
        assistant, meeting, _ = st.columns([2, 2, 4])
        assistant.button(label="Talk to my assistant", use_container_width=True, on_click=self.toggle_sidebar)
        meeting.button(label="Book a meeting", use_container_width=True, on_click=self.book_a_meeting)

        # st.write("Or you can ask my assistant to book a meeting..")

        if st.session_state.sidebar_open:
            with st.sidebar:
                self.chat.chat_box()

        st.write('---')
        st.subheader("Project Gallery")
        for project in PROJECTS:
            with st.expander(project['title']):
                self.show_project_details(project)

    def show_project_details(self, project):
        link = project.get('link', '')
        title_string = project['title'] if link == '' else f'[{project['title']}]({link})'
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

