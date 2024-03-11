const http=require("http");
const fs=require("fs");

const myserver = http.createServer((req,res)=>{
   const log = `${Date.now()}: (${req.url}) new req received\n`;
   fs.appendFile("log.txt",log,(err,data)=>{
      switch(req.url){
         case"/":res.end("HomePage");
         break;
         case '/about':res.end("I am yashveer singh");
         break;
         default:res.end("404 not found");

      }
   })
});
myserver.listen(8000,()=>console.log("server started..."));