const express = require("express");
const { spawn } = require("node:child_process");
const path = require("path");
const cors = require("cors")
const translate = require('@vitalets/google-translate-api');


const app = express();
app.use(cors());          
app.use(express.json()); 


const py = spawn(
  "/home/storm/techsprint/env/bin/python3",
  ["-u","/home/storm/techsprint/public/rag2.py"]
);

async function translateToEnglish(text) {
  try {
    const res = await translate(text, { to: 'en' });
    return res.text;
  } catch (err) {
    console.error("Translation error:", err);
    return text;
  }
}

console.log("Starting")

let pythonReady = false;

py.stdout.on("data", data => {
    const msg = data.toString().trim();
    if (msg === "RAG_READY") {
        pythonReady = true;
        console.log("Python RAG is ready");
    }
});

py.stderr.on("data", err => {
    console.error("PYTHON ERROR:", err.toString());
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index2.html"));
});

app.post("/ask", (req, res) => {
    if (!pythonReady) {
        return res.status(503).json({ error: "RAG not ready" });
    }

    const query = req.body.query;
    console.log("quer received")
    py.stdin.write(query + "\n");

    py.stdout.once("data", data => {
        const [answer, confidence] = data.toString().split("||");
        console.log(answer)
        res.json({
            answer: answer.trim(),
            confidence: confidence.trim()
        });
    });
});

app.listen(4000, () => {
    console.log("server running");
});
