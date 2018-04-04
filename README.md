### background
华南理工大学毕业设计：
- 爬取soscholar学者、文章信息，并存储在数据库

### step
```
读取姓名列表names
for name in names:
    get authors by search name:
        for author in authors:
            调用soscholar接口获取Author信息并存储到数据库
            获取author的合作者：调用soscholar接口获取合作者信息并存储到数据库
            获取author的paper: 调用soscholar接口获取paper并存储到数据库
```

### database
sql
```
学者信息
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| author_id    | varchar(255) | NO   | PRI | NULL    |       |
| name         | varchar(255) | NO   |     | NULL    |       |
| image_url    | varchar(255) | NO   |     | NULL    |       |
| organization | varchar(255) | NO   |     | NULL    |       |
| home_page    | varchar(255) | NO   |     | NULL    |       |
| paper_count  | int(11)      | YES  |     | NULL    |       |
| citied_count | int(11)      | YES  |     | NULL    |       |
| g_index      | int(11)      | YES  |     | NULL    |       |
| h_index      | int(11)      | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+


文章
+-----------+----------------+------+-----+---------+-------+
| Field     | Type           | Null | Key | Default | Extra |
+-----------+----------------+------+-----+---------+-------+
| paper_id  | varchar(255)   | NO   | PRI | NULL    |       |
| title     | varchar(10240) | NO   |     | NULL    |       |
| abstract  | varchar(10240) | NO   |     | NULL    |       |
| cited_num | int(11)        | YES  |     | NULL    |       |
| cite_num  | int(11)        | YES  |     | NULL    |       |
| url       | varchar(255)   | NO   |     | NULL    |       |
| publisher | varchar(255)   | YES  | MUL | NULL    |       |
+-----------+----------------+------+-----+---------+-------+

研究领域
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| domain_id | varchar(255) | NO   | PRI | NULL    |       |
| name      | varchar(255) | NO   |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+

```


### deploy
- 首先：先创建数据库soscholar
```
create database soscholar
```

- 修改配置文件，填入你的access_token和数据库信息
```
cd sospider
cp config.sample config.py
vim config.py
cd ..
```

- 接着运行以下命令（python3）
```
pip install -r requirements
cd sospider
python main.py
```