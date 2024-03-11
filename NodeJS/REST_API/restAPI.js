const express=require("express");
const users=require("./MOCK_DATA.json")
const app=express();
const PORT=8001;

app.get("/",(req,res)=>res.json("home page"));

app.get("/api/users",(req,res)=>{
   return res.json(users);
})

app.route("/api/users/:id")
.get((req,res)=>{
   const id=Number(req.params.id);
   const user=users.find((user=>user.id===id))
   return res.json(user)
})
.put((req,res)=>{
   
})
.delete((req,res)=>{
   
});
app.listen(PORT,()=> console.log(`severe strated at port {PORT}`));