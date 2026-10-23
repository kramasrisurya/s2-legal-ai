"""
S2 Legal AI Pro - Real-World Story & Fact-Pattern Legal Reasoning Engine
Module: backend.scenario_engine

Analyzes real-world legal scenarios, family disputes, property conflicts, financial fraud,
consumer disputes, wrongful termination, medical negligence, cyber crimes, and police inaction to determine:
1. Legal standing: WHO IS RIGHT & WHO IS WRONG under Indian Law.
2. Governing statutory sections: WHICH SECTIONS SUPPORT THEM (IPC, BNS, CrPC, BNSS, Special Acts).
3. Essential legal ingredients & evidentiary proof required.
4. Actionable strategic roadmap (Advocate vs Client perspective).
5. Landmark Supreme Court of India precedents.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple


SCENARIO_CONFIGS: List[Dict[str, Any]] = [
    # 1. Family Dispute: Cruelty, Domestic Violence & Dowry Harassment
    {
        "domain": "family_cruelty_dowry",
        "title": "Matrimonial Harassment, Domestic Violence & Dowry Demands",
        "triggers": [
            r"\b(husband|in-laws|mother-in-law|father-in-law|sister-in-law|brother-in-law)\b",
            r"\b(beat|beating|beaten|torture|torturing|harass|harassing|harassment|abuse|abusing|assault)\b",
            r"\b(dowry|gold|stridhan|car|cash|demanding money|ask money|money demand|property demand)\b",
            r"\b(throw.*out|thrown out|expel|kicked out|matrimonial home|shared household|leave house)\b",
        ],
        "negative_triggers": [
            r"\b(?:died|death|burnt|burn\s+injuries|strangled|poisoned|hanging|suicide|unnatural\s+death)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Wife / Complainant is legally in the right.**\n"
            "Under Indian Law, demanding dowry, subjecting a married woman to physical or mental cruelty, "
            "and dispossessing her from the shared matrimonial home are cognizable criminal offences and actionable domestic abuse. "
            "The husband and his relatives have no legal right to harass the wife, demand gifts/money, or forcibly evict her from the matrimonial home."
        ),
        "supporting_sections": [
            "**Section 498A IPC / Section 85 & 86 BNS**: Cruelty by husband or his relatives. Punishable with up to 3 years rigorous imprisonment and fine (Cognizable & Non-Bailable).",
            "**Dowry Prohibition Act, 1961 (Sections 3 & 4)**: Strictly prohibits demanding or giving dowry. Penalty of imprisonment not less than 5 years and fine of ₹15,000 or dowry value.",
            "**Section 12 PWDVA 2005 (Domestic Violence Act)**: Comprehensive petition before Judicial Magistrate for urgent protection, residence, and monetary orders.",
            "**Section 17 PWDVA 2005**: Absolute statutory right to reside in the shared household. The husband cannot throw the wife out without due process of law.",
            "**Section 18 & 19 PWDVA 2005**: Protection Orders restraining husband/in-laws from contacting, entering her residence/workplace, or alienating the shared home.",
            "**Section 125 CrPC / Section 144 BNSS**: Mandatory monthly maintenance for wife and minor children unable to maintain themselves.",
        ],
        "evidence_required": [
            "Photographs of marriage and marriage certificate / invitation card.",
            "WhatsApp chats, text messages, email records, or call recordings proving harassment, abusive language, or monetary demands.",
            "Bank account statements and UPI records showing any cash or electronic transfers made to husband or in-laws.",
            "Medico-Legal Certificate (MLC), hospital emergency slips, or prescriptions if physical assault occurred.",
            "Detailed inventory list of Stridhan (jewellery, gold, electronic appliances, and gifts) received at or after marriage.",
        ],
        "action_plan_advocate": (
            "1. **Emergency Protection (Section 12 PWDVA)**: Immediately file an application before the Metropolitan Magistrate / Judicial Magistrate First Class seeking ex-parte interim protection under Section 18 and residence order under Section 19.\n"
            "2. **Police / CAW Cell Complaint (Section 498A IPC / Section 85 BNS)**: Lodge a written formal complaint with the Crime Against Women (CAW) Cell or local Police Station. Inquire about Section 35(3) BNSS compliance.\n"
            "3. **Interim Maintenance Application (Section 125 CrPC / Section 144 BNSS)**: File maintenance petition along with income/asset affidavit under Supreme Court guidelines in *Rajnesh v. Neha*."
        ),
        "action_plan_client": (
            "1. **Safety First**: Move to a safe location with trusted family or shelter, and do not sign any blank papers or mutual consent agreements under duress.\n"
            "2. **Secure Evidence**: Keep safe copies of all marriage photographs, medical slips, hospital discharge summaries, and WhatsApp messages.\n"
            "3. **Stridhan Protection**: List down all gold ornaments and gifts given to you during marriage; they belong exclusively to you as Stridhan.\n"
            "4. **Call Helplines**: You can reach the National Women Helpline at **1091** or Women in Distress Helpline at **181** for immediate police escort."
        ),
        "landmarks": [
            "***Rajnesh v. Neha* (2020) Supreme Court**: Mandated uniform maintenance calculation and mandatory disclosure of assets and liabilities by husband.",
            "***Arnesh Kumar v. State of Bihar* (2014) Supreme Court**: Safeguards under Section 35(3) BNSS (Section 41A CrPC) against arbitrary mechanical arrest.",
            "***Prabha Tyagi v. Kamlesh Devi* (2022) Supreme Court**: Confirmed that a woman has the right to shared household under Section 17 PWDVA even if living separately at time of petition.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/family_and_matrimonial_disputes_scenarios.pdf (Matrimonial Harassment & Cruelty Scenario)",
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Section 498A: Cruelty by Husband or Relatives)",
            "[Statute] Protection of Women from Domestic Violence Act, 2005 (Sections 12, 17, 18, 19)",
            "[Landmark Precedent] Rajnesh v. Neha (2020) & Arnesh Kumar v. State of Bihar (2014)",
        ],
        "canonical_expansion": "Section 498A IPC Section 85 BNS Cruelty husband relatives Dowry Prohibition Act PWDVA shared household Section 17 18 19 Section 125 CrPC maintenance Rajnesh v Neha",
    },

    # 2. Property Dispute: Ancestral Partition & Daughters' Equal Rights
    {
        "domain": "property_partition_daughters",
        "title": "Ancestral Property Partition & Daughters' Equal Coparcenary Rights",
        "triggers": [
            r"\b(ancestral property|ancestral land|ancestral house|family land)\b",
            r"\b(partition|share|shares|divide|division|portion)\b",
            r"\b(father died|father passed away|father death|without a will|without will|intestate)\b",
            r"\b(brother|brothers|brother's|son|sons)\b",
            r"\b(daughter|daughters|daughter's|sister|sisters)\b",
            r"\b(refusing.*share|deny.*share|locked.*house|taking all|no right)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Daughters / Sisters are completely in the right.**\n"
            "Under Indian Law, daughters have an equal birthright in ancestral coparcenary property identical to sons. "
            "Brothers have no legal authority to exclude their sisters or claim that daughters have no share in ancestral property."
        ),
        "supporting_sections": [
            "**Section 6 Hindu Succession Act, 1956 (Amended by Act 39 of 2005)**: A daughter of a coparcener by birth becomes a coparcener in her own right in the same manner as the son, with identical coparcenary rights and liabilities.",
            "**Section 8 Hindu Succession Act, 1956**: General rules of succession for male dying intestate. All Class I heirs (sons, daughters, widow, mother) take equal individual shares.",
            "**Order XXXIX Rules 1 & 2 CPC / Section 38 Specific Relief Act, 1963**: Application for temporary injunction restraining brothers from selling, alienating, or creating third-party rights.",
            "**Section 441 & 447 IPC / Section 329 BNS**: Criminal trespass if brothers forcefully displace lawful co-owners from joint possession.",
        ],
        "evidence_required": [
            "Death Certificate of the deceased father/ancestor.",
            "Legal Heir Certificate or Family Tree Certificate issued by the Tahsildar / Revenue Authority.",
            "Title Deeds, 7/12 extract, Jamabandi, or Sub-Registrar registered Sale/Gift deeds of the ancestral property.",
            "Proof of relationship (Aadhaar Card, Birth Certificate, School Leaving Certificate showing father's name).",
        ],
        "action_plan_advocate": (
            "1. **Civil Partition Suit**: File a formal Suit for Partition and Separate Possession before the Civil Court of competent pecuniary and territorial jurisdiction.\n"
            "2. **Ad-Interim Status Quo Injunction (Order 39 Rules 1-2 CPC)**: Move an urgent application for an interim injunction restraining brothers from mutating records, selling, transferring, or developing the property.\n"
            "3. **Caveat & Sub-Registrar Notice**: Issue a formal legal notice to the local Sub-Registrar alerting them not to register any unilateral transfer deed on the property schedule."
        ),
        "action_plan_client": (
            "1. **Do Not Sign Relinquishment**: Never sign any blank document, Release Deed, or Hakka Sod Patra (Relinquishment Deed) without your own independent advocate reviewing it.\n"
            "2. **Obtain Certified Records**: Apply online or through MeeSeva/e-District for certified copies of the ancestral land title records (Khata/Pahani/7-12).\n"
            "3. **Lodge Caveat**: File a caveat in the jurisdictional civil court so no ex-parte orders can be obtained against you."
        ),
        "landmarks": [
            "***Vineeta Sharma v. Rakesh Sharma* (2020) 9 SCC 1 (Supreme Court 3-Judge Bench)**: Authoritatively held that daughters have equal coparcenary rights by birth under Section 6 HSA from 1956 onwards, regardless of whether the father was alive on 9th September 2005.",
            "***Prasanta Kumar Sahoo v. Charulata Sahoo* (2023) Supreme Court**: Affirmed that prior oral partitions or unregistered family settlements cannot defeat a daughter's statutory coparcenary share.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/family_and_matrimonial_disputes_scenarios.pdf (Ancestral Property & Partition Scenario)",
            "[Statute] Hindu Succession Act, 1956 (Section 6: Devolution of Coparcenary Property)",
            "[Landmark Precedent] Vineeta Sharma v. Rakesh Sharma (2020) 9 SCC 1 (3-Judge Bench)",
            "[Procedural Law] Code of Civil Procedure, 1908 (Order XXXIX Rules 1 & 2 Injunctions)",
        ],
        "canonical_expansion": "Section 6 Hindu Succession Act 2005 coparcenary rights daughters Vineeta Sharma v Rakesh Sharma partition suit ancestral property Order 39 CPC injunction",
    },

    # 3. Financial Dispute: Cheque Bounce (Section 138 NI Act)
    {
        "domain": "cheque_bounce_138",
        "title": "Dishonour of Cheque & Financial Debt Recovery (Section 138 NI Act)",
        "triggers": [
            r"\b(cheque|check)\b",
            r"\b(bounce|bounced|dishonour|dishonored|insufficient funds|signature mismatch|account closed)\b",
            r"\b(loan|money|borrowed|lakhs|repayment|debt|creditor|debtor)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Payee (Creditor / Holder in Due Course) is in the right.**\n"
            "The issuance of a cheque that bounces due to insufficient funds or stopping payment constitutes a statutory criminal offence under Section 138 of the Negotiable Instruments Act, 1881. The drawer is criminally liable to face imprisonment and fine up to twice the cheque amount."
        ),
        "supporting_sections": [
            "**Section 138 Negotiable Instruments Act, 1881**: Dishonour of cheque for insufficiency of funds. Imprisonment up to 2 years, or fine up to twice the amount of the cheque, or both.",
            "**Section 142 NI Act**: Procedure for taking cognizance upon written complaint within 30 days of cause of action.",
            "**Section 143A NI Act**: Power of the Court to direct the accused drawer to deposit Interim Compensation up to 20% of the cheque amount during trial.",
            "**Sections 118 & 139 NI Act**: Statutory legal presumption in favor of holder that cheque was issued in discharge of a legally enforceable debt.",
        ],
        "evidence_required": [
            "Original Cheque with signature of drawer.",
            "Bank Return Memo with date and specific reason of dishonour (e.g. Funds Insufficient).",
            "Copy of the Statutory Legal Demand Notice issued within 30 days of Bank Memo.",
            "Postal Speed Post Receipt and Online Delivery Tracking Report showing delivery or refusal.",
            "Proof of transaction (Loan agreement, promissory note, invoice, or bank statement showing disbursement).",
        ],
        "action_plan_advocate": (
            "1. **Statutory Demand Notice (Strict 30-Day Window)**: Issue legal notice within 30 days of receiving bank memo demanding payment within 15 days of notice receipt.\n"
            "2. **Complaint under Section 142 NI Act (Strict 30-Day Window)**: Cause of action arises on the 16th day after notice delivery. File criminal complaint before Judicial Magistrate within 30 days.\n"
            "3. **Interim Compensation Application (Section 143A NI Act)**: Apply to court on first appearance of accused to order deposit of 20% interim compensation."
        ),
        "action_plan_client": (
            "1. **Act Within Timelines**: The 30-day notice timeline from the bank return memo is strict. Do not delay.\n"
            "2. **Retain Original Cheque & Memo**: Never surrender original cheque or return memo to the debtor without full cleared payment.\n"
            "3. **Preserve Postal Proof**: Download and save the India Post tracking delivery confirmation."
        ),
        "landmarks": [
            "***Dashrath Rupsingh Rathod v. State of Maharashtra* (2014) & 2015 NI Act Amendment**: Clarified territorial jurisdiction lies where payee's bank branch is located.",
            "***Bir Singh v. Mukesh Kumar* (2019) Supreme Court**: Held that even if particulars in cheque are filled by someone else, a voluntarily signed cheque attracts mandatory presumption under Section 139.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/financial_fraud_cheque_bounce_scenarios.pdf (Section 138 NI Act Scenario)",
            "[Statute] Negotiable Instruments Act, 1881 (Sections 138, 142, 143A)",
            "[Landmark Precedent] Dashrath Rupsingh Rathod v. State of Maharashtra & Bir Singh v. Mukesh Kumar",
        ],
        "canonical_expansion": "Section 138 Negotiable Instruments Act 30 days notice 15 days cure Section 142 NI complaint Section 143A interim compensation Dashrath Rupsingh Rathod",
    },

    # 4. Property Dispute: Illegal Land Encroachment & Trespass
    {
        "domain": "land_encroachment_trespass",
        "title": "Illegal Land Encroachment, Boundary Dispute & Criminal Trespass",
        "triggers": [
            r"\b(land encroachment|boundary wall|trespass|trespassing|encroached|illegal possession)\b",
            r"\b(vacant plot|neighbor building|dispossessed|illegal construction|shed|demolish)\b",
            r"\b(land grabbing|mafia|occupying|occupied my land)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Registered Titleholder / Lawful Owner is legally in the right.**\n"
            "Under Indian Law, unauthorized entry, breaking boundary walls, or constructing on another person's property constitutes actionable civil tort and cognizable criminal offences. The encroacher has zero legal claim to possession."
        ),
        "supporting_sections": [
            "**Section 441 & 447 IPC / Section 329 BNS**: Criminal Trespass. Punishable with imprisonment up to 3 months and fine.",
            "**Section 427 IPC / Section 324 BNS**: Mischief causing damage to property.",
            "**Section 5 & 6 Specific Relief Act, 1963**: Summary suit for recovery of possession within 6 months of dispossession.",
            "**Section 38 Specific Relief Act, 1963**: Perpetual Injunction restraining trespasser from interfering with peaceful possession.",
            "**Order XXXIX Rules 1 & 2 CPC**: Ad-interim injunction order for maintaining status quo.",
        ],
        "evidence_required": [
            "Registered Sale Deed / Title Deed of the property.",
            "Latest Revenue Encumbrance Certificate (EC) and Mutation / Khata extract.",
            "Photographs and video evidence of the encroachment, construction, or damage.",
            "Demarcation report issued by the local Revenue Inspector / Tehsildar.",
        ],
        "action_plan_advocate": (
            "1. **Civil Injunction Suit**: File suit for Perpetual Injunction and Declaration of Title under Section 34/38 Specific Relief Act with Order 39 interim stay.\n"
            "2. **Police FIR (Section 447 IPC)**: Lodge written complaint under Section 447 IPC for criminal trespass and Section 427 for mischief.\n"
            "3. **Revenue Demarcation**: Submit urgent demarcation petition before the Tahsildar with police assistance."
        ),
        "action_plan_client": (
            "1. **Do Not Engage in Physical Clashes**: Call emergency police (112) immediately and record timestamps of all unauthorized construction.\n"
            "2. **Gather Revenue Records**: Keep certified copies of your registered title deed and property tax receipts ready.\n"
            "3. **Erect Warning Signboard**: Put up an official sign indicating property ownership and pending legal proceedings."
        ),
        "landmarks": [
            "***Ramesh Chand Ardawatiya v. Anil Panjwani* (2003) Supreme Court**: Even an unauthorized occupant cannot be dispossessed by force without due process of law.",
            "***Sopan Sukhdeo Sable v. Assistant Charity Commissioner* (2004) Supreme Court**: Established tests for maintaining possession and grant of injunction.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/property_land_and_civil_disputes_scenarios.pdf (Land Encroachment Scenario)",
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Sections 441, 447: Criminal Trespass)",
            "[Statute] Specific Relief Act, 1963 (Sections 5, 6, 38)",
        ],
        "canonical_expansion": "Section 441 447 IPC Section 329 BNS Criminal Trespass Section 5 6 Specific Relief Act recovery possession Section 38 perpetual injunction Order 39 CPC",
    },

    # 5. Landlord-Tenant: Eviction & Non-Payment of Rent
    {
        "domain": "tenant_landlord_eviction",
        "title": "Tenant Non-Payment of Rent, Eviction & Unlawful Self-Help",
        "triggers": [
            r"\b(tenant|landlord|rent\s+agreement|lease|rented\s+(?:flat|house|shop|property)|my\s+flat|my\s+house)\b",
            r"\b(?:not\s+paying|stopped\s+paying|unpaid|defaulted\s+on).*(?:rent|dues)\b|\b(?:refus\w*|not)\s+to\s+vacate\b|\b(?:evict\w*|eviction|arrears\s+of\s+rent|holding\s+over)\b",
            r"\b(?:cut\s+(?:electricity|water|power)|locked\s+(?:premises|gate|door|flat)|force\s+out|throw\s+out|vacate)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**Both parties have specific legal boundaries:**\n"
            "1. **Landlord's Right**: Landlord has the absolute right to recover rent arrears, mesne profits, and vacant possession through due process of law.\n"
            "2. **Landlord's Unlawful Acts**: Landlord CANNOT cut off electricity, water, or lock premises. Such acts constitute criminal wrongful restraint (Section 339 IPC) and are punishable under State Rent Control Acts.\n"
            "3. **Tenant's Liability**: Tenant has no legal right to remain on premises without paying rent after notice expiry."
        ),
        "supporting_sections": [
            "**Section 106 Transfer of Property Act, 1882**: Mandatory 15-day (residential) or 6-month (commercial/manufacturing) Notice to Quit.",
            "**Section 339 & 341 IPC / Section 126 BNS**: Wrongful Restraint if landlord obstructs entry or cuts utilities.",
            "**Order XX Rule 12 CPC**: Mesne profits compensation for unauthorized use and occupation from date of expiry.",
            "**State Rent Control Act**: Statutory grounds for eviction (default in rent for over 2 months, bona fide personal requirement).",
        ],
        "evidence_required": [
            "Registered or Notarized Rent Agreement / Lease Deed.",
            "Bank statements showing default in monthly rent payments.",
            "Copy of the formal Notice to Quit sent via registered post with acknowledgment card.",
            "Property tax receipts and electricity meter documents.",
        ],
        "action_plan_advocate": (
            "1. **Notice to Quit (Section 106 TPA)**: Terminate tenancy by serving formal 15-day notice to quit.\n"
            "2. **Eviction Suit & Mesne Profits**: File suit for eviction and mesne profits before the Rent Controller or Civil Court.\n"
            "3. **Interim Rent Deposit (Order 39A CPC / Section 15 Rent Act)**: Move application directing tenant to deposit all admitted arrears in court before filing written statement."
        ),
        "action_plan_client": (
            "1. **Never Cut Utilities**: Do not cut power or water supply, as tenant can file criminal complaint or obtain re-connection order.\n"
            "2. **Issue Written Notice**: Do not rely on oral requests; serve written statutory notice through speed post.\n"
            "3. **Demand Mesne Profits**: Maintain written records of market rent in the locality to claim higher damages."
        ),
        "landmarks": [
            "***Ramesh Chand Ardawatiya v. Anil Panjwani* (2003) Supreme Court**: Due process of law is mandatory for evicting any tenant in settled possession.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/property_land_and_civil_disputes_scenarios.pdf (Tenant Eviction Scenario)",
            "[Statute] Transfer of Property Act, 1882 (Section 106 Notice to Quit)",
            "[Procedural Law] Code of Civil Procedure, 1908 (Order XX Rule 12 Mesne Profits)",
        ],
        "canonical_expansion": "Section 106 Transfer of Property Act Notice to Quit civil suit eviction mesne profits Ramesh Chand Ardawatiya due process of law",
    },

    # 6. Matrimonial: Mutual Consent Divorce & Child Custody
    {
        "domain": "divorce_custody_maintenance",
        "title": "Mutual Consent Divorce, Permanent Alimony & Child Custody",
        "triggers": [
            r"\b(mutual consent divorce|divorce|separated|living separately)\b",
            r"\b(cooling period|6 months period|waiver)\b",
            r"\b(child custody|custody of child|minor child|visitation rights)\b",
            r"\b(permanent alimony|alimony settlement|maintenance)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**In mutual consent divorce, both spouses have equal rights to separate amicably.**\n"
            "In child custody disputes, the supreme legal principle is: **The best physical, psychological, and educational welfare of the child is paramount**, overriding parental claims."
        ),
        "supporting_sections": [
            "**Section 13B Hindu Marriage Act, 1955**: Divorce by mutual consent after living separately for at least 1 year.",
            "**Section 25 Hindu Marriage Act, 1955**: Permanent alimony and maintenance based on financial status of parties.",
            "**Sections 7 & 17 Guardians and Wards Act, 1890**: Paramount welfare of the minor child.",
            "**Section 6 Hindu Minority and Guardianship Act, 1956**: Mother ordinarily has custody preference for children under 5 years.",
        ],
        "evidence_required": [
            "Marriage Certificate and proof of separate residence for more than 1 year.",
            "Joint Comprehensive Settlement Agreement specifying alimony amount and visitation schedule.",
            "Income affidavits and tax returns of both spouses.",
        ],
        "action_plan_advocate": (
            "1. **Joint Petition (Section 13B(1) HMA)**: File First Motion along with Memorandum of Understanding (MoU).\n"
            "2. **Waiver Application (Amardeep Singh Principle)**: Move application under Section 13B(2) to waive the 6-month statutory waiting period if mediation is complete.\n"
            "3. **Structured Alimony Escrow**: Ensure alimony Demand Drafts are handed over on recorded court record during Second Motion."
        ),
        "action_plan_client": (
            "1. **Formalize MoU**: Put every term (jewellery return, alimony installments, visitation days) into writing.\n"
            "2. **Child Stability**: Keep schooling, medical insurance, and emotional stability of children as joint priority.\n"
            "3. **Quashing of Criminal FIRs**: Ensure the settlement includes mutual withdrawal of any pending 498A or DV cases."
        ),
        "landmarks": [
            "***Amardeep Singh v. Harveen Kaur* (2017) Supreme Court**: 6-month cooling period under Section 13B(2) is directory and can be waived.",
            "***Gaurav Nagpal v. Sumedha Nagpal* (2009) Supreme Court**: Welfare of the child is the sole paramount consideration.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/family_and_matrimonial_disputes_scenarios.pdf (Divorce & Custody Scenario)",
            "[Statute] Hindu Marriage Act, 1955 (Section 13B, Section 25)",
            "[Landmark Precedent] Amardeep Singh v. Harveen Kaur & Gaurav Nagpal v. Sumedha Nagpal",
        ],
        "canonical_expansion": "Section 13B Hindu Marriage Act mutual consent divorce waiver cooling period Amardeep Singh Section 25 permanent alimony Guardians and Wards Act child welfare Gaurav Nagpal",
    },

    # 7. Real Estate: Builder Delay & Flat Possession
    {
        "domain": "builder_delay_rera",
        "title": "Delayed Flat Possession & Builder Default (RERA Protections)",
        "triggers": [
            r"\b(builder|developer|promoter|society)\b",
            r"\b(flat|apartment|possession|handover|hand over|booking amount)\b",
            r"\b(delayed|delay|late|years delay|not giving flat)\b",
            r"\b(rera|consumer court|compensation)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Homebuyer is entirely in the right.**\n"
            "Under Indian Law and RERA 2016, a builder cannot delay project completion indefinitely. One-sided clauses in builder agreements are unfair trade practice and unenforceable against homebuyers."
        ),
        "supporting_sections": [
            "**Section 18 RERA 2016**: Absolute right to full refund with interest (SBI MCLR + 2%) OR monthly interest compensation for every month of delay.",
            "**Section 19 RERA 2016**: Right of allottee to claim possession and compensation.",
            "**Consumer Protection Act, 2019**: Jurisdiction to claim compensation for mental harassment and deficiency in service.",
        ],
        "evidence_required": [
            "Builder-Buyer Agreement (BBA) with agreed possession date.",
            "Payment receipts, account statements, and home loan sanction letters.",
            "Written correspondence, emails, and demand letters sent to builder.",
        ],
        "action_plan_advocate": (
            "1. **RERA Complaint**: File formal complaint before the State Real Estate Regulatory Authority under Section 18/31.\n"
            "2. **Consumer Commission**: Alternatively, file consumer complaint before State/National Commission for deficiency in service.\n"
            "3. **Insolvency Petition**: Evaluate Section 7 IBC petition before NCLT if minimum threshold of 100 allottees or 10% is satisfied."
        ),
        "action_plan_client": (
            "1. **Do Not Sign Unfair Extensions**: Refuse to sign one-sided addendums waiving delay compensation.\n"
            "2. **Check RERA Registration**: Verify quarterly progress reports (QPR) on the State RERA portal.\n"
            "3. **Form Allottees Association**: Connect with other buyers in the same project to pool resources."
        ),
        "landmarks": [
            "***Pioneer Urban Land & Infrastructure v. Govindan Raghavan* (2019) Supreme Court**: Homebuyer cannot be compelled to wait indefinitely for possession.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/property_land_and_civil_disputes_scenarios.pdf (Builder Delay Scenario)",
            "[Statute] Real Estate (Regulation and Development) Act, 2016 (Section 18)",
            "[Landmark Precedent] Pioneer Urban Land v. Govindan Raghavan (2019)",
        ],
        "canonical_expansion": "Section 18 RERA refund with interest delay compensation Pioneer Urban Land Govindan Raghavan Consumer Protection Act",
    },

    # 8. Cyber Crime: Online Financial Fraud & OTP Scam
    {
        "domain": "cyber_financial_fraud",
        "title": "Cyber Financial Fraud, OTP Siphoning & Online Impersonation",
        "triggers": [
            r"\b(cyber|scam|scammer|hacked|fake call|caller)\b",
            r"\b(otp|bank account|upi|credit card|debit card|siphoned|money stolen)\b",
            r"\b(impersonating|fake profile|phishing)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Victim is in the right.**\n"
            "Identity theft, OTP manipulation, and computer-assisted cheating are severe criminal offences under the Information Technology Act, 2000 and Indian Penal Code."
        ),
        "supporting_sections": [
            "**Section 66C & 66D IT Act, 2000**: Identity theft and cheating by personation using computer resource (up to 3 years imprisonment).",
            "**Section 419 & 420 IPC / Section 318 & 319 BNS**: Cheating and cheating by personation.",
            "**RBI Circular on Customer Liability (2017)**: Zero liability of customer if reported within 3 days."
        ],
        "evidence_required": [
            "Bank transaction statement with UTR / Reference numbers.",
            "SMS screenshots containing fraudulent debit alerts.",
            "Phone numbers, URLs, and UPI IDs used by the scammer.",
        ],
        "action_plan_advocate": (
            "1. **Cyber Helpline (1930)**: Dial 1930 immediately to freeze the beneficiary bank account within the 'Golden Hour'.\n"
            "2. **Lodge Cyber Portal FIR**: Register complaint on **cybercrime.gov.in** with complete transaction trail.\n"
            "3. **Bank Grievance & Ombudsman**: Submit formal notice under RBI Zero Liability framework within 72 hours."
        ),
        "action_plan_client": (
            "1. **Call 1930 Immediately**: First 2 hours are critical to freeze stolen funds in scammer's bank accounts.\n"
            "2. **Block Cards & UPI**: Block cards, reset UPI PINs, and freeze compromised net banking.\n"
            "3. **Do Not Delete Messages**: Preserve the exact SMS and call logs as cyber forensic evidence."
        ),
        "landmarks": [
            "***RBI Guidelines on Zero Liability of Bank Customers (2017)***: Customer is immune from liability if unauthorized fraud is reported promptly.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/financial_fraud_cheque_bounce_scenarios.pdf (Cyber Fraud Scenario)",
            "[Statute] Information Technology Act, 2000 (Sections 66C, 66D)",
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Sections 419, 420)",
        ],
        "canonical_expansion": "Section 66C 66D IT Act 2000 identity theft Section 419 420 IPC 1930 helpline cybercrime portal golden hour RBI zero liability",
    },

    # 9. Motor Accident & Negligence
    {
        "domain": "accident_negligent_driving",
        "title": "Road Accident, Rash Driving & Motor Accident Claims (MACT)",
        "triggers": [
            r"\b(?:accident|crash|collision|hit\s+and\s+run|hit\s+by|speeding|truck\s+hit|car\s+hit|bike\s+hit|vehicle\s+hit)\b",
            r"\b(?:rash|negligent|speeding|careless).*(?:driving|driver|vehicle|truck|car|bus)\b|\b(?:injur\w*|fractur\w*|grievous\s+hurt|hospitalized|fatal|death|died|killed)\b",
            r"\b(?:mact|accident\s+claim|motor\s+accident|compensation|third\s+party\s+insurance|insurance\s+claim)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Victim / Injured / Heirs of Deceased are in the right.**\n"
            "Rash or negligent driving endangering human life is a criminal offence. The owner and insurer of the offending vehicle are strictly liable to pay compensation under the Motor Vehicles Act."
        ),
        "supporting_sections": [
            "**Section 279 & 304A IPC / Section 281 & 106 BNS**: Rash driving and causing death by negligence.",
            "**Section 106(2) BNS (Hit & Run)**: Up to 10 years imprisonment for fleeing without reporting to police.",
            "**Section 166 Motor Vehicles Act, 1988**: Claim petition for comprehensive compensation before MACT.",
        ],
        "evidence_required": [
            "Certified copy of FIR and Final Charge-sheet under Section 279/304A IPC.",
            "Medico-Legal Certificate (MLC), post-mortem report, and disability certificate.",
            "Offending vehicle registration number, driving license, and insurance policy details.",
            "Proof of income of victim (Salary slips, ITR, bank statements).",
        ],
        "action_plan_advocate": (
            "1. **Police FIR**: Ensure FIR is lodged immediately and Motor Accident Claims Tribunal (MACT) DAR (Detailed Accident Report) is prepared within 90 days under Section 159 MV Act.\n"
            "2. **MACT Claim Petition**: File Section 166 petition against driver, registered owner, and insurance company.\n"
            "3. **Multiplier Calculation**: Compute claim using the *Sarla Verma* and *Pranay Sethi* formulas."
        ),
        "action_plan_client": (
            "1. **Medical Care & MLC**: Obtain formal Medico-Legal Certificate (MLC) from the treating hospital.\n"
            "2. **Note Vehicle Details**: Note down license plate number, color, and photos of the offending vehicle.\n"
            "3. **Preserve Medical Bills**: Retain all original pharmacy receipts, surgery bills, and diagnostic scans."
        ),
        "landmarks": [
            "***Sarla Verma v. DTC* (2009) & *National Insurance v. Pranay Sethi* (2017) Supreme Court**: Established standard multiplier method and 40-50% future prospects addition.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/criminal_accidents_and_general_exceptions_scenarios.pdf (Road Accident Scenario)",
            "[Statute] Motor Vehicles Act, 1988 (Section 166: Compensation Claims)",
            "[Landmark Precedent] Sarla Verma v. DTC & National Insurance v. Pranay Sethi",
        ],
        "canonical_expansion": "Section 279 304A IPC Section 281 106 BNS Section 166 Motor Vehicles Act MACT Sarla Verma Pranay Sethi multiplier compensation",
    },

    # 10. Criminal: Self-Defence & Private Defence
    {
        "domain": "private_defence_assault",
        "title": "Right of Private Defence (Self-Defence of Person & Property)",
        "triggers": [
            r"\b(?:self\s+defen[cs]e|private\s+defen[cs]e|attacked\s+(?:me|us|my)|assaulted\s+(?:me|us)|ambushed)\b",
            r"\b(?:hit|struck|fought|defended|pushed|beat\w*).*(?:back|attacker)|protect\w*\s+myself|save\w*\s+(?:my|our)\s+life\b",
            r"\b(?:knife|gun|sword|rod|stick|weapon|deadly\s+weapon|imminent\s+threat|threatened\s+to\s+kill)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Defender acting in bona fide self-defence is protected under law.**\n"
            "Under Indian Law, nothing is an offence which is done in the lawful exercise of the right of private defence against imminent threat to life, grievous hurt, rape, or robbery."
        ),
        "supporting_sections": [
            "**Section 96 IPC / Section 34 BNS**: General Exception: Nothing is an offence which is done in private defence.",
            "**Section 100 IPC / Section 38 BNS**: When private defence of body extends to causing death (reasonable apprehension of death, grievous hurt, rape, kidnapping).",
            "**Section 103 IPC / Section 41 BNS**: When private defence of property extends to causing death (robbery, house-breaking by night).",
            "**Section 99 IPC / Section 37 BNS**: Proportionate force requirement; harm must not exceed necessity.",
        ],
        "evidence_required": [
            "Medical reports showing injuries sustained by defender during the assault.",
            "Photographs of scene of incident, weapons used by assailants, and damaged property.",
            "Immediate emergency call (112) records establishing who called police first.",
        ],
        "action_plan_advocate": (
            "1. **Raise Private Defence at Inception**: Plead General Exception under Section 96/100 IPC in the bail petition and statement under Section 313 CrPC.\n"
            "2. **Anticipatory / Regular Bail**: Move bail before Sessions Court citing *Satender Kumar Antil* and *Darshan Singh*.\n"
            "3. **Cross-FIR**: Ensure counter-complaint is formally registered against the actual aggressors."
        ),
        "action_plan_client": (
            "1. **Report to Police First**: Always report the attack immediately; being the first complainant establishes bona fides.\n"
            "2. **Document Your Injuries**: Get examined immediately at a government hospital to create an official MLC.\n"
            "3. **Do Not Conceal**: Truthfully state the sequence of aggression; law protects those facing imminent peril."
        ),
        "landmarks": [
            "***Darshan Singh v. State of Punjab* (2010) Supreme Court**: Formulated 10 cardinal principles of private defence; defender in imminent peril cannot weigh strikes in golden scales.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/criminal_accidents_and_general_exceptions_scenarios.pdf (Private Defence Scenario)",
            "[Local ChromaDB] backend/data/indian_penal_code_1860.pdf (Sections 96, 100, 103: Right of Private Defence)",
            "[Landmark Precedent] Darshan Singh v. State of Punjab (2010)",
        ],
        "canonical_expansion": "Section 96 100 103 IPC Section 34 38 41 BNS Right of Private Defence imminent peril Darshan Singh v State of Punjab",
    },

    # 11. Disputed Inheritance & Conflicting Wills (Indian Succession Act, 1925)
    {
        "domain": "conflicting_wills_inheritance_probate",
        "title": "Disputed Inheritance & Conflicting Wills (Indian Succession Act, 1925)",
        "triggers": [
            r"\b(will|wills|testament|testamentary|codicil|probate)\b",
            r"\b(conflicting wills|two wills|multiple wills|fake will|forged will|genuine will|later will|earlier will|second will|first will|registered will)\b",
            r"\b(grandfather|father|mother|grandmother|testator|deceased|passed away|died|demise|death)\b",
            r"\b(inheritance|inherit|inherited|property|ancestral|estate|bequeath|bequeathed|succession|share)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Propounder of the Subsequent (Later) Validly Executed Will has the primary legal claim, subject to strict judicial scrutiny:**\n\n"
            "1. **Rule of Later Will (The Last Will Prevails in Law)**: Under **Section 62 of the Indian Succession Act, 1925**, a Will is revocable by the testator at any point during their lifetime. Therefore, where two conflicting wills are presented, the **subsequent (later) valid Will operates as a statutory revocation of all prior inconsistent wills** (*'Voluntas posterior derogat priori'*).\n"
            "2. **Mandatory Burden of Proof & Dispelling Suspicious Circumstances**: Under the landmark Constitution Bench ruling in ***H. Venkatachala Iyengar v. B.N. Thimmajamma (AIR 1959 SC 443)***, the person who propounds the later Will bears the strict legal burden of proving: (a) valid execution and attestation by at least two witnesses under Section 63, (b) sound disposing state of mind and testamentary capacity of your grandfather, and (c) satisfactorily dispelling all suspicious circumstances (e.g., unnatural disposition, exclusion of natural heirs, or active involvement of a beneficiary in drafting/registering the Will).\n"
            "3. **What Happens if the Later Will is Forged or Invalidated**: If the probate court finds the subsequent Will forged, fabricated, or executed under coercion/undue influence, the earlier genuine Will remains legally binding. If both wills fail or are declared void, your grandfather's estate devolves by statutory **Intestate Succession** under Section 8 of the Hindu Succession Act, 1956 among all Class-I legal heirs in equal shares."
        ),
        "supporting_sections": [
            "**Section 62 Indian Succession Act, 1925**: Revocability of Will — A Will is liable to be revoked or altered by the maker at any time when competent to dispose of property. A subsequent inconsistent Will operates as an express or implied revocation of prior wills.",
            "**Section 63(c) Indian Succession Act, 1925**: Mandatory Statutory Execution — The Will must be signed/marked by the testator and attested by at least TWO witnesses, each of whom must have seen the testator sign and must sign the will in the presence of the testator.",
            "**Section 276 & 218 Indian Succession Act, 1925**: Petition for Probate (by Executor) or Letters of Administration with Will Annexed (by legal heir/beneficiary) before the District Judge / High Court exercising Original Testamentary Jurisdiction.",
            "**Section 284 Indian Succession Act & Section 148A CPC (Caveat)**: Statutory right of any interested legal heir to lodge a Caveat before the probate court to ensure no ex-parte probate or letters of administration can be issued without prior formal notice to them.",
            "**Section 68 Bharatiya Sakshya Adhiniyam, 2023 (BSA) / Section 68 Indian Evidence Act**: Mandatory Evidentiary Proof — A Will cannot be received in evidence until at least ONE attesting witness has been called to prove its execution, if alive and capable of giving evidence.",
            "**Section 69 Bharatiya Sakshya Adhiniyam, 2023 (BSA) / Section 69 IEA**: Proof when both attesting witnesses are dead or untraceable — The Will is proved by establishing the genuine handwriting and signature of at least one attesting witness and the testator.",
            "**Section 247 Indian Succession Act, 1925**: Appointment of Administrator *Pendente Lite* — Power of the court to appoint an independent administrator/receiver to manage, collect rents, and prevent waste or alienation of the estate while the probate suit is contested.",
            "**Order XXXIX Rules 1 & 2 CPC / Section 151 CPC**: Urgent application for Temporary Injunction restraining any family member, uncle, or claimant from selling, transferring, leasing, mortgaging, or mutating the inheritance properties pending court adjudication.",
            "**Section 52 Transfer of Property Act, 1882 (Doctrine of Lis Pendens)**: Any transfer or sale of estate property during pending court proceedings is strictly subservient to the final decree of the court.",
            "**Section 8 Hindu Succession Act, 1956**: Default rules of intestate succession for male Hindu dying without a valid will — all Class-I heirs (sons, daughters, widow, mother) take per capita equal shares.",
        ],
        "evidence_required": [
            "Originals of both conflicting Wills (or certified registration copies if registered at the Sub-Registrar office).",
            "Official Death Certificate of your grandfather issued by the Municipal Corporation / Registrar of Births & Deaths.",
            "Legal Heir Certificate or Family Genealogy Tree Certificate issued by the Tahsildar / Revenue Authority.",
            "Affidavits and sworn court testimonies of the two attesting witnesses who signed the genuine Will.",
            "Medical records, doctor's prescriptions, or mental fitness certificate of the grandfather around the date of execution proving sound disposing state of mind.",
            "Schedule of all movable and immovable estate properties (registered title deeds, Khata/Patta, bank accounts, FD receipts).",
        ],
        "action_plan_advocate": (
            "1. **File Urgent Caveat (Section 148A CPC / Section 284 Indian Succession Act)**: Immediately lodge a caveat in the District Court / High Court testamentary division to ensure no ex-parte grant of probate or letters of administration can be obtained by the rival party.\n"
            "2. **Petition for Probate / Letters of Administration (Section 276 Indian Succession Act)**: File a formal probate petition with the original Will annexed before the District Judge. When the rival party enters a caveat, the proceeding is automatically numbered and tried as a **Contested Testamentary Suit** under the Code of Civil Procedure.\n"
            "3. **Urgent Injunction & Administrator Pendente Lite (Order 39 CPC & Section 247 ISA)**: File an interim application restraining all parties from alienating, selling, or creating third-party rights on the estate, or pray for appointment of an Administrator *pendente lite* under Section 247 to collect rents and protect properties.\n"
            "4. **Dispel Suspicious Circumstances (Venkatachala Iyengar Doctrine)**: Prepare examination-in-chief of attesting witnesses and handwriting forensic expert to conclusively prove signature, voluntariness, and sound mental capacity of grandfather."
        ),
        "action_plan_client": (
            "1. **Do NOT Hand Over Original Will**: Keep the original Will, death certificate, and title deeds in a secure bank locker; only submit them directly to the Court through your advocate.\n"
            "2. **Locate the Attesting Witnesses Immediately**: Contact the two witnesses who signed the Will. Their sworn affidavit and court testimony are mandatory under Section 68 of the Evidence Act / BSA.\n"
            "3. **Stop Any Property Sale or Mutation**: Send a formal legal alert letter to the local Sub-Registrar and Revenue Tehsildar notifying them of the disputed wills and pending litigation so no property mutation or sale can take place.\n"
            "4. **Collect Medical Records**: If grandfather was elderly, obtain prescriptions or fitness slips from his treating doctor from the time the Will was made to defeat any claim of unsound mind or incapacity."
        ),
        "landmarks": [
            "***H. Venkatachala Iyengar v. B.N. Thimmajamma* (AIR 1959 SC 443 - Constitution Bench)**: Supreme Court Magna Carta on Wills: Propounder must prove due execution, attestation by 2 witnesses, testamentary capacity, and eliminate all suspicious circumstances.",
            "***Jaswant Kaur v. Amrit Kaur* ((1977) 1 SCC 369 - Supreme Court)**: Reaffirmed that the presence of suspicious circumstances shifts the entire burden onto the person propounding the will to satisfactorily explain them before probate can be granted.",
            "***Kavita Kanwar v. Pamela Mehta* ((2021) 11 SCC 209 - Supreme Court)**: Held that where a major beneficiary plays an active and leading part in the execution of the will which excludes other natural heirs, it constitutes a grave suspicious circumstance requiring conclusive proof.",
            "***Murthy v. C. Saradambal* ((2022) 3 SCC 209 - Supreme Court)**: Re-emphasized that registration of a Will does not dispense with the mandatory requirement of proving execution and attestation under Section 68 of the Evidence Act.",
        ],
        "citations": [
            "[Local ChromaDB] backend/data/property_land_and_civil_disputes_scenarios.pdf (Testamentary Succession & Disputed Will Scenario)",
            "[Statute] The Indian Succession Act, 1925 - Section 62 (Revocation of Will), Section 63 (Execution), Section 276 (Probate)",
            "[Statute] Bharatiya Sakshya Adhiniyam, 2023 - Section 68 & 69 (Mandatory Proof of Execution by Attesting Witness)",
            "[Landmark Precedent] H. Venkatachala Iyengar v. B.N. Thimmajamma, AIR 1959 SC 443 (Constitution Bench)",
            "[Landmark Precedent] Jaswant Kaur v. Amrit Kaur (1977) 1 SCC 369 & Kavita Kanwar v. Pamela Mehta (2021) 11 SCC 209",
            "[Procedural Law] Code of Civil Procedure, 1908 - Section 148A (Caveat) & Order XXXIX Rules 1-2 (Injunction)",
        ],
        "canonical_expansion": "Section 62 Indian Succession Act revocation later will Section 63 execution attestation Section 276 probate letters of administration Section 68 BSA evidence attesting witness H Venkatachala Iyengar suspicious circumstances Order 39 CPC injunction",
    },

    # 12. Police Inaction & Refusal to Register FIR
    {
        "domain": "police_fir_refusal_inaction",
        "title": "Police Refusal to Register FIR & Inaction (Mandatory Registration under Lalita Kumari)",
        "triggers": [
            r"\b(police|police station|station house officer|sho|inspector|cop|cops|thana)\b",
            r"\b(refus.*fir|not registering.*fir|won't register.*fir|denied fir|refusing complaint|no action|police inaction|not filing fir)\b",
            r"\b(fir|first information report|zero fir|complaint not taken)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Citizen / Complainant is legally in the right.**\n"
            "Under Indian Law, registration of a First Information Report (FIR) is **MANDATORY** for the police upon receiving information disclosing a cognizable offence. "
            "A police officer has **zero legal discretion to refuse or delay FIR registration**, and doing so is a punishable criminal offence under Section 166A IPC / Section 199 BNS."
        ),
        "supporting_sections": [
            "**Section 154(1) CrPC / Section 173(1) BNSS**: Mandatory registration of FIR in cognizable cases. Police MUST reduce the information to writing and provide a free copy to the informant.",
            "**Section 173(1) BNSS (Zero FIR & e-FIR)**: Explicit codification allowing registration of FIR irrespective of territorial jurisdiction, to be transferred to the jurisdictional police station.",
            "**Section 154(3) CrPC / Section 173(4) BNSS**: Remedy when Police Station refuses: Send substance of information in writing by registered post to the **Superintendent of Police (SP / DCP)**.",
            "**Section 156(3) CrPC / Section 175(3) BNSS**: Judicial Remedy: Application before the **Judicial Magistrate First Class (JMFC) / Metropolitan Magistrate** directing the police to register FIR and investigate.",
            "**Section 166A(c) IPC / Section 199 BNS**: Criminal penal liability on any public servant / police officer who fails to record any information given under Section 154(1) CrPC (punishable with 1 to 2 years rigorous imprisonment and fine).",
            "**Section 200 CrPC / Section 223 BNSS**: Direct Private Criminal Complaint before the Magistrate if police continue to stonewall.",
        ],
        "evidence_required": [
            "Copy of the written complaint submitted to the Police Station with acknowledgment seal / diary number (General Diary/GD entry).",
            "Speed Post receipt and online delivery tracking report showing delivery of complaint to the Superintendent of Police (SP/DCP).",
            "Date, time, and names/belt numbers of the police officers who refused to accept the complaint.",
            "All underlying documentary evidence of the cognizable crime (medical slips, chat screenshots, bank transactions, photos).",
        ],
        "action_plan_advocate": (
            "1. **Written SP Representation (Section 154(3) CrPC / Section 173(4) BNSS)**: Draft and send comprehensive written complaint by registered speed post to the Superintendent of Police / Commissioner of Police.\n"
            "2. **Magistrate Application (Section 156(3) CrPC / Section 175(3) BNSS)**: If SP fails to direct FIR within a reasonable time, file application under Section 156(3) CrPC supported by affidavit complying with *Priyanka Srivastava v. State of UP*.\n"
            "3. **High Court Writ of Mandamus (Article 226)**: If grave public injury or threat to life exists, move the High Court seeking a writ of mandamus commanding the Director General of Police (DGP) to register FIR and initiate disciplinary inquiry under Section 166A IPC."
        ),
        "action_plan_client": (
            "1. **Never Leave Without Proof**: Always take a signed, stamped acknowledgment on a photocopy of your complaint, or demand the GD (General Diary) Entry Number.\n"
            "2. **Send via Speed Post to SP**: If local police refuse, post the complaint immediately to the Superintendent of Police (SP/DCP) through India Post Speed Post and save the receipt.\n"
            "3. **Zero FIR Right**: If they claim 'this is not our jurisdiction', demand a **Zero FIR**. By law, they must record it and transfer it to the concerned police station.\n"
            "4. **Senior Helpline**: You can dial **112** (Emergency) or tweet to the official State Police Handle with the post tracking number."
        ),
        "landmarks": [
            "***Lalita Kumari v. Govt. of U.P.* (2014) 2 SCC 1 (5-Judge Constitution Bench)**: Supreme Court held that registration of FIR is MANDATORY under Section 154 if information discloses a cognizable offence. Police cannot conduct preliminary inquiry except in limited categories (matrimonial, medical, commercial, corruption).",
            "***Sakiri Vasu v. State of U.P.* (2008) 2 SCC 409**: Held that Section 156(3) CrPC provides an effective, complete statutory remedy; High Court writ petitions should not be filed without first exhausting Section 154(3) and Section 156(3).",
            "***Priyanka Srivastava v. State of U.P.* (2015) 6 SCC 287**: Mandated that every Section 156(3) application must be accompanied by an affidavit demonstrating prior compliance with Section 154(1) and 154(3).",
        ],
        "citations": [
            "[Landmark Precedent] Lalita Kumari v. Govt. of U.P. (2014) 2 SCC 1 (Mandatory FIR Registration)",
            "[Statute] Code of Criminal Procedure, 1973 - Section 154 & Section 156(3)",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 173 (Zero FIR) & Section 175(3)",
            "[Statute] Indian Penal Code, 1860 - Section 166A (Public Servant disobeying direction of law)",
        ],
        "canonical_expansion": "Section 154 CrPC Section 173 BNSS Lalita Kumari mandatory FIR registration Section 156 3 CrPC Section 175 3 BNSS SP complaint Section 154 3 Sakiri Vasu Section 166A IPC",
    },

    # 13. Landlord Refusing to Refund Security Deposit
    {
        "domain": "landlord_security_deposit_refund",
        "title": "Landlord Refusing to Refund Tenant Security Deposit after Vacating",
        "triggers": [
            r"\b(security deposit|rental deposit|deposit money|advance rent|caution deposit)\b",
            r"\b(landlord|owner|lessor)\b",
            r"\b(not returning|refusing to return|refund|withholding|deduct.*deposit|vacated|moved out|handover)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Tenant is legally in the right.**\n"
            "Under Indian Law, a security deposit is held by the landlord **in trust** as a guarantee against unpaid rent or actual physical damages. "
            "Once the tenant vacates, hands over peaceful possession, and clears utility bills, the landlord **MUST refund the deposit** within the agreed period (ordinarily within 30 days under the Model Tenancy Act). "
            "Unilateral deductions for normal wear and tear, repainting without contractual agreement, or arbitrary withholding constitutes **Breach of Contract** and **Criminal Breach of Trust**."
        ),
        "supporting_sections": [
            "**Section 73 Indian Contract Act, 1872**: Compensation for loss or damage caused by breach of contract. Landlord is liable for interest on unlawfully withheld funds.",
            "**Section 405 & 406 IPC / Section 316 BNS**: Criminal Breach of Trust. Landlord misappropriating entrusted security deposit is punishable with imprisonment up to 3 years or fine.",
            "**Section 415 & 420 IPC / Section 318(4) BNS**: Cheating if landlord induced deposit with prior dishonest intent not to refund.",
            "**Order XXXVII CPC (Summary Suit)**: Summary procedure for speedy recovery of liquidated money debt based on written rent agreement without full trial delay.",
            "**Model Tenancy Act (Section 11)**: Security deposit capped at 2 months for residential premises; must be refunded on date of taking vacant possession after adjusting dues.",
            "**Consumer Protection Act, 2019**: Available if tenancy was arranged through a commercial builder, co-living operator (e.g. Zolo, Stanza), or property management broker.",
        ],
        "evidence_required": [
            "Rent Agreement / Lease Deed showing deposit amount and refund terms.",
            "Bank statement / UPI transaction receipt showing payment of security deposit at inception.",
            "Written notice of vacating given within agreed notice period (email, WhatsApp, letter).",
            "Date-stamped photographs and video walkthrough of the flat upon vacating showing clean condition.",
            "No-dues electricity, water, and maintenance clearance receipts.",
            "Key handover acknowledgment or WhatsApp/email confirmation of possession transfer.",
        ],
        "action_plan_advocate": (
            "1. **Statutory Legal Demand Notice (15-Day Cure Period)**: Issue a formal advocate's notice demanding refund of principal deposit along with 18% p.a. commercial interest within 15 days.\n"
            "2. **Summary Suit (Order XXXVII CPC)**: File Summary Suit in the competent Civil Court for liquidated money recovery based on admitted rent agreement clause.\n"
            "3. **Police Complaint for Criminal Breach of Trust (Section 406 IPC / 316 BNS)**: If landlord behaves abusively or fraudulently evades, lodge formal criminal complaint for misappropriation of entrusted money."
        ),
        "action_plan_client": (
            "1. **Document Flat Condition**: Take a comprehensive 360-degree video walkthrough on the day you vacate showing intact walls, appliances, and fixtures.\n"
            "2. **Send Written Handover Email**: Send a formal email: 'I have handed over keys on [Date]. All utility bills are cleared. Please transfer the deposit of ₹[Amount] to [Bank Account] within 7 days.'\n"
            "3. **Reject Unlawful Painting Deductions**: Normal wear and tear is legally borne by landlord unless your agreement explicitly specifies repainting deduction.\n"
            "4. **Serve Legal Notice**: If unpaid after 15 days, have an advocate serve a legal notice; 90% of landlords refund upon receiving a formal advocate notice."
        ),
        "landmarks": [
            "***H.R. Basavaraj v. Canara Bank* (2010) 12 SCC 197**: Principles of breach of contract and recovery of deposited security sums.",
            "***State of Gujarat v. Jaswantlal Nathalal* (AIR 1968 SC 700)**: Entrustment under Section 405 IPC requires that property is handed over for a specific purpose and cannot be converted to personal use.",
        ],
        "citations": [
            "[Statute] Indian Contract Act, 1872 - Section 73 (Breach of Contract & Damages)",
            "[Statute] Indian Penal Code, 1860 - Section 405 & 406 (Criminal Breach of Trust)",
            "[Statute] Bharatiya Nyaya Sanhita, 2023 - Section 316 (Criminal Breach of Trust)",
            "[Procedural Law] Code of Civil Procedure, 1908 - Order XXXVII (Summary Suits for Debt Recovery)",
        ],
        "canonical_expansion": "security deposit refund landlord tenant flat vacated Section 73 Contract Act Section 406 IPC Section 316 BNS Order 37 CPC summary suit legal notice wear and tear",
    },

    # 14. Wrongful Termination & Unpaid Salary
    {
        "domain": "wrongful_termination_unpaid_salary",
        "title": "Wrongful Termination, Unpaid Salary & Relieving Letter Denial",
        "triggers": [
            r"\b(terminated|fired|dismissed|laid off|layoff|sacked|forced to resign)\b",
            r"\b(unpaid salary|salary not paid|pending salary|withholding salary|severance|gratuity|pf|provident fund)\b",
            r"\b(notice period|relieving letter|experience letter|without notice)\b",
            r"\b(employer|company|boss|hr|management)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Employee is legally in the right.**\n"
            "Under Indian Labour and Contract Law, an employer cannot arbitrarily terminate an employee without adhering to contractual notice period provisions or paying salary in lieu of notice. "
            "Furthermore, withholding accrued salary for days worked, denying statutory Gratuity (if 5+ years of service), or refusing to issue Relieving/Experience Letters is unlawful and actionable."
        ),
        "supporting_sections": [
            "**Section 73 Indian Contract Act, 1872**: Damages for breach of employment contract (notice pay, pending wages, incentive compensation).",
            "**Payment of Wages Act, 1936 (Section 5 & 15)**: Wages must be paid within 7 to 10 days of the wage period; employee can claim unpaid wages plus statutory compensation up to 10 times.",
            "**Industrial Disputes Act, 1947 (Section 25F)**: Retrenchment of workman without 1 month written notice and retrenchment compensation (15 days average pay per year of service) is void ab initio.",
            "**Payment of Gratuity Act, 1972 (Section 4 & 7)**: Mandatory gratuity for 5+ years continuous service; must be paid within 30 days along with simple interest.",
            "**State Shops and Commercial Establishments Act**: Statutory requirement of 30-day notice or wages in lieu thereof before termination.",
            "**Section 405 & 406 IPC / Section 316 BNS**: Criminal Breach of Trust if employer deducted Provident Fund (PF) or ESI from employee's salary but failed to deposit with EPFO.",
        ],
        "evidence_required": [
            "Employment Offer Letter, Employment Contract, and latest Appraisal/Revision letters.",
            "Salary slips for the last 6 months and bank statement showing salary credits.",
            "Termination email, termination letter, or WhatsApp communications from HR/Manager.",
            "Resignation acceptance or written handover completion confirmation.",
            "PF Account Number (UAN) and EPFO member passbook statement.",
        ],
        "action_plan_advocate": (
            "1. **Statutory Legal Notice for Recovery**: Issue formal demand notice for unpaid salary, notice pay, leave encashment, and issuance of Relieving Certificate within 15 days.\n"
            "2. **Labour Commissioner Complaint**: File conciliation petition before the jurisdictional Labour Commissioner / Conciliation Officer under the Industrial Disputes Act / Shops Act.\n"
            "3. **Summary Recovery Suit (Order XXXVII CPC)**: Initiate summary civil suit for recovery of liquidated contractual dues with 18% commercial interest.\n"
            "4. **EPFO / Gratuity Authority**: File complaint with Controlling Authority under Payment of Gratuity Act if gratuity is withheld."
        ),
        "action_plan_client": (
            "1. **Preserve All Work Records**: Backup all offer letters, salary slips, performance reviews, and email chains proving successful handover to your personal drive before company email is locked.\n"
            "2. **Do Not Sign Coerced Settlement**: Never sign a 'Full & Final Settlement' (FnF) or Release voucher that waives claims unless the money is actually credited into your bank account.\n"
            "3. **File Grievance on Samadhan Portal**: Register an online complaint on the Ministry of Labour & Employment portal (shramsuvidha.gov.in / samadhan.labour.gov.in).\n"
            "4. **EPFO Vigilance**: If PF deductions were not credited, lodge an immediate complaint on the EPFiGMS portal (epfigms.gov.in)."
        ),
        "landmarks": [
            "***Central Inland Water Transport Corp v. Brojo Nath Ganguly* (1986) 3 SCC 156**: Supreme Court held that arbitrary termination clauses permitting hire and fire without notice are unconscionable, void, and against public policy.",
            "***D.K. Yadav v. J.M.A. Industries* (1993) 3 SCC 259**: Principles of natural justice apply to termination of employment; termination without fair opportunity is invalid.",
        ],
        "citations": [
            "[Landmark Precedent] Central Inland Water Transport Corp v. Brojo Nath Ganguly (1986) 3 SCC 156",
            "[Statute] Payment of Wages Act, 1936 (Sections 5 & 15)",
            "[Statute] Industrial Disputes Act, 1947 (Section 25F Retrenchment)",
            "[Statute] Payment of Gratuity Act, 1972 (Section 4 & 7)",
            "[Contract Law] Indian Contract Act, 1872 (Section 73 Damages for Breach)",
        ],
        "canonical_expansion": "wrongful termination fired without notice unpaid salary notice period relieving letter experience letter Payment of Wages Act Industrial Disputes Act 25F Gratuity Brojo Nath Ganguly",
    },

    # 15. Consumer Protection & E-Commerce Fraud (Flipkart/Amazon Delivery Fraud)
    {
        "domain": "consumer_ecommerce_fraud",
        "title": "Consumer Rights, E-Commerce Delivery Fraud & Defective Goods (Consumer Protection Act, 2019)",
        "triggers": [
            r"\b(flipkart|amazon|meesho|myntra|zomato|swiggy|ecommerce|e-commerce|online\s+shopping|online\s+order|seller)\b",
            r"\b(?:fake|counterfeit|wrong|defective|damaged|empty|broken).*(?:product|item|good|device|phone|parcel|box|delivery|shipment)\b|\b(?:soap|stone|brick|tile|wood).*(?:box|package|delivery|parcel|received)\b|\b(?:received|got).*(?:soap|stone|fake|counterfeit|empty)\b",
            r"\b(refund\s+(?:refused|denied|rejected|not\s+given)|refusing\s+(?:refund|return|replacement)|replacement\s+(?:denied|refused)|customer\s+care|consumer\s+(?:court|forum|commission|complaint|helpline))\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Consumer is legally in the right.**\n"
            "Under the **Consumer Protection Act, 2019** and the **Consumer Protection (E-Commerce) Rules, 2020**, online marketplaces and sellers are strictly prohibited from indulging in Unfair Trade Practices or Deficiency in Service. "
            "Delivering a counterfeit item, fake product, or soap/stone instead of the ordered product is both an actionable consumer wrong and a criminal offence of **Cheating (Section 420 IPC / Section 318 BNS)**. "
            "The platform cannot escape liability by claiming to be merely an 'intermediary'."
        ),
        "supporting_sections": [
            "**Section 2(47) Consumer Protection Act, 2019**: Unfair Trade Practice (delivering false goods, misleading representations).",
            "**Section 2(11) CPA 2019**: Deficiency in Service (refusal to rectify, non-refund, or failure to honor warranty).",
            "**Section 35 CPA 2019**: Filing consumer complaint before the **District Consumer Disputes Redressal Commission (DCDRC)** (pecuniary jurisdiction up to ₹50 Lakhs).",
            "**Section 84 & 86 CPA 2019**: Product Liability action against Product Manufacturer and E-Commerce Service Provider for defective goods and damages.",
            "**Consumer Protection (E-Commerce) Rules, 2020**: Rule 5 & 6 mandatory grievance redressal, return/refund mechanism, and prohibition of unfair platform fees.",
            "**Section 415 & 420 IPC / Section 318(4) BNS**: Cheating and dishonest inducement to deliver money.",
        ],
        "evidence_required": [
            "Order invoice and payment receipt showing transaction ID.",
            "Unboxing video of the parcel showing delivery label, tracking barcode, and parcel opening without cuts.",
            "Photographs of the fake/wrong item received along with the original outer courier box.",
            "Screenshots of communication with Customer Care, complaint ticket IDs, and refusal emails.",
            "Courier delivery confirmation SMS / OTP timestamp.",
        ],
        "action_plan_advocate": (
            "1. **Statutory Demand Notice to E-Commerce & Seller**: Issue 7-day legal notice demanding full refund plus compensation for mental harassment.\n"
            "2. **File E-Daakhil Consumer Complaint (Section 35 CPA 2019)**: File petition online on **edaakhil.nic.in** before the District Consumer Commission praying for: (a) full refund with 12% interest, (b) compensation of ₹25,000–₹50,000 for mental agony, and (c) litigation costs.\n"
            "3. **Police Complaint for Delivery Fraud**: If systematic courier theft or deliberate fraud occurred, file complaint with the Cyber Crime / Local Police under Section 420 IPC."
        ),
        "action_plan_client": (
            "1. **Lodge National Consumer Helpline (NCH) Complaint**: Call **1915** or register on **consumerhelpline.gov.in** / WhatsApp to 8800001915 immediately; NCH achieves 70%+ resolution for e-commerce.\n"
            "2. **Always Record Unboxing Video**: For high-value electronics (iPhone, laptop), always take a continuous, unedited video while cutting the tamper tape.\n"
            "3. **Credit Card Chargeback**: If paid via Credit Card, raise a formal Chargeback dispute with your card issuing bank for 'Goods Not As Described' within 60 days.\n"
            "4. **Social Media Grievance**: Post on X (formerly Twitter) tagging the company's official grievance handle and Consumer Affairs Ministry (@jagograhakjago)."
        ),
        "landmarks": [
            "***SGS India Ltd. v. Dolphin International Ltd.* (2021) Supreme Court**: Clarified burden of proof in deficiency of service under consumer law.",
            "***Amazon Wholesale India v. Competition Commission of India***: E-commerce platforms held to strict accountability standards for seller representations.",
        ],
        "citations": [
            "[Statute] Consumer Protection Act, 2019 (Sections 2(47), 35, 84-86)",
            "[Statute] Consumer Protection (E-Commerce) Rules, 2020",
            "[Portal] National Consumer Helpline (NCH - 1915) & E-Daakhil Portal",
            "[Statute] Indian Penal Code, 1860 - Section 420 (Cheating)",
        ],
        "canonical_expansion": "Consumer Protection Act 2019 unfair trade practice deficiency in service flipkart amazon refund soap in box fake product edaakhil NCH 1915 Section 35 DCDRC",
    },

    # 16. Medical Negligence & Surgical Malpractice
    {
        "domain": "medical_negligence_malpractice",
        "title": "Medical Negligence, Surgical Carelessness & Hospital Malpractice",
        "triggers": [
            r"\b(doctor|surgeon|hospital|clinic|nursing home|anaesthetist)\b",
            r"\b(medical negligence|wrong surgery|wrong operation|sponge inside|surgical tool left|careless surgery|died during surgery|wrong injection|wrong medicine|medical malpractice)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Patient / Family of the Victim is legally in the right.**\n"
            "Under Indian Law, a medical professional owes a duty of care in deciding whether to undertake the case, duty of care in deciding what treatment to give, and duty of care in the administration of that treatment. "
            "Leaving a surgical sponge, cotton swab, or instrument inside the patient's body is an open and shut case of gross negligence where the doctrine of ***Res Ipsa Loquitur* (the thing speaks for itself)** applies directly."
        ),
        "supporting_sections": [
            "**Section 304A IPC / Section 106(1) BNS**: Causing death by rash or negligent act (punishable with imprisonment up to 2 years or fine or both; 5 years under BNS).",
            "**Section 336, 337, 338 IPC / Section 125 BNS**: Causing hurt or grievous hurt by rash or negligent act endangering human life.",
            "**Consumer Protection Act, 2019 (Section 35 / 47 / 58)**: Compensation before Consumer Commission for medical deficiency in service (*IMA v. V.P. Shantha*).",
            "**Law of Torts (Vicarious Liability)**: Hospital is strictly vicariously liable for the negligent acts and surgical omissions of its doctors, nurses, and operating theatre staff.",
            "**National Medical Commission (NMC) Regulations**: Disciplinary inquiry and permanent cancellation of medical license for gross professional misconduct.",
        ],
        "evidence_required": [
            "Complete Certified In-Patient Bed Head Ticket (BHT), OT notes, and Anaesthesia notes from the hospital.",
            "Subsequent diagnostic CT scans, X-rays, or Ultrasound reports showing foreign object / surgical complication.",
            "Second surgery operative notes and pathology report of the extracted foreign body.",
            "Discharge summary, pharmacy bills, and death certificate / post-mortem report (if fatality occurred).",
        ],
        "action_plan_advocate": (
            "1. **Seize Medical Records Immediately**: Issue urgent legal notice demanding certified copies of the complete hospital record under NMC Regulations.\n"
            "2. **State / National Consumer Commission Claim**: File consumer complaint for medical negligence claiming substantial damages (for loss of life, revision surgeries, physical trauma, and loss of income).\n"
            "3. **Medical Board Reference (*Jacob Mathew* Protocol)**: For criminal prosecution under Section 304A IPC, ensure reference to an independent panel of qualified doctors through the Chief Medical Officer (CMO).\n"
            "4. **State Medical Council Complaint**: Lodge complaint for disciplinary action and suspension of medical license."
        ),
        "action_plan_client": (
            "1. **Demand Complete Case Sheet Immediately**: Under NMC (Medical Council) regulations, the hospital is legally bound to provide complete medical records within **72 hours** of request.\n"
            "2. **Preserve Forensic Proof**: If a second corrective surgery was conducted, preserve the extracted surgical object and hospital histopathology report.\n"
            "3. **Independent Medical Opinion**: Consult a specialist from an independent government teaching hospital (e.g. AIIMS/PGI) to evaluate treatment deviation.\n"
            "4. **Police Complaint for Inquest**: If patient expired under suspicious circumstances, request immediate police inquest and post-mortem examination."
        ),
        "landmarks": [
            "***Jacob Mathew v. State of Punjab* (2005) 6 SCC 1 (3-Judge Bench)**: Supreme Court Magna Carta on Medical Negligence: Criminal liability requires 'gross negligence'; police cannot arrest doctors without an independent medical board opinion.",
            "***Achutrao Haribhau Khodwa v. State of Maharashtra* (1996) 2 SCC 634**: Supreme Court held that leaving a mop/towel in the patient's abdomen during surgery is negligence per se; *res ipsa loquitur* applies directly.",
            "***Indian Medical Association (IMA) v. V.P. Shantha* (1995) 6 SCC 651**: Medical services rendered for consideration fall squarely within the definition of 'service' under consumer protection laws.",
        ],
        "citations": [
            "[Landmark SC] Jacob Mathew v. State of Punjab (2005) 6 SCC 1 (Gross Negligence Standard)",
            "[Landmark SC] Achutrao Haribhau Khodwa v. State of Maharashtra (1996) 2 SCC 634 (Res Ipsa Loquitur)",
            "[Statute] Indian Penal Code, 1860 - Section 304A & Section 338",
            "[Statute] Consumer Protection Act, 2019 (Medical Services Compensation)",
        ],
        "canonical_expansion": "medical negligence doctor wrong surgery surgical sponge inside Jacob Mathew Achutrao Haribhau Khodwa res ipsa loquitur Section 304A IPC Section 106 BNS consumer forum NMC",
    },

    # 17. Cyber Blackmail, Sextortion, Morphed Photos & Revenge Porn
    {
        "domain": "cyber_blackmail_sextortion_morphing",
        "title": "Cyber Blackmail, Sextortion, Morphed Photos & Non-Consensual Imagery",
        "triggers": [
            r"\b(blackmail|blackmailing|extortion|extorting money|demanding ransom)\b",
            r"\b(private photos|nude photos|naked pictures|morphed photos|deepfake|intimate video|video call trap|sextortion|revenge porn|leaking video)\b",
            r"\b(instagram|facebook|telegram|whatsapp|social media|contacts)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Victim is legally in the right and completely protected under law.**\n"
            "Under Indian Law, capturing, publishing, transmitting, or blackmailing anyone with private or sexually explicit images is a **grave, non-bailable criminal offence** under the Information Technology Act and Bharatiya Nyaya Sanhita / IPC. "
            "The victim has the absolute right to emergency content takedown, privacy preservation, and police protection."
        ),
        "supporting_sections": [
            "**Section 66E IT Act, 2000**: Violation of privacy (capturing, publishing, or transmitting images of private area of any person without consent) — imprisonment up to 3 years and fine.",
            "**Section 67 & 67A IT Act, 2000**: Publishing or transmitting sexually explicit act in electronic form — **Cognizable & Non-Bailable**, imprisonment up to 5 years (first conviction) / 7 years (subsequent).",
            "**Section 354C IPC / Section 77 BNS (Voyeurism)**: Watching, capturing, or disseminating images of a woman in private acts — imprisonment up to 3 to 7 years.",
            "**Section 354D IPC / Section 78 BNS (Stalking)**: Online stalking and monitoring woman's internet/electronic use.",
            "**Section 383 & 384 IPC / Section 308 BNS (Extortion)**: Putting person in fear of injury to reputation and dishonestly inducing payment — up to 3 years imprisonment.",
            "**Section 503 & 506 IPC / Section 351 BNS (Criminal Intimidation)**: Threatening injury to reputation or person.",
            "**Rule 3(2)(b) Information Technology Rules, 2021**: Mandatory **24-Hour Takedown Rule**: Social media intermediaries (Instagram, Meta, Telegram) MUST remove non-consensual intimate content within 24 hours of receipt of complaint.",
        ],
        "evidence_required": [
            "Screenshots of the blackmail chats showing phone numbers, usernames, and threats.",
            "Profile URLs and handles of the extortionists on Instagram, Telegram, or WhatsApp.",
            "UPI IDs, QR codes, or cryptocurrency addresses provided by the blackmailer.",
            "Call logs with timestamps of threatening calls.",
        ],
        "action_plan_advocate": (
            "1. **Emergency Police & Cyber Cell FIR**: Lodge formal FIR under Sections 66E, 67A IT Act and Sections 384, 506 IPC at the Cyber Crime Police Station.\n"
            "2. **Intermediary Notice under IT Rules 2021**: Serve immediate legal takedown notice to Grievance Officers of Meta/Instagram/Telegram mandating content deletion within 24 hours under Rule 3(2)(b).\n"
            "3. **In-Camera & Identity Concealment Application**: Move application before Magistrate under Section 327 CrPC / Section 366 BNSS to ensure victim's name is completely redacted and masked from all public records."
        ),
        "action_plan_client": (
            "1. **NEVER PAY MONEY**: Do NOT pay a single rupee. Blackmailers never delete files after payment; they demand more money.\n"
            "2. **Report Immediately on Cybercrime Portal**: File an anonymous or formal complaint on **cybercrime.gov.in** under the 'Report Women/Children Related Crime' section.\n"
            "3. **Dial Cyber Helpline 1930**: Call **1930** immediately to report the transaction trail if any money was paid.\n"
            "4. **Take Down Content via StopNCII.org**: Upload the image hashes on **StopNCII.org** (Stop Non-Consensual Intimate Image Abuse); it hashes images so Meta, Instagram, and TikTok automatically block them from being uploaded."
        ),
        "landmarks": [
            "***Shreya Singhal v. Union of India* (2015) 5 SCC 1**: Upheld blocking of unlawful content and clarified intermediary liability under Section 79 IT Act.",
            "***Justice K.S. Puttaswamy v. Union of India* (2017) 10 SCC 1**: Right to privacy and bodily integrity is an inviolable fundamental right under Article 21.",
        ],
        "citations": [
            "[Statute] Information Technology Act, 2000 (Sections 66E, 67, 67A - Non-Bailable)",
            "[Statute] Information Technology (Intermediary Guidelines) Rules, 2021 (Rule 3(2)(b) 24-Hour Takedown)",
            "[Statute] Indian Penal Code, 1860 - Section 354C (Voyeurism), Section 384 (Extortion)",
            "[Portal] National Cyber Crime Reporting Portal (cybercrime.gov.in) & StopNCII.org",
        ],
        "canonical_expansion": "sextortion cyber blackmail morphed photos private pictures 66E 67 67A IT Act Section 354C IPC voyeurism Section 384 extortion 1930 cybercrime portal StopNCII",
    },

    # 18. Defamation & Social Media Slander
    {
        "domain": "defamation_social_media_slander",
        "title": "Defamation, Online Slander & Social Media Character Smear",
        "triggers": [
            r"\b(defamation|defame|defamed|defaming|slander|libel|tarnishing reputation|character assassination)\b",
            r"\b(social media|instagram|facebook|twitter|youtube|whatsapp group|linkedin|public post)\b",
            r"\b(calling me fraud|false allegations|fake review|smear campaign|called me scammer)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Defamed Party / Complainant is legally in the right.**\n"
            "Under Indian Law, a person's reputation is an intrinsic component of their personal liberty and dignity protected under Article 21 of the Constitution. "
            "Publishing or speaking unverified, scandalous, or false imputations intending to harm reputation is actionable both as a **Civil Tort (for monetary damages)** and as a **Criminal Offence (Section 499/500 IPC / Section 356 BNS)**."
        ),
        "supporting_sections": [
            "**Section 499 IPC / Section 356(1) BNS**: Definition of Criminal Defamation (words spoken, written, or visual representations intending to harm reputation, subject to 10 statutory exceptions like truth for public good).",
            "**Section 500 IPC / Section 356(2) BNS**: Punishment for Defamation (simple imprisonment up to 2 years, or fine, or both; community service introduced in BNS).",
            "**Section 501 & 502 IPC / Section 356(3) BNS**: Printing or selling defamatory matter.",
            "**Civil Law of Torts**: Civil Suit for recovery of unliquidated general and special damages for loss of reputation, business distress, and mental agony.",
            "**Order XXXIX Rules 1 & 2 CPC**: Application for **Interim Injunction (Gag Order)** directing removal of defamatory posts and restraining future publications.",
            "**Section 199 CrPC / Section 222 BNSS**: Prosecution procedure for defamation upon private complaint before Judicial Magistrate.",
        ],
        "evidence_required": [
            "Screen captures and full URL links of the defamatory social media posts, comments, or video streams.",
            "Proof of publication to third parties (likes, shares, comments, or witness affidavits who read the post).",
            "Certificate under Section 63 Bharatiya Sakshya Adhiniyam, 2023 (BSA) / Section 65B Evidence Act for electronic printouts.",
            "Evidence demonstrating that the allegations are completely false and fabricated.",
            "Proof of actual injury or damage (loss of employment, cancelled contracts, business decline, or psychiatric distress).",
        ],
        "action_plan_advocate": (
            "1. **Cease and Desist Legal Notice**: Serve formal legal notice demanding unconditional public apology and immediate deletion of posts within 48 hours.\n"
            "2. **Civil Suit for Damages & Injunction**: File Civil Suit for Defamation with Order 39 application for immediate ex-parte ad-interim injunction directing removal of URLs.\n"
            "3. **Criminal Complaint under Section 500 IPC**: File private criminal complaint under Section 200 CrPC / Section 223 BNSS before the Metropolitan Magistrate.\n"
            "4. **Intermediary Takedown Notice**: Serve takedown notice on the social media platform attaching court complaint."
        ),
        "action_plan_client": (
            "1. **Do NOT Engage in Flame Wars**: Never post counter-abuses or retaliatory slurs, as it weakens your legal standing and gives them a cross-defamation claim.\n"
            "2. **Take High-Resolution Screenshots**: Capture full screenshots showing date, timestamp, profile handle, URL, and follower/like counts.\n"
            "3. **Archive via Wayback Machine**: Save the URL on archive.org or archive.is to preserve permanent proof in case they delete the post.\n"
            "4. **Issue Advocate Notice**: Most social media bullies delete posts immediately once they receive a formal Advocate's Legal Notice."
        ),
        "landmarks": [
            "***Subramanian Swamy v. Union of India* (2016) 7 SCC 221**: Supreme Court upheld the constitutional validity of Sections 499 & 500 IPC, holding that the right to free speech (Art 19(1)(a)) cannot destroy another's right to reputation (Art 21).",
            "***Swami Ramdev v. Juggernaut Books Pvt Ltd* (2018) Delhi High Court**: Affirmed principles for grant of injunction against defamatory publications.",
        ],
        "citations": [
            "[Landmark SC] Subramanian Swamy v. Union of India (2016) 7 SCC 221 (Validity of Criminal Defamation)",
            "[Statute] Indian Penal Code, 1860 - Section 499 & Section 500",
            "[Statute] Bharatiya Nyaya Sanhita, 2023 - Section 356 (Defamation)",
            "[Procedural Law] Code of Civil Procedure, 1908 - Order XXXIX Rules 1 & 2 (Injunction against Publication)",
        ],
        "canonical_expansion": "Section 499 500 IPC Section 356 BNS defamation slander libel social media false allegations damages Subramanian Swamy cease and desist Order 39 CPC",
    },

    # 19. Recovery of Unpaid Loan & Debt
    {
        "domain": "money_recovery_unpaid_loan",
        "title": "Recovery of Unpaid Friendly Loan, Promissory Note & Business Debt",
        "triggers": [
            r"\b(?:borrow\w*|lent|gave|loan\w*|advance\w*).*(?:money|lakhs|crores|cash|funds|amount)\b|\b(?:friendly\s+loan|hand\s+loan|personal\s+loan|unpaid\s+loan)\b",
            r"\b(?:not|refus\w*|failed|default\w*).*(?:return|pay\s+back|repay|refund).*(?:money|loan|amount|dues)\b|\b(?:debt\s+recovery|recover\s+money|defaulter)\b",
            r"\b(?:promissory\s+note|pronote|cheque|iou|borrower|creditor|summary\s+suit|order\s+37)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Creditor / Lender is legally in the right.**\n"
            "Under Indian Law, when money is lent under an express or implied promise of repayment, the borrower is under a strict legal obligation to return the principal sum with agreed interest. "
            "Failing to repay is a breach of contract, and where the borrower borrowed with dishonest intention from the very beginning, it also constitutes **Cheating (Section 420 IPC / Section 318 BNS)**."
        ),
        "supporting_sections": [
            "**Order XXXVII CPC (Summary Suit)**: Fast-track civil suit for recovery of debt arising on a written contract, bill of exchange, promissory note, or admitted financial transaction.",
            "**Section 73 Indian Contract Act, 1872**: Compensation for loss caused by breach of contractual repayment obligation.",
            "**Negotiable Instruments Act, 1881 (Section 4)**: Enforcement of Promissory Note (pronote).",
            "**Article 19 & 21 Limitation Act, 1963**: Strict **3-Year Limitation Period** from the date when the loan was made or date of default.",
            "**Section 18 Limitation Act, 1963**: A written acknowledgment of debt (including WhatsApp message or email admitting balance) resets the 3-year limitation clock.",
            "**Section 415 & 420 IPC / Section 318(4) BNS**: Cheating if the debtor gave false promises or induced money with zero intention to return.",
        ],
        "evidence_required": [
            "Bank account statement showing debit / NEFT / RTGS / UPI transfer of the loan amount to the borrower.",
            "Promissory Note, loan agreement, IOU, or signed acknowledgment on stamp paper.",
            "WhatsApp chats, SMS, or audio recordings where borrower admits the debt and promises repayment.",
            "Copy of the Statutory Legal Demand Notice with speed post delivery tracking receipt.",
            "Income tax return (ITR) records if the loan was reflected in your balance sheet.",
        ],
        "action_plan_advocate": (
            "1. **Statutory Demand Notice (15 Days)**: Serve formal demand notice calling upon debtor to repay the outstanding sum with 18% p.a. interest within 15 days.\n"
            "2. **Summary Suit (Order XXXVII CPC)**: Institute summary suit in Civil Court; defendant cannot defend unless they obtain leave to defend by demonstrating a bona fide defense.\n"
            "3. **Attachment Before Judgment (Order 38 Rule 5 CPC)**: Move application to attach borrower's bank accounts or immovable property before judgment if they attempt to dispose of assets.\n"
            "4. **Criminal Complaint (Section 420 IPC)**: If debtor gave fake cheques or forged security documents, lodge FIR for cheating."
        ),
        "action_plan_client": (
            "1. **Get Written Acknowledgment**: Send a casual WhatsApp message: 'Hi, just reminding you that ₹[Amount] borrowed on [Date] is overdue. When can you transfer it?' A reply like 'Will pay next month' is legally binding proof resetting limitation!\n"
            "2. **Watch the 3-Year Clock**: Do not delay past 3 years from the date of loan; time-barred debts cannot be enforced through courts.\n"
            "3. **Avoid Cash Transactions**: Courts strictly scrutinize cash loans above ₹20,000 under Section 269SS of the Income Tax Act; always rely on bank transfer proof.\n"
            "4. **Serve Legal Notice**: Engage an advocate to issue a formal demand notice; this is mandatory before instituting commercial summary suits."
        ),
        "landmarks": [
            "***IDBI Trusteeship Services Ltd. v. Hubtown Ltd.* (2017) 1 SCC 568**: Supreme Court established definitive principles governing leave to defend in Order 37 summary suits.",
            "***Basalingappa v. Mudibasappa* (2019) 5 SCC 418**: Financial capacity and transaction records are essential to prove loan disbursement.",
        ],
        "citations": [
            "[Procedural Law] Code of Civil Procedure, 1908 - Order XXXVII (Summary Procedure)",
            "[Statute] Indian Contract Act, 1872 - Section 73 (Damages for Breach)",
            "[Statute] Limitation Act, 1963 - Article 19 & Section 18 (Acknowledgment of Debt)",
            "[Landmark Precedent] IDBI Trusteeship Services v. Hubtown Ltd. (2017)",
        ],
        "canonical_expansion": "recovery of money unpaid loan friendly loan Order 37 CPC summary suit Section 73 Contract Act limitation 3 years promissory note legal notice",
    },

    # 20. Forged Property Documents & Registry Fraud
    {
        "domain": "property_document_forgery_fraud",
        "title": "Forged Property Documents, Sale Deed Impersonation & Registry Fraud",
        "triggers": [
            r"\b(forged|fake|fabricated|forgery|impersonat\w*).*(?:signature|sale\s+deed|deed|registry|document|paper|power\s+of\s+attorney|poa|title|agreement)\b|\b(?:forged|fabricated|impersonation|fake\s+registry|fake\s+sale\s+deed)\b",
            r"\b(?:sold|transferred|alienated|registered|grabbed|looted).*(?:land|property|house|flat|plot|site|home|estate|patta|khata)\b|\b(?:fraudulent\s+transfer|fake\s+power\s+of\s+attorney|fake\s+poa)\b",
            r"\b(sub-registrar|registrar|patwari|tehsildar|land\s+mafia|property\s+fraud|registry\s+fraud)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Lawful Registered Titleholder is legally in the right.**\n"
            "Under Indian Law, a forged document is **a complete nullity (*void ab initio*)**. "
            "No title or ownership can ever pass on the basis of a forged deed (*'Nemo dat quod non habet'* — no one can give what they do not have). "
            "Creating or registering fraudulent land records constitutes grave non-bailable criminal forgery punishable with up to **Life Imprisonment**."
        ),
        "supporting_sections": [
            "**Section 463 & 465 IPC / Section 336 BNS**: Forgery and punishment for forgery (up to 2 years imprisonment).",
            "**Section 467 IPC / Section 338 BNS**: Forgery of valuable security, will, or authority to transfer property — **Punishable with Imprisonment for Life**, or imprisonment up to 10 years, and fine (**Cognizable & Non-Bailable**).",
            "**Section 468 & 471 IPC / Section 336 & 340 BNS**: Forgery for purpose of cheating and using as genuine a forged document.",
            "**Section 31 Specific Relief Act, 1963**: Suit for **Cancellation of a Void Instrument** (adjudging the fraudulent sale deed void and ordering it to be delivered up and cancelled).",
            "**Section 34 Specific Relief Act, 1963**: Suit for **Declaration of Title** declaring the genuine owner's absolute ownership.",
            "**Section 82 & 83 Registration Act, 1908**: Severe criminal penalty for false statements, delivering false copies, and personation before the Sub-Registrar.",
            "**Order XXXIX Rules 1 & 2 CPC**: Interim Injunction restraining fraudsters from selling, mutating, or entering the land.",
        ],
        "evidence_required": [
            "Certified copy of your genuine prior registered Title Deed / Parent deeds.",
            "Certified copy of the fraudulent / forged Sale Deed obtained from the Sub-Registrar.",
            "Admitted standard signatures of the true owner for forensic comparison.",
            "Forensic Handwriting & Fingerprint Expert Examination Report.",
            "Revenue Encumbrance Certificate (EC) showing fraudulent transaction entries.",
            "Police complaint / FIR under Section 467 IPC.",
        ],
        "action_plan_advocate": (
            "1. **Civil Cancellation & Declaration Suit**: Institute suit under Sections 31 & 34 Specific Relief Act with Order 39 interim status quo injunction.\n"
            "2. **Criminal FIR under Section 467/471 IPC**: Lodge formal complaint before Police / Magistrate under Section 156(3) CrPC for forgery of valuable security.\n"
            "3. **Sub-Registrar & Revenue Protest**: Submit written representation to District Registrar and Tehsildar putting the property on the 'Prohibited / Caution Register'.\n"
            "4. **Forensic Handwriting Comparison**: Move court application under Section 45 Evidence Act / Section 39 BSA to send signatures to Central Forensic Science Laboratory (CFSL)."
        ),
        "action_plan_client": (
            "1. **Apply for Certified Copies Immediately**: Go to the Sub-Registrar office or state land portal and download certified copies of the fraudulent deed.\n"
            "2. **Check Encumbrance Certificate (EC)**: Pull the 30-year EC to verify what fraudulent mortgages or transfers have been registered.\n"
            "3. **Maintain Physical Possession**: Do not let fraudsters take possession; erect signboards stating title ownership and warning trespassers.\n"
            "4. **Lodge Police Complaint**: File criminal complaint immediately; Section 467 IPC carries severe non-bailable penalties."
        ),
        "landmarks": [
            "***Satya Pal Anand v. State of M.P.* (2016) 10 SCC 767**: Clarified remedies against fraudulent registration and jurisdiction of civil court vs registrar.",
            "***Suraj Lamp & Industries v. State of Haryana* (2012) 1 SCC 656**: Held that transfer of immovable property cannot take place via GPA/Agreement to Sell; only registered conveyance deeds transfer title.",
        ],
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 467 (Forgery of Valuable Security - Life Imprisonment)",
            "[Statute] Bharatiya Nyaya Sanhita, 2023 - Section 338 (Forgery of Valuable Security)",
            "[Statute] Specific Relief Act, 1963 - Section 31 (Cancellation of Instruments) & Section 34 (Declaration)",
            "[Landmark Precedent] Suraj Lamp & Industries v. State of Haryana (2012) 1 SCC 656",
        ],
        "canonical_expansion": "forged property document fake sale deed forged signature Section 467 IPC Section 338 BNS Section 31 Specific Relief Act cancellation Suraj Lamp",
    },

    # 21. Right to Information (RTI) Inaction & Delayed Public Services
    {
        "domain": "rti_inaction_pio_penalty",
        "title": "Right to Information (RTI) Inaction, Refusal & Mandatory PIO Penalties",
        "triggers": [
            r"\b(?:rti|right\s+to\s+information|rti\s+application|rti\s+appeal|pio|cpio|public\s+information\s+officer)\b",
            r"\b(?:failed\s+to\s+provide|not\s+provid\w*|refus\w*|denied|withheld|no\s+reply|not\s+replied|delayed).*(?:information|records|reply|response)\b|\b(?:30\s+days|after\s+30\s+days|48\s+hours|penalty|first\s+appeal|second\s+appeal|sic|cic)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Citizen / RTI Applicant is legally in the right.**\n"
            "Under the **Right to Information Act, 2005**, every citizen has a fundamental legal right to access public records from public authorities. "
            "The Public Information Officer (PIO) is under a mandatory statutory duty to supply information within **30 DAYS** (or **48 HOURS** if concerning life or liberty). "
            "Refusing or delaying without lawful cause attracts a mandatory personal penalty of **₹250 per day up to ₹25,000** on the PIO."
        ),
        "supporting_sections": [
            "**Section 6 RTI Act, 2005**: Request for obtaining information without giving reasons.",
            "**Section 7(1) RTI Act**: Mandatory timeline: Information MUST be provided within **30 days**; if concerning life or liberty of a person, within **48 hours**.",
            "**Section 7(2) RTI Act**: Deemed Refusal: Failure to give decision within 30 days is deemed a refusal, and information must be provided **FREE OF COST** under Section 7(6).",
            "**Section 19(1) RTI Act**: **First Appeal**: Appeal before the First Appellate Authority (FAA) within 30 days of expiry of 30-day timeline.",
            "**Section 19(3) RTI Act**: **Second Appeal**: Appeal before the **Central Information Commission (CIC)** or **State Information Commission (SIC)** within 90 days.",
            "**Section 20(1) RTI Act**: **Mandatory Penalty on PIO**: Commission shall impose penalty of **₹250 per day** up to maximum of **₹25,000** directly payable from the PIO's personal salary.",
            "**Section 20(2) RTI Act**: Disciplinary action recommended against defaulting PIO under service rules.",
        ],
        "evidence_required": [
            "Copy of the original RTI Application with registration/tracking number.",
            "Proof of payment of RTI application fee (IPO, demand draft, online payment receipt).",
            "Speed Post receipt and online delivery tracking showing delivery to the PIO.",
            "Calendar computation proving expiry of 30 days without response.",
        ],
        "action_plan_advocate": (
            "1. **Draft First Appeal (Section 19(1) RTI Act)**: File First Appeal before First Appellate Authority praying for: (a) deemed refusal declaration, (b) free supply of information under Section 7(6), and (c) notice to PIO.\n"
            "2. **Second Appeal to Commission (Section 19(3))**: If FAA fails to decide within 30-45 days, file Second Appeal before State/Central Information Commission.\n"
            "3. **Prayer for Section 20 Penalties & Compensation**: Specifically plead for imposition of maximum penalty of ₹25,000 and compensation under Section 19(8)(b) for loss/detriment."
        ),
        "action_plan_client": (
            "1. **Count 30 Days from Delivery**: The clock begins on the date the PIO receives your letter, not the posting date.\n"
            "2. **File Online First Appeal**: If filed on **rtionline.gov.in**, you can click 'File First Appeal' directly using your RTI registration number for free.\n"
            "3. **Claim Free Records**: Since 30 days lapsed, you cannot be charged photocopy fees; demand information completely free of charge under Section 7(6).\n"
            "4. **Highlight Public Interest**: State that information pertains to governance transparency and falls outside the Section 8 exemptions."
        ),
        "landmarks": [
            "***CBSE v. Aditya Bandopadhyay* (2011) 8 SCC 497**: Supreme Court affirmed the citizen's right to information and fiduciary limits.",
            "***Reserve Bank of India v. Jayantilal N. Mistry* (2016) 3 SCC 525**: RBI held accountable to disclose audit and inspection reports of defaulting banks under RTI.",
        ],
        "citations": [
            "[Statute] Right to Information Act, 2005 (Sections 6, 7, 19, 20)",
            "[Portal] Central RTI Online Portal (rtionline.gov.in) & State RTI Portals",
            "[Landmark SC] CBSE v. Aditya Bandopadhyay (2011) & RBI v. Jayantilal N. Mistry (2016)",
        ],
        "canonical_expansion": "RTI Act 2005 Section 6 Section 7 30 days timeline 48 hours life liberty First Appeal Section 19 1 Second Appeal CIC SIC Section 20 penalty 25000",
    },

    # 22. Workplace Sexual Harassment (POSH Act, 2013)
    {
        "domain": "posh_workplace_harassment",
        "title": "Workplace Sexual Harassment & POSH Act Protections (Internal Committee Redressal)",
        "triggers": [
            r"\b(?:sexual\w*\s+harass\w*|posh|inappropriate\s+(?:touch|message|messages|text|behavior|conduct)|demanding\s+sexual\s+favor|sexually\s+coloured\s+remarks|unwelcome\s+advances)\b",
            r"\b(?:office|workplace|work|boss|manager|colleague|coworker|employer|company)\b",
            r"\b(?:internal\s+committee|icc|internal\s+complaints\s+committee|posh\s+complaint|local\s+committee)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Aggrieved Woman is legally in the right and comprehensively protected.**\n"
            "Under the **Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 (POSH Act)**, every woman has a fundamental right to a safe and dignified workplace free from sexual harassment. "
            "Every employer with 10 or more employees MUST constitute an **Internal Committee (IC)** headed by a senior woman. "
            "Sexual harassment at work is both a statutory violation and a cognizable criminal offence."
        ),
        "supporting_sections": [
            "**Section 2(n) & 3 POSH Act, 2013**: Definition of Sexual Harassment (physical contact, sexually coloured remarks, showing pornography, implied or explicit promise of preferential treatment or threat of detrimental treatment).",
            "**Section 4 POSH Act**: Mandatory constitution of Internal Committee (IC) with external NGO member and 50% women members.",
            "**Section 9 POSH Act**: Filing written complaint before the IC within **3 months** of the incident (extendable by another 3 months).",
            "**Section 12 POSH Act**: **Interim Relief**: Power of IC to recommend transfer of the complainant or respondent, or grant paid leave up to 3 months.",
            "**Section 11 & 13 POSH Act**: IC has same powers as a **Civil Court** under CPC to summon witnesses and examine under oath; must complete inquiry within **90 days**.",
            "**Section 16 POSH Act**: Strict prohibition on publication or disclosure of victim's identity (penalty on employer).",
            "**Section 354A IPC / Section 75 BNS**: Criminal punishment for sexual harassment (rigorous imprisonment up to 3 years and fine).",
        ],
        "evidence_required": [
            "WhatsApp chats, emails, Slack/Teams messages, or notes showing inappropriate remarks, requests, or advances.",
            "Witness names of colleagues who witnessed inappropriate behavior or to whom contemporaneous disclosure was made.",
            "Work performance records proving that retaliatory negative appraisals or threats were issued following refusal.",
            "Audio/video recordings or CCTV footage requests from the workplace.",
        ],
        "action_plan_advocate": (
            "1. **Submit Formal POSH Complaint**: Draft structured complaint to the Internal Committee (IC) detailing dates, locations, witnesses, and impact on working environment.\n"
            "2. **Prayer for Immediate Section 12 Interim Relief**: Pray for immediate reassignment of reporting manager, remote work option, or 3 months paid leave.\n"
            "3. **Police Complaint under Section 354A IPC**: File parallel criminal complaint at the local police station (civil POSH inquiry and criminal FIR run concurrently).\n"
            "4. **Challenge Biased IC**: If IC lacks external member or acts with bias, file writ petition in High Court or appeal under Section 18 POSH Act."
        ),
        "action_plan_client": (
            "1. **Write Detailed Diary**: Note down every incident immediately: date, exact words spoken, time, location, and who was nearby.\n"
            "2. **Do Not Delete Messages**: Keep raw digital files and take screenshots of Slack/WhatsApp messages with date headers visible.\n"
            "3. **Identify IC Presiding Officer**: Check company POSH policy portal for email of the Presiding Officer and External Member.\n"
            "4. **SHE-Box Portal**: You can also lodge a complaint on the Ministry of Women & Child Development **SHe-Box portal** (shebox.nic.in)."
        ),
        "landmarks": [
            "***Vishaka v. State of Rajasthan* (1997) 6 SCC 241**: Historic Supreme Court judgment formulating mandatory guidelines for workplace sexual harassment, subsequently codified into the POSH Act.",
            "***Aureliano Fernandes v. State of Goa* (2023) Supreme Court**: Directed strict pan-India implementation of the POSH Act, noting serious deficiencies in IC constitutions across institutions.",
        ],
        "citations": [
            "[Landmark SC] Vishaka v. State of Rajasthan (1997) 6 SCC 241 (Vishaka Guidelines)",
            "[Statute] POSH Act, 2013 (Act No. 14 of 2013) - Sections 4, 9, 12, 13",
            "[Statute] Indian Penal Code, 1860 - Section 354A (Sexual Harassment)",
            "[Portal] SHe-Box Portal - Ministry of Women & Child Development (shebox.nic.in)",
        ],
        "canonical_expansion": "POSH Act 2013 workplace sexual harassment Internal Committee Section 9 12 interim relief Vishaka guidelines Section 354A IPC Aureliano Fernandes SHe-Box",
    },

    # 23. Senior Citizen Abuse, Eviction of Abusive Son & Gift Revocation
    {
        "domain": "senior_citizen_abuse_eviction",
        "title": "Senior Citizen Protection, Eviction of Abusive Children & Property Gift Revocation",
        "triggers": [
            r"\b(elderly|senior\s+citizen|old\s+parents|aged\s+parents|elderly\s+father|elderly\s+mother|aged\s+mother|aged\s+father|parents)\b",
            r"\b(?:son|daughter|children|daughter-in-law|son-in-law).*(?:abus\w*|harass\w*|beat\w*|tortur\w*|starv\w*|neglect\w*|evict\w*|throw\w*|kicked\s+out|threat\w*|property)\b|\b(?:abus\w*|harass\w*|beat\w*|tortur\w*|starv\w*|neglect\w*|kicked\s+out|throw\w*\s+out).*(?:parents|father|mother|elderly|senior)\b",
            r"\b(?:revoke|cancel).*(?:gift|deed|transfer|property)\b|\b(?:evict|throw\s+out|remove).*(?:son|daughter|children|daughter-in-law)\b|\b(?:senior\s+citizens\s+act|maintenance\s+tribunal|sdm|welfare\s+of\s+parents)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Senior Citizens / Elderly Parents are legally in the right.**\n"
            "Under the **Maintenance and Welfare of Parents and Senior Citizens Act, 2007**, elderly parents have a paramount statutory right to live with dignity and peace in their self-acquired property. "
            "Children have **zero legal right to abuse, harass, or starve their parents**, or forcefully occupy their house. "
            "The Maintenance Tribunal (SDM) has summary powers to **evict abusive children** and **unilaterally declare any property transfer or gift deed VOID**."
        ),
        "supporting_sections": [
            "**Section 23 Senior Citizens Act, 2007**: **Revocation of Property Transfer**: Where a senior citizen transfers property by gift or otherwise subject to condition of care, and children fail to provide basic amenities, the transfer **SHALL BE DEEMED FRAUDULENT AND VOID** by the Tribunal.",
            "**Section 4 & 5 Senior Citizens Act**: Statutory maintenance allowance payable monthly by children/heirs to parents.",
            "**Summary Eviction Powers of Maintenance Tribunal (SDM)**: Power to order summary eviction of abusive children/relatives from parents' self-acquired property (*S. Vanitha v. Deputy Commissioner*).",
            "**Section 24 Senior Citizens Act**: Criminal punishment for exposure and abandonment of senior citizen (imprisonment up to 3 months or fine).",
            "**Section 125 CrPC / Section 144 BNSS**: Parallel right to claim monthly maintenance before Magistrate.",
        ],
        "evidence_required": [
            "Proof of age establishing applicant is 60+ years old (Aadhaar Card, Voter ID, Senior Citizen Card).",
            "Original Registered Gift Deed / Settlement Deed containing care condition or recital.",
            "Proof of ownership of the property (Sale deed, Khata/Patta, Municipal tax receipts in parents' name).",
            "Medical prescriptions, hospital bills showing age-related illnesses, or police complaints of harassment.",
        ],
        "action_plan_advocate": (
            "1. **Petition before Maintenance Tribunal (SDM)**: File petition under Sections 4 & 23 of the Senior Citizens Act before the Sub-Divisional Magistrate (SDM).\n"
            "2. **Prayer for Summary Eviction**: Pray for immediate eviction of the abusive son/daughter-in-law from the parents' self-acquired residence.\n"
            "3. **Prayer for Gift Deed Cancellation**: Pray to declare the gift deed void under Section 23 and direct the Sub-Registrar to record cancellation.\n"
            "4. **Police Protection Order**: Obtain an interim order directing local SHO to provide physical safety and prevent children from entering the house."
        ),
        "action_plan_client": (
            "1. **You Are the Master of Your House**: Children have no inherent right to live in your self-acquired property; you can legally evict them at any time.\n"
            "2. **Dial Elder Helpline 14567**: Call the **National Helpline for Senior Citizens (14567)**; they provide direct legal aid and police intervention.\n"
            "3. **File Petition with Local SDM**: You do not need heavy legal fees; an application on plain paper to the Sub-Divisional Magistrate (SDM) Tribunal triggers fast-track hearings.\n"
            "4. **Revoke the Gift Deed**: If you gifted the house to your child on the promise of care and they mistreat you, the SDM can cancel the gift deed."
        ),
        "landmarks": [
            "***S. Vanitha v. Deputy Commissioner* (2021) 15 SCC 730 (Supreme Court)**: Affirmed that the Senior Citizens Act overrides other laws to protect elderly parents; Maintenance Tribunal has jurisdiction to order eviction of children.",
            "***Sunny Paul v. State of NCT of Delhi* (2018) Delhi High Court**: Confirmed that SDM Tribunal has plenary powers to evict abusive son and daughter-in-law from self-acquired house of parents.",
        ],
        "citations": [
            "[Landmark SC] S. Vanitha v. Deputy Commissioner (2021) 15 SCC 730",
            "[Statute] Maintenance and Welfare of Parents and Senior Citizens Act, 2007 (Sections 4, 5, 23)",
            "[Landmark HC] Sunny Paul v. State of NCT of Delhi (2018) (Eviction of Children)",
            "[Helpline] National Helpline for Senior Citizens (14567)",
        ],
        "canonical_expansion": "Senior Citizens Act 2007 Section 23 cancel gift deed revoke property transfer evict abusive son daughter S Vanitha Sunny Paul SDM Tribunal 14567 helpline",
    },

    # 24. Extortion, Gang Protection Money & Criminal Threats
    {
        "domain": "extortion_threat_protection_money",
        "title": "Extortion, Gang Protection Money (Hafta) & Threat to Life",
        "triggers": [
            r"\b(extortion|hafta|protection money|rangdari|gangster|goon|mafia|extort)\b",
            r"\b(threatening to kill|threat to kill|pay money or die|ransom demand|threatening calls|parcha)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Victim is in the right and entitled to state protection.**\n"
            "Extortion, demanding protection money, and threatening death or grievous hurt are **heinous, non-bailable criminal offences** under the Indian Penal Code and Bharatiya Nyaya Sanhita. "
            "The state police is mandated to provide immediate protection and initiate organized crime prosecution."
        ),
        "supporting_sections": [
            "**Section 383 & 384 IPC / Section 308 BNS**: Definition and punishment for Extortion (imprisonment up to 3 years and fine).",
            "**Section 386 IPC / Section 308(4) BNS**: **Extortion by putting person in fear of death or grievous hurt** — **Imprisonment up to 10 years and Fine** (**Cognizable & Non-Bailable**).",
            "**Section 387 IPC / Section 308(5) BNS**: Putting person in fear of death or grievous hurt in order to commit extortion.",
            "**Section 503 & 506 Part II IPC / Section 351 BNS**: Criminal Intimidation with threat to cause death — imprisonment up to 7 years.",
            "**Section 111 BNS 2023 (Organized Crime)**: Severe organized crime penalties (death or life imprisonment and min ₹5 lakh fine).",
            "**Witness Protection Scheme, 2018**: Statutory witness protection (identity concealment, police escort, relocation).",
        ],
        "evidence_required": [
            "Audio recordings of extortion calls and threatening voice notes.",
            "Screenshots of WhatsApp/SMS messages demanding cash, UPI, or crypto transfers.",
            "Call Detail Records (CDR) and timestamps of incoming threatening numbers.",
            "CCTV footage of any physical visits by extortionists to home/workplace.",
        ],
        "action_plan_advocate": (
            "1. **Emergency FIR under Section 386/506 IPC**: Lodge FIR directly with the Anti-Extortion Cell / Special Cell / Crime Branch.\n"
            "2. **Police Protection Application**: Move formal application under the Witness Protection Scheme 2018 before the Competent Authority (District Judge) for 24x7 armed police guard.\n"
            "3. **High Court Writ for Protection**: If local police drag feet, move the High Court under Article 226 seeking an urgent writ directing the Commissioner of Police to ensure security."
        ),
        "action_plan_client": (
            "1. **NEVER PAY PROTECTION MONEY**: Paying once ensures you will be extorted repeatedly. Refuse calmly and contact police.\n"
            "2. **Record Every Call**: Enable automatic call recording on your phone for all unknown numbers.\n"
            "3. **Dial 112 Immediately**: Inform police emergency 112 with exact caller phone numbers.\n"
            "4. **Approach Senior Officers**: Go directly to the Superintendent of Police (SP) or Commissioner of Police (CP) if the local police station is hesitant."
        ),
        "landmarks": [
            "***Mahender Chawla v. Union of India* (2019) 14 SCC 615**: Supreme Court endorsed and enforced the **Witness Protection Scheme, 2018** as binding law under Article 141.",
            "***Dhananjay v. State of Bihar* (2007) 1 SCC 768**: Ingredients of extortion under Section 383 IPC.",
        ],
        "citations": [
            "[Statute] Indian Penal Code, 1860 - Section 386 (Extortion with threat of death - Non-Bailable)",
            "[Statute] Bharatiya Nyaya Sanhita, 2023 - Section 308 & Section 111 (Organized Crime)",
            "[Landmark SC] Mahender Chawla v. Union of India (2019) (Witness Protection Scheme)",
            "[Emergency] National Police Helpline (112)",
        ],
        "canonical_expansion": "extortion hafta protection money Section 386 IPC Section 308 BNS threat to kill Section 506 Witness Protection Scheme Mahender Chawla 112 police",
    },

    # 25. Illegal Arrest, Police Custody & Custodial Torture
    {
        "domain": "illegal_arrest_custodial_violence",
        "title": "Illegal Police Arrest, Unlawful Custody & Custodial Torture (D.K. Basu Guidelines)",
        "triggers": [
            r"\b(?:illegal\s+arrest|arrested\s+without|police\s+detain\w*|police\s+arrest\w*|police\s+beat\w*|custodial\s+torture|custodial\s+violence|custodial\s+death|illegal\s+detention|beaten\s+in\s+(?:police|thana|lockup))\b",
            r"\b(?:24\s+hours|two\s+days|3\s+days|not\s+produced|without\s+warrant|without\s+memo|without\s+producing).*(?:magistrate|judge|court|lockup|custody)\b|\b(?:lockup|police\s+custody|custodial\s+death|torture\s+in\s+custody)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Detainee / Citizen is legally in the right.**\n"
            "Under the Constitution of India (Article 21 and 22), arbitrary arrest and custodial violence are gross violations of fundamental rights. "
            "Every arrested person MUST be produced before the nearest Judicial Magistrate within **24 HOURS** (excluding travel time). "
            "Detention beyond 24 hours without magisterial remand is **illegal and unconstitutional**, rendering the police officers liable for abduction, wrongful confinement, and contempt of court."
        ),
        "supporting_sections": [
            "**Article 22(2) Constitution of India & Section 57 CrPC / Section 58 BNSS**: Mandatory production before nearest Magistrate within **24 HOURS**.",
            "**Section 41 & 41A CrPC / Section 35 BNSS**: For offences punishable up to 7 years, arrest is NOT routine; police MUST issue a Notice of Appearance under *Arnesh Kumar*.",
            "**Section 41B CrPC / Section 36 BNSS**: Mandatory preparation of **Arrest Memo** countersigned by a family member or respectable citizen of the locality.",
            "**Section 41D CrPC / Section 38 BNSS**: Statutory right of the arrested person to consult an advocate of their choice during interrogation.",
            "**Section 54 CrPC / Section 53 BNSS**: Mandatory medical examination of the arrested person by a medical officer.",
            "**Section 330 & 331 IPC / Section 120 BNS**: Voluntarily causing hurt or grievous hurt to extort confession (up to 7 to 10 years imprisonment).",
            "**Section 342 IPC / Section 127 BNS**: Wrongful confinement.",
            "**Article 226 / Article 32 Constitution**: **Writ of Habeas Corpus** to produce the illegally detained person in court immediately.",
        ],
        "evidence_required": [
            "Timestamp of when police picked up the person (CCTV footage, neighbor testimonies, PCR call records).",
            "Written complaint sent to SP / Magistrate recording missing person / illegal detention.",
            "General Diary (GD) records and lockup register of the concerned police station.",
            "Medical examination report showing fresh custodial injuries.",
        ],
        "action_plan_advocate": (
            "1. **Emergency Writ of Habeas Corpus (Article 226)**: Move urgent Writ of Habeas Corpus before the High Court roster bench praying for search warrant and production of detainee.\n"
            "2. **Emergency Application before Duty Magistrate**: File application under Section 97 CrPC (Search for person wrongfully confined) before the Chief Judicial Magistrate / Duty Magistrate.\n"
            "3. **Independent Medical Examination**: Move application before the Magistrate to direct immediate examination by a medical board at a government hospital to document torture marks.\n"
            "4. **Contempt Petition (*Arnesh Kumar* / *D.K. Basu*)**: Initiate contempt proceedings against the Investigating Officer in High Court."
        ),
        "action_plan_client": (
            "1. **Demand Arrest Memo**: Insist on receiving a signed copy of the Arrest Memo specifying reasons, date, time, and custody location.\n"
            "2. **Inform Family & Call 112**: Police MUST notify a family member within 8 to 12 hours under D.K. Basu guidelines; dial 112 to record distress call.\n"
            "3. **Tell the Magistrate Directly**: When produced before the Magistrate, tell the Judge immediately if you were beaten or detained past 24 hours; the Magistrate is legally bound to order a medical checkup.\n"
            "4. **National Human Rights Commission (NHRC)**: File an online complaint on **nhrc.nic.in** for custodial torture."
        ),
        "landmarks": [
            "***D.K. Basu v. State of West Bengal* (1997) 1 SCC 416**: Supreme Court laid down 11 mandatory procedural safeguards for arrest and detention to prevent custodial violence.",
            "***Arnesh Kumar v. State of Bihar* (2014) 8 SCC 273**: Arrest is strictly forbidden without complying with Section 41A CrPC checklist for offences up to 7 years.",
        ],
        "citations": [
            "[Landmark SC] D.K. Basu v. State of West Bengal (1997) 1 SCC 416 (Arrest Guidelines)",
            "[Landmark SC] Arnesh Kumar v. State of Bihar (2014) 8 SCC 273 (Arrest Checklist)",
            "[Constitutional Law] Constitution of India - Article 21 & Article 22(2) (24-Hour Rule)",
            "[Statute] Code of Criminal Procedure, 1973 - Section 41A, 54, 57",
        ],
        "canonical_expansion": "illegal arrest custodial torture 24 hours magistrate Section 57 CrPC Section 58 BNSS Article 22 2 DK Basu Arnesh Kumar habeas corpus Section 41A",
    },

    # 26. Neighbour Nuisance, Noise Pollution & Illegal Society Construction
    {
        "domain": "neighbour_nuisance_illegal_construction",
        "title": "Neighbour Nuisance, Noise Pollution & Illegal Society Construction",
        "triggers": [
            r"\b(?:neighbour|neighbor|next\s+door|society\s+member|flat\s+above|flat\s+below)\b",
            r"\b(?:loud|noise|sound|vibration|generator|music|barking|garbage|leakage|water\s+leak|blocked\s+passage|illegal\s+construction|encroach\w*).*(?:noise|sound|music|vibration|generator|corridor|passage|terrace|common\s+area|nuisance)\b|\b(?:noise\s+pollution|loud\s+music|throwing\s+garbage|public\s+nuisance)\b",
            r"\b(?:public\s+nuisance|nuisance|housing\s+society|rwa|sdm|133\s+crpc|152\s+bnss)\b",
        ],
        "min_trigger_matches": 2,
        "who_is_right": (
            "**The Aggrieved Resident / Lawful Occupant is in the right.**\n"
            "Under Indian Law, every resident has a right to peaceful enjoyment of their home and clean environment under Article 21. "
            "No neighbour has the legal right to create a continuous public nuisance, blast loud music beyond prescribed decibel limits after 10 PM, or carry out unauthorized construction obstructing common areas."
        ),
        "supporting_sections": [
            "**Section 133 CrPC / Section 152 BNSS**: **Conditional Order for Removal of Nuisance**: Summary magisterial remedy where the Sub-Divisional Magistrate (SDM) can direct immediate removal of public nuisance or demolition of illegal obstructions.",
            "**Noise Pollution (Regulation and Control) Rules, 2000**: Complete ban on loud speakers / public address systems between **10:00 PM and 6:00 AM**; ambient noise levels must not exceed 55 dB (day) and 45 dB (night) in residential zones.",
            "**Section 268 & 290 IPC / Section 270 BNS**: Public Nuisance punishable with fine.",
            "**Civil Suit for Perpetual Injunction (Section 38 Specific Relief Act)**: Civil Court injunction restraining neighbour from causing nuisance or encroaching on common areas.",
            "**State Apartment Ownership Act / RWA Byelaws**: Sanctions and municipal demolition notices for unauthorized alterations to common areas or load-bearing columns.",
        ],
        "evidence_required": [
            "Decibel meter readings / smartphone sound level app screenshots showing sound levels exceeding 55 dB.",
            "Video recordings with clear audio timestamps of the nuisance, loud music, or garbage dumping.",
            "Written complaints sent to the Housing Society / RWA Managing Committee with acknowledgment.",
            "Police emergency PCR call records (112 call timestamps).",
            "Photographs of unauthorized construction in common passages or shafts.",
        ],
        "action_plan_advocate": (
            "1. **Magisterial Petition under Section 133 CrPC / Section 152 BNSS**: File application before the Sub-Divisional Magistrate (SDM) seeking conditional order to stop the nuisance immediately.\n"
            "2. **Civil Injunction Suit (Order 39 CPC)**: File suit for perpetual injunction with interim application to seal unauthorized construction and restrain noise.\n"
            "3. **Municipal Notice**: Issue notice to Municipal Corporation building department under Municipal Act to inspect and demolish unauthorized structural deviations."
        ),
        "action_plan_client": (
            "1. **Dial 112 After 10 PM**: Noise rules strictly prohibit loud music after 10 PM; call 112 every time and note the PCR dispatch number.\n"
            "2. **File Written Complaint to RWA**: Submit written complaint to the society President/Secretary demanding fine under society byelaws.\n"
            "3. **Collect Decibel Evidence**: Download the 'Sound Meter' app and record videos showing the decibel level inside your bedroom.\n"
            "4. **Approach SDM**: If neighbour refuses to cooperate, approach the local Sub-Divisional Magistrate (SDM) under Section 133 CrPC."
        ),
        "landmarks": [
            "***In Re: Noise Pollution* (2005) 5 SCC 733**: Supreme Court held that freedom from noise pollution is part of Article 21; established strict ban on loudspeakers between 10 PM and 6 AM.",
            "***Church of God (Full Gospel) in India v. K.K.R. Majestic Colony Welfare Assn* (2000) 7 SCC 282**: Supreme Court held that no religion or person prescribes that prayers or celebrations should be performed by disturbing the peace of neighbours.",
        ],
        "citations": [
            "[Landmark SC] In Re: Noise Pollution (2005) 5 SCC 733 (10 PM to 6 AM Ban)",
            "[Statute] Code of Criminal Procedure, 1973 - Section 133 (Removal of Public Nuisance)",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 152",
            "[Statute] Noise Pollution (Regulation and Control) Rules, 2000",
        ],
        "canonical_expansion": "neighbour nuisance noise pollution loud music 10 PM Section 133 CrPC Section 152 BNSS SDM Order 39 CPC injunction RWA byelaws In Re Noise Pollution",
    },

    # 27. Dowry Death (Section 304B IPC / Section 80 BNS)
    {
        "domain": "dowry_death_unnatural",
        "title": "Dowry Death & Unnatural Death of Bride within 7 Years (Section 304B IPC)",
        "triggers": [
            r"\b(?:dowry\s+death|bride\s+died|wife\s+died|woman\s+died|daughter\s+died|unnatural\s+death|died\s+in\s+in-laws\s+house)\b",
            r"\b(?:within\s+\d+\s+years\s+of\s+marriage|burnt|burn\s+injuries|poison\w*|hung|strangled|hanged|suicide|hanging)\b",
            r"\b(?:dowry\s+harassment|dowry\s+demand|gold\s+demand|money\s+demand|harassment)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Parents / Family of the Deceased Victim are legally in the right.**\n"
            "Under Indian Law, where the death of a woman is caused by burns, bodily injury, or occurs under abnormal circumstances within **7 YEARS OF HER MARRIAGE**, "
            "and it is shown that soon before her death she was subjected to cruelty or harassment for dowry, it is classified as **DOWRY DEATH**. "
            "The law applies a mandatory **statutory presumption of guilt against the husband and in-laws**."
        ),
        "supporting_sections": [
            "**Section 304B IPC / Section 80 BNS (Dowry Death)**: Punishment of imprisonment for **NOT LESS THAN 7 YEARS** which may extend to **IMPRISONMENT FOR LIFE** (**Cognizable & Non-Bailable, Triable by Court of Session**).",
            "**Section 113B Indian Evidence Act / Section 118 BSA**: **Mandatory Statutory Presumption**: When the question is whether a person committed dowry death and it is shown that soon before death she was subjected to dowry cruelty, the Court **SHALL PRESUME** that such person caused the dowry death.",
            "**Section 498A IPC / Section 85 BNS**: Cruelty by husband and in-laws.",
            "**Section 302 IPC / Section 103(1) BNS**: Murder charge added where forensic evidence indicates homicide / strangulation / poisoning.",
            "**Section 174 & 176 CrPC / Section 194 & 196 BNSS**: Mandatory **Executive Magisterial Inquest (SDM Inquest)** for any woman dying within 7 years of marriage.",
        ],
        "evidence_required": [
            "Marriage certificate / invitation showing date of marriage (proving death occurred within 7 years).",
            "Post-Mortem Report (PMR) detailing cause of death, ligature marks, burns, or visceral chemical analysis.",
            "Statements recorded before the Sub-Divisional Magistrate (SDM) during Inquest proceedings.",
            "WhatsApp chats, text messages, or diary entries showing dowry harassment 'soon before death'.",
            "List of dowry articles and bank transaction receipts given to husband/in-laws.",
        ],
        "action_plan_advocate": (
            "1. **Magisterial Inquest Presence**: Ensure parents and family record comprehensive statements directly before the Sub-Divisional Magistrate (SDM) under Section 176 CrPC.\n"
            "2. **Registration of FIR under Section 304B & 302 IPC**: Ensure the FIR charges both Section 304B and Section 302 IPC, invoking the Section 113B statutory presumption.\n"
            "3. **Oppose Bail**: Rigorously oppose bail applications of husband and in-laws citing Category C/D parameters in *Satender Kumar Antil* and statutory presumption under Section 113B.\n"
            "4. **Preserve Viscera & PMR**: Direct application to CFSL/FSL for expedited viscera and forensic chemical analysis."
        ),
        "action_plan_client": (
            "1. **Demand SDM Inquest**: By law, an Executive Magistrate (SDM) MUST conduct the inquest when a bride dies within 7 years; do not let local police conduct a routine inquest.\n"
            "2. **State Truth to the SDM**: Give a detailed statement to the SDM mentioning all previous dowry demands, beaten incidents, and phone calls.\n"
            "3. **Preserve Phone Records**: Keep the deceased daughter's phone, WhatsApp messages, and call recordings safe as vital forensic proof.\n"
            "4. **Demand Video Recording of Post-Mortem**: Request the hospital to conduct post-mortem by a panel of two doctors with video recording."
        ),
        "landmarks": [
            "***Satbir Singh v. State of Haryana* (2021) 6 SCC 1**: Supreme Court laid down detailed guidelines for trial of offences under Section 304B IPC; held that 'soon before death' does not mean immediately before, but implies a proximate and live link.",
            "***Sher Singh v. State of Haryana* (2015) 3 SCC 724**: Clarified the operation of statutory presumption under Section 113B Evidence Act.",
        ],
        "citations": [
            "[Landmark SC] Satbir Singh v. State of Haryana (2021) 6 SCC 1 (Dowry Death Guidelines)",
            "[Statute] Indian Penal Code, 1860 - Section 304B (Minimum 7 Years to Life Imprisonment)",
            "[Statute] Bharatiya Nyaya Sanhita, 2023 - Section 80 (Dowry Death)",
            "[Evidence Law] Indian Evidence Act, 1872 - Section 113B (Mandatory Presumption of Guilt)",
        ],
        "canonical_expansion": "dowry death Section 304B IPC Section 80 BNS 7 years of marriage Section 113B Evidence Act presumption soon before death SDM inquest Section 176 CrPC Satbir Singh",
    },

    # 28. Kidnapping & Abduction of Minor
    {
        "domain": "kidnapping_abduction_ransom",
        "title": "Kidnapping, Abduction & Kidnapping for Ransom (Section 364A IPC)",
        "triggers": [
            r"\b(kidnap|kidnapped|kidnapping|abduct|abducted|abduction)\b",
            r"\b(minor child|taken away|school kid|child missing|without parents consent)\b",
            r"\b(ransom|ransom money|demanding ransom|hostage)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Parents / Guardians of the Minor are legally in the right.**\n"
            "Taking or enticing away any minor (under 16 years for males, under 18 years for females) out of the keeping of lawful guardianship without consent is **KIDNAPPING**. "
            "Kidnapping a child for **Ransom** or threatening death is one of the gravest capital offences under Indian Law, punishable with **DEATH or LIFE IMPRISONMENT**."
        ),
        "supporting_sections": [
            "**Section 359 & 361 IPC / Section 137 BNS**: Kidnapping from Lawful Guardianship (taking minor under 16 male / 18 female without guardian's consent).",
            "**Section 363 IPC / Section 137(2) BNS**: Punishment for kidnapping (imprisonment up to 7 years and fine).",
            "**Section 364A IPC / Section 140 BNS**: **Kidnapping for Ransom**: Kidnapping and threatening to cause death/hurt to compel payment of ransom — **Punishable with DEATH or IMPRISONMENT FOR LIFE** (**Non-Bailable**).",
            "**Section 363A IPC / Section 139 BNS**: Kidnapping or maiming minor for purposes of begging (up to 10 years / life imprisonment).",
            "**Supreme Court Bachpan Bachao Andolan Directives**: Every missing child report MUST be registered as an FIR of Kidnapping immediately.",
        ],
        "evidence_required": [
            "Birth Certificate / School Certificate proving child is a minor (under 18 years).",
            "Audio recordings, WhatsApp messages, or letters demanding ransom.",
            "CCTV footage from last known location or transit points.",
            "Photographs and physical identification marks of the child.",
        ],
        "action_plan_advocate": (
            "1. **Immediate Section 364A FIR**: Ensure police register FIR under Section 364A IPC / Section 140 BNS immediately.\n"
            "2. **Anti-Human Trafficking Unit (AHTU)**: Involve the specialized Crime Branch / Anti-Human Trafficking Unit and Cyber Cell for cell tower triangulation.\n"
            "3. **Habeas Corpus Writ**: If police show negligence, move High Court under Article 226 for immediate directions to trace child."
        ),
        "action_plan_client": (
            "1. **Dial 112 & Childline 1098 Immediately**: Inform Police (112) and National Childline (**1098**) without delay.\n"
            "2. **Mandatory FIR**: By Supreme Court order, police CANNOT treat a missing child as a missing entry; they MUST register a **Kidnapping FIR** immediately.\n"
            "3. **Do Not Delete Ransom Calls**: Keep recording all calls and provide numbers to police for electronic tracking.\n"
            "4. **Track via TrackChild Portal**: Register details on the Govt. of India **TrackChild portal** (trackchild.gov.in)."
        ),
        "landmarks": [
            "***Bachpan Bachao Andolan v. Union of India* (2013) Supreme Court**: Mandated that upon receiving information of a missing child, police MUST register an FIR of Kidnapping under Section 363 IPC and deploy a Special Juvenile Police Unit (SJPU).",
            "***Vikram Singh v. Union of India* (2015) 9 SCC 502**: Upheld the constitutional validity of capital punishment under Section 364A IPC for kidnapping for ransom.",
        ],
        "citations": [
            "[Landmark SC] Bachpan Bachao Andolan v. Union of India (2013) (Mandatory Kidnapping FIR)",
            "[Statute] Indian Penal Code, 1860 - Section 361 (Kidnapping) & Section 364A (Ransom - Capital Punishment)",
            "[Statute] Bharatiya Nyaya Sanhita, 2023 - Section 137 & Section 140",
            "[Emergency] Childline India Helpline (1098) & Police Emergency (112)",
        ],
        "canonical_expansion": "kidnapping abduction ransom Section 364A IPC Section 140 BNS Section 361 minor child missing Bachpan Bachao Andolan 1098 Childline trackchild",
    },

    # 29. Hit-and-Run & Drunk Driving
    {
        "domain": "hit_and_run_drunk_driving",
        "title": "Hit-and-Run Accidents, Fleeing the Scene & Drunk Driving",
        "triggers": [
            r"\b(hit and run|fled the scene|sped away|ran away after hitting|car fled|driver fled)\b",
            r"\b(drunk driver|drunk driving|alcohol driving|intoxicated driver|hit pedestrian)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Victim / Injured / Bereaved Family is legally in the right.**\n"
            "Fleeing the scene of a road accident without rendering medical aid or reporting to the police is a grave statutory offence. "
            "Under the modern **Bharatiya Nyaya Sanhita (BNS 2023)**, Section 106(2) prescribes up to **10 YEARS IMPRISONMENT** for hit-and-run drivers who fail to report to police. "
            "Drunk driving is strictly penalized under Section 185 of the Motor Vehicles Act."
        ),
        "supporting_sections": [
            "**Section 106(2) BNS 2023 (Hit & Run)**: Causing death by rash/negligent driving and escaping without reporting to police officer or Magistrate soon after incident — imprisonment up to **10 YEARS and Fine**.",
            "**Section 279 & 304A IPC / Section 281 & 106(1) BNS**: Rash driving on public way and causing death by negligence.",
            "**Section 185 Motor Vehicles Act, 1988 (Drunk Driving)**: Driving with alcohol exceeding 30 mg per 100 ml of blood — imprisonment up to 6 months and suspension of license (2 years for second offence).",
            "**Section 134 Motor Vehicles Act**: Duty of driver in case of accident to secure medical attention for injured person and report to police within 24 hours.",
            "**Solatium Scheme 2022 (Govt. of India)**: Enhanced statutory compensation for hit-and-run victims: **₹2,00,000 for death** and **₹50,000 for grievous injury** payable by government even if vehicle is untraced.",
            "**Section 166 Motor Vehicles Act**: Comprehensive compensation claim before MACT against owner and insurer once vehicle is identified.",
        ],
        "evidence_required": [
            "CCTV footage from traffic cameras, toll plazas, or nearby shops capturing the vehicle make and license plate.",
            "Certified copy of FIR under Section 279/304A IPC (or Section 281/106 BNS).",
            "Medico-Legal Certificate (MLC) and Post-Mortem Report.",
            "Debris from accident scene (broken headlamp glass, paint scrapings) matching offending vehicle.",
        ],
        "action_plan_advocate": (
            "1. **CCTV Preservation Order**: Immediately file application under Section 91 CrPC / Section 94 BNSS directing police and traffic authorities to preserve CCTV footage of traffic intersections.\n"
            "2. **Detailed Accident Report (DAR / e-DAR)**: Ensure compliance with Section 159 MV Act where police must submit e-DAR within 90 days to Claims Tribunal.\n"
            "3. **Solatium Scheme Claim**: File application before District Magistrate (Inquiry Officer) for immediate statutory Solatium compensation.\n"
            "4. **MACT Claim Petition**: Institute Section 166 petition for full dependency compensation under *Sarla Verma* multiplier."
        ),
        "action_plan_client": (
            "1. **Get Immediate Medical Attention**: Save life first; hospital emergency staff will automatically prepare the Medico-Legal Certificate (MLC).\n"
            "2. **Note Vehicle Clues**: Note vehicle color, make (SUV, sedan, truck), last four digits of license plate, or direction of flight.\n"
            "3. **Claim Hit-and-Run Solatium Fund**: If vehicle is unknown, apply to the District Collector / Sub-Divisional Officer for ₹2 Lakh death / ₹50,000 grievous injury compensation under the 2022 Scheme.\n"
            "4. **Preserve Damaged Vehicle**: Do not repair the victim's damaged bike/car until the Motor Vehicle Inspector (MVI) conducts mechanical inspection."
        ),
        "landmarks": [
            "***State of Punjab v. Saurabh Bakshi* (2015) 5 SCC 738**: Supreme Court held that professional drivers committing fatal road accidents cannot be let off lightly with mere fine.",
            "***Sarla Verma v. DTC* (2009) 6 SCC 121**: Binding standard formula for computing compensation in fatal motor accidents.",
        ],
        "citations": [
            "[Statute] Bharatiya Nyaya Sanhita, 2023 - Section 106(2) (Hit-and-Run 10-Year Imprisonment)",
            "[Statute] Motor Vehicles Act, 1988 - Section 185 (Drunk Driving) & Section 166 (Compensation)",
            "[Government Scheme] Compensation to Victims of Hit and Run Motor Accidents Scheme, 2022",
            "[Landmark SC] Sarla Verma v. DTC (2009) 6 SCC 121",
        ],
        "canonical_expansion": "hit and run Section 106 2 BNS 10 years imprisonment drunk driving Section 185 MV Act Section 134 Sarla Verma Solatium Scheme 2 lakhs MACT compensation",
    },

    # 30. Cheque Bounce Defense (Accused Perspective)
    {
        "domain": "cheque_bounce_defense_accused",
        "title": "Cheque Bounce Defense: Misuse of Security Cheque & Rebuttal of Presumption (Section 139 NI Act)",
        "triggers": [
            r"\b(?:security\s+cheque|blank\s+cheque|cheque\s+misused|misused.*cheque|cheque.*given.*security|falsely\s+implicated.*138|false.*138|false\s+cheque\s+case)\b",
            r"\b(?:defen[cs]e.*(?:138|cheque)|accused.*(?:138|cheque)|(?:no\s+debt|never\s+borrowed|already\s+paid|already\s+repaid).*(?:cheque|138)|rebut.*presumption)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Accused has a strong, recognized legal defense under Supreme Court Precedents:**\n\n"
            "Under Indian Law, while Section 139 of the Negotiable Instruments Act creates a statutory presumption that a cheque was issued for discharge of debt, **this presumption is REBUTTABLE** on a **preponderance of probabilities**. "
            "A cheque issued merely as **Security / Collateral** for a transaction where no crystallised debt existed cannot be prosecuted under Section 138 if the underlying obligation was already fulfilled or never disbursed."
        ),
        "supporting_sections": [
            "**Section 139 Negotiable Instruments Act**: Presumption in favour of holder — Rebuttable by accused raising a probable defense (*Basalingappa v. Mudibasappa*).",
            "**Section 118 NI Act**: Presumption as to consideration — Rebuttable on preponderance of probabilities.",
            "**Section 138 NI Act Explanation**: Debt or other liability means **ONLY a legally enforceable debt or other liability**.",
            "**Section 143A NI Act**: Interim compensation (up to 20%) is **discretionary**, not mandatory (*Rakesh Ranjan Shrivastava v. State of Jharkhand*, 2024).",
            "**Section 313 CrPC / Section 351 BNSS**: Power of accused to explain circumstances and establish defense without stepping into witness box.",
        ],
        "evidence_required": [
            "Proof of underlying transaction (contract, receipts, account statement proving loan was never disbursed or was already repaid).",
            "Police complaint or bank stop-payment letter filed prior to presentation of cheque proving loss/misuse of security cheque.",
            "Complainant's Income Tax Returns (ITR) establishing complainant lacked financial capacity to advance the alleged cash loan.",
            "Handwriting mismatch evidence proving body of blank cheque was filled by someone else with inflated amounts.",
        ],
        "action_plan_advocate": (
            "1. **Reply to Statutory Demand Notice**: Send a comprehensive reply within 15 days of notice receipt detailing that the cheque was handed over solely as security and no legally enforceable debt exists.\n"
            "2. **Cross-Examination of Complainant**: Cross-examine complainant on: (a) source of funds/cash, (b) non-disclosure of alleged loan in Income Tax Returns, and (c) absence of written loan agreement.\n"
            "3. **Oppose Section 143A Interim Compensation**: Oppose application citing Supreme Court 2024 ruling in *Rakesh Ranjan Shrivastava* demonstrating prima facie frivolous complaint.\n"
            "4. **Rebuttal without Witness Box**: Rebut presumption through complainant's admissions without exposing accused to hostile cross-examination (*Basalingappa* doctrine)."
        ),
        "action_plan_client": (
            "1. **Reply to Notice Promptly**: Never ignore a Section 138 legal notice; silence creates an adverse inference against you.\n"
            "2. **Check Stop Payment Date**: If you lost cheques or gave them for security, ensure you have copy of the written letter submitted to your bank requesting stop payment.\n"
            "3. **Demand Complainant's ITR**: Ask your advocate to summon the complainant's Income Tax Returns; if they cannot show declared income, the case fails under Supreme Court law.\n"
            "4. **Obtain Bail on First Date**: Section 138 is **bailable**; appear with counsel on summons and furnish personal bond to avoid warrant."
        ),
        "landmarks": [
            "***Basalingappa v. Mudibasappa* (2019) 5 SCC 418 (3-Judge Bench)**: Supreme Court held accused is NOT required to step into witness box; presumption under Section 139 can be rebutted on a preponderance of probabilities by exposing lack of financial capacity of complainant.",
            "***M.S. Narayana Menon v. State of Kerala* (2006) 6 SCC 39**: Held that a cheque issued as collateral or security for a running account does not attract Section 138 if no liability existed on date of presentation.",
            "***Rakesh Ranjan Shrivastava v. State of Jharkhand* (2024) Supreme Court**: Held that grant of 20% interim compensation under Section 143A NI Act is directory and discretionary, not mandatory.",
        ],
        "citations": [
            "[Landmark SC] Basalingappa v. Mudibasappa (2019) 5 SCC 418 (Rebuttal of Section 139 Presumption)",
            "[Landmark SC] M.S. Narayana Menon v. State of Kerala (2006) 6 SCC 39 (Security Cheque Defense)",
            "[Landmark SC] Rakesh Ranjan Shrivastava v. State of Jharkhand (2024) (Section 143A Discretionary)",
            "[Statute] Negotiable Instruments Act, 1881 - Sections 138, 139, 143A",
        ],
        "canonical_expansion": "cheque bounce defense accused security cheque Section 139 NI Act rebuttal Basalingappa Mudibasappa MS Narayana Menon Rakesh Ranjan Shrivastava 143A financial capacity",
    },

    # 31. Contested Divorce on Fault Grounds (Cruelty, Desertion, Adultery)
    {
        "domain": "contested_divorce_cruelty_desertion",
        "title": "Contested Divorce on Fault Grounds (Cruelty, Desertion & Mental Harassment)",
        "triggers": [
            r"\b(contested divorce|file for divorce|divorce on cruelty|grounds of divorce)\b",
            r"\b(wife left home|husband left home|deserted me|living apart for years|refusing to come back|desertion)\b",
            r"\b(adultery|extra marital affair|cheating on spouse|mental cruelty in marriage)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Petitioning Spouse establishing statutory fault grounds is legally entitled to a Decree of Dissolution of Marriage:**\n\n"
            "Under **Section 13(1) of the Hindu Marriage Act, 1955**, either spouse can petition the Family Court for dissolution of marriage on specific statutory grounds, including **Cruelty (mental or physical)**, **Desertion for a continuous period of not less than 2 years**, and voluntary sexual intercourse with any person other than spouse."
        ),
        "supporting_sections": [
            "**Section 13(1)(i-a) Hindu Marriage Act, 1955**: **Cruelty**: Conduct causing reasonable apprehension in petitioner's mind that it will be harmful or injurious to live with spouse.",
            "**Section 13(1)(i-b) HMA**: **Desertion**: Deserted the petitioner for a continuous period of **not less than 2 years** immediately preceding presentation of petition without reasonable cause.",
            "**Section 24 HMA**: Interim Maintenance and litigation expenses during pendency of divorce proceedings.",
            "**Section 25 HMA**: Permanent alimony and maintenance at time of passing decree.",
            "**Family Courts Act, 1984 (Section 9)**: Mandatory duty of Family Court to endeavor conciliation and mediation between parties first.",
        ],
        "evidence_required": [
            "Marriage certificate, wedding photographs, and marriage registration certificate.",
            "Evidence of cruelty: abusive audio/video recordings, derogatory WhatsApp/email chats, or false police complaints.",
            "Evidence of desertion: proof of living in separate residences continuously for 2+ years without communication.",
            "Income affidavits and tax returns filed under *Rajnesh v. Neha* guidelines for maintenance adjudication.",
        ],
        "action_plan_advocate": (
            "1. **File Petition before Family Court**: Institute petition under Section 13(1)(ia)/(ib) before Family Court having territorial jurisdiction (where marriage solemnized, respondent resides, or parties last resided together).\n"
            "2. **Mediation / Reconciliation**: Participate in mandatory court mediation; if conciliation fails, proceed to formal framing of issues.\n"
            "3. **Interim Maintenance Defense/Claim**: Adjudicate Section 24 interim maintenance based on detailed assets disclosure.\n"
            "4. **Evidence & Cross-Examination**: Lead comprehensive oral testimony to prove sustained course of cruel conduct."
        ),
        "action_plan_client": (
            "1. **Document Date of Separation**: Establish the precise date when the spouse departed the matrimonial home without intent to return.\n"
            "2. **Do Not Engage in False Complaints**: Avoid filing exaggerated or omnibus criminal cases, as false criminal allegations against spouse are themselves legally classified as **Mental Cruelty** granting divorce to the other side (*K. Srinivas Rao*).\n"
            "3. **Attend Mandatory Counseling**: Family Courts require both parties to attend counseling sessions before regular trial begins.\n"
            "4. **Secure Child Custody / Visitation**: File interim application under Section 26 HMA to ensure child visitation is not blocked."
        ),
        "landmarks": [
            "***Naveen Kohli v. Neelu Kohli* (2006) 4 SCC 558**: Supreme Court held that where marriage is dead emotionally and practically, insisting on maintaining the legal bond causes more cruelty.",
            "***K. Srinivas Rao v. D.A. Deepa* (2013) 5 SCC 226**: Supreme Court held that filing false, scandalous, and defamatory complaints against spouse or their family amounts to mental cruelty entitling divorce.",
        ],
        "citations": [
            "[Landmark SC] Naveen Kohli v. Neelu Kohli (2006) 4 SCC 558 (Irretrievable Breakdown & Cruelty)",
            "[Landmark SC] K. Srinivas Rao v. D.A. Deepa (2013) 5 SCC 226 (False Complaints as Cruelty)",
            "[Statute] Hindu Marriage Act, 1955 - Section 13(1) (Grounds of Divorce)",
            "[Procedural Law] Family Courts Act, 1984 - Sections 7 & 9 (Mediation Mandate)",
        ],
        "canonical_expansion": "contested divorce Section 13 1 Hindu Marriage Act cruelty mental cruelty desertion 2 years adultery Naveen Kohli K Srinivas Rao Section 24 interim maintenance Family Court",
    },

    # 32. Non-Payment of Court-Ordered Maintenance (Execution & Distress Warrant)
    {
        "domain": "interim_maintenance_execution",
        "title": "Non-Payment of Court-Ordered Maintenance & Execution Proceedings (Section 125(3) CrPC)",
        "triggers": [
            r"\b(?:not\s+paying|stopped\s+paying|refusing\s+to\s+pay|defaulted\s+on|arrears\s+of|unpaid).*(?:maintenance|alimony)\b|\b(?:maintenance|alimony).*(?:not\s+paid|stopped|defaulted|arrears|recovery|execution)\b",
            r"\b(?:execution\s+petition|distress\s+warrant|attachment\s+of\s+salary|maintenance\s+order|arrears\s+of\s+maintenance|jail\s+for\s+maintenance)\b",
        ],
        "min_trigger_matches": 1,
        "who_is_right": (
            "**The Wife / Dependent Children are legally in the right.**\n"
            "Under Indian Law, a judicial order directing payment of maintenance under Section 125 CrPC, PWDVA, or Hindu Marriage Act is a **binding court decree**. "
            "A defaulting husband cannot defy court orders; the Magistrate has statutory power to issue **Distress Warrants for attachment of property, freeze bank accounts, and jail the defaulting husband** for up to 1 month for each month of default."
        ),
        "supporting_sections": [
            "**Section 125(3) CrPC / Section 144(3) BNSS**: **Enforcement of Maintenance Order**: Magistrate may issue warrant for levying the amount due in the manner provided for levying fines, and sentence defaulting person to **imprisonment for a term up to 1 month for each unpaid month** or until payment.",
            "**Section 128 CrPC / Section 147 BNSS**: Enforcement of order of maintenance anywhere in India where the defaulting person resides.",
            "**Section 20 & 28 PWDVA 2005**: Enforcement of monetary relief under Domestic Violence Act as a criminal fine.",
            "**Order XXI Rule 30 & 37 CPC**: Execution of maintenance decree by attachment of salary, bank accounts, and civil detention.",
            "**Civil Contempt of Court**: Deliberate disobedience of Supreme Court or High Court maintenance orders attracts contempt punishment.",
        ],
        "evidence_required": [
            "Certified copy of the Court Order granting interim or final maintenance.",
            "Arrears Calculation Sheet computing total months defaulted, payments received, and balance due.",
            "Bank statement of the wife showing non-receipt of monthly maintenance.",
            "Details of the husband's employment, salary, bank accounts, or immovable properties for attachment.",
        ],
        "action_plan_advocate": (
            "1. **File Execution Petition (Section 125(3) CrPC / Section 144(3) BNSS)**: File execution petition within 1 year from the date the arrears became due.\n"
            "2. **Prayer for Non-Bailable Distress Warrant**: Pray for issuance of Non-Bailable Warrant (NBW) / Distress Warrant against the husband.\n"
            "3. **Salary & Bank Account Attachment**: Move application directing the husband's employer to deduct maintenance directly from salary (garnishee order).\n"
            "4. **Striking off Defense**: If husband appears in matrimonial divorce proceedings while defaulting on maintenance, move application to **strike off his defense** until arrears are cleared."
        ),
        "action_plan_client": (
            "1. **Keep Arrears Ledger Updated**: Maintain a clear table showing: Month, Ordered Amount, Received Amount, Default Amount.\n"
            "2. **File within 1 Year**: By law, Section 125(3) warrants must be applied for within **1 year** from the date the amount became due; do not wait indefinitely.\n"
            "3. **Provide Employer Details**: Give your advocate the company name, branch, and HR email where your husband works so salary attachment can be served.\n"
            "4. **Jail Sentence Does Not Wipe Debt**: Remember that even if the husband spends 1 month in jail for default, the debt is NOT erased; he remains liable to pay the full arrears."
        ),
        "landmarks": [
            "***Rajnesh v. Neha* (2020) 10 SCC 733**: Supreme Court held that maintenance orders are immediately enforceable as money decrees; defense can be struck off and contempt initiated for willful non-payment.",
            "***Kuldip Kaur v. Surjit Singh* (1989) 1 SCC 406**: Supreme Court held that sentencing defaulting husband to jail under Section 125(3) is a mode of enforcement, not a satisfaction of debt.",
        ],
        "citations": [
            "[Landmark SC] Rajnesh v. Neha (2020) 10 SCC 733 (Enforcement of Maintenance)",
            "[Landmark SC] Kuldip Kaur v. Surjit Singh (1989) 1 SCC 406",
            "[Statute] Code of Criminal Procedure, 1973 - Section 125(3) & Section 128",
            "[Statute] Bharatiya Nagarik Suraksha Sanhita, 2023 - Section 144(3) & Section 147",
        ],
        "canonical_expansion": "maintenance arrears not paying maintenance Section 125 3 CrPC Section 144 3 BNSS distress warrant attachment of salary Kuldip Kaur Rajnesh v Neha execution petition",
    },
]


def match_story_scenario(query: str) -> Optional[Dict[str, Any]]:
    """
    Evaluates whether an incoming query describes a real-world story or legal dispute scenario.
    Returns the matching scenario config dictionary, or None if not a scenario.
    """
    q_lower = query.lower().strip()

    best_match: Optional[Dict[str, Any]] = None
    max_score = 0

    for config in SCENARIO_CONFIGS:
        if any(re.search(neg, q_lower) for neg in config.get("negative_triggers", [])):
            continue
        score = 0
        for pat in config["triggers"]:
            if re.search(pat, q_lower):
                score += 1
        if score >= config["min_trigger_matches"] and score > max_score:
            max_score = score
            best_match = config

    return best_match


def synthesize_story_scenario_response(
    scenario: Dict[str, Any], query: str, role: str
) -> Tuple[str, List[str]]:
    """
    Synthesizes rich, structured, research-grade legal advice for a real-world scenario,
    explicitly declaring WHO IS RIGHT, WHICH SECTIONS SUPPORT THEM, and the STRATEGIC ROADMAP.
    """
    sections_block = "\n".join([f"• {sec}" for sec in scenario["supporting_sections"]])
    evidence_block = "\n".join([f"• {ev}" for ev in scenario["evidence_required"]])
    landmarks_block = "\n".join([f"• {lm}" for lm in scenario["landmarks"]])

    action_plan = (
        scenario["action_plan_advocate"] if role == "advocate" else scenario["action_plan_client"]
    )

    text = (
        f"### 📌 Real-World Dispute Assessment: {scenario['title']}\n"
        f"Based on your factual scenario: **'{query}'**, here is the authoritative legal analysis, "
        f"rights determination, and procedural roadmap under the Indian Legal Framework.\n\n"
        f"### 🧑‍⚖️ Factual Matrix & Legal Standing (WHO IS RIGHT & WHO IS WRONG)\n"
        f"{scenario['who_is_right']}\n\n"
        f"### 📜 Governing Statutory Provisions & Sections (Which Sections Support You)\n"
        f"Here are the explicit penal and protective provisions supporting your legal standing:\n"
        f"{sections_block}\n\n"
        f"### 🚨 Essential Legal Ingredients & Evidentiary Proof\n"
        f"To successfully maintain proceedings or prosecution, you must assemble the following records:\n"
        f"{evidence_block}\n\n"
        f"### 🛡️ Step-by-Step Strategic Roadmap ({role.upper()} Perspective)\n"
        f"{action_plan}\n\n"
        f"### 🏛️ Binding Supreme Court Precedents\n"
        f"{landmarks_block}\n\n"
        f"> **Disclaimer**: Educational legal prototype. Please verify all draftings with an Advocate before filing."
    )

    citations = scenario["citations"]
    return text, citations
