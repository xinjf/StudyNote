import os
import unittest


def choose_all_cases(case_suite, pattern):
    """
    获取指定路径下所有的测试用例
    :param
    pattern: 匹配模式
    case_suite: 执行的用例集的文件
    cases_path: case的路径
    :return: 测试用例集"""
    case_suite = os.path.join(cases_path, case_suite)
    discover_all_cases = unittest.defaultTestLoader.discover(case_suite, pattern=pattern,
                                                             top_level_dir=None)
    return discover_all_cases






