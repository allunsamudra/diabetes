import pickle
import streamlit as st

# Load the model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Title of the web app
st.title('Prediksi Diabetes')

# Add a subtitle for better understanding
st.subheader('Masukkan Data untuk Memprediksi Diabetes')

# Four column layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    Pregnancies = st.number_input('Angka Kehamilan', min_value=0, step=1, format="%d")

with col2:
    Glucose = st.number_input('Glukosa', min_value=0, step=1, format="%d")

with col3:
    BloodPressure = st.number_input('Tekanan Darah (mmHg)', min_value=0, step=1, format="%d")

with col4:
    SkinThickness = st.number_input('Ketebalan lipatan kulit trisep (mm)', min_value=0, step=1, format="%d")

with col1:
    Insulin = st.number_input('Insulin serum (mu U/ml)', min_value=0, step=1, format="%d")

with col2:
    BMI = st.number_input('BMI', min_value=0.0, step=0.1, format="%.1f")

with col3:
    DiabetesPedigreeFunction = st.number_input('Indikator riwayat diabetes dalam keluarga', min_value=0.0, step=0.01, format="%.2f")

with col4:
    Age = st.number_input('Usia (tahun)', min_value=0, step=1, format="%d")

# Placeholder for the diagnosis result
diab_diagnosis = ''

# Create a button for prediction
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
        
    # Display the diagnosis result
    st.success(diab_diagnosis)

# Add footer
st.write("---")
st.write("Aplikasi Prediksi Diabetes ini dibuat untuk membantu memprediksi kemungkinan diabetes berdasarkan data kesehatan yang dimasukkan.")
