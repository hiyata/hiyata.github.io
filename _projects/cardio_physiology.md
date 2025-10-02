---
layout: default
excerpt: An interactive learning tool for understanding the channels involved in generating action potential of cells of the heart.
title: Cardiac Cells Action Potential Channels Learning Tool 
category: cardiophysiology 
---

import React, { useMemo, useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Switch } from "@/components/ui/switch";
import { Label } from "@/components/ui/label";
import { Slider } from "@/components/ui/slider";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend, ReferenceLine, ReferenceDot } from "recharts";
import { RotateCcw } from "lucide-react";

/**
 * Ion Channel Action Potential Playground — Minimalist UI (Pro pass)
 * Modules added per request:
 *  - Phase-grouped controls (progressive disclosure)
 *  - Snapshot gallery + 2-way compare with diff table
 *  - Environment presets (Hypo-/Hyperkalemia, Ischemia)
 *  - Pacing control (BPM) + cycle-length coupling (adjusts phase 4)
 *  - Sensitivity mini-panel (±20% effect on APD90 & dV/dt_max)
 *
 * Notes:
 *  - Still a qualitative model; trends > exact biophysics.
 *  - Recharts `ReferenceLine` uses `segment` prop for leader stems.
 */

// ------------------------------ Constants ------------------------------
const BASELINE_PARAMS = {
  INa: 100, ICaL: 100, Ito: 100, IKr: 100, IKs: 100, IK1: 100,
  If: 100, ICaT: 100, IK_ACh: 100, NaKATPase: 100
};

const CHANNEL_LABELS = {
  INa: "I_Na (fast Na⁺)",
  ICaL: "I_CaL (L-type Ca²⁺)",
  Ito: "I_to (transient outward K⁺)",
  IKr: "I_Kr (rapid delayed rectifier K⁺)",
  IKs: "I_Ks (slow delayed rectifier K⁺)",
  IK1: "I_K1 (inward rectifier K⁺)",
  If: "I_f (funny)",
  ICaT: "I_CaT (T-type Ca²⁺)",
  IK_ACh: "I_K,ACh (ACh-activated K⁺)",
  NaKATPase: "Na⁺/K⁺-ATPase"
};

const CELL_TYPES = [
  { id: "ventricular", name: "Ventricular Myocyte", phases: [0,1,2,3,4], uses: { INa:1, ICaL:1, Ito:1, IKr:1, IKs:1, IK1:1, If:0, ICaT:0, IK_ACh:0, NaKATPase:1 } },
  { id: "atrial", name: "Atrial Myocyte",       phases: [0,1,2,3,4], uses: { INa:1, ICaL:1, Ito:1, IKr:1, IKs:1, IK1:1, If:0, ICaT:0, IK_ACh:1, NaKATPase:1 } },
  { id: "sa", name: "SA Node (Pacemaker)",     phases: [0,3,4],     uses: { INa:0, ICaL:1, Ito:0, IKr:1, IKs:1, IK1:1, If:1, ICaT:1, IK_ACh:1, NaKATPase:1 } },
  { id: "purkinje", name: "Purkinje Cell",      phases: [0,1,2,3,4], uses: { INa:1, ICaL:1, Ito:1, IKr:1, IKs:1, IK1:1, If:1, ICaT:1, IK_ACh:0, NaKATPase:1 } },
];

const DRUG_PRESETS = {
  None: {}, Lidocaine: { INa: 50 }, Tetrodotoxin: { INa: 5 }, Ranolazine: { INa: 70 }, Quinine: { INa: 60 },
  Verapamil: { ICaL: 40 }, Nifedipine: { ICaL: 50 }, Ivabradine: { If: 30 }, "Acetylcholine ↑": { IK_ACh: 150 },
  Ouabain: { NaKATPase: 40 }
};

// Environment presets (qualitative)
const ENV_PRESETS = {
  None: {},
  Hypokalemia: { IK1: 120, IKr: 90, IKs: 95 }, // more negative Vrest, mild APD↑
  Hyperkalemia: { IK1: 60, INa: 80 }, // depolarized rest, ↓upstroke
  Ischemia: { NaKATPase: 50, IK1: 70, IKr: 120 }, // pump↓, K+ efflux↑ → APD↓
};

// ------------------------------ Helpers ------------------------------
const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
const pct = (x) => clamp(x / 100, 0, 2);

/**
 * generateAP returns { data, marks, segs }
 * - data: array of {t, v}
 * - segs: array of { phase, tStart, tEnd }
 * - marks: array of { label, t, v } at midpoints of segs, with v on-curve
 */
function generateAP(cellId, params) {
  const isPacemaker = cellId === "sa";
  let t0 = 2, t1 = 8, t2 = 180, t3 = 120, t4 = 100;
  let vmax = 30, vrest = -85;
  const kINa = pct(params.INa), kICaL = pct(params.ICaL), kIto = pct(params.Ito);
  const kIKr = pct(params.IKr), kIKs = pct(params.IKs), kIK1 = pct(params.IK1);
  const kIf = pct(params.If), kICaT = pct(params.ICaT), kIK_ACh = pct(params.IK_ACh);
  const kPump = pct(params.NaKATPase);

  if (isPacemaker) {
    t1 = 0; t2 = 0; t0 = 15 / clamp(kICaL, 0.2, 2); vmax = 20 * kICaL;
    const kK = 0.6 * kIKr + 0.4 * kIKs; t3 = 150 / clamp(kK, 0.2, 2);
    const slope = 0.4 * kIf + 0.2 * kICaT - 0.3 * (kIK_ACh - 1);
    t4 = clamp(220 / clamp(1 + slope, 0.2, 3), 60, 600);
    vrest = -85 - 3 * (kPump - 1) + 3 * (1 - kIK1);
  } else {
    t0 = clamp(2 / clamp(kINa, 0.2, 2), 0.5, 6); vmax = 30 * clamp(kINa, 0.4, 1.6);
    t1 = clamp(8 * (0.6 + 0.4 * kIto), 2, 18);
    const kK = 0.6 * kIKr + 0.4 * kIKs; t2 = clamp(180 * (kICaL / clamp(kK, 0.3, 2)), 40, 400);
    t3 = clamp(120 / clamp(kK, 0.3, 2), 30, 300);
    vrest = -85 - 4 * (kPump - 1) + 5 * (1 - kIK1);
    if (cellId === "purkinje") {
      const s = 0.1 * (kIf - 1) + 0.05 * (kICaT - 1);
      t4 = clamp(100 / clamp(1 + s, 0.3, 2), 40, 300);
    } else { t4 = 100; }
  }

  const data = []; const push = (t, v) => data.push({ t, v });
  const segs = []; let tA = 0; const vTh = isPacemaker ? -40 : -60;

  // pacing adjustment: if a target cycle is set via params.__targetCycle, adjust t4 to fit
  if (params && typeof params.__targetCycle === 'number') {
    const baseCycle = t4 + t0 + (isPacemaker ? 0 : (t1 + t2)) + t3;
    const extra = params.__targetCycle - baseCycle;
    t4 = clamp(t4 + extra, 20, 1200);
  }

  // phase 4
  const n4 = Math.max(5, Math.round(t4 / 2));
  for (let i = 0; i <= n4; i++) { const f = i / n4; push(tA + f * t4, vrest + (vTh - vrest) * f); }
  segs.push({ phase: 4, tStart: tA, tEnd: tA + t4 }); tA += t4;

  // phase 0
  const n0 = Math.max(5, Math.round(t0 / 0.5));
  for (let i = 0; i <= n0; i++) { const f = i / n0; push(tA + f * t0, vTh + (vmax - vTh) * (1 - Math.pow(1 - f, 3))); }
  segs.push({ phase: 0, tStart: tA, tEnd: tA + t0 }); tA += t0;

  if (!isPacemaker) {
    // phase 1
    const notch = vmax - 20 * kIto, n1 = Math.max(3, Math.round(t1 / 0.5));
    for (let i = 0; i <= n1; i++) { const f = i / n1; push(tA + f * t1, vmax + (notch - vmax) * f); }
    segs.push({ phase: 1, tStart: tA, tEnd: tA + t1 }); tA += t1;

    // phase 2
    const plateau = -5 + 10 * (kICaL - (0.6 * kIKr + 0.4 * kIKs)), n2 = Math.max(10, Math.round(t2 / 2));
    for (let i = 0; i <= n2; i++) { const f = i / n2; push(tA + f * t2, notch + (plateau - notch) * (1 - Math.cos(Math.PI * f)) / 2); }
    segs.push({ phase: 2, tStart: tA, tEnd: tA + t2 }); tA += t2;
  }

  // phase 3
  const vEnd = vrest, vStart = isPacemaker ? vmax : (data[data.length - 1]?.v ?? vmax);
  const n3 = Math.max(10, Math.round(t3 / 2));
  for (let i = 0; i <= n3; i++) { const f = i / n3; push(tA + f * t3, vStart + (vEnd - vStart) * (1 - Math.cos(Math.PI * f)) / 2); }
  segs.push({ phase: 3, tStart: tA, tEnd: tA + t3 }); tA += t3;

  // labels
  const marks = segs.map(s => {
    const mid = (s.tStart + s.tEnd) / 2; let nearest = data[0];
    for (let i = 1; i < data.length; i++) if (Math.abs(data[i].t - mid) < Math.abs(nearest.t - mid)) nearest = data[i];
    return { label: `Phase ${s.phase}`, t: nearest.t, v: nearest.v };
  }).filter(m => !(cellId === "sa" && (m.label === "Phase 1" || m.label === "Phase 2")));

  return { data, marks, segs };
}

function computeMetrics(curve) {
  const pts = curve.data || curve; // backward compat if needed
  if (!pts.length) return { apd90: 0, dvdtMax: 0, cycle: 0 };
  const vrest = pts[0].v; const vmax = pts.reduce((m, p) => Math.max(m, p.v), -Infinity);
  const v90 = vrest + 0.1 * (vmax - vrest); const up = pts.findIndex(p => p.v > v90);
  let down = pts.length - 1; for (let i = pts.length - 1; i >= 0; i--) { if (pts[i].v > v90) { down = i; break; } }
  const apd90 = (up >= 0 && down > up) ? (pts[down].t - pts[up].t) : 0;
  let dvdtMax = 0; for (let i = 1; i < pts.length; i++) { const dv = pts[i].v - pts[i - 1].v; const dt = pts[i].t - pts[i - 1].t || 1e-6; dvdtMax = Math.max(dvdtMax, dv / dt); }
  const cycle = pts[pts.length - 1].t; return { apd90: Math.round(apd90), dvdtMax: Math.round(dvdtMax * 100) / 100, cycle: Math.round(cycle) };
}

function applyPreset(base, preset) {
  const out = { ...base };
  Object.entries(preset).forEach(([k, v]) => { if (k in out) out[k] = Math.round(out[k] * (v / 100)); });
  return out;
}

// ------------------------------ UI ------------------------------
export default function IonChannelPlayground() {
  const [cellTypeId, setCellTypeId] = useState("ventricular");
  const [name, setName] = useState("My Experiment");
  const [params, setParams] = useState({ ...BASELINE_PARAMS });
  const [ko, setKo] = useState({});
  const [preset, setPreset] = useState("None");
  const [envPreset, setEnvPreset] = useState("None");
  const [showCurrents, setShowCurrents] = useState(false);
  const [showBaseline, setShowBaseline] = useState(true);
  const [bpm, setBpm] = useState(60);
  const [snapshots, setSnapshots] = useState([]); // {id, name, cell, params, ko, preset, env, metrics}
  const [compareIds, setCompareIds] = useState([]); // up to 2 ids

  const cell = useMemo(() => CELL_TYPES.find(c => c.id === cellTypeId) || CELL_TYPES[0], [cellTypeId]);

  const workingParams = useMemo(() => {
    const env = applyPreset(params, ENV_PRESETS[envPreset] || {});
    const drugbed = applyPreset(env, DRUG_PRESETS[preset] || {});
    const out = { ...drugbed };
    Object.keys(ko).forEach(k => { if (ko[k]) out[k] = 0; });
    Object.keys(out).forEach(k => { if (!cell.uses[k]) out[k] = 0; });
    // pacing coupling
    const targetCycle = clamp(60000 / Math.max(20, Math.min(220, bpm)), 250, 3000);
    out.__targetCycle = targetCycle;
    return out;
  }, [params, preset, envPreset, ko, cell, bpm]);

  const baseline = useMemo(() => generateAP(cell.id, { ...BASELINE_PARAMS, __targetCycle: 60000 / bpm }), [cell.id, bpm]);
  const modified = useMemo(() => generateAP(cell.id, workingParams), [cell.id, workingParams]);
  const baseMetrics = useMemo(() => computeMetrics(baseline), [baseline]);
  const curMetrics = useMemo(() => computeMetrics(modified), [modified]);

  const laidOutMarks = useMemo(() => layoutPhaseMarks(modified.marks), [modified.marks]);

  function resetAll() { setParams({ ...BASELINE_PARAMS }); setKo({}); setPreset("None"); setEnvPreset("None"); setBpm(60); }
  const channelOrder = Object.keys(CHANNEL_LABELS).filter(k => cell.uses[k]);

  return (
    <div className="min-h-screen bg-white text-slate-900">
      {/* App header */}
      <header className="sticky top-0 z-10 bg-white/90 backdrop-blur supports-[backdrop-filter]:bg-white/70 border-b border-slate-200">
        <div className="max-w-6xl mx-auto px-4 md:px-8 h-14 flex items-center justify-between">
          <div className="font-semibold tracking-tight">Ion Channel AP Playground</div>
          <div className="flex items-center gap-2">
            <Button variant="ghost" size="sm" onClick={resetAll} className="h-8 px-3">Reset<RotateCcw className="w-4 h-4 ml-1"/></Button>
          </div>
        </div>
      </header>

      {/* Main grid */}
      <main className="max-w-6xl mx-auto px-4 md:px-8 py-6 md:py-10 grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Controls Column */}
        <section className="lg:col-span-4">
          <div className="mb-6">
            <div className="text-[13px] uppercase tracking-wide text-slate-500 mb-1">Session</div>
            <Input id="name" value={name} onChange={e => setName(e.target.value)} className="h-9" />
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
            <div>
              <div className="text-[13px] uppercase tracking-wide text-slate-500 mb-1">Cell Type</div>
              <Select value={cellTypeId} onValueChange={setCellTypeId}>
                <SelectTrigger className="h-9"><SelectValue placeholder="Cell type" /></SelectTrigger>
                <SelectContent>
                  {CELL_TYPES.map(c => (<SelectItem key={c.id} value={c.id}>{c.name}</SelectItem>))}
                </SelectContent>
              </Select>
            </div>
            <div>
              <div className="text-[13px] uppercase tracking-wide text-slate-500 mb-1">Drug Preset</div>
              <Select value={preset} onValueChange={setPreset}>
                <SelectTrigger className="h-9"><SelectValue placeholder="None" /></SelectTrigger>
                <SelectContent>
                  {Object.keys(DRUG_PRESETS).map(p => (<SelectItem key={p} value={p}>{p}</SelectItem>))}
                </SelectContent>
              </Select>
            </div>
            <div>
              <div className="text-[13px] uppercase tracking-wide text-slate-500 mb-1">Environment</div>
              <Select value={envPreset} onValueChange={setEnvPreset}>
                <SelectTrigger className="h-9"><SelectValue placeholder="None" /></SelectTrigger>
                <SelectContent>
                  {Object.keys(ENV_PRESETS).map(p => (<SelectItem key={p} value={p}>{p}</SelectItem>))}
                </SelectContent>
              </Select>
            </div>
            <div>
              <div className="text-[13px] uppercase tracking-wide text-slate-500 mb-1">Pacing (BPM)</div>
              <div className="flex items-center gap-3">
                <Slider value={[bpm]} min={20} max={220} step={1} onValueChange={([v]) => setBpm(v)} className="flex-1"/>
                <Input type="number" className="w-20 h-8" min={20} max={220} value={bpm}
                  onChange={(e) => setBpm(clamp(Number(e.target.value)||60, 20, 220))} />
              </div>
            </div>
          </div>

          <div className="flex items-center gap-3 mb-4">
            <Switch checked={showCurrents} onCheckedChange={setShowCurrents} id="currents" />
            <Label htmlFor="currents" className="text-sm text-slate-700">Show phase hints</Label>
          </div>

          {/* Phase-grouped controls */}
          {renderPhaseGroups(channelOrder, params, ko, setParams, setKo)}

          <p className="mt-3 text-xs leading-relaxed text-slate-600">
            This teaching tool illustrates qualitative trends. It is not a biophysical solver.
          </p>
        </section>

        {/* Snapshots manager */}
        <section className="lg:col-span-4">
          <div className="flex items-center justify-between mb-2">
            <div className="text-[13px] uppercase tracking-wide text-slate-500">Snapshots</div>
            <Button size="sm" variant="secondary" onClick={() => saveSnapshot({ snapshots, setSnapshots, name, cell, params, ko, preset, envPreset, curMetrics })}>Save</Button>
          </div>
          <div className="space-y-2">
            {snapshots.length === 0 && <div className="text-xs text-slate-500">No snapshots yet.</div>}
            {snapshots.map(s => (
              <div key={s.id} className="flex items-center justify-between text-sm border-b pb-1">
                <div className="truncate">
                  <div className="font-medium truncate">{s.name}</div>
                  <div className="text-xs text-slate-500">{s.cell} • {s.preset} • {s.env}</div>
                </div>
                <div className="flex items-center gap-2">
                  <input type="checkbox" checked={compareIds.includes(s.id)} onChange={(e) => toggleCompare(s.id, e.target.checked, compareIds, setCompareIds)} />
                  <Button size="xs" variant="ghost" onClick={() => loadSnapshot(s, setParams, setKo, setPreset, setEnvPreset, setCellTypeId)}>Load</Button>
                </div>
              </div>
            ))}
          </div>

          {compareIds.length === 2 && (
            <div className="mt-3 border-t pt-2">
              {renderCompareBlock(compareIds, snapshots)}
            </div>
          )}
        </section>

        {/* Chart + Metrics Column */}
        <section className="lg:col-span-4">
          <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-2 mb-2">
            <div>
              <h2 className="text-xl font-semibold tracking-tight">{name}</h2>
              <p className="text-slate-500 text-sm">Baseline vs modified</p>
            </div>
            <Tabs defaultValue="metrics" className="w-full md:w-auto">
              <TabsList className="h-9">
                <TabsTrigger value="metrics" className="text-sm">Metrics</TabsTrigger>
                <TabsTrigger value="table" className="text-sm">Table</TabsTrigger>
              </TabsList>
              <TabsContent value="metrics" className="pt-2">
                <div className="grid grid-cols-3 gap-3 text-sm">
                  <Metric label="APD90" base={baseMetrics.apd90} cur={curMetrics.apd90} unit="ms"/>
                  <Metric label="dV/dt_max" base={baseMetrics.dvdtMax} cur={curMetrics.dvdtMax} unit="mV/ms"/>
                  <Metric label="Cycle" base={baseMetrics.cycle} cur={curMetrics.cycle} unit="ms"/>
                </div>
              </TabsContent>
              <TabsContent value="table" className="pt-2">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="text-left text-slate-600">
                      <th className="font-medium py-2">Channel</th>
                      <th className="font-medium py-2">% of baseline</th>
                      <th className="font-medium py-2">KO</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-200">
                    {channelOrder.map(k => (
                      <tr key={k}>
                        <td className="py-2">{CHANNEL_LABELS[k]}</td>
                        <td className="py-2 tabular-nums">{(ko[k] ? 0 : params[k])}%</td>
                        <td className="py-2">{ko[k] ? "Yes" : "No"}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </TabsContent>
            </Tabs>
          </div>

          <div className="w-full overflow-x-auto">
            {/* Legend pills for clarity */}
            <div className="flex items-center gap-4 text-sm mb-2">
              <div className="flex items-center gap-2">
                <span className="inline-block w-8 h-[2px]" style={{ background: '#0f172a' }} /> Modified
              </div>
              <div className="flex items-center gap-2">
                <span className="inline-block w-8 h-[0] border-t border-dashed" style={{ borderColor: '#94a3b8' }} /> Baseline
              </div>
              <div className="ml-auto flex items-center gap-3">
                <Switch id="showbase" checked={showBaseline} onCheckedChange={setShowBaseline} />
                <Label htmlFor="showbase" className="text-xs text-slate-700">Show baseline</Label>
              </div>
            </div>

            <LineChart width={900} height={420} data={modified.data} margin={{ top: 8, right: 24, bottom: 20, left: 0 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis type="number" dataKey="t" domain={[0, 'dataMax']} tickCount={10}
                     label={{ value: 'time (ms)', position: 'insideBottomRight', offset: -10 }} />
              <YAxis domain={[-100, 50]} tickCount={8}
                     label={{ value: 'membrane potential (mV)', angle: -90, position: 'insideLeft' }} />
              <Tooltip formatter={(v) => `${Number(v).toFixed(1)} mV`} labelFormatter={(l) => `${Number(l).toFixed(1)} ms`} />
              {showBaseline && (
                <Line dot={false} type="monotone" dataKey="v" data={baseline.data} name="Baseline" stroke="#94a3b8" strokeWidth={2} strokeDasharray="6 4" />
              )}
              <Line dot={false} type="monotone" dataKey="v" data={modified.data} name="Modified" stroke="#0f172a" strokeWidth={3} />
              <ReferenceLine y={-85} stroke="#e5e7eb" />

              {laidOutMarks.map((m, i) => (
                <React.Fragment key={i}>
                  <ReferenceLine segment={[{ x: m.t, y: m.v }, { x: m.t, y: m.displayY }]} stroke="#cbd5e1" />
                  <ReferenceDot x={m.t} y={m.displayY} r={1} fill="#0f172a" isFront
                    label={{ value: m.label, position: 'top', offset: 6, fill: '#334155', fontSize: 12 }} />
                </React.Fragment>
              ))}

              <ReferenceDot x={modified.data[modified.data.length - 1]?.t} y={modified.data[modified.data.length - 1]?.v} r={0}
                label={{ value: 'Modified', position: 'right', offset: 8, fill: '#0f172a', fontSize: 12 }} />
              {showBaseline && (
                <ReferenceDot x={baseline.data[baseline.data.length - 1]?.t} y={baseline.data[baseline.data.length - 1]?.v} r={0}
                  label={{ value: 'Baseline', position: 'right', offset: 8, fill: '#64748b', fontSize: 12 }} />
              )}
            </LineChart>
          </div>

          {/* Sensitivity mini-panel */}
          <div className="mt-4">
            <div className="text-[13px] uppercase tracking-wide text-slate-500 mb-1">Sensitivity (±20%)</div>
            {renderSensitivity(channelOrder, cell, params, preset, envPreset, ko, bpm)}
          </div>

          {showCurrents && (
            <div className="grid grid-cols-2 md:grid-cols-4 gap-3 text-xs text-slate-600 mt-3">
              <PhaseHint label="Phase 0" bullets={["Upstroke", cell.id === 'sa' ? 'ICaL-driven' : 'INa-driven']} />
              {cell.id !== 'sa' && <PhaseHint label="Phase 1" bullets={["Notch", "Ito on, INa inactivates"]} />}
              {cell.id !== 'sa' && <PhaseHint label="Phase 2" bullets={["Plateau", "ICaL ↔ IKr/IKs balance"]} />}
              <PhaseHint label="Phase 3" bullets={["Repolarization", "IKr/IKs dominate"]} />
              <PhaseHint label="Phase 4" bullets={[cell.id === 'sa' ? 'Diastolic depolarization (If, ICaT)' : 'Rest (IK1, pump)']} />
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

// ---- helpers for presets, snapshots, groups, sensitivity ----
function saveSnapshot({ snapshots, setSnapshots, name, cell, params, ko, preset, envPreset, curMetrics }) {
  const id = Math.random().toString(36).slice(2, 8);
  setSnapshots([{ id, name: `${name} (${new Date().toLocaleTimeString()})`, cell: cell.name, preset, env: envPreset, params: { ...params }, ko: { ...ko }, metrics: curMetrics }, ...snapshots].slice(0, 12));
}

function loadSnapshot(s, setParams, setKo, setPreset, setEnvPreset, setCellTypeId) {
  setParams(s.params); setKo(s.ko); setPreset(s.preset); setEnvPreset(s.env === undefined ? 'None' : s.env);
  const id = (CELL_TYPES.find(c => c.name === s.cell) || CELL_TYPES[0]).id; setCellTypeId(id);
}

function toggleCompare(id, checked, compareIds, setCompareIds) {
  const set = new Set(compareIds); if (checked) set.add(id); else set.delete(id);
  const arr = Array.from(set).slice(0, 2); setCompareIds(arr);
}

function renderCompareBlock(ids, snapshots) {
  const [a, b] = ids.map(id => snapshots.find(s => s.id === id));
  if (!a || !b) return null;
  const rows = [
    { k: 'APD90 (ms)', va: a.metrics.apd90, vb: b.metrics.apd90 },
    { k: 'dV/dt_max (mV/ms)', va: a.metrics.dvdtMax, vb: b.metrics.dvdtMax },
    { k: 'Cycle (ms)', va: a.metrics.cycle, vb: b.metrics.cycle },
  ];
  return (
    <div>
      <div className="text-sm font-medium mb-1">Compare: {a.name} ↔ {b.name}</div>
      <table className="w-full text-xs">
        <thead>
          <tr className="text-left text-slate-600">
            <th className="font-medium py-1">Metric</th><th className="font-medium py-1">A</th><th className="font-medium py-1">B</th><th className="font-medium py-1">Δ (B−A)</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-200">
          {rows.map((r,i)=> (
            <tr key={i}><td className="py-1">{r.k}</td><td className="py-1 tabular-nums">{r.va}</td><td className="py-1 tabular-nums">{r.vb}</td><td className="py-1 tabular-nums">{Math.round((r.vb - r.va)*100)/100}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const PHASE_GROUPS = [
  { phase: 0, label: 'Phase 0 (Upstroke)', keys: ['INa','ICaL'] },
  { phase: 1, label: 'Phase 1 (Notch)', keys: ['Ito'] },
  { phase: 2, label: 'Phase 2 (Plateau)', keys: ['ICaL','IKr','IKs'] },
  { phase: 3, label: 'Phase 3 (Repolarization)', keys: ['IKr','IKs'] },
  { phase: 4, label: 'Phase 4 (Rest/Diastolic)', keys: ['IK1','If','ICaT','IK_ACh','NaKATPase'] },
];

function renderPhaseGroups(channelOrder, params, ko, setParams, setKo) {
  const used = new Set(channelOrder);
  return (
    <div className="border-y divide-y">
      {PHASE_GROUPS.map(g => {
        const keys = g.keys.filter(k => used.has(k)); if (!keys.length) return null;
        return (
          <details key={g.phase} open>
            <summary className="py-2 text-sm font-medium cursor-pointer select-none">{g.label}</summary>
            <div className="pb-2">
              {keys.map(key => (
                <div key={key} className="py-2">
                  <div className="flex items-center justify-between mb-1">
                    <Label className="font-medium text-sm">{CHANNEL_LABELS[key]}</Label>
                    <div className="flex items-center gap-2 text-xs text-slate-600">
                      <Label htmlFor={`ko-${key}`}>KO</Label>
                      <Switch id={`ko-${key}`} checked={!!ko[key]} onCheckedChange={(v) => setKo({ ...ko, [key]: v })} />
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <Slider value={[Math.min(200, Math.max(0, Number(params[key] || 0)))]} min={0} max={200} step={5}
                      onValueChange={([v]) => setParams({ ...params, [key]: v })} className="flex-1"/>
                    <Input type="number" inputMode="numeric" min={0} max={200} step={5} className="w-20 h-8"
                      value={ko[key] ? 0 : params[key]}
                      onChange={(e) => { const v = Math.max(0, Math.min(200, Number(e.target.value) || 0)); setParams({ ...params, [key]: v }); }} />
                  </div>
                </div>
              ))}
            </div>
          </details>
        );
      })}
    </div>
  );
}

function renderSensitivity(channelOrder, cell, params, preset, envPreset, ko, bpm) {
  const used = channelOrder;
  const entries = used.map(k => {
    const baseP = { ...params };
    const env = applyPreset(baseP, ENV_PRESETS[envPreset] || {});
    const drug = applyPreset(env, DRUG_PRESETS[preset] || {});
    const common = { ...drug };
    Object.keys(ko).forEach(x => { if (ko[x]) common[x] = 0; });
    common.__targetCycle = 60000 / bpm;

    const mod = (scale) => {
      const p = { ...common, [k]: clamp((common[k] ?? 100) * scale, 0, 200) };
      const m = computeMetrics(generateAP(cell.id, p));
      return m;
    };

    const m0 = computeMetrics(generateAP(cell.id, common));
    const mUp = mod(1.2), mDn = mod(0.8);
    return { k, up: mUp.apd90 - m0.apd90, dn: mDn.apd90 - m0.apd90, dv: mUp.dvdtMax - m0.dvdtMax };
  });

  return (
    <div className="space-y-1">
      {entries.map(e => (
        <div key={e.k} className="flex items-center gap-3 text-xs">
          <div className="w-40 truncate">{CHANNEL_LABELS[e.k]}</div>
          <div className="flex-1 h-2 bg-slate-100 relative overflow-hidden">
            <div className="absolute left-1/2 top-0 bottom-0 w-px bg-slate-300" />
            {/* left (−20%) */}
            <div style={{ width: `${Math.min(100, Math.abs(e.dn))}%` }} className={`h-full ${e.dn<0? 'bg-emerald-600':'bg-rose-600'}`} />
            {/* right (+20%) */}
            <div style={{ width: `${Math.min(100, Math.abs(e.up))}%`, marginLeft: '50%' }} className={`h-full ${e.up>0? 'bg-emerald-600':'bg-rose-600'}`} />
          </div>
          <div className="w-28 tabular-nums text-right">ΔAPD: −20% {Math.round(e.dn)} / +20% {Math.round(e.up)} ms</div>
        </div>
      ))}
    </div>
  );
}

// label layout
function layoutPhaseMarks(marks) {
  if (!marks || !marks.length) return [];
  const sorted = [...marks].sort((a, b) => a.t - b.t);
  const minGap = 25; // ms separation before bumping
  const baseStem = 18; // mV vertical separation in axis units
  const extra = 12; // additional per level
  const yMin = -95; const yMax = 45;
  let lastT = -Infinity; let level = 0;
  return sorted.map((m) => {
    if (m.t - lastT < minGap) level = (level + 1) % 3; else level = 0;
    lastT = m.t;
    const desired = m.v - (baseStem + level * extra);
    const displayY = clamp(desired, yMin, yMax);
    const stem = m.v - displayY;
    return { ...m, displayY, stem };
  });
}

function Metric({ label, base, cur, unit }) {
  const delta = cur - base; const up = delta > 0;
  const cls = delta === 0 ? 'text-slate-500' : up ? 'text-emerald-700' : 'text-rose-700';
  const arrow = delta === 0 ? '→' : up ? '↑' : '↓';
  return (
    <div>
      <div className="text-slate-600 text-xs">{label}</div>
      <div className="text-base font-semibold tabular-nums">{cur} {unit}</div>
      <div className={`text-xs tabular-nums ${cls}`}>{arrow} {Math.abs(delta)} {unit} <span className="text-slate-500">vs baseline</span></div>
    </div>
  );
}

function PhaseHint({ label, bullets }) {
  return (
    <div>
      <div className="font-medium text-sm mb-1">{label}</div>
      <ul className="list-disc ml-4 leading-relaxed">
        {bullets.map((b, i) => <li key={i}>{b}</li>)}
      </ul>
    </div>
  );
}

// ------------------------------ Minimal Unit Tests ------------------------------
function runUnitTests() {
  const results = [];
  const v = generateAP('ventricular', BASELINE_PARAMS);
  results.push({ name: 'ventricular phases', pass: v.segs.length === 5 && v.marks.length === 5 });
  const sa = generateAP('sa', BASELINE_PARAMS);
  results.push({ name: 'sa-node phases', pass: sa.segs.length === 3 && sa.marks.length === 3 });
  const inc = v.data.every((p, i, arr) => i === 0 || p.t >= arr[i-1].t);
  results.push({ name: 'time monotonic', pass: inc });
  const mV = computeMetrics(v);
  results.push({ name: 'APD90 positive', pass: mV.apd90 > 0 });
  const lowNa = generateAP('ventricular', { ...BASELINE_PARAMS, INa: 10 });
  const mLowNa = computeMetrics(lowNa);
  results.push({ name: 'INa↓ reduces dV/dt_max', pass: mLowNa.dvdtMax < mV.dvdtMax });
  const hiIKr = generateAP('ventricular', { ...BASELINE_PARAMS, IKr: 200 });
  results.push({ name: 'IKr↑ shortens APD', pass: computeMetrics(hiIKr).apd90 < mV.apd90 });
  const hiICa = generateAP('ventricular', { ...BASELINE_PARAMS, ICaL: 200 });
  results.push({ name: 'ICaL↑ lengthens APD', pass: computeMetrics(hiICa).apd90 > mV.apd90 });
  console.log('[IonChannelAP Playground] Test Results:', results);
  return results;
}

if (typeof window !== 'undefined' && window.__RUN_AP_TESTS__) {
  runUnitTests();
}

export { runUnitTests };
