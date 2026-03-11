## dumps(): use to perform encryption
## loads(): use to perform decryption

'''
1. Json,
2. pickle
'''

# import json
# file = open('temp1.txt','a+')
# data = {
#     'fullname': 'Niteesh',
#     'userid': 1234,
#     'password': '*****',
# }
# print(f'original data: {data}')
# print(f'Type of original data: {type(data)}')

# enc_data = json.dumps(data)
# file.write(enc_data)

# file.seek(0)
# enc_data = file.read()
# print(type(enc_data))

# ori_data = json.loads(enc_data)
# print(ori_data, type(ori_data))
# print(f'original data: {enc_data}')
# print(f'Type of original data: {type(enc_data)}')

# dec_data = json.loads(enc_data)
# print(f'original data: {dec_data}')
# print(f'Type of original data: {type(dec_data)}')


import pickle
file = open('temp1.txt','ab+')
data = {
    'fullname': 'Niteesh',
    'userid': 1234,
    'password': '*****',
}
# print(f'original data: {data}')
# print(f'Type of original data: {type(data)}')

enc_data = pickle.dumps(data)
file.write(enc_data)

file.seek(0)
enc_data = file.read()
print(type(enc_data))

ori_data = pickle.loads(enc_data)
print(ori_data, type(ori_data))

file.close()