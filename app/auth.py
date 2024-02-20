import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

class Auth:

    def __init__(self):
        with open('./config.yaml') as file:
            self.config = yaml.load(file, Loader=SafeLoader)

            self.authenticator = stauth.Authenticate(
                self.config['credentials'],
                self.config['cookie']['name'],
                self.config['cookie']['key'],
                self.config['cookie']['expiry_days'],
                self.config['preauthorized']
            )
            self.authenticator.login()


    def logout(self, location='main'):
        self.authenticator.logout(location=location)


    def signup(self, location='main'):
        name, authentication_status, username = self.authenticator.signup(location=location)
        return name, authentication_status, username

    def check_credentials(self, st):
        if st.session_state["authentication_status"]:
            with st.sidebar.container():
                st.write(f'Welcome *{st.session_state["name"]}*')
                self.logout()
            return True
        elif st.session_state["authentication_status"] == False:
            st.error('Username/password is incorrect')
        elif st.session_state["authentication_status"] == None:
            st.warning('Please enter your username and password')