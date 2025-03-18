import streamlit as st
import requests

# Define the mapping of selections to image and text URLs


# Streamlit UI
st.title("Company Production & Delivery Dashboard")

# User inputs company name
company_name = st.text_input("Enter Company Name:")
company_name=company_name.upper()

data_links = {
    "delivery_annual": {
        "image": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/delivery_annual/delivery_annual.png",
        "text": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/delivery_annual/delivery_annual.txt",
    },
    "production_annual": {
        "image": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/production_annual/production_annual.png",
        "text": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/production_annual/production_annual.txt",
    },
    "delivery_quarterly": {
        "image":"https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/delivery_quarter/delivery_quarter.png",
        "text": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/delivery_quarter/delivery_quarter.txt",
    },
    "production_quarterly": {
        "image": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/production_quarter/production_quarter.png",
        "text": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/production_quarter/production_quarter.txt",
    },
    "delivery_comparison": {
        "image": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/quarter_comparison_delivery/quarter_comparison_delivery.png",
        "text": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/quarter_comparison_delivery/quarter_comparison_delivery.txt",
    },
    "production_comparison": {
        "image": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/quarter_comparison_production/quarter_comparison_production.png",
        "text": "https://checkitanalytics.s3.us-east-1.amazonaws.com/TESLA_PROD_DEL/graphs_and_explanations/quarter_comparison_production/quarter_comparison_production.txt",
    },
}
# Radio buttons for category selection
data_type = st.radio("Select Data Type:", ["Delivery", "Production"], index=None)

# Options for analysis type
analysis_type = st.selectbox(
    "Select Analysis Type:",
    ["Select an Option", "Annual", "Quarterly", "Quarterly Comparison for Last Two Years"],
    index=0
)

# Display graph and text only after all selections are made
if company_name and data_type and analysis_type != "Select an Option":
    selection_key = f"{data_type.lower()}_{'comparison' if 'Comparison' in analysis_type else analysis_type.lower()}"
    
    if selection_key in data_links:
        st.image(data_links[selection_key]["image"], caption=f"{data_type} - {analysis_type}")
        
        # Fetch and display text content
        text_url = data_links[selection_key]["text"]
        response = requests.get(text_url)
        if response.status_code == 200:
            st.markdown("""
                <div style="padding:10px; background-color:#f4f4f4; border-radius:10px;">
                    <p style="font-size:16px; color:#333;">""" + response.text.replace("\n", "<br>") + """</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Unable to load description text.")

