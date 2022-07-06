
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from streamlit_option_menu import option_menu

st.markdown("<h1 style='text-align: center; color: Blue;'>Self Diagnosis</h1>", unsafe_allow_html=True)



selected= option_menu(menu_title=None, options=["model","contact"],icons=['book','book'],orientation='horizontal')





if selected =='model':
    import pandas as pd
    import streamlit as st
    import pandas as pd
    import streamlit as st
    import plotly.express as px
    import random
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split as tts

    uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
    df = pd.read_csv(uploaded_data)

    if uploaded_data:
        del df["id"]
        df = df.dropna()
        df = df[df['age'] >= 2]
        df = df[df['gender'] != 'Other']
    ###

        df2 = df
        df2['stroke'] = df2['stroke'].replace([0],'No')
        df2['stroke'] = df2['stroke'].replace([1],'Yes')
        df2['Count'] = 1

        df2 = df2.sort_values(
        by=['stroke'],
        ascending=False).iloc[0:len(df2[df2['stroke']=='Yes'])*2]

        

        cleanup_vals = {"gender": {"Male": 0, "Female": 1},
                    "ever_married": {"No": 0, "Yes": 1},
                    "work_type": {"Never_worked": 0, "children": 1, "Self-employed": 2, "Private": 3, "Govt_job": 4},
                    "Residence_type" : {"Urban": 0, "Rural": 1},
                    "smoking_status": {"Unknown": 0, "never smoked": 1, "formerly smoked": 2, "smokes": 3}}

    # df['avg_glucose_level']=df['avg_glucose_level'].apply(lambda x: x * 100)
    # predict_df['avg_glucose_level'].iloc[0]=predict_df['avg_glucose_level'].iloc[0]*100
    # df['bmi']=df['bmi'].apply(lambda x: x * 10)
    # predict_df['bmi']=predict_df['bmi'].apply(lambda x: x * 10)

        df = df.replace(cleanup_vals)
        df = df.drop(columns=['Count'], axis=1)

        y=df['stroke']
        x=df.drop('stroke',axis=1)

        x_train,x_test,y_train,y_test=tts(x,y,test_size=0.25)

        rf = RandomForestClassifier(n_estimators=25, random_state=0)
        rf.fit(x_train, y_train) 

        def user_report():
            st.write("""Male =0 , Female = 1""")
            gender =st.radio('Sex:',options=[0,1])
            st.write("""Type your age""")
            age=st.text_input('Age:', max_chars=3, value=0)
            st.write("""No hypertension = 0, otherwise 1""")
            hypertension=st.select_slider('Hypertension',options=[0,1])
            st.write("""No hypertension = 0, otherwise 1""")
            heart_disease=st.select_slider('Heart Disease: (0 for no Heart Disease, 1 for Heart Disease)',options=[0,1])
            st.write("""Yes=1, 0 otherwise""")
            ever_married=st.radio('Ever Married:', options=[0,1])
            st.write("Never_worked: 0, children: 1, Self-employed: 2, Private: 3, Govt_job: 4")
            work_type=st.select_slider('Work Type:', options=[0,1,2,3,4])
            st.write("Urban: 0, Rural: 1")
            Residence_type=st.radio('Residence Type:', options=[0,1])
            st.write("please type your average glucose level")
            avg_glucose_level=st.text_input('Average Glucose Level:', max_chars=6, value=0)
            st.write("please type your BMI")
            bmi=st.text_input('BMI:', max_chars=4, value=0)
            st.write("Unknown: 0, never smoked: 1, formerly smoked: 2, smokes: 3")
            smoking_status=st.select_slider('Smoking Status:', options=[0,1,2,3])

            user_report_data = {
        
            'gender':gender,
            'age':age,
            'hypertension':hypertension,
            'heart_disease':heart_disease,
            'ever_married':ever_married,
            'work_type':work_type,
            'Residence_type':Residence_type,
            'avg_glucose_level':avg_glucose_level,
            'bmi':bmi,
            'smoking_status':smoking_status
            }

            report_data =pd.DataFrame(user_report_data, index = [0])
            return report_data
    
        user_data = user_report()
        st.subheader('Prediction')
        st.write(user_data)

        outcome = (rf.predict(user_data))
        st.subheader('Stroke Prediction')
        st.subheader(outcome)
        st.title("please head to the contact page if the stroke prediction returned Yes")
if selected == 'contact':
    import pandas as pd
    st.markdown("<h1 style='text-align: center; color: green;'>Save Yourself While You can!</h1>", unsafe_allow_html=True)



    contact_form = """<form action="https://formsubmit.co/mad58@mail.aub.edu" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name="message" placeholder="Please Book an appointment if your entries returned 1"></textarea>
     <button type="submit">Send</button>
</form>"""


    st.markdown(contact_form, unsafe_allow_html= True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

    local_css("style.css")