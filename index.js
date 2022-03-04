const { spawn } = require("child_process");
const express = require("express");

const app = express();

app.get("/", function (req, res) {
  const child_python = spawn("python", ["codespace.py"]);
  child_python.stdout.on("data", (data) => {
	let x = data.toString();
    var map = JSON.parse(x);
	res.send(map);
  });
  child_python.stderr.on("data", (data) => {
	res.send("Error" + data);
    console.error("stderr" + data);
  });
  child_python.on("close", (code) => {
    console.log("std code" + code);
  });
});

const port = process.env.PORT || "3000";
app.listen(port, function () {
  console.log("Server started at port " + port);
});
