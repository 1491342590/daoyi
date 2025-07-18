import requests


class DirScan():
    def run(self, url, dir_dict):
        dics = open(dir_dict, 'r').readlines()
        for dic in dics:
            res = requests.get(url + dic.replace('\n', '')).status_code
            if res != 404:
                print(url + dic.replace('\n', ''))


dir_scan = DirScan()
dir_scan.run()
