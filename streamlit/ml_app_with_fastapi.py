import streamlit as st
import requests
import json

st.set_page_config(layout='wide')

st.title('Elderly People Safety Predictor')
st.image("""https://anlan.ru/files/uploads/datchik-dvizheniya-na-stene.jpg""")
st.header('Enter the characteristics of the room:')

model = st.selectbox('Model:', ['LogReg', 'SVM'])
t = st.number_input('temperature:', min_value=-50.0, max_value=100.0, value=20.0)
h = st.number_input('humidity:', min_value=0.0, max_value=100.0, value=50.0)
co2 = st.number_input('CO2MG811Value:', min_value=0.0, max_value=200.0, value=70.0)
mox1 = st.number_input('MOX1:', min_value=0.0, max_value=1000.0, value=540.0)
mox2 = st.number_input('MOX2:', min_value=0.0, max_value=1000.0, value=700.0)
cov = st.number_input('COValue:', min_value=0.0, max_value=1000.0, value=120.0)
hour = st.number_input('Time hour:', min_value=0, max_value=24, value=12)

inputs = {'model': model, 't': t, 'h': h, 'co2': co2, 'mox1': mox1,
          'mox2': mox2, 'cov': cov, 'hour': hour}

if st.button('Predict Price'):
    danger_risk = requests.post(url="http://ml_services_fastapi_1:8502/model-predict", data=json.dumps(inputs))
    print(danger_risk.text)
    # if float(danger_risk.text) > 0.5:
    #     text = 'Call the ambulance!'
    # else:
    #     text = 'Situation is fine'
    text = '?'
    st.success(f'The predicted chance of danger is {danger_risk.text}\n{text}')


