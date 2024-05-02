import pickle
import streamlit as st 

# Load the model
model = pickle.load(open('logistic_regression_model.pkl', 'rb'))

def main():
    st.title('CardioCare: Heart Failure Prediction')
    
    # Input Variables
    Age = st.number_input('AGE', min_value=0, max_value=120, step=1, value=0)
    Gender = st.selectbox('Gender', ['Male', 'Female'], index=0)
    ChestPainType = st.selectbox('Chest Pain Level', ['0', '1', '2', '3'], index=0)
    RestingBP = st.number_input('Blood Pressure', min_value=0, max_value=1000, step=1, value=0)
    Cholesterol = st.number_input('Cholesterol', min_value=0, max_value=600, step=1, value=0)
    FastingBS = st.selectbox('Fasting Blood Sugar (If above 120 mg/dl choose yes)', ['Yes', 'No'], index=0)
    MaxHR = st.number_input('Maximum Heart Rate', min_value=0, max_value=300, step=1, value=0)
    ExerciseAngina = st.selectbox('Exercise-Induced Angina', ['Yes', 'No'], index=0)
    Oldpeak = st.number_input('Oldpeak', min_value=-2.6, max_value=10.0, step=0.1, value=0.0)
    ST_Slope = st.selectbox('ST depression induced by exercise Downsloping(0), Flat(1), Upsloping(2)', ['0', '1', '2'], index=0)
    
    # Prediction code
    if st.button('Predict', key='predict_button'):
        try:
            # Convert input values to appropriate types
            Gender = 1 if Gender == 'Male' else 0
            ChestPainType = float(ChestPainType)
            FastingBS = 1 if FastingBS == 'Yes' else 0
            ExerciseAngina = 1 if ExerciseAngina == 'Yes' else 0
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