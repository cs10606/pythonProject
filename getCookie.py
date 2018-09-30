def test_get_token():
    hdata = {
        "username": husername,
        "password": hpassword,
        "otp": hotp}
    headers = {'content-type': hcontent_type
               }
    r = requests.post(hurl + '/login', data=json.dumps(hdata), headers=headers)
    hjson = json.loads(r.text)  # 获取并处理返回的json数据
    herror = "error"
    if herror in hjson:
        print("登陆失败，退出程序！")
        exit()
    else:
        hcode = str(hjson['code'])
        print('请求返回状态为：' + hcode)
        if hcode == table.cell(9, 1).value:
            token = hjson['data']['token']  # 获取token
            print('当前token为：' + token)
            # 将获取的TOKEN保存到testdata中
            oldWb = xlrd.open_workbook('C:/Jin/workpase/ApiTest/src/testdata.xls', formatting_info=True)
            newWb = copy(oldWb)
            newWs = newWb.get_sheet(0)
            newWs.write(8, 1, token)
            print("Token写入成功")
            newWb.save('C:/Jin/workpase/ApiTest/src/testdata.xls')
            print("TestdDate保存成功")

        else:
            print('登陆失败，程序退出')
            exit()