import os
import time
from StudyNote.APIAuto_study.html_report import htmltestrunner


def generate_htmlreport():
    """
    生成测试报告
    :param
    report_path： 生成html报告的路径
    htmltestrunner: 生成html报告的模板
    """
    time_now = time.strftime("%Y_%m_%d-%H_%M_%S_")
    htmlreport = time_now + "report.html"
    fp = open(os.path.join(report_path, htmlreport), "wb")
    runner = htmltestrunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title="测试报告",
        description="用例执行情况:",
    )
    return runner
