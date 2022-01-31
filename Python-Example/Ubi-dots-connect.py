from ubidots import ApiClient

# API KEY QUE É RETIRADA DO SITE
api = ApiClient("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# PEGA O ID DO DEVICE QUE VAI SER UTILIZADO
my_device = api.get_variable('XXXXXXXXXXXXXXXXX')

last_value = my_device.get_values()
print(last_value)

