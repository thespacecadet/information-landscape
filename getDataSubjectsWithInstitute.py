#similar to getDataSubjects, only this script delivers data per institute selected
# was neederd in an earlier version that focused on a specific institute
import mysql.connector

cnx = mysql.connector.connect(user='spacecadet', password='3smashing3',
                              host='127.0.0.1',
                              database='ikon_som')
cursor = cnx.cursor()


query = "select * from (SELECT project_abstract,min(id) as pro_id \
	FROM ikon_som.projects \
    where project_abstract NOT LIKE '%Keine Zusammenfassung%'\
    GROUP BY project_abstract) as a \
    INNER JOIN (SELECT project_id as inst_id,institution_id from ikon_som.project_institution_v2 WHERE institution_id = 13232) as b \
    ON b.inst_id = a.pro_id \
    LEFT JOIN (SELECT project_id, subject_area from ikon_som.subject_area) as c \
    ON c.project_id = a.pro_id \
    LIMIT 250"


cursor.execute(query)
data = cursor.fetchall()

abstract_subject = {}
weight_counter = {}

for paper_index in range(len(data)):
    if data[paper_index][5] in abstract_subject:
        abstract_subject[data[paper_index][5]] += ' ' + data[paper_index][0]
        weight_counter[data[paper_index][5]] += 1
    else:
        abstract_subject[data[paper_index][5]] =  data[paper_index][0]
        weight_counter[data[paper_index][5]] = 1
cnx.close()