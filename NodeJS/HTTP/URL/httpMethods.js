const url=require("url");
const http=require("http");
const fs=require("fs");

const myserver = http.createServer((req,res)=>{
   const log = `${Date.now()}: (${req.method}) (${req.url}) new req received\n`;
   const myurl=url.parse(req.url);
   console.log(myurl);
   fs.appendFile("log.txt",log,(err,data)=>{
      switch(myurl.pathname){
         case"/":
         if(req.method==="GET") res.end("Home Page");
         break;
         case "/about": res.end("about");
         break;
         case '/search': res.end("here are your reslut for ");
         break
         case '/signup':
            if(req.method==="GET") res.end("this is signup form");
            else if(req.method==="POST") res.end("success");
            break
         default:res.end("404 not found");

      }
   })
});

myserver.listen(8000,()=>console.log("server started..."));