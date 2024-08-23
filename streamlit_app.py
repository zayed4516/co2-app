# import streamlit as st
# import pickle
# st.title("🎈 car co2 emssion")
# f1=st.number_input('feature 1',min_value=1,max_value=10)
# f2=st.number_input('feature 2',min_value=1,max_value=10)
# f3=st.number_input('feature 3',min_value=1,max_value=10)

# with open('model.pkl','rb') as file:
#  model= pickle.load(file)
 
#  res=model.predict([[f1,f2,f3]])

# st.write(res[0])
import streamlit as st
import pickle
import numpy as np
from PIL import Image

# تحميل النموذج
model = pickle.load(open('model.pkl', 'rb'))

# تحميل الصورة
image = Image.open('logo.png')

# عرض الصورة
st.image(image, use_column_width=True)

# عنوان التطبيق
st.title('Model Prediction App')

# وصف قصير للتطبيق
st.write("""
Welcome to the Model Prediction App! Use the sidebar to input the features, and the model will predict the result.
""")

# استخدام sidebar لإدخال الميزات
st.sidebar.header('Input Features')

feature1 = st.sidebar.number_input('Feature 1', min_value=0.0, max_value=100.0, value=50.0)
feature2 = st.sidebar.number_input('Feature 2', min_value=0.0, max_value=100.0, value=50.0)
feature3 = st.sidebar.number_input('Feature 3', min_value=0.0, max_value=100.0, value=50.0)

# زر لبدء التنبؤ
if st.sidebar.button('Predict'):
    features = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(features)
    st.subheader('Prediction:')
    st.write(f'The predicted value is: {prediction[0]}')

# إضافة نص إضافي أو روابط
st.sidebar.write("""
You can adjust the features using the sliders and click on "Predict" to see the model's output.
""")

