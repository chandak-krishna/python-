#dictionary
dict={
   "key" : "value",
   "name" : "krishna ",
   "age" : 18,
   "marks" : 93.5,
   "subject":["c++","c","python" ,"java"],
   "topics":("dict","set"),
   1:"best",
   

}
null_dic={}
print(null_dic)
print(dict)
print(type(dict))
dict["name"]="krishna chandak"#changing the value 
print(dict)
#nesting dictionary
student={
    "name":"krishna",
    "subject":{
        "pyh":98,
        "chem": 67,
        "maths":45
    }
}
print(student)
print(student["subject"]["chem"])
#dictionary methord 
#1) key()
print(student.keys())
#2) vaues()
print(student.values())
#3) items ()
print(student.items())
#4) get
print(student.get("name"))
#5) update
new_dict={"city":"jodhpur"}
student.update(new_dict)
print(student)