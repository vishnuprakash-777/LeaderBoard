import streamlit as st
import pandas as pd

# Sample data for departments and points
data = {
    'Department': [
        'Computer Science', 'Economics', 'Commerce', 'Plant Science', 
        'Polymer Chemistry', 'Maths', 'English', 'History', 
        'Malayalam', 'Statistics', 'Physics', 'Zoology'
    ],
    'Points': [16, 0, 5, 3, 13, 0, 0, 21, 13, 19, 5, 0]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Sorting the DataFrame by points in descending order
df = df.sort_values(by='Points', ascending=False)

# Reindexing the DataFrame to start from 1
df.index = range(1, len(df) + 1)

# Reordering columns to display Index (starting from 1), Department, and Points
df = df[['Department', 'Points']]

# Streamlit app with improved styling
st.set_page_config(page_title="Pravda Nehru College Union Kalolsavam")  # Fullscreen layout

# App Title
st.markdown("<h1 style='text-align: center; color: #ffffff;'>Pravda Nehru College Union Kalolsavam</h1>", unsafe_allow_html=True)

# Subtitlent
st.markdown("<h3 style='text-align: center; color: #ffffff;'>Leaderboard On-Stage</h3>", unsafe_allow_html=True)

# Define a function to highlight the top 3 rows
def highlight_top_rows(row):
    if row.name < 4:  # Highlight top 3 rows (index 0, 1, 2 internally)
        return ['background-color: #FFF4CC; color: black; font-weight: bold;'] * len(row)
    return [''] * len(row)

# Apply the highlighting to the DataFrame
styled_df = df.style.apply(highlight_top_rows, axis=1).set_table_styles([
    {
        'selector': 'thead th',
        'props': [('background-color', '#444444'), ('color', '#ffffff'), ('text-align', 'center'), ('font-weight', 'bold')]
    },
    {
        'selector': 'tbody td',
        'props': [('text-align', 'center'), ('font-size', '16px')]
    },
    {
        'selector': 'table',
        'props': [('width', '60%'), ('margin', '0 auto')]  # Reduced width to 60% and centered
    }
])

# Displaying the leaderboard
st.table(styled_df)
