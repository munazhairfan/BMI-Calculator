import streamlit as st

st.set_page_config(layout="wide",page_title="Doctor",page_icon="💚")

st.markdown(
    """
    <style>
    .stApp{
        background-color: #daffc4;
    }

    div.stButton > button {
        background-color: #4CAF50 !important; /* Green */
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background-color: #45a049 !important; /* Darker Green */
    }

    div[data-testid="stRadio"] > label {
        font-size: 18px !important;
        color: #333333 !important;
        font-weight: bold !important;
    }

    div[data-testid="stRadio"] {
        background-color: #a1cf85 !important;
        padding: 10px !important;
        border-radius: 10px !important;
        width: fit-content !important;
    }
    [data-testid="stVerticalBlock"] {
        background-color: #a1cf85 !important;
        padding: 20px;
        border-radius: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])

def bmi_calculator(height, weight, age, gender, height_unit):
    try:
        height = float(height) if height.strip() else 0.0
        weight = float(weight) if weight.strip() else 0.0
        age = int(age) if age.strip() else 0
        if height == 0 or weight == 0 or age == 0:
            return "Please enter valid values.", None, None

        if height_unit == "feet":
            height = round(height * 0.3048, 2)
        elif height_unit == "centimetres":
            height = round(height / 100, 2)

        bmi = round(weight / (height ** 2), 1)

        adult_bmi_range = (18.5, 25) if gender == "Male" else (18.5, 24)

        if age < 5:
            healthy_bmi_min, healthy_bmi_max = 14, 18
        elif age < 10:
            healthy_bmi_min, healthy_bmi_max = 14.5, 19
        elif age < 15:
            healthy_bmi_min, healthy_bmi_max = 15, 21
        elif age < 18:
            healthy_bmi_min, healthy_bmi_max = 16, 23
        else:
            healthy_bmi_min, healthy_bmi_max = adult_bmi_range

        healthy_weight_min = round(healthy_bmi_min * (height ** 2), 1)
        healthy_weight_max = round(healthy_bmi_max * (height ** 2), 1)

        if bmi < healthy_bmi_min:
            category = f"Underweight (BMI < {healthy_bmi_min} kg/m²)"
        elif bmi > healthy_bmi_max:
            if bmi >= 30:
                category = f"Obese (BMI ≥ 30 kg/m²)"
            else:
                category = f"Overweight (BMI > {healthy_bmi_max} kg/m²)"
        else:
            category = "Healthy weight"

        result = f"BMI = {bmi} kg/m² ({category})"
        weight_range = f"Healthy weight range: {healthy_weight_min} - {healthy_weight_max} kg"

        return result, category, weight_range
    except ValueError:
        return "Invalid input. Please enter numbers only.", None, None


with col1:
    st.title("BMI Calculator")
    st.write("""BMI (body mass index) is a measure for adults to check what category their height and weight puts them in - underweight, healthy, or overweight.
    The calculator will give you an idea of how your weight compares to common values. Body Mass Index (BMI) is calculated as your weight divided by the square of your height or BMI = weight/height².""")

    with st.container():
        st.header("Calculate your BMI")
        st.subheader("Height")
        h_col1, h_col2 = st.columns(2)
        height = h_col1.text_input("Enter your height:", placeholder="0")
        height_unit = h_col2.selectbox("Choose the unit:", ["centimetres", "feet"])

        st.subheader("Weight")
        weight = st.text_input("Enter your weight in kg:", placeholder="0")

        a_col1, a_col2 = st.columns(2)
        a_col1.subheader("Age")
        age = a_col1.text_input("Enter your age:", placeholder="0")

        a_col2.subheader("Gender")
        gender = a_col2.radio("Select your gender:", ["Male", "Female"])

        if st.button("Calculate"):
            result, category, weight_range = bmi_calculator(height, weight, age, gender, height_unit)
            st.header("Results:")
            st.subheader(result)
            if category and weight_range:
                st.subheader(weight_range)


with col2:
    st.image("https://static.vecteezy.com/system/resources/previews/045/706/338/non_2x/body-mass-index-scale-infographics-of-underweight-and-normal-weight-vector.jpg")
    st.header("What your BMI score means")
    st.subheader("Underweight")
    st.write("""Being underweight might mean you're not getting all the nutrients, vitamins, and minerals that your body needs to be healthy. It may affect your skin, hair, and teeth, or you may feel more tired than you should. Women may have irregular periods and a greater chance of osteoporosis.
    You should speak to your doctor to find out why you have a low BMI and about how to gain weight healthily.""")

    st.subheader("Healthy weight")
    st.write("""Having a BMI score within the healthy weight range is a good sign that you are the right weight for your height. However, BMI does not tell you anything about the make-up of your body - such as how much muscle or fat you have, how much physical activity you do, or your body type.
    So, keep an eye on your general health, diet, and exercise and track any changes in your weight.""")

    st.subheader("Overweight")
    st.write("""If your BMI is in the overweight range, you may be more at risk of developing health conditions such as type 2 diabetes, heart disease, gallstones, and cancer.""")

    st.subheader("Obese")
    st.write("""If your BMI score is above 30, there is a high chance you have class 1 obesity. If it is between 35 and 40, you are in class 2 obesity. The chances of developing health issues associated with being overweight increase significantly if you are obese.""")
