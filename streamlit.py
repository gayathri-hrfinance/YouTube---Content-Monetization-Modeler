import streamlit as st
import pickle
import numpy as np

# Set background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fce4ec;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set page config
st.set_page_config(page_title="YouTube Revenue Predictor", layout="wide")

# Load model and scaler
with open('final_lr_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Initialize session state
if "show_form" not in st.session_state:
    st.session_state.show_form = False

# Landing Page
st.image("E:/YouTube/youtube.jpeg", use_column_width=True)  # Update path if needed
st.title("Welcome to the YouTube Revenue Prediction App")
st.markdown("This app helps you estimate your ad revenue based on video performance metrics.")

# Button to reveal input form
if st.button("Start Revenue Prediction"):
    st.session_state.show_form = True

# Show input form if button was clicked
if st.session_state.show_form:
    st.markdown("---")
    st.subheader("Please provide your video details below")

    col1, col2, col3 = st.columns([1.2, 1.2, 1.6])

    with col1:
        views = st.number_input("Views", min_value=0)
        likes = st.number_input("Likes", min_value=0)
        comments = st.number_input("Comments", min_value=0)
        watch_time_minutes = st.number_input("Watch Time (minutes)", min_value=0.0, step=0.1)
        subscribers = st.number_input("Subscribers", min_value=0)
        video_length_minutes = st.number_input("Video Length (minutes)", min_value=0)

    with col2:
        category = st.radio("Video Category", ["Entertainment", "Gaming", "Lifestyle", "Music", "Tech", "Education"])
        device = st.radio("Device Type", ["Mobile", "TV", "Tablet", "Desktop"])
        country = st.selectbox("Country", ["CA-Canada", "DE-Denmark", "IN-India", "UK-United Kingdom", "US-United States", "AU-Australia"])

    with col3:
        st.subheader("Prediction Output")
        if st.button("Click here to Predict the Revenue"):
            Views_Outlier_Flag = int(views > 500000 or views < 100)
            engagement_rate = (likes + comments) / views if views > 0 else 0
            watch_per_view = watch_time_minutes / views if views > 0 else 0

            # One-hot encoding
            category_Entertainment = int(category == "Entertainment")
            category_Gaming = int(category == "Gaming")
            category_Lifestyle = int(category == "Lifestyle")
            category_Music = int(category == "Music")
            category_Tech = int(category == "Tech")

            device_Mobile = int(device == "Mobile")
            device_TV = int(device == "TV")
            device_Tablet = int(device == "Tablet")

            country_CA = int(country == "CA-Canada")
            country_DE = int(country == "DE-Denmark")
            country_IN = int(country == "IN-India")
            country_UK = int(country == "UK-United Kingdom")
            country_US = int(country == "US-United States")

            input_data = np.array([[views, likes, comments, watch_time_minutes, video_length_minutes, subscribers,
                                    Views_Outlier_Flag, engagement_rate, watch_per_view,
                                    category_Entertainment, category_Gaming, category_Lifestyle,
                                    category_Music, category_Tech,
                                    device_Mobile, device_TV, device_Tablet,
                                    country_CA, country_DE, country_IN, country_UK, country_US]])

            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)
            predicted_value = max(0, prediction[0])

            st.markdown(f"<p style='font-size:36px;'>Predicted Revenue: ${predicted_value:,.2f}</p>", unsafe_allow_html=True)
