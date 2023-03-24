import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import time
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
    
def build_dataset(path):
    cols ="""duration,protocol_type,service,flag,src_bytes,dst_bytes,land,wrong_fragment,urgent,hot,num_failed_logins, 
    logged_in,num_compromised,root_shell,su_attempted,num_root,num_file_creations,num_shells,num_access_files,num_outbound_cmds,
    is_host_login,is_guest_login,count,srv_count,serror_rate,srv_serror_rate,rerror_rate,srv_rerror_rate,same_srv_rate,diff_srv_rate,
    srv_diff_host_rate,dst_host_count,dst_host_srv_count,dst_host_same_srv_rate,dst_host_diff_srv_rate,dst_host_same_src_port_rate,
    dst_host_srv_diff_host_rate,dst_host_serror_rate,dst_host_srv_serror_rate,dst_host_rerror_rate,dst_host_srv_rerror_rate"""

    columns =[]
    for c in cols.split(','):
        if(c.strip()):
            columns.append(c.strip())

    columns.append('target')

    # Create dictionary of training_attack_types 
    attacks_types = {
        'normal': 'normal',
        'back': 'dos',
        'buffer_overflow': 'u2r',
        'ftp_write': 'r2l',
        'guess_passwd': 'r2l',
        'imap': 'r2l',
        'ipsweep': 'probe',
        'land': 'dos',
        'loadmodule': 'u2r',
        'multihop': 'r2l',
        'neptune': 'dos',
        'nmap': 'probe',
        'perl': 'u2r',
        'phf': 'r2l',
        'pod': 'dos',
        'portsweep': 'probe',
        'rootkit': 'u2r',
        'satan': 'probe',
        'smurf': 'dos',
        'spy': 'r2l',
        'teardrop': 'dos',
        'warezclient': 'r2l',
        'warezmaster': 'r2l',
    }
    
    df = pd.read_csv(path, names = columns)

    # Add Attack Type column to DataFrame
    df['Attack_Type'] = df.target.apply(lambda r:attacks_types[r[:-1]])
    non_numeric_features = list(df.select_dtypes(exclude=['number']).columns)

    numeric_features = list(df.select_dtypes(include=['number']).columns)
    df.target=df.target.apply(lambda x: 0 if x == 'normal.' else 1)

    # keep columns where there are more than 1 unique values
    df = df[[col for col in df if df[col].nunique() > 1]]

    return df

def delete_high_correlated_features(df):
    #This variable is highly correlated with num_compromised and should be ignored for analysis.
    #(Correlation = 0.9938277978738366)
    df.drop('num_root',axis = 1,inplace = True)

    #This variable is highly correlated with serror_rate and should be ignored for analysis.
    #(Correlation = 0.9983615072725952)
    df.drop('srv_serror_rate',axis = 1,inplace = True)

    #This variable is highly correlated with rerror_rate and should be ignored for analysis.
    #(Correlation = 0.9947309539817937)
    df.drop('srv_rerror_rate',axis = 1, inplace=True)

    #This variable is highly correlated with srv_serror_rate and should be ignored for analysis.
    #(Correlation = 0.9993041091850098)
    df.drop('dst_host_srv_serror_rate',axis = 1, inplace=True)

    #This variable is highly correlated with rerror_rate and should be ignored for analysis.
    #(Correlation = 0.9869947924956001)
    df.drop('dst_host_serror_rate',axis = 1, inplace=True)

    #This variable is highly correlated with srv_rerror_rate and should be ignored for analysis.
    #(Correlation = 0.9821663427308375)
    df.drop('dst_host_rerror_rate',axis = 1, inplace=True)

    #This variable is highly correlated with rerror_rate and should be ignored for analysis.
    #(Correlation = 0.9851995540751249)
    df.drop('dst_host_srv_rerror_rate',axis = 1, inplace=True)

    #This variable is highly correlated with dst_host_srv_count and should be ignored for analysis.
    #(Correlation = 0.9736854572953938)
    df.drop('dst_host_same_srv_rate',axis = 1, inplace=True)
    
    return df

def bar_graph(df,feature):
    df[feature].value_counts().plot(kind="bar")

def label_encoding(df):
    for column in df.columns:
        if df[column].dtype == np.object:
            encoded = LabelEncoder()
        
            encoded.fit(df[column])
            df[column] = encoded.transform(df[column])
    return df

def MinMaxScaling(df):
    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df







