"""Fifth pass: trim length advantage in the newly added questions (n-sections are in RETRO scope too)."""
def _o(pairs): return dict(o=dict(pairs))
R = {
"Toxic shock: staph vs strep": _o([("Staphylococcal toxic shock is usually bacteremic, while streptococcal disease is culture-negative",
    "Staphylococcal toxic shock is usually bacteremic, while streptococcal disease is culture-negative early on")]),
"Proteus: urine microscopy": _o([("Uric acid stones in persistently acidic urine", "Uric acid stones forming in persistently acidic urine")]),
"IGRA vs tuberculin skin test": _o([("IGRA distinguishes latent infection from active tuberculosis disease", "IGRA distinguishes latent infection from active tuberculosis disease reliably")]),
"Multidrug-resistant tuberculosis": _o([("Mono-resistant TB, which responds to standard four-drug therapy", "Mono-resistant TB, which still responds to standard four-drug therapy")]),
"Norovirus infection control": _o([("Prophylactic oral antibiotics for exposed staff members", "Prophylactic oral antibiotics given to exposed staff members")]),
"CMV in transplant recipients": _o([("This combination carries the lowest risk of CMV disease after transplant", "This combination carries the lowest risk of CMV disease after transplantation")]),
"HIV screening recommendation": _o([("Screen only patients who inject drugs or have had transfusions", "Screen only patients who inject drugs or have received transfusions")]),
"Hepatitis B vaccination of adults": _o([("Vaccination is needed only after a documented exposure occurs", "Vaccination is needed only after a documented exposure has occurred")]),
"Oral candidiasis risk factors": _o([("Taking a daily multivitamin supplement regularly", "Taking a daily multivitamin supplement on a regular basis")]),
"Pinworm household management": _o([("Boil all drinking water used by the household members", "Boil all of the drinking water used by household members")]),
"Malaria: species identification importance": _o([("Species identification affects prognosis but never treatment", "Species identification affects prognosis but never the treatment")]),
"Eosinophilia workup in a traveler": _o([("A single stool ova and parasite examination reliably excludes helminths", "A single stool ova and parasite examination reliably excludes all helminths")]),
"Antibiogram interpretation": _o([("To confirm that a specific patient's isolate is susceptible", "To confirm that one specific patient's isolate is truly susceptible")]),
"Endotoxin": _o([("It is highly antigenic and can be converted into a toxoid vaccine", "It is highly antigenic and can be converted into a protective toxoid vaccine")]),
"Positive vs negative sense RNA": _o([("Positive-sense genomes all require reverse transcriptase to replicate", "Positive-sense genomes all require a reverse transcriptase in order to replicate")]),
}
