import pandas
import jaydebeapi
conn = jaydebeapi.connect(
'oracle.jdbc.driver.OracleDriver',
'jdbc:oracle:thin:demipt2/peregrintook@de-oracle.chronosavant.ru:1521/deoracle',
['demipt2’,’peregrintook'],
'C:\\sqldeveloper\\jdk\\jre\\bin\\ojdbc8.jar'
#'/home/demipt2/ojdbc8.jar'
)
curs = conn.cursor()


# conn = jaydebeapi.connect('oracle.jdbc.driver.OracleDriver', ['jdbc:oracle:thin:@hostname:1521:orcl', "username", "password"],"C:\\Users\\user\\Documents\\Drivers\\ojdbc6.jar")