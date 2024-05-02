import pickle
import streamlit as st 

model = pickle.load(open('C:/Users/Ziad/Desktop/heartrate/logistic_regression_model.pkl', 'rb'))

def main():
    st.title('CardioCare: Heart Failure Prediction')
    
    # Input Variables
    Age = st.text_input('AGE')
    Gender = st.text_input('Gender')
    ChestPainType = st.text_input('ChestPainType') 
    Cholesterol = st.text_input('Cholesterol')
    FastingBS = st.text_input('FastingBS')
    MaxHR = st.text_input('MaxHR')
    ExerciseAngina = st.text_input('ExerciseAngina')
    Oldpeak = st.text_input('Oldpeak')
    ST_Slope = st.text_input('ST_Slope')
    
    # Prediction code
    if st.button('Predict'):
        if '' not in [Age, Gender, ChestPainType, Cholesterol, FastingBS, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]:
            try:
                # Convert input values to float
                Age = float(Age)
                Gender = float(Gender)  # Assuming '1' represents male and '0' represents female
                ChestPainType = float(ChestPainType)  # Assuming '1', '2', '3', '4' as numeric values
                Cholesterol = float(Cholesterol)
                FastingBS = float(FastingBS)
                MaxHR = float(MaxHR)
                ExerciseAngina = float(ExerciseAngina)
                Oldpeak = float(Oldpeak)
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

if __name__ == '__main__':
    main()