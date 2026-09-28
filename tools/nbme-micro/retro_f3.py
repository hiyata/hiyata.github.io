"""Third figure pass: images for the n08-n15 questions and newly fetched diagrams.

`img` puts a picture beside the question stem (the student sees it while answering);
`fig` puts a teaching figure in the explanation, with `steps` walking through it.
Every file here is listed in credits.json, so its licence and author print under the image.
"""
from qcore import F

R = {
# ---------------- laboratory identification, shown with the stem ----------------
"S. aureus: mannitol salt agar": dict(
  img="msa-agar.jpg",
  fig=F("msa-agar.jpg",
        "Mannitol salt agar. The yellow colonies and surrounding yellow medium are S. aureus, which ferments mannitol and acidifies the phenol red indicator; the pink colonies are coagulase-negative staphylococci, which grow in the salt but leave the medium red."),
  steps=["7.5% sodium chloride makes the medium selective: almost nothing but staphylococci grows.",
         "Mannitol plus phenol red makes it differential.",
         "S. aureus ferments mannitol, producing acid, so the indicator turns yellow.",
         "S. epidermidis and S. saprophyticus grow but do not ferment mannitol, so their colonies stay pink-red.",
         "This is why a nasal carriage swab is plated here: yellow on yellow means S. aureus."]),

"S. aureus: coagulase & clumping factor": dict(
  img="coagulase.jpg",
  fig=F("coagulase.jpg",
        "Tube coagulase test. The tube on the left has set into a solid clot (positive, S. aureus); the tube on the right remains liquid and runs when tilted (negative, a coagulase-negative staphylococcus).")),

"S. pyogenes: PYR and bacitracin": dict(
  img="beta-hemolysis.jpg",
  fig=F("hemolysis-types.jpg",
        "The three hemolysis patterns on blood agar: alpha (partial, green discoloration), beta (complete clearing), and gamma (no change)."),
  steps=["Read hemolysis first: complete clearing around the colony is beta-hemolysis.",
         "Beta-hemolytic and catalase-negative puts you in groups A and B.",
         "Group A (S. pyogenes) is bacitracin-sensitive and PYR-positive.",
         "Group B (S. agalactiae) is bacitracin-resistant, CAMP-positive, and hippurate-positive.",
         "Alpha-hemolysis instead sends you to pneumococcus (optochin-sensitive, bile-soluble) versus viridans (resistant, insoluble)."]),

"S. agalactiae: CAMP test": dict(
  img="camp-test.jpg",
  fig=F("camp-test.jpg",
        "Positive CAMP test. Group B streptococcus is streaked perpendicular to a central streak of S. aureus; where the two hemolysins overlap, an arrowhead of enhanced clearing points at the staphylococcal streak.")),

"S. pneumoniae: bile solubility and optochin": dict(
  img="optochin.jpg",
  fig=[F("optochin.jpg", "Optochin disk test. A wide zone of inhibition around the P disk identifies S. pneumoniae; viridans streptococci grow up to the disk edge."),
       F("alpha-hemolysis.jpg", "Alpha-hemolysis: the partial, greenish discoloration produced when hydrogen peroxide oxidizes hemoglobin around the colonies.")],
  steps=["Alpha-hemolysis narrows it to pneumococcus and the viridans group.",
         "Pneumococcus is optochin-sensitive; viridans strep is optochin-resistant.",
         "Pneumococcus is bile-soluble: deoxycholate activates its autolysin and the colonies dissolve.",
         "Viridans strep is bile-insoluble.",
         "Mnemonic: OVRPS - Optochin, Viridans Resistant, Pneumococcus Sensitive."]),

"Candida: germ tube test": dict(
  img="germ-tube.jpg",
  fig=F("germ-tube.jpg",
        "Positive germ tube test: true germ tubes extend from the yeast cells with no constriction at their point of origin, identifying Candida albicans."),
  steps=["Incubate the yeast in serum at 37°C for two to three hours.",
         "C. albicans extends a true germ tube: a parallel-sided filament with no pinch where it meets the mother cell.",
         "A pseudohypha, by contrast, is constricted at its base - that is not a germ tube.",
         "Germ tube positive means C. albicans (or the rarer C. dubliniensis).",
         "This matters clinically: germ tube-negative species such as C. glabrata and C. krusei are frequently fluconazole-resistant."]),

"Enterics: lactose fermentation logic": dict(
  img="macconkey.jpg",
  fig=F("macconkey.jpg",
        "MacConkey agar. The pink colonies are lactose fermenters, which produce acid that precipitates the bile salts and turns the neutral red indicator; the pale colorless colonies are non-fermenters."),
  steps=["Bile salts and crystal violet make MacConkey selective for Gram-negative rods.",
         "Lactose plus neutral red makes it differential.",
         "Fermenters (E. coli, Klebsiella, Enterobacter, Citrobacter, Serratia slowly) acidify the medium and go pink.",
         "Non-fermenters (Salmonella, Shigella, Proteus, Yersinia, Pseudomonas) stay colorless.",
         "So a colorless colony from a stool culture is the one worth chasing for Salmonella or Shigella."]),

"Listeria: tumbling motility and cold growth": dict(
  img="listeria-gram.jpg",
  fig=F("listeria-gram.jpg", "Gram stain of Listeria monocytogenes: short Gram-positive rods, easily mistaken for diphtheroids or even for cocci in a hurried read.")),

"Pertussis: toxin actions": dict(
  img="bpertussis.jpg",
  fig=F("bpertussis.jpg", "Bordetella pertussis, a small Gram-negative coccobacillus. It needs Bordet-Gengou or Regan-Lowe charcoal medium to grow.")),

"Legionella: staining and culture": dict(
  img="legionella.jpg",
  fig=F("legionella.jpg", "Legionella pneumophila. The organism stains poorly with the standard Gram method because of its branched-chain fatty acids, so a sputum smear shows neutrophils with no visible organisms.")),

"TB: acid-fast alternatives": dict(
  img="afb-smear.jpg",
  fig=F("afb-smear.jpg",
        "Acid-fast smear of sputum: slender red beaded bacilli against the blue counterstain. Mycolic acids in the wall retain carbol fuchsin through acid-alcohol decolorization.")),

"Trachoma: mechanism of blindness": dict(
  img="trachoma.jpg",
  fig=F("trachoma.jpg", "Trachomatous trichiasis: conjunctival scarring has turned the lid margin and lashes inward so that they sweep the cornea with every blink.")),

"N. meningitidis: carriage to invasion": dict(
  img="nmen-gram.jpg",
  fig=F("nmen-gram.jpg", "Gram stain of cerebrospinal fluid in meningococcal meningitis: Gram-negative diplococci, many of them inside neutrophils.")),

"Shigella: toxin and complication": dict(
  img="shigella-stool.jpg"),

"Cryptococcus: capsule and India ink": dict(
  img="crypto-ink.jpg",
  fig=[F("crypto-ink.jpg", "India ink preparation of CSF: the ink particles cannot penetrate the polysaccharide capsule, so each yeast sits in a clear halo."),
       F("crypto-mucicarmine.jpg", "Mucicarmine stain of tissue, which colors the cryptococcal capsule red.")],
  steps=["The capsule of glucuronoxylomannan is the main virulence factor: it blocks phagocytosis and complement.",
         "India ink shows it as a negative image - a clear halo the ink cannot enter.",
         "That same capsular polysaccharide is what the cryptococcal antigen (CrAg) test detects, in serum or CSF.",
         "CrAg is far more sensitive than India ink and is the test actually used now.",
         "Capsular material shed into CSF also raises the opening pressure, which is what kills these patients, hence the serial lumbar punctures."]),

"Pneumocystis: diagnosis and steroid indication": dict(
  img="pcp-gms.jpg",
  fig=F("pcp-gms.jpg",
        "Methenamine silver stain showing the crushed ping-pong ball cysts of Pneumocystis jirovecii in alveolar exudate. The organism cannot be cultured, so diagnosis rests on staining induced sputum or lavage fluid, or on PCR.")),

"Aspergillus: three syndromes by host": dict(
  img="halo-sign.jpg",
  fig=F("halo-sign.jpg",
        "CT halo sign: a pulmonary nodule surrounded by a rim of ground-glass attenuation. The nodule is infarcted lung and the halo is hemorrhage around it, produced when Aspergillus invades and occludes a vessel.")),

"HPV: koilocytes": dict(
  img="koilocytes.jpg",
  fig=F("koilocytes.jpg",
        "Koilocytes on cervical cytology: squamous cells with a large clear perinuclear halo and a wrinkled, hyperchromatic nucleus - the cytopathic signature of productive HPV infection.")),

"Rotavirus: mechanism and vaccine caution": dict(
  img="rotavirus-em.jpg",
  fig=F("rotavirus-em.jpg", "Rotavirus particles on electron microscopy. The double-shelled capsid gives the wheel-like outline that named the virus.")),

"Trichinella: muscle and clinical clue": dict(
  img="trichinella-muscle.jpg",
  fig=F("trichinella-muscle.jpg",
        "Trichinella spiralis larvae coiled inside skeletal muscle fibers, each within a nurse cell. Biopsy of a tender muscle is diagnostic, though serology is usually used first.")),

"Filariasis: Wolbachia and doxycycline": dict(
  img="wuchereria.jpg",
  fig=F("wuchereria.jpg",
        "Sheathed microfilaria of Wuchereria bancrofti on a Giemsa-stained blood film. Blood is drawn at night because the microfilariae are nocturnally periodic, matching the biting habit of the mosquito vector.")),

"Liver flukes and cholangiocarcinoma": dict(
  img="clonorchis-egg.jpg",
  fig=[F("clonorchis-egg.jpg", "Operculated egg of Clonorchis sinensis in stool, with the characteristic shoulders at the operculum and a small knob at the opposite end."),
       F("fig-clonorchis-cycle.jpg", "Life cycle: eggs in water are eaten by snails, cercariae encyst in freshwater fish, and humans are infected by eating that fish raw or undercooked. Adults then live in the bile ducts.")],
  steps=["Humans eat raw or undercooked freshwater fish carrying metacercariae.",
         "The larvae excyst in the duodenum and ascend the biliary tree.",
         "Adult flukes live for years in the bile ducts, causing chronic inflammation and periductal fibrosis.",
         "Repeated injury and repair drives biliary epithelial proliferation.",
         "The end result in a subset of patients is cholangiocarcinoma, which is why this is a WHO group 1 carcinogen.",
         "Praziquantel kills the flukes but does not reverse established malignancy, so prevention is what matters."]),

"Toxoplasma: ring lesions vs lymphoma": dict(
  fig=F("toxo-cyst.jpg",
        "A Toxoplasma gondii tissue cyst packed with bradyzoites. Cysts persist for life in brain and muscle; reactivation follows when CD4 counts fall.")),

"African trypanosomiasis: stage determines drug": dict(
  img="tbrucei.jpg",
  fig=F("tbrucei.jpg", "Trypomastigotes of Trypanosoma among red cells on a stained blood film, showing the undulating membrane and free flagellum.")),

"Necrotizing fasciitis: clinical clue": dict(
  img="necrotizing-fasciitis.jpg",
  fig=F("necrotizing-fasciitis.jpg",
        "Necrotizing fasciitis of the leg. Note how modest the skin changes are compared with the patient's pain and toxicity: the infection is tracking along fascia beneath skin that still looks almost viable.")),

"Actinomyces: sulfur granules": dict(
  img="actino-histo.jpg",
  fig=F("actino-histo.jpg",
        "Histology of actinomycosis: a colony of filamentous organisms - the sulfur granule - ringed by dense neutrophils. The granule is bacterial, not mineral; the name comes only from its yellow color.")),

"Viridans strep: dextran and valve adherence": dict(
  img="osler-nodes.jpg",
  fig=F("osler-nodes.jpg",
        "Osler nodes: tender violaceous nodules on the finger pads in infective endocarditis. Mnemonic: Osler nodes are Ouchy; Janeway lesions are painless.")),

"Hookworm: anemia mechanism": dict(
  img="larva-migrans.jpg",
  fig=[F("larva-migrans.jpg", "Cutaneous larva migrans - the serpiginous track of an animal hookworm larva that can penetrate skin but cannot complete its cycle in humans."),
       F("fig-hookworm-cycle.jpg", "Human hookworm cycle: filariform larvae in soil penetrate skin, travel through lungs, are swallowed, and attach in the small intestine.")],
  steps=["Filariform larvae in warm moist soil penetrate the skin of a bare foot.",
         "They enter the circulation, reach the lungs, break into alveoli, and are coughed up and swallowed.",
         "Adults attach to small bowel mucosa with cutting plates or teeth and feed on blood.",
         "Each worm takes a small but continuous volume of blood, and heavy burdens persist for years.",
         "The result is iron deficiency anemia with eosinophilia - treat with albendazole plus iron replacement."]),

"Dermatophytes vs Malassezia": dict(
  img="malassezia.jpg",
  fig=[F("malassezia.jpg", "KOH preparation in tinea versicolor: short curved hyphae among clusters of round yeast, the 'spaghetti and meatballs' appearance."),
       F("onychomycosis.jpg", "Onychomycosis for contrast - a dermatophyte infection of the nail, which needs systemic terbinafine or itraconazole rather than a topical agent.")]),

"Syphilis: congenital": dict(
  img="congenital-syphilis.jpg"),

"Ebola": dict(
  img="ebola-em.jpg",
  fig=F("ebola-em.jpg", "Ebola virion on electron microscopy: the filamentous, sometimes shepherd's-crook shaped particle that gives the filoviruses their name.")),
}
