#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on: 2022/04/03 20:14
Desc      : 数据库 ORM
"""

__author__ = 'martin.xiao'

import os
from contextlib import contextmanager
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import Config

__all__ = ['Base',
    'insert',
    'insertMany',
    'selectOne',
    'executeSQL']

Base = declarative_base()

def _get_session():
    conf = Config(os.path.dirname(os.path.abspath(__file__))+'/config.ini')

    db_connect = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=%s' % (
        conf.get('default', 'DB_USER'),
        conf.get('default', 'DB_PASSWORD'),
        conf.get('default', 'DB_HOST'),
        conf.get('default', 'DB_PORT'),
        conf.get('default', 'DB_NAME'),
        conf.get('default', 'CHARSET')
    )

    show_sql = conf.get('option', 'SHOW_SQL')
    engine = create_engine(db_connect,
                echo=bool(int(show_sql)),   # 打印输出 SQL
                max_overflow=0,             # 超过连接池大小外最多创建的连接
                pool_size=5,                # 连接池大小
                pool_timeout=10,            # 池中没有线程时最多等待的时间(s)
                pool_recycle=100            # N 次之后对线程池中的线程进行连接重置
            )
    session = sessionmaker(bind=engine, expire_on_commit=False)

    print(id(engine))
    print(id(session))
    return session


def _get_scoped_session():
    session = _get_session()
    return scoped_session(session)


@contextmanager
def _dbsession():
    session = _get_scoped_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert(obj: Base):
    with _dbsession() as sess:
        sess.add(obj)


def insertMany(objs: List[Base]):
    with _dbsession() as sess:
        sess.add_all(objs)


def selectOne(obj: Base, filter_cond: dict) -> Base:
    ret = None
    with _dbsession() as sess:
        ret = sess.query(obj).filter_by(**filter_cond).one()
    return ret


def executeSQL(sql: str) -> List[dict]:
    cursor = None
    with _dbsession() as sess:
        cursor = sess.execute(sql).cursor

    # 数据集转字典列表
    result_dict  = [dict(zip([field[0].lower() for
                field in cursor.description], d)) for d in cursor.fetchall()]
    return result_dict
