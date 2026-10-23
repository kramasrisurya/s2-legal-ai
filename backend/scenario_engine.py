"""
S2 Legal AI Pro - Real-World Story & Fact-Pattern Legal Reasoning Engine
Module: backend.scenario_engine

Analyzes real-world legal scenarios, family disputes, property conflicts, financial fraud,
and accidents to determine:
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
            r"\b(family issue|family dispute|marital dispute|in-laws issue)\b",
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
            r"\b(tenant|landlord|rent agreement|lease)\b",
            r"\b(not paying rent|refusing to vacate|unpaid rent|arrears|holding over)\b",
            r"\b(cut electricity|cut water|locked premises|locked gate|force out)\b",
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

    # 8. Cyber Crime: Online Fraud & OTP Scam
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
            r"\b(accident|car crash|hit and run|speeding vehicle|truck hit|bike hit)\b",
            r"\b(rash driving|negligent driving|injured|grievous hurt|death in accident)\b",
            r"\b(mact|accident claim|compensation)\b",
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
            r"\b(self defence|self defense|attacked me|attacked us|ambushed)\b",
            r"\b(struck back|hit back|killed in self defence|protected myself)\b",
            r"\b(armed attacker|deadly weapon|threatened to kill me)\b",
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
]


def match_story_scenario(query: str) -> Optional[Dict[str, Any]]:
    """
    Evaluates whether an incoming query describes a real-world story or legal dispute scenario.
    Returns the matching scenario config dictionary, or None if not a scenario.
    """
    q_lower = query.lower()

    # Story indicators
    narrative_cues = [
        "my husband", "my wife", "my in-laws", "my father", "my brother", "my sister",
        "my son", "my daughter", "my neighbor", "my tenant", "my landlord", "my friend",
        "bought land", "ancestral property", "cheated me", "bounced", "took loan",
        "family issue", "family dispute", "who is right", "who is correct", "which section supports",
        "what can i do", "what should i do", "is it legal", "what are my rights",
        "road accident", "hit and run", "self defence", "self defense", "threatened to"
    ]
    has_narrative = any(cue in q_lower for cue in narrative_cues) or len(query.split()) >= 8

    if not has_narrative:
        return None

    best_match: Optional[Dict[str, Any]] = None
    max_score = 0

    for config in SCENARIO_CONFIGS:
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
