
from random import choices

import pandas as pd
import numpy as np
import streamlit as st
st.set_page_config(layout="wide")


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


def main():
	"""Welcome to E-Hospital"""

	st.title("Welcome to MSBA's e-Hospital")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		
		
		html_string3 ='<a href="https://im.ge/i/ujJwLL"><img src="https://i.im.ge/2022/07/06/ujJwLL.webp" alt="ujJwLL.webp" border="0"></a>'
		st.markdown(html_string3, unsafe_allow_html= True)
		st.markdown("<h1 style='text-align: left; color: Red;'>You have Reached the Stroke Web Pannel</h1>", unsafe_allow_html=True)

		st.write("Please Login or Signup if New!This web application is restricted to certain individuals only due to the confidentiality of the data and thus would require access permission.")

		

        
        

        
        
        

	elif choice == "Login":
        
		st.subheader("Login Section")
        

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Welcome you're logged in as {}".format(username))

				Select = st.selectbox("Selection",["upload data","Data Exploration","Registered Users"])
				if Select == "upload data":
					
					uploaded_data = st.file_uploader('Upload dataset', type='csv')
					if uploaded_data:
						df= pd.read_csv(uploaded_data)
						st.markdown("<h1 style='text-align: center; color: red;'>Introduction</h1>", unsafe_allow_html=True)
						st.write("""Stroke is one of the leading causes of death worldwide. It can lead to long term disabilities if not a short-termm death. Therefore, managing Stroke's leading risk factors and trying to predict a stroke before happening is paramount.This web application will aims to provide a closer look at stroke in general, identify risk factors correlations and insights sing various data sources and help in the prediction of a potential stroke in favor of preventing it.""")
						
    					
						
    					


				elif Select == "Data Exploration":
					uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
					if uploaded_data:
						df=pd.read_csv(uploaded_data)
						st.sidebar.header("filter Through")
						gender=st.sidebar.multiselect("select Gender:",options=df["gender"].unique(),default= df["gender"].unique())
						Marriage=st.sidebar.multiselect("select Marital Status:",options=df["ever_married"].unique(),default= df["ever_married"].unique())
						Smoking=st.sidebar.multiselect("select Smoking status:",options=df["smoking_status"].unique(),default= df["smoking_status"].unique())

						df_selection =df.query("gender == @gender & ever_married == @Marriage & smoking_status ==@Smoking")

						st.dataframe(df_selection)
    					


				elif Select == "Registered Users":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
                    
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		st.title("""Please sign in to request access""")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")


	


if __name__ == '__main__':
	main()










#menu = ["Login","signup"]
#choice = st.sidebar.selectbox("Menu",menu)

#if choice == "Login":
    #st.subheader("Login Section")

    #username = st.sidebar.text_input("Username")
    #password = st.sidebar.text_input("password", type="password")
    #if st.sidebar.button("Login"):
        #st.success("Logged in as {}".format(username))

        #st.markdown("""Mohamad""")

        #st.title("Dbouking")