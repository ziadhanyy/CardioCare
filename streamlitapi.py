import pickle
import streamlit as st 

# Load the model
model = pickle.load(open('logistic_regression_model.pkl', 'rb'))

def main():
    st.title('CardioCare: Heart Failure Prediction')
    
    # Input Variables
    Age = st.number_input('AGE', min_value=0, max_value=120, step=1, value=0)
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    ChestPainType = st.selectbox('Chest Pain Type', ['0', '1', '2', '3'], index=0)
    RestingBP = st.number_input('Blood Pressure', min_value=0, max_value=1000, step=1, value=0)
    Cholesterol = st.number_input('Cholesterol (mg/dl)', min_value=0, max_value=600, step=1, value=0)
    FastingBS = st.selectbox('Fasting Blood Sugar (mg/dl)', ['0', '1'], index=0)
    MaxHR = st.number_input('Maximum Heart Rate', min_value=0, max_value=300, step=1, value=0)
    ExerciseAngina = st.selectbox('Exercise-Induced Angina', ['0', '1'], index=0)
    Oldpeak = st.number_input('ST Depression induced by Exercise', min_value=0.0, max_value=10.0, step=0.1, value=0.0)
    ST_Slope = st.selectbox('ST Slope', ['0', '1', '2'], index=0)
    
    # Prediction code
    if st.button('Predict', key='predict_button'):
        try:
            # Convert input values to appropriate types
            Gender = 1 if Gender == 'Male' else 0
            ChestPainType = float(ChestPainType)
            FastingBS = float(FastingBS)
            ExerciseAngina = float(ExerciseAngina)
            ST_Slope = float(ST_Slope)
            
            # Make prediction
            input_data = [[Age, Gender, ChestPainType,RestingBP , Cholesterol, FastingBS, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]]
            make_prediction = model.predict(input_data)
            prediction = make_prediction[0]
            
            # Display prediction result
            if prediction == 1:
                st.error('Emergency Alert: Potential Heart Failure Detected! Seek immediate medical attention.')
            else:
                st.success('No Immediate Risk Detected. Continue monitoring your health.')
        except ValueError:
            st.error('Please enter valid values for all input fields.')

    # Add viewport meta tag
    st.markdown(
        """
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()