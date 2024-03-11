const url=require("url");
const http=require("http");
const fs=require("fs");

const myserver = http.createServer((req,res)=>{
   const log = `${Date.now()}: ${req.url} new req received\n`;
   const myurl=url.parse(req.url);
   console.log(myurl);
   fs.appendFile("log.txt",log,(err,data)=>{
      switch(myurl.pathname){
         case"/":res.end("HomePage");
         break;
         case '/about':
            const name=myurl.query.myname;
            res.end(`hi,{username}`);
         break;
         case '/search':
            const search=myurl.query.search_query;
            res.end("here are your reslut for "+search);
         default:res.end("404 not found");

      }
   })
});

myserver.listen(8000,()=>console.log("server started..."));