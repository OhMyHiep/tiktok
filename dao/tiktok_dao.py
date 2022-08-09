from tkinter.messagebox import NO

from pip import List
from models.tiktok import TikTok
from util import db_util
from datetime import datetime

class TikTokDao():

    def tiktok_mapper(self,dbRecord:tuple)->TikTok:
        if dbRecord is not None:
            return TikTok(dbRecord[0],datetime.timestamp(dbRecord[1]),dbRecord[2])
        return None


    def add_tiktok(self,tk:TikTok)->TikTok:
        sql="""insert into Tiktok (tk_link,date_added,downloaded_title)
                values(%s,%s,%s) RETURNING *;"""
        result=db_util.executeSimpleQuery(sql,tk.tk_link,tk.date_added,tk.downloaded_title)
        
        if result is not None:
            return self.tiktok_mapper(result[0])
        return None
        

    def get_all(self)->list:
        sql="""SELECT * From Tiktok"""
        result=db_util.executeSimpleQuery(sql)
        tiktok_list:list=[]
        for tuple in result:
            a=self.tiktok_mapper(tuple)
            tiktok_list.append(a)
        return tiktok_list

  
    def update(self,tk:TikTok)->TikTok:
        sql="""UPDATE Tiktok
                SET downloaded_title=%s
                WHERE tk_link=%s RETURNING *;"""
        result=db_util.executeSimpleQuery(sql,tk.downloaded_title,tk.tk_link)
        if result is not None:
            return self.tiktok_mapper(result[0])
        return None


    def get_tiktok_by_id(self,tk:TikTok):
        sql="""SELECT * 
                FROM Tiktok 
                WHERE tk_link=%s;"""
        result=db_util.executeSimpleQuery(sql,tk.tk_link)
        if result is not None:
            return self.tiktok_mapper(result[0])
        return None