class DirScan():
    def run(self, url, dir_dict):
        dics = open(dir_dict, 'r').readlines()
        for dic in dics:
            print(dic)


dir_scan = DirScan()
dir_scan.run()
