"""Sixth cue pass: stem-echo fixes for the original questions.

Each entry rewords the correct answer (and, once, a distractor) so it no longer
shares a distinctive word with the stem that no other option uses - the kind
of clang-association shortcut that lets a test taker answer without reading.
Keys are the question `topic`; `c` replaces the correct option, `o` rewords a
distractor by its unique prefix, `why` (supplied in full, since a later pass
replaces rather than merges it) documents why each distractor is wrong.

Every replacement below was cross-checked against the full stem text, not just
the flagged word, since a rewording can trade one echo for another.
"""
R = {
"S. aureus: osteomyelitis": dict(
  c="S. aureus, using MSCRAMM adhesins for collagen and fibronectin"),

"Enterococcus: treatment & synergy": dict(
  c="The cell wall agent lets aminoglycosides enter the cell"),

"B. anthracis: toxins": dict(
  c="It is a calmodulin-dependent adenylyl cyclase producing uncontrolled cAMP"),

"C. botulinum vs other paralyses": dict(
  c="Paralysis progressing downward, sensation preserved"),

"E. coli: UTI & culture": dict(
  c="P fimbriae binding Gal-Gal on urinary epithelium"),

"H. pylori: virulence & disease": dict(
  c="Urease, which raises local pH by releasing ammonia"),

"H. pylori: MALT lymphoma": dict(
  c="Eradication of the causative organism"),

"Syphilis: primary chancre": dict(
  c="Dark-field microscopy of exudate from the ulcer"),

"Daptomycin": dict(
  c="It is inactivated by surfactant in the lungs; monitor CPK for myopathy"),

"Antibiotic prophylaxis: HIV": dict(
  o={"Valganciclovir": "Pyrimethamine alone to prevent Toxoplasma reactivation"},
  why={"Azithromycin to prevent MAC": "MAC prophylaxis is considered below 50 and is often unnecessary once ART starts.",
       "Fluconazole to prevent Cryptococcus": "Primary antifungal prophylaxis is not routine.",
       "Pyrimethamine alone to prevent Toxoplasma": "Pyrimethamine is never used without sulfadiazine and leucovorin.",
       "Isoniazid to prevent TB regardless of TST": "Isoniazid is given only for latent infection confirmed by testing."}),

"JC virus: PML": dict(
  c="JC virus reactivation causing demyelination"),

"HBV serology: window period": dict(
  c="Window period of hepatitis B"),

"HBV: histology": dict(
  c="Ground-glass hepatocellular inclusions packed with HBsAg"),

"HDV": dict(
  c="A defective RNA virus needing HBsAg, worse when it strikes a carrier"),

"Cryptosporidium": dict(
  c="Chlorine resistance in water, with ART the key treatment in AIDS"),

"Toxoplasma: congenital": dict(
  c="Avoid cat litter and thoroughly cook all meat"),

"Malaria: life cycle": dict(
  c="Sporozoites, which travel to the liver"),

"Malaria: host protective factors": dict(
  c="One copy of the sickle hemoglobin gene"),

"Echinococcus": dict(
  c="Spillage of the fluid can cause anaphylaxis and disseminate the parasite"),

"Actinomyces: pelvic infection": dict(
  c="Actinomyces israelii; commensal mucosal and gut flora"),

"N. meningitidis: epidemiology": dict(
  c="A conjugate vaccine covering four serogroups"),

"Salmonella Typhi: carriers & vaccines": dict(
  c="The gallbladder; prevention uses both an oral and an injectable vaccine"),

"Anaplasma": dict(
  c="Ixodes scapularis, the same vector as Lyme disease and Babesia"),
}
