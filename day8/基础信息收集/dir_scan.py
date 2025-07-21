import requests


class DirScan():
    def run(self, url, dir_dict):
        dic_list = []
        dics = open(dir_dict, 'r', encoding='utf-8').readlines()
        for dic in dics:
            res = requests.get(url + dic.replace('\n', '')).status_code
            if res != 404:
                dic_list.append(url + dic.replace('\n', ''))
                print(url + dic.replace('\n', ''))
        return dic_list


# dir_scan = DirScan()
# dir_scan.run('https://gbdsj.gd.gov.cn/gkmlpt/', 'test/dict.txt')
