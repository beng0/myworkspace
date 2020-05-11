import uiautomator2 as u2

# d = u2.connect()
# print(d.info)

d = u2.connect('P7C0218115006106')
print(d.info)

d.settings['xpath_debug']=True
d.settings['wait_timeout']=20
d.set_new_command_timeout(300)

d.implicitly_wait(10)
d(xpath="//*[@text='筑龙标事通'']").click()
print("wait timeout",d.implicitly_wait())