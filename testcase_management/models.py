from django.db import models


class Testcase(models.Model):

	id = models.AutoField(primary_key=True)  # 主键
	name = models.CharField("用例名",max_length=160,db_index=True)
	module = models.CharField("模块名",default="transaction",max_length=80,db_index=True)
	submodule = models.CharField("子模块名", max_length=80,db_index=True)
	conditions = models.TextField("前置条件")
	steps = models.TextField("步骤")
	expect = models.TextField("预期值")
	priority = models.IntegerField("优先级", default=0)
	type = models.CharField("执行方式",default="自动",max_length=32) # 自动、半自动、手动
	autotest_path = models.CharField("关联自动化用例路径",default="", max_length=128)
	ticket = models.CharField("关联jira",default="", max_length=20,db_index=True)
	create_time = models.IntegerField("创建时间",default=0)
	update_time = models.IntegerField("更新时间",default=0)
	author = models.CharField("创建者", default="dan.huo", max_length=32)
	extra_data = models.TextField("备注")


	class Meta:
		db_table = 'testcase_tab'


class Testplan(models.Model):

	id = models.AutoField(primary_key=True)  # 主键
	plan_name = models.CharField("测试计划名称",default="",max_length=128,db_index=True)
	plan_describe = models.TextField("测试计划描述")
	author = models.CharField("创建者",default="dan.huo",max_length=32)
	create_time = models.IntegerField("创建时间")


	class Meta:
		db_table = 'testplan_tab'


class TestPlanMidTab(models.Model):

	id =  models.AutoField(primary_key=True)  # 主键
	testcase_id = models.ForeignKey(Testcase, to_field="id", on_delete=models.CASCADE, db_column='testcase_id', db_index=True)  # 测试用例编号
	testplan_id = models.ForeignKey(Testplan, to_field="id", on_delete=models.CASCADE, db_column='testplan_id', db_index=True)  # 测试计划编号

	class Meta:
		db_table = 'testplan_mid_tab'



class TestcastRunLog(models.Model):

	id = models.AutoField(primary_key=True)  # 主键
	testcase_id = models.ForeignKey(Testcase,to_field="id",on_delete=models.CASCADE,db_column='testcase_id',db_index=True)  # 测试用例编号
	testplan_id = models.ForeignKey(Testplan,to_field="id",on_delete=models.CASCADE,db_column='testplan_id',db_index=True)  # 测试计划编号
	result = models.BooleanField("执行结果")
	run_log = models.TextField("执行过程日志")
	run_time = models.IntegerField("执行时间")


	class Meta:
		db_table = 'testcase_run_log_tab'


