'''

'''
from zonghe.caw import DbOp
from zonghe.caw.DbOp import disconnect


def delete_user(db,phone):
    '''
    根据手机号删除用户
    :param db:
    :param phone:
    :return:
    '''
    conn = DbOp.connect(db)
    # 根据手机号删除用户
    DbOp.execute(conn, f"delete from member where mobilephone={phone};")
    disconnect(conn)