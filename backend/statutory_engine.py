"""
S2 Legal AI Pro - Specific Statutory Section & Article Legal Purpose Resolver
Module: backend.statutory_engine

Provides immediate, authoritative, primary-purpose legal explanations for specific
statutory sections and constitutional articles (e.g. IPC 300, IPC 420, IPC 302,
Article 21, Section 138 NI Act, Section 41A CrPC, Section 154 CrPC, Section 438 CrPC).

States WHAT IT IS PRIMARILY FOR in the very first sentence, followed by essential
elements, exceptions, IPC <-> BNS 2023 concordance, and actionable strategy.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple


STATUTORY_REGISTRY: Dict[str, Dict[str, Any]] = {
    # --------------------------------------------------------------------------
    # 1. IPC / BNS OFFENCES
    # --------------------------------------------------------------------------
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
    "304a": {
        "title": "Section 304A IPC: Causing Death by Negligence",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 106(1) BNS (General Negligence) & Section 106(2) BNS (Hit & Run)",
        "primary_purpose": (
            "**Section 304A of the Indian Penal Code (IPC) is primarily for CAUSING DEATH BY RASH OR NEGLIGENT ACT NOT AMOUNTING TO CULPABLE HOMICIDE.**\n"
            "It applies to fatal accidents resulting from rash driving, medical negligence, or industrial carelessness without an intention to kill. "
            "Under the **Bharatiya Nyaya Sanhita (BNS 2023)**, it is codified under **Section 106(1)** (punishable with up to 5 years imprisonment) "
            "and **Section 106(2)** (Hit and run punishable with up to 10 years)."
        ),
        "definition": (
            "**Statutory Text (Section 304A IPC)**:\n"
            "> *\"Whoever causes the death of any person by doing any rash or negligent act not amounting to culpable homicide, shall be punished with imprisonment of either description for a term which may extend to two years, or with fine, or with both.\"*\n\n"
            "**Key Elements**:\n"
            "1. Death of a human being.\n"
            "2. Act done with criminal rashness (recklessness) or criminal negligence (gross lack of reasonable care).\n"
            "3. Death must be the direct and proximate result of the rash or negligent act without intention."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 304A IPC", "Section 106(1) BNS"),
            "punishment_sec": ("Section 304A IPC", "Section 106(1) & (2) BNS"),
            "penalty": ("Imprisonment up to 2 years, or fine, or both", "Up to 5 years (General) / Up to 10 years (Hit & Run)"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Bailable", "Bailable / Non-Bailable (Hit & Run)"),
            "court": ("Magistrate of the first class", "Magistrate of the first class / Sessions"),
        },
        "advocate_strategy": (
            "• **Proximate Cause (*Causa Causans*)**: Establish whether the victim's own contributory negligence was the proximate cause of death.\n"
            "• **Medical Negligence (*Jacob Mathew*)**: For medical professionals, demand compliance with Supreme Court guidelines requiring an independent medical board opinion before prosecution.\n"
            "• **Bailable Nature**: Section 304A is bailable as of right before the Magistrate; arrange surety bonds immediately."
        ),
        "client_strategy": (
            "• **Furnish Bail**: You are legally entitled to bail at the police station or before the Magistrate upon furnishing solvent surety.\n"
            "• **Mechanical Inspection Report**: In motor accidents, obtain the Motor Vehicle Inspector (MVI) report showing brake or mechanical failure.\n"
            "• **MACT Linkage**: Criminal liability under 304A does not preclude insurance companies from paying compensation under Section 166 MV Act."
        ),
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 304A",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 106(1) & 106(2)",
            "[Landmark SC] Jacob Mathew v. State of Punjab (2005) 6 SCC 1 (Medical Negligence Standard)",
        ],
    },
    "304b": {
        "title": "Section 304B IPC: Dowry Death",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 80 BNS (Dowry Death)",
        "primary_purpose": (
            "**Section 304B of the Indian Penal Code (IPC) is primarily for DOWRY DEATH.**\n"
            "It penalizes the husband and in-laws when a woman dies under abnormal circumstances within 7 years of marriage having been subjected to cruelty or harassment for dowry soon before death. "
            "Under the **Bharatiya Nyaya Sanhita (BNS 2023)**, it is codified under **Section 80 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 304B IPC)**:\n"
            "> *\"Where the death of a woman is caused by any burns or bodily injury or occurs otherwise than under normal circumstances within seven years of her marriage and it is shown that soon before her death she was subjected to cruelty or harassment by her husband or any relative of her husband for, or in connection with, any demand for dowry, such death shall be called 'dowry death', and such husband or relative shall be deemed to have caused her death.\"*\n\n"
            "**Prescribed Sentence**: Imprisonment for a term which **shall not be less than seven years** but which may extend to **imprisonment for life**."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 304B IPC", "Section 80(1) BNS"),
            "punishment_sec": ("Section 304B(2) IPC", "Section 80(2) BNS"),
            "penalty": ("Imprisonment NOT less than 7 years, up to Life Imprisonment", "Imprisonment NOT less than 7 years, up to Life Imprisonment"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Court of Session", "Court of Session"),
        },
        "advocate_strategy": (
            "• **Rebut Section 113B Presumption**: Prove absence of proximate demand for dowry 'soon before death' (*Satbir Singh v. State of Haryana*).\n"
            "• **Alibi & Separate Residence for In-Laws**: Establish through rental deeds or employment records that distant in-laws lived separately (*Geeta Mehrotra*).\n"
            "• **Inquest Scrutiny**: Scrutinize statements given before the Sub-Divisional Magistrate (SDM) during the Section 176 CrPC inquest."
        ),
        "client_strategy": (
            "• **For Victim's Parents**: State all previous dowry demands truthfully before the Executive Magistrate (SDM); demand videography of post-mortem.\n"
            "• **For Accused Family**: Engage an advocate immediately; Section 304B is non-bailable and triable exclusively by the Sessions Court.\n"
            "• **Preserve Communications**: Keep WhatsApp messages, bank records, and call logs showing cordial family relations."
        ),
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 304B",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 80",
            "[Evidence Law] Indian Evidence Act, 1872 - Section 113B (Statutory Presumption of Dowry Death)",
            "[Landmark SC] Satbir Singh v. State of Haryana (2021) 6 SCC 1",
        ],
    },
    "307": {
        "title": "Section 307 IPC: Attempt to Murder",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 109 BNS (Attempt to Murder)",
        "primary_purpose": (
            "**Section 307 of the Indian Penal Code (IPC) is primarily for ATTEMPT TO MURDER.**\n"
            "It penalizes committing an act with such intention or knowledge and under such circumstances that, if death had been caused, the offender would be guilty of murder. "
            "Under the **Bharatiya Nyaya Sanhita (BNS 2023)**, it is codified under **Section 109 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 307 IPC)**:\n"
            "> *\"Whoever does any act with such intention or knowledge, and under such circumstances that, if he by that act caused death, he would be guilty of murder, shall be punished with imprisonment of either description for a term which may extend to ten years, and shall also be liable to fine; and if hurt is caused to any person by such act, the offender shall be liable either to imprisonment for life, or to such punishment as is hereinbefore mentioned.\"*\n\n"
            "**Key Elements**:\n"
            "1. Nature of weapon used (firearms, sharp lethal weapons).\n"
            "2. Vitality of the body part targeted (head, neck, chest).\n"
            "3. Number and severity of blows inflicted."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 307 IPC", "Section 109(1) BNS"),
            "punishment_sec": ("Section 307 IPC", "Section 109(1) BNS"),
            "penalty": ("Up to 10 years imprisonment & Fine; if hurt caused, up to Life Imprisonment", "Up to 10 years imprisonment; if hurt caused, up to Life"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Court of Session", "Court of Session"),
        },
        "advocate_strategy": (
            "• **Absence of Murderous Intention**: Demonstrate through Medico-Legal Certificate (MLC) that injuries were simple or non-vital, arguing charge reduction to Section 324/326 IPC.\n"
            "• **Private Defence**: Plead self-defence under Section 96/100 IPC if complainant party were the initial aggressors.\n"
            "• **Bail Parameters**: Argue parity, recovery of weapon, and completion of investigation to obtain regular bail under Section 480 BNSS (Section 439 CrPC)."
        ),
        "client_strategy": (
            "• **Immediate Sessions Court Bail**: Section 307 is non-bailable; apply for anticipatory bail or regular bail before the Sessions Court immediately.\n"
            "• **Preserve CCTV & Phone Location**: Prove your location and gather CCTV footage proving who initiated the altercation.\n"
            "• **Cross-MLC**: If you also sustained injuries, get examined at a government hospital to file a cross-complaint."
        ),
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 307",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 109",
            "[Landmark SC] State of Maharashtra v. Balram Bama Patil (1983) 2 SCC 28 (Intention in Section 307)",
        ],
    },
    "378": {
        "title": "Section 378 IPC: Offence of Theft",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 303(1) BNS (Definition) & Section 303(2) BNS (Punishment)",
        "primary_purpose": (
            "**Section 378 of the Indian Penal Code (IPC) is primarily for THEFT.**\n"
            "It defines the act of intending to take dishonestly any movable property out of the possession of any person without that person's consent, and moving that property in order to such taking. "
            "Punishment for theft is codified under **Section 379 IPC** (up to 3 years imprisonment or fine), and under the **Bharatiya Nyaya Sanhita (BNS 2023)** under **Section 303(2) BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 378 IPC)**:\n"
            "> *\"Whoever, intending to take dishonestly any movable property out of the possession of any person without that person's consent, moves that property in order to such taking, is said to commit theft.\"*\n\n"
            "**5 Essential Ingredients of Theft**:\n"
            "1. **Dishonest Intention**: Intention to cause wrongful gain or wrongful loss.\n"
            "2. **Movable Property**: Corporeal property capable of being moved (including cut trees, minerals once severed).\n"
            "3. **OutOf Possession**: Property must be in someone's possession (not abandoned).\n"
            "4. **Without Consent**: Express or implied consent absent.\n"
            "5. **Moving**: Physical movement of the property to effect the taking."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 378 IPC", "Section 303(1) BNS"),
            "punishment_sec": ("Section 379 IPC", "Section 303(2) BNS"),
            "penalty": ("Imprisonment up to 3 years, or fine, or both", "Imprisonment up to 3 years, or fine, or community service (under ₹5,000 upon return)"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Any Magistrate", "Any Magistrate"),
        },
        "advocate_strategy": (
            "• **Bona Fide Claim of Right**: If property was taken under honest assertion of title or ownership, dishonest intent is negated (*Chandi Kumar v. Abanidhar*).\n"
            "• **Notice in Lieu of Arrest (Section 35(3) BNSS)**: Since sentence is up to 3 years, arrest is impermissible without complying with Section 35(3) BNSS (*Arnesh Kumar*).\n"
            "• **Community Service (BNS 2023)**: For petty theft of property valued under ₹5,000 where property is returned, advocate can pray for community service instead of prison."
        ),
        "client_strategy": (
            "• **File Police FIR Immediately**: Report theft to police with purchase invoices, serial numbers, IMEI (for phones), or vehicle registration.\n"
            "• **Check Section 35(3) Notice**: If accused of theft under ₹5,000, you are entitled to pre-arrest notice and compounding.\n"
            "• **Preserve Purchase Receipts**: Maintain bills establishing that the property belongs lawfully to you."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Page 87, Section 378: Theft)",
            "[Statute] Indian Penal Code, 1860 - Section 378 & Section 379",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 303(1) & 303(2)",
        ],
    },
    "383": {
        "title": "Section 383 IPC: Offence of Extortion",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 308(1) BNS (Definition) & Section 308(2) BNS (Punishment)",
        "primary_purpose": (
            "**Section 383 of the Indian Penal Code (IPC) is primarily for EXTORTION (BLACKMAIL & COERCION).**\n"
            "It penalizes intentionally putting any person in fear of any injury to that person or to any other, and thereby dishonestly inducing the person so put in fear to deliver valuable property or security. "
            "Under the **Bharatiya Nyaya Sanhita (BNS 2023)**, it is codified under **Section 308 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 383 IPC)**:\n"
            "> *\"Whoever intentionally puts any person in fear of any injury to that person, or to any other, and thereby dishonestly induces the person so put in fear to deliver to any person any property or valuable security... commits 'extortion'.\"*\n\n"
            "**Punishment (Section 384 IPC / Section 308(2) BNS)**: Imprisonment up to 3 years, or fine, or both (Cognizable & Non-Bailable)."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 383 IPC", "Section 308(1) BNS"),
            "punishment_sec": ("Section 384 IPC", "Section 308(2) BNS"),
            "penalty": ("Imprisonment up to 3 years, or fine, or both", "Imprisonment up to 3 years, or fine, or both"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Magistrate of the first class", "Magistrate of the first class"),
        },
        "advocate_strategy": (
            "• **Delivery of Property is Mandatory**: Unlike intimidation, extortion requires actual delivery of property under fear. If no property was delivered, charge is attempt under Section 385/511.\n"
            "• **Quashing (Section 528 BNSS / Section 482 CrPC)**: If allegations arise from a civil commercial dispute, petition High Court for quashing.\n"
            "• **Bail Application**: Apply for regular bail citing compliance with Section 35(3) BNSS (*Arnesh Kumar*)."
        ),
        "client_strategy": (
            "• **Do Not Pay Extortionists**: Never pay; preserve call recordings, WhatsApp messages, and extortion notes as evidence.\n"
            "• **Lodge Police Complaint**: File written complaint at the local police station or Anti-Extortion Cell.\n"
            "• **Emergency Protection**: Dial 112 if facing immediate physical peril."
        ),
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 383 & Section 384",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 308",
            "[Landmark SC] Dhananjay v. State of Bihar (2007) 1 SCC 768",
        ],
    },
    "390": {
        "title": "Section 390 IPC: Offence of Robbery",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 309 BNS (Robbery)",
        "primary_purpose": (
            "**Section 390 of the Indian Penal Code (IPC) is primarily for ROBBERY.**\n"
            "It explains that in all robbery there is either theft or extortion, accompanied by causing or attempting to cause death, hurt, or wrongful restraint (or fear of instant death/hurt). "
            "Punishment for robbery is codified under **Section 392 IPC** (rigorous imprisonment up to 10 years; up to 14 years on highway at night), "
            "and under the **Bharatiya Nyaya Sanhita (BNS 2023)** under **Section 309 BNS**."
        ),
        "definition": (
            "**When Theft is Robbery**: Theft is robbery if the offender, in order to the committing of the theft, or in committing the theft, or in carrying away property obtained by the theft, voluntarily causes or attempts to cause death or hurt or wrongful restraint, or fear of instant death or instant hurt or instant wrongful restraint.\n\n"
            "**When Extortion is Robbery**: Extortion is robbery if the offender, at the time of committing the extortion, is in the presence of the person put in fear, and commits the extortion by putting that person in fear of instant death, instant hurt, or instant wrongful restraint."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 390 IPC", "Section 309(1) BNS"),
            "punishment_sec": ("Section 392 IPC", "Section 309(2) BNS"),
            "penalty": ("Rigorous imprisonment up to 10 years & Fine (up to 14 years on highway at night)", "Rigorous imprisonment up to 10 years (up to 14 years on highway)"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Magistrate First Class / Court of Session", "Magistrate First Class / Court of Session"),
        },
        "advocate_strategy": (
            "• **Test Identification Parade (TIP)**: Challenge the validity of TIP under Section 54A CrPC / Section 54 BNSS if suspect was shown to witnesses beforehand.\n"
            "• **Absence of Deadly Weapon**: If no deadly weapon was used, defend against the 7-year minimum statutory bar under Section 397 IPC.\n"
            "• **Recovery Challenges**: Challenge seizure memo under Section 27 Evidence Act / Section 23 BSA for lack of independent panch witnesses."
        ),
        "client_strategy": (
            "• **Report Immediately**: Dial 112 immediately to enable police highway barricades and prompt recovery.\n"
            "• **Do Not Resist Armed Robbers**: Safety of life is primary; observe physical traits, scars, vehicle plates for police identification.\n"
            "• **Non-Bailable Offence**: Robbery is non-bailable; bail requires moving the Sessions Court through an advocate."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 390: Robbery)",
            "[Statute] Indian Penal Code, 1860 - Section 390 & Section 392",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 309",
        ],
    },
    "391": {
        "title": "Section 391 IPC: Offence of Dacoity",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 310 BNS (Dacoity)",
        "primary_purpose": (
            "**Section 391 of the Indian Penal Code (IPC) is primarily for DACOITY (ROBBERY BY FIVE OR MORE PERSONS).**\n"
            "When five or more persons conjointly commit or attempt to commit a robbery, every person so committing, attempting, or aiding is said to commit dacoity. "
            "Punishment for dacoity is codified under **Section 395 IPC** (**Imprisonment for Life or rigorous imprisonment up to 10 years, and Fine**), "
            "and under the **Bharatiya Nyaya Sanhita (BNS 2023)** under **Section 310 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 391 IPC)**:\n"
            "> *\"When five or more persons conjointly commit or attempt to commit a robbery, or where the whole number of persons conjointly committing or attempting to commit a robbery, and persons present and aiding such commission or attempt, amount to five or more, every person so committing, attempting or aiding, is said to commit 'dacoity'.\"*\n\n"
            "**Key Difference between Robbery and Dacoity**: Robbery involves 1 to 4 persons. The moment **5 or more persons** participate conjointly, the offence escalates to Dacoity."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 391 IPC", "Section 310(1) BNS"),
            "punishment_sec": ("Section 395 IPC", "Section 310(2) BNS"),
            "penalty": ("Imprisonment for Life, or Rigorous Imprisonment up to 10 years, and Fine", "Imprisonment for Life, or Rigorous Imprisonment up to 10 years, and Fine"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Court of Session", "Court of Session"),
        },
        "advocate_strategy": (
            "• **Scrutinize Number of Participants**: If the evidence proves fewer than 5 persons participated, the charge of dacoity fails and drops to robbery.\n"
            "• **Test Identification Parade (TIP)**: Challenge dock identification if no prior judicial TIP was conducted.\n"
            "• **Strict Bail Scrutiny**: Dacoity is Category C in *Satender Kumar Antil*; bail is strictly at Sessions/High Court discretion."
        ),
        "client_strategy": (
            "• **Dacoity with Murder (Section 396 IPC)**: If any member commits murder during dacoity, ALL members are liable to the **Death Penalty or Life Imprisonment**.\n"
            "• **Seek Sessions Court Counsel**: Triable exclusively by the Court of Session; engage experienced criminal defense counsel.\n"
            "• **Cooperate with Inquest & TIP**: Victims must attend TIP before the Magistrate to identify perpetrators."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 391: Dacoity)",
            "[Statute] Indian Penal Code, 1860 - Section 391 & Section 395",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 310",
        ],
    },
    "405": {
        "title": "Section 405 IPC: Criminal Breach of Trust",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 316 BNS (Criminal Breach of Trust)",
        "primary_purpose": (
            "**Section 405 of the Indian Penal Code (IPC) is primarily for CRIMINAL BREACH OF TRUST.**\n"
            "It penalizes anyone who, being in any manner entrusted with property or dominion over property, dishonestly misappropriates or converts that property to their own use, "
            "or dishonestly uses or disposes of that property in violation of any legal direction. "
            "Punishment is prescribed under **Section 406 IPC** (up to 3 years imprisonment or fine), and under the **Bharatiya Nyaya Sanhita (BNS 2023)** under **Section 316 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 405 IPC)**:\n"
            "> *\"Whoever, being in any manner entrusted with property, or with any dominion over property, dishonestly misappropriates or converts to his own use that property, or dishonestly uses or disposes of that property in violation of any direction of law... commits 'criminal breach of trust'.\"*\n\n"
            "**Essential Ingredients**:\n"
            "1. **Entrustment**: Complainant handed over property or dominion over property to the accused in trust.\n"
            "2. **Dishonest Misappropriation**: Accused converted the property to their own use or violated the trust condition."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 405 IPC", "Section 316(1) BNS"),
            "punishment_sec": ("Section 406 IPC", "Section 316(2) BNS"),
            "penalty": ("Imprisonment up to 3 years, or fine, or both", "Imprisonment up to 3 years, or fine, or both"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Magistrate of the first class", "Magistrate of the first class"),
        },
        "advocate_strategy": (
            "• **Distinguish from Civil Breach of Contract**: Mere failure to pay debt is civil; prosecution must prove dishonest misappropriation of entrusted property (*Jaswantlal Nathalal*).\n"
            "• **Stridhan Misappropriation**: For retained marriage gifts, cite *Pratibha Rani v. Suraj Kumar* (Section 405/406 IPC applies to husband withholding Stridhan).\n"
            "• **Notice in Lieu of Arrest**: Enforce Section 35(3) BNSS (*Arnesh Kumar*) safeguards against mechanical arrest."
        ),
        "client_strategy": (
            "• **Maintain Proof of Handover**: Keep receipts, bank transfers, or written agreements proving the property was given in trust.\n"
            "• **Stridhan Claims**: Wives can file complaint under Section 406 IPC for recovery of gold jewellery and dowry gifts retained by in-laws.\n"
            "• **Security Deposit Recovery**: Landlord refusing to return tenant deposit after vacating can be prosecuted under Section 406 IPC."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Page 94, Section 405: Criminal Breach of Trust)",
            "[Statute] Indian Penal Code, 1860 - Section 405 & Section 406",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 316",
            "[Landmark SC] Pratibha Rani v. Suraj Kumar (1985) 2 SCC 370 (Stridhan Entrustment)",
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
    "441": {
        "title": "Section 441 IPC: Criminal Trespass",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 329 BNS (Criminal Trespass)",
        "primary_purpose": (
            "**Section 441 of the Indian Penal Code (IPC) is primarily for CRIMINAL TRESPASS.**\n"
            "It penalizes entering into or upon property in possession of another with intent to commit an offence, or to intimidate, insult, or annoy any person in possession, "
            "or unlawfully remaining there with intent to intimidate, insult, or annoy. "
            "Punishment is codified under **Section 447 IPC** (imprisonment up to 3 months and fine) and under **Section 329 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 441 IPC)**:\n"
            "> *\"Whoever enters into or upon property in the possession of another with intent to commit an offence or to intimidate, insult or annoy any person in possession of such property... is said to commit 'criminal trespass'.\"*\n\n"
            "**House Trespass (Section 442 IPC / Section 329(2) BNS)**: Criminal trespass by entering into any building, tent, or vessel used as human dwelling."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 441 IPC", "Section 329(1) BNS"),
            "punishment_sec": ("Section 447 IPC", "Section 329(3) BNS"),
            "penalty": ("Imprisonment up to 3 months, or fine up to ₹500, or both", "Imprisonment up to 3 months, or fine up to ₹5,000, or both"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Bailable", "Bailable"),
            "court": ("Any Magistrate", "Any Magistrate"),
        },
        "advocate_strategy": (
            "• **Actual Physical Possession**: Prosecution must establish that complainant was in actual physical possession on the date of trespass.\n"
            "• **Civil Injunction Alongside**: File suit for Perpetual Injunction under Section 38 Specific Relief Act with Order 39 interim stay.\n"
            "• **Bailable Nature**: Section 447 is bailable as of right."
        ),
        "client_strategy": (
            "• **Document Boundaries**: Keep certified Khata/Patta and boundary demarcation reports ready.\n"
            "• **Erect Warning Signboard**: Put up clear private property board.\n"
            "• **Dial 112**: Call emergency police if someone attempts unauthorized construction."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 441: Criminal Trespass)",
            "[Statute] Indian Penal Code, 1860 - Section 441 & Section 447",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 329",
        ],
    },
    "463": {
        "title": "Section 463 IPC: Offence of Forgery",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 336 BNS (Forgery)",
        "primary_purpose": (
            "**Section 463 of the Indian Penal Code (IPC) is primarily for FORGERY.**\n"
            "It defines the making of any false document or false electronic record with intent to cause damage or injury to the public or any person, "
            "or to support any claim or title, or to cause any person to part with property. "
            "Punishment for forgery is codified under **Section 465 IPC** (up to 2 years imprisonment or fine), and under **Section 336 BNS**."
        ),
        "definition": (
            "**Making a False Document (Section 464 IPC / Section 335 BNS)**:\n"
            "A person makes a false document if they dishonestly or fraudulently sign, seal, or execute a document without authority, "
            "or alter a document without authority after it has been executed."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 463 IPC", "Section 336(1) BNS"),
            "punishment_sec": ("Section 465 IPC", "Section 336(2) BNS"),
            "penalty": ("Imprisonment up to 2 years, or fine, or both", "Imprisonment up to 2 years, or fine, or both"),
            "cognizance": ("Non-Cognizable (Cognizable under BNS)", "Cognizable"),
            "bail": ("Bailable", "Bailable"),
            "court": ("Magistrate of the first class", "Magistrate of the first class"),
        },
        "advocate_strategy": (
            "• **Forensic Handwriting Comparison**: Move application under Section 45 Evidence Act / Section 39 BSA to send signatures to CFSL/FSL.\n"
            "• **Valuable Security Escalation**: If the forged document is a Will or Sale Deed, urge invocation of Section 467 IPC (Life Imprisonment).\n"
            "• **Civil Cancellation**: File civil suit under Section 31 Specific Relief Act for cancellation of forged instrument."
        ),
        "client_strategy": (
            "• **Obtain Certified Copy**: Download certified copy of the forged document from the Sub-Registrar or bank.\n"
            "• **Preserve Admitted Signatures**: Collate standard admitted signatures of the victim from old bank accounts or government records.\n"
            "• **Lodge FIR**: File criminal complaint; if police refuse, file application under Section 156(3) CrPC before Magistrate."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 463: Forgery)",
            "[Statute] Indian Penal Code, 1860 - Section 463 & Section 465",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 336",
        ],
    },
    "467": {
        "title": "Section 467 IPC: Forgery of Valuable Security, Will, etc.",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 338 BNS (Forgery of Valuable Security)",
        "primary_purpose": (
            "**Section 467 of the Indian Penal Code (IPC) is primarily for FORGERY OF A VALUABLE SECURITY, WILL, OR AUTHORITY TO TRANSFER PROPERTY.**\n"
            "It is a grave, non-bailable felony penalizing anyone who forges a document purporting to be a valuable security (e.g. Sale Deed, Cheque, Promissory Note) or a Will. "
            "It is punishable with **IMPRISONMENT FOR LIFE**, or imprisonment up to **10 years**, and fine. "
            "Under the **Bharatiya Nyaya Sanhita (BNS 2023)**, it is codified under **Section 338 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 467 IPC)**:\n"
            "> *\"Whoever forges a document which purports to be a valuable security or a will, or an authority to make or transfer any valuable security, or to receive the principal, interest or dividends thereon... shall be punished with imprisonment for life, or with imprisonment of either description for a term which may extend to ten years, and shall also be liable to fine.\"*"
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 467 IPC", "Section 338 BNS"),
            "punishment_sec": ("Section 467 IPC", "Section 338 BNS"),
            "penalty": ("Imprisonment for Life, or imprisonment up to 10 years, and Fine", "Imprisonment for Life, or imprisonment up to 10 years, and Fine"),
            "cognizance": ("Cognizable", "Cognizable"),
            "bail": ("Non-Bailable", "Non-Bailable"),
            "court": ("Magistrate of the first class", "Magistrate of the first class"),
        },
        "advocate_strategy": (
            "• **Valuable Security Definition**: Ensure the forged document falls under Section 30 IPC definition of 'valuable security'.\n"
            "• **Oppose Bail**: Rigorously oppose bail citing life imprisonment sentence and non-bailable nature.\n"
            "• **CFSL Handwriting Opinion**: Insist on state forensic examination of signatures."
        ),
        "client_strategy": (
            "• **Severe Non-Bailable Charge**: Forging a property sale deed or will is a major crime punishable with Life Imprisonment.\n"
            "• **File Injunction in Civil Court**: Seek immediate Order 39 stay on the property schedule so the forged deed cannot be used.\n"
            "• **Inform Sub-Registrar**: Submit written letter alerting Sub-Registrar not to entertain transfers on the disputed property."
        ),
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 467",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 338",
            "[Landmark SC] Suraj Lamp & Industries v. State of Haryana (2012) 1 SCC 656",
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
    "499": {
        "title": "Section 499 IPC: Offence of Defamation",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 356(1) BNS (Defamation)",
        "primary_purpose": (
            "**Section 499 of the Indian Penal Code (IPC) is primarily for CRIMINAL DEFAMATION.**\n"
            "It defines the making or publishing of any imputation concerning any person, intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person. "
            "Punishment is codified under **Section 500 IPC** (simple imprisonment up to 2 years or fine or both), and under **Section 356 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 499 IPC)**:\n"
            "> *\"Whoever, by words either spoken or intended to be read, or by signs or by visible representations, makes or publishes any imputation concerning any person intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person, is said... to defame that person.\"*\n\n"
            "**10 Statutory Exceptions**: Including imputation of truth made for public good, public conduct of public servants, merits of public performance, and bona fide censure."
        ),
        "exceptions": [
            "**First Exception**: Imputation of truth which public good requires to be made or published.",
            "**Second Exception**: Public conduct of public servants.",
            "**Third Exception**: Conduct of any person touching any public question.",
            "**Eighth Exception**: Accusation preferred in good faith to authorized person.",
            "**Ninth Exception**: Imputation made in good faith by person for protection of his or other's interests.",
        ],
        "punishment_table": {
            "definition_sec": ("Section 499 IPC", "Section 356(1) BNS"),
            "punishment_sec": ("Section 500 IPC", "Section 356(2) BNS"),
            "penalty": ("Simple imprisonment up to 2 years, or fine, or both", "Simple imprisonment up to 2 years, or fine, or both, or community service"),
            "cognizance": ("Non-Cognizable (Private Complaint)", "Non-Cognizable"),
            "bail": ("Bailable", "Bailable"),
            "court": ("Magistrate of the first class", "Magistrate of the first class"),
        },
        "advocate_strategy": (
            "• **Establish Publication**: Lead proof that defamatory material was disseminated to at least one third party.\n"
            "• **Plead Exceptions**: For defense, establish bona fides and truth for public good under First/Ninth Exception.\n"
            "• **Electronic Certificate**: Ensure compliance with Section 63 BSA / 65B Evidence Act for online printouts."
        ),
        "client_strategy": (
            "• **Cease and Desist Notice**: Serve legal notice demanding deletion of defamatory posts and public apology within 48 hours.\n"
            "• **Civil Damages Claim**: File civil suit alongside criminal complaint to seek compensation for business or personal harm.\n"
            "• **Preserve URLs**: Archive screenshots and web links before the poster deletes them."
        ),
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 499 & Section 500",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 356",
            "[Landmark SC] Subramanian Swamy v. Union of India (2016) 7 SCC 221",
        ],
    },
    "503": {
        "title": "Section 503 IPC: Criminal Intimidation",
        "act": "Indian Penal Code, 1860",
        "bns_equiv": "Section 351 BNS (Criminal Intimidation)",
        "primary_purpose": (
            "**Section 503 of the Indian Penal Code (IPC) is primarily for CRIMINAL INTIMIDATION (THREATS).**\n"
            "It penalizes threatening another with injury to their person, reputation, or property, or to the person or reputation of anyone in whom that person is interested, "
            "with intent to cause alarm to that person, or to cause that person to do any act which they are not legally bound to do. "
            "Punishment is codified under **Section 506 IPC** (up to 2 years; up to 7 years if threat is to cause death or grievous hurt), "
            "and under **Section 351 BNS**."
        ),
        "definition": (
            "**Statutory Text (Section 503 IPC)**:\n"
            "> *\"Whoever threatens another with any injury to his person, reputation or property, or to the person or reputation of any one in whom that person is interested, with intent to cause alarm to that person... commits criminal intimidation.\"*\n\n"
            "**Section 506 Part II (Threat to Cause Death)**: If threat be to cause death or grievous hurt, or destruction of property by fire, imprisonment up to **7 years and Fine**."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 503 IPC", "Section 351(1) BNS"),
            "punishment_sec": ("Section 506 Part I / II IPC", "Section 351(2) / (3) BNS"),
            "penalty": ("Up to 2 years (Part I) / Up to 7 years (Part II - Threat to kill)", "Up to 2 years / Up to 7 years (Threat to cause death)"),
            "cognizance": ("Non-Cognizable (Part I) / Cognizable (Part II in many states)", "Cognizable / Non-Cognizable"),
            "bail": ("Bailable", "Bailable / Non-Bailable (State amendments)"),
            "court": ("Any Magistrate / Magistrate First Class", "Magistrate of the first class"),
        },
        "advocate_strategy": (
            "• **Intent to Cause Alarm**: Mere words without causing actual alarm do not constitute criminal intimidation (*Amitabh Adhar v. NCT of Delhi*).\n"
            "• **Part II Escalation**: Ensure FIR incorporates Section 506 Part II if threat involved killing or burning property.\n"
            "• **Preventive Action**: Apply before Executive Magistrate under Section 107/116 CrPC to bind over respondent to keep peace."
        ),
        "client_strategy": (
            "• **Record Threatening Calls**: Save audio recordings and WhatsApp voice notes of threats.\n"
            "• **Lodge Police Complaint**: File written complaint for criminal intimidation at police station; dial 112.\n"
            "• **Police Protection**: Request police security if threats come from known criminals or gangs."
        ),
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 503 & Section 506",
            "[BNS Concordance] Bharatiya Nyaya Sanhita, 2023 - Section 351",
            "[Landmark SC] Vikram Johar v. State of U.P. (2019) 14 SCC 207",
        ],
    },

    # --------------------------------------------------------------------------
    # 2. CONSTITUTIONAL ARTICLES
    # --------------------------------------------------------------------------
    "14": {
        "title": "Article 14: Equality Before Law & Equal Protection of the Laws",
        "act": "Constitution of India, 1950",
        "bns_equiv": "Part III Fundamental Right (Supreme Lex)",
        "primary_purpose": (
            "**Article 14 of the Constitution of India is primarily for THE FUNDAMENTAL RIGHT TO EQUALITY.**\n"
            "It mandates that *\"The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India.\"* "
            "It strikes down arbitrary state action, unfair executive classifications, and discrimination."
        ),
        "definition": (
            "**Two Pillars of Article 14**:\n"
            "1. **Equality Before Law (Negative Concept - English Common Law)**: Absence of any special privilege in favor of any individual; all individuals are subject to the ordinary law of the land.\n"
            "2. **Equal Protection of Laws (Positive Concept - US Constitution)**: Equality of treatment under equal circumstances, permitting **Reasonable Classification** based on an intelligible differentia having a rational nexus to the object sought to be achieved.\n"
            "3. **Doctrine of Non-Arbitrariness (*E.P. Royappa* & *Maneka Gandhi*)**: Arbitrariness and equality are sworn enemies; an arbitrary act of the State violates Article 14."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Article 14 Constitution of India", "Part III Fundamental Right"),
            "punishment_sec": ("Enforceable via Articles 32 & 226", "Writ Jurisdiction"),
            "penalty": ("State Action Declared Void (Article 13)", "Constitutional Mandate"),
            "cognizance": ("Applicable against State (Article 12)", "State Instrumentalities"),
            "bail": ("Equal treatment in bail jurisprudence", "Article 14 Fairness"),
            "court": ("Supreme Court & High Courts", "Constitutional Benches"),
        },
        "advocate_strategy": (
            "• **Challenge Arbitrary State Action**: Move writ petition under Article 226/32 challenging government orders, tender cancellations, or discriminatory notifications as arbitrary and violative of Article 14.\n"
            "• **Test of Reasonable Classification**: Demonstrate absence of 'intelligible differentia' or absence of 'rational nexus'.\n"
            "• **Parity in Criminal Bail**: In bail applications, plead parity under Article 14 where similarly situated co-accused have been granted bail."
        ),
        "client_strategy": (
            "• **Protection Against Discrimination**: Government departments, public universities, and PSU employers cannot treat you arbitrarily or discriminate against you.\n"
            "• **Challenge Tender / Exam Irregularities**: You can approach the High Court immediately if government recruitment or tenders show favoritism.\n"
            "• **Legal Aid Access**: Under Article 14 and Article 39A, underprivileged persons are entitled to equal access to justice through free legal aid."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/constitution/ (Constitution of India - Article 14)",
            "[Landmark SC] E.P. Royappa v. State of Tamil Nadu (1974) 4 SCC 3 (Non-Arbitrariness Doctrine)",
            "[Landmark SC] Shayara Bano v. Union of India (2017) 9 SCC 1 (Manifest Arbitrariness)",
        ],
    },
    "19": {
        "title": "Article 19: Protection of Six Democratic Freedoms",
        "act": "Constitution of India, 1950",
        "bns_equiv": "Part III Fundamental Right (Supreme Lex)",
        "primary_purpose": (
            "**Article 19 of the Constitution of India is primarily for THE SIX DEMOCRATIC FREEDOMS OF CITIZENS.**\n"
            "It guarantees: (a) Freedom of speech and expression, (b) Freedom to assemble peacefully without arms, "
            "(c) Freedom to form associations or unions, (d) Freedom to move freely throughout India, "
            "(e) Freedom to reside and settle in any part of India, and (g) Freedom to practice any profession, trade, or business, "
            "subject only to reasonable restrictions specified in Clauses (2) to (6)."
        ),
        "definition": (
            "**The 6 Guaranteed Freedoms (Article 19(1))**:\n"
            "• **19(1)(a)**: Freedom of speech and expression (includes freedom of press, right to know, right to internet).\n"
            "• **19(1)(b)**: Peaceful assembly without arms.\n"
            "• **19(1)(c)**: Right to form associations, unions, or co-operative societies.\n"
            "• **19(1)(d)**: Free movement throughout the territory of India.\n"
            "• **19(1)(e)**: Right to reside and settle anywhere in India.\n"
            "• **19(1)(g)**: Right to practice any profession or carry on any occupation, trade, or business.\n\n"
            "**Reasonable Restrictions (Article 19(2))**: Restrictions can only be imposed by law on grounds of sovereignty, integrity of India, security of State, friendly relations with foreign States, public order, decency, morality, or contempt of court."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Article 19 Constitution of India", "Part III Fundamental Right"),
            "punishment_sec": ("Enforceable via Articles 32 & 226", "Writ Jurisdiction"),
            "penalty": ("Unreasonable State Restrictions Struck Down", "Constitutional Remedy"),
            "cognizance": ("Enforceable by Indian Citizens", "Citizen Rights"),
            "bail": ("Proportionality of Bail Conditions", "Free Movement Safeguards"),
            "court": ("Supreme Court & High Courts", "Constitutional Benches"),
        },
        "advocate_strategy": (
            "• **Proportionality Test**: Challenge speech curbs, internet bans, or protest prohibitions under the 4-pronged proportionality test (*Anuradha Bhasin*).\n"
            "• **Quash Speech FIRs**: File High Court quashing for Section 153A/295A/505 IPC charges where bona fide political criticism is falsely prosecuted (*Shreya Singhal*).\n"
            "• **Business Restrictions**: Challenge arbitrary municipal trade licensing curbs under Article 19(1)(g)."
        ),
        "client_strategy": (
            "• **Right to Criticize Government**: Constructive criticism of government policies is protected speech and does not constitute sedition or crime.\n"
            "• **Internet Access Protected**: Supreme Court recognized internet access as an integral part of freedom of speech under Article 19(1)(a).\n"
            "• **Challenge Gag Orders**: State cannot impose sweeping gag orders on media without satisfying strict public order necessity."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/constitution/ (Constitution of India - Article 19)",
            "[Landmark SC] Shreya Singhal v. Union of India (2015) 5 SCC 1 (Free Speech Online)",
            "[Landmark SC] Anuradha Bhasin v. Union of India (2020) 3 SCC 637 (Internet as Right under Art 19)",
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
    "32": {
        "title": "Article 32: Right to Constitutional Remedies (Supreme Court Writ Jurisdiction)",
        "act": "Constitution of India, 1950",
        "bns_equiv": "Part III Fundamental Right (The Heart & Soul of the Constitution)",
        "primary_purpose": (
            "**Article 32 of the Constitution of India is primarily for THE RIGHT TO CONSTITUTIONAL REMEDIES (Writ Jurisdiction of the Supreme Court).**\n"
            "Described by Dr. B.R. Ambedkar as the *'heart and soul of the Constitution'*, Article 32 guarantees the fundamental right to move the Supreme Court directly "
            "for the enforcement of any Fundamental Right via the five prerogative writs: Habeas Corpus, Mandamus, Prohibition, Quo Warranto, and Certiorari."
        ),
        "definition": (
            "**The 5 Prerogative Writs under Article 32**:\n"
            "1. **Habeas Corpus ('Produce the Body')**: Issued against illegal detention or unlawful police custody.\n"
            "2. **Mandamus ('We Command')**: Issued to compel a public official, court, or government department to perform a mandatory statutory duty.\n"
            "3. **Certiorari ('To Be Certified')**: Issued to quash an order passed by a lower court, tribunal, or quasi-judicial body without jurisdiction or in violation of natural justice.\n"
            "4. **Prohibition**: Issued to prevent an inferior court or tribunal from exceeding its jurisdiction while proceedings are pending.\n"
            "5. **Quo Warranto ('By What Authority')**: Issued to challenge the usurpation of a public office by an unqualified person."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Article 32 Constitution of India", "Part III Fundamental Right"),
            "punishment_sec": ("Article 32(2) Powers of Supreme Court", "Issue directions, orders, or writs"),
            "penalty": ("Binding on all Authorities in India (Article 144)", "Supreme Lex Enforcement"),
            "cognizance": ("Direct Petition before Supreme Court", "Original Jurisdiction"),
            "bail": ("Supreme Court Plenary Power under Art 142", "Complete Justice"),
            "court": ("Supreme Court of India (Apex Court)", "New Delhi"),
        },
        "advocate_strategy": (
            "• **Direct Approach Justification**: Plead why High Court remedy under Article 226 is inadequate or why pan-India fundamental right violation requires Apex Court intervention.\n"
            "• **Public Interest Litigation (PIL)**: Invoke relaxation of locus standi for marginalized communities under Article 32 (*Bandhua Mukti Morcha*).\n"
            "• **Complete Justice (Article 142)**: Pray for invocation of Article 142 to pass equitable orders."
        ),
        "client_strategy": (
            "• **Apex Court Protection**: You have a guaranteed constitutional right to approach the Supreme Court directly if your fundamental rights are violated by the State.\n"
            "• **Approach High Court First**: In individual disputes, Supreme Court often directs petitioners to exhaust High Court remedies under Article 226 first.\n"
            "• **Supreme Court Legal Aid**: Underprivileged citizens can access the Supreme Court Legal Services Committee (SCLSC) for free advocate representation."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/constitution/ (Constitution of India - Article 32)",
            "[Landmark SC] Kesavananda Bharati v. State of Kerala (1973) 4 SCC 225 (Basic Structure)",
            "[Landmark SC] Bandhua Mukti Morcha v. Union of India (1984) 3 SCC 161 (PIL Doctrine)",
        ],
    },
    "226": {
        "title": "Article 226: Power of High Courts to Issue Writs",
        "act": "Constitution of India, 1950",
        "bns_equiv": "Part VI Extraordinary Constitutional Jurisdiction",
        "primary_purpose": (
            "**Article 226 of the Constitution of India is primarily for THE EXTRAORDINARY WRIT JURISDICTION OF HIGH COURTS.**\n"
            "It empowers High Courts throughout India to issue directions, orders, or writs (including Habeas Corpus, Mandamus, Prohibition, Quo Warranto, and Certiorari) "
            "for the enforcement of Fundamental Rights **AND FOR ANY OTHER PURPOSE** (statutory, contractual, or civil legal rights). "
            "Its scope is wider than Article 32."
        ),
        "definition": (
            "**Key Constitutional Facets of Article 226**:\n"
            "1. **Wider Scope than Supreme Court (Article 32)**: While Article 32 is restricted strictly to Fundamental Rights, Article 226 can be invoked for Fundamental Rights *and for any other legal right*.\n"
            "2. **Territorial Jurisdiction (Clause 2)**: Exercisable where the cause of action wholly or in part arises within the State, even if the government authority is located outside.\n"
            "3. **Judicial Review of Administrative Action**: Quashing illegal government tenders, disciplinary inquiries, police inaction, or university decisions."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Article 226 Constitution of India", "Constitutional Jurisdiction of High Courts"),
            "punishment_sec": ("Article 226(1) & (3)", "Interim orders and final writs"),
            "penalty": ("Quashing of State Orders & Direction to Comply", "Contempt under Contempt of Courts Act"),
            "cognizance": ("High Court of the State", "Original Jurisdiction"),
            "bail": ("Writ of Habeas Corpus & Bail Jurisdiction", "High Court Roster Benches"),
            "court": ("High Courts across India", "Principal Seats & Benches"),
        },
        "advocate_strategy": (
            "• **Exhaustion of Alternative Remedy**: High Courts ordinarily require exhaustion of statutory tribunals; demonstrate why alternative remedy is illusory or that natural justice was violated (*Whirlpool Corp v. Registrar of Trade Marks*).\n"
            "• **Interim Stay (Article 226(3))**: Move for ad-interim stay on government recovery notices or demolitions.\n"
            "• **Police Protection & Inaction**: File writ of mandamus directing registration of FIR or provision of security."
        ),
        "client_strategy": (
            "• **Fastest State Protection**: High Court is the highest judicial authority in your state; writ petitions are taken up quickly for urgent personal liberty issues.\n"
            "• **Challenge Unfair Government Orders**: Any arbitrary cancellation of licenses, land acquisition notices, or employment dismissals can be stayed under Article 226.\n"
            "• **High Court Legal Services**: You can apply to the High Court Legal Services Committee for free legal representation if eligible."
        ),
        "citations": [
            "[Local ChromaDB] backend/data/constitution/ (Constitution of India - Article 226)",
            "[Landmark SC] Whirlpool Corp v. Registrar of Trade Marks (1998) 8 SCC 1 (Exceptions to Alternative Remedy)",
            "[Landmark SC] L. Chandra Kumar v. Union of India (1997) 3 SCC 261 (Judicial Review as Basic Structure)",
        ],
    },

    # --------------------------------------------------------------------------
    # 3. PROCEDURAL STATUTES (CrPC / BNSS / NI ACT)
    # --------------------------------------------------------------------------
    "41a": {
        "title": "Section 41A CrPC: Notice of Appearance Before Police Officer",
        "act": "Code of Criminal Procedure, 1973",
        "bns_equiv": "Section 35(3) BNSS, 2023",
        "primary_purpose": (
            "**Section 41A of the Code of Criminal Procedure (CrPC) is primarily for MANDATORY NOTICE OF APPEARANCE IN LIEU OF ARREST.**\n"
            "It mandates that for offences punishable with imprisonment up to 7 years, police **SHALL NOT mechanically arrest the accused**. "
            "Instead, the police MUST issue a formal written Notice of Appearance directing the person to join investigation. "
            "Under the **Bharatiya Nagarik Suraksha Sanhita (BNSS 2023)**, it is codified under **Section 35(3) BNSS**."
        ),
        "definition": (
            "**Statutory Text (Section 41A CrPC / Section 35(3) BNSS)**:\n"
            "> *\"The police officer shall, in all cases where the arrest of a person is not required under the provisions of sub-section (1) of section 41, issue a notice directing the person against whom a reasonable complaint has been made... to appear before him or at such other place as may be specified in the notice.\"*\n\n"
            "**Right Against Arrest**: So long as the person complies with and continues to comply with the notice, they **SHALL NOT BE ARRESTED** unless the police officer records reasons in writing and obtains prior permission from the Magistrate."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 41A CrPC", "Section 35(3) BNSS"),
            "punishment_sec": ("Section 41A(3) Arrest on non-compliance", "Section 35(5) BNSS"),
            "penalty": ("Mandatory Arnesh Kumar compliance", "Contempt of Court on defaulting police"),
            "cognizance": ("Applicable to offences up to 7 years", "Mandatory statutory safeguard"),
            "bail": ("Protection against Custodial Arrest", "Appearance before Police"),
            "court": ("Judicial Magistrate", "Magistrate First Class"),
        },
        "advocate_strategy": (
            "• **Arnesh Kumar Compliance**: If police arrest an accused in a 498A or Section 420 case without serving Section 41A notice, file contempt petition against police in High Court.\n"
            "• **Written Defense Submission**: Accompany the client to the police station and submit a formal written statement in response to the Section 41A notice.\n"
            "• **Anticipatory Bail Protection**: If police threaten arrest despite compliance, file Section 482 BNSS (438 CrPC) anticipatory bail."
        ),
        "client_strategy": (
            "• **Do Not Fear the Notice**: A Section 41A notice means police CANNOT arrest you so long as you appear and cooperate with the inquiry.\n"
            "• **Always Attend with an Advocate**: Take your lawyer with you; submit a written acknowledgment of appearance.\n"
            "• **Take Stamped Acknowledgment**: Get the Investigating Officer's signature and stamp on a duplicate copy of your appearance reply."
        ),
        "citations": [
            "[Statute] Code of Criminal Procedure, 1973 - Section 41A",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 35(3)",
            "[Landmark SC] Arnesh Kumar v. State of Bihar (2014) 8 SCC 273 (Mandatory Arrest Guidelines)",
            "[Landmark SC] Satender Kumar Antil v. CBI (2022) 10 SCC 51 (Category A Offences)",
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
    "154": {
        "title": "Section 154 CrPC: Information in Cognizable Cases (First Information Report - FIR)",
        "act": "Code of Criminal Procedure, 1973",
        "bns_equiv": "Section 173 BNSS, 2023 (Codification of Zero FIR & e-FIR)",
        "primary_purpose": (
            "**Section 154 of the Code of Criminal Procedure (CrPC) is primarily for THE REGISTRATION OF A FIRST INFORMATION REPORT (FIR).**\n"
            "It obligates the police officer in charge of a police station to reduce every information relating to the commission of a cognizable offence into writing, "
            "read it over to the informant, enter it into the prescribed station register, and give a free copy to the complainant. "
            "Under the **Bharatiya Nagarik Suraksha Sanhita (BNSS 2023)**, it is codified under **Section 173 BNSS**."
        ),
        "definition": (
            "**Mandatory Nature (*Lalita Kumari v. Govt. of U.P.*)**:\n"
            "> The registration of an FIR is **MANDATORY** under Section 154 if the information discloses the commission of a cognizable offence. "
            "> Police have no discretion to refuse registration or conduct preliminary inquiry except in limited exceptions (medical negligence, matrimonial disputes, corruption).\n\n"
            "**Remedy on Refusal (Section 154(3) CrPC / Section 173(4) BNSS)**: If the station officer refuses to register the FIR, the complainant can send the substance in writing to the **Superintendent of Police (SP / DCP)** by registered post."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 154(1) CrPC", "Section 173(1) BNSS"),
            "punishment_sec": ("Section 166A IPC on police for refusal", "Section 199 BNS (1 to 2 years imprisonment)"),
            "penalty": ("Mandatory Free Copy to Informant", "Section 173(2) BNSS"),
            "cognizance": ("Cognizable Offences", "Zero FIR permissible"),
            "bail": ("Trigger for Criminal Machinery", "Investigation Starts"),
            "court": ("Jurisdictional Police Station / SP", "Magistrate receiving copy under Sec 157"),
        },
        "advocate_strategy": (
            "• **SP Representation**: Immediately draft Section 154(3) CrPC representation to the SP with registered post receipt before moving Magistrate.\n"
            "• **Section 156(3) Application**: File Section 156(3) CrPC application accompanied by affidavit of compliance under *Priyanka Srivastava*.\n"
            "• **Section 166A IPC Action**: Pray for initiation of disciplinary action against the defaulting police officer under Section 166A IPC."
        ),
        "client_strategy": (
            "• **Demand Stamped Copy**: By law, police MUST give you a free copy of the FIR immediately upon registration.\n"
            "• **Zero FIR Rights**: If police say 'out of jurisdiction', insist on a Zero FIR; they must record it and transfer it.\n"
            "• **Send to SP via Speed Post**: If local police refuse, post the complaint to the SP/DCP by speed post and save tracking."
        ),
        "citations": [
            "[Landmark SC] Lalita Kumari v. Govt. of U.P. (2014) 2 SCC 1 (Mandatory FIR Registration)",
            "[Statute] Code of Criminal Procedure, 1973 - Section 154",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 173 (Zero FIR)",
            "[Statute] Indian Penal Code, 1860 - Section 166A",
        ],
    },
    "156": {
        "title": "Section 156(3) CrPC: Magistrate's Power to Direct Investigation & FIR Registration",
        "act": "Code of Criminal Procedure, 1973",
        "bns_equiv": "Section 175(3) BNSS, 2023",
        "primary_purpose": (
            "**Section 156(3) of the Code of Criminal Procedure (CrPC) is primarily for JUDICIAL ORDERS COMPELLING THE POLICE TO REGISTER AN FIR AND CONDUCT AN INVESTIGATION.**\n"
            "When police refuse or fail to register an FIR under Section 154, any aggrieved person can approach the Judicial Magistrate / Metropolitan Magistrate, "
            "who has statutory power under Section 156(3) to order the police to register an FIR and submit an investigation report. "
            "Under the **Bharatiya Nagarik Suraksha Sanhita (BNSS 2023)**, it is codified under **Section 175(3) BNSS**."
        ),
        "definition": (
            "**Statutory Text (Section 156(3) CrPC)**:\n"
            "> *\"Any Magistrate empowered under section 190 may order such an investigation as above-mentioned.\"*\n\n"
            "**Procedural Prerequisites (*Priyanka Srivastava v. State of U.P.*)**:\n"
            "1. The applicant must have first approached the Police Station under Section 154(1).\n"
            "2. The applicant must have approached the Superintendent of Police under Section 154(3).\n"
            "3. The application under Section 156(3) **MUST be supported by a sworn affidavit** attesting to the truth of facts."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 156(3) CrPC", "Section 175(3) BNSS"),
            "punishment_sec": ("Judicial Order Binding on Police", "Mandatory FIR & Status Report"),
            "penalty": ("Contempt on Police for Non-Compliance", "Magistrate Monitors Investigation"),
            "cognizance": ("Pre-Cognizance Stage", "Investigation Directed"),
            "bail": ("Remedy Against Police Inaction", "Judicial Safeguard"),
            "court": ("Judicial Magistrate First Class / MM", "Territorial Jurisdiction"),
        },
        "advocate_strategy": (
            "• **Annex Proof of 154(1) and 154(3)**: Attach copy of police complaint with acknowledgment seal and SP speed post receipt with delivery report.\n"
            "• **Affidavit of Compliance**: Ensure affidavit adheres strictly to the *Priyanka Srivastava* format to avoid rejection on technicality.\n"
            "• **Judicial Monitoring (*Sakiri Vasu*)**: Remind Magistrate that power under Section 156(3) includes the power to monitor investigation and order proper investigation."
        ),
        "client_strategy": (
            "• **Court Route Against Lazy Police**: If police refuse to act, you do not need their mercy; your advocate can obtain a binding order from the Judge.\n"
            "• **Keep All Postal Proof Safe**: Retain the India Post receipt and delivery printout proving you informed the SP.\n"
            "• **Court Timeline**: A Section 156(3) application typically results in an Action Taken Report (ATR) from police within 2 to 4 weeks."
        ),
        "citations": [
            "[Landmark SC] Sakiri Vasu v. State of U.P. (2008) 2 SCC 409 (Scope of Section 156(3))",
            "[Landmark SC] Priyanka Srivastava v. State of U.P. (2015) 6 SCC 287 (Mandatory Affidavit)",
            "[Statute] Code of Criminal Procedure, 1973 - Section 156(3)",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 175(3)",
        ],
    },
    "437": {
        "title": "Section 437 CrPC: Bail in Non-Bailable Offences Before Magistrate",
        "act": "Code of Criminal Procedure, 1973",
        "bns_equiv": "Section 480 BNSS, 2023",
        "primary_purpose": (
            "**Section 437 of the Code of Criminal Procedure (CrPC) is primarily for BAIL IN NON-BAILABLE OFFENCES BEFORE A MAGISTRATE.**\n"
            "It lays down when a person accused of or suspected of the commission of a non-bailable offence may be released on bail by the Magistrate's Court, "
            "subject to statutory restrictions (e.g. no bail if reasonable grounds exist to believe person is guilty of offence punishable with death or life imprisonment, "
            "with special dispensations for women, minors, and sick persons). Under **BNSS 2023**, it is codified under **Section 480 BNSS**."
        ),
        "definition": (
            "**Statutory Discretion & Statutory Bar**:\n"
            "1. **General Rule**: Magistrate has discretion to grant bail in non-bailable offences.\n"
            "2. **Statutory Bar**: Bail shall not be granted if reasonable grounds appear for believing accused has committed offence punishable with death or imprisonment for life.\n"
            "3. **Proviso Exception**: Court may direct release on bail if accused is **under the age of 16 years, or is a woman, or is sick or infirm**."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 437 CrPC", "Section 480 BNSS"),
            "punishment_sec": ("Discretionary Bail by Magistrate", "Bail Conditions Applicable"),
            "penalty": ("Bail Bond & Surety", "Section 480 BNSS"),
            "cognizance": ("Non-Bailable Offences", "Magistrate Court"),
            "bail": ("Regular Bail Application", "Custodial / First Production"),
            "court": ("Court of Judicial Magistrate / MM", "Subordinate Judiciary"),
        },
        "advocate_strategy": (
            "• **Proviso for Women & Minors**: Invoke the first proviso to Section 437(1) for women, elderly, or sick accused where statutory bar does not apply.\n"
            "• **Category A Offences (*Satender Kumar Antil*)**: Argue that for offences punishable up to 7 years, bail should be granted upon appearance without taking into custody.\n"
            "• **Surety Readiness**: Keep solvent local sureties and identity papers ready at the first remand appearance."
        ),
        "client_strategy": (
            "• **Apply at First Production**: Move bail application on the very first day you are produced before the Magistrate.\n"
            "• **Keep Sureties Ready**: Arrange two respectable family members/friends with Aadhaar and property/tax documents to stand surety.\n"
            "• **Appeal to Sessions if Rejected**: If Magistrate rejects bail under Section 437, apply immediately to Sessions Court under Section 439 CrPC."
        ),
        "citations": [
            "[Statute] Code of Criminal Procedure, 1973 - Section 437",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 480",
            "[Landmark SC] Satender Kumar Antil v. CBI (2022) 10 SCC 51",
        ],
    },
    "438": {
        "title": "Section 438 CrPC: Direction for Grant of Bail to Person Apprehending Arrest (Anticipatory Bail)",
        "act": "Code of Criminal Procedure, 1973",
        "bns_equiv": "Section 482 BNSS, 2023",
        "primary_purpose": (
            "**Section 438 of the Code of Criminal Procedure (CrPC) is primarily for ANTICIPATORY BAIL (PRE-ARREST BAIL).**\n"
            "It empowers the **High Court or Court of Session** to direct that in the event of arrest on an accusation of a non-bailable offence, "
            "the applicant shall be released on bail immediately without spending a single moment in police custody. "
            "Under the **Bharatiya Nagarik Suraksha Sanhita (BNSS 2023)**, it is codified under **Section 482 BNSS**."
        ),
        "definition": (
            "**Statutory Text (Section 438 CrPC / Section 482 BNSS)**:\n"
            "> *\"Where any person has reason to believe that he may be arrested on an accusation of having committed a non-bailable offence, he may apply to the High Court or the Court of Session for a direction under this section; that in the event of such arrest he shall be released on bail; and that Court may, after taking into consideration, inter alia, the following factors... grant anticipatory bail.\"*\n\n"
            "**Factors Considered by Court**:\n"
            "1. The nature and gravity of the accusation.\n"
            "2. Antecedents of the applicant (previous criminal record).\n"
            "3. Possibility of applicant fleeing from justice.\n"
            "4. Whether accusation has been made with the object of injuring or humiliating the applicant."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 438 CrPC", "Section 482 BNSS"),
            "punishment_sec": ("Pre-Arrest Bail Protection", "Sessions Court & High Court"),
            "penalty": ("Immunity from Lockup Arrest", "Interim Protection Granted"),
            "cognizance": ("Apprehension of Non-Bailable Offence", "Concurrent Jurisdiction"),
            "bail": ("Anticipatory Bail", "Life of Anticipatory Bail does not end on charge-sheet (*Sushila Aggarwal*)"),
            "court": ("Court of Session or High Court", "Direct Jurisdiction"),
        },
        "advocate_strategy": (
            "• **Sushila Aggarwal 5-Judge Bench**: Reassure court that under *Sushila Aggarwal*, anticipatory bail is not limited to a fixed timeline and can continue until trial completion.\n"
            "• **Demonstrate Malice or Commercial Dispute**: Prove dispute is civil, commercial, or matrimonial with omnibus allegations.\n"
            "• **Interim Protection on Day One**: Move application praying for ad-interim protection against coercive steps while notice is issued to Public Prosecutor."
        ),
        "client_strategy": (
            "• **Apply BEFORE Police Arrest You**: Anticipatory bail can ONLY be applied for BEFORE you are arrested; once handcuffed or detained, Section 438 is unavailable.\n"
            "• **Join the Investigation**: When granted anticipatory bail, cooperate with the Investigating Officer whenever summoned.\n"
            "• **Surrender Passport**: Be prepared to surrender your passport and furnish local sureties as standard bail conditions."
        ),
        "citations": [
            "[Landmark SC] Sushila Aggarwal v. State (NCT of Delhi) (2020) 5 SCC 1 (5-Judge Constitution Bench on Anticipatory Bail)",
            "[Landmark SC] Gurbaksh Singh Sibbia v. State of Punjab (1980) 2 SCC 565 (Magna Carta on Anticipatory Bail)",
            "[Statute] Code of Criminal Procedure, 1973 - Section 438",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 482",
        ],
    },
    "439": {
        "title": "Section 439 CrPC: Special Powers of High Court or Court of Session Regarding Bail",
        "act": "Code of Criminal Procedure, 1973",
        "bns_equiv": "Section 483 BNSS, 2023",
        "primary_purpose": (
            "**Section 439 of the Code of Criminal Procedure (CrPC) is primarily for REGULAR BAIL BEFORE THE SESSIONS COURT OR HIGH COURT.**\n"
            "It confers plenary, overriding powers on the High Court or Court of Session to direct that any person accused of an offence and in custody be released on bail, "
            "or to set aside, modify, or cancel bail previously granted. Under **BNSS 2023**, it is codified under **Section 483 BNSS**."
        ),
        "definition": (
            "**Supreme Principle (*State of Rajasthan v. Balchand*)**: **'BAIL IS THE RULE, JAIL IS THE EXCEPTION.'**\n\n"
            "**Core Considerations for Regular Bail**:\n"
            "1. Nature and seriousness of the offence.\n"
            "2. Prima facie evidence and reasonable grounds for believing the accused committed the crime.\n"
            "3. Danger of accused absconding or tampering with witnesses/evidence.\n"
            "4. Period of custody undergone and whether investigation / charge-sheet is complete."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 439 CrPC", "Section 483 BNSS"),
            "punishment_sec": ("Plenary Bail Power", "Court of Session & High Court"),
            "penalty": ("Personal Bond & Surety", "Conditions imposed"),
            "cognizance": ("Accused in Judicial Custody", "Post-Arrest Bail"),
            "bail": ("Regular Bail", "Cancellation of Bail Power (Sec 439(2))"),
            "court": ("Court of Session or High Court", "Superior Criminal Courts"),
        },
        "advocate_strategy": (
            "• **Charge-Sheet Filed**: Emphasize that charge-sheet is filed, investigation complete, and custodial interrogation is no longer required.\n"
            "• **Satender Kumar Antil 4-Tier Categorization**: Categorize offence into Category A, B, C, or D to apply binding bail timelines.\n"
            "• **Long Incarceration & Delayed Trial**: Invoke Article 21 and *Union of India v. K.A. Najeeb* where trial delay violates speedy trial rights."
        ),
        "client_strategy": (
            "• **Custody Requirement**: Section 439 is filed AFTER you are in judicial custody (jail) or surrender to court.\n"
            "• **No Tampering with Witnesses**: Never contact the complainant or witnesses while out on bail; doing so results in immediate cancellation under Section 439(2).\n"
            "• **Attend Court on Every Date**: Regular attendance prevents forfeiture of bond and issuance of non-bailable warrants."
        ),
        "citations": [
            "[Landmark SC] State of Rajasthan v. Balchand (1977) 4 SCC 308 (Bail is Rule, Jail is Exception)",
            "[Landmark SC] Satender Kumar Antil v. CBI (2022) 10 SCC 51 (Bail Guidelines)",
            "[Statute] Code of Criminal Procedure, 1973 - Section 439",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 483",
        ],
    },
    "482": {
        "title": "Section 482 CrPC: Inherent Powers of the High Court (FIR Quashing & Abuse of Process)",
        "act": "Code of Criminal Procedure, 1973",
        "bns_equiv": "Section 528 BNSS, 2023",
        "primary_purpose": (
            "**Section 482 of the Code of Criminal Procedure (CrPC) is primarily for THE INHERENT POWERS OF THE HIGH COURT TO QUASH FIRs, CHARGE-SHEETS, AND PREVENT ABUSE OF COURT PROCESS.**\n"
            "It preserves the High Court's extraordinary inherent jurisdiction to make such orders as may be necessary to give effect to any order under the Code, "
            "or to prevent abuse of the process of any court, or otherwise to secure the ends of justice. "
            "Under the **Bharatiya Nagarik Suraksha Sanhita (BNSS 2023)**, it is codified under **Section 528 BNSS**."
        ),
        "definition": (
            "**Statutory Text (Section 482 CrPC / Section 528 BNSS)**:\n"
            "> *\"Nothing in this Code shall be deemed to limit or affect the inherent powers of the High Court to make such orders as may be necessary to give effect to any order under this Code, or to prevent abuse of the process of any court or otherwise to secure the ends of justice.\"*\n\n"
            "**7 Cardinal Principles of Quashing (*State of Haryana v. Bhajan Lal*)**:\n"
            "1. Allegations in FIR, even if taken at face value, do not disclose any cognizable offence.\n"
            "2. Allegations are so absurd and inherently improbable that no prudent person could reach a conclusion of guilt.\n"
            "3. Criminal proceeding is manifestly attended with mala fides or instituted with an ulterior motive for wreaking vengeance."
        ),
        "exceptions": [],
        "punishment_table": {
            "definition_sec": ("Section 482 CrPC", "Section 528 BNSS"),
            "punishment_sec": ("Inherent Powers of High Court", "Quashing of FIR / Charge-Sheet"),
            "penalty": ("Complete Annulment of Prosecution", "Ends of Justice"),
            "cognizance": ("High Court Jurisdiction Strictly", "Overriding Inherent Power"),
            "bail": ("Stay on Coercive Steps / Arrest", "Interim Relief Granted"),
            "court": ("High Courts across India", "Single Judge / Division Bench"),
        },
        "advocate_strategy": (
            "• **Bhajan Lal Categories**: Frame petition grounds strictly within the 7 categories formulated in *State of Haryana v. Bhajan Lal*.\n"
            "• **Purely Civil / Commercial Dispute**: Show through contracts and correspondence that transaction is civil in nature without criminal inception (*Hridaya Ranjan*).\n"
            "• **Quashing on Compromise**: If parties have amicably settled matrimonial or commercial dispute, petition for quashing under *Gian Singh v. State of Punjab*."
        ),
        "client_strategy": (
            "• **Quash False FIRs Permanently**: A successful Section 482 petition permanently wipes out the criminal case, police records, and trial stigma.\n"
            "• **Apply for Stay on Arrest**: High Court can grant interim protection staying your arrest and staying trial court proceedings.\n"
            "• **Assemble Pure Documentary Defense**: High Court does not appreciate disputed oral facts; rely on admitted emails, contracts, and bank records."
        ),
        "citations": [
            "[Landmark SC] State of Haryana v. Bhajan Lal (1992) Supp (1) SCC 335 (7 Quashing Guidelines)",
            "[Landmark SC] Gian Singh v. State of Punjab (2012) 10 SCC 303 (Quashing on Compromise)",
            "[Statute] Code of Criminal Procedure, 1973 - Section 482",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 528",
        ],
    },
}


# Map companion punishment/definition sections to identical definitions
STATUTORY_REGISTRY["406"] = STATUTORY_REGISTRY["405"]
STATUTORY_REGISTRY["506"] = STATUTORY_REGISTRY["503"]
STATUTORY_REGISTRY["379"] = STATUTORY_REGISTRY["378"]
STATUTORY_REGISTRY["392"] = STATUTORY_REGISTRY["390"]
STATUTORY_REGISTRY["395"] = STATUTORY_REGISTRY["391"]
STATUTORY_REGISTRY["465"] = STATUTORY_REGISTRY["463"]
STATUTORY_REGISTRY["500"] = STATUTORY_REGISTRY["499"]
STATUTORY_REGISTRY["41"] = STATUTORY_REGISTRY["41a"]


COMPANION_ALIASES = {
    "406": "405",
    "506": "503",
    "379": "378",
    "392": "390",
    "395": "391",
    "465": "463",
    "500": "499",
    "41": "41a",
}


def _determine_statute_type(key: str, clean_query: str) -> str:
    cfg = STATUTORY_REGISTRY.get(key)
    if not cfg:
        return "ipc"
    act_str = cfg.get("act", "").lower()
    if "constitution" in act_str:
        return "constitution"
    if "criminal procedure" in act_str or any(c in clean_query for c in ["crpc", "bnss", "bail", "fir", "arrest", "inquest"]):
        return "crpc"
    if "negotiable" in act_str or "ni act" in clean_query or "cheque" in clean_query:
        return "special_act"
    return "ipc"


def match_statutory_section(query: str) -> Optional[Tuple[str, str]]:
    """
    Evaluates whether query asks about a specific statutory section (IPC, CrPC, NI Act, Constitution).
    Returns (section_key, statute_type) or None.
    """
    clean = re.sub(r"[^\w\s]", " ", query).strip().lower()
    clean = re.sub(r"\s+", " ", clean)

    # 1. Constitution Articles: e.g. "article 21", "art 21", "article 14", "art 32", "article 226", "article 19"
    m_art = re.search(r"\b(?:article|art)\.?\s*(\d+[a-zA-Z]?)\b", clean)
    if m_art:
        key = m_art.group(1).lower()
        if key in STATUTORY_REGISTRY:
            return key, "constitution"

    # 2. Section queries with statute indicators:
    # "ipc 300", "section 300", "sec 300", "300 ipc", "what is ipc 300", "crpc 154", "sec 156 3", "section 41a crpc"
    m_sec_complex = re.search(r"\b(?:section|sec|crpc|bnss|ipc|act)\.?\s*(156\s*\(?3\)?|167\s*\(?2\)?|41\s*a|304\s*a|304\s*b|498\s*a)\b|\b(156\s*\(?3\)?|167\s*\(?2\)?|41\s*a|304\s*a|304\s*b|498\s*a)\s*(?:crpc|bnss|ipc)\b", clean)
    if m_sec_complex:
        raw_key = m_sec_complex.group(1) or m_sec_complex.group(2)
        clean_key = re.sub(r"[\s\(\)]", "", raw_key).lower()
        clean_key = COMPANION_ALIASES.get(clean_key, clean_key)
        if clean_key in STATUTORY_REGISTRY:
            return clean_key, _determine_statute_type(clean_key, clean)

    m_ipc = re.search(
        r"\b(?:ipc|indian penal code|crpc|bnss|bns|section|sec|act)\.?\s*(\d+[a-zA-Z]?)\b|\b(\d+[a-zA-Z]?)\s*(?:ipc|indian penal code|crpc|bnss|bns|section|sec|act)\b",
        clean,
    )
    if m_ipc:
        key = (m_ipc.group(1) or m_ipc.group(2)).lower()
        key = COMPANION_ALIASES.get(key, key)
        if key in STATUTORY_REGISTRY:
            return key, _determine_statute_type(key, clean)

    # 3. Plain section numbers if query is very short: e.g. "300", "420", "302", "154", "482"
    tokens = clean.split()
    if len(tokens) <= 3:
        for t in tokens:
            canon_t = COMPANION_ALIASES.get(t, t)
            if canon_t in STATUTORY_REGISTRY:
                return canon_t, _determine_statute_type(canon_t, clean)

    # 4. Direct conceptual queries: "what is murder", "definition of theft", "anticipatory bail", etc.
    concept_map = {
        "punishment for murder": ("302", "ipc"),
        "murder": ("300", "ipc"),
        "causing death by negligence": ("304a", "ipc"),
        "dowry death": ("304b", "ipc"),
        "attempt to murder": ("307", "ipc"),
        "theft": ("378", "ipc"),
        "extortion": ("383", "ipc"),
        "robbery": ("390", "ipc"),
        "dacoity": ("391", "ipc"),
        "criminal breach of trust": ("405", "ipc"),
        "cheating": ("420", "ipc"),
        "criminal trespass": ("441", "ipc"),
        "forgery": ("463", "ipc"),
        "cruelty by husband": ("498a", "ipc"),
        "domestic cruelty": ("498a", "ipc"),
        "defamation": ("499", "ipc"),
        "criminal intimidation": ("503", "ipc"),
        "cheque bounce": ("138", "ni_act"),
        "dishonour of cheque": ("138", "ni_act"),
        "anticipatory bail": ("438", "crpc"),
        "pre arrest bail": ("438", "crpc"),
        "quashing": ("482", "crpc"),
        "fir": ("154", "crpc"),
        "first information report": ("154", "crpc"),
        "magistrate investigation": ("156", "crpc"),
        "equality before law": ("14", "constitution"),
        "right to life": ("21", "constitution"),
        "right to privacy": ("21", "constitution"),
        "habeas corpus": ("32", "constitution"),
    }
    for concept, (sec, stype) in concept_map.items():
        if re.search(r"\b(?:what\s+is|define|definition\s+of|explain|tell\s+me\s+about)?\s*" + re.escape(concept) + r"\b", clean):
            if not re.search(r"\b(can\s+i|how\s+to|should\s+i|want\s+to|kill|shoot|stab|rob|steal)\b", clean):
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

    # 3. Inquiries regarding whether killing / murder is legal
    legal_killing_pattern = r"\b(is\s+killing\s+legal|is\s+murder\s+legal|is\s+killing\s+allowed|legality\s+of\s+killing|right\s+to\s+kill)\b"
    if re.search(legal_killing_pattern, clean):
        return {
            "type": "violent_harm",
            "action": "kill",
            "target": "another person",
            "query": query,
        }

    # 4. Robbery, Dacoity, Bank Robbery, Theft, Looting & Heists
    robbery_pattern = (
        r"\b(can\s+i|can\s+we|may\s+i|is\s+it\s+legal(?:\s+to)?|is\s+it\s+allowed(?:\s+to)?|"
        r"how\s+to|how\s+can\s+i|how\s+do\s+i|should\s+i|i\s+want\s+to|i\s+need\s+to|"
        r"allowed\s+to|permission\s+to|ways\s+to|can\s+one|could\s+i|where\s+can\s+i)\s+"
        r"(?:commit\s+)?(rob|robbery|dacoit|dacoity|steal|theft|loot|looting|extort|extortion|burgle|burglary|heist)\b|"
        r"\b(rob|robbery|dacoity|steal|loot|extort)\s+(?:a\s+|the\s+)?(bank|atm|cash|money|store|shop|house|person|jewelry|jewellery|gold|vault)\b|"
        r"\b(is\s+robbing\s+legal|is\s+stealing\s+legal|is\s+dacoity\s+legal|is\s+looting\s+legal)\b|"
        r"\brob\s+bank\b|\bcan\s+i\s+rob\b"
    )
    if re.search(robbery_pattern, clean):
        target_m = re.search(r"\b(bank|atm|vault|store|shop|house|person|cash|money|gold|jewelry|jewellery)\b", clean)
        target = target_m.group(1) if target_m else "a bank or financial institution"
        return {
            "type": "robbery_dacoity",
            "action": "rob",
            "target": target,
            "query": query,
        }

    return None


def synthesize_violent_harm_response(
    match_info: Dict[str, Any], query: str, role: str
) -> Tuple[str, List[str]]:
    """
    Synthesizes an immediate, unequivocal, authoritative legal declaration establishing
    that killing, causing physical harm, or committing robbery/dacoity is strictly prohibited
    and punished under Indian Law.
    """
    match_type = match_info.get("type")

    # A. ROBBERY & DACOITY SAFETY INTERCEPTOR
    if match_type == "robbery_dacoity":
        target = match_info.get("target", "a bank or financial institution")
        text = (
            f"### 🚨 ABSOLUTELY NOT: Robbery and Dacoity Are Severe Criminal Felonies Under Indian Law\n\n"
            f"> ⚠️ **IMMEDIATE LEGAL DECLARATION**:\n"
            f"> **NO, you CANNOT rob {target} or any entity under any circumstances.**\n"
            f"> Under Indian Criminal Law, robbery, dacoity, theft, and extortion are grave non-bailable offences "
            f"punishable with **RIGOROUS IMPRISONMENT FOR LIFE** or up to **10–14 YEARS**, along with heavy fines.\n\n"
            f"---\n\n"
            f"### ⚖️ Governing Penal Framework (IPC 1860 vs BNS 2023 Concordance)\n\n"
            f"| Legal Metric | Indian Penal Code (IPC 1860) | Bharatiya Nyaya Sanhita (BNS 2023) |\n"
            f"|---|---|---|\n"
            f"| **Substantive Offence (Robbery)** | **Section 390 IPC** (Definition) & **Section 392 IPC** (Punishment) | **Section 309 BNS** |\n"
            f"| **Prescribed Penalty (Robbery)** | **Rigorous Imprisonment up to 10 Years & Fine** (Up to **14 Years** on Highway at night) | **Rigorous Imprisonment up to 10–14 Years & Fine** |\n"
            f"| **Dacoity (5 or More Persons)** | **Section 391 IPC** (Definition) & **Section 395 IPC** (Punishment) | **Section 310 BNS** |\n"
            f"| **Prescribed Penalty (Dacoity)** | **IMPRISONMENT FOR LIFE**, or Rigorous Imprisonment up to **10 Years & Fine** | **IMPRISONMENT FOR LIFE**, or Rigorous Imprisonment up to 10 Years & Fine |\n"
            f"| **Robbery with Deadly Weapon** | **Section 397 IPC** (Mandatory Minimum **7 Years** Imprisonment) | **Section 311 BNS** |\n"
            f"| **Attempt / Preparation** | **Section 393, 398 & 399 IPC** (Making preparation to commit dacoity: Up to 10 Years) | **Section 310(4) & 312 BNS** |\n"
            f"| **Cognizability** | **Cognizable** (Police MUST arrest immediately without warrant) | **Cognizable** |\n"
            f"| **Bail Classification** | **Non-Bailable** (Bail is exception, strictly at Sessions discretion) | **Non-Bailable** |\n"
            f"| **Jurisdictional Court** | **Court of Session / Magistrate First Class** | **Court of Session** |\n\n"
            f"---\n\n"
            f"### 🏛️ Severe Statutory Aggravations\n"
            f"1. **Armed Robbery & Arms Act Violations**: Using or carrying any unlicensed firearm, pistol, or deadly weapon invokes **Sections 25 and 27 of the Arms Act, 1959**, adding consecutive prison terms up to 7 years to life.\n"
            f"2. **Dacoity with Murder (Section 396 IPC / Section 310(3) BNS)**: If any one of five or more persons conjointly committing dacoity commits murder in so committing dacoity, **EVERY ONE OF THOSE PERSONS** is punishable with **DEATH or IMPRISONMENT FOR LIFE**.\n"
            f"3. **Bank Security & Counter-Terrorism Protocols**: Banks and financial vaults operate under Central Reserve Police / Armed Guard protection; armed attempts trigger immediate lawful lethal force in private defence of property under Section 103 IPC / Section 41 BNS.\n\n"
            f"---\n\n"
            f"### 🆘 Lawful Financial Relief & Emergency Support\n"
            f"If you are facing acute financial distress or unmanageable debt, Indian law provides lawful avenues for relief:\n"
            f"• **Insolvency & Debt Resolution**: Apply under the **Insolvency and Bankruptcy Code (IBC, 2016)** for statutory debt restructuring and protection against coercive recovery.\n"
            f"• **Banking Ombudsman & RBI Restructuring**: Lodge formal dispute with the RBI Banking Ombudsman (cms.rbi.org.in) against predatory recovery agents or usurious interest.\n"
            f"• **Free Legal Aid (NALSA)**: Approach the National Legal Services Authority (nalsa.gov.in) or dial **15100** for free advocate representation.\n"
            f"• 🚨 **National Police Emergency**: **112** (or **100**)"
        )
        citations = [
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 390: Robbery, Section 392: Punishment up to 14 Years)",
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 391: Dacoity, Section 395: Life Imprisonment)",
            "[Statute] Bharatiya Nyaya Sanhita (BNS), 2023 - Section 309 (Robbery) & Section 310 (Dacoity & Sanctions)",
            "[Statute] Arms Act, 1959 - Section 25 & 27 (Severe Penalties for Unlicensed Weapons)",
            "[Procedural Law] Code of Criminal Procedure, 1973 - First Schedule (Cognizable, Non-Bailable, Sessions Court)",
        ]
        return text, citations

    # B. VIOLENT HARM & HOMICIDE HANDLER
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
            f"\n\n### 🛡️ Statutory Exceptions & Defenses\n"
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
        f"| Legal Metric | Pre-2024 Provision / Substantive Law | Modern Concordance (BNS 2023 / BNSS 2023) |\n"
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
        f"### 📜 Statutory Definition & Essential Legal Ingredients\n"
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
