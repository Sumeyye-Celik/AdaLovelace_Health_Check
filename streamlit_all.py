import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder
from sklearn.preprocessing import StandardScaler
import numpy as np
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False)


st.set_page_config(layout = "wide")
@st.cache_data
def get_data():
    df = pd.read_csv(r"data/prepared_data.csv")
    return df

def get_model():
    model = joblib.load(r"model/stacking_model.joblib")
    return model


@st.cache_data
def get_heart_data():
    heart = pd.read_csv(r"data/heart (1).csv")
    return heart

def get_heart_model():
    model_heart = joblib.load(r"model/heart_health_model.joblib")
    return model_heart


st.header("💜 Ada Lovelace Health Control System 🩺" )


# Her bir sütunu ayrı bir değişkene ata
tab_info, tab_home, tab_vis,tab_heart, tab_model = st.tabs(("Information", "Sleep Disorder", "Sleep Disorder Graphics","Heart ", "Model"))


#TAB INFO#

tab_info.title("")

# Sayfa içeriğini ortala ve büyüt
tab_info.markdown("""
<div style='text-align: center; font-size: 25px;'> 
This application is a data science project that predicts important health conditions such as <strong>sleep disorders</strong> and <strong>heart health</strong>.
Health predictions provide valuable information about individuals' lifestyle and health habits.
It can help in early diagnosis, personalised treatment and development of healthy living strategies.
This project was carried out by <strong>Betül Ulucak</strong> and <strong>Sümeyye Çelik</strong> as a graduation project of <strong>SistersLab - Women in Science and Technology Association AdaLovelace Academy</strong>.
We would like to thank our lecturer <strong>Kemal Soylu</strong>, our <strong>project assistants</strong> and our mentor <strong>Aylin Kaymaz</strong> for taking care of us during the academy. 
</div>
""", unsafe_allow_html=True)

tab_info.title("")

tab_info.markdown("""
<div style='text-align: center; font-size: 40px;'>
    <h1 style="color:#3498db;">About Us</h1>
</div>
""", unsafe_allow_html=True)

column_betul,column_sumeyye = tab_info.columns(2)



col_image2 , col_text2 = column_betul.columns([1,2])

# Fotoğrafı ekleyin
image_path = "media/IMG_4410.png"  # Resminizin doğru dosya yolunu belirtin
image = Image.open(image_path)
new_image = image.resize((200,200))
col_image2.image(new_image)

col_image2.header("Betül Uluocak")


# LinkedIn simgesi ve bağlantısı
linkedin_icon = """
<head>
    <style>
    .fa {
    float: right;
    </style>
</head>
<body>
    <div class ="fa">
        <a href="https://www.linkedin.com/in/betululuocak/" target="_blank">
            <img width="48" height="48" src="https://img.icons8.com/color/48/linkedin.png" alt="linkedin"/>
        </a>
    </div>
</body>
""" 

github_icon = """
<head>
    <style>
    .fa {
    float: right;
    </style>
</head>
<body>
    <div class ="fa">
        <a href="https://github.com/betul13" target="_blank">
            <img width="48" height="48" src="https://img.icons8.com/fluency/48/000000/github.png" alt="github"/>
        </a>
    </div>
</body>
""" 

# LinkedIn ve GitHub simgelerini yan yana görüntüle
icons = f"{linkedin_icon} {github_icon}"
col_image2.markdown(icons, unsafe_allow_html=True)


# Metni bir şeklin içine yaz
text_inside_shape = """
<p class="shape" style="color: black; font-size: 18px; text-align: center; line-height: 1.6;">
    I graduated from Yıldız Technical University, Department of Electrical Engineering in 2023. 
    With my graduation, my interest in the field of data science and machine learning increased. 
    My passion for continuous learning and improvement in this field has led me to further progress in this field. 
    Thanks to the various trainings and events I attended, I increased my knowledge on data science and machine learning. 
    With the skills I acquired during this process, I improved my skills in generating solutions to real-world problems. 
    Now, I want to work in the field of data science and machine learning, gain experience in this field and constantly improve myself. 
    My goals include taking part in new projects in this field, participating in teamwork, 
    and producing solutions to problems in various sectors by using the power of technology.
</p>

"""

# Şekli oluştur
shape_container = column_betul.container()

# Şeklin arkaplan rengini ayarla
shape_container.markdown(
    """
    <style>
        .shape {
            background-color: #add8e6;  
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1); /* Hafif bir gölge efekti */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Şeklin içine metni yerleştir
col_text2.markdown(f'<div class="shape">{text_inside_shape}</div>', unsafe_allow_html=True)

col_image, col_text = column_sumeyye.columns([1,2])

# Fotoğrafı ekleyin
image_path = "media/Ekran Görüntüsü (213).png"  
image = Image.open(image_path)
new_image = image.resize((200,200))
image_knm ="""
<head>
    <style>
    .fa {
    float: right;
    </style>
</head>
<body>
    <div class ="fa">
        <a target="_blank">
            <img width="200" height="200" src="media/Ekran Görüntüsü (213).png" alt="linkedin"/>
        </a>
    </div>
</body>
""" 
col_image.image(new_image)

col_image.header("Sümeyye Çelik")


# LinkedIn simgesi ve bağlantısı
linkedin_icon = """
<head>
    <style>
    .fa {
    float: left;
    </style>
</head>
<body>
    <div class ="fa">
        <a href="https://www.linkedin.com/in/sumeyyecelik/" target="_blank">
            <img width="48" height="48" src="https://img.icons8.com/color/48/linkedin.png" alt="linkedin"/>
        </a>
    </div>
</body>
"""

github_icon = """
<head>
    <style>
    .fa {
    float: left;
    </style>
</head>
<body>
    <div class ="fa">
        <a href="https://github.com/Sumeyye-Celik" target="_blank">
            <img width="48" height="48" src="https://img.icons8.com/fluency/48/000000/github.png" alt="github"/>
        </a>
    </div>
</body>
"""

# LinkedIn ve GitHub simgelerini yan yana görüntüle
icons = f"{linkedin_icon} {github_icon}"


col_image.markdown(icons, unsafe_allow_html=True)


# Metni bir şeklin içine yaz
text_inside_shape = """
<p class="shape" style="color: black; font-size: 18px; text-align: center; line-height: 1.6;">
  I graduated from Kütahya Dumlupınar University, Department of Computer Engineering. During my university life, 
  I took part in international communities to be active. I continue to be an organiser of Google Developer Groups and Women Techmakers ambassador. 
  I have been improving myself in data for 1.5 years. In this process, I made Bitcoin price prediction as an engineering graduation project and wrote a published article about it. 
  I had the opportunity to work on NLP with my internship experiences. I am working to shape my career life on data analysis, data science and NLP.
</p>

"""

# Şekli oluştur
shape_container = column_sumeyye.container()

# Şeklin arkaplan rengini ayarla
shape_container.markdown(
    """
    <style>
        .shape {
            background-color: #add8e6; /* Açık mavi tonu */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1); /* Hafif bir gölge efekti */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Şeklin içine metni yerleştir
col_text.markdown(f'<div class="shape">{text_inside_shape}</div>', unsafe_allow_html=True)


#TAB HOME#

column_sleep, column_dataset = tab_home.columns(2,gap = "large")

column_sleep.subheader(":blue[Purpose of Sleeping Sickness Prediction App]")
column_sleep.markdown("""
Sleep disorders can significantly impact the quality of life,
yet people tend to neglect these conditions. 
This application has been developed with an 85% accuracy rate to detect sleep disorders early and encourage seeking medical attention before consulting a doctor.
""")

column_sleep.subheader(":blue[What is Sleep Apnea?]")
column_sleep.markdown("""
Sleep apnea is a sleep disorder characterized by the repetitive cessation and resumption of breathing during sleep. 
This occurs when the muscles in the airway relax or become blocked, causing the normal breathing to stop. 
Sleep apnea often disrupts a person's sleep and can lead to serious health issues in severe cases.
""")


# Fotoğrafı ekleyin
image_path = "media/Ekran Görüntüsü (212).png"  # Resminizin doğru dosya yolunu belirtin
image = Image.open(image_path)
new_image = image.resize((300, 150))
column_sleep.image(new_image)


# İlk sütuna metni ekleyin
column_sleep.subheader(":blue[What is Insomnia?:]")
column_sleep.markdown("""

Insomnia is a sleep disorder characterized by difficulty falling asleep, staying asleep, 
                     or experiencing non-restorative sleep, despite having the opportunity to do so. 
                     People with insomnia may have trouble falling asleep initially, 
                     waking up during the night and struggling to go back to sleep, or waking up too early in the morning.
""")

# Fotoğrafı ekleyin
image_path = "media/SF-23-112_Insomnia_Causes_Graphic-1536x1075.webp"  # Resminizin doğru dosya yolunu belirtin
image = Image.open(image_path)
new_image = image.resize((300, 150))
column_sleep.image(new_image)


df = get_data()

column_dataset.subheader(":blue[About the Sleep Disorder Dataset]")
column_dataset.markdown("""This health prediction app works on a dataset containing various personal information and health metrics. Below, we focus on some of the key columns in the data set and the information they carry:

- **Gender:** The person's gender.
- **Age:** The person's age.
- **Occupation:** One's occupation.
- **Sleep Duration:** The person's daily sleep duration.
- **Quality of Sleep:** Evaluation of the person's sleep quality.
- **Physical Activity Level:** The person's physical activity level.
- **Stress Level:** The person's stress level.
- **BMI Category:** The person's body mass index category.
- **Blood Pressure:** A person's blood pressure measurements.
- **Heart Rate:** The person's heart rate.
- **Daily Steps:** The person's daily step count.
- **Sleep Disorder:** The person's type of sleep disorder, if any.

This information is the basic data that our health prediction model tries to use to predict various health conditions. Users can evaluate their health status and get information about possible health problems through this application.""")

column_dataset.dataframe(df,width = 500)



#  Local URL: http://localhost:8501
#Network URL: http://192.168.1.36:8501


#TAB VIS
##grafik 1

tab_vis.subheader(":blue[Explaining the variables that affect our sleep health with graphics]")

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")


def grab_col_names(dataframe, cat_th=5, car_th=20):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    # print(f"Observations: {dataframe.shape[0]}")
    # print(f"Variables: {dataframe.shape[1]}")
    # print(f'cat_cols: {len(cat_cols)}')
    # print(f'num_cols: {len(num_cols)}')
    # print(f'cat_but_car: {len(cat_but_car)}')
    # print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)

# Kategorik değişken analizi
tab_vis.subheader("Categorical Variable Analysis 📊")
selected_cat_var = tab_vis.multiselect("Select a categorical variable", cat_cols)

# Seçilen her bir kategorik değişken için işlemleri gerçekleştir
for col in selected_cat_var:

    plt.figure(figsize=(2, 2))

    # Kategorik değişkenin genel bilgileri
    cat_summary(df, col, plot=True)

    target_summary_df = df.pivot_table(index=col, columns="SLEEP DISORDER", aggfunc="size", fill_value=0)
    target_summary_df = target_summary_df.div(target_summary_df.sum(axis=1), axis=0)

    # Görselleştirmek için bir bar plot
    target_summary_df.plot(kind='bar', stacked=True)
    plt.xlabel(col)
    plt.ylabel("Proportion")
    plt.title(f"Relationship between {col} and Sleep Disorder")
    tab_vis.pyplot()

# Sayısal değişken analizi
tab_vis.subheader("Numerical Variable Analysis 📊")
selected_num_var = tab_vis.multiselect("Select a numerical variable", num_cols)

# Seçilen her bir nümerik değişken için işlemleri gerçekleştir
for col in selected_num_var:
    # Streamlit ayarlarını yapılandırın
    plt.figure(figsize=(2, 2))
    # Nümerik değişkenin genel bilgileri
    num_summary(df, col, plot=True)

    # Box plot kullanarak ilişkiyi gösterme örneği
    fig, ax = plt.subplots()
    sns.boxplot(x="SLEEP DISORDER", y=col, data=df)
    ax.set_xlabel("SLEEP DISORDER")
    ax.set_ylabel(col)
    ax.set_title(f"Relationship between {col} and Sleep Disorder")
    tab_vis.pyplot(fig)



#TAB HEART

row1, row2 = tab_heart.columns(2)

# İlk container
with row1.container(border=True):
    st.subheader("Heart")

    st.markdown("Heart health is a fundamental part of our overall health and is of vital importance. The heart is an organ that pumps blood through the arteries, carrying oxygen and nutrients to our body. Heart health therefore affects our overall quality of life.")
    st.image(r"media/heart-2.jpg")

# İkinci container
with row2.container(border=True):
    st.subheader("About The Data")
    st.markdown("This dataset is a medical dataset containing various clinical and demographic characteristics that may influence the diagnosis of heart disease.")
    
    heart = get_heart_data()
    st.dataframe(heart)

    st.markdown("Each row represents a patient and contains information such as age, gender, type of chest pain, resting blood pressure, cholesterol level, fasting blood glucose, resting electrocardiographic results, maximum heart rate, ST depression, slope of the exercise ST segment, number of large vessels, Talium Stress Test results and the presence or absence of exercise-induced angina or heart disease. Features include numeric and categorical values and have been studied to predict patients' risk of heart disease using machine learning models. The target variable represents the heart disease state that the model is trying to learn and predict; 1 means heart disease and 0 means no heart disease. This dataset is an important resource that can be used to assess heart disease risk in clinical applications.")

# Bir contaier içerisinde iki container oluşturma
with tab_heart.container(border=True):
    st.subheader("Visualisation")
    col1, col2 = st.columns(2)


vis_df = heart.copy()
# İlk sütunun ilk container'ı
with col1.container(border=True):
        vis_df['sex'] = vis_df['sex'].map({0: 'Female', 1: 'Male'})
        gender_count_combined = vis_df.groupby(['sex','output']).size().unstack()

        custom_palette = sns.color_palette("Reds", 2)

        fig, ax = plt.subplots()
        gender_count_combined.plot(kind='bar', stacked=True, ax=ax, color=custom_palette)
        ax.set_ylabel('Number of People')
        ax.set_xlabel('Gender')
        ax.set_title('Gender Distribution for Patients and Non-Patients')
        ax.legend(title='Patient Status')

        # Grafik streamlit'e gömün
        st.pyplot(fig)

        #st.subheader("Gender Distribution")
        #gender_count = df['sex'].value_counts()
        #st.bar_chart(gender_count)

# İlk sütunun ikinci container'ı
with col1.container(border=True):
        st.subheader("Resting Blood Pressure and Maximum Heart Rate")
        plt.figure(figsize=(10, 7))
        sns.scatterplot(x='trtbps', y='thalachh', data=heart, hue='output', palette=sns.color_palette("Reds", 2),s=50)
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

# İkinci sütunun ilk container'ı
with col2.container(border=True):
        st.subheader("Distribution of Chest Pain Type")
        cp_count = heart['cp'].value_counts()
        fig = px.pie(cp_count, names=cp_count.index, width=620, height=440)
        st.plotly_chart(fig)

# İkinci sütunun ikinci container'ı
with col2.container(border=True):
        st.subheader("Heart Disease Diagnosis Distribution")
        output_count = heart['output'].value_counts()
        fig, ax = plt.subplots()
        output_count.plot(kind='bar', color=sns.color_palette("Reds", 2), ax=ax)
        ax.set_ylabel('Number of People')
        ax.set_xlabel('Diagnostic Status')
        ax.set_title('Diagnosis Breakdown for Sick and Non-Sick')

        st.pyplot(fig)


#TAB MODEL

column_model,column_heart = tab_model.columns(2,gap = "large")

column_model.title("😴Predict Sleep Disorder😴")
# Modeli yükle
model = get_model()


# Veri setindeki sütunları büyük harfe çevir
df.columns = df.columns.str.upper()


# Kullanıcıdan veri girişi al
new_data = {}

#AGE,OCCUPATION,SLEEP DURATION,BMI CATEGORY,HEART RATE,SYSTOLIC,SLEEP QUALITY SCORE,ACTIVITY SCORE,SLEEP DISORDER

# Kullanıcıdan elle giriş al

gender = column_model.selectbox("GENDER", df['GENDER'].unique())


age = column_model.number_input("AGE", min_value=df['AGE'].min(), max_value=df['AGE'].max(), value=df['AGE'].min())
                             

occupation = column_model.selectbox("OCCUPATION", df['OCCUPATION'].unique())

sleep_duration = column_model.number_input("SLEEP DURATION", min_value=df['SLEEP DURATION'].min(), max_value=df['SLEEP DURATION'].max(), value=df['SLEEP DURATION'].min())

quality_sleep = column_model.number_input("QUALITY OF SLEEP", min_value=df['QUALITY OF SLEEP'].min(), max_value=df['QUALITY OF SLEEP'].max(), value=df['QUALITY OF SLEEP'].min())

physical_activity_level = column_model.number_input("PHYSICAL ACTIVITY LEVEL", min_value=df['PHYSICAL ACTIVITY LEVEL'].min(), max_value=df['PHYSICAL ACTIVITY LEVEL'].max(), value=df['PHYSICAL ACTIVITY LEVEL'].min())

stress_level = column_model.number_input("STRESS LEVEL", min_value=df['STRESS LEVEL'].min(), max_value=df['STRESS LEVEL'].max(), value=df['STRESS LEVEL'].min())

bmı_category = column_model.selectbox("BMI CATEGORY", df['BMI CATEGORY'].unique())

heart_rate = column_model.number_input("HEART RATE", min_value=df['HEART RATE'].min(), max_value=df['HEART RATE'].max(), value=df['HEART RATE'].min())

daily_steps = column_model.number_input("DAILY STEPS", min_value=df['DAILY STEPS'].min(), max_value=df['DAILY STEPS'].max(), value=df['DAILY STEPS'].min())

blood_pressure_cat = column_model.selectbox("BLOOD PRESSURE CATEGORY", df['BLOOD PRESSURE CATEGORY'].unique())

systolic = column_model.number_input("SYSTOLIC", min_value=df['SYSTOLIC'].min(), max_value=df['SYSTOLIC'].max(), value=df['SYSTOLIC'].min())


diastolic = column_model.number_input("DIASTOLIC", min_value=df['DIASTOLIC'].min(), max_value=df['DIASTOLIC'].max(), value=df['DIASTOLIC'].min())

sleep_quality_score = sleep_duration * quality_sleep
activity_score = daily_steps * physical_activity_level
# Yaş kategorisini belirle
if age < 35:
    new_age_cat = 'young'
elif 35 <= age <= 55:
    new_age_cat = 'middleage'
else:
    new_age_cat = 'old'



# Kullanıcının girdiği değerleri bir veri çerçevesine ekleyin
user_df = pd.DataFrame({
    'GENDER' : [gender],
    'AGE' : [age],
    'SLEEP DURATION' : [sleep_duration],
    'QUALITY OF SLEEP' : [quality_sleep],
    'PHYSICAL ACTIVITY LEVEL' : [physical_activity_level],
    'STRESS LEVEL' : [stress_level],
    'HEART RATE' : [heart_rate],
    'DAILY STEPS' : [daily_steps],
    'SYSTOLIC' : [systolic],
    'DIASTOLIC' : [diastolic],
    'SLEEP QUALITY SCORE': [sleep_quality_score],
    'ACTIVITY SCORE' : [activity_score],
    'OCCUPATION': [occupation],
    'BMI CATEGORY' : [bmı_category],
    'BLOOD PRESSURE CATEGORY' : [blood_pressure_cat],
    'NEW_AGE_CAT' : [new_age_cat]
 
})


ohe_columns = ['OCCUPATION', 'BMI CATEGORY', 'BLOOD PRESSURE CATEGORY', 'NEW_AGE_CAT']
num_cols = ['AGE', 'SLEEP DURATION', 'QUALITY OF SLEEP', 'PHYSICAL ACTIVITY LEVEL', 'STRESS LEVEL', 'HEART RATE', 'DAILY STEPS', 'SYSTOLIC', 'DIASTOLIC', 'SLEEP QUALITY SCORE', 'ACTIVITY SCORE']

scale = StandardScaler()
user_df[num_cols] = scale.fit_transform(user_df[num_cols])


# One-Hot Encoder ve Standard Scaler'ı yükle
with open('model/label_encoder.pkl', 'rb') as le_file:
    label = pickle.load(le_file)

with open('model/encoded_data.pkl', 'rb') as ohe_file:
    encoder = pickle.load(ohe_file)

# Kullanıcıdan gelen veriyi uygun formata dönüştür
gender_encoded = label.transform([gender])[0]
user_df['GENDER'] = gender_encoded

# One-Hot Encoding işlemi
encoded_user_data = encoder.transform(user_df[['OCCUPATION', 'BMI CATEGORY', 'BLOOD PRESSURE CATEGORY', 'NEW_AGE_CAT']]).toarray()

# One-Hot Encoding sonrası sütun isimlerini al
encoded_columns = encoder.get_feature_names_out(input_features=['OCCUPATION', 'BMI CATEGORY', 'BLOOD PRESSURE CATEGORY', 'NEW_AGE_CAT'])

# One-Hot Encoding sonrası veriyi DataFrame'e dönüştür
encoded_user_data = pd.DataFrame(encoded_user_data, columns=encoded_columns)

# Sayısal değişkenleri standardize et
scale = StandardScaler()
user_df[['AGE', 'SLEEP DURATION', 'QUALITY OF SLEEP', 'PHYSICAL ACTIVITY LEVEL', 'STRESS LEVEL', 'HEART RATE', 'DAILY STEPS', 'SYSTOLIC', 'DIASTOLIC', 'SLEEP QUALITY SCORE', 'ACTIVITY SCORE']] = scale.fit_transform(user_df[['AGE', 'SLEEP DURATION', 'QUALITY OF SLEEP', 'PHYSICAL ACTIVITY LEVEL', 'STRESS LEVEL', 'HEART RATE', 'DAILY STEPS', 'SYSTOLIC', 'DIASTOLIC', 'SLEEP QUALITY SCORE', 'ACTIVITY SCORE']])

# Kullanıcının girdiği veriyi diğer sayısal sütunlarla birleştir
user_data_combined = pd.concat([user_df[['AGE', 'SLEEP DURATION', 'QUALITY OF SLEEP', 'PHYSICAL ACTIVITY LEVEL', 'STRESS LEVEL', 'HEART RATE', 'DAILY STEPS', 'SYSTOLIC', 'DIASTOLIC', 'SLEEP QUALITY SCORE', 'ACTIVITY SCORE']], encoded_user_data], axis=1)
user_data_combined = pd.concat([user_df['GENDER'],user_data_combined],axis=1)



if column_model.button("Tahmin Et"):
    # Modeli yükle
    with open('model/stacking_model.joblib', 'rb') as model_file:
       final_model = joblib.load(model_file)

    # Model tahmini
    prediction = final_model.predict(user_data_combined)
     # Tahmin sonucunu kullanıcıya göster
    if prediction == 0:
        column_model.success("SLEEPING SICKNESS PREDICTION: You have healthy sleep!")
    elif prediction == 1:
        column_model.warning("SLEEPING SICKNESS PREDICTION: You may have sleep problems, you should see a doctor! You are showing symptoms of insomnia.")
    elif prediction == 2:
        column_model.error("SLEEPING SICKNESS PREDICTION: You have healthy sleep! You are showing symptoms of Sleep Apnea.")





#TAB MODEL
        
#Kalp Modelinin yükelenmsei
def get_heart_model():
    heart_model = joblib.load("model/heart_health_model.joblib")
    return heart_model

heart_model = get_heart_model()

# Kalp sağlığı tahmin bölümü:
label_encoder_sex = LabelEncoder()
label_encoder_cp = LabelEncoder()
label_encoder_fbs = LabelEncoder()
label_encoder_resteg = LabelEncoder()
label_encoder_slp = LabelEncoder()

# Kategorik sütunları uyumla
label_encoder_sex.fit(["Male", "Female"])
label_encoder_cp.fit(["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
label_encoder_fbs.fit(["Yes", "No"])
label_encoder_resteg.fit(["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"])
label_encoder_slp.fit(["Upsloping", "Flat", "Downsloping"])

column_heart.title("💗 Predict Heart Health 💗")
age = column_heart.number_input("Age", min_value=0, max_value=200)
sex = column_heart.selectbox("Gender", ["Male", "Female"])
encode_sex = label_encoder_sex.transform([sex])[0]
cp = column_heart.selectbox("Type of chest pain", ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
encode_cp = label_encoder_cp.transform([cp])[0]
trtbps = column_heart.number_input("Resting blood pressure", min_value=90, max_value=250)
chol =column_heart.number_input("Cholesterol level", min_value=100, max_value=600)
fbs = column_heart.selectbox("Blood glucose level above 120 mg/dl", ["Yes", "No"])
encode_fbs = label_encoder_fbs.transform([fbs])[0]
restecg = column_heart.selectbox("Resting electrocardiographic results", ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"])
encode_restecg = label_encoder_resteg.transform([restecg])[0]
thalachh = column_heart.number_input("Maximum heart rate", min_value=50, max_value=300)
slp = column_heart.selectbox("Slope of the exercise ST segment", ["Upsloping", "Flat", "Downsloping"])
encode_slp = label_encoder_slp.transform([slp])[0]

user_input = pd.DataFrame({"age": [age], "sex": [encode_sex], "cp": [encode_cp], "trtbps": [trtbps], "chol": [chol], "fbs": [encode_fbs], "restecg": [encode_restecg], "thalachh": [thalachh], "slp": [encode_slp]})
if column_heart.button("Tahmin et", key="heart_button_key"):
    prediction = heart_model.predict(user_input)
    if prediction == 0:
        column_heart.success(f"You have a healthy heart, but it is recommended that you see a doctor for a definitive conclusion.")
    else:
        column_heart.warning('You seem to have a heart condition. It is recommended that you go to the doctor for a check-up.', icon="⚠️")