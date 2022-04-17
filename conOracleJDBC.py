import os
import platform
import sys
import pandas as pd
import jaydebeapi

plat = platform.system()
print("Common info:\nOS name:\t{}\nplatform:\t{}\nversion:\t{}\nrelease:\t{}\nPython v.:\t{}.{}.{}".format(
    os.name,
    plat,
    platform.version(),
    platform.release(),
    sys.version_info.major,
    sys.version_info.minor,
    sys.version_info.micro
))

if plat == "Linux":
    jarFile = '/home/demipt2/ojdbc8.jar'
    print("Unix-specific info: {}".format(platform.linux_distribution()))
if plat == "Windows":
    jarFile = r'C:\sqldeveloper\jdbc\lib\ojdbc8.jar'
dirver = 'oracle.jdbc.driver.OracleDriver'
addr_ = 'de-oracle.chronosavant.ru' + ':' + '1521' + '/' + 'deoracle'
url = 'jdbc:oracle:thin:@' + addr_
#print('url', url)
DBUser = 'demipt2'
DBPwd = 'peregrintook'

print("\ngeting info from database: {}...\n".format(url))
conn = jaydebeapi.connect(dirver, url, [DBUser, DBPwd], jarFile)
#sql_str = "select 'oracle' from dual"
sql_str = "select ID_MODEL, NAME_MODEL, YEAR_ISSUE from pana_models"
#df = pd.read_sql_query(sql_str, conn)
#df.head()
#print(df)
curs = conn.cursor()
curs.execute(sql_str)

df = pd.DataFrame(curs.fetchall(), columns=['ID_MODEL', 'NAME_MODEL', 'YEAR_ISSUE'])
#df.reset_index(drop=True, inplace=True)
#df.index = df['ID_MODEL']

print(df)
#print(curs.fetchall())
curs.close()
conn.close()
