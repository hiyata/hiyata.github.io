"""Reusable comparison tables for explanations."""
from qcore import T

# ---------------- Bacteria: Gram-positive ----------------
STAPH = T("Staphylococci compared",
  ["Species", "Coagulase", "Novobiocin", "Key features", "Classic diseases"],
  [["S. aureus", "+", "Sensitive", "Protein A, TSST-1, PVL, exfoliatins, enterotoxins; yellow colonies; ferments mannitol", "Abscesses, osteomyelitis, acute endocarditis (IVDU), post-flu pneumonia, TSS, SSSS, food poisoning"],
   ["S. epidermidis", "−", "Sensitive", "Biofilm on plastic; skin flora; common contaminant", "Prosthetic device, catheter, and shunt infections"],
   ["S. saprophyticus", "−", "Resistant", "Urease +; adheres to uroepithelium", "Cystitis in young sexually active women"]])

STREP = T("Catalase-negative Gram-positive cocci",
  ["Organism", "Hemolysis", "Key test", "Classic diseases"],
  [["S. pyogenes (GAS)", "β", "Bacitracin S, PYR +", "Pharyngitis, impetigo, erysipelas, necrotizing fasciitis, scarlet fever; ARF, PSGN"],
   ["S. agalactiae (GBS)", "β", "Bacitracin R, CAMP +, hippurate +", "Neonatal sepsis, pneumonia, meningitis"],
   ["S. pneumoniae", "α", "Optochin S, bile soluble, quellung +", "Pneumonia, otitis media, sinusitis, meningitis"],
   ["Viridans strep", "α", "Optochin R, bile insoluble", "Dental caries (S. mutans), subacute endocarditis"],
   ["Enterococcus", "γ (usually)", "Grows in 6.5% NaCl, bile esculin +, PYR +", "UTI, biliary infection, endocarditis after GU/GI procedures"],
   ["S. gallolyticus", "γ", "Bile esculin +, no growth in 6.5% NaCl", "Endocarditis linked to colon cancer"]])

GPC_ALGORITHM = T("Gram-positive cocci: first branch points",
  ["Test", "Positive", "Negative"],
  [["Catalase", "Staphylococcus (and Micrococcus)", "Streptococcus, Enterococcus"],
   ["Coagulase (staph)", "S. aureus", "S. epidermidis, S. saprophyticus"],
   ["Novobiocin (CoNS)", "Sensitive: S. epidermidis", "Resistant: S. saprophyticus"],
   ["Optochin (α-hemolytic)", "Sensitive: S. pneumoniae", "Resistant: viridans strep"],
   ["Bacitracin (β-hemolytic)", "Sensitive: GAS", "Resistant: GBS"]])

GAS_SEQUELAE = T("Post-streptococcal sequelae",
  ["Feature", "Acute rheumatic fever", "Post-streptococcal GN"],
  [["Preceding infection", "Pharyngitis only", "Pharyngitis or skin (impetigo)"],
   ["Mechanism", "Type II: anti-M protein cross-reacts with myosin (molecular mimicry)", "Type III: immune complexes"],
   ["Prevented by antibiotics?", "Yes (treat within ~9 days)", "No"],
   ["Findings", "Carditis, migratory polyarthritis, chorea, nodules, erythema marginatum", "Cola urine, edema, hypertension, low C3"],
   ["Labs", "ASO or anti-DNase B, ESR", "Low C3; subepithelial humps"]])

CLOSTRIDIA = T("Clostridia compared (anaerobic, spore-forming Gram-positive rods)",
  ["Species", "Toxin and mechanism", "Disease", "Treatment / prevention"],
  [["C. tetani", "Tetanospasmin cleaves synaptobrevin in inhibitory interneurons (↓ glycine, GABA)", "Spastic paralysis, trismus, opisthotonus", "TIG + toxoid, metronidazole, benzodiazepines"],
   ["C. botulinum", "Botulinum toxin cleaves SNAREs at NMJ (↓ ACh)", "Descending flaccid paralysis; infant (honey), food, wound", "Antitoxin (BabyBIG in infants)"],
   ["C. perfringens", "α-toxin = phospholipase C (lecithinase)", "Gas gangrene; late-onset food poisoning", "Debridement + penicillin + clindamycin"],
   ["C. difficile", "Toxins A and B glucosylate Rho GTPases", "Pseudomembranous colitis after antibiotics", "Oral fidaxomicin or vancomycin; FMT for recurrence"]])

GPR = T("Other Gram-positive rods and branching organisms",
  ["Organism", "Key features", "Disease", "Treatment"],
  [["Corynebacterium diphtheriae", "Club-shaped, metachromatic granules; phage-encoded toxin (EF-2)", "Pseudomembranous pharyngitis, myocarditis", "Antitoxin + erythromycin/penicillin"],
   ["Listeria monocytogenes", "Tumbling motility, cold growth, actin rockets, β-hemolytic", "Neonatal/elderly meningitis, amnionitis", "Ampicillin"],
   ["Bacillus anthracis", "Aerobic, spores, poly-D-glutamate capsule", "Cutaneous eschar, inhalational mediastinitis", "Ciprofloxacin/doxycycline"],
   ["Bacillus cereus", "Spores survive cooking rice; cereulide", "Emetic (1–5 h) or diarrheal food poisoning", "Supportive"],
   ["Actinomyces israelii", "Anaerobic, non–acid-fast, sulfur granules; oral flora", "Cervicofacial abscess with sinus tracts; IUD PID", "Penicillin"],
   ["Nocardia", "Aerobic, weakly acid-fast, catalase +, soil", "Pneumonia, brain abscess in immunocompromised", "TMP-SMX"]])

# ---------------- Toxins ----------------
TOXINS = T("Bacterial exotoxins by mechanism",
  ["Mechanism", "Toxins", "Effect"],
  [["ADP-ribosylate EF-2", "Diphtheria toxin, Pseudomonas exotoxin A", "Stop protein synthesis → cell death"],
   ["Cleave 28S rRNA (60S)", "Shiga toxin, Shiga-like toxin (EHEC)", "Stop protein synthesis → HUS, dysentery"],
   ["ADP-ribosylate Gs (↑cAMP)", "Cholera toxin, ETEC heat-labile toxin", "Watery diarrhea"],
   ["Activate guanylyl cyclase (↑cGMP)", "ETEC heat-stable toxin", "Watery diarrhea"],
   ["ADP-ribosylate Gi (↑cAMP)", "Pertussis toxin", "Lymphocytosis, impaired phagocytes"],
   ["Adenylyl cyclase itself", "Anthrax edema factor, B. pertussis adenylate cyclase toxin", "Edema, impaired neutrophils"],
   ["Zinc protease on MAPKK", "Anthrax lethal factor", "Macrophage death"],
   ["Cleave SNAREs", "Tetanospasmin (CNS inhibitory neurons), botulinum toxin (NMJ)", "Spastic vs flaccid paralysis"],
   ["Glucosylate Rho GTPases", "C. difficile toxins A and B", "Colonocyte death, pseudomembranes"],
   ["Phospholipase / pore", "C. perfringens α-toxin; streptolysin O; listeriolysin O", "Membrane damage, hemolysis"],
   ["Superantigen (MHC II–TCR Vβ)", "TSST-1, staph enterotoxins, SpeA/SpeC", "Cytokine storm, shock"],
   ["Protease on desmoglein-1", "Staph exfoliative toxins", "Bullous impetigo, SSSS"]])

ENDO_EXO = T("Endotoxin vs exotoxin",
  ["Feature", "Endotoxin (LPS)", "Exotoxin"],
  [["Source", "Outer membrane of Gram-negatives", "Secreted by Gram-positives and Gram-negatives"],
   ["Chemistry", "Lipid A (toxic part)", "Protein"],
   ["Genes", "Chromosomal", "Often plasmid or phage"],
   ["Heat", "Stable", "Mostly labile (staph enterotoxin is stable)"],
   ["Antigenicity / toxoid", "Weak; no toxoid", "Strong; toxoids for tetanus and diphtheria"],
   ["Action", "TLR4/CD14 → IL-1, IL-6, TNF; complement; DIC", "Specific enzymatic targets"]])

# ---------------- Gram-negative ----------------
NEISSERIA = T("Neisseria compared",
  ["Feature", "N. meningitidis", "N. gonorrhoeae"],
  [["Carbohydrates fermented", "Glucose and maltose", "Glucose only"],
   ["Capsule", "Yes (polysaccharide)", "No"],
   ["Vaccine", "Yes (MenACWY conjugate; MenB protein)", "No (antigenic variation of pili)"],
   ["Transmission", "Respiratory droplets", "Sexual, perinatal"],
   ["Diseases", "Meningitis, meningococcemia, Waterhouse-Friderichsen", "Urethritis, cervicitis, PID, septic arthritis, ophthalmia neonatorum"],
   ["Treatment", "Ceftriaxone or penicillin G", "Ceftriaxone (+ doxycycline if chlamydia not excluded)"],
   ["Prophylaxis", "Rifampin, ciprofloxacin, or ceftriaxone for contacts", "Erythromycin eye ointment for neonates"]])

ATYPICAL_PNA = T("Atypical pneumonia organisms",
  ["Organism", "Setting / clue", "Diagnosis", "Treatment"],
  [["Mycoplasma pneumoniae", "Young adults in close quarters; cold agglutinins", "PCR; no cell wall", "Macrolide, doxycycline, FQ"],
   ["Chlamydophila pneumoniae", "Mild pneumonia, pharyngitis, hoarseness", "PCR, serology", "Macrolide, doxycycline"],
   ["Legionella pneumophila", "Water aerosols; GI symptoms, confusion, hyponatremia", "Urine antigen; BCYE culture", "Levofloxacin or azithromycin"],
   ["Chlamydia psittaci", "Birds (parrots)", "Serology, PCR", "Doxycycline"],
   ["Coxiella burnetii", "Livestock birth products; no rash", "Serology", "Doxycycline"]])

HAEMOPHILUS_BORD_LEG = T("Fastidious respiratory Gram-negatives",
  ["Organism", "Culture", "Key virulence", "Disease"],
  [["H. influenzae", "Chocolate agar (factors X and V); satellites around S. aureus", "Type b PRP capsule; IgA protease", "Epiglottitis, meningitis (Hib); otitis, COPD flares (nontypeable)"],
   ["B. pertussis", "Bordet-Gengou or Regan-Lowe; PCR preferred", "Pertussis toxin (Gi), adenylate cyclase toxin, tracheal cytotoxin", "Whooping cough"],
   ["Legionella", "BCYE with cysteine and iron; silver stain", "Type IV secretion; intracellular in macrophages", "Legionnaires' disease, Pontiac fever"],
   ["Moraxella catarrhalis", "Blood/chocolate agar", "β-lactamase", "Otitis, sinusitis, COPD flares"]])

ECOLI = T("E. coli pathotypes",
  ["Pathotype", "Mechanism", "Clinical picture"],
  [["ETEC", "Heat-labile (↑cAMP) and heat-stable (↑cGMP) toxins; no invasion", "Traveler's watery diarrhea"],
   ["EPEC", "Bundle-forming pili, intimin–Tir attaching and effacing lesions; no toxin", "Watery diarrhea in infants"],
   ["EHEC (O157:H7)", "Shiga-like toxin; A/E lesions; sorbitol-negative", "Bloody diarrhea without fever → HUS; avoid antibiotics"],
   ["EIEC", "Invades colonic mucosa (like Shigella)", "Dysentery"],
   ["EAEC", "Stacked-brick adherence, biofilm", "Persistent diarrhea"],
   ["UPEC", "Type 1 fimbriae (cystitis), P fimbriae (pyelonephritis)", "UTI"],
   ["K1 strains", "Polysialic acid capsule", "Neonatal meningitis"]])

SALM_SHIG = T("Salmonella vs Shigella",
  ["Feature", "Salmonella", "Shigella"],
  [["Motility", "Motile (flagella)", "Non-motile"],
   ["H2S", "Produces (black colonies)", "No"],
   ["Infectious dose", "High (~10⁵; acid-labile)", "Very low (10–200; acid-stable)"],
   ["Reservoir", "Animals (poultry, eggs, reptiles); Typhi only humans", "Humans only"],
   ["Spread", "Hematogenous (Typhi via macrophages)", "Cell-to-cell (actin); rarely bacteremic"],
   ["Antibiotics", "Not for uncomplicated non-typhoidal (prolong carriage)", "Yes (shorten illness and spread)"],
   ["Lactose", "Non-fermenter", "Non-fermenter"]])

DIARRHEA = T("Infectious diarrhea patterns",
  ["Type", "Organisms", "Clues"],
  [["Preformed toxin (1–6 h)", "S. aureus, B. cereus (emetic)", "Vomiting predominant, no fever"],
   ["Watery, non-inflammatory", "V. cholerae, ETEC, C. perfringens, Giardia, Cryptosporidium, norovirus, rotavirus", "No blood, no fecal leukocytes"],
   ["Bloody, inflammatory", "Campylobacter, Salmonella, Shigella, EHEC, EIEC, Yersinia, C. difficile, E. histolytica", "Fever, blood, fecal leukocytes"],
   ["Pseudoappendicitis", "Yersinia enterocolitica", "Mesenteric adenitis, pork"],
   ["Seafood", "V. parahaemolyticus, V. vulnificus, norovirus", "Raw oysters"]])

VIBRIO = T("Vibrio species",
  ["Species", "Source", "Disease", "Treatment"],
  [["V. cholerae", "Fecally contaminated water", "Rice-water diarrhea (cholera toxin)", "Oral rehydration ± doxycycline/azithromycin"],
   ["V. parahaemolyticus", "Raw shellfish", "Self-limited gastroenteritis", "Supportive"],
   ["V. vulnificus", "Raw oysters, seawater wounds", "Sepsis and hemorrhagic bullae in liver disease/iron overload", "Doxycycline + ceftriaxone, debridement"]])

UREASE = T("Urease-positive organisms (CHuNKS PUNCH)",
  ["Organism", "Clinical relevance"],
  [["Proteus", "Struvite (staghorn) stones, alkaline urine"],
   ["Klebsiella", "UTI, struvite stones"],
   ["S. saprophyticus", "Cystitis"],
   ["H. pylori", "Ammonia buffers gastric acid; urea breath test"],
   ["Cryptococcus", "Virulence factor"],
   ["Nocardia", "Soil organism"],
   ["Ureaplasma", "Urethritis"]])

LACTOSE = T("MacConkey agar reactions",
  ["Lactose fermenters (pink)", "Non-fermenters (colorless)"],
  [["E. coli", "Proteus"], ["Klebsiella", "Pseudomonas (oxidase +)"], ["Enterobacter", "Salmonella (H2S +)"], ["Citrobacter", "Shigella"], ["Serratia (late)", "Yersinia"]])

# ---------------- Zoonoses & spirochetes ----------------
ZOONOSES = T("Zoonotic bacteria",
  ["Organism", "Reservoir / vector", "Disease", "Treatment"],
  [["Yersinia pestis", "Rodents; fleas", "Bubonic, septicemic, pneumonic plague", "Gentamicin/streptomycin, FQ"],
   ["Francisella tularensis", "Rabbits; ticks, deer flies, aerosols", "Ulceroglandular or pneumonic tularemia", "Gentamicin/streptomycin"],
   ["Brucella", "Unpasteurized dairy, livestock", "Undulant fever, sacroiliitis", "Doxycycline + rifampin"],
   ["Pasteurella multocida", "Cat and dog mouths", "Rapid cellulitis after bites", "Amoxicillin-clavulanate"],
   ["Bartonella henselae", "Cats (kittens); cat fleas", "Cat scratch disease, bacillary angiomatosis", "Azithromycin; erythromycin/doxycycline"],
   ["Coxiella burnetii", "Cattle, sheep, goat birth products", "Q fever, culture-negative endocarditis", "Doxycycline"],
   ["Leptospira", "Rat and animal urine in water", "Leptospirosis, Weil disease", "Doxycycline or penicillin"],
   ["Chlamydia psittaci", "Parrots and birds", "Psittacosis", "Doxycycline"],
   ["Capnocytophaga", "Dog mouths", "Sepsis in asplenic patients", "β-lactam/β-lactamase inhibitor"]])

SYPHILIS_STAGES = T("Syphilis stages",
  ["Stage", "Timing", "Findings", "Treatment"],
  [["Primary", "~3 weeks", "Painless indurated chancre, painless nodes", "Benzathine penicillin G IM × 1"],
   ["Secondary", "Weeks–months", "Palm/sole rash, condylomata lata, alopecia, lymphadenopathy", "Benzathine penicillin G IM × 1"],
   ["Latent", "Years", "Positive serology, no symptoms", "Early: × 1; late: weekly × 3"],
   ["Tertiary", "Decades", "Gummas, aortitis (vasa vasorum), tabes dorsalis, Argyll Robertson pupils", "Neurosyphilis: IV aqueous penicillin G"],
   ["Congenital", "In utero", "Snuffles, rash; later Hutchinson teeth, saddle nose, saber shins, deafness", "Treat mother; penicillin"]])

SYPH_TESTS = T("Syphilis serology",
  ["Test", "Detects", "Use", "After treatment"],
  [["VDRL / RPR (nontreponemal)", "Anti-cardiolipin antibodies", "Screening; follow titers", "Titers fall"],
   ["FTA-ABS, TP-PA, EIA (treponemal)", "Anti-treponemal antibodies", "Confirmation", "Usually positive for life"],
   ["Dark-field / PCR", "Organisms in lesion", "Primary and secondary lesions", "—"]])

TICKBORNE = T("Tick-borne infections in the US",
  ["Disease", "Organism", "Tick", "Clues", "Treatment"],
  [["Lyme disease", "Borrelia burgdorferi", "Ixodes", "Erythema migrans, facial palsy, AV block, arthritis", "Doxycycline"],
   ["Babesiosis", "Babesia microti", "Ixodes", "Hemolysis, Maltese cross, asplenia", "Atovaquone + azithromycin"],
   ["Anaplasmosis", "Anaplasma phagocytophilum", "Ixodes", "Morulae in neutrophils, leukopenia", "Doxycycline"],
   ["Ehrlichiosis", "Ehrlichia chaffeensis", "Amblyomma (lone star)", "Morulae in monocytes, no rash", "Doxycycline"],
   ["RMSF", "Rickettsia rickettsii", "Dermacentor", "Rash wrists/ankles → palms/soles", "Doxycycline (all ages)"],
   ["Tularemia", "Francisella tularensis", "Dermacentor, Amblyomma", "Ulcer + regional nodes", "Gentamicin/streptomycin"],
   ["Relapsing fever", "Borrelia hermsii", "Ornithodoros (soft)", "Recurrent fevers, cabins", "Doxycycline"]])

LYME_STAGES = T("Lyme disease stages",
  ["Stage", "Timing", "Findings", "Treatment"],
  [["Early localized", "Days–1 month", "Erythema migrans, flu-like illness", "Oral doxycycline"],
   ["Early disseminated", "Weeks–months", "Multiple EM, facial palsy, meningitis, AV block", "Doxycycline; IV ceftriaxone for severe carditis"],
   ["Late", "Months–years", "Oligoarthritis (knee), encephalopathy", "Doxycycline 28 days; ceftriaxone if refractory or CNS"]])

RICKETTSIAE = T("Rickettsial and related infections",
  ["Organism", "Vector", "Rash", "Notes"],
  [["R. rickettsii (RMSF)", "Dermacentor tick", "Wrists/ankles → trunk, palms, soles", "Endothelial vasculitis"],
   ["R. prowazekii (epidemic typhus)", "Human body louse", "Trunk → out, spares palms/soles", "Brill-Zinsser recrudescence"],
   ["R. typhi (murine typhus)", "Fleas", "Truncal", "Milder"],
   ["Ehrlichia / Anaplasma", "Amblyomma / Ixodes", "Usually none", "Morulae; leukopenia"],
   ["Coxiella burnetii", "None (aerosol)", "None", "Q fever, endocarditis"]])

CHLAMYDIA_SEROVARS = T("Chlamydia trachomatis serovars",
  ["Serovars", "Disease", "Notes"],
  [["A–C", "Trachoma", "Blindness; flies, hands; Africa"],
   ["D–K", "Urethritis, cervicitis, PID, neonatal conjunctivitis and pneumonia", "Most common bacterial STI"],
   ["L1–L3", "Lymphogranuloma venereum", "Painless ulcer → painful buboes, proctitis"]])

# ---------------- Mycobacteria & misc ----------------
TB_DRUGS = T("First-line TB drugs (RIPE)",
  ["Drug", "Mechanism", "Key toxicity"],
  [["Rifampin", "Inhibits DNA-dependent RNA polymerase (rpoB)", "Orange fluids, CYP450 induction, hepatotoxicity"],
   ["Isoniazid", "Prodrug (KatG) → inhibits mycolic acid synthesis (InhA)", "Neuropathy (give B6), hepatotoxicity, drug-induced lupus"],
   ["Pyrazinamide", "Unclear; active at acidic pH", "Hyperuricemia/gout, hepatotoxicity"],
   ["Ethambutol", "Inhibits arabinosyltransferase", "Optic neuritis (red-green color loss)"]])

TST = T("Tuberculin skin test cutoffs (induration)",
  ["≥5 mm", "≥10 mm", "≥15 mm"],
  [["HIV, recent contacts of active TB, fibrotic CXR, transplant/immunosuppressed", "Recent immigrants, IVDU, healthcare/prison/shelter workers and residents, children <4", "No risk factors"]])

LEPROSY = T("Leprosy spectrum",
  ["Feature", "Tuberculoid", "Lepromatous"],
  [["Immune response", "Th1 (IFN-γ, IL-2)", "Th2 (IL-4, IL-10)"],
   ["Lesions", "Few, well-demarcated, hypoesthetic plaques", "Diffuse nodules, leonine facies"],
   ["Bacilli", "Few", "Many (foamy macrophages)"],
   ["Lepromin test", "Positive", "Negative"],
   ["Treatment", "Dapsone + rifampin", "Dapsone + rifampin + clofazimine"]])

VAGINITIS = T("Vaginitis compared",
  ["Feature", "Bacterial vaginosis", "Trichomoniasis", "Candida"],
  [["Discharge", "Thin gray-white, fishy", "Frothy yellow-green", "Thick white 'cottage cheese'"],
   ["pH", ">4.5", ">4.5", "Normal (<4.5)"],
   ["Microscopy", "Clue cells, few WBCs", "Motile flagellated trophozoites", "Pseudohyphae on KOH"],
   ["Other", "Positive whiff test", "Strawberry cervix; STI", "Itching; antibiotics, diabetes, pregnancy"],
   ["Treatment", "Metronidazole or clindamycin", "Metronidazole (treat partners)", "Azoles"]])

GENITAL_ULCERS = T("Genital ulcers",
  ["Disease", "Organism", "Ulcer", "Nodes"],
  [["Primary syphilis", "Treponema pallidum", "Painless, indurated, clean base", "Painless, rubbery"],
   ["Genital herpes", "HSV-2 (or HSV-1)", "Painful grouped vesicles → shallow ulcers", "Tender"],
   ["Chancroid", "Haemophilus ducreyi", "Painful, soft, ragged, purulent", "Painful, suppurative"],
   ["LGV", "C. trachomatis L1–L3", "Painless, transient", "Painful buboes, groove sign"],
   ["Donovanosis", "Klebsiella granulomatis", "Painless, beefy red, bleeds", "Pseudobuboes"]])

# ---------------- Antibiotics ----------------
CELL_WALL = T("Cell wall and membrane agents",
  ["Drug", "Target", "Key points"],
  [["Fosfomycin", "MurA (first cytoplasmic step)", "Single-dose cystitis therapy"],
   ["Bacitracin", "Bactoprenol recycling", "Topical only (nephrotoxic)"],
   ["Vancomycin", "Binds D-Ala-D-Ala", "MRSA, C. difficile (oral); resistance D-Ala-D-Lac"],
   ["β-lactams", "PBPs (transpeptidases)", "Resistance: β-lactamase, altered PBPs, porins"],
   ["Daptomycin", "Depolarizes Gram-positive membrane", "Inactivated by surfactant; CPK"],
   ["Polymyxins", "Bind lipid A, disrupt membranes", "Last resort Gram-negatives; nephro-/neurotoxic"]])

CEPHS = T("Cephalosporin generations",
  ["Generation", "Examples", "Coverage / use"],
  [["1st", "Cefazolin, cephalexin", "Gram-positives, PEcK; surgical prophylaxis, MSSA"],
   ["2nd", "Cefoxitin, cefuroxime", "Adds H. influenzae, Enterobacter, Neisseria; cefoxitin anaerobes"],
   ["3rd", "Ceftriaxone, cefotaxime, ceftazidime", "Serious Gram-negatives; meningitis, gonorrhea; ceftazidime → Pseudomonas"],
   ["4th", "Cefepime", "Gram-positives + Pseudomonas; AmpC-stable"],
   ["5th", "Ceftaroline", "MRSA (binds PBP2a); not Pseudomonas"],
   ["None cover", "—", "Listeria, Atypicals, MRSA (except 5th), Enterococci (LAME)"]])

PROTEIN_SYNTH = T("Protein synthesis inhibitors",
  ["Drug", "Subunit / action", "Key toxicity"],
  [["Aminoglycosides", "30S; misreading, block initiation", "Nephrotoxicity, ototoxicity, NM blockade, teratogen"],
   ["Tetracyclines", "30S; block aminoacyl-tRNA", "Teeth/bone in kids, photosensitivity, esophagitis"],
   ["Chloramphenicol", "50S; peptidyltransferase", "Aplastic anemia, gray baby"],
   ["Clindamycin", "50S; peptide transfer", "C. difficile"],
   ["Linezolid", "50S (23S); initiation complex", "Myelosuppression, serotonin syndrome"],
   ["Macrolides", "50S (23S); translocation", "QT prolongation, GI motility, CYP3A4 inhibition"]])

ABX_TOX = T("High-yield antibiotic toxicities",
  ["Drug", "Toxicity"],
  [["Fluoroquinolones", "Tendon rupture, QT, cartilage damage, CNS effects"],
   ["TMP-SMX", "Hyperkalemia (ENaC), SJS, kernicterus, hemolysis in G6PD"],
   ["Metronidazole", "Disulfiram-like reaction, metallic taste, neuropathy"],
   ["Nitrofurantoin", "Pulmonary fibrosis, hemolysis in G6PD"],
   ["Vancomycin", "Nephrotoxicity, ototoxicity, infusion reaction"],
   ["Chloramphenicol", "Aplastic anemia, gray baby syndrome"],
   ["Linezolid", "Thrombocytopenia, serotonin syndrome, optic neuropathy"],
   ["Imipenem", "Seizures"],
   ["Ceftriaxone", "Biliary sludge, kernicterus in neonates"]])

ANTI_PSEUDOMONAL = T("Antipseudomonal agents",
  ["Class", "Active drugs", "Not active"],
  [["Penicillins", "Piperacillin-tazobactam", "Ampicillin, nafcillin"],
   ["Cephalosporins", "Ceftazidime, cefepime, ceftolozane-tazobactam", "Ceftriaxone, cefazolin, ceftaroline"],
   ["Carbapenems", "Imipenem, meropenem", "Ertapenem"],
   ["Others", "Aztreonam, ciprofloxacin/levofloxacin, aminoglycosides, polymyxins", "Tigecycline, TMP-SMX"]])

RESISTANCE = T("Resistance mechanisms",
  ["Drug", "Main mechanism"],
  [["β-lactams", "β-lactamases; altered PBPs (MRSA PBP2a, pneumococcus); porin loss"],
   ["Vancomycin", "D-Ala-D-Ala → D-Ala-D-Lac (vanA)"],
   ["Aminoglycosides", "Acetylation, adenylation, phosphorylation"],
   ["Macrolides", "23S rRNA methylation (erm), efflux (mef)"],
   ["Tetracyclines", "Efflux, ribosomal protection"],
   ["Fluoroquinolones", "Gyrase/topo IV mutations, efflux, qnr"],
   ["Rifampin", "rpoB mutation"],
   ["Sulfonamides", "Altered dihydropteroate synthase, ↑PABA"]])

# ---------------- Bacterial genetics & lab ----------------
GENETICS = T("Bacterial gene transfer",
  ["Process", "Mechanism", "DNase-sensitive?", "Examples"],
  [["Transformation", "Uptake of naked DNA", "Yes", "S. pneumoniae, H. influenzae, Neisseria"],
   ["Conjugation", "Sex pilus (F factor); plasmid transfer", "No", "R plasmids, ESBL spread"],
   ["Generalized transduction", "Phage packages random host DNA (lytic)", "No", "Any gene"],
   ["Specialized transduction", "Faulty prophage excision (lysogenic)", "No", "Genes next to insertion site"],
   ["Lysogenic conversion", "Prophage genes expressed", "No", "Diphtheria, cholera, botulinum, Shiga-like, erythrogenic toxins"],
   ["Transposition", "Transposons jump without homology", "No", "vanA (Tn1546)"]])

STAINS = T("Special stains",
  ["Stain", "Organisms"],
  [["Giemsa", "Chlamydia, Borrelia, Rickettsia, trypanosomes, Plasmodium, Toxoplasma"],
   ["PAS", "Tropheryma whipplei (macrophages)"],
   ["Ziehl-Neelsen / acid-fast", "Mycobacteria; Nocardia (modified); Cryptosporidium, Cyclospora, Cystoisospora oocysts"],
   ["India ink", "Cryptococcus capsule"],
   ["Silver", "Helicobacter, Legionella, Bartonella, fungi (Pneumocystis)"],
   ["Mucicarmine", "Cryptococcus capsule in tissue"]])

MEDIA = T("Special culture media",
  ["Organism", "Medium"],
  [["H. influenzae", "Chocolate agar with factors V and X"],
   ["Neisseria", "Thayer-Martin (VPN + trimethoprim)"],
   ["B. pertussis", "Bordet-Gengou, Regan-Lowe"],
   ["C. diphtheriae", "Tellurite, Löffler"],
   ["M. tuberculosis", "Löwenstein-Jensen, Middlebrook"],
   ["Mycoplasma", "Eaton agar"],
   ["Legionella", "Buffered charcoal yeast extract + cysteine + iron"],
   ["Fungi", "Sabouraud"],
   ["Vibrio", "TCBS"],
   ["E. coli O157:H7", "Sorbitol MacConkey"]])

# ---------------- Viruses ----------------
HERPES = T("Human herpesviruses",
  ["Virus", "Latency site", "Key diseases", "Treatment"],
  [["HSV-1", "Trigeminal ganglion", "Oral herpes, temporal lobe encephalitis, keratitis", "Acyclovir family"],
   ["HSV-2", "Sacral ganglia", "Genital herpes, neonatal herpes, recurrent meningitis", "Acyclovir family"],
   ["VZV (HHV-3)", "Dorsal root / cranial ganglia", "Chickenpox, shingles", "Acyclovir family; vaccines"],
   ["EBV (HHV-4)", "B cells", "Mono, Burkitt, nasopharyngeal carcinoma, Hodgkin, PTLD", "Supportive"],
   ["CMV (HHV-5)", "Monocytes/macrophages", "Congenital deafness, retinitis, colitis, transplant disease", "Ganciclovir, foscarnet, cidofovir"],
   ["HHV-6/7", "T cells", "Roseola", "Supportive"],
   ["HHV-8", "B cells, endothelium", "Kaposi sarcoma, primary effusion lymphoma, Castleman", "ART ± chemotherapy"]])

HERPES_DRUGS = T("Anti-herpesvirus drugs",
  ["Drug", "Activation", "Use", "Toxicity"],
  [["Acyclovir, valacyclovir, famciclovir", "Viral thymidine kinase", "HSV, VZV", "Crystal nephropathy"],
   ["Ganciclovir, valganciclovir", "CMV UL97 kinase", "CMV", "Myelosuppression"],
   ["Foscarnet", "None (pyrophosphate analog)", "Resistant CMV, acyclovir-resistant HSV", "Nephrotoxicity, ↓Ca/Mg, seizures"],
   ["Cidofovir", "None (nucleotide analog)", "Resistant CMV, adenovirus", "Nephrotoxicity (give probenecid)"]])

DNA_VIRUSES = T("DNA virus families",
  ["Family", "Genome", "Envelope", "Examples"],
  [["Herpesviridae", "dsDNA, linear", "Yes", "HSV, VZV, EBV, CMV, HHV-6/7/8"],
   ["Hepadnaviridae", "Partially dsDNA, circular", "Yes", "HBV"],
   ["Adenoviridae", "dsDNA, linear", "No", "Adenovirus"],
   ["Parvoviridae", "ssDNA, linear", "No", "Parvovirus B19"],
   ["Papillomaviridae", "dsDNA, circular", "No", "HPV"],
   ["Polyomaviridae", "dsDNA, circular", "No", "JC, BK"],
   ["Poxviridae", "dsDNA, linear; cytoplasmic replication", "Yes", "Smallpox, molluscum, mpox"]])

RASHES = T("Childhood exanthems",
  ["Disease", "Cause", "Features"],
  [["Measles", "Paramyxovirus", "3 Cs, Koplik spots, descending rash"],
   ["Rubella", "Togavirus", "Postauricular nodes, mild descending rash"],
   ["Roseola", "HHV-6", "High fever, then rash as fever breaks"],
   ["Erythema infectiosum", "Parvovirus B19", "Slapped cheeks, lacy rash"],
   ["Varicella", "VZV", "Crops of lesions in different stages"],
   ["Hand-foot-mouth", "Coxsackie A", "Oral ulcers, palm/sole vesicles"],
   ["Scarlet fever", "GAS", "Sandpaper rash, strawberry tongue, desquamation"]])

RNA_FAMILIES = T("RNA virus families",
  ["Family", "Genome", "Envelope", "Examples"],
  [["Picornavirus", "+ssRNA", "No", "Polio, coxsackie, echo, rhino, HAV"],
   ["Calicivirus", "+ssRNA", "No", "Norovirus"],
   ["Reovirus", "dsRNA, segmented", "No", "Rotavirus"],
   ["Hepevirus", "+ssRNA", "No", "HEV"],
   ["Flavivirus", "+ssRNA", "Yes", "HCV, dengue, yellow fever, West Nile, Zika"],
   ["Togavirus", "+ssRNA", "Yes", "Rubella, chikungunya, EEE"],
   ["Coronavirus", "+ssRNA", "Yes", "SARS-CoV-2"],
   ["Retrovirus", "+ssRNA (RT)", "Yes", "HIV, HTLV"],
   ["Orthomyxovirus", "−ssRNA, segmented", "Yes", "Influenza"],
   ["Paramyxovirus", "−ssRNA", "Yes", "Measles, mumps, RSV, parainfluenza"],
   ["Rhabdovirus", "−ssRNA", "Yes", "Rabies"],
   ["Filovirus", "−ssRNA", "Yes", "Ebola, Marburg"],
   ["Bunya / Arena", "−ssRNA, segmented", "Yes", "Hantavirus / LCMV, Lassa"]])

PARAMYXO = T("Paramyxoviruses",
  ["Virus", "Disease", "Key points"],
  [["Measles", "Rubeola", "Koplik spots; vitamin A; SSPE; giant cell pneumonia"],
   ["Mumps", "Parotitis", "Orchitis, aseptic meningitis, pancreatitis"],
   ["RSV", "Bronchiolitis", "F protein; no hemagglutinin; nirsevimab"],
   ["Parainfluenza", "Croup", "Steeple sign; dexamethasone"],
   ["hMPV", "Bronchiolitis/pneumonia", "Similar to RSV"]])

ARBO = T("Mosquito-borne viruses",
  ["Virus", "Family", "Vector", "Hallmark"],
  [["Dengue", "Flavivirus", "Aedes", "Breakbone fever; severe with second serotype (ADE)"],
   ["Zika", "Flavivirus", "Aedes (also sexual)", "Congenital microcephaly"],
   ["Yellow fever", "Flavivirus", "Aedes", "Jaundice, black vomit, Councilman bodies"],
   ["Chikungunya", "Togavirus", "Aedes", "Severe prolonged polyarthralgia"],
   ["West Nile", "Flavivirus", "Culex (birds reservoir)", "Encephalitis, flaccid paralysis in elderly"]])

HIV_DRUGS = T("Antiretroviral classes",
  ["Class", "Examples", "Mechanism", "Key toxicity"],
  [["NRTIs", "Tenofovir, emtricitabine, lamivudine, abacavir, zidovudine", "Chain terminators of RT", "Lactic acidosis; abacavir HLA-B*57:01; TDF kidney/bone; AZT anemia"],
   ["NNRTIs", "Efavirenz, rilpivirine, doravirine", "Allosteric RT inhibition", "Rash; efavirenz CNS effects"],
   ["Integrase inhibitors", "Dolutegravir, bictegravir, raltegravir", "Block strand transfer", "Weight gain, ↑CK"],
   ["Protease inhibitors", "Darunavir, atazanavir (boosted)", "Block Gag-Pol cleavage", "Hyperglycemia, lipodystrophy, CYP interactions"],
   ["Entry/fusion", "Maraviroc, enfuvirtide", "CCR5 / gp41", "Hepatotoxicity / injection reactions"]])

HIV_OI = T("HIV opportunistic infections by CD4 count",
  ["CD4 (cells/μL)", "Infections / conditions", "Prophylaxis"],
  [["<500", "Thrush, zoster, TB, oral hairy leukoplakia", "—"],
   ["<200", "Pneumocystis, PML, HIV dementia", "TMP-SMX"],
   ["<100", "Toxoplasma, Cryptococcus, Candida esophagitis, histoplasmosis", "TMP-SMX if Toxo IgG +"],
   ["<50", "CMV retinitis/colitis, disseminated MAC, primary CNS lymphoma", "Azithromycin only if ART delayed"]])

HBV_SEROLOGY = T("Hepatitis B serology",
  ["Pattern", "HBsAg", "Anti-HBs", "Anti-HBc", "HBeAg"],
  [["Acute infection", "+", "−", "IgM", "+"],
   ["Window period", "−", "−", "IgM", "±"],
   ["Chronic (high infectivity)", "+", "−", "IgG", "+"],
   ["Chronic (low infectivity)", "+", "−", "IgG", "−"],
   ["Recovered", "−", "+", "IgG", "−"],
   ["Vaccinated", "−", "+", "−", "−"]])

HEPATITIS = T("Hepatitis viruses",
  ["Virus", "Family / genome", "Spread", "Chronic?", "Notes"],
  [["HAV", "Picornavirus, +ssRNA, naked", "Fecal-oral", "No", "Travel, shellfish; vaccine"],
   ["HBV", "Hepadnavirus, partially dsDNA, RT", "Blood, sex, perinatal", "Yes (90% neonates)", "HCC; PAN; vaccine"],
   ["HCV", "Flavivirus, +ssRNA", "Blood (IVDU)", "Yes (60–80%)", "Cryoglobulinemia; DAAs cure"],
   ["HDV", "Deltavirus, −ssRNA circular", "Blood; needs HBsAg", "Yes", "Superinfection severe"],
   ["HEV", "Hepevirus, +ssRNA, naked", "Fecal-oral, pork", "No (except immunosuppressed)", "Fulminant in pregnancy"]])

HCV_DAA = T("HCV direct-acting antivirals",
  ["Target", "Suffix", "Examples"],
  [["NS5B polymerase", "-buvir", "Sofosbuvir"],
   ["NS5A", "-asvir", "Ledipasvir, velpatasvir, pibrentasvir"],
   ["NS3/4A protease", "-previr", "Glecaprevir, grazoprevir, voxilaprevir"]])

# ---------------- Fungi ----------------
DIMORPHIC = T("Endemic dimorphic fungi",
  ["Fungus", "Region", "Tissue form", "Treatment"],
  [["Histoplasma", "Ohio/Mississippi valleys; bird/bat droppings", "Small yeast inside macrophages", "Itraconazole; amphotericin B if severe"],
   ["Blastomyces", "Great Lakes, Ohio/Mississippi, southeast", "Large yeast, broad-based budding", "Itraconazole; amphotericin B if severe"],
   ["Coccidioides", "Southwest US deserts", "Spherules with endospores", "Fluconazole/itraconazole; amphotericin B"],
   ["Paracoccidioides", "Latin America", "Multiple buds ('captain's wheel')", "Itraconazole"],
   ["Sporothrix", "Worldwide; plants, soil", "Cigar-shaped yeast", "Itraconazole"]])

OPP_FUNGI = T("Opportunistic fungi",
  ["Fungus", "Morphology", "Setting", "Treatment"],
  [["Candida", "Yeast + pseudohyphae; germ tube", "Thrush, candidemia (lines, TPN)", "Azoles; echinocandins for candidemia"],
   ["Aspergillus", "Septate hyphae, acute-angle branching", "Neutropenia; ABPA; aspergilloma", "Voriconazole"],
   ["Mucor / Rhizopus", "Broad nonseptate hyphae, right-angle branching", "DKA, neutropenia, deferoxamine", "Debridement + amphotericin B"],
   ["Cryptococcus", "Encapsulated yeast (India ink)", "AIDS meningitis", "Amphotericin B + flucytosine → fluconazole"],
   ["Pneumocystis", "Cup-shaped cysts (GMS)", "CD4 <200, steroids", "TMP-SMX ± steroids"]])

ANTIFUNGALS = T("Antifungal drugs",
  ["Drug", "Target", "Toxicity / notes"],
  [["Amphotericin B, nystatin", "Bind ergosterol → pores", "Nephrotoxicity, ↓K/Mg, infusion reactions"],
   ["Azoles", "14α-demethylase (ergosterol synthesis)", "CYP3A4 inhibition; ketoconazole antiandrogen; voriconazole visual changes"],
   ["Echinocandins", "β-(1,3)-glucan synthase", "Well tolerated; poor for Cryptococcus"],
   ["Flucytosine", "Converted to 5-FU", "Bone marrow suppression"],
   ["Terbinafine", "Squalene epoxidase", "Hepatotoxicity; onychomycosis"],
   ["Griseofulvin", "Microtubules", "Teratogen, CYP induction; tinea capitis"]])

# ---------------- Parasites ----------------
INTESTINAL_PROTOZOA = T("Intestinal protozoa",
  ["Organism", "Disease", "Diagnosis", "Treatment"],
  [["Giardia", "Fatty diarrhea, bloating (campers)", "Stool antigen, cysts/trophozoites", "Tinidazole or metronidazole"],
   ["Entamoeba histolytica", "Bloody diarrhea, liver abscess", "Trophozoites with RBCs; serology", "Metronidazole + paromomycin"],
   ["Cryptosporidium", "Watery diarrhea; chronic in AIDS", "Acid-fast oocysts", "Nitazoxanide; ART"],
   ["Cyclospora", "Watery diarrhea (imported produce)", "Acid-fast larger oocysts", "TMP-SMX"]])

MALARIA = T("Plasmodium species",
  ["Species", "Cycle", "Features", "Relapse?"],
  [["P. falciparum", "Irregular", "Multiple rings, banana gametocytes, all RBC ages; cerebral malaria", "No"],
   ["P. vivax", "48 h", "Enlarged RBCs, Schüffner dots; Duffy antigen", "Yes (hypnozoites)"],
   ["P. ovale", "48 h", "Oval RBCs, Schüffner dots", "Yes (hypnozoites)"],
   ["P. malariae", "72 h", "Band forms; nephrotic syndrome", "No"],
   ["P. knowlesi", "24 h", "Southeast Asia macaques; high parasitemia", "No"]])

BLOOD_TISSUE_PROTOZOA = T("Blood and tissue protozoa",
  ["Organism", "Vector / source", "Disease", "Treatment"],
  [["Babesia microti", "Ixodes tick", "Hemolysis, Maltese cross", "Atovaquone + azithromycin"],
   ["Trypanosoma cruzi", "Reduviid bug", "Chagas: cardiomyopathy, megacolon, megaesophagus", "Benznidazole, nifurtimox"],
   ["Trypanosoma brucei", "Tsetse fly", "Sleeping sickness", "Suramin, fexinidazole, melarsoprol"],
   ["Leishmania donovani", "Sandfly", "Kala-azar", "Liposomal amphotericin B"],
   ["Toxoplasma gondii", "Cat feces, undercooked meat", "Encephalitis (AIDS), congenital", "Pyrimethamine + sulfadiazine + leucovorin"],
   ["Naegleria fowleri", "Warm freshwater", "Primary amebic meningoencephalitis", "Amphotericin B + miltefosine"]])

NEMATODES = T("Nematodes (roundworms)",
  ["Worm", "Transmission", "Disease", "Treatment"],
  [["Enterobius", "Fecal-oral", "Perianal itch; tape test", "Albendazole, pyrantel"],
   ["Ascaris", "Fecal-oral (eggs)", "Löffler syndrome, obstruction", "Albendazole"],
   ["Strongyloides", "Skin penetration; autoinfection", "Hyperinfection with steroids", "Ivermectin"],
   ["Hookworm", "Skin penetration", "Iron deficiency anemia", "Albendazole"],
   ["Trichinella", "Undercooked pork/game", "Myositis, periorbital edema", "Albendazole"],
   ["Toxocara", "Dog/cat feces", "Visceral and ocular larva migrans", "Albendazole"],
   ["Onchocerca", "Blackfly", "River blindness", "Ivermectin"],
   ["Loa loa", "Deer fly", "Eye worm, Calabar swellings", "Diethylcarbamazine"],
   ["Wuchereria", "Mosquito", "Elephantiasis", "DEC, ivermectin + albendazole"]])

CESTODES_TREMATODES = T("Cestodes (tapeworms) and trematodes (flukes)",
  ["Worm", "Source", "Disease", "Treatment"],
  [["Taenia solium", "Pork (taeniasis) or eggs (cysticercosis)", "Neurocysticercosis", "Albendazole ± praziquantel"],
   ["Diphyllobothrium latum", "Raw freshwater fish", "B12 deficiency", "Praziquantel"],
   ["Echinococcus granulosus", "Dog feces (sheep)", "Hydatid cysts", "Albendazole + surgery/PAIR"],
   ["Schistosoma mansoni/japonicum", "Snails (skin penetration)", "Portal hypertension", "Praziquantel"],
   ["Schistosoma haematobium", "Snails", "Hematuria, bladder SCC", "Praziquantel"],
   ["Clonorchis", "Raw fish", "Cholangiocarcinoma", "Praziquantel"],
   ["Paragonimus", "Undercooked crab", "Hemoptysis", "Praziquantel"]])

ANTHELMINTICS = T("Anthelmintics",
  ["Drug", "Mechanism", "Uses"],
  [["Albendazole / mebendazole", "Bind β-tubulin; block glucose uptake", "Most nematodes; cysticercosis, echinococcus"],
   ["Pyrantel pamoate", "Nicotinic agonist (spastic paralysis)", "Pinworm, Ascaris, hookworm"],
   ["Ivermectin", "Glutamate-gated Cl− channels", "Strongyloides, Onchocerca, scabies, lice"],
   ["Praziquantel", "↑Ca2+ permeability", "Trematodes and cestodes"],
   ["Diethylcarbamazine", "Sensitizes microfilariae", "Loa loa, Wuchereria"]])

# ---------------- Systems ----------------
MENINGITIS_AGE = T("Bacterial meningitis by age",
  ["Age", "Common causes", "Empiric therapy"],
  [["0–6 months", "GBS, E. coli, Listeria", "Ampicillin + cefotaxime (or gentamicin)"],
   ["6 months–6 years", "S. pneumoniae, N. meningitidis, Hib (unvaccinated), enteroviruses", "Ceftriaxone + vancomycin"],
   ["6–60 years", "N. meningitidis, S. pneumoniae, enteroviruses, HSV", "Ceftriaxone + vancomycin"],
   [">60 years", "S. pneumoniae, N. meningitidis, Listeria", "Ceftriaxone + vancomycin + ampicillin"]])

CSF = T("CSF patterns",
  ["Cause", "Cells", "Protein", "Glucose", "Opening pressure"],
  [["Bacterial", "↑↑ neutrophils", "↑", "↓", "↑"],
   ["Viral", "↑ lymphocytes", "Normal/slightly ↑", "Normal", "Normal/↑"],
   ["TB / fungal", "↑ lymphocytes", "↑↑", "↓", "↑ (very high in Crypto)"],
   ["Guillain-Barré", "Normal", "↑↑", "Normal", "Normal"]])

TORCH = T("Congenital (TORCH) infections",
  ["Infection", "Classic findings"],
  [["Toxoplasma", "Chorioretinitis, hydrocephalus, diffuse calcifications"],
   ["Rubella", "PDA, cataracts, deafness, blueberry muffin rash"],
   ["CMV", "Periventricular calcifications, microcephaly, sensorineural deafness"],
   ["HSV", "Vesicles, keratoconjunctivitis, encephalitis, dissemination"],
   ["Syphilis", "Snuffles, rash; later Hutchinson teeth, saddle nose, saber shins"],
   ["Varicella", "Limb hypoplasia, cicatricial scars"],
   ["Parvovirus B19", "Hydrops fetalis"],
   ["Zika", "Severe microcephaly"]])

VACCINES = T("Vaccine types",
  ["Type", "Examples", "Notes"],
  [["Live attenuated", "MMR, varicella, yellow fever, rotavirus, intranasal flu, oral typhoid, BCG", "Strong cellular + humoral immunity; avoid in pregnancy and severe immunosuppression"],
   ["Inactivated", "Rabies, injectable influenza, IPV, hepatitis A", "Humoral; boosters needed"],
   ["Subunit / recombinant", "HBV, HPV, recombinant zoster, acellular pertussis", "Safe in immunocompromised"],
   ["Toxoid", "Tetanus, diphtheria", "Antitoxin antibodies"],
   ["Conjugate", "Hib, PCV, MenACWY", "T-cell help → IgG and memory in infants"],
   ["mRNA", "COVID-19", "Encodes antigen (spike)"]])

IMMUNODEF = T("Immune defects and typical infections",
  ["Defect", "Examples", "Typical organisms"],
  [["B cell / antibody", "XLA, CVID", "Encapsulated bacteria, enteroviruses, Giardia"],
   ["T cell", "DiGeorge, HIV", "Candida, Pneumocystis, viruses, intracellular bacteria"],
   ["Phagocyte", "CGD, neutropenia, LAD", "Catalase-positive bacteria, Aspergillus, Candida"],
   ["Terminal complement (C5–C9)", "Congenital, eculizumab", "Neisseria"],
   ["Asplenia", "Splenectomy, sickle cell", "Encapsulated bacteria, Babesia, Capnocytophaga"]])
