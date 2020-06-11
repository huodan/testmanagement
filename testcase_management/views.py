from django.shortcuts import render
from django.http import JsonResponse
from testcase_management.models import Testcase
from datetime import datetime
from django.forms.models import model_to_dict



def get_testcases(request):
	"""
	查询测试用例
	:param request: json
	:return: 测试用例详情
	"""
	req_body = request.body
	import json
	if type(req_body) is not str:
		req_body = req_body.decode("utf-8")
	print("req:{}".format(req_body))
	req = json.loads(req_body)  # todo 支持查询 当前是返回所有用例

	# 返回查询的用例信息
	query_sets = Testcase.objects.all()
	testcase_list = []
	for item in query_sets:
		testcase = model_to_dict(item)
		testcase_list.append(testcase)

	reply = {
		"return_code": "00",
		"message": "success",
		"data": testcase_list
	}
	print("res:{}".format(reply))
	return JsonResponse(reply)


def update_testcase(request):
	"""
	修改用例信息
	:param request: json
	req:{
        "id": 2, # 用例id
        "data": # 修改数据
        	{
                "name": "充值失败",
                "module": "payment"
        	}
		}
	:return:
	"""
	req_body = request.body
	import json
	if type(req_body) is not str:
		req_body = req_body.decode("utf-8")
	print("req:{}".format(req_body))
	req = json.loads(req_body)

	# 更新用例
	Testcase.objects.filter(id=req["id"]).update(**req["data"])

	# 返回用例更新后的信息
	query_sets = Testcase.objects.get(id=req["id"])
	testcase_list = []
	testcase = model_to_dict(query_sets)
	testcase_list.append(testcase)
	reply = {
		"return_code": "00",
		"message": "success",
		"data": testcase_list
	}
	print("res:{}".format(reply))
	return JsonResponse(reply)


def create_testcase(request):
	"""

	:param request:
	:return:
	"""
	req_body = request.body
	import json
	if type(req_body) is not str:
		req_body = req_body.decode("utf-8")
	print("req:{}".format(req_body))
	req = json.loads(req_body)

	# 插入新增用例数据
	tc = Testcase(**req["data"])
	tc.save()
	query_sets = Testcase.objects.get(id=tc.id)
	testcase_list = []
	testcase = model_to_dict(query_sets)
	testcase_list.append(testcase)
	reply = {
		"return_code": "00",
		"message": "success",
		"data": testcase_list
	}
	print("res:{}".format(reply))
	return JsonResponse(reply)


def get_testplans():
	pass


def update_testplan():
	pass


def create_testplan():
	pass


def run_testcase():
	pass


def run_testplan():
	pass
