from models.tiktok import TikTok
from util import db_util

class TikTokDao():

    def add_tiktok(self,tk:TikTok):
        sql="""insert into Tiktok (tk_link,date_added,downloaded_title)
                values=? RETURNING *"""
        db_util.executeSimpleQuery(sql,tk.tk_link,tk.date_added,tk.downloaded_title)

    
    def get_all(self):
        sql="""SELECT * From Tiktok"""
        result=db_util.executeSimpleQuery(sql)
        print(result[0])
        print(type(result[0]))


    def tiktok_mapper(self,dbResult:list):
        tiktok_list=[]
        for tuple in dbResult:
            TikTok(tuple[0],tuple[1],tuple[2])
        pass
