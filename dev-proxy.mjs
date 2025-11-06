import express from "express";
import fetch from "node-fetch";

const app = express();
const ORIGIN = "https://vmslide.med.wayne.edu/slides";

// Proxies ANYTHING after /tiles/ to the upstream /slides/
app.get("/tiles/*", async (req, res) => {
  const rest = req.params[0]; // e.g. "WS_057/6/22/30.jpg" or "LH0098/6/23/30.jpg"
  const upstream = `${ORIGIN}/${rest}`;
  console.log("→", upstream);

  const r = await fetch(upstream, {
    // Some servers require this; harmless to include:
    headers: { Referer: "https://webslide2.med.wayne.edu" },
  });

  res.set("Access-Control-Allow-Origin", "*");
  res.set("Cache-Control", "public, max-age=3600");
  res.status(r.status);
  if (!r.ok) return res.end();
  r.body.pipe(res);
});

app.listen(8787, () => {
  console.log("Tile proxy: http://localhost:8787/tiles/<everything after /slides/>");
});
