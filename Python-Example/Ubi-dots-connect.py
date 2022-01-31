from ubidots import ApiClient

# API KEY QUE É RETIRADA DO SITE
api = ApiClient("BBFF-e93867912285537517c307dc821ec8bd09b")

# PEGA O ID DO DEVICE QUE VAI SER UTILIZADO
my_device = api.get_variable('61e1d9dd1d8472662f59d711')

last_value = my_device.get_values()
print(last_value)

