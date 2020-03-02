import psycopg2
import os, glob, codecs


conn = psycopg2.connect(host='10.248.96.23', database='unicorn',
                        user='dkornienko', password='dkornienko12345')
cur = conn.cursor()

cur_dir = os.path.dirname(os.path.abspath(__file__))
path_start = '{}/static/ratios/as_is/'.format(cur_dir)
path_finish = '{}/static/ratios/to_be/'.format(cur_dir)
start_list = []
finish_list = []
for infile in glob.glob(os.path.join(path_start, '*.*')):
    start_list.append(infile)
for infile in glob.glob(os.path.join(path_finish, '*.*')):
    finish_list.append(infile)




def insert_data_as_is(file_name):
    cur.execute('truncate table test_inv.start_tbl')
    with codecs.open(file_name, 'r','cp1251') as file:
        cur.execute("insert into test_inv.start_tbl values {0}".format(file.read()))
        conn.commit()


def insert_data_to_be(file_name):
    cur.execute('truncate table test_inv.res_calc_ratios_t')
    with codecs.open(file_name, 'r','cp1251') as file:
        cur.execute('insert into test_inv.res_calc_ratios_t (test_no, test_name, hcode_id, '
                    'hcode_name, hcode_'
                    'unit_name,'
                    ' org_id, dor_kod, duch_id, nod_id, date_type_id, metric_type_id, cargo_type_id, val_type_id,'
                    ' unit_id, dt, value, ss, dir_id, kato_id, vids_id) values {0}'.format(file.read()))
        conn.commit()


def summoner():
    fun_sql_set = []
    fun_query = """select * from test_inv.test_ratios('1','15')"""
    for i in range(len(finish_list)):
        print(finish_list[i])
        insert_data_as_is(start_list[i])
        insert_data_to_be(finish_list[i])
        fun_sql_set.append(finish_list[i])
        cur.execute(fun_query)
        rows = cur.fetchall()
        for row in rows:
            fun_sql_set.append(row)
    return fun_sql_set

