import os
import platform
import sys
import pandas as pd
import jaydebeapi
from sqlalchemy import types

pd.set_option("display.max_columns", 200)

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
conn = jaydebeapi.connect(dirver, url, [DBUser, DBPwd], jarFile)
conn.jconn.setAutoCommit(False)
curs = conn.cursor()

sql_str = "insert into demipt2.PANA_MANUFACTORY (ID_MANUFACTORY, MANUFACTORY) Values(6, 'Жигули')"
print("\ninserting to  database...\n'{}'".format(sql_str))
try:
    curs.execute(sql_str)
except Exception as e:
    print("Error insertion:{}".format(e))
else:
    conn.commit()
finally:
    print("inserted {} rows".format(curs.rowcount))

print("\ngeting info from database: {}...\n".format(url))
sql_str = "select * from PANA_MANUFACTORY order by ID_MANUFACTORY asc"
curs.execute(sql_str)
df = pd.DataFrame(curs.fetchall(), columns = [ x[0] for x in curs.description])
print(df)

dtyp = {c:types.VARCHAR(df[c].str.len().max()) for c in df.columns[df.dtypes == 'object'].tolist()}

sql_str = "delete from demipt2.PANA_MANUFACTORY WHERE ID_MANUFACTORY =  6"
print("\ndeleting from  database...\n'{}'".format(sql_str))
try:
    curs.execute(sql_str)
except Exception as e:
    print("Error insertion:{}".format(e))
else:
    conn.commit()
finally:
    print("deleted {} rows".format(curs.rowcount))
curs.close()
conn.close()
