import time,unittest
from HTMLTestRunner import HTMLTestRunner

test_dir='./test_case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    report_dir='./test_report'
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'
    with open(report_name,'wb')as f:
        runner=HTMLTestRunner(stream=f,title="测试报告标题",description="测试报告副标题")
        runner.run(discover)
    f.close()