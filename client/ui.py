import streamlit as st
import utils

st.set_page_config(layout='centered',page_title="Vehicle CO\u2082 Emission",page_icon=":car:")
st.markdown(
"""
<style> 
.stDeployButton {
    visibility: hidden;
}
#MainMenu {
    visibility: hidden;
}
div.row-widget.stButton{
    text-align: center
}
</style>
""", unsafe_allow_html=True)

st.markdown("""<h1 style="text-align:center; color:blue">Vehicle CO\u2082 Emission Prediction<h1/>""",unsafe_allow_html=True)

categories = utils.get_categories()

if 'enable_button' not in st.session_state:
    st.session_state.enable_button = False

with st.container():

    make = st.selectbox(label=":blue[Manufacturer]", options=categories['make'], index=None, placeholder="Choose the Manufacturer")
    vehicle_class = st.selectbox(label=":blue[Vehicle Class]", options=categories['vehicle_class'], index=None, placeholder='Choose the Vehicle Class')
    cylinders = st.selectbox(label=":blue[Cylinders]", options=categories['cylinders'], index=None, placeholder='Choose the amount of Cylinders')
    transmission = st.selectbox(label=":blue[Transmission Type]", options=categories['transmission_type'], index=None, placeholder='Choose the Transmission Type')
    fuel_type = st.selectbox(label=":blue[Fuel Type]", options=categories['fuel_type'], index=None, placeholder='Choose the Fuel Type')
    engine_size = st.number_input(label=":blue[Engine Size]",value=None,placeholder='Enter the Engine Size in litres',min_value=0.0,step=.1)
    fuel_consumption = st.number_input(label=":blue[Fuel Consumption]",value=None,placeholder='Enter the Fuel Consumption in litres per 100 kilometres',min_value=0.0,step=.1)
    gear = st.number_input(label=":blue[Gear]",step=1,value=None,placeholder='Enter the Gear Count',min_value=0)    
    
    st.session_state.enable_button = utils.button_availability(make,vehicle_class,cylinders,transmission,fuel_type,engine_size,fuel_consumption,gear)
    submitted = st.button(label=":blue[Predict Emission]",disabled=not st.session_state.enable_button)
  
    if submitted:
        prediction = utils.get_prediction(make,vehicle_class,cylinders,transmission,fuel_type,engine_size,fuel_consumption,gear)
        col1, col2, col3 = st.columns(3)
        col2.metric(label=":blue[Emission]",value=f'{prediction} g/km',
                      delta=round(250-prediction,2),
                      help="Delta represents the difference between the predicted emission value and the mean emission value, indicating how far the prediction is from the average.")

clear = st.button(label=":blue[Clear Output]")