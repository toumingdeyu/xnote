# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/05/18
# 

"""Description here"""
import re

import xauth
import xutils
from . import dao

class handler:

    @xauth.login_required()
    def GET(self):
        days = xutils.get_argument("days", 30, type=int)
        db = dao.get_file_db()
        last_month = xutils.days_before(days, format=True)
        user_name  = xauth.get_current_user()["name"]
        rows = db.query("SELECT * FROM file WHERE creator = $creator"
            + " AND sctime >= $ctime ORDER BY sctime DESC", 
            dict(creator=user_name, ctime=last_month))
        result = dict()
        for row in rows:
            date = re.match(r"\d+\-\d+", row.sctime).group(0)
            row.url = "/file/view?id={}".format(row.id);
            # 优化数据大小
            row.content = ""
            if date not in result:
                result[date] = []
            result[date].append(row)

        return xutils.json_str(**result)