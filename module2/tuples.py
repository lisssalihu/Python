# words=("spam","white","black")
#
# # word[0]="red"
# print(words[2])
#
# person=("Alice", 30,'Engineer')
#
# name,age,proffesion=person
#
# print(name, "'s", "proffesion is", proffesion,"and she is",age,"years old")
from urllib3.poolmanager import key_fn_by_scheme

# dictionaries
#
# contact_info={
#     "Alice":"555-3433",
#     "Bob":"5558098"
# }
#
# alice_phone=contact_info['Alice']
# print(alice_phone)
#
# contact_info['Daris']='138129232'
#
# print(contact_info)
#
#
# # del contact_info['Bob']
# # print(contact_info)
#
#
# keys=contact_info.keys()
# print(keys)
#
# values=contact_info.values()
# print(values)
#
# items=contact_info.items()
# print(items)


# contact_info={
#     "Alice":{
#         "phone":"344 34243",
#         "email":"alice@gmail.com"
#     }
# }

contact_info={
    "Alice":("344 34243","alice@gmail.com")
}

alice_info=contact_info['Alice']
phone=alice_info[0]

print(phone)







