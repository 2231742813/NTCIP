
# print(len(b'\x30\x3a\x02\x01\x00\x04\x0d\x61\x64\x6d\x69\x6e\x69\x73\x74\x72\x61\x74\x6f\x72\xa3\x26\x02\x01\x0c\x02\x01\x00\x02\x01\x00\x30\x1b\x30\x19\x06\x10\x2b\x06\x01\x04\x01\x89\x36\x04\x02\x03\x05\x08\x01\x03\x03\x01\x04\x05\x37\x37\x37\x37\x37'))
# print(len('3039020100040d61646d696e6973747261746f72a32502012e020100020100301a301806102b060104018936040203050801030301040432323232')/2)
# print(len('3038020100040d61646d696e6973747261746f72a3240201400201000201003019301706102b0601040189360402030508010303010403333333')/2)



# def encode_length(length ):
#     if length <= 127:  # 短格式
#
#         offset = length.to_bytes(2, byteorder = 'big', signed = True)
#         print(offset)
#         print(offset.hex())
#
#         return bytes([length])
#     els e:  # 长格式
#         encoded_bytes = [(length & 0x7F) | 0x80]  # 第一个字节的前七位为1，表示长格式
#         length >>= 7  # 右移7位，处理下一个字节
#         while length > 0:
#             encoded_bytes.insert(0, (length & 0x7F) | 0x80)  # 每个字节的前七位为1，表示后面还有字节
#             length >>= 7  # 右移7位，处理下一个字节
#         return bytes(encoded_bytes)


# # 示例用法
# length1 = 57
# encoded = encode_length(length1)
# print(encoded.hex())  # 输出结果为：1e
# print(type(encoded))

#
# hahah = '12'
# print(hahah[0:1:])
# print(hahah[1:2:])


# length = 169
# encoded = encode_length(length)
# print(encoded.hex())  # 输出结果为：81a9
#
# length = 1500
# encoded = encode_length(length)
# print(encoded.hex())  # 输出结果为：8205dc

# num1 = 57
# byte_data1 = bytes([num1 // 10 + 48, num1 % 10 + 48])
# print(byte_data1)  # 输出结果为：b'0:'
# print(byte_data1.hex())
#
# num2 = 56
# byte_data2 = bytes([num2 // 10 + 48, num2 % 10 + 48])
# print(byte_data2)  # 输出结果为：b'09'
# print(byte_data2.hex())


# numbers = [63, 29, 30, 80, 100, 300]
#
# byte_data = []
# for num in numbers :
#
#     if num < 128 :
#         byte_data.append(bytes([0x30, num]))
#     else :
#         byte_data.append(bytes([0x31, num - 128]))
#
# for data in byte_data :
#     print(data)
#     print(data.hex())

#
# def head_Convert(num1) :
#     if num1 < 128 :
#         res = bytes([0x30, num1])
#         return res
#     else :
#         return bytes([0x31, num1 - 128])


# a = head_Convert(24)
# print(a)
# print(a.hex())


def encode_length(length) :
    if length < 128 :
        res = bytes([0x30, length])
        return res
    else :
        return bytes([0x31, length - 128])


a = encode_length(24)
print(a)
print(a.hex())
