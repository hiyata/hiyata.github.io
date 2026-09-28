"""Fifth cue pass over the original questions.

Removes two cues the build did not previously check for:
  - punctuation cues: parentheses, semicolons, or colons appearing only in the key,
    which mark it as the option carrying the extra detail;
  - keys that are conspicuously shorter than every distractor.
Keys are the question `topic`; `c` replaces the correct option, `o` rewords distractors.
"""
R = {
# ---------------- parentheses only in the key ----------------
"B. anthracis: cutaneous anthrax": dict(
  c="A capsule made of poly-D-glutamic acid",
  o={"A lipooligosaccharide outer membrane": "A lipooligosaccharide-rich outer membrane",
     "A hyaluronic acid capsule": "A capsule made of hyaluronic acid",
     "Mycolic acid in the cell wall": "Mycolic acid within the cell wall"}),

"C. perfringens: gas gangrene": dict(
  c="Alpha-toxin, a lecithinase acting on membranes",
  o={"Toxin B, a glucosyltransferase": "Toxin B, a glucosyltransferase acting on Rho proteins"}),

"C. difficile: treatment": dict(
  c="Oral fidaxomicin or oral vancomycin",
  o={"IV ceftriaxone": "Intravenous ceftriaxone",
     "Loperamide": "Loperamide alone",
     "IV vancomycin": "Intravenous vancomycin"}),

"Y. pestis: morphology": dict(
  c="Bipolar safety-pin staining of Gram-negative rods",
  o={"Spirochetes between red cells": "Loose spirochetes lying between red cells",
     "Acid-fast beaded rods": "Beaded rods that are acid-fast"}),

"Syphilis: primary chancre": dict(
  c="Dark-field microscopy of the lesion exudate",
  o={"Nontreponemal serology alone, which is always positive": "Nontreponemal serology alone, which is reliably positive here",
     "Tzanck smear": "A Tzanck smear of the base",
     "Gram stain of the exudate": "Gram stain of exudate from the ulcer"}),

"TB drugs: isoniazid": dict(
  c="Isoniazid; give supplemental pyridoxine",
  o={"Pyrazinamide; give allopurinol": "Pyrazinamide; give allopurinol as well"}),

"Viral envelope & transmission": dict(
  c="It lacks a lipid envelope around the capsid",
  o={"It has a segmented genome": "It has a segmented RNA genome",
     "It has a helical nucleocapsid": "It has a helical nucleocapsid core",
     "It buds from the plasma membrane": "It buds through the host plasma membrane"}),

"Measles: complications": dict(
  c="Pneumonia; subacute sclerosing panencephalitis",
  o={"Orchitis; sterility": "Orchitis; subsequent infertility",
     "Hepatitis; Reye syndrome": "Hepatitis; Reye syndrome after aspirin"}),

"Candida: immune defense": dict(
  c="T cells, especially Th17 responses",
  o={"Complement C5": "Terminal complement C5 through C9",
     "Splenic macrophages": "Macrophages of the splenic red pulp"}),

"P. vivax: hypnozoites": dict(
  c="Primaquine or tafenoquine; G6PD testing",
  o={"Artesunate; ECG": "Artesunate; an ECG before dosing",
     "Doxycycline; pregnancy test": "Doxycycline; a pregnancy test first"}),

"Malaria: host protective factors": dict(
  c="Sickle cell trait",
  o={"Blood group O deficiency": "Blood group AB phenotype",
     "Duffy antigen positivity": "Duffy antigen positive red cells"}),

"Ascaris": dict(
  c="Larvae migrating through the lungs",
  o={"Cysts forming in the lung parenchyma": "Cysts forming within the lung parenchyma"}),

"N. meningitidis: epidemiology": dict(
  c="The quadrivalent conjugate meningococcal vaccine",
  o={"The BCG vaccine": "The BCG vaccine before departure"}),

# ---------------- semicolons or colons only in the key ----------------
"Chlamydia: life cycle": dict(
  c="Elementary bodies enter cells and reticulate bodies divide",
  o={"It makes its own ATP and needs no host cell": "It makes its own ATP and does not need a host cell"}),

"Tetracyclines": dict(
  c="Avoid milk, antacids, and iron, and use sun protection"),

"Transduction": dict(
  c="Generalized moves any gene, specialized only flanking genes",
  o={"There is no meaningful difference between them": "There is no meaningful difference between the two"}),

"Positive vs negative sense RNA": dict(
  c="Positive-sense RNA is read directly, negative-sense is not",
  o={"Positive-sense viruses always have envelopes": "Positive-sense RNA viruses always carry an envelope",
     "Negative-sense genomes are single-stranded DNA": "Negative-sense genomes are made of single-stranded DNA",
     "Positive-sense genomes all require a reverse transcriptase": "Positive-sense genomes need a reverse transcriptase"}),

"HDV": dict(
  c="A defective RNA virus needing HBsAg, severe in superinfection",
  o={"It is spread mainly by the fecal-oral route": "It is spread mainly by the fecal-oral route in water",
     "The HBV vaccine does not protect against it": "The hepatitis B vaccine gives no protection against it"}),

"Cryptosporidium": dict(
  c="Chlorine-resistant oocysts, with ART the key treatment in AIDS",
  o={"It invades the liver and forms abscesses": "It invades the liver and forms abscesses there"}),

"S. epidermidis: contaminant vs true infection": dict(
  c="Most likely a skin contaminant needing no therapy"),

"Shigella: treatment & complications": dict(
  c="Antibiotics help, and seizures, arthritis, and HUS may follow",
  o={"Shigella has a very high infectious dose": "Shigella requires a very high infectious dose"}),

"Lyme: serologic testing": dict(
  c="Two-tier serology, a screening EIA then an immunoblot",
  o={"Blood culture on routine media": "Blood culture on routine bacteriologic media"}),

# ---------------- key conspicuously shorter than every distractor ----------------
"Salmonella: non-typhoidal": dict(
  c="Oral rehydration without antibiotics",
  o={"Cholecystectomy to prevent chronic gallbladder carriage": "Cholecystectomy to prevent gallbladder carriage"}),

"Atypical pneumonia: organism features": dict(
  c="Growth only inside living host cells",
  o={"Absence of a cell wall, with sterols in the membrane": "Absence of a cell wall, with membrane sterols"}),

"Pneumonia by host": dict(
  c="Cystic fibrosis — Pseudomonas aeruginosa in an adolescent",
  o={"Healthy college student with walking pneumonia — Klebsiella": "Healthy college student with walking pneumonia — Klebsiella"}),

"Chlamydia screening": dict(
  c="A sexually active woman who is 21 years old",
  o={"A sexually active 40-year-old woman in a monogamous relationship": "A sexually active 40-year-old woman with one partner"}),
}
