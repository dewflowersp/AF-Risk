import os
import pandas as pd
from app.common import set_page_container_style


class DataList():

    def __init__(self):
        self.file_path = "patient_data.csv"
        set_page_container_style()

    def show_data(self, st):
        st.header("Patient Data")
        if os.path.exists(self.file_path):
            df = pd.read_csv(self.file_path)
            st.dataframe(df)