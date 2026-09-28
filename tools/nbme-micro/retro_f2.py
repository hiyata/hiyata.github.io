"""Second batch of explanation figures and step walkthroughs."""
from qcore import F

R = {
# ---------------- cell wall / stains ----------------
"Gram stain: color logic": dict(
  fig=F("fig-gram-wall.jpg",
        "Top: the Gram-negative envelope, with a thin peptidoglycan layer (2) sandwiched between inner (1) and outer (3) membranes. Bottom: the Gram-positive envelope, a single membrane (1) under a thick peptidoglycan wall (2) crossed by teichoic acids."),
  steps=["Crystal violet enters every cell, and iodine fixes it as a large crystal violet-iodine complex.",
         "Alcohol is then applied. In Gram-positive cells the thick, highly cross-linked peptidoglycan dehydrates and traps the complex.",
         "In Gram-negative cells the alcohol dissolves the lipid-rich outer membrane, and the thin peptidoglycan cannot hold the complex, so it washes out.",
         "Safranin is applied last. It stains the now-colorless Gram-negative cells pink; Gram-positive cells are already too dark to change.",
         "So the color reports wall thickness, not the organism's identity - which is why old or antibiotic-treated Gram-positive cells can appear falsely Gram-negative."]),

"Organisms that stain poorly with Gram stain": dict(
  steps=["Gram staining needs a peptidoglycan wall of a certain thickness and an organism large enough to see.",
         "Mycoplasma has no cell wall at all, so there is nothing to retain either dye.",
         "Treponema and Leptospira have walls but are too thin to resolve, so dark-field or silver stains are used instead.",
         "Mycobacteria have waxy mycolic acids that repel aqueous dyes, so acid-fast staining is required.",
         "Legionella, Rickettsia, Chlamydia, and Coxiella live mostly inside host cells and stain faintly, so silver stains, Giemsa, antigen tests, or PCR are used.",
         "Mnemonic: These Microbes May Lack Real Color - Treponema, Mycobacteria, Mycoplasma, Legionella, Rickettsia, Chlamydia."]),

# ---------------- bacterial genetics ----------------
"Transduction": dict(
  steps=["Both forms of transduction move bacterial DNA inside a bacteriophage coat, so neither is blocked by DNase.",
         "In generalized transduction the phage enters the lytic cycle and chops up the host chromosome.",
         "During packaging it occasionally stuffs a random piece of bacterial DNA into a capsid instead of its own genome.",
         "That particle injects the fragment into a new cell, so any host gene can be moved.",
         "In specialized transduction the phage first integrates as a prophage at a specific chromosomal site.",
         "When it later excises imprecisely, it carries the adjacent bacterial genes with it, so only genes flanking that site are transferred.",
         "Lysogenic conversion is related but different: the prophage stays put and the cell simply expresses phage genes, which is how diphtheria, cholera, botulinum, Shiga, and erythrogenic toxins are encoded."]),

# ---------------- toxins ----------------
"C. diphtheriae: toxin mechanism": dict(
  steps=["Only strains lysogenized by the beta-phage carry the tox gene, so toxin production depends on the phage.",
         "The B subunit binds the heparin-binding EGF-like growth factor receptor on host cells.",
         "The toxin is endocytosed and the A subunit escapes into the cytoplasm.",
         "The A subunit transfers ADP-ribose from NAD+ onto elongation factor 2.",
         "Inactivated EF-2 can no longer translocate the ribosome along mRNA, so protein synthesis halts and the cell dies.",
         "Locally this necrosis builds the gray pseudomembrane; systemically absorbed toxin damages heart (myocarditis) and nerves (palatal and cranial palsies).",
         "Antitoxin neutralizes only toxin that has not yet entered cells, which is why it is given immediately on suspicion."]),

"C. tetani: tetanospasmin": dict(
  steps=["Spores in soil germinate in a deep, poorly oxygenated wound and the vegetative bacteria release tetanospasmin.",
         "The toxin binds peripheral motor nerve endings and is carried backwards along the axon by dynein.",
         "It reaches the spinal cord and crosses into inhibitory interneurons, including Renshaw cells.",
         "Its light chain is a zinc protease that cleaves synaptobrevin (VAMP), a SNARE protein.",
         "Without intact SNAREs, vesicles of glycine and GABA cannot fuse and release their contents.",
         "Motor neurons lose their inhibitory brake, producing sustained contraction: trismus, risus sardonicus, and opisthotonus.",
         "Botulinum toxin cleaves the same family of SNAREs but acts at the neuromuscular junction, blocking acetylcholine and causing flaccid paralysis instead."]),

"C. difficile: pathogenesis": dict(
  steps=["Antibiotics wipe out the protective colonic flora, removing colonization resistance.",
         "Ingested C. difficile spores survive gastric acid and germinate in the colon.",
         "Vegetative organisms release toxin A (an enterotoxin) and toxin B (a cytotoxin).",
         "Both toxins glucosylate Rho, Rac, and Cdc42, the GTPases that maintain the actin cytoskeleton.",
         "Colonocytes round up, tight junctions fail, and cells die, causing fluid secretion and intense neutrophil recruitment.",
         "Fibrin, mucus, and dead cells form the yellow-white plaques of pseudomembranous colitis.",
         "Spores resist alcohol, so soap-and-water handwashing and bleach cleaning are required, and treatment is oral fidaxomicin or vancomycin - drugs that stay in the lumen."]),

"E. coli: EHEC & HUS": dict(
  steps=["Undercooked beef or contaminated produce delivers E. coli O157:H7, which needs only a tiny inoculum.",
         "The organism attaches to colonic epithelium and forms attaching-and-effacing lesions, but it does not invade, so fever is often absent.",
         "It releases Shiga-like toxin, an AB5 toxin acquired from a bacteriophage.",
         "The B subunits bind globotriaosylceramide (Gb3), which is densely expressed on glomerular endothelium.",
         "The A subunit removes an adenine from 28S rRNA of the 60S subunit, shutting down protein synthesis and killing the cell.",
         "Endothelial injury exposes von Willebrand factor and triggers platelet microthrombi.",
         "Red cells are sheared as they pass (schistocytes), platelets are consumed, and glomerular perfusion falls - the anemia, thrombocytopenia, and kidney injury of HUS.",
         "Antibiotics may increase toxin release, so treatment is supportive."]),

"B. pertussis: toxin mechanism": dict(
  steps=["B. pertussis attaches to ciliated respiratory epithelium using filamentous hemagglutinin and pertactin.",
         "Tracheal cytotoxin kills ciliated cells, so mucus can no longer be cleared - this produces the violent paroxysmal cough.",
         "Pertussis toxin ADP-ribosylates the alpha subunit of Gi.",
         "Because Gi normally inhibits adenylyl cyclase, disabling it leaves cAMP elevated.",
         "Raised cAMP impairs phagocyte killing, and blocked chemokine signaling prevents lymphocytes from leaving the blood for lymph nodes.",
         "Lymphocytes therefore pile up in the circulation, giving the striking lymphocytosis that predicts severe disease in infants.",
         "Since damage is toxin-driven, macrolides given late reduce transmission but do not shorten the cough."]),

# ---------------- streptococcal sequelae ----------------
"S. pyogenes: M protein & rheumatic fever": dict(
  steps=["Group A strep pharyngitis exposes the immune system to M protein on the bacterial surface.",
         "Antibodies and T cells generated against M protein also recognize structurally similar human proteins - molecular mimicry.",
         "Cross-reactive antibodies bind cardiac myosin and valve glycoproteins, activating complement and recruiting inflammation.",
         "This produces pancarditis with Aschoff bodies, most damaging at the mitral valve.",
         "The same cross-reactivity affects joints (migratory polyarthritis), skin (nodules, erythema marginatum), and basal ganglia (Sydenham chorea).",
         "Symptoms begin 2-4 weeks after pharyngitis, once the antibody response has developed.",
         "Only pharyngitis triggers it, and treating strep throat within about 9 days prevents it - unlike post-streptococcal glomerulonephritis, which antibiotics do not prevent."]),

# ---------------- resistance ----------------
"S. aureus: MRSA resistance": dict(
  steps=["Normal staphylococci build their cell wall using penicillin-binding proteins, which beta-lactams inhibit.",
         "MRSA carries the mecA gene on a mobile element called SCCmec, acquired from another staphylococcal species.",
         "mecA encodes PBP2a, an alternative transpeptidase.",
         "PBP2a has very low affinity for almost all beta-lactams, so it keeps cross-linking the wall while the drug is present.",
         "Because the target has changed rather than the drug being destroyed, beta-lactamase inhibitors such as sulbactam do not help.",
         "This makes the organism resistant to every penicillin and cephalosporin at once - except ceftaroline, which binds PBP2a.",
         "Treatment for serious infection is vancomycin, daptomycin, or linezolid."]),

"Enterococcus: VRE": dict(
  steps=["Vancomycin works by binding the terminal D-Ala-D-Ala of peptidoglycan precursors, physically blocking cross-linking.",
         "The vanA gene cluster, carried on a transposon, encodes enzymes that build a different precursor.",
         "The terminal D-alanine is replaced with D-lactate, giving D-Ala-D-Lac.",
         "Losing one hydrogen bond drops vancomycin binding roughly a thousandfold, so the drug no longer blocks wall synthesis.",
         "Because the change is enzymatic and transposon-borne, it can spread to other organisms, including S. aureus (VRSA).",
         "Treatment shifts to drugs with different targets: linezolid (50S ribosome) or daptomycin (membrane depolarization)."]),

"β-lactamase inhibitors": dict(
  steps=["Beta-lactamases are bacterial enzymes that hydrolyze the beta-lactam ring before it can reach its target.",
         "Clavulanate, sulbactam, and tazobactam resemble beta-lactams closely enough to be attacked by the enzyme.",
         "The enzyme binds the inhibitor and is irreversibly inactivated - a suicide substrate.",
         "The partner antibiotic is then free to reach the penicillin-binding proteins and block cell wall cross-linking.",
         "This restores activity against beta-lactamase producers: MSSA, H. influenzae, Moraxella, and Bacteroides.",
         "It does not overcome resistance from an altered target (MRSA) or from loss of entry (porin mutations).",
         "Newer inhibitors such as avibactam also cover serine carbapenemases like KPC, but not metallo-enzymes such as NDM."]),

# ---------------- antibiotic targets ----------------
"Fosfomycin & bacitracin: cell wall steps": dict(
  fig=F("fig-abx-targets.jpg",
        "Antibiotic classes by target. The cell wall synthesis inhibitors at the top left act at different points along the same assembly line, from cytoplasmic precursor synthesis to final cross-linking."),
  steps=["Step 1, in the cytoplasm: UDP-GlcNAc is converted to UDP-MurNAc by MurA. Fosfomycin blocks this first committed step.",
         "Step 2, at the membrane: the bactoprenol lipid carrier ferries precursors across. Bacitracin blocks its recycling, so it is topical only because of nephrotoxicity.",
         "Step 3, outside the membrane: vancomycin binds the D-Ala-D-Ala end of the precursor itself, preventing it from being added to the chain.",
         "Step 4, the final cross-link: transpeptidases (penicillin-binding proteins) join the peptide stems, and beta-lactams inhibit these enzymes.",
         "Remembering the order clarifies resistance too: changing the precursor (D-Ala-D-Lac) defeats vancomycin, while changing the enzyme (PBP2a) defeats beta-lactams."]),

# ---------------- HIV drugs ----------------
"HIV: integrase & protease inhibitors": dict(
  fig=F("fig-hiv-cycle.jpg",
        "Each antiretroviral class blocks one labelled step: entry inhibitors at attachment and fusion, NRTIs and NNRTIs at reverse transcription, integrase inhibitors at integration, and protease inhibitors at the final maturation step."),
  steps=["After reverse transcription, integrase inserts the viral DNA into the host chromosome; -tegravir drugs block that strand transfer step.",
         "The provirus is transcribed and translated as long Gag and Gag-Pol polyproteins.",
         "HIV protease must cut those polyproteins into functional capsid, matrix, and enzyme units as the virion buds.",
         "Protease inhibitors (-navir) block that cleavage, so released particles are immature and non-infectious.",
         "Protease inhibitors are cleared by CYP3A4, so low-dose ritonavir or cobicistat is added purely to inhibit that enzyme and keep drug levels up.",
         "The same CYP3A4 inhibition causes many interactions, and the class is associated with hyperglycemia, dyslipidemia, and fat redistribution."]),

"HIV: pathogenesis": dict(
  fig=F("fig-hiv-cycle.jpg",
        "Integration of the provirus into host DNA is the step that makes HIV incurable: infected resting memory CD4 cells become a silent reservoir that antiretrovirals cannot reach."),
  steps=["HIV enters CCR5-expressing memory CD4+ T cells, which are densely concentrated in gut lymphoid tissue.",
         "Within weeks of infection the gut CD4 population is massively depleted, long before blood counts fall much.",
         "Loss of that mucosal barrier lets bacterial products translocate into the circulation, driving chronic immune activation.",
         "Ongoing activation accelerates CD4 loss, including bystander cells dying by pyroptosis.",
         "Meanwhile the integrated provirus persists silently in resting memory cells, which do not express viral proteins and so escape immune clearance.",
         "Antiretrovirals block new infection of cells but cannot touch that integrated reservoir, which is why therapy is lifelong and stopping causes rebound."]),

# ---------------- malaria ----------------
"P. vivax: hypnozoites": dict(
  fig=F("fig-malaria-cycle.jpg",
        "The liver stage of the malaria cycle. In P. vivax and P. ovale, some sporozoites become dormant hypnozoites here rather than replicating immediately, and they reactivate weeks to months later."),
  steps=["Sporozoites injected by the mosquito travel to the liver and enter hepatocytes.",
         "In P. falciparum and P. malariae they all replicate and move on to the blood, so once the blood stage is cured, the infection is over.",
         "In P. vivax and P. ovale a fraction stay dormant as hypnozoites.",
         "Blood-stage drugs such as chloroquine and artemisinin combinations never reach these dormant forms.",
         "Weeks to months later hypnozoites activate, release merozoites, and the illness relapses with no new mosquito exposure.",
         "Primaquine or tafenoquine kills liver hypnozoites - so-called radical cure.",
         "Both cause oxidative hemolysis in G6PD deficiency, so G6PD testing comes before the prescription."]),

"P. falciparum: severe malaria": dict(
  fig=F("fig-malaria-cycle.jpg",
        "The blood stage of the cycle. In P. falciparum this stage is dangerous because the parasite invades red cells of every age and makes infected cells stick to blood vessel walls."),
  steps=["Merozoites released from the liver invade red blood cells; P. falciparum invades cells of any age, so parasitemia climbs steeply.",
         "The parasite exports PfEMP1 onto knobs on the red cell surface.",
         "PfEMP1 binds endothelial receptors such as ICAM-1, CD36, and EPCR, so infected cells adhere to capillary walls.",
         "Sequestration keeps mature forms out of the circulating blood, which is why smears usually show only rings and gametocytes.",
         "Adherent cells obstruct cerebral microvessels, causing confusion, seizures, and coma.",
         "The same process damages kidney (hemoglobinuria), lung (ARDS), and placenta, and massive hemolysis causes severe anemia and hypoglycemia.",
         "Severe disease is treated with IV artesunate; delayed hemolysis can appear 1-3 weeks later and needs follow-up blood counts."]),

# ---------------- TB ----------------
"TB: miliary disease": dict(
  fig=F("fig-tb-latency.jpg",
        "When containment fails, bacilli escape the granuloma. If they enter the bloodstream they seed innumerable tiny foci throughout the body, producing miliary disease."),
  steps=["A granuloma normally walls off the organism, and containment depends on Th1 cells, IFN-gamma, and TNF.",
         "When cell-mediated immunity is weak - infancy, old age, HIV, steroids, TNF inhibitors - that structure fails.",
         "Bacilli erode into a blood vessel or lymphatic and disseminate.",
         "They seed innumerable small foci in lungs, liver, spleen, marrow, meninges, and adrenals; the millet-seed nodules give the disease its name.",
         "Because organisms are spread thinly through tissue rather than pouring into airways, sputum smears are often negative.",
         "Tuberculin skin testing may be falsely negative too, since anergy accompanies overwhelming disease.",
         "Extrapulmonary sites explain the classic complications: basilar meningitis, Pott disease of the spine, and adrenal insufficiency."]),

# ---------------- herpes ----------------
"HSV-1: latency": dict(
  fig=F("fig-hsv-latency.jpg",
        "Productive HSV-1 replication in an epithelial cell, with ordered immediate-early, early, and late gene expression. In sensory neurons this cascade is suppressed instead, leaving the genome quiet until reactivation."),
  steps=["Primary infection occurs in mucosal or skin epithelium, where the full lytic cascade runs and vesicles form.",
         "Virions enter sensory nerve endings in that territory.",
         "The nucleocapsid is carried backwards along the axon to the trigeminal ganglion (HSV-1) or sacral ganglia (HSV-2).",
         "In the neuron the viral genome circularizes as an episome and lytic genes are silenced; only latency-associated transcripts are made.",
         "Because no viral proteins are displayed, the immune system cannot find and clear the infected neuron - latency is lifelong.",
         "Stress, fever, ultraviolet light, or immunosuppression reactivate transcription.",
         "New virions travel forward down the same axon to the skin, so recurrences appear in the same dermatome each time.",
         "Acyclovir needs viral thymidine kinase, expressed only during active replication, so it treats outbreaks but cannot clear latent virus."]),

"Acyclovir mechanism": dict(
  steps=["Acyclovir is a guanosine analog and is inert as given.",
         "In an infected cell, viral thymidine kinase adds the first phosphate - uninfected cells cannot do this efficiently, which is the basis of its selectivity.",
         "Host kinases add the second and third phosphates, producing acyclovir triphosphate.",
         "That molecule competes with dGTP for viral DNA polymerase, which has far higher affinity for it than the host enzyme does.",
         "Once incorporated it terminates the chain, because it lacks the 3'-hydroxyl needed for the next nucleotide.",
         "Resistance usually arises from loss of viral thymidine kinase, so valacyclovir and famciclovir fail too.",
         "Foscarnet and cidofovir inhibit the viral polymerase directly and need no viral kinase, so they still work."]),

# ---------------- hepatitis ----------------
"HBV: replication": dict(
  steps=["HBV enters hepatocytes and delivers its partially double-stranded circular DNA to the nucleus.",
         "Host enzymes repair the gap, producing covalently closed circular DNA (cccDNA), a stable mini-chromosome.",
         "cccDNA is transcribed by host RNA polymerase into several RNAs, including a pregenomic RNA.",
         "Pregenomic RNA is packaged into a capsid together with the viral polymerase.",
         "Inside that capsid, the polymerase reverse-transcribes the RNA back into DNA - the step nucleoside analogs such as tenofovir and entecavir block.",
         "Some capsids recycle their DNA back to the nucleus, replenishing the cccDNA pool.",
         "Because cccDNA persists even when serum HBV DNA is undetectable, therapy suppresses rather than cures, and immunosuppression such as rituximab can reactivate infection."]),

"HBV serology: window period": dict(
  steps=["HBsAg appears first, usually weeks before symptoms, and marks active infection.",
         "Anti-HBc IgM appears next, as the immune response targets the core antigen.",
         "As infection resolves, HBsAg is cleared from the blood.",
         "Anti-HBs takes time to become detectable, so for a period both HBsAg and anti-HBs are negative - the window period.",
         "During that gap, IgM anti-HBc is the only positive marker, which is why the core antibody is essential to the panel.",
         "Later, anti-HBs and IgG anti-HBc are both positive: resolved infection with immunity.",
         "The vaccine contains only surface antigen, so vaccinated people have anti-HBs but never anti-HBc - that single marker separates vaccination from past infection."]),

# ---------------- viral oncogenesis / prions ----------------
"HPV: oncogenesis": dict(
  steps=["High-risk HPV types (16, 18, 31, 33) infect basal keratinocytes through a mucosal break.",
         "In persistent infection the viral genome integrates into host DNA, which disrupts the E2 gene.",
         "E2 normally restrains E6 and E7, so losing it causes both oncoproteins to be overexpressed.",
         "E6 recruits the E6AP ubiquitin ligase to tag p53 for degradation, removing the checkpoint that halts damaged cells.",
         "E7 binds Rb and releases E2F, pushing the cell into S phase without the usual controls.",
         "With both brakes gone, mutations accumulate and dysplasia progresses to invasive carcinoma over years.",
         "Koilocytes - squamous cells with wrinkled nuclei and perinuclear halos - are the cytologic footprint of this process.",
         "The vaccine uses L1 capsid virus-like particles, which prevent infection but cannot reverse integration that has already happened."]),

"Prion disease": dict(
  steps=["PrPc is a normal cellular protein, rich in alpha-helix, present on neurons.",
         "In disease it refolds into PrPsc, which is rich in beta-pleated sheet.",
         "PrPsc acts as a template, forcing normal PrPc molecules to adopt the misfolded shape - an autocatalytic chain reaction.",
         "The beta-sheet form resists proteases and accumulates as aggregates and amyloid plaques.",
         "Neurons die and the cortex takes on the vacuolated, spongiform appearance, with no inflammatory infiltrate because no foreign antigen is present.",
         "Clinically this gives rapidly progressive dementia with startle myoclonus, periodic sharp waves on EEG, and cortical ribboning on MRI.",
         "Prions contain no nucleic acid and resist standard autoclaving and disinfection, which is why contaminated neurosurgical instruments have transmitted disease."]),

# ---------------- other life cycles ----------------
"Toxoplasma: AIDS": dict(
  fig=F("fig-toxo-cycle.jpg",
        "Tissue cysts full of slow-growing bradyzoites persist for life after primary infection. When cell-mediated immunity fails, they convert back to fast-dividing tachyzoites."),
  steps=["Primary infection is usually mild and leaves tissue cysts in brain and muscle, held in check by CD4+ T cells.",
         "As the CD4 count falls below about 100, that surveillance fails.",
         "Bradyzoites inside cysts convert back into rapidly dividing tachyzoites.",
         "Tachyzoites destroy surrounding brain tissue, producing multiple abscesses with surrounding edema.",
         "On MRI these appear as multiple ring-enhancing lesions, typically at the gray-white junction and basal ganglia.",
         "Positive Toxoplasma IgG confirms prior exposure and therefore the potential for reactivation; a negative IgG makes the diagnosis unlikely.",
         "Treatment is pyrimethamine plus sulfadiazine with leucovorin, and clinical response within two weeks supports the diagnosis over CNS lymphoma."]),

"Neurocysticercosis": dict(
  fig=F("fig-taenia-cycle.jpg",
        "Swallowing Taenia solium eggs - not pork - puts humans in the intermediate-host position, so larvae encyst in tissue. Brain cysts are what cause seizures."),
  steps=["Eggs are swallowed from food, water, or hands contaminated by a human tapeworm carrier's feces.",
         "Larvae hatch, cross the intestinal wall, and travel in the blood to muscle, eye, and brain.",
         "Each larva forms a cyst that stays quiet while it is alive, because it actively suppresses local inflammation.",
         "When the larva dies, that suppression stops and the host mounts an inflammatory response.",
         "Surrounding edema and gliosis irritate the cortex and provoke seizures - the commonest presentation.",
         "Imaging shows cysts, sometimes with a visible scolex inside, plus calcified remnants of older dead cysts.",
         "Viable cysts are treated with albendazole plus corticosteroids, since killing them transiently worsens inflammation; calcified lesions need only seizure control."]),

"Schistosoma haematobium": dict(
  fig=F("fig-schisto-cycle.jpg",
        "The schistosome cycle. S. haematobium adults live in the vesical venous plexus, so eggs are shed in urine and lodge in the bladder wall rather than the gut."),
  steps=["Cercariae from freshwater snails penetrate skin during wading or swimming.",
         "Adults mature and pair in the venous plexus around the bladder.",
         "The female lays eggs with a terminal spine that work their way through the bladder wall into urine.",
         "Many eggs stay trapped in the wall, where they trigger granulomas and fibrosis.",
         "Chronic irritation causes painless hematuria and, over years, squamous metaplasia of the urothelium.",
         "Metaplastic epithelium can progress to squamous cell carcinoma of the bladder - a different pathway from the urothelial carcinoma caused by smoking.",
         "Praziquantel increases calcium permeability in the worm tegument, paralyzing adults and allowing immune clearance."]),

"Lyme disease: erythema migrans": dict(
  fig=F("fig-tick-cycle.jpg",
        "The Ixodes life cycle. Nymphs feed in late spring and summer and cause most human Lyme disease; they are tiny and their bite is usually unnoticed."),
  steps=["A nymphal Ixodes tick attaches, typically in late spring or summer, and feeds unnoticed.",
         "Borrelia burgdorferi lives in the tick midgut and must migrate to the salivary glands before it can be injected.",
         "That migration takes roughly 36-48 hours, which is why prompt tick removal prevents infection.",
         "Once inoculated, spirochetes spread outward through the skin.",
         "The host immune response to that advancing edge creates the expanding annular rash, often with central clearing - erythema migrans.",
         "The rash appears days to a month after the bite and is diagnostic on its own; serology is frequently still negative at this point.",
         "Untreated infection disseminates to nerves (facial palsy), heart (AV block), and later joints. Oral doxycycline treats early disease."]),

"Anaplasma": dict(
  fig=F("fig-tick-cycle.jpg",
        "Anaplasma shares the Ixodes vector with Lyme disease and babesiosis, so a single tick bite can transmit more than one pathogen."),
  steps=["The same Ixodes nymph that transmits Borrelia can also carry Anaplasma phagocytophilum and Babesia microti.",
         "Anaplasma infects granulocytes, where it grows in vacuoles that appear as mulberry-like morulae in neutrophils.",
         "Infection of white cells and marrow suppression cause leukopenia, thrombocytopenia, and raised transaminases.",
         "There is usually no rash, which distinguishes it from Rocky Mountain spotted fever.",
         "Ehrlichia chaffeensis is the close mimic but comes from the lone star tick and forms morulae in monocytes.",
         "Doxycycline treats Anaplasma, Ehrlichia, and Lyme disease, but not Babesia - so a patient failing to improve should be checked for babesiosis."]),
}
