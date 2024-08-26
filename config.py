class Config:
    SECRET_KEY = '871b3bc3bc34c102a3d0bed857a1abb7'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://youruser:yourpassword@DOMAINNAMEHOST/DATABASE?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False