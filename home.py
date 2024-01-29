import pandas as pd
import os

class Home:

    def __init__(self):
        file_path = "patient_data.xlsx"


    # Function to save data to an Excel file
    def save_data_to_excel(self, data):
        # Check if the file exists
        if os.path.exists(self.file_path):
            # Read existing data
            existing_data = pd.read_excel(self.file_path)
            # Append new data
            updated_data = existing_data.append(data, ignore_index=True)
        else:
            # If file does not exist, just use the new data
            updated_data = data

        # Save updated data to the Excel file
        updated_data.to_excel(self.file_path, index=False)

    def main(self, st):
        st.title("AF Risk and Health Parameters")

        # Patient Information Section
        st.header("Patient Information")
        email = st.text_input("Email")
        name = st.text_input("Firstname")
        surname = st.text_input("Lastname")

        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender_options = ['Male', 'Female', 'Other']
        gender = st.selectbox("Gender", gender_options)

        # Creating columns for AF Risk, Blood, and Echo Parameters
        col1, col2, col3 = st.columns(3)

        # AF Risk Parameters Section
        with col1:
            st.subheader("AF Risk Parameters")
            bmi = st.number_input("Body Mass Index", min_value=0.0, max_value=100.0, step=0.1, key='bmi')
            hypertension = st.radio("Hypertension", ('Present', 'Absent'), key='hypertension')
            diabetes = st.radio("Diabetes", ('Present', 'Absent'), key='diabetes')

        # Blood Parameters Section
        with col2:
            st.subheader("Blood Parameters")
            cholesterol = st.number_input("Cholesterol", key='cholesterol')
            triglyceride = st.number_input("Triglyceride", key='triglyceride')
            hemogram = st.number_input("Hemogram", key='hemogram')
            iron = st.number_input("Iron", key='iron')
            creatinine = st.number_input("Creatinine", key='creatinine')
            tsh = st.number_input("TSH", key='tsh')

        # Echo Parameters Section
        with col3:
            st.subheader("Echo Parameters")
            lv_hypertrophy = st.radio("Left Ventricular Hypertrophy", ('Yes', 'No'), key='lv_hypertrophy')
            la_dilatation = st.radio("Left Atrial Dilatation", ('Yes', 'No'), key='la_dilatation')
            valve_problem = st.radio("Valve Problem", ('Yes', 'No'), key='valve_problem')
            ra_dilatation = st.radio("Right Atrial Dilatation", ('Yes', 'No'), key='ra_dilatation')
            pa_pressure = st.radio("Pulmonary Artery Pressure", ('Yes', 'No'), key='pa_pressure')
            ejection_fraction = st.selectbox("Ejection Fraction", ('Reduced', 'Middle', 'Preserved'), key='ejection_fraction')

        # Submit Button
        if st.button("Submit"):
            # Collect all data into a DataFrame
            data = pd.DataFrame({
                "Email": [email], 
                "Firstname": [name],
                "Lastname": [surname],
                "Age": [age],
                "Gender": [gender],
                "BMI": [bmi],
                "Hypertension": [hypertension],
                "Diabetes": [diabetes],

                "Cholesterol": [cholesterol],
                "Triglyceride": [triglyceride],
                "Hemogram": [hemogram],
                "Iron": [iron],
                "Creatinine": [creatinine],
                "TSH": [tsh],
                "LV Hypertrophy": [lv_hypertrophy],
                "LA Dilatation": [la_dilatation],
                "Valve Problem": [valve_problem],
                "RA Dilatation": [ra_dilatation],
                "PA Pressure": [pa_pressure],
                "Ejection Fraction": [ejection_fraction]
                # Add other parameters here...
            })

            self.save_data_to_excel(data)

            st.success("Data saved successfully!")

        # ECG Data Upload and Processing
        st.subheader("ECG Data Upload and Analysis")
        ecg_data = st.file_uploader("Upload ECG Data", type=['csv'], help="Drag and drop file here. Limit 200MB per file. Format: CSV")

        col1, col2 = st.columns(2)

        with col1:
            if ecg_data is not None:
                st.write("ECG Data Uploaded")
                # Here you would process the ECG data and apply the machine learning model
                # For demonstration, I'll just read and display the CSV
                df_ecg = pd.read_csv(ecg_data)
                st.write(df_ecg)
                # Here you can apply your ML model to df_ecg and show the result
                # e.g., ecg_score = simple_ml_model(df_ecg)

        # Display a sample ECG image or generated plot
