import speedtest
from random import randrange
from time import sleep

from TestResult import TestResult


class TestManager:
    def __init__(self, mockData):
        self.results = []
        self.mockData = mockData
        self.promptConfig()

        if not self.mockData:
            self.__servers = []
            self.__speedTest = speedtest.Speedtest()
            self.__speedTest.get_servers(self.__servers)
            self.__speedTest.get_best_server()

    def speedtest(self):
        executions = self.__executions

        while executions > 0:
            if not self.mockData:
                self.__speedTest.download(threads=1)
                self.__speedTest.upload(threads=1)

                download = self.__speedTest.results.download
                upload = self.__speedTest.results.upload
                timestamp = self.__speedTest.results.timestamp
                self.results.append(TestResult(download, upload, timestamp))
            else:
                download = randrange(1, 100000000)
                upload = randrange(1, 50000000)
                self.results.append(TestResult(download, upload, ""))

            executions -= 1
            sleep(self.__interval)
            print("Noch {} Tests übrig!".format(executions))

    def promptConfig(self):
        self.__interval = int(input(
            "Wieviele Sekunden soll zwischen den Tests gewartet werden? "))
        self.__executions = int(input(
            "Wie oft soll der Test durchgeführt werden? "))
