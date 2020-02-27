import unittest
import common.HTMLTestRunner_cn as Runner

casePath = "./case"
rule = "test_*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
print(discover)

with open("report.html", "wb") as f:
    runner = Runner.HTMLTestRunner(stream=f, title="报告名", description="报告描述", retry=1)
    runner.run(discover)
