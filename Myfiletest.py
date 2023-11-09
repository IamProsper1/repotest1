import streamlit as st
import pandas as pd

st.title("Prosper keep it up..")


st.write("Here you can learn streamlit tutorials.")

 # creating dataset

df = pd.DataFrame({'first':["None",1,2,3,4,5], 'second':[6,7,8,9,10,11]})
st.sidebar.write(df)

#or
#df #magic command

# visualization
st.sidebar.line_chart(df)

#checkbox

if st.checkbox("show the table.."):
    df

#selectbox

opt = st.selectbox("which number you want to select: ", df["first"])
if opt == "None":
    st.write("You havent selected yet.. Please select a value")
else:
    st.write("you just selected: ",opt)
#slidebar
maxval = 50
minval = 0
val = st.slider("slider", maxval, minval)
if val != 50:
    st.write("the slider value is: ", val)
else:
    st.write("you just reached the maximum value")

#progress bar
import time

pro = st.progress(0)

for i in range(50):
    pro.progress(i+1)

    time.sleep(0.2)

#beta columns

left, right = st.columns(2)
left.write(df["first"])
right.write(df["second"])
