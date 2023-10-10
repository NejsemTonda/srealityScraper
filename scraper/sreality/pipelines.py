# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface



from itemadapter import ItemAdapter
import psycopg2

class SrealityPipeline(object):
    def __init__(self):
        raise NotImplementedError("to use this pipeline you need to fill up the PostgreSQL form")
        hostname = '127.0.0.1'
        port = '5423'
        username = 'POSTGRE_USER'
        password = 'POSTGRE_PASSWORD'
        database = 'flats'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        # Insert the JSON data into PostgreSQL
        try:    
            insert_query = "INSERT INTO flats (title, url_images) VALUES (%s, %s)"
            self.cursor.execute(insert_query, (item['name'], item['imgs']))
            self.conn.commit()
        except Exception as e:
            self.connection.rollback()
            spider.logger.error(f"Error inserting item into PostgreSQL: {e}")
        finally:
            cursor.close()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

