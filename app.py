import streamlit as st
import requests
import json

def main():
    st.title("Profit prediction")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8000/predict")
    rd_spend = st.number_input("Inserisci spese di Ricerca e Sviluppo")
    administration = st.number_input("Inserisci spese di amministrazione")
    marketing_spend = st.number_input("Inserisci spese di marketing")


    ############## GET REQUEST #################
    if st.button("Predici Profit - GET"):
        url = url_API
        url2 = f"?RD_Spend={rd_spend}&administration={administration}&marketing_spend={marketing_spend}"
        link = url+url2
        response = requests.get(link)
        result =response.json()
        st.success(f"Profit prediction: {result}")

    ############## POST REQUEST #################
    if st.button("Predici Profit - POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "RD_Spend":rd_spend,
                                                   "administration":administration,
                                                   "marketing_spend":marketing_spend,
                                                   })
                                )
        result =response.json()
        st.success(f"Profit prediction : {result}")

if __name__ == '__main__':
    main()