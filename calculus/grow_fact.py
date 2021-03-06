import psycopg2
import os, glob, codecs,csv


post_fun = 'test_inv.test_grow'
finish_table = 'test_inv.res_calc_grow_t'
static_start = 'grow_fact/start/'
static_finish = 'grow_fact/finish/'

conn = psycopg2.connect(host='10.248.96.23', database='unicorn',
                        user='dkornienko', password='dkornienko12345')
cur = conn.cursor()

cur_dir = os.path.dirname(os.path.abspath(__file__))
path_start = '{}/static/{}'.format(cur_dir,static_start)
path_finish = '{}/static/{}'.format(cur_dir,static_finish)
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
    cur.execute('truncate table {}'.format(finish_table))
    with codecs.open(file_name, 'r','cp1251') as file:
        cur.execute('insert into {0} (test_no, test_name, hcode_id, '
                    'hcode_name, hcode_'
                    'unit_name,'
                    ' org_id, dor_kod, duch_id, nod_id, date_type_id, metric_type_id, cargo_type_id, val_type_id,'
                    ' unit_id, dt, value, ss, dir_id, kato_id, vids_id) values {1}'.format(finish_table,file.read()))
        conn.commit()


def summoner():
    fun_sql_set = []
    for i in range(len(finish_list)):
        insert_data_as_is(start_list[i])
        insert_data_to_be(finish_list[i])
        fun_sql_set.append(finish_list[i])
        with codecs.open(finish_list[i], "r",'cp1251') as f:
            reader = csv.reader(f, delimiter=",")
            data = list(reader)
            row_count = len(data)
        fun_query = """select * from {}('1','{}')""".format(post_fun,row_count)
        cur.execute(fun_query)
        rows = cur.fetchall()
        for row in rows:
            fun_sql_set.append(row)
    return fun_sql_set





