import streamlit as st
import os
import pandas as pd
from dif import *
from PIL import Image
import shutil

st.set_page_config(
    page_title="Duplicate Image Finder",
    page_icon="🖼",
    layout="wide",
    initial_sidebar_state="auto",
)

@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def clean_directory(dir):
    shutil.rmtree(dir)
    os.makedirs(dir)

single_folder_upload_path = "single_uploads/"
multi_folder1_upload_path = "multi_uploads/folder_1/"
multi_folder2_upload_path = "multi_uploads/folder_2/"

clean_directory(single_folder_upload_path)
clean_directory(multi_folder1_upload_path)
clean_directory(multi_folder2_upload_path)

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')

st.sidebar.image(top_image,use_column_width='auto')
selection_choice = st.sidebar.selectbox('Search for duplicate Images under? 🎯',["Single Directory","Two Directories"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.title("👨‍💻 Duplicate Image Finder 📷")
st.info('✨ Supports all popular image formats 📷 - PNG, JPG, BMP 😉')

if selection_choice == "Single Directory":
    uploaded_files = st.file_uploader("Upload Images 🚀", type=["png","jpg","bmp","jpeg"], accept_multiple_files=True)
    with st.spinner(f"Working... 💫"):
        if uploaded_files:
            for uploaded_file in uploaded_files:
                with open(os.path.join(single_folder_upload_path,uploaded_file.name),"wb") as f:
                    f.write((uploaded_file).getbuffer())

            search = dif("single_uploads/")

            dup_imgs = [key for key in search.result.keys()]
            low_res_imgs = [str(img.split("/")[-1]) for img in search.lower_quality]
            stats_metrics = [search.stats[key] for key in search.stats.keys()]
            time_metrics = [stats_metrics[2][key] for key in stats_metrics[2].keys()]

            similarity_grade = str(stats_metrics[3])
            similarity_mse = str(stats_metrics[4])
            total_imgs_searched = str(stats_metrics[5])
            total_imgs_found = str(stats_metrics[6])
            strt_datetime = str(time_metrics[0])+ " " + str(time_metrics[1])
            end_datetime = str(time_metrics[2])+ " " + str(time_metrics[3])
            secs_elapsed = str(time_metrics[-1])

            df  = pd.DataFrame(columns = ['names of duplicate images'])
            df['names of duplicate images'] = dup_imgs
            df['names of lowest quality images'] = low_res_imgs

            if len(total_imgs_searched) != 0:
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Total Images Searched", total_imgs_searched)
                    col2.metric("Duplicate Images Found", total_imgs_found)
                    col3.metric("Lowest Quality Images Found", len(low_res_imgs))

                    col1.metric("Similarity Grade", similarity_grade.title())
                    col2.metric("Similarity MSE", similarity_mse)
                    col3.metric("Seconds Elapsed", secs_elapsed)
                    with col2:
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.dataframe(df)

        else:
            st.warning('⚠ Please upload your images! 😯')

if selection_choice == "Two Directories":
    main_col1, main_col2 = st.columns(2)
    with main_col1:
        multi_folder1_uploaded_files = st.file_uploader("Upload Images (folder 1)🖼", type=["png","jpg","bmp","jpeg"], accept_multiple_files=True)

    with main_col2:
        multi_folder2_uploaded_files = st.file_uploader("Upload Images (folder 2)🖼", type=["png","jpg","bmp","jpeg"], accept_multiple_files=True)

    with st.spinner(f"Working... 💫"):
        if multi_folder1_uploaded_files and multi_folder2_uploaded_files:
            for uploaded_file in multi_folder1_uploaded_files:
                with open(os.path.join(multi_folder1_upload_path,uploaded_file.name),"wb") as f:
                    f.write((uploaded_file).getbuffer())

            for uploaded_file in multi_folder2_uploaded_files:
                with open(os.path.join(multi_folder2_upload_path,uploaded_file.name),"wb") as f:
                    f.write((uploaded_file).getbuffer())

            search = dif("multi_uploads/folder_1/", "multi_uploads/folder_2/")

            dup_imgs = [key for key in search.result.keys()]
            low_res_imgs = [str(img.split("/")[-1]) for img in search.lower_quality]
            stats_metrics = [search.stats[key] for key in search.stats.keys()]
            time_metrics = [stats_metrics[2][key] for key in stats_metrics[2].keys()]

            similarity_grade = str(stats_metrics[3])
            similarity_mse = str(stats_metrics[4])
            total_imgs_searched = str(stats_metrics[5])
            total_imgs_found = str(stats_metrics[6])
            strt_datetime = str(time_metrics[0])+ " " + str(time_metrics[1])
            end_datetime = str(time_metrics[2])+ " " + str(time_metrics[3])
            secs_elapsed = str(time_metrics[-1])

            df  = pd.DataFrame(columns = ['names of duplicate images'])
            df['names of duplicate images'] = dup_imgs
            df['names of lowest quality images'] = low_res_imgs

            if len(total_imgs_searched) != 0:
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Total Images Searched", total_imgs_searched)
                    col2.metric("Duplicate Images Found", total_imgs_found)
                    col3.metric("Lowest Quality Images Found", len(low_res_imgs))

                    col1.metric("Similarity Grade", similarity_grade.title())
                    col2.metric("Similarity MSE", similarity_mse)
                    col3.metric("Seconds Elapsed", secs_elapsed)
                    with col2:
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.dataframe(df)
        else:
            st.warning('⚠ Please upload your images! 😯')


st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Instance Segmentator WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a> with the help of [difPy](https://github.com/elisemercury/Duplicate-Image-Finder) built by [elsiemercury](https://github.com/elisemercury) ✨</center><hr>", unsafe_allow_html=True)



