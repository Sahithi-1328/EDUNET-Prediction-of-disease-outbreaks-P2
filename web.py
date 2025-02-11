import os
import pickle  # Pre-trained model loading
import streamlit as st  # Web app
from streamlit_option_menu import option_menu

# Streamlit page configuration
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

#getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load pre-trained models
diabetes_model = pickle.load(open(f'{working_dir}/Saved_Models/diabetes.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/Saved_Models/heartdisease.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/Saved_Models/parkinsons.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# ================= Diabetes Prediction =================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(Bloodpressure), float(SkinThickness), float(Insulin),
                          float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.success(diab_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values.")

# ================= Heart Disease Prediction =================
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        CP = st.text_input('Chest Pain Type (CP)')
    with col1:
        Trestbps = st.text_input('Resting Blood Pressure (Trestbps)')
    with col2:
        Chol = st.text_input('Cholesterol Level')
    with col3:
        Fbs = st.text_input('Fasting Blood Sugar (1 = True, 0 = False)')
    with col1:
        Restecg = st.text_input('Resting ECG Results')
    with col2:
        Thalach = st.text_input('Maximum Heart Rate Achieved (Thalach)')
    with col3:
        Exang = st.text_input('Exercise-Induced Angina (1 = Yes, 0 = No)')
    with col1:
        Oldpeak = st.text_input('ST Depression Induced by Exercise (Oldpeak)')
    with col2:
        Slope = st.text_input('Slope of Peak Exercise ST Segment')
    with col3:
        CA = st.text_input('Number of Major Vessels (CA)')
    with col1:
        Thal = st.text_input('Thalassemia (Thal)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(Age), float(Sex), float(CP), float(Trestbps), float(Chol), float(Fbs), float(Restecg),
                          float(Thalach), float(Exang), float(Oldpeak), float(Slope), float(CA), float(Thal)]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'

            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values.")

# ================= Parkinson's Prediction (Add if needed) =================
elif selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction using ML')
    #st.warning("Parkinson's prediction logic is not implemented yet.")
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('Spread1')
    with col2:
        spread2 = st.text_input('Spread2')
    with col3:
        D2 = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button('Parkinson\'s Test Result'):
        try:
            user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ,
                      Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ,
                      Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            user_input = [float(x) for x in user_input]  # Convert inputs to float
            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The person has Parkinson\'s disease'
            else:
                parkinsons_diagnosis = 'The person does not have Parkinson\'s disease'

            st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values.")    

