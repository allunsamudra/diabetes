import pickle
import streamlit as st

# Load the model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Web title
st.title('Prediksi Diabetes')

# Description and instructions
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        .description {
            font-size: 1.2em;
            margin-bottom: 20px;
            text-align: center;
        }
        .input-section {
            margin: 20px 0;
        }
        .result {
            font-size: 1.5em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <div class="description">
        Masukkan data pasien untuk memprediksi apakah mereka terkena diabetes atau tidak.
    </div>
""", unsafe_allow_html=True)

# Create form for input
with st.form(key='diabetes_form'):
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input('Bulan Kehamilan (0 jika tidak hamil)')
        BloodPressure = st.text_input('Tekanan Darah')
        Insulin = st.text_input('Insulin')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')

    with col2:
        Glucose = st.text_input('Glukosa')
        SkinThickness = st.text_input('Ketebalan Kulit')
        BMI = st.text_input('BMI')
        Age = st.text_input('Umur')

    # Create button for prediction
    submit_button = st.form_submit_button(label='Test Prediksi Diabetes')

    # Code for prediction
    if submit_button:
        try:
            # Convert inputs to appropriate format
            input_features = [[
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
            ]]

            diab_prediction = diabetes_model.predict(input_features)

            if diab_prediction[0] == 1:
                diab_diagnosis = 'Pasien terkena Diabetes'
            else:
                diab_diagnosis = 'Pasien tidak terkena Diabetes'

            st.markdown(f"<div class='result'>{diab_diagnosis}</div>", unsafe_allow_html=True)
        except ValueError:
            st.error("Pastikan semua input adalah angka yang valid.")
