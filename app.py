import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import io

web_apps = st.sidebar.selectbox("Select Web Apps",
                                ("Exploratory Data Analysis", "Pairplot for Dataset"))


if web_apps == "Pairplot for Dataset":

  uploaded_file = st.sidebar.file_uploader("Choose a file")

  if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    show_df = st.checkbox("Show Data Frame", key="disabled")
    show_5num = st.checkbox("Show 5 Number Summary", key = "disabledd")
    showdatainfo = st.checkbox("Show Info About Dataset", key = 'disableddd')

    if show_df:
      st.write(df)

    if showdatainfo:
      st.write("Rows and columns:", df.shape, "\nCounts of variables:", df.count())

    if show_5num:
        st.write(df.describe())

    fig = sns.pairplot(data = df)
    st.pyplot(fig)
    


if web_apps == "Exploratory Data Analysis":

  uploaded_file = st.sidebar.file_uploader("Choose a file")

  if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    show_df = st.checkbox("Show Data Frame", key="disabled")
    showdatainfo = st.checkbox("Show Info About Dataset", key = 'disableddd')
    

    if show_df:
      st.write(df)

    if showdatainfo:
      st.write("Rows and columns:", df.shape, "\nCounts of variables:", df.count())

    column_type = st.sidebar.selectbox('Select Data Type',
                                       ("Numerical", "Categorical"))

    if column_type == "Numerical":
      show_5num = st.checkbox("Show 5 Number Summary", key = "disabledd")

      numerical_column = st.sidebar.selectbox(
          'Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)
      
      if show_5num:
        st.write(df[numerical_column].describe())

      # histogram
      choose_color = st.color_picker('Pick a Color', "#687FF3")
      choose_opacity = st.slider(
          'Color Opacity', min_value=0.0, max_value=1.0, step=0.05, value= 0.5)

      hist_bins = st.slider('Number of bins', min_value=5,
                            max_value=150, value=30)
      hist_title = st.text_input('Set Title', 'Histogram')
      hist_xtitle = st.text_input('Set x-axis Title', numerical_column)

      fig, ax = plt.subplots()
      ax.hist(df[numerical_column], bins=hist_bins,
              edgecolor="black", color=choose_color, alpha=choose_opacity)
      ax.set_title(hist_title)
      ax.set_xlabel(hist_xtitle)
      ax.set_ylabel('Count')

      st.pyplot(fig)
      filename = "plot.png"
      fig.savefig(filename,dpi = 300)

      # Display the download button
      with open("plot.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )

    if column_type == "Categorical":
      categorical_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include=['object', 'bool']).columns)

      # barplot
      choose_color = st.color_picker('Pick a Color', "#687FF3")
      choose_opacity = st.slider('Color Opacity', min_value=0.0, max_value=1.0, step=0.05, value = 0.5)
      bplot_title = st.text_input('Set Title', 'Barplot')
      bplot_xtitle = st.text_input('Set x-axis Title', categorical_column)

      fig, ax = plt.subplots()
      sns.countplot(data = df, x = categorical_column, edgecolor="black", color=choose_color, alpha=choose_opacity)
      ax.set_title(bplot_title)
      ax.set_xlabel(bplot_xtitle)
      ax.set_ylabel('Count')

      st.pyplot(fig)
      filename = "plot.png"
      fig.savefig(filename,dpi = 300)

      # Display the download button
      with open("plot.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )
