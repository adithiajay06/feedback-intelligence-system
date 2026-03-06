import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Feedback Intelligence Hub", layout="wide")

# 2. PDF GENERATION LOGIC
def create_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Feedback Intelligence Weekly Report", ln=True, align='C')
    pdf.ln(10)
    
    # Summary Statistics
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Executive Summary", ln=True)
    pdf.set_font("Arial", size=12)
    
    pos = len(df[df['Status'] == 'Positive'])
    neu = len(df[df['Status'] == 'Neutral'])
    neg = len(df[df['Status'] == 'Negative'])
    
    pdf.cell(200, 10, txt=f"Total Reviews Analyzed: {len(df)}", ln=True)
    pdf.cell(200, 10, txt=f"Positive: {pos} | Neutral: {neu} | Negative: {neg}", ln=True)
    pdf.ln(10)

    # Top Issues Section
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Sample Critical Feedback:", ln=True)
    pdf.set_font("Arial", size=10)
    
    # Grab top 5 negative reviews and clean them for PDF compatibility
    neg_list = df[df['Status'] == 'Negative']['Review'].head(5)
    for review in neg_list:
        # This cleaning step is CRITICAL to prevent PDF crashes from emojis
        clean_text = str(review).encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 10, txt=f"- {clean_text[:150]}...") 
        pdf.ln(2)
        
    return pdf.output(dest='S').encode('latin-1')

# 3. DASHBOARD UI
st.title("📊 App Feedback Intelligence Dashboard")
st.markdown("Real-time analysis of Google Play Store reviews")

# Load the data generated in Phase 2
try:
    df = pd.read_csv("analyzed_reviews.csv")
    
    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filters")
    status_filter = st.sidebar.multiselect(
        "Select Sentiment Labels:",
        options=df['Status'].unique(),
        default=df['Status'].unique()
    )

    filtered_df = df[df['Status'].isin(status_filter)]

    # --- TOP METRICS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Filtered", len(filtered_df))
    col2.metric("Avg Sentiment Score", round(filtered_df['Sentiment_Score'].mean(), 2))
    col3.metric("Negative Count", len(df[df['Status'] == 'Negative']))

    # --- VISUAL CHARTS ---
    st.divider()
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Sentiment Distribution")
        fig = px.pie(df, names='Status', color='Status',
                     color_discrete_map={'Positive':'#2ecc71', 'Neutral':'#95a5a6', 'Negative':'#e74c3c'})
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("Ratings Distribution")
        fig2 = px.histogram(filtered_df, x='Rating', color='Status', nbins=5, 
                           color_discrete_map={'Positive':'#2ecc71', 'Neutral':'#95a5a6', 'Negative':'#e74c3c'})
        st.plotly_chart(fig2, use_container_width=True)

    # --- DATA TABLE ---
    st.subheader("Review Details")
    st.dataframe(filtered_df[['Date', 'Rating', 'Status', 'Review']], use_container_width=True)

    # --- EXPORT SECTION ---
    st.divider()
    st.subheader("📩 Export Stakeholder Report")
    if st.button("Step 1: Prepare PDF Data"):
        pdf_bytes = create_pdf(df)
        st.success("PDF Ready for download!")
        st.download_button(
            label="Step 2: Download Weekly Report",
            data=pdf_bytes,
            file_name="App_Feedback_Report.pdf",
            mime="application/pdf"
        )

except FileNotFoundError:
    st.error("Error: 'analyzed_reviews.csv' not found. Please run analyze_sentiment.py first!")