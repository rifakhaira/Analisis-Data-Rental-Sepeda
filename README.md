# Setup Environmet
conda create--name main-ds python=3.9
conda active main-ds
pip install -r requirements.txt

# Run Streamlit
streamlit run dashboard.py
