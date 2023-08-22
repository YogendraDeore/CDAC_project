# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np





#Load saved models

diabetes_model = pickle.load(open(r'C:/Users/user/Downloads/diabetes_prediction_model.sav','rb'))

heart_model = pickle.load(open(r'C:/Users/user/Downloads/heart_xgb_model.sav','rb'))

brain_model = pickle.load(open(r'C:/Users/user/Downloads/brain_stroke_prediction_model.sav','rb'))

#Diabetes prediction function
def diabatic_disease_prediction(input_data):
    #changing the input_data to numpy array
    input_data_as_numpy_array = np.array(input_data)
    
    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = diabetes_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0]==1):
        return 'The person is Diabatic'
    else:
        return 'The person does not Diabaties'

#Heart Disease prediction function    
def heart_disease_prediction(input_data):
    #changing the input_data to numpy array
    #input_data_as_numpy_array = np.asarray(input_data)
    input_data_as_numpy_array = np.array(input_data,dtype=object)
    
    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = heart_model.predict(input_data_reshaped)
    #print(prediction)
    
    if (prediction[0]==1):
        return 'The person has heart disease'
    else:
        return 'The person does not have heart disease'

#Brain Stroke prediction function
def brain_stroke_prediction(input_data):
    #changing the input_data to numpy array
    #input_data_as_numpy_array = np.asarray(input_data)
    input_data_as_numpy_array = np.array(input_data,dtype=object)
    
    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = brain_model.predict(input_data_reshaped)
    #print(prediction)
    
    if (prediction[0]==1):
        return 'The person has brain stroke'
    else:
        return 'The person does not have brain stroke'

#sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction Web Application', \
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Brain Stroke Prediction'],
                           icons=['activity','heart','person'], #edit the icons
                           default_index=0)
######### Diabetes Prediction Page
if (selected=='Diabetes Prediction'):
    #Page title
    
    st.title("Diabetes Prediction app")
    
    #arranging user input in 3 columns
    col1,col2,col3 = st.columns(3)
    
    #Ordinal features
    BMI = st.text_input('BMI value')
    
    MentalHealth = st.slider('For how many days in the past 30 days was your Mental Health not good?', \
                                 min_value=0.0,max_value=30.0,value=31.0,step=1.0)
    PhysicalHealth = st.slider('Physical illness and injury for how many days during past 30 days?', \
                               min_value=0.0,max_value=30.0,value=31.0,step=1.0)
    GenHlth = st.selectbox('General Health',['Excellent', 'Very good', 'Good', 'Fair','Poor'])
    Age = st.selectbox('Age(Years)',['18-24','24-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older'])
    Education = st.selectbox('Education level',['Never Attended','Elementry','Secondory','Higher Secondory','Graduate','Post Graduate'])
    Income = st.selectbox('Income',['Less Than $10k','$10k-$15k','$15k-$20k','$20k-$25k','$25k-$30k','$30k-$35k','$35k-$40k','Above $40k'])
    HighBP = st.selectbox('High Blood Pressure',['No','Yes'])
    HighChol = st.selectbox('High Cholesterol',['No','Yes'])
    CholCheck = st.selectbox('Cholesterol check in 5 years',['No','Yes']) 
    Smoking = st.selectbox('Smoking?',['No','Yes']) #No,Yes
    Stroke = st.selectbox('Stroke?',['No','Yes']) #No,Yes
    HeartDiseaseorAttack = st.selectbox('Suffering from heart disease or Heart Attact',['No','Yes'])
    PhysicalActivity = st.selectbox('Physical Activity',['No','Yes']) #No,Yes
    Fruits = st.selectbox('Consume Fruit 1 or more times per day',['No','Yes'])
    Veggies = st.selectbox('Consume Vegetables 1 or more times per day',['No','Yes'])
    AlcoholDrinking = st.selectbox('Alcohol Consumption?',['No','Yes']) #No,Yes
    AnyHealthcare = st.selectbox('Health Insurance',['Yes','No'])
    NoDocbcCost = st.selectbox('Inaccessible healthcare due to cost recently ?',['Yes','No'])
    DiffWalking = st.selectbox('Difficulty in Walking?',['No','Yes']) #No,Yes
    Sex = st.selectbox('Sex?',['Female','Male']) #Female,Male 
    
    
    gen_hlth_mapping = {'Excellent': 1, 'Very good': 2, 'Good': 3, 'Fair': 4}
    dum_GenHlth = gen_hlth_mapping.get(GenHlth, 5)
    age_mapping = {'18-24': 1,'24-29': 2,'30-34': 3,'35-39': 4,'40-44': 5,'45-49': 6,'50-54': 7,'55-59': 8,'60-64': 9,'65-69': 10,'70-74': 11,'75-79': 12}
    dum_Age = age_mapping.get(Age, 13)
    education_mapping = {'Never Attended': 1,'Elementary': 2,'Secondary': 3,'Higher Secondary': 4,'Graduate': 5}

    income_mapping = {'Less Than $10k': 1,'$10k-$15k': 2,'$15k-$20k': 3,'$20k-$25k': 4,'$25k-$30k': 5,'$30k-$35k': 6,'$35k-$40k': 7}
    dum_Education = education_mapping.get(Education,6)  
    dum_Income = income_mapping.get(Income,8)      
    
    
    if Smoking == 'No':
        dum_Smoking=[1,0]
    else:
        dum_Smoking=[0,1]
    
    if AlcoholDrinking == 'No':
        dum_AlcoholDrinking=[1,0]
    else:
        dum_AlcoholDrinking=[0,1]

    if Stroke == 'No':
        dum_Stroke=[1,0]
    else:
        dum_Stroke=[0,1]
    
    if DiffWalking == 'No':
        dum_DiffWalking=[1,0]
    else:
        dum_DiffWalking=[0,1]
    
    if Sex == 'Female':
        dum_Sex=[1,0]
    else:
        dum_Sex=[0,1]
   
    if HighBP == 'No':
        dum_HighBP=[1,0]
    else:
        dum_HighBP=[0,1]
    
    if HighChol == 'No':
        dum_HighChol=[1,0]
    else:
        dum_HighChol=[0,1]

    if CholCheck == 'No':
        dum_CholCheck=[1,0]
    else:
        dum_CholCheck=[0,1]
    
    if HeartDiseaseorAttack == 'No':
        dum_HeartDiseaseorAttack=[1,0]
    else:
        dum_HeartDiseaseorAttack=[0,1]
    
    if PhysicalActivity == 'No':
        dum_PhysicalActivity=[1,0]
    else:
        dum_PhysicalActivity=[0,1]  
    
    if Fruits == 'No':
        dum_Fruits=[1,0]
    else:
        dum_Fruits=[0,1]
    
    if Veggies == 'No':
        dum_Veggies=[1,0]
    else:
        dum_Veggies=[0,1]

    if AnyHealthcare == 'No':
        dum_AnyHealthcare=[1,0]
    else:
        dum_AnyHealthcare=[0,1]
    
    if NoDocbcCost == 'No':
        dum_NoDocbcCost=[1,0]
    else:
        dum_NoDocbcCost=[0,1]
    
    
    # code for Prediction
    diagnosis = ''
    
    #Defining list of features
    features = []
    ordinal_features = [BMI,dum_GenHlth,MentalHealth,PhysicalHealth,dum_Age,
                        dum_Education,dum_Income]
    dum_features = [dum_HighBP,dum_HighChol,dum_CholCheck,dum_Smoking,dum_Stroke,
                    dum_HeartDiseaseorAttack,dum_PhysicalActivity,dum_Fruits,dum_Veggies,
                    dum_AlcoholDrinking , dum_AnyHealthcare,dum_NoDocbcCost,dum_DiffWalking,dum_Sex ]
    
    for var in ordinal_features:
        features.append(var)
    
    for var in dum_features:
        features.extend(var)
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabatic_disease_prediction(features)
        
    st.success(diagnosis)
    

######### Heart Disease Prediction Page
if (selected=='Heart Disease Prediction'):
    #Page title
    st.title("Heart Disease Prediction app")
    
    AgeCategory = st.selectbox('Age Category? (Young<30, 30<Adult<50, 50<Old<70, 70<Very Old)',['Young','Adult','Old','Very Old']) #Adult,Old,VeryOld,Young
    PhysicalHealth = st.slider('Physical illness and injury for how many days during past 30 days?', \
                               min_value=0.0,max_value=30.0,value=31.0,step=1.0)
    MentalHealth = st.slider('For how many days in the past 30 days was your Mental Health not good?', \
                                 min_value=0.0,max_value=30.0,value=31.0,step=1.0)
    SleepTime = st.slider('Average Sleep Time in hours',min_value=1.0,max_value=24.0,value=24.0,step=1.0)
    
    #arranging user input in 3 columns
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Sex = st.selectbox('Sex?',['Female','Male']) #Female,Male
        PhysicalActivity = st.selectbox('Physical Activity',['No','Yes']) #No,Yes
        Diabetic = st.selectbox('Diabetic?',['No','Yes']) #No,Yes
        Asthma = st.selectbox('Asthma?',['No','Yes']) #No,Yes
    
    with col2:
        BMI = st.text_input('BMI value') #Ordinal features
        DiffWalking = st.selectbox('Difficulty in Walking?',['No','Yes']) #No,Yes
        Smoking = st.selectbox('Smoking?',['No','Yes']) #No,Yes  
        KidneyDisease = st.selectbox('Kidney Disease?',['No','Yes']) #No,Yes
        Race = st.selectbox('Race?',['White', 'Black', 'Asian', 'American Indian/Alaskan Native',
           'Other', 'Hispanic']) #American Indian/Alaskan Native,Asian,Black,Hispanic,Other,White
        
    with col3:
        GenHealth = st.selectbox('Overall Health?',['Very good', 'Fair', 'Good', 'Poor', 'Excellent']) #Excellent,Fair,Good,Poor,Very good
        Stroke = st.selectbox('Ever had a heart Stroke?',['No','Yes']) #No,Yes
        AlcoholDrinking = st.selectbox('Alcohol Consumption?',['No','Yes']) #No,Yes
        SkinCancer = st.selectbox('Skin Cancer?',['No','Yes'])
    
    #Encoding the dummy features
    if Smoking == 'No':
        dum_Smoking=[1,0]
    else:
        dum_Smoking=[0,1]
        
    if AlcoholDrinking == 'No':
        dum_AlcoholDrinking=[1,0]
    else:
        dum_AlcoholDrinking=[0,1]
    
    if Stroke == 'No':
        dum_Stroke=[1,0]
    else:
        dum_Stroke=[0,1]
        
    if DiffWalking == 'No':
        dum_DiffWalking=[1,0]
    else:
        dum_DiffWalking=[0,1]
        
    if Sex == 'Female':
        dum_Sex=[1,0]
    else:
        dum_Sex=[0,1]
    
    #Adult,Old,VeryOld,Young
    if AgeCategory == 'Adult':
        dum_AgeCategory=[1,0,0,0]
    elif AgeCategory == 'Old':
        dum_AgeCategory=[0,1,0,0]
    elif AgeCategory == 'Very Old':
        dum_AgeCategory=[0,0,1,0]
    else:
        dum_AgeCategory=[0,0,0,1]
    
    #American Indian/Alaskan Native,Asian,Black,Hispanic,Other,White
    if Race == 'American Indian/Alaskan Native':
        dum_Race = [1,0,0,0,0,0]
    elif Race == 'Asian':
        dum_Race = [0,1,0,0,0,0]
    elif Race == 'Black':
        dum_Race = [0,0,1,0,0,0]
    elif Race == 'Hispanic':
        dum_Race = [0,0,0,1,0,0]
    elif Race == 'Other':
        dum_Race = [0,0,0,0,1,0]
    else:
        dum_Race = [0,0,0,0,0,1]
    
    if Diabetic == 'No':
        dum_Diabetic=[1,0]
    else:
        dum_Diabetic=[0,1]
        
    if PhysicalActivity == 'No':
        dum_PhysicalActivity=[1,0]
    else:
        dum_PhysicalActivity=[0,1]
    
    #Excellent,Fair,Good,Poor,Very good
    if GenHealth == 'Excellent':
        dum_GenHealth = [1,0,0,0,0]
    elif GenHealth == 'Fair':
        dum_GenHealth = [0,1,0,0,0]
    elif GenHealth == 'Good':
        dum_GenHealth = [0,0,1,0,0]
    elif GenHealth == 'Poor':
        dum_GenHealth = [0,0,0,1,0]
    else:
        dum_GenHealth = [0,0,0,0,1]
        
    if Asthma == 'No':
        dum_Asthma=[1,0]
    else:
        dum_Asthma=[0,1]
        
    if KidneyDisease == 'No':
        dum_KidneyDisease=[1,0]
    else:
        dum_KidneyDisease=[0,1]
    
    if SkinCancer == 'No':
        dum_SkinCancer=[1,0]
    else:
        dum_SkinCancer=[0,1]
        
    # code for Prediction
    diagnosis = ''
    
    #Defining list of features
    features = []
    ordinal_features = [BMI,PhysicalHealth,MentalHealth,SleepTime]
    dum_features = [dum_Smoking,dum_AlcoholDrinking,dum_Stroke,dum_DiffWalking,dum_Sex,
                    dum_AgeCategory,dum_Race,dum_Diabetic,dum_PhysicalActivity,
                    dum_GenHealth,dum_Asthma,dum_KidneyDisease,dum_SkinCancer]
                    
    for var in ordinal_features:
        features.append(var)
        
    for var in dum_features:
        features.extend(var)
        
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_disease_prediction(features)
    st.success(diagnosis)
    
####### Brain Stroke Web page
if (selected=='Brain Stroke Prediction'):
    #Page title
    st.title("Brain Stroke Prediction app")
    
    #getting the input data from the user
    
    #arranging user input in 3 columns
    col1,col2,col3 = st.columns(3)
    
   
    age = st.text_input('Age (in Years)')
    glucoseLevel = st.text_input('Average Glucose level (mg/dL)')
    BMI = st.text_input('BMI value')
    
    #Dummies start from here
    Sex = st.selectbox('Sex?',['Female','Male']) #Female,Male
    hypertension = st.selectbox('Hypertension?',['No','Yes']) #No,Yes
    HeartDisease = st.selectbox('Heart Disease?',['No','Yes']) #No,Yes
    everMarried = st.selectbox('Ever Married?',['No','Yes']) #No,Yes
    workType = st.selectbox('Work Type?',['Children','Never worked','Government Job', \
                                          'Private Job','Self employed']) #Government Job,Never worked,Private Job,Self employed,Children
    residence = st.selectbox('Residence type?',['Rural','Urban']) #Rural,Urban
    Smoking = st.selectbox('Smoking?',['Never Smoked','Formerly smoked','Smokes']) #Formerly smoked,Never Smoked,Smokes
    
    #Encoding the dummy features
    if Sex == 'Female':
        dum_Sex=[1,0]
    else:
        dum_Sex=[0,1]
        
    if hypertension == 'No':
        dum_hypertension=[1,0]
    else:
        dum_hypertension=[0,1]
    
    if HeartDisease == 'No':
        dum_HeartDisease=[1,0]
    else:
        dum_HeartDisease=[0,1]
        
    if everMarried == 'No':
        dum_everMarried=[1,0]
    else:
        dum_everMarried=[0,1]
    
    #Government Job,Never worked,Private Job,Self employed,Children
    if workType == 'Government Job':
        dum_workType =[1,0,0,0,0]
    elif workType == 'Never worked':
        dum_workType =[0,1,0,0,0]
    elif workType == 'Private Job':
        dum_workType =[0,0,1,0,0]
    elif workType == 'Self employed':
        dum_workType =[0,0,0,1,0]
    else:
        dum_workType =[0,0,0,0,1]
        
    if residence == 'Rural':
        dum_residence=[1,0]
    else:
        dum_residence=[0,1]
    
    #Formerly smoked,Never Smoked,Smokes
    if Smoking == 'Formerly smoked':
        dum_Smoking = [1,0,0]
    elif Smoking == 'Never Smoked':
        dum_Smoking = [0,1,0]
    else:
        dum_Smoking = [0,0,1]
    
        
    # code for Prediction
    diagnosis = ''
    
    #Defining list of features
    features = []
    ordinal_features = [age,glucoseLevel,BMI]
    dum_features = [dum_Sex,dum_hypertension,dum_HeartDisease,dum_everMarried,
                    dum_workType,dum_residence,dum_Smoking]
                    
                    
    for var in ordinal_features:
        features.append(var)
        
    for var in dum_features:
        features.extend(var)
        
    # creating a button for Prediction
    
    if st.button('Brain Stroke Test Result'):
        diagnosis = brain_stroke_prediction(features)
        
    st.success(diagnosis)
    
    
    
    
    