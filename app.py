import streamlit as st
from model_helper import predict


st.title("Car Damage Prediction")


uploaded_file = st.file_uploader(
    "Upload car image",
    type=["jpg","jpeg","png"]
)


if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded Image"
    )


    if st.button("Predict"):

        result = predict(uploaded_file)

        st.success(
            f"Damage Type: {result}"
        )
