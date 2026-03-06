📊 Feedback Intelligence Multi-Source System
An end-to-end data engineering and NLP pipeline that scrapes app reviews from the Google Play Store, performs sentiment analysis using Natural Language Processing (NLP), and visualizes the insights in a real-time web dashboard.

🚀 Features
Real-time Scraping: Fetches the latest user reviews directly from the Google Play Store.

Sentiment Analysis: Categorizes feedback as Positive, Neutral, or Negative using NLP.

Interactive Dashboard: Built with Streamlit to filter data and visualize ratings distribution.

Automated Reporting: Generates and downloads a stakeholder-ready PDF report.

Cloud Deployed: Accessible from any browser via Streamlit Community Cloud.

🛠️ Tech Stack
Language: Python 3.11+

Data Handling: Pandas, NumPy

NLP: TextBlob / NLTK

Visualization: Plotly, Streamlit

Reporting: FPDF

📂 Project Structure
Plaintext
├── dashboard.py           # Main Streamlit web application
├── scripts/
│   ├── fetch_reviews.py   # Script to scrape Play Store data
│   └── find_issues.py     # Script for keyword extraction
├── analyzed_reviews.csv   # The processed dataset
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation
⚙️ Installation & Setup
Clone the repository:

Bash
https://github.com/adithiajay06/feedback-intelligence-system
cd feedback_intelligence_multi_source_hidevs
Install dependencies:

Bash
pip install -r requirements.txt
Run the dashboard locally:

Bash
streamlit run dashboard.py
📈 Dashboard Preview
(Insert a screenshot of your live Streamlit dashboard here to show it off!)

🎥 Project Demo
[Link to your YouTube Demo Video]
In this video, I demonstrate the full pipeline from data extraction to automated PDF reporting.

🤝 Contact
Developed by Adithi.A
