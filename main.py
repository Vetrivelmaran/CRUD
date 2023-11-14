from fastapi import FastAPI

app = FastAPI()
stu_data=[{'name':'vetri',"age":23,'id':1},{"name":"pravin","age":22,'id':2},
          {
              'id':3,'age':23,'name':'david'
          }]

@app.get("/")
async def root():
    return {"message": "Hello World"}
# get by id
@app.get('/getbyid/{id}')
async def getById(id:int):
    if id!=0:
        return stu_data[id-1]
    else:
        return 'not id found'
# get by name
@app.get('/getbyname/{name}')
async def getName(name:str):
  for i in stu_data:
      if i['name']==name:
          return i
  return 'not found data'

# get by ID
@app.post('/add')
async def addbyid(id:int,age:int,name:str):
    stu_data.append({'id':id,'name':name,'age':age})
    return stu_data
@app.put('/edit/{id}')
async def edit(id:int,name:str,age:int):
    s =stu_data[id-1]
    s['name']=name
    s['age']=age
    return s

# delete by id 
@app.delete('/delete')
async def  delete(id:int):
    deleted_stu=stu_data.pop(id-1)
    return {'deleted id':id,'delede data':deleted_stu}