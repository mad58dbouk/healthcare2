import pandas as pd
import streamlit as st

from streamlit_option_menu import option_menu


selected= option_menu(menu_title="Stroke types", options=["Ischemic Stroke","Hemorrhagic Stroke",'TIA (Transient Ischemic Attack)','Cryptogenic Stroke']
,icons=['heart','heart','heart','heart'],orientation='horizontal')

if selected =='Ischemic Stroke':
    st.markdown("<h1 style='text-align: center; color: Red;'>Ischemic Stroke (Clots)</h1>", unsafe_allow_html=True)

    html_string5 ='<a href="https://im.ge/i/uA49uq"><img src="https://i.im.ge/2022/07/06/uA49uq.jpg" alt="uA49uq.jpg" border="0"></a>'
    st.markdown(html_string5,unsafe_allow_html=True)

    st.write("When the blood flow to a portion of the brain is blocked or diminished, brain tissue cannot receive oxygen and nutrients, which results in an ischemic stroke. In minutes, brain cells start to degenerate.")


if selected == 'Hemorrhagic Stroke':
    st.markdown("<h1 style='text-align: center; color: Red;'>Hemorrhagic Stroke (Bleeds)</h1>", unsafe_allow_html=True)

    html_string6 ='<a href="https://im.ge/i/uABnZc"><img src="https://i.im.ge/2022/07/06/uABnZc.png" alt="uABnZc.png" border="0"></a>'
    st.markdown(html_string6, unsafe_allow_html= True)
    st.write("When blood from an artery suddenly starts bleeding into the brain, it results in a hemorrhagic stroke. As a result, the portion of the body that the damaged section of the brain controls cannot function normally.Hemorrhagic stroke can occur in two major ways:When there is bleeding inside the brain, it is known as an intracranial hemorrhage.Subarachnoid hemorrhages are when there is bleeding between the membranes covering the brain.")


if selected =='TIA (Transient Ischemic Attack)':
    st.markdown("<h1 style='text-align: center; color: Red;'>TIA (Transient Ischemic Attack)</h1>", unsafe_allow_html=True)

    html_string7 ='<a href="https://im.ge/i/uAGxcG"><img src="https://i.im.ge/2022/07/06/uAGxcG.jpg" alt="uAGxcG.jpg" border="0"></a>'
    st.markdown(html_string7, unsafe_allow_html= True)

    st.write("An episode of transient ischemic attack (TIA), which has symptoms resembling those of a stroke, occurs suddenly. A TIA typically lasts only a few minutes and has no lasting effects.A TIA, often known as a ministroke, may be an alert. A stroke will eventually occur in roughly 1 in 3 TIA patients, with about half happening within a year after the TIA.It can act as both a stroke warning sign and a window of opportunity to stop one.")

if selected =='Cryptogenic Stroke':
    st.markdown("<h1 style='text-align: center; color: Red;'>Cryptogenic Stroke</h1>", unsafe_allow_html=True)

    html_string8 ='<a href="https://im.ge/i/uCrtXS"><img src="https://i.im.ge/2022/07/06/uCrtXS.jpg" alt="uCrtXS.jpg" border="0"></a>'
    st.markdown(html_string8, unsafe_allow_html=True)

    st.write("The majority of the time, a blood clot that prevents blood flow to the brain is what causes a stroke. However, sometimes the cause cannot be identified despite testing. Strokes that are cryptogenic are those having an unknown cause.")
    st.write(" Potential hidden causes could be: Irregular heartbeat, heart structure problems, hardening of the arteries, blood clotting disorder")
