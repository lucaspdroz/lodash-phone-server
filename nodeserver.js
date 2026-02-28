const http = require("http");

const server = http.createServer((req, res) => {
  if (req.method === "POST" && req.url === "/compute") {
    let body = "";

    req.on("data", chunk => {
      body += chunk.toString();
    });

    req.on("end", () => {
      const data = JSON.parse(body);
      const { start, end } = data;

      let total = 0;
      for (let i = start; i < end; i++) {
        total += Math.sqrt(i);
      }

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ result: total }));
    });
  } else {
    res.writeHead(405);
    res.end("Method Not Allowed");
  }
});

server.listen(8000, "0.0.0.0", () => {
  console.log("Worker rodando na porta 8000");
});
