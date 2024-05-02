import pickle
import streamlit as st 

model = pickle.load(open('logistic_regression_model.pkl', 'rb'))

def main():
    st.title('CardioCare: Heart Failure Prediction')
    
    # Input Variables
    Age = st.number_input('AGE')
    Gender = st.selectbox('Gender', ['Male', 'Female'])  # Use a selectbox for gender selection
    ChestPainType = st.selectbox('ChestPainType', ['1', '2', '3', '4'])  # Use a selectbox for ChestPainType
    Cholesterol = st.number_input('Cholesterol')
    FastingBS = st.selectbox('FastingBS', ['0', '1'])  # Use a selectbox for FastingBS
    MaxHR = st.number_input('MaxHR')
    ExerciseAngina = st.selectbox('ExerciseAngina', ['0', '1'])  # Use a selectbox for ExerciseAngina
    Oldpeak = st.number_input('Oldpeak')
    ST_Slope = st.selectbox('ST_Slope', ['0', '1', '2'])  # Use a selectbox for ST_Slope
    
    # Prediction code
    if st.button('Predict', key='predict_button'):
        if None not in [Age, Gender, ChestPainType, Cholesterol, FastingBS, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]:
            try:
                # Convert input values to appropriate types
                Gender = 1 if Gender == 'Male' else 0
                ChestPainType = float(ChestPainType)
                FastingBS = float(FastingBS)
                ExerciseAngina = float(ExerciseAngina)
                ST_Slope = float(ST_Slope)
                
                # Make prediction
                input_data = [[Age, Gender, ChestPainType, Cholesterol, FastingBS, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]]
                make_prediction = model.predict(input_data)
                prediction = make_prediction[0]
                
                # Display prediction result
                if prediction == 1:
                    st.success('Emergency Alert: Potential Heart Failure Detected! Based on the data provided, our prediction model indicates a potential risk of heart failure. We strongly advise seeking immediate medical attention. Please call emergency services or visit the nearest healthcare facility as soon as possible for a thorough evaluation and treatment. Remember, early intervention is crucial in managing heart-related emergencies. Stay calm and prioritize your health.')
                else:
                    st.success('No Immediate Risk Detected. Based on the data provided, our prediction model suggests that there is no immediate risk of heart failure. While this is encouraging, it is essential to continue monitoring your heart rate and maintain a healthy lifestyle.')
            except ValueError:
                st.error('Please enter valid numeric values for input.')
        else:
            st.error('Please fill all input fields.')

    # Add viewport meta tag
    st.markdown(
        """
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()