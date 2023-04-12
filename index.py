# Berikut kode tampilan app.py
import streamlit as st
import time
from PIL import Image
from prediksi import predict
import cv2
import numpy as np


def show(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.set_option('deprecation.showfileUploaderEncoding', False)


        st.sidebar.markdown("<h2 style='text-align: center; color: #ff8720;'>Informasi Tambahan</h2>", unsafe_allow_html=True)
        st.sidebar.markdown("""
                <p style='color: #ff8720;'>Skripsi :</p>
                <ol style='color: #ff8720;'>
                    <li>Moch. Andyka Saputra</li>
                    <li>Dr. Wahyudi Setaiawan, S.Kom., M.Kom.</li>
                    <li>Dr. Meidya Koeshardianto, S.Si., M.T.</li>
                    <li>Eka Malasari Rochman, S.Kom., M.Kom.</li>
                    <li>Husni, S.Kom., M.T.</li>
                    <li>Muhammad Ali Syakur, S.Si., M.T.</li>
                </ol>
                """, unsafe_allow_html=True)
        st.sidebar.markdown("")
        st.sidebar.markdown("")
        st.sidebar.markdown("")
        st.sidebar.markdown("")
        st.sidebar.markdown("<h3 style='text-align: center; color: #ff8720;'>Power By</h3>", unsafe_allow_html=True)
        st.sidebar.markdown("""
        <p align="center">
            <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/UTM_DIKBUDRISTEK.png/800px-UTM_DIKBUDRISTEK.png" alt="Logo UTM">
        </p>
        """, unsafe_allow_html=True)
        st.sidebar.markdown("<h4 style='text-align: center; color: #ff8720;'>Copyright &copy; 2023</h4>", unsafe_allow_html=True)


        st.markdown("<h2 style='text-align: center;'>Classification Maize Seed</h2>", unsafe_allow_html=True)
        st.write("")
        st.write("""
        <p>Rule :</p>
        <ul>
            <li>Klasifikasi ini hanya untuk gambar benih jagung</li>
            <li>Akurasi dari program ini 96.83%</li>
            <li>Hasil output dari program ini ada 2, yaitu: Haploid/Diploid</li>
        </ul>
        """, unsafe_allow_html=True)
        st.write("")
        st.write("")

        file_up = st.file_uploader("Upload an image")

        if file_up is not None:
            image = Image.open(file_up)
            classes = ('Haploid', 'Diploid')

            # konversi file_up menjadi numpy array
            img = np.array(image.convert('RGB'))

            # lakukan resize dan normalisasi pada numpy array
            img = cv2.resize(img, (224, 224))
            st.image(img, caption='Upload Image.', use_column_width=True)
            img = img.astype("float32") / 255.0

            # lakukan prediksi pada numpy array
            labels = predict(img)

            hasil = classes[labels]
            st.write("<p class='pred'>Predicted : {}</p>".format(hasil), unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="UTM|Classification Maize Seed", page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/UTM_DIKBUDRISTEK.png/800px-UTM_DIKBUDRISTEK.png")
    show("style.css")