const express = require("express");
const app=express();

// app.method(path,handler)

app.get("/",(req,res)=> res.end("hello from Home page"));
app.get("/about",(req,res)=> res.end("hello from about page"));

app.listen(8000,()=> console.log("server started..."))