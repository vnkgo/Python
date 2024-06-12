class cellphone:
    __is_5g_enable=False
    def __check_5g_enable(self):
        if self.__is_5g_enable==True:
            print("5G开启")
        else:
            print("5g关闭")

    def call_by_5g(self):
        self.__check_5g_enable()
        print("正在通话中")


phone=cellphone()
phone.call_by_5g()