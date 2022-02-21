print("欢迎致电10086客服，我们提供了以下服务：1、话费相关：2、业务办理：3、人工服务")
choice = input("请输入服务编号：")
if int(choice) == 1:
    print("我们为您提供以下服务："
          "1、话费查询"
          "2、话费充值")
    code1 = input("请输入您要的服务：")
    if code1 == "1":
        print("您的话费余额为100元整")
    elif code1 == "2":
        print("话费充值请转至人工服务")
elif int(choice) == 2:
    print("我们为您提供以下套餐："
          "1、冰淇淋套餐"
          "2、5G畅爽包")
elif int(choice) == 3:
    print("人工客服正忙，请您稍候再拨")
else:
    print("感谢您的来电，再见")
