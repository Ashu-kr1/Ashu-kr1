# Dict
# Key and value
#name - > "Pramod"

student_infor = {
"name":"Ashu",
"age":67,
"address":"KA"
}

print(student_infor)
print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])

student_infor["age"] = 100

student_infor = dict(name ="Pramod",age="67",address="KA")
print(student_infor)

student_infor1={
    "name" : "Ashu",
    "age":25,
    "address" : {
        "home_adrress":"NA",
        "office_address":"KA"
    }
}

student_infor2= {
    "name" : "Ashu",
    "age":25,
    "address" : {
        "home_adrress":"NA",
        "office_address":"KA"
    }
}

student_list = [f"student_list {student_infor1,student_infor2}"]
print(student_list)