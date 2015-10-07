# coding=utf-8
import ConfigParser
import json
import redis

import redisHelper

from flask import render_template, Flask,url_for, jsonify


__author__ = 'xuqh'

import sys

reload(sys)
sys.setdefaultencoding('utf8')


app = Flask(__name__)



#错误页
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route('/')
@app.route('/index')
def index():
	return  render_template('dashboard.html')


#redis服务器列表
@app.route('/redis/list')
def redisMonitor():
	redisList = redisHelper.rList

	return  render_template('redisIndex.html',redisList = redisList)

#某个redis实例信息
@app.route('/redis/<server>')
def redisDetail(server):
	list = redisHelper.rList

	for item in list:
		key = item["Host"] + ":" + item["Port"]

		if key == server:
			host = item["Host"]
			port = item["Port"]
			password = item["Password"]
			break

	dict = redisHelper.getRedisDetail(host,port,password)

	Summary = {
		"Server":key,
		"Name":item["Name"],
		"Version":dict["redis_version"],
		"Update":dict["uptime_in_days"],
		"Role":dict["role"],
		"Slaves":dict["connected_slaves"]
	}

	Stats = {
		"total_connections_received":dict["total_connections_received"],
		"total_commands_processed":dict["total_commands_processed"],
		"instantaneous_ops_per_sec":dict["instantaneous_ops_per_sec"],
		"keyspace_hits":dict["keyspace_hits"],
		"keyspace_misses":dict["keyspace_misses"],
		"expired_keys":dict["expired_keys"]
	}

	Memory = {
		"used_memory":dict["used_memory_human"],
		"used_memory_rss":dict["used_memory_rss"],
		"used_memory_peak":dict["used_memory_peak_human"],
		"used_memory_lua":dict["used_memory_lua"],
		"mem_fragmentation_ratio":dict["mem_fragmentation_ratio"]
	}

	dbList = []

	for i in range(0,15):
		dbKey = 'db' + str(i)

		if dict.has_key(dbKey):
			dbList.append({"dbid":i,"avg_ttl":dict[dbKey]["avg_ttl"],"expires":dict[dbKey]["expires"],"KeyNum":dict[dbKey]["keys"]})


	return  render_template('redisDetail.html',host=server,Summary=Summary,Stats=Stats,Memory=Memory,DbList=dbList)

@app.route('/json/<server>')
def testJson(server):
	list = redisHelper.rList

	for item in list:
		key = item["Host"] + ":" + item["Port"]

		if key == server:
			host = item["Host"]
			port = item["Port"]
			password = item["Password"]
			break

	dict = redisHelper.getRedisInfo(host,port,password)

	return jsonify(dict)



if __name__ == '__main__':
	app.run(debug=True)

