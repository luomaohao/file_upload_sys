####文档
***
文档是 MongoDB 的核心，类似于 SQLite 数据库（关系数据库）中的每一行数据。多个键及其关联的值放在一起就是文档。在 Mongodb 中使用一种类 json 的 bson 存储数据，bson 数据可以理解为在 json 的基础上添加了一些 json 中没有的数据类型。

例如：

```json
{"company":"Chenshi keji"}
```

#####文档间的联系
***
1.

```json
# 这就是嵌入式的关系
{
   "name": "Tom Hanks",
   "contact": "987654321",
   "dob": "01-01-1991",
   "address":
   [{
   "building": "22 A, Indiana Apt",
   "pincode": 123456,
   "city": "chengdu",
   "state": "sichuan"
   },
   {
   "building": "170 A, Acropolis Apt",
   "pincode": 456789,
   "city": "beijing",
   "state": "beijing"
   }]
}
```

2. 引用式关系

```json
{
   "name": "Tom Benzamin",
   "contact": "987654321",
   "dob": "01-01-1991",
   "address_ids": [
      ObjectId("52ffc4a5d85242602e000000")    #对应address文档的id字段
   ]
}
```
在实际应用的时候，嵌入式关系比较适合一对一的关系，引用式关系比较适合一对多或者多对多的情况

####集合
***
例如：
```json
{"company":"Chenshi keji"} {"people":"man","name":"peter"}
```

#### save() 与 insert()的区别
***
为了方便记忆，可以先从字面上进行理解，insert 是插入，侧重于新增一个记录的含义；save 是保存，可以保存一个新的记录，也可以保存对一个记录的修改。因此，insert 不能插入一条已经存在的记录，如果已经有了一条记录(以主键为准)，insert 操作会报错，而使用 save 指令则会更新原记录。
