import streamlit as st


st.title("Unit Convertor App")
st.markdown("### Converts Length, Weight, And Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

# Select category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Set unit options based on category
if category == "Length":
    unit = st.selectbox("Choose a unit conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Choose a unit conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Choose a unit conversion", ["Seconds to Minutes", "Minutes to Hours",
                                                      "Hours to Days", "Days to Hours"])

# Input value
value = st.number_input("Enter the value you want to convert", min_value=0.0, format="%.2f")

# Conversion function
def convert_unit(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462 
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None

# Show result if value is entered
if value:
    result = convert_unit(category, value, unit)
    if result is not None:
        st.success(f"Converted Value: {result:.2f}")
    else:
        st.error("Conversion not available.")
