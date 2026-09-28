"""Encyclopedia: general microbiology principles, antimicrobials, and cross-cutting syndromes."""
from ecore import E, S, P, H

ENTRIES = [
E("gram-stain", "Gram Stain, Cell Walls & Special Stains", "Principles & Pharmacology",
  "Why organisms take up the dyes they do, and what to reach for when the Gram stain shows nothing.",
  aka=["Gram staining", "acid-fast", "peptidoglycan", "LPS", "endotoxin"],
  keywords=["crystal violet", "safranin", "mycolic acid", "India ink", "silver stain", "Giemsa", "PAS"],
  quick=[("Gram-positive", "Thick peptidoglycan retains crystal violet - purple"),
         ("Gram-negative", "Thin peptidoglycan + outer membrane - decolorizes, pink"),
         ("Acid-fast", "Mycolic acids resist acid-alcohol - mycobacteria, Nocardia"),
         ("No wall", "Mycoplasma - does not stain at all"),
         ("Too thin", "Treponema, Leptospira - dark-field or silver stain")],
  images=[("fig-gram-wall.jpg", "Gram-positive and Gram-negative envelopes compared."),
          ("fig-lps.jpg", "Lipopolysaccharide: lipid A, core sugars, and the O antigen.")],
  sections=[
    S("Why the colors happen", [
      H("Gram-positive organisms have a thick multilayer peptidoglycan wall that traps the crystal violet-iodine complex when alcohol is applied, so they stay purple. Gram-negative organisms have a thin peptidoglycan layer and a lipid-rich outer membrane that alcohol dissolves, so the complex washes out and they take up the pink safranin counterstain."),
      P("Teichoic and lipoteichoic acids thread through the Gram-positive wall and signal through TLR2, driving cytokine release. The Gram-negative outer membrane carries lipopolysaccharide and porins, which is the structural basis for both endotoxic shock and several antibiotic resistance mechanisms."),
      H("Organisms that stain poorly or not at all: Treponema and Leptospira (too thin - use dark-field or silver stain), Mycoplasma (no cell wall), Rickettsia and Chlamydia (intracellular, poorly staining), Legionella (branched-chain fatty acids - use silver stain), and Mycobacteria (mycolic acid - use acid-fast)."),
    ]),
    S("Endotoxin", [
      H("Lipid A is the toxic portion of lipopolysaccharide. It engages CD14 and the TLR4/MD-2 complex on macrophages, triggering release of IL-1, IL-6, and TNF-alpha. The result is fever, vasodilation, and hypotension; complement activation yields C3a and C5a, and tissue factor expression drives disseminated intravascular coagulation."),
      P("Unlike exotoxins, endotoxin is a structural component released on lysis rather than a secreted protein, it is heat-stable, it cannot be converted into a toxoid, and it is far less potent by weight. The O antigen is the variable outer polysaccharide used for serotyping and is not itself toxic."),
    ]),
    S("Special stains worth memorizing", [
      H("India ink or mucicarmine for Cryptococcus; silver (GMS) for Pneumocystis and fungi; Giemsa for Borrelia, Plasmodium, Trypanosoma, Chlamydia, and Rickettsia; PAS for Whipple disease and fungal walls; Ziehl-Neelsen for acid-fast organisms; and Congo red with apple-green birefringence for amyloid."),
    ]),
  ]),

E("genetics", "Bacterial Genetics & Gene Transfer", "Principles & Pharmacology",
  "The four ways bacteria acquire new DNA, and why that determines how fast resistance spreads.",
  aka=["transformation", "conjugation", "transduction", "transposition"],
  keywords=["plasmid", "F factor", "Hfr", "bacteriophage", "lysogeny", "transposon", "integron"],
  quick=[("Transformation", "Naked DNA from the environment; blocked by DNase"),
         ("Conjugation", "Direct cell contact via pilus; NOT blocked by DNase"),
         ("Transduction", "Phage-mediated; generalized or specialized"),
         ("Transposition", "Jumping genes within and between genomes"),
         ("Naturally competent", "SHiN - Strep pneumoniae, Haemophilus, Neisseria")],
  images=[("fig-conjugation.jpg", "Conjugation: the donor extends a pilus, then transfers one plasmid strand.")],
  sections=[
    S("The four mechanisms", [
      H("Transformation is uptake of naked DNA from the environment. Naturally competent organisms are remembered as SHiN: Streptococcus pneumoniae, Haemophilus influenzae, and Neisseria. Because the DNA is free in solution, adding DNase prevents it - the classic experimental discriminator."),
      H("Conjugation transfers DNA through direct contact: an F-plasmid-bearing donor extends a sex pilus, pulls the cells together, nicks the plasmid, and passes one strand. Both cells end up as donors, which is why resistance plasmids sweep through a population. DNase does not block it because the DNA never enters the medium. An Hfr cell has the F plasmid integrated into the chromosome and transfers chromosomal genes."),
      H("Transduction is phage-mediated. Generalized transduction happens during the lytic cycle when a phage mispackages any random fragment of host DNA. Specialized transduction happens when a lysogenic prophage excises imprecisely and carries the adjacent flanking genes - which is how several toxin genes travel."),
      P("Transposition moves segments within or between genomes, and integrons capture and express arrays of resistance cassettes. Together these account for the multidrug resistance plasmids seen in Enterobacterales."),
    ]),
    S("Phage-encoded toxins", [
      H("Several major toxins are carried by lysogenic phages - mnemonic ABCDE: shigA-like toxin, Botulinum toxin, Cholera toxin, Diphtheria toxin, and Erythrogenic (streptococcal pyrogenic) toxin. This is why only phage-infected strains of C. diphtheriae are toxigenic."),
    ]),
  ]),

E("cell-wall-abx", "Cell Wall Inhibitors", "Principles & Pharmacology",
  "Beta-lactams and glycopeptides: how they work, what they miss, and how bacteria defeat them.",
  aka=["penicillin", "cephalosporin", "carbapenem", "vancomycin", "aztreonam", "beta-lactam"],
  keywords=["transpeptidase", "PBP", "beta-lactamase", "D-Ala-D-Ala", "ESBL", "red man syndrome"],
  quick=[("Beta-lactams", "Mimic D-Ala-D-Ala; acylate transpeptidase (PBP)"),
         ("Vancomycin", "Binds D-Ala-D-Ala directly; Gram-positive only"),
         ("Cephalosporin gaps", "LAME - Listeria, Atypicals, MRSA, Enterococci"),
         ("Aztreonam", "Gram-negative only; safe in penicillin allergy"),
         ("Ertapenem", "The one carbapenem without Pseudomonas coverage")],
  images=[("fig-abx-targets.jpg", "Antibiotic classes grouped by the bacterial structure each attacks.")],
  sections=[
    S("Mechanism", [
      H("Peptidoglycan is built from sugar chains cross-linked through peptide stems ending in D-Ala-D-Ala. Transpeptidases (penicillin-binding proteins) form those cross-links. The beta-lactam ring is a structural mimic of D-Ala-D-Ala, so the enzyme binds the drug instead of its substrate and is irreversibly acylated."),
      P("Cross-linking stops while autolysins continue degrading the wall, so the cell can no longer resist osmotic pressure and lyses. This is why beta-lactams are bactericidal but only against actively dividing organisms - the basis of the Eagle effect, where very high inocula in stationary phase respond poorly."),
      H("Vancomycin takes a different route to the same pathway: it binds the D-Ala-D-Ala terminus itself, sterically blocking transpeptidation. Because it is a large glycopeptide it cannot cross the Gram-negative outer membrane, so it is Gram-positive only. Resistance (vanA) substitutes D-Ala-D-Lac, dropping affinity about a thousandfold."),
    ]),
    S("Spectrum and generations", [
      H("First-generation cephalosporins (cefazolin, cephalexin) cover PEcK - Proteus mirabilis, E. coli, Klebsiella - plus staphylococci and streptococci. Second generation (cefuroxime, cefoxitin) adds HENS PEcK. Third generation (ceftriaxone, ceftazidime) has strong Gram-negative and CNS penetration. Fourth (cefepime) adds Pseudomonas with better Gram-positive activity. Ceftaroline is the one that binds PBP2a and covers MRSA."),
      H("No cephalosporin covers LAME organisms: Listeria, Atypicals (Mycoplasma, Chlamydia), MRSA (except ceftaroline), and Enterococci. This single mnemonic explains several empiric regimens, including why ampicillin is added for Listeria in meningitis."),
      P("Carbapenems are the broadest beta-lactams and are stable against most beta-lactamases including ESBLs; imipenem is given with cilastatin to block renal dehydropeptidase. Ertapenem lacks antipseudomonal and anti-Acinetobacter activity. Aztreonam is a monobactam active only against aerobic Gram-negative rods, with no cross-reactivity in penicillin allergy."),
    ]),
    S("Resistance and adverse effects", [
      H("Resistance arises by destroying the drug (beta-lactamase, ESBL, carbapenemase), altering the target (PBP2a in MRSA, mosaic PBPs in pneumococcus), or keeping it out (porin loss, efflux). Beta-lactamase inhibitors such as clavulanate, tazobactam, and avibactam restore activity only against the enzyme-mediated mechanism - they do nothing for altered PBPs."),
      P("Beta-lactams cause hypersensitivity (from rash to anaphylaxis), interstitial nephritis, and at high doses seizures; a maculopapular rash with amoxicillin during EBV infection is not a true allergy. Vancomycin causes red man syndrome, a direct mast cell degranulation reaction from rapid infusion that is prevented by slowing the rate, plus nephrotoxicity and ototoxicity."),
    ]),
  ]),

E("protein-synth-abx", "Protein Synthesis Inhibitors", "Principles & Pharmacology",
  "The 30S and 50S agents, their signature toxicities, and why one of them is so useful in toxin-mediated disease.",
  aka=["aminoglycoside", "tetracycline", "macrolide", "clindamycin", "linezolid", "chloramphenicol"],
  keywords=["30S", "50S", "ototoxicity", "nephrotoxicity", "gray baby", "D-test", "QT prolongation"],
  quick=[("30S", "Aminoglycosides (bactericidal), Tetracyclines (bacteriostatic)"),
         ("50S", "Chloramphenicol, Clindamycin, linEzolid, macroLides, Streptogramins"),
         ("Mnemonic", "'Buy AT 30, CCEL at 50'"),
         ("Aminoglycosides", "Need oxygen for uptake - useless against anaerobes"),
         ("Linezolid", "Serotonin syndrome risk; reversible myelosuppression")],
  images=[("fig-abx-targets.jpg", "Where each antibiotic class acts.")],
  sections=[
    S("30S agents", [
      H("Aminoglycosides (gentamicin, tobramycin, amikacin) bind the 30S subunit, cause misreading of mRNA, and block initiation. They are bactericidal and concentration-dependent, which is why once-daily dosing is both effective and less toxic - it maximizes peak concentration and exploits the post-antibiotic effect while giving tubular cells a drug-free interval."),
      P("Their uptake across the bacterial membrane requires an oxygen-dependent transport system, so they have no activity against anaerobes and cannot work alone against enterococci - the basis of beta-lactam synergy. Toxicities are nephrotoxicity (usually reversible acute tubular necrosis), ototoxicity (often irreversible, and worsened by loop diuretics), neuromuscular blockade, and teratogenicity."),
      H("Tetracyclines (doxycycline, minocycline) block aminoacyl-tRNA entry to the 30S A site. Divalent cations - milk, antacids, iron, calcium - chelate them and block absorption. They deposit in growing bone and teeth, causing discoloration and growth inhibition, so they are avoided under 8 years and in pregnancy, and they cause photosensitivity. Doxycycline is the exception that is safe in renal failure because it is eliminated in feces."),
    ]),
    S("50S agents", [
      H("Macrolides (azithromycin, clarithromycin, erythromycin) block translocation. They cause QT prolongation, gastrointestinal upset (erythromycin is a motilin agonist), and hepatitis, and clarithromycin and erythromycin are CYP450 inhibitors. Resistance is by erm-mediated methylation of 23S rRNA or by efflux."),
      H("Clindamycin blocks translocation at the 50S subunit and covers anaerobes above the diaphragm and Gram-positives. It is uniquely useful in toxic shock and necrotizing fasciitis because it halts toxin synthesis regardless of growth phase, unlike beta-lactams. Its signature adverse effect is C. difficile colitis."),
      P("Linezolid binds the 50S subunit and prevents formation of the initiation complex - a mechanism no other drug shares, so cross-resistance is rare. It covers MRSA and VRE, is fully orally bioavailable, and causes reversible myelosuppression, peripheral and optic neuropathy with prolonged use, and serotonin syndrome with serotonergic drugs because it is a weak MAO inhibitor."),
      P("Chloramphenicol inhibits peptidyl transferase and is rarely used now because of dose-dependent reversible marrow suppression, idiosyncratic irreversible aplastic anemia, and gray baby syndrome in neonates, who lack UDP-glucuronyl transferase."),
    ]),
  ]),

E("other-abx", "Folate, DNA & Membrane Antibiotics", "Principles & Pharmacology",
  "Sulfonamides and trimethoprim, fluoroquinolones, metronidazole, and the agents of last resort.",
  aka=["TMP-SMX", "ciprofloxacin", "metronidazole", "nitrofurantoin", "daptomycin", "polymyxin", "rifampin"],
  keywords=["folate", "DNA gyrase", "tendon rupture", "disulfiram", "G6PD", "surfactant"],
  quick=[("Sulfonamides", "Block dihydropteroate synthase (PABA analog)"),
         ("Trimethoprim", "Blocks dihydrofolate reductase - sequential blockade"),
         ("Fluoroquinolones", "Block DNA gyrase (topo II) and topo IV"),
         ("Metronidazole", "Reduced to radicals in anaerobes - damages DNA"),
         ("Daptomycin", "Depolarizes membrane; INACTIVATED by surfactant")],
  sections=[
    S("Folate antagonists", [
      H("Sulfamethoxazole is a structural analog of PABA and inhibits dihydropteroate synthase; trimethoprim inhibits dihydrofolate reductase. Blocking two sequential steps in one pathway is synergistic and bactericidal. Bacteria must synthesize folate de novo while humans take it up from the diet, which is the basis of selectivity."),
      P("TMP-SMX causes hypersensitivity reactions including Stevens-Johnson syndrome, hemolysis in G6PD deficiency, hyperkalemia (trimethoprim blocks the epithelial sodium channel, an amiloride-like effect), a rise in creatinine without a fall in GFR (it blocks tubular creatinine secretion), and bone marrow suppression relieved by leucovorin. It is the drug of choice for Pneumocystis and Nocardia."),
    ]),
    S("Fluoroquinolones and metronidazole", [
      H("Fluoroquinolones inhibit DNA gyrase (topoisomerase II) in Gram-negatives and topoisomerase IV in Gram-positives, preventing supercoiling and relaxation of DNA. They cause tendinitis and tendon rupture (especially with steroids and over 60), QT prolongation, peripheral neuropathy, CNS effects, and aortic dissection, and are avoided in pregnancy and children when alternatives exist."),
      H("Metronidazole is reduced by ferredoxin-like systems present only in anaerobes and certain protozoa, generating free radicals that damage DNA - which is precisely why it is selective for anaerobes, Trichomonas, Giardia, and Entamoeba. It causes a disulfiram-like reaction with alcohol, metallic taste, and peripheral neuropathy with prolonged use."),
    ]),
    S("Agents with narrow niches", [
      H("Daptomycin is a lipopeptide that inserts into the Gram-positive membrane and depolarizes it. It is inactivated by pulmonary surfactant, so it must never be used for pneumonia, and it causes myopathy with a raised creatine kinase."),
      P("Nitrofurantoin is concentrated in urine and used only for cystitis, never pyelonephritis; it causes pulmonary fibrosis with chronic use and hemolysis in G6PD deficiency. Polymyxins (colistin) disrupt the Gram-negative outer membrane like a detergent and are reserved for multidrug-resistant organisms because of nephrotoxicity and neurotoxicity. Fosfomycin blocks the very first committed step of peptidoglycan synthesis (MurA) and is a single-dose option for cystitis."),
      H("Rifampin inhibits DNA-dependent RNA polymerase, penetrates biofilm and abscesses well, and induces CYP450 potently. Resistance emerges within days through a single rpoB mutation, which is why it is never used as monotherapy except for prophylaxis of meningococcal or Hib contacts."),
    ]),
  ]),

E("antifungal-antiviral", "Antifungals & Antivirals", "Principles & Pharmacology",
  "Ergosterol, glucan, and nucleic acid: the small number of targets these drugs have, and what that costs.",
  aka=["amphotericin", "azole", "echinocandin", "flucytosine", "acyclovir", "oseltamivir"],
  keywords=["ergosterol", "glucan synthase", "14-alpha-demethylase", "squalene epoxidase", "thymidine kinase"],
  quick=[("Amphotericin B", "Binds ergosterol, forms pores; nephrotoxic, K+/Mg2+ wasting"),
         ("Azoles", "Inhibit 14-alpha-demethylase; CYP450 inhibitors"),
         ("Echinocandins", "Inhibit beta-1,3-glucan synthase; very well tolerated"),
         ("Flucytosine", "Converted to 5-FU; marrow suppression"),
         ("Terbinafine", "Inhibits squalene epoxidase")],
  sections=[
    S("Antifungals", [
      H("Fungal membranes use ergosterol where human membranes use cholesterol, and fungal walls contain beta-glucan and chitin, which humans lack entirely. Those two differences carry almost the whole antifungal armamentarium - which is why the echinocandins, targeting a structure with no human counterpart, are the best tolerated."),
      P("Amphotericin B binds ergosterol directly and forms membrane pores. Because it has some affinity for cholesterol, it causes infusion reactions with fever and rigors, dose-dependent nephrotoxicity with distal tubular potassium and magnesium wasting, and anemia. Sodium loading, electrolyte repletion, and liposomal formulations reduce the renal injury."),
      H("Azoles inhibit lanosterol 14-alpha-demethylase, blocking ergosterol synthesis. Because that enzyme is a cytochrome P450, azoles inhibit human CYP3A4 as well, raising levels of tacrolimus, warfarin, and statins. Voriconazole causes transient visual disturbance and photosensitivity; itraconazole is negatively inotropic and avoided in heart failure."),
      P("Flucytosine is deaminated by fungal cytosine deaminase into 5-fluorouracil, disrupting nucleic acid synthesis; human cells lack that enzyme. It is used with amphotericin for cryptococcal meningitis and causes marrow suppression. Griseofulvin binds microtubules and deposits in keratin; terbinafine inhibits squalene epoxidase."),
    ]),
    S("Antivirals", [
      H("Acyclovir is selectively activated by viral thymidine kinase and then inhibits viral DNA polymerase with chain termination. Resistance is usually loss of thymidine kinase, so resistant HSV and VZV are treated with foscarnet or cidofovir, which inhibit the polymerase directly and require no viral activation."),
      P("Ganciclovir is the CMV analog and causes marrow suppression; foscarnet is a pyrophosphate analog causing nephrotoxicity with hypocalcemia, hypomagnesemia, and seizures; cidofovir is nephrotoxic and given with probenecid and hydration."),
      H("Neuraminidase inhibitors (oseltamivir, zanamivir) prevent release of progeny influenza virions; baloxavir inhibits the viral cap-dependent endonuclease. For HIV, drug class is readable from the suffix: -gravir integrase, -navir protease, -virine NNRTI, -viroc CCR5 antagonist. Hepatitis C is cured with -previr, -asvir, and -buvir combinations."),
    ]),
  ]),

E("syndromes", "Infections by System & Host", "Principles & Pharmacology",
  "The cross-cutting tables: meningitis by age, pneumonia by host, diarrhea by pattern, and infections by immune defect.",
  aka=["meningitis", "pneumonia", "UTI", "diarrhea", "TORCH", "immunodeficiency"],
  keywords=["CSF", "empiric therapy", "neutropenia", "asplenia", "complement", "vaccines"],
  quick=[("Neonatal meningitis", "GBS, E. coli, Listeria"),
         ("Meningitis 2-50", "S. pneumoniae, N. meningitidis"),
         ("Meningitis >50", "S. pneumoniae, Listeria, Gram-negatives"),
         ("Bacterial CSF", "High neutrophils, LOW glucose, high protein"),
         ("Viral CSF", "Lymphocytes, NORMAL glucose, mildly high protein")],
  images=[("nmen-csf.jpg", "Purulent CSF in bacterial meningitis."),
          ("lobar-pneumonia.jpg", "Lobar consolidation in pneumococcal pneumonia.")],
  sections=[
    S("Meningitis and CSF", [
      H("Empiric therapy tracks the age-based organisms: neonates get ampicillin plus cefotaxime or gentamicin (covering GBS, E. coli, Listeria); children and adults get vancomycin plus ceftriaxone; over 50 or immunocompromised adds ampicillin for Listeria. Dexamethasone before or with the first dose reduces hearing loss and mortality in pneumococcal meningitis."),
      H("CSF patterns: bacterial gives high opening pressure, hundreds to thousands of neutrophils, low glucose (under two-thirds of serum), and high protein. Viral gives lymphocytes with normal glucose. Fungal and tuberculous give lymphocytes with low glucose and very high protein - and TB classically shows a high opening pressure with basilar involvement."),
      P("Low CSF glucose reflects consumption by both organisms and neutrophils plus impaired glucose transport across inflamed meninges, which is why it separates bacterial and fungal from viral causes so reliably."),
    ]),
    S("Pneumonia and diarrhea by pattern", [
      H("Pneumonia by host: typical community-acquired is pneumococcus; walking pneumonia in a young adult is Mycoplasma; alcohol use disorder with currant-jelly sputum is Klebsiella; post-influenza cavitary disease is S. aureus; cystic fibrosis is Pseudomonas; HIV with CD4 under 200 and ground-glass opacities is Pneumocystis; and aspiration gives anaerobes in dependent segments."),
      H("Bloody, inflammatory diarrhea: Shigella, EHEC, Campylobacter, Salmonella, EIEC, Yersinia, and Entamoeba. Watery, non-inflammatory diarrhea: Vibrio cholerae, ETEC, viruses, Giardia, and Cryptosporidium. The key discriminator is whether the organism invades or acts through a secretory toxin."),
      P("Food poisoning by incubation: 1-6 hours means preformed toxin (S. aureus, B. cereus emetic); 8-16 hours means toxin produced in the gut (C. perfringens, B. cereus diarrheal); over 18 hours means infection (Salmonella, Campylobacter, Shigella, EHEC)."),
    ]),
    S("Infections by immune defect", [
      H("Neutropenia or neutrophil dysfunction gives bacterial and fungal infection: S. aureus, Pseudomonas, Candida, Aspergillus. Chronic granulomatous disease specifically gives catalase-positive organisms, because those destroy the hydrogen peroxide the defective neutrophil would otherwise borrow."),
      H("T-cell defects give intracellular and opportunistic pathogens: mycobacteria, Listeria, Salmonella, fungi, PCP, and the herpesviruses. B-cell and antibody defects give encapsulated bacteria and enteroviruses. Terminal complement (C5-C9) deficiency gives recurrent Neisseria. Asplenia gives encapsulated organisms - pneumococcus, H. influenzae type b, meningococcus."),
      P("Encapsulated organisms worth grouping: Streptococcus pneumoniae, Haemophilus influenzae type b, Neisseria meningitidis, Klebsiella pneumoniae, E. coli, Salmonella, group B strep, and Cryptococcus neoformans. All are opsonized by antibody and complement and cleared in the spleen, which is why the same list recurs in asplenia, antibody deficiency, and complement deficiency."),
    ]),
    S("Congenital infection", [
      H("TORCH: Toxoplasma (chorioretinitis, hydrocephalus, diffuse intracranial calcifications), Other (syphilis, listeria, parvovirus B19), Rubella (cataracts, patent ductus arteriosus, deafness, 'blueberry muffin' rash), CMV (microcephaly, periventricular calcifications, sensorineural hearing loss), and HSV (skin-eye-mouth, CNS, or disseminated disease acquired at delivery)."),
      P("The two calcification patterns are worth fixing firmly: toxoplasmosis is diffuse and scattered, CMV is periventricular. Both cause chorioretinitis, but hydrocephalus points to toxoplasmosis and microcephaly to CMV."),
    ]),
  ]),

E("vaccines", "Vaccines & Sterilization", "Principles & Pharmacology",
  "Live versus inactivated, conjugate versus polysaccharide, and what actually kills spores.",
  aka=["vaccination", "immunization", "toxoid", "live attenuated", "autoclave"],
  keywords=["MMR", "varicella", "BCG", "conjugate", "passive immunization", "cold chain"],
  quick=[("Live attenuated", "MMR, varicella, zoster (old), rotavirus, oral polio, BCG, yellow fever, intranasal flu"),
         ("Contraindicated", "Live vaccines in pregnancy and severe immunosuppression"),
         ("Toxoid", "Tetanus, diphtheria - antibody against the toxin, not the organism"),
         ("Conjugate", "Recruits T-cell help; works under age 2"),
         ("Autoclave", "121°C for 15 min - required to kill spores")],
  sections=[
    S("Vaccine types", [
      H("Live attenuated vaccines produce strong, durable cellular and humoral immunity, often after a single dose, but carry a small risk of reversion and are contraindicated in pregnancy and severe immunosuppression. Inactivated and subunit vaccines are safe in those groups but produce mainly humoral immunity and need boosters."),
      H("Pure polysaccharide antigens are T-independent: they produce IgM without class switching or memory, and children under two respond poorly because the marginal zone B-cell compartment is immature. Conjugating the polysaccharide to a carrier protein lets helper T cells recognize carrier peptides and provide help to polysaccharide-specific B cells, giving IgG, memory, and protection in infants - plus reduced nasopharyngeal carriage and herd effects."),
      P("Passive immunization gives preformed antibody for immediate but temporary protection, and is used when there is no time to mount a response: tetanus, rabies, hepatitis B, varicella, botulism, and RSV prophylaxis. For rabies and hepatitis B, passive and active immunization are given together at different sites."),
    ]),
    S("Sterilization", [
      H("Endospores are the benchmark: they survive boiling, drying, alcohol, and many disinfectants because of a dehydrated core stabilized by calcium dipicolinate and protective small acid-soluble proteins. Autoclaving at 121°C for 15 minutes or ethylene oxide is required. Alcohol hand gel does not kill C. difficile spores or non-enveloped viruses such as norovirus - soap-and-water washing and bleach are needed."),
      P("Enveloped viruses are fragile: alcohol, detergents, drying, and heat destroy the lipid envelope, so they need close contact or body fluids to spread. Non-enveloped viruses are stable in the environment and on surfaces, which is why they transmit by the fecal-oral route and via fomites."),
    ]),
  ]),
]
