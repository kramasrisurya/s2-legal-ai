"""
S2 Legal AI Pro - Specific Statutory Section & Article Legal Purpose Resolver
Module: backend.statutory_engine

Provides immediate, authoritative, primary-purpose legal explanations for specific
statutory sections and constitutional articles (e.g. IPC 300, IPC 420, IPC 302,
Article 21, Section 138 NI Act, Section 41A CrPC).

States WHAT IT IS PRIMARILY FOR in the very first sentence, followed by essential
elements, exceptions, IPC <-> BNS 2023 concordance, and actionable strategy.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple


STATUTORY_REGISTRY: Dict[str, Dict[str, Any]] = {
    "300": {
        "title": "Section 300 IPC: Offence of Murder",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 101 BNS (Definition) & Section 103(1) BNS (Punishment)",
        "primary_purpose": (
            "**Section 300 of the Indian Penal Code (IPC) is primarily for MURDER.**\n"
            "It defines the four legal conditions under which causing death (culpable homicide) constitutes murder, "
            "and provides five strict exceptions where causing death is treated as culpable homicide NOT amounting to murder. "
            "Under the modern **Bharatiya Nyaya Sanhita, 2023 (BNS)**, this definition is codified under **Section 101 BNS**, "
            "with punishment under **Section 103(1) BNS** (formerly Section 302 IPC)."
        ),
        "definition": (
            "Except in the cases hereinafter excepted, culpable homicide is **murder**, if the act by which the death is caused satisfies any of the following 4 clauses:\n"
            "1. **Intention to cause death**: The act is committed with the premeditated or deliberate intention of causing death.\n"
            "2. **Intentional fatal bodily injury known to offender**: The act is done with the intention of causing such bodily injury as the offender *knows* is likely to cause the death of that particular person.\n"
            "3. **Bodily injury sufficient in ordinary course of nature**: The injury intentionally inflicted is sufficient in the ordinary course of nature to cause death (e.g., weapon strike to a vital organ).\n"
            "4. **Imminently dangerous act**: The offender commits an act so imminently dangerous that it must in all probability cause death or fatal bodily injury, without any lawful excuse."
        ),
        "exceptions": [
            "**Exception 1 (Grave and Sudden Provocation)**: Offender is deprived of the power of self-control by grave and sudden provocation (not sought or self-created).",
            "**Exception 2 (Exceeding Private Defence in Good Faith)**: Offender exceeds the right of private defence of body or property in good faith without premeditation.",
            "**Exception 3 (Public Servant Acting for Justice)**: A public servant acting in good faith believing their act to be lawful and necessary for public justice.",
            "**Exception 4 (Sudden Fight in Heat of Passion)**: Death caused in a sudden fight in the heat of passion upon a sudden quarrel, without premeditation or taking undue advantage.",
            "**Exception 5 (Consent of Adult Victim)**: Death caused with the voluntary consent of a person above 18 years of age.",
        ],
        "punishment_table": {
            "definition_sec": ("Section 300 IPC", "Section 101 BNS"),
            "punishment_sec": ("Section 302 IPC", "Section 103(1) BNS"),
            "penalty": ("Death or Imprisonment for Life, and Fine", "Death or Imprisonment for Life, and Fine"),
            "cognizance": ("Cognizable (Arrest without warrant)", "Cognizable"),
            "bail": ("Non-Bailable (Sessions Court strictly)", "Non-Bailable"),
            "court": ("Court of Session", "Court of Session"),
        },
        "advocate_strategy": (
            "• **Forensic Autopsy Review**: Scrutinize the Post-Mortem Report (PMR) to verify whether injury was 'sufficient in the ordinary course of nature' (Clause 3) or merely 'likely' to cause death.\n"
            "• **Exception Pleading**: If sudden fight, provocation, or private defence occurred, prepare defense pleadings under Section 300 Exceptions to reduce charge to Section 304 IPC / Section 105 BNS.\n"
            "• **Bail Jurisprudence**: Governed by Category C/D parameters in *Satender Kumar Antil v. CBI*. Bail requires demonstrating absence of prima facie murderous intent or common object."
        ),
        "client_strategy": (
            "• **Immediate Legal Representation**: Section 300/302 offences are non-bailable; contact an Advocate immediately for Sessions Court representation.\n"
            "• **Preserve Exculpatory Evidence**: Collect CCTV footage, phone call logs, medical records, or witness statements establishing provocation, self-defence, or an alibi.\n"
            "• **Custodial Safeguards**: Under *D.K. Basu v. State of West Bengal*, you have the right to a medical examination upon arrest, representation by counsel, and immediate notification of next-of-kin."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Page 69, Section 300: Murder & 5 Statutory Exceptions)",
            "[Statute] Indian Penal Code, 1860 (Act No. 45 of 1860) - Section 300 (Offence) & Section 302 (Punishment)",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 101 & Section 103(1)",
        ],
    },
    "302": {
        "title": "Section 302 IPC: Punishment for Murder",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 103(1) BNS (Murder) & Section 103(2) BNS (Mob Lynching)",
        "primary_purpose": (
            "**Section 302 of the Indian Penal Code (IPC) is primarily for the PUNISHMENT FOR MURDER.**\n"
            "While Section 300 defines what murder is, Section 302 prescribes the penal sanction: whoever commits murder shall be punished with death, "
            "or imprisonment for life, and shall also be liable to fine. Under the **Bharatiya Nyaya Sanhita (BNS 2023)**, this is codified under **Section 103(1)**."
        ),
        "definition": (
            "**Statutory Text (Section 302 IPC)**:\n"
            "> *\"Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine.\"*\n\n"
            "**Key Elements for Conviction**:\n"
            "1. Proof of death of the victim.\n"
            "2. Proof that death was caused by the bodily injury inflicted by the accused.\n"
            "3. Proof of intention or knowledge falling within any of the four clauses of Section 300 IPC."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 300 IPC", "Section 101 BNS"),
            "punishment_sec": ("Section 302 IPC", "Section 103(1) BNS"),
            "penalty": ("Death or Imprisonment for Life, and Fine", "Death or Imprisonment for Life, and Fine"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Court of Session", "Court of Session"),
        },
        "advocate_strategy": (
            "• **Motive & Chain of Circumstances**: In circumstantial evidence cases, enforce the *Sharad Birdhichand Sarda* 5 golden principles (panchsheel). The chain must be complete leaving no reasonable doubt.\n"
            "• **Rarest of Rare Doctrine**: If prosecution seeks capital punishment, argue mitigating circumstances under *Bachan Singh* and *Machhi Singh* (age, socio-economic background, probability of reform).\n"
            "• **Electronic Proof (BSA 2023)**: Insist on strict certificate compliance for CDR and electronic records under Section 63 of Bharatiya Sakshya Adhiniyam, 2023 (BSA)."
        ),
        "client_strategy": (
            "• **No Self-Incrimination**: Under Article 20(3) of the Constitution, you cannot be compelled to give self-incriminating confessions in police custody.\n"
            "• **Apply for Regular Bail**: Move bail before the Sessions Court or High Court under Section 480 BNSS (Section 439 CrPC) through senior legal counsel.\n"
            "• **Preserve Evidence**: Assemble proof of alibi or presence elsewhere at the exact time of the alleged incident."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Page 70, Section 302: Punishment for Murder)",
            "[Statute] Indian Penal Code, 1860 - Section 302",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 103(1)",
        ],
    },
    "420": {
        "title": "Section 420 IPC: Cheating & Dishonestly Inducing Delivery of Property",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 318(4) BNS",
        "primary_purpose": (
            "**Section 420 of the Indian Penal Code (IPC) is primarily for CHEATING AND FRAUD.**\n"
            "It penalizes anyone who cheats and thereby dishonestly induces the deceived person to deliver property or make/alter/destroy valuable security. "
            "Under the **Bharatiya Nyaya Sanhita (BNS 2023)**, it is codified under **Section 318(4)**."
        ),
        "definition": (
            "**Statutory Text (Section 420 IPC)**:\n"
            "> *\"Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person, or to make, alter or destroy the whole or any part of a valuable security... shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine.\"*\n\n"
            "**Essential Legal Ingredients**:\n"
            "1. **Deception**: Fraudulent or dishonest representation made to the victim.\n"
            "2. **Dishonest Intention at Inception**: As settled by the Supreme Court in *Hridaya Ranjan Prasad Verma*, fraudulent intent must exist at the very beginning of the transaction. Mere subsequent inability to pay is a breach of contract, not cheating.\n"
            "3. **Inducement to Deliver Property**: The victim handed over valuable property or money solely relying on that deception."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 415 IPC (Definition)", "Section 318(1) BNS"),
            "punishment_sec": ("Section 420 IPC", "Section 318(4) BNS"),
            "penalty": ("Imprisonment up to 7 years, and Fine", "Imprisonment up to 7 years, and Fine"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Magistrate of the first class", "Magistrate of the first class"),
        },
        "advocate_strategy": (
            "• **Notice in Lieu of Arrest (Section 35(3) BNSS)**: For offences up to 7 years, police must follow *Arnesh Kumar* guidelines and issue notice before arrest.\n"
            "• **Quashing Petition (Section 528 BNSS / Section 482 CrPC)**: If the dispute is a commercial contract breach without dishonest intent at inception, petition the High Court to quash the FIR.\n"
            "• **Anticipatory Bail**: File pre-arrest protection under Section 482 BNSS (Section 438 CrPC) before the Sessions Court or High Court."
        ),
        "client_strategy": (
            "• **Assemble All Documents**: Gather written agreements, receipts, bank statements, invoices, and WhatsApp chats proving genuine business intent.\n"
            "• **Respond to Notice Promptly**: If police issue a Section 35(3) BNSS notice, attend with counsel and submit a written defense showing lack of fraud.\n"
            "• **Seek Anticipatory Bail**: If an FIR is registered, seek anticipatory bail immediately to protect against arrest."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Page 95, Section 420: Cheating)",
            "[Statute] Indian Penal Code, 1860 - Section 420",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 318(4)",
            "[Precedent] Arnesh Kumar v. State of Bihar (2014) & Hridaya Ranjan Prasad Verma v. State of Bihar (2000)",
        ],
    },
    "498a": {
        "title": "Section 498A IPC: Cruelty by Husband or Relatives (Dowry Harassment)",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 85 (Punishment) & Section 86 (Definition) BNS",
        "primary_purpose": (
            "**Section 498A of the Indian Penal Code (IPC) is primarily for CRUELTY & HARASSMENT AGAINST A MARRIED WOMAN BY HER HUSBAND OR IN-LAWS (including Dowry demands).**\n"
            "It penalizes subjecting a woman to physical cruelty, mental torment, or coercion to meet unlawful demands for property or money. "
            "Under the **Bharatiya Nyaya Sanhita (BNS 2023)**, it is codified under **Section 85 (Punishment)** and **Section 86 (Definition)**."
        ),
        "definition": (
            "**Statutory Text (Section 498A IPC)**:\n"
            "> *\"Whoever, being the husband or the relative of the husband of a woman, subjects such woman to cruelty shall be punished with imprisonment for a term which may extend to three years and shall also be liable to fine.\"*\n\n"
            "**Definition of 'Cruelty'**:\n"
            "1. **Clause (a)**: Any wilful conduct likely to drive the woman to commit suicide or cause grave injury or danger to life, limb, or mental health.\n"
            "2. **Clause (b)**: Harassment with a view to coercing her or her family to meet any unlawful demand for property or valuable security (dowry)."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 498A IPC (Explanation)", "Section 86 BNS"),
            "punishment_sec": ("Section 498A IPC", "Section 85 BNS"),
            "penalty": ("Imprisonment up to 3 years, and Fine", "Imprisonment up to 3 years, and Fine"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Magistrate of the first class", "Magistrate of the first class"),
        },
        "advocate_strategy": (
            "• **Mandatory Arnesh Kumar Checklist**: Arrest cannot be mechanical; police must satisfy Section 35(3) BNSS checklist before arresting in-laws.\n"
            "• **Quashing for Distant Relatives**: File High Court petition under Section 528 BNSS (Section 482 CrPC) for non-resident in-laws where allegations are vague or omnibus (*Geeta Mehrotra v. State of UP*).\n"
            "• **PWDVA & Maintenance Cross-Proceedings**: Coordinate defense/claim alongside Section 12 Domestic Violence Act and Section 125 CrPC / 144 BNSS maintenance."
        ),
        "client_strategy": (
            "• **For Victims/Complainants**: Preserve WhatsApp messages, photographs, medical injury reports (MLC), bank transaction slips, and Stridhan inventory.\n"
            "• **For Accused Husband/In-Laws**: Do not evade; respond to police notice with an advocate and file for anticipatory bail under Section 482 BNSS.\n"
            "• **Emergency Helplines**: Women in distress can contact Women Helpline **1091** or Domestic Abuse Support at **181**."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 498A: Cruelty by Husband or Relatives)",
            "[Statute] Indian Penal Code, 1860 - Section 498A",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 85 & Section 86",
            "[Precedents] Arnesh Kumar (2014) & Social Action Forum for Manav Adhikar (2018)",
        ],
    },
    "21": {
        "title": "Article 21: Protection of Life and Personal Liberty",
        "act": "Constitution of India, 1950",
        "bns_equiv": "Part III Fundamental Right (Supreme Lex)",
        "primary_purpose": (
            "**Article 21 of the Constitution of India is primarily for the SACROSANCT RIGHT TO LIFE AND PERSONAL LIBERTY.**\n"
            "It establishes that *\"No person shall be deprived of his life or personal liberty except according to procedure established by law.\"* "
            "It is the bedrock of Indian constitutional jurisprudence, expansively protecting human dignity, privacy, health, fair trial, and livelihood."
        ),
        "definition": (
            "**Statutory Text (Article 21)**:\n"
            "> *\"No person shall be deprived of his life or personal liberty except according to procedure established by law.\"*\n\n"
            "**Expansive Facets Recognized by Supreme Court**:\n"
            "1. **Right to Dignity**: Life means more than mere animal existence (*Maneka Gandhi*, 1978).\n"
            "2. **Right to Privacy**: An intrinsic fundamental right under Article 21 (*K.S. Puttaswamy*, 9-Judge Bench, 2017).\n"
            "3. **Right to Fair Trial & Legal Aid**: State must provide free legal aid to underprivileged (*Hussainara Khatoon*).\n"
            "4. **Right to Clean Environment**: Environmental protection is a direct facet of life (*M.C. Mehta*).\n"
            "5. **Safeguard Against Custodial Torture**: Police arrest procedures must follow *D.K. Basu* guidelines."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Article 21 (Constitution of India)", "Fundamental Right (Part III)"),
            "punishment_sec": ("Enforceable via Articles 32 & 226", "Writ Jurisdiction (Supreme & High Court)"),
            "penalty": ("State Action Declared Void (Article 13)", "Constitutional Mandate"),
            "cognizance": ("Applicable against State & State Instrumentalities", "Article 12 State definition"),
            "bail": ("Right to Speedy Trial encompasses Bail", "Bail is Rule, Jail is Exception"),
            "court": ("High Courts & Supreme Court of India", "Constitutional Benches"),
        },
        "advocate_strategy": (
            "• **Writ Remedies**: Directly invoke Article 32 (Supreme Court) or Article 226 (High Court) for Habeas Corpus or Mandamus when liberty is infringed.\n"
            "• **Substantive Due Process**: Challenge state procedures that are unjust, unfair, or unreasonable under the *Maneka Gandhi* triple-test (Articles 14, 19, and 21).\n"
            "• **Speedy Trial Bail**: Cite *Satender Kumar Antil* and Article 21 where undertrial detention exceeds reasonable bounds."
        ),
        "client_strategy": (
            "• **Police Interrogation Rights**: You have the right to remain silent, consult a lawyer, and be produced before a Magistrate within 24 hours.\n"
            "• **Legal Aid Access**: Under Article 39A and Article 21, you are entitled to free legal assistance through the Legal Services Authority.\n"
            "• **Challenge Arbitrary Action**: Any illegal arrest, surveillance, or physical harassment by state officials can be challenged immediately in the High Court."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/constitution/ (Constitution of India - Article 21: Part III)",
            "[Landmark SC] Maneka Gandhi v. Union of India (1978) 1 SCC 248 (Substantive Due Process)",
            "[Landmark SC] Justice K.S. Puttaswamy v. Union of India (2017) 10 SCC 1 (Right to Privacy)",
            "[Landmark SC] D.K. Basu v. State of West Bengal (1997) 1 SCC 416 (Custodial Safeguards)",
        ],
    },
    "138": {
        "title": "Section 138 Negotiable Instruments Act: Dishonour of Cheque",
        "act": "Negotiable Instruments Act, 1881",
        "bns_equiv": "Section 138 NI Act (Special Statutory Enactment)",
        "primary_purpose": (
            "**Section 138 of the Negotiable Instruments Act is primarily for CHEQUE BOUNCE (DISHONOUR OF CHEQUE).**\n"
            "It imposes criminal liability when a cheque drawn for the discharge of a legally enforceable debt is returned unpaid by the bank due to insufficient funds or exceeding arrangement."
        ),
        "definition": (
            "**Mandatory Statutory Timeline to Maintain Prosecution**:\n"
            "1. **Presentation**: Cheque presented within validity period (3 months from issuance date).\n"
            "2. **Dishonour Memo**: Bank returns cheque with memo (e.g. 'Funds Insufficient', 'Account Closed').\n"
            "3. **Statutory Demand Notice**: Complainant must issue formal legal demand notice within **30 days** of receiving bank memo.\n"
            "4. **15-Day Grace Period**: Drawer has **15 days** from notice receipt to pay the cheque amount.\n"
            "5. **Cause of Action & Filing**: If unpaid, criminal complaint must be filed within **30 days** before Judicial Magistrate."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 138 NI Act", "Dishonour of Cheque"),
            "punishment_sec": ("Section 138 NI Act", "Imprisonment & Fine"),
            "penalty": ("Imprisonment up to 2 years, or Fine up to twice cheque amount, or both", "Compoundable offence"),
            "cognizance": ("Non-Cognizable (Direct Complaint to Court)", "Magistrate First Class"),
            "bail": ("Bailable", "Bailable"),
            "court": ("Metropolitan Magistrate / JMFC", "Court of competent jurisdiction"),
        },
        "advocate_strategy": (
            "• **Notice Tracking**: Ensure strict proof of dispatch and postal tracking / WhatsApp delivery acknowledgment within 30 days.\n"
            "• **Interim Compensation (Section 143A NI Act)**: Apply for 20% interim compensation payable by drawer during trial.\n"
            "• **Rebuttal of Presumption (Section 139 NI Act)**: For defense, discharge statutory presumption by demonstrating security cheque or absence of legally enforceable debt."
        ),
        "client_strategy": (
            "• **Do Not Miss Deadlines**: The 30-day notice and 30-day court filing windows are strictly enforced by courts.\n"
            "• **Retain Original Cheque & Memo**: Keep the original cheque, bank return memo, copy of notice, and postal receipt in a safe folder.\n"
            "• **Settlement Option**: Section 138 offences can be compounded at any stage if the accused pays the cheque sum."
        ),
        "citations": [
            "[Statute] Negotiable Instruments Act, 1881 - Section 138, 139, 141, 143A",
            "[Precedent] Meters and Instruments Pvt Ltd v. Kanchan Mehta (2018) 1 SCC 560",
            "[Precedent] Rangappa v. Sri Mohan (2010) 11 SCC 441 (Section 139 Presumption)",
        ],
    },
}


def match_statutory_section(query: str) -> Optional[Tuple[str, str]]:
    """
    Evaluates whether query asks about a specific statutory section (IPC, CrPC, NI Act, Constitution).
    Returns (section_key, statute_type) or None.
    """
    clean = re.sub(r"[^\w\s]", " ", query).strip().lower()
    clean = re.sub(r"\s+", " ", clean)

    # 1. Constitution Articles: e.g. "article 21", "art 21", "article 14", "art 32", "article 226"
    m_art = re.search(r"\b(?:article|art)\s*(\d+[a-zA-Z]?)\b", clean)
    if m_art:
        key = m_art.group(1).lower()
        if key in STATUTORY_REGISTRY:
            return key, "constitution"

    # 2. IPC / Criminal Sections: e.g. "ipc 300", "section 300", "sec 300", "300 ipc", "what is ipc 300", "ipc 420"
    m_ipc = re.search(
        r"\b(?:ipc|indian penal code|section|sec)\s*(\d+[a-zA-Z]?)\b|\b(\d+[a-zA-Z]?)\s*(?:ipc|indian penal code|section|sec)\b",
        clean,
    )
    if m_ipc:
        key = (m_ipc.group(1) or m_ipc.group(2)).lower()
        if key in STATUTORY_REGISTRY:
            return key, "ipc"

    # 3. Plain section numbers if query is very short: e.g. "300", "420", "302"
    tokens = clean.split()
    if len(tokens) <= 2:
        for t in tokens:
            if t in STATUTORY_REGISTRY:
                return t, "ipc"

    # 4. Direct conceptual queries: "what is murder", "definition of murder", "cheating", "theft", etc.
    concept_map = {
        "punishment for murder": ("302", "ipc"),
        "murder": ("300", "ipc"),
        "cheating": ("420", "ipc"),
        "theft": ("378", "ipc"),
        "dowry death": ("304b", "ipc"),
        "cruelty by husband": ("498a", "ipc"),
        "domestic cruelty": ("498a", "ipc"),
        "defamation": ("499", "ipc"),
        "cheque bounce": ("138", "ipc"),
        "dishonour of cheque": ("138", "ipc"),
    }
    # Check if query asks what/definition of these concepts
    for concept, (sec, stype) in concept_map.items():
        if re.search(r"\b(?:what\s+is|define|definition\s+of|explain|tell\s+me\s+about)?\s*" + re.escape(concept) + r"\b", clean):
            if not re.search(r"\b(can\s+i|how\s+to|should\s+i|want\s+to|kill|shoot|stab)\b", clean):
                return sec, stype

    return None


# ==============================================================================
# Violent Crime, Harmful Act & Offence Safety Guardrail Interceptor
# ==============================================================================

def match_harm_or_violent_crime_query(query: str) -> Optional[Dict[str, Any]]:
    """
    Detects queries contemplating, asking about the legality of, or inquiring about
    the commission of violent acts, murder, culpable homicide, shooting, stabbing,
    or physical assault under Indian Law.
    
    Examples:
    - "can i kill me brother?"
    - "can i kill my brother?"
    - "is it legal to kill someone"
    - "how can i kill someone"
    - "i want to kill my brother"
    - "can i murder someone"
    - "can i shoot someone"
    - "is killing allowed"
    """
    clean = re.sub(r"[^\w\s]", " ", query).strip().lower()
    clean = re.sub(r"\s+", " ", clean)

    # 1. Direct permission, contemplation, or solicitation of violent harm / killing
    intent_pattern = (
        r"\b(can\s+i|can\s+we|may\s+i|is\s+it\s+legal(?:\s+to)?|is\s+it\s+allowed(?:\s+to)?|"
        r"how\s+to|how\s+can\s+i|how\s+do\s+i|should\s+i|i\s+want\s+to|i\s+need\s+to|"
        r"allowed\s+to|permission\s+to|ways\s+to|can\s+one|could\s+i|where\s+can\s+i)\s+"
        r"(?:commit\s+)?(kill|murder|shoot|poison|stab|slay|strangle|assault|harm|beat|eliminate|lynch|attack)\b"
    )
    m1 = re.search(intent_pattern, clean)
    if m1:
        action = m1.group(2)
        # Extract target relationship if present
        target_m = re.search(
            r"\b(kill|murder|shoot|poison|stab|slay|strangle|assault|harm|beat|eliminate|lynch|attack)\s+"
            r"(?:my|me|his|her|their|a|an|the|someone|somebody|anyone|anybody)?\s*"
            r"(brother|bro|sister|sis|father|dad|mother|mom|parents|son|daughter|wife|husband|spouse|neighbor|neighbour|friend|enemy|man|woman|child|person|human|boss|relative|uncle|aunt|cousin|someone|somebody|anyone|anybody)\b",
            clean,
        )
        target = target_m.group(2) if target_m and target_m.group(2) else "another person"
        return {
            "type": "violent_harm",
            "action": action,
            "target": target,
            "query": query,
        }

    # 2. Direct violent imperative or queries: "kill my brother", "kill me brother", "kill my bro", "murder someone"
    direct_pattern = (
        r"\b(kill|murder|shoot|poison|stab|strangle|eliminate|slay)\s+"
        r"(?:my|me|his|her|their|someone|somebody|a\s+person|anyone|anybody|"
        r"brother|bro|sister|sis|father|dad|mother|mom|parents|son|daughter|wife|husband|spouse|neighbor|neighbour|friend|enemy|uncle|aunt|cousin)\b"
    )
    m2 = re.search(direct_pattern, clean)
    if m2:
        action = m2.group(1)
        # Check target
        target_m = re.search(
            r"\b(kill|murder|shoot|poison|stab|strangle|eliminate|slay)\s+"
            r"(?:my|me|his|her|their|someone|somebody|a\s+person|anyone|anybody)?\s*"
            r"(brother|bro|sister|sis|father|dad|mother|mom|parents|son|daughter|wife|husband|spouse|neighbor|neighbour|friend|enemy|uncle|aunt|cousin)?\b",
            clean,
        )
        target = target_m.group(2) if target_m and target_m.group(2) else "another person"
        return {
            "type": "violent_harm",
            "action": action,
            "target": target,
            "query": query,
        }

    # 3. Inquiries regarding whether killing / murder is legal: "is killing legal", "is murder allowed", "right to kill"
    legal_killing_pattern = r"\b(is\s+killing\s+legal|is\s+murder\s+legal|is\s+killing\s+allowed|legality\s+of\s+killing|right\s+to\s+kill)\b"
    if re.search(legal_killing_pattern, clean):
        return {
            "type": "violent_harm",
            "action": "kill",
            "target": "another person",
            "query": query,
        }

    return None


def synthesize_violent_harm_response(
    match_info: Dict[str, Any], query: str, role: str
) -> Tuple[str, List[str]]:
    """
    Synthesizes an immediate, unequivocal, authoritative legal declaration establishing
    that killing or causing physical harm is strictly prohibited under Indian Law,
    details the governing penal statutes (Section 300/302 IPC & Section 101/103 BNS),
    punishment (Death Penalty / Life Imprisonment), private defence boundaries,
    civil dispute remedies, and crisis emergency helplines.
    """
    target = match_info.get("target", "another person")
    if target in {"brother", "bro"}:
        target_str = "your brother"
    elif target in {"sister", "sis"}:
        target_str = "your sister"
    elif target in {"father", "dad"}:
        target_str = "your father"
    elif target in {"mother", "mom"}:
        target_str = "your mother"
    elif target in {"wife", "husband", "son", "daughter", "spouse", "cousin", "uncle", "aunt"}:
        target_str = f"your {target}"
    elif target in {"neighbor", "neighbour", "friend", "enemy", "boss", "relative"}:
        target_str = f"your {target}"
    elif target in {"another person", "the person in question", "someone", "somebody", "anyone", "anybody", "person", "human"}:
        target_str = "any human being"
    else:
        target_str = f"{target}"

    text = (
        f"### 🚨 ABSOLUTELY NOT: Killing Any Person is Strictly Illegal Under Indian Law\n\n"
        f"> ⚠️ **IMMEDIATE LEGAL DECLARATION**:\n"
        f"> **NO, you CANNOT kill {target_str} or any human being under any circumstances.**\n"
        f"> Under Indian Criminal Law, deliberately taking another person's life is strictly prohibited, "
        f"constitutes the grave capital offence of **MURDER**, and is punishable by **DEATH or IMPRISONMENT FOR LIFE**.\n\n"
        f"---\n\n"
        f"### ⚖️ Governing Penal Framework (IPC 1860 vs BNS 2023 Concordance)\n\n"
        f"| Legal Metric | Indian Penal Code (IPC 1860) | Bharatiya Nyaya Sanhita (BNS 2023) |\n"
        f"|---|---|---|\n"
        f"| **Substantive Offence** | **Section 300 IPC** (Definition of Murder) | **Section 101 BNS** |\n"
        f"| **Punishment Provision** | **Section 302 IPC** (Punishment for Murder) | **Section 103(1) BNS** |\n"
        f"| **Prescribed Penalty** | **Death Penalty or Life Imprisonment, and Fine** | **Death Penalty or Life Imprisonment, and Fine** |\n"
        f"| **Attempt to Murder** | **Section 307 IPC** (Up to 10 Years or Life Imprisonment) | **Section 109 BNS** |\n"
        f"| **Criminal Conspiracy** | **Section 120B IPC** (Treated as Co-Principal Offender) | **Section 61(2) BNS** |\n"
        f"| **Cognizability** | **Cognizable** (Police must arrest immediately without warrant) | **Cognizable** |\n"
        f"| **Bail Classification** | **Non-Bailable** (Bail is exception, strictly at Sessions discretion) | **Non-Bailable** |\n"
        f"| **Jurisdictional Court** | **Court of Session** (Exclusive Jurisdiction) | **Court of Session** |\n\n"
        f"---\n\n"
        f"### 🛡️ Why Self-Defence or Family Disputes Do NOT Justify Killing\n"
        f"1. **Strict Limits of Private Defence**: Under **Sections 96 to 106 IPC** (**Sections 34 to 44 BNS 2023**), "
        f"the right of private defence is strictly preventive and defensive. It extends to causing death *only* "
        f"when there is a reasonable, imminent apprehension of death or grievous hurt (*Darshan Singh v. State of Punjab, AIR 2010 SC 1212*).\n"
        f"2. **Zero Tolerance for Disputes, Anger, or Revenge**: Private defence **NEVER** justifies killing due to family quarrels, "
        f"property disputes, inheritance disagreements, verbal abuse, or past provocation. Any premeditated retaliation is classified as Murder under Section 300 IPC / Section 101 BNS.\n\n"
        f"---\n\n"
        f"### 🏛️ Lawful Remedies to Resolve Family & Sibling Disputes\n"
        f"If you are facing serious conflicts or disputes with family members or siblings, Indian law provides strict legal mechanisms to protect your rights:\n"
        f"• **Civil Partition Suit**: If the dispute involves ancestral or shared property, file a **Suit for Partition and Separate Possession** before the competent Civil Court under the Code of Civil Procedure (CPC, 1908).\n"
        f"• **Injunction to Protect Possession**: Apply for an **Ad-Interim Temporary Injunction** under Order 39 Rules 1 & 2 of CPC to restrain any family member from dispossessing you, creating third-party rights, or causing harm.\n"
        f"• **Criminal Complaint for Threats (Section 506 IPC / Sec 351 BNS)**: If you or your family are receiving threats, lodge a written complaint / FIR at the local police station for Criminal Intimidation.\n"
        f"• **Preventive Magisterial Action (Sec 107/116 CrPC / Sec 126/135 BNSS)**: Request the Executive Magistrate to initiate proceedings to bind over threatening parties to keep the peace.\n\n"
        f"---\n\n"
        f"### 🆘 Immediate Emergency Helplines & Crisis Support\n"
        f"If you are experiencing extreme distress, domestic conflict, or unsafe thoughts, immediate help is available:\n"
        f"• 🚨 **National Police Emergency Helpline**: **112** (or **100**)\n"
        f"• 🧠 **Tele-MANAS (Govt. of India 24x7 Mental Health Helpline)**: **14416** or **1800-891-4416** (Toll-Free)\n"
        f"• 🤝 **KIRAN Mental Health Support (Ministry of Social Justice)**: **1800-599-0019** (24x7 Free & Confidential)"
    )

    citations = [
        "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 300: Murder, Section 302: Capital Punishment)",
        "[Statute] Bharatiya Nyaya Sanhita (BNS), 2023 - Section 101 (Definition) & Section 103(1) (Punishment for Murder)",
        "[Landmark Precedent] Darshan Singh v. State of Punjab, AIR 2010 SC 1212 (Supreme Court on Limits of Private Defence)",
        "[Procedural Code] Code of Criminal Procedure, 1973 - First Schedule (Cognizable, Non-Bailable, Triable by Court of Session)",
    ]

    return text, citations


def synthesize_statutory_section_response(
    sec_key: str, statute_type: str, role: str
) -> Tuple[str, List[str]]:
    """
    Constructs an authoritative response stating WHAT IT IS PRIMARILY FOR in the very first sentence,
    followed by essential ingredients, exceptions, concordance, and strategy.
    """
    config = STATUTORY_REGISTRY.get(sec_key)
    if not config:
        return "", []

    title = config["title"]
    primary_purpose = config["primary_purpose"]
    definition = config["definition"]
    exceptions = config.get("exceptions", [])
    table_data = config["punishment_table"]
    strategy = (
        config["advocate_strategy"] if role == "advocate" else config["client_strategy"]
    )

    exceptions_block = ""
    if exceptions:
        exc_lines = "\n".join([f"• {e}" for e in exceptions])
        exceptions_block = (
            f"\n\n### 🛡️ The 5 Statutory Exceptions (When Causing Death is NOT Murder)\n"
            f"If death is caused under any of these five exceptions, the charge is reduced to **Culpable Homicide Not Amounting to Murder** (punishable under Section 304 IPC / Section 105 BNS instead of Section 302):\n"
            f"{exc_lines}"
        )

    # Build concordance table
    t_def_ipc, t_def_bns = table_data["definition_sec"]
    t_pun_ipc, t_pun_bns = table_data["punishment_sec"]
    t_pen_ipc, t_pen_bns = table_data["penalty"]
    t_cog_ipc, t_cog_bns = table_data["cognizance"]
    t_bail_ipc, t_bail_bns = table_data["bail"]
    t_court_ipc, t_court_bns = table_data["court"]

    table_markdown = (
        f"| Legal Metric | Indian Penal Code (IPC 1860) / Pre-2024 | Bharatiya Nyaya Sanhita (BNS 2023) |\n"
        f"|---|---|---|\n"
        f"| **Governing Definition** | **{t_def_ipc}** | **{t_def_bns}** |\n"
        f"| **Punishment Provision** | **{t_pun_ipc}** | **{t_pun_bns}** |\n"
        f"| **Prescribed Penalty** | {t_pen_ipc} | {t_pen_bns} |\n"
        f"| **Cognizability** | **{t_cog_ipc}** | **{t_cog_bns}** |\n"
        f"| **Bail Classification** | **{t_bail_ipc}** | **{t_bail_bns}** |\n"
        f"| **Jurisdictional Court** | **{t_court_ipc}** | **{t_court_bns}** |"
    )

    text = (
        f"### ⚖️ {title}\n\n"
        f"> 📌 **PRIMARY PURPOSE**: {primary_purpose}\n\n"
        f"### 📜 Statutory Definition & Essential Ingredients\n"
        f"{definition}"
        f"{exceptions_block}\n\n"
        f"### ⚖️ Statutory Framework (IPC vs BNS 2023 Concordance)\n"
        f"{table_markdown}\n\n"
        f"### 💡 Actionable Strategic Roadmap ({role.upper()} Perspective)\n"
        f"{strategy}\n\n"
        f"> **Disclaimer**: Educational legal prototype. Please verify all draftings with an Advocate before filing."
    )

    citations = config["citations"]
    return text, citations
