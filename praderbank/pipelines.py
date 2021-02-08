import re
import sqlite3


class PraderbankPipeline:
    conn = sqlite3.connect('praderbank.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `praderbank` (
                                                                        title varchar(100),
                                                                        description text
                                                                        )''')
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            title = item['title']
            title = re.sub('"', "'", title).strip()
        except:
            title = ''
        try:
            description = item['description']
            description = re.sub('"', "'", description)
        except:
            description = ''

        self.cursor.execute(f'''select * from praderbank where title = "{title}"''')
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(
                f'''insert into `praderbank` (`title`, `description`) values ("{title}", "{description}")''')
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
