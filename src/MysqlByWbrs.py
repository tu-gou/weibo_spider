# -*- coding: utf-8 -*-

#   保存热搜
def save_rs(db, item):
    cur = db.cursor()
    cur.execute('INSERT INTO rs(`rank`,title,search,link) values(%s,%s,%s,%s)',
                (item.rank, item.title, item.search, item.link))
    cur.close()
    db.commit()


#   保存级联热搜
def save_context(db, item):
    cur = db.cursor()
    print(item[0], item[1], item[2])
    cur.execute('INSERT INTO rs_context(`rank`,title,context) values(%s,%s,%s)',
                (item[0], item[1], item[2]))
    cur.close()
    db.commit()


#   读取热搜
def read_rs(db, rank):
    cur = db.cursor()
    sql = "select `rank`, title, search, link from rs where `rank` = %s"
    cur.execute(sql, rank)
    result = cur.fetchone()
    cur.close()
    return result


#   读取热搜内容
def read_rs_context(db, rank):
    cur = db.cursor()
    sql = "select * from rs_context where `rank` = %s"
    cur.execute(sql, rank)
    result = cur.fetchone()
    cur.close()
    return result
