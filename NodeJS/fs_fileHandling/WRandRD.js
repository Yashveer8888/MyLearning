const fs=require("fs");

// create file
//fs.create


// Sync...      blocking...
fs.writeFileSync("./test.txt","hello yashveer");
// ASync...     Non-blocking...
fs.writeFile("./test.txt","hello yashveer Async",(err)=>{});


// Sync...  
const result=fs.readFileSync("./test.txt","utf-8");
console.log(result);
// Async...
fs.readFile("./test.txt","utf-8",(err,result)=>{
   if(err){
      console.log("Error",err);
   }
   else{
      console.log(result);
   }
});


// Sync...
fs.appendFileSync("./test.txt"," hello yashveer Async");
//Async...
fs.appendFile("./test.txt"," hello yashveer Async",(err)=>{});