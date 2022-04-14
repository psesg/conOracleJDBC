
import jaydebeapi
import pandas as pd


dirver = 'oracle.jdbc.driver.OracleDriver'
jarFile = r'C:\sqldeveloper\jdbc\lib\ojdbc8.jar'
addr_ = 'de-oracle.chronosavant.ru' + ':' + '1521' + '/' + 'deoracle'
url = 'jdbc:oracle:thin:@' + addr_
print('url', url)
DBUser = 'demipt2'
DBPwd = 'peregrintook'
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
