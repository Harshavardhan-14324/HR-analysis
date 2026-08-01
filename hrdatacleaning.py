import pandas as pd
data=pd.read_csv("c:\\Users\\Tejeshewini\\OneDrive\\Desktop\excel data\\HR_dataset1.csv")
print(data)
print(data.columns)
data.rename(columns={"Performance Score":"performancescore"},inplace=True)
print(data.columns)
print(data.loc[0:"Unnamed:0"])
data.drop("Unnamed: 0",axis=1,inplace=True)
print(data)
print(data.columns)
print(data.info())
print(data.shape)

#find number null values column
print(data.isnull().sum())
#data types
print(data.dtypes)

#count duplicated rows
print(data.duplicated().count())
#count duplicated rows
print(data.duplicated().sum())
data.rename(columns={"Trainingduration":"Training_duration","LocationCode":"Location_Code",
                     "EmployeeClassificationType":"Employee_ClassificationType","EmployeeStatus":"Employee_Status","EmployeeType":"Employee_Type",
                     "JobFunctionDescription":"JobFunction_Description"},inplace=True)
print(data.columns)

#remove extra space in full name
print(data["Full_Name"].str.strip())

#change to proper case
print(data["DepartmentType"].str.title())
print(data["DepartmentType"].head())

#change to lower case
print(data["Emails"].str.lower())
print(data["Emails"].head())

#replace unk with unknown
print(data["TerminationType"])
print(data["TerminationType"].replace("Unk","Unknown"))

#fill misssing values
print(data["DepartmentType"].isnull().sum())
print(data["TerminationType"].fillna("not available"))
print(data["DepartmentType"].head())

#change datetime
columns1=["StartDate","ExitDate","Survey_Date","Training_Date"]
for i in columns1:
    data[i]=pd.to_datetime(data[i],format="mixed")
print(data[i].dtypes)
data["DOB"]=pd.to_datetime(data["DOB"],errors="coerce")

#replace null with dates
data["DOB"]=data["DOB"].fillna(pd.Timestamp("2000-01-01"))

#duplicate in specific columns
print(data["Emails"].duplicated().sum())
print(data["Employee ID"].duplicated().sum())

#check if exitdate is eralier
data["invalid_date"]=data["ExitDate"]<data["StartDate"]
print(data[data["invalid_date"]])

#add age
data["age"]=(pd.Timestamp.today()-data["DOB"]).dt.days//365
print(data[["DOB","age"]].head())


from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = "harsha@2005"
host = "localhost"
port = 3306
database = "mysql"
password = quote_plus(password)
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)
try:
    with engine.connect() as conn:
        print("MySQL connection successful!")
    data.to_sql("hrdata1",con=engine,if_exists="replace",index=False)
    print("Data imported successfully!")
except Exception as e:
    print("Connection failed:")
    print(e)
