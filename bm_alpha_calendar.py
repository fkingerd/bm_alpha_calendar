import streamlit as st
import pandas as pd

# Function to load data
@st.cache_data
def load_data():
    df = pd.read_csv('twitters.csv')
    return df

# Load data
df = load_data()

# Function to create hyperlinked values
def hyperlink(column):
    if column.empty:
        return column
    return column.apply(lambda x: f'<a href="{x}" target="_blank">{x.split(".com/")[1]}</a>')

# Create a calendar app using Streamlit
st.title("BM/Alpha Calendar App")

# Filter data by category
categories = df["Category"].unique()
category = st.sidebar.selectbox("Select Category", categories)

# Filter the data based on the selected category
filtered_df = df[df["Category"] == category]

# Check if 'Link' column exists and create hyperlinked values
if "Link" in filtered_df.columns:
    filtered_df["Link"] = hyperlink(filtered_df["Link"])

# Check if 'Date' column exists for "Minting soon" category
# and make sure the Date column is displayed in the correct format
if category == "Minting soon" and "Date" in filtered_df.columns:
    filtered_df['Date'] = filtered_df['Date'].astype(str)

# Display data for the selected category
st.subheader(f"{category} Category")
st.write(filtered_df.to_html(escape=False, index=False), unsafe_allow_html=True)

st.write('\n')
bm_discord_invite_link = lambda x: f'<a href="https://discord.gg/EqcHvkgBdg" target="_blank">Join Black Mage Discord</a>'
st.markdown(bm_discord_invite_link(None), unsafe_allow_html=True)
