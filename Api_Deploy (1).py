# -*- coding: utf-8 -*-
"""API_Deploy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rnRzOW2FUZu7RVbreZ1HbEcOww2Lmfgc
"""

import pickle
import streamlit as st 


pickle_in = open("BankNote.pickle","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Fake Note Detection")
    variance = st.text_input("variance")
    skewness= st.text_input("skewness")
    curtosis = st.text_input("curtosis")
    entropy = st.text_input("entropy")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()