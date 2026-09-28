"""Teaching figures and step-by-step walkthroughs attached to explanations.

Every figure is openly licensed (public domain, CC0, CC BY, or CC BY-SA) and its source,
author, and licence are shown under the image on the page, from credits.json.
"""
from qcore import F

R = {
# ---------------- bacterial structure & genetics ----------------
"Gram-positive cell wall": dict(
  fig=F("fig-gram-wall.jpg",
        "Envelope layers. Top, Gram-negative: (1) inner membrane, (2) thin peptidoglycan, (3) outer membrane, with lipoprotein (6), porin (7), lipoteichoic-type anchor (8), and a transport channel (9). Bottom, Gram-positive: (1) a single membrane under a thick multilayer peptidoglycan wall (2) threaded by teichoic acids (green, 5) and lipoteichoic acid (4)."),
  steps=["Gram-positive cells have one membrane and a thick peptidoglycan wall, so the crystal violet-iodine complex is trapped when alcohol is applied, and the cell stays purple.",
         "Teichoic and lipoteichoic acids run through that thick wall; they are the molecules that signal through TLR2 and drive cytokine release.",
         "Gram-negative cells have only a thin peptidoglycan layer, sitting in the periplasmic space between two membranes.",
         "Alcohol dissolves the lipid-rich outer membrane, the dye complex washes out, and the cell takes up the pink safranin counterstain.",
         "The same outer membrane carries LPS and porins, which explains endotoxin and several antibiotic-resistance mechanisms."]),

"Endotoxin": dict(
  fig=F("fig-lps.jpg",
        "Lipopolysaccharide, drawn from the membrane outward: lipid A anchored in the outer leaflet, then inner and outer core sugars, then the long repeating O antigen."),
  steps=["Lipid A is the innermost part, embedded in the outer membrane, and it is the toxic portion of the molecule.",
         "When bacteria are lysed or divide, LPS is shed and lipid A is delivered to host cells by LPS-binding protein.",
         "Lipid A engages CD14 and the TLR4/MD-2 complex on macrophages.",
         "Macrophages release IL-1, IL-6, and TNF-alpha, producing fever, vasodilation, and hypotension.",
         "Complement activation (C3a, C5a) and tissue factor expression follow, which is how endotoxin drives DIC.",
         "The outer O antigen is highly variable and is what serotyping detects; it is not the toxic part."]),

"Conjugation": dict(
  fig=F("fig-conjugation.jpg",
        "Bacterial conjugation. (1) The F-plasmid-bearing donor extends a pilus; (2) the pilus contacts the recipient and retracts, pulling the cells together; (3) the relaxosome nicks the plasmid and one strand is transferred while DNA polymerase copies it; (4) both cells now carry the plasmid and can act as donors."),
  steps=["The donor cell carries the F (fertility) plasmid and uses it to build a sex pilus.",
         "The pilus attaches to a recipient and retracts, bringing the two cells into direct contact.",
         "A relaxase nicks one plasmid strand, and that single strand is passed through the mating bridge.",
         "Each cell synthesizes the complementary strand, so both end up with a complete plasmid.",
         "The recipient is now itself a donor, which is why resistance plasmids sweep through a population so quickly.",
         "Because DNA never enters the surrounding medium, DNase does not block conjugation, unlike transformation."]),

# ---------------- antibiotics ----------------
"Protein synthesis: subunit targets": dict(
  fig=F("fig-abx-targets.jpg",
        "Antibiotic classes grouped by the bacterial structure each one attacks: cell wall synthesis, cell membrane, DNA gyrase, RNA synthesis, folate synthesis, and the ribosome."),
  steps=["Locate the ribosome in the diagram: protein synthesis inhibitors act here, and they split by subunit.",
         "The 30S subunit is the target of aminoglycosides (misreading, blocked initiation) and tetracyclines (blocked aminoacyl-tRNA entry).",
         "The 50S subunit is the target of chloramphenicol, clindamycin, linezolid, macrolides, and streptogramins.",
         "Mnemonic: 'Buy AT 30, CCEL at 50' - Aminoglycosides and Tetracyclines at 30S; Chloramphenicol, Clindamycin, Erythromycin (macrolides), and Linezolid at 50S.",
         "Every other arrow in the figure marks a different target class, which is why combination regimens can attack several pathways at once."]),

"Penicillins: mechanism": dict(
  fig=F("fig-abx-targets.jpg",
        "Antibiotic targets in a bacterial cell. Beta-lactams sit in the 'cell wall synthesis inhibitors' group at the top left, alongside glycopeptides such as vancomycin."),
  steps=["Peptidoglycan is built from repeating sugar chains cross-linked through short peptide stems ending in D-Ala-D-Ala.",
         "Transpeptidases, also called penicillin-binding proteins, form those cross-links and give the wall its strength.",
         "The beta-lactam ring is a structural mimic of D-Ala-D-Ala, so the enzyme binds the drug instead of its true substrate.",
         "The drug acylates the active site permanently, so cross-linking stops while wall breakdown by autolysins continues.",
         "The weakened wall cannot resist osmotic pressure and the cell lyses, which is why beta-lactams work best on dividing bacteria.",
         "Resistance follows from destroying the drug (beta-lactamase), changing the target (PBP2a in MRSA), or keeping it out (porin loss)."]),

# ---------------- toxins & exotoxin mechanism ----------------
"Vibrio cholerae: mechanism": dict(
  steps=["Cholera toxin is an AB5 toxin: five B subunits bind GM1 ganglioside on the enterocyte surface.",
         "The A subunit is taken into the cell and ADP-ribosylates the alpha subunit of Gs.",
         "Modified Gs can no longer hydrolyze GTP, so it stays locked in its active form.",
         "Adenylyl cyclase runs continuously and intracellular cAMP rises sharply.",
         "Protein kinase A phosphorylates CFTR, which pumps chloride into the lumen, with sodium and water following.",
         "The result is massive watery diarrhea with no invasion, so there is no fever, blood, or inflammatory infiltrate."]),

# ---------------- viruses ----------------
"HIV: entry & CCR5": dict(
  fig=F("fig-hiv-cycle.jpg",
        "HIV replication cycle: gp120 attaches to CD4 and a co-receptor, gp41 drives fusion, reverse transcriptase copies RNA into DNA, integrase inserts it into host DNA, and protease cleaves the polyprotein during assembly and release."),
  steps=["gp120 binds CD4 on the target cell, which changes its shape and exposes the co-receptor binding site.",
         "gp120 then binds a chemokine co-receptor: CCR5 on macrophages and memory T cells early in infection, or CXCR4 later.",
         "gp41 inserts into the host membrane and pulls the two membranes together so the core enters the cell.",
         "Reverse transcriptase copies the RNA genome into DNA, with no proofreading, which is the source of rapid mutation.",
         "Integrase splices the provirus into host DNA, creating the latent reservoir that prevents cure.",
         "Protease cleaves the Gag-Pol polyprotein during budding; without this step the released virions stay immature and non-infectious.",
         "Each step is a drug target, which is why a CCR5-Delta32 deletion blocks entry of R5 strains entirely."]),

"HIV: genes & proteins": dict(
  fig=F("fig-hiv-cycle.jpg",
        "The labelled virion at the upper left shows the products of the three structural genes: env makes gp120 and gp41, gag makes the capsid and matrix, and pol makes reverse transcriptase, integrase, and protease."),
  steps=["env encodes gp160, which host protease cuts into gp120 (attachment) and gp41 (fusion).",
         "gag encodes the structural core: p24 capsid, p17 matrix, and nucleocapsid proteins.",
         "pol encodes the three enzymes packaged inside the virion: reverse transcriptase, integrase, and protease.",
         "Regulatory genes add control: tat boosts transcription, rev exports unspliced RNA, and nef lowers MHC I and CD4 on the cell surface.",
         "p24 is the antigen detected by 4th-generation screening assays before antibodies appear."]),

"Influenza: antigenic shift": dict(
  fig=F("fig-flu-shift.jpg",
        "Antigenic shift by reassortment: a cell co-infected with an avian strain and a human strain packages a mixture of the eight genome segments, producing a new strain with avian surface proteins and human-adapted internal genes."),
  steps=["Influenza A has a segmented genome of eight separate RNA pieces.",
         "If two different strains infect the same cell, usually in pigs or birds, the segments mix freely during packaging.",
         "A new virus can emerge carrying a hemagglutinin the human population has never seen.",
         "Because there is no pre-existing immunity, the new subtype can spread worldwide as a pandemic.",
         "Antigenic drift is the slower alternative: point mutations accumulate in HA and NA, causing seasonal epidemics and requiring yearly vaccine updates.",
         "Only segmented viruses can reassort, which is why shift happens with influenza but not with measles or rabies."]),

"Herpesvirus structure": dict(
  fig=F("fig-hsv-latency.jpg",
        "HSV-1 replication: the virion binds and enters, the nucleocapsid travels to the nucleus and injects its DNA, and genes are transcribed in ordered waves - immediate-early (alpha), early (beta), then late (gamma) - before assembly and nuclear budding."),
  steps=["The enveloped virion attaches to the cell surface and fuses, releasing the nucleocapsid into the cytoplasm.",
         "The capsid is carried to a nuclear pore and injects its linear double-stranded DNA into the nucleus.",
         "Immediate-early (alpha) genes are transcribed first and make regulatory proteins.",
         "Early (beta) genes follow and make the replication machinery, including viral thymidine kinase - the enzyme acyclovir needs.",
         "Late (gamma) genes make the structural proteins after DNA replication begins.",
         "New capsids assemble in the nucleus and bud through the nuclear membrane, which is where herpesviruses get their envelope.",
         "In sensory neurons the cycle can stall instead, leaving the genome as a quiet episome - latency, from which reactivation occurs."]),

# ---------------- mycobacteria ----------------
"TB: granuloma immunology": dict(
  fig=F("fig-tb-latency.jpg",
        "Tuberculosis after inhalation: bacilli reach the alveoli, dendritic cells carry antigen to lymph nodes and activate T cells, and the granuloma that forms either clears the organism, contains it as latent infection, or breaks down into active, transmissible disease."),
  steps=["Droplet nuclei are inhaled and reach the alveoli, where macrophages take up the bacilli.",
         "M. tuberculosis blocks phagolysosome fusion and survives inside the macrophage.",
         "Dendritic cells carry antigen to draining lymph nodes and prime CD4+ T cells.",
         "Infected macrophages secrete IL-12, which drives those T cells down the Th1 pathway.",
         "Th1 cells release IFN-gamma, which activates macrophages into epithelioid cells and Langhans giant cells.",
         "TNF-alpha holds the granuloma together; the center becomes caseous necrosis, and the organism is contained but not always killed.",
         "Blocking TNF with infliximab or adalimumab dismantles that structure, which is why latent TB is screened for and treated before these drugs are started."]),

"TB: primary vs reactivation": dict(
  fig=F("fig-tb-latency.jpg",
        "The three outcomes after infection: elimination with recovery, a stable granuloma holding latent infection, or breakdown of the granuloma into active tuberculosis that can be transmitted again."),
  steps=["Inhaled bacilli land in the well-ventilated lower and middle lung zones, forming the Ghon focus.",
         "Bacilli drain to hilar nodes; focus plus node make the Ghon complex, which usually calcifies.",
         "Most people contain the infection inside granulomas, which is latent infection with no symptoms and no transmission.",
         "If cell-mediated immunity later weakens, from HIV, TNF inhibitors, steroids, diabetes, or age, the granuloma breaks down.",
         "Reactivation favors the upper lobe apices because M. tuberculosis is an obligate aerobe and oxygen tension is highest there.",
         "Cavities form, connect to airways, and release large numbers of organisms, making the patient infectious again."]),

# ---------------- protozoa ----------------
"Malaria: life cycle": dict(
  fig=F("fig-malaria-cycle.jpg",
        "Plasmodium life cycle: the mosquito injects sporozoites that infect liver cells, merozoites are released into the blood and cycle through red cells, and gametocytes taken up in a blood meal complete sexual development in the mosquito."),
  steps=["A female Anopheles mosquito bites and injects sporozoites from its salivary glands.",
         "Sporozoites travel in the blood to the liver and infect hepatocytes, multiplying silently for 1-2 weeks.",
         "In P. vivax and P. ovale some parasites stay dormant here as hypnozoites, the cause of later relapse.",
         "The liver cells rupture and release merozoites, which invade red blood cells.",
         "Inside red cells the parasite cycles through ring, trophozoite, and schizont stages, then bursts the cell - synchronized lysis is what produces the fever pattern.",
         "Some parasites become gametocytes; a feeding mosquito takes them up, and sexual reproduction completes the cycle in the insect gut.",
         "This is why blood-stage drugs clear symptoms but only primaquine or tafenoquine kills hypnozoites and prevents relapse."]),

"Toxoplasma: congenital": dict(
  fig=F("fig-toxo-cycle.jpg",
        "Toxoplasma gondii: cats shed oocysts in feces, and humans are infected by swallowing oocysts or by eating tissue cysts in undercooked meat. Tachyzoites spread through tissues, then convert to slow bradyzoite cysts in brain and muscle."),
  steps=["Cats are the definitive host, the only animal in which the sexual cycle completes, and they shed oocysts in feces.",
         "Humans are infected two ways: swallowing oocysts from cat litter, soil, or unwashed produce, or eating tissue cysts in undercooked meat.",
         "In the gut the parasite is released and converts to rapidly dividing tachyzoites.",
         "Tachyzoites spread through the bloodstream and can cross the placenta if the mother is infected for the first time during pregnancy.",
         "In the fetus they damage brain and retina, producing the triad of chorioretinitis, hydrocephalus, and diffuse intracranial calcifications.",
         "In immunocompetent hosts tachyzoites convert to bradyzoites inside tissue cysts, which persist for life.",
         "If cell-mediated immunity later fails, as at CD4 counts under 100, those cysts reactivate and cause ring-enhancing brain lesions."]),

"Chagas disease": dict(
  fig=F("fig-tcruzi-cycle.jpg",
        "Trypanosoma cruzi: the reduviid bug deposits infected feces while feeding, trypomastigotes enter through the wound or conjunctiva, become intracellular amastigotes that multiply and burst the cell, and circulating trypomastigotes are taken up at the next blood meal."),
  steps=["A triatomine ('kissing') bug feeds at night, typically near the face, and defecates on the skin.",
         "Scratching rubs infected feces into the bite wound or the conjunctiva - not the bite itself.",
         "Unilateral periorbital swelling at the entry site is the Romana sign of acute infection.",
         "Trypomastigotes enter host cells and transform into amastigotes, which multiply and rupture the cell.",
         "Over decades the parasite destroys autonomic ganglia in heart and gut.",
         "That denervation produces dilated cardiomyopathy with apical aneurysm and arrhythmias, megaesophagus, and megacolon.",
         "Benznidazole or nifurtimox helps in acute and early infection but cannot reverse established organ damage."]),

"Visceral leishmaniasis": dict(
  fig=F("fig-leish-cycle.jpg",
        "Leishmania: a sandfly injects promastigotes, macrophages take them up, and inside the macrophage they become amastigotes that multiply until the cell ruptures. Another sandfly bite returns the parasite to the insect."),
  steps=["A female sandfly bites and injects promastigotes into the skin.",
         "Macrophages phagocytose them, but the parasite survives inside the phagolysosome.",
         "Inside the cell the promastigote becomes an amastigote - a small oval form with a nucleus and a rod-shaped kinetoplast.",
         "Amastigotes multiply until the macrophage bursts, and neighboring macrophages are infected.",
         "In visceral disease the parasite spreads to spleen, liver, and bone marrow, causing massive splenomegaly and pancytopenia.",
         "In cutaneous disease it stays at the bite site and produces a slow, painless ulcer with raised edges.",
         "The kinetoplast is the feature that distinguishes amastigotes from Histoplasma yeasts, which also sit inside macrophages."]),

"Giardia": dict(
  fig=F("fig-giardia-cycle.jpg",
        "Giardia: chlorine-resistant cysts are swallowed in contaminated water, excyst in the small intestine into trophozoites that attach to the duodenal wall, and new cysts are passed in stool."),
  steps=["Cysts are swallowed in untreated stream water, or passed person to person in daycare settings.",
         "The cyst wall resists chlorination, which is why filtration or boiling is required.",
         "Stomach acid triggers excystation in the duodenum, releasing trophozoites.",
         "Trophozoites attach to the mucosa with a ventral sucking disk but do not invade, so there is no blood or fever.",
         "Coating the absorptive surface blocks fat absorption, producing greasy, foul-smelling, floating stools and bloating.",
         "Some trophozoites encyst again and pass in stool, continuing the cycle.",
         "Secretory IgA normally limits attachment, so IgA deficiency and hypogammaglobulinemia cause chronic infection."]),

"Entamoeba histolytica": dict(
  fig=F("fig-entamoeba-cycle.jpg",
        "Entamoeba histolytica: cysts are swallowed, excyst in the intestine, and trophozoites either live in the lumen or invade the colonic wall, from which they can travel by the portal vein to the liver."),
  steps=["Cysts are ingested from fecally contaminated food or water.",
         "Excystation in the small intestine releases trophozoites that colonize the colon.",
         "Most remain luminal commensals, but pathogenic strains invade the mucosa.",
         "Invasion produces flask-shaped ulcers, causing bloody diarrhea with cramps.",
         "Trophozoites that eat red blood cells are the finding specific for E. histolytica rather than harmless E. dispar.",
         "Organisms entering portal venules travel to the liver and form an abscess with 'anchovy paste' contents, often weeks later and often with negative stool studies.",
         "Treatment needs two drugs: metronidazole for invasive tissue forms, then paromomycin to clear luminal cysts."]),

"Babesia": dict(
  fig=F("fig-babesia-cycle.jpg",
        "Babesia microti: the Ixodes tick injects sporozoites that invade red blood cells directly, where they divide and sometimes form the tetrad 'Maltese cross'. There is no liver stage."),
  steps=["An Ixodes tick, usually a nymph, injects sporozoites while feeding.",
         "Unlike malaria, the parasite goes straight into red blood cells with no liver phase.",
         "Inside red cells it divides, producing rings that closely resemble Plasmodium falciparum.",
         "Four daughter cells arranged as a tetrad give the 'Maltese cross' that is diagnostic when seen.",
         "Red cell rupture causes hemolytic anemia, jaundice, and dark urine, which is severe in asplenic or elderly patients.",
         "Babesia makes no hemozoin pigment, and there is no travel history - two ways to separate it from malaria.",
         "The same tick carries Borrelia burgdorferi and Anaplasma, so co-infection is common."]),

# ---------------- helminths ----------------
"Enterobius": dict(
  fig=F("fig-pinworm-cycle.jpg",
        "Enterobius vermicularis: (1) eggs on perianal skin are swallowed, (2) larvae hatch in the small intestine, (3-5) adults mature in the colon, and gravid females migrate at night to lay eggs on the perianal skin. 'i' marks the infective stage and 'd' the diagnostic stage."),
  steps=["Eggs are swallowed from contaminated fingers, bedding, or clothing.",
         "Larvae hatch in the small intestine and mature into adults in the colon.",
         "At night the gravid female migrates out to the perianal skin and deposits eggs.",
         "The eggs cause intense itching; scratching loads the fingers and leads to autoinfection and household spread.",
         "Eggs become infective within hours and survive on surfaces for days.",
         "They are collected with the morning tape test, not by stool examination, because they are laid outside the gut.",
         "Treatment is albendazole, mebendazole, or pyrantel for the whole household, repeated at two weeks to kill worms that hatched after the first dose."]),

"Ascaris": dict(
  fig=F("fig-ascaris-cycle.jpg",
        "Ascaris lumbricoides: swallowed eggs hatch in the intestine, larvae cross into the bloodstream and travel through the lungs, are coughed up and swallowed, then mature into adults in the small intestine."),
  steps=["Eggs are swallowed from soil or produce contaminated with human feces.",
         "Larvae hatch in the small intestine and penetrate the gut wall into the portal circulation.",
         "They reach the lungs and break into the alveoli, causing cough, wheeze, eosinophilia, and fleeting infiltrates - Loffler syndrome.",
         "Larvae climb the bronchial tree to the throat and are swallowed a second time.",
         "Back in the small intestine they mature into large adult worms and lay eggs that pass in stool.",
         "Heavy worm burdens cause intestinal obstruction, and migrating adults can block the bile duct.",
         "Treat with albendazole or mebendazole; the lung phase explains why symptoms can precede any stool findings."]),

"Hookworm": dict(
  fig=F("fig-hookworm-cycle.jpg",
        "Hookworm: filariform larvae in soil penetrate skin, travel through the bloodstream to the lungs, are coughed up and swallowed, and attach to the small intestinal mucosa where they feed on blood."),
  steps=["Filariform larvae in warm, moist soil penetrate bare skin, typically on the feet, causing local itching known as ground itch.",
         "Larvae enter the bloodstream and are carried to the lungs.",
         "They break into the alveoli, are coughed up, and are swallowed.",
         "In the small intestine they mature and attach to the mucosa with cutting plates or teeth.",
         "Each worm sucks blood continuously and causes ongoing occult blood loss.",
         "Chronic loss depletes iron stores, producing microcytic hypochromic anemia with eosinophilia.",
         "Treatment is albendazole or mebendazole plus iron replacement; dog and cat hookworms instead cause creeping cutaneous larva migrans."]),

"Strongyloides: hyperinfection": dict(
  fig=F("fig-strongy-cycle.jpg",
        "Strongyloides stercoralis: skin-penetrating larvae migrate through lungs to the gut, and unlike other nematodes, larvae can mature inside the host and reinvade through the bowel wall or perianal skin - autoinfection."),
  steps=["Filariform larvae penetrate skin, travel through the lungs, and mature in the duodenum.",
         "Females lay eggs that hatch in the gut into rhabditiform larvae, which normally pass in stool.",
         "Crucially, some larvae mature into the infective filariform stage while still inside the host.",
         "These reinvade through the colonic wall or perianal skin, so the infection sustains itself for decades without re-exposure.",
         "Corticosteroids and HTLV-1 infection remove the immune brake on this cycle, and larval numbers explode.",
         "Larvae disseminate to lungs, brain, and other organs, carrying gut bacteria with them and causing Gram-negative sepsis or meningitis.",
         "This is why patients from endemic areas are screened with serology and treated with ivermectin before starting steroids."]),

"Taenia solium: transmission": dict(
  fig=F("fig-taenia-cycle.jpg",
        "Taenia solium has two routes. Eating undercooked pork containing cysticerci gives an intestinal tapeworm; swallowing eggs shed in human feces gives cysticercosis, with larvae encysting in tissue including brain."),
  steps=["Pigs eat eggs from human feces, and larvae encyst in pig muscle as cysticerci.",
         "A person who eats undercooked pork swallows those cysticerci; each becomes an adult tapeworm in the intestine (taeniasis), which is usually mild.",
         "That tapeworm carrier then sheds eggs in their own feces.",
         "A second person - or the carrier themselves - swallows those eggs by the fecal-oral route.",
         "The eggs hatch and larvae cross the gut wall, spreading to muscle, eye, and brain, where they encyst: this is cysticercosis.",
         "Brain cysts cause seizures, which makes neurocysticercosis the leading cause of acquired epilepsy worldwide.",
         "This is why a strict vegetarian can develop neurocysticercosis from a household tapeworm carrier, while pork itself only causes the intestinal worm."]),

"Echinococcus": dict(
  fig=F("fig-echino-cycle.jpg",
        "Echinococcus granulosus: dogs are the definitive host and shed eggs, sheep are the usual intermediate host, and a human who swallows eggs becomes an accidental intermediate host in whom hydatid cysts grow in liver and lung."),
  steps=["Adult worms live in the intestine of dogs and other canids, which shed eggs in feces.",
         "Sheep and other livestock swallow the eggs and develop cysts; dogs are infected by eating that offal, completing the natural cycle.",
         "Humans swallow eggs from dog feces on hands, produce, or fur, and become accidental intermediate hosts.",
         "Larvae cross the gut wall and lodge mainly in the liver, next most often the lung.",
         "A slow-growing fluid-filled hydatid cyst forms, with daughter cysts inside and an eggshell-calcified wall.",
         "The fluid is highly antigenic, so rupture or careless aspiration can cause anaphylaxis and seed new cysts.",
         "Treatment is albendazole with careful surgery or the PAIR technique: puncture, aspirate, inject a scolicidal agent, then re-aspirate."]),

"Schistosoma mansoni": dict(
  fig=F("fig-schisto-cycle.jpg",
        "Schistosoma: eggs passed in stool or urine hatch in fresh water, infect snails, and release cercariae that penetrate human skin. Adults pair in the venous plexus, and it is the trapped eggs that cause disease."),
  steps=["Eggs leave the body in stool (S. mansoni, S. japonicum) or urine (S. haematobium) and hatch in fresh water.",
         "Miracidia infect freshwater snails, the intermediate host, and multiply.",
         "Snails release cercariae, which penetrate the intact skin of someone wading or swimming, causing 'swimmer's itch'.",
         "Larvae migrate through the blood and lungs, then mature into paired adult worms in the venous plexus - mesenteric for mansoni and japonicum, vesical for haematobium.",
         "Adults themselves cause little harm; the disease comes from eggs lodging in tissue.",
         "Eggs in portal venules trigger Th2 granulomas and periportal 'pipestem' fibrosis, giving portal hypertension with preserved liver function.",
         "S. haematobium eggs in the bladder wall cause hematuria and chronic irritation leading to squamous cell carcinoma. Praziquantel treats all species."]),

# ---------------- ticks ----------------
"Lyme disease: tick & co-infection": dict(
  fig=F("fig-tick-cycle.jpg",
        "The two-year Ixodes scapularis cycle: larvae feed on mice (acquiring Borrelia), moult to nymphs that feed the following spring and summer, and adults feed on deer in the fall. Nymphs transmit most human infections."),
  steps=["Adult ticks feed and mate on deer in the fall; deer maintain the tick population but do not carry Borrelia.",
         "Eggs are laid in spring and hatch into larvae, which take a single blood meal from small mammals.",
         "White-footed mice are the reservoir, so the larva acquires Borrelia burgdorferi here.",
         "The larva moults into a nymph, which feeds the following spring and summer - and nymphs cause most human Lyme disease.",
         "Nymphs are poppy-seed sized and easily missed, so the bite often goes unnoticed.",
         "Spirochetes must move from the tick midgut to the salivary glands, which takes roughly 36-48 hours of attachment - the reason prompt removal prevents infection.",
         "The same tick can also carry Babesia microti and Anaplasma phagocytophilum, so co-infection should be considered."]),
}
