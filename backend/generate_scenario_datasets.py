"""
Generator for Comprehensive Legal Scenario Datasets for S2 Legal AI Pro
Builds rich, authoritative scenario and problem-solving statutory PDF documents in backend/data/:
1. family_and_matrimonial_disputes_scenarios.pdf
2. property_land_and_civil_disputes_scenarios.pdf
3. financial_fraud_cheque_bounce_scenarios.pdf
4. criminal_accidents_and_general_exceptions_scenarios.pdf
"""

from pathlib import Path
import sys

# Ensure backend can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from backend.corpus_builder import create_pdf_binary

DATA_DIR = Path(__file__).resolve().parent / "data"

def build_family_disputes_data():
    return [
        (
            "FAMILY SCENARIO: MATRIMONIAL HARASSMENT, CRUELTY & DOWRY DEMANDS",
            "FACTUAL MATRIX & DISPUTE: A wife is harassed, mentally and physically tortured by her husband and in-laws "
            "with persistent demands for money, vehicles, or ancestral gold. In-laws threaten to expel her from the matrimonial home.\n\n"
            "LEGAL STANDING & WHO IS IN THE RIGHT: The wife is legally in the right. The husband and in-laws are guilty of cognizable "
            "criminal offences and civil domestic abuse under Indian Law.\n\n"
            "STATUTORY SECTIONS SUPPORTING THE WIFE:\n"
            "1. Section 498A IPC / Section 85 & 86 BNS: Cruelty by husband or relatives of husband. Punishment up to 3 years imprisonment and fine. Non-bailable and cognizable.\n"
            "2. Dowry Prohibition Act, 1961 (Sections 3 & 4): Penalty for giving, taking, or demanding dowry. Minimum 5 years imprisonment.\n"
            "3. Protection of Women from Domestic Violence Act, 2005 (PWDVA):\n"
            "   - Section 12: Application to Magistrate for comprehensive protection and monetary relief.\n"
            "   - Section 17: Right to reside in a shared household; husband cannot evict her without due process of law.\n"
            "   - Section 18: Protection Orders restraining husband/in-laws from contacting or entering her residence/workplace.\n"
            "   - Section 19: Residence Orders directing in-laws to provide alternative accommodation or vacate shared home.\n"
            "   - Section 20 & 22: Monetary relief for medical expenses, loss of earnings, and compensation for mental agony.\n"
            "4. Section 125 CrPC / Section 144 BNSS: Mandatory monthly maintenance for wife and minor children unable to maintain themselves.\n\n"
            "LANDMARK PRECEDENTS:\n"
            "- Rajnesh v. Neha (2020) Supreme Court: Mandatory disclosure of assets and income affidavits by husband for maintenance.\n"
            "- Arnesh Kumar v. State of Bihar (2014) Supreme Court: Safeguards under Section 35(3) BNSS / 41A CrPC against routine arrest.\n"
            "- Prabha Tyagi v. Kamlesh Devi (2022) Supreme Court: Woman has right to shared household even if residing separately at time of complaint."
        ),
        (
            "FAMILY SCENARIO: ANCESTRAL PROPERTY PARTITION & DAUGHTERS EQUAL RIGHTS",
            "FACTUAL MATRIX & DISPUTE: A Hindu father passes away intestate (without leaving a will). Sons and brothers take control "
            "of all agricultural land, houses, and bank accounts, refusing to provide any share to married or unmarried daughters, claiming daughters have no coparcenary rights.\n\n"
            "LEGAL STANDING & WHO IS IN THE RIGHT: The daughters are entirely in the right. The brothers' exclusion of daughters is illegal and void ab initio.\n\n"
            "STATUTORY SECTIONS SUPPORTING THE DAUGHTERS:\n"
            "1. Section 6 Hindu Succession Act, 1956 (amended by Act 39 of 2005): A daughter of a coparcener shall by birth become a coparcener in her own right in the same manner as the son, with identical coparcenary rights and liabilities.\n"
            "2. Section 8 Hindu Succession Act, 1956: General rules of succession in the case of males dying intestate. Class I heirs (sons, daughters, widow, mother) take equally.\n"
            "3. Order XXXIX Rules 1 & 2 CPC / Section 38 Specific Relief Act, 1963: Application for temporary injunction restraining brothers from selling, mortgaging, or creating third-party interests in ancestral property pending partition.\n"
            "4. Section 441 & 447 IPC (Criminal Trespass) & Section 406 IPC (Criminal Breach of Trust): Actionable if brothers illegally usurp movable stridhan or forged transfer papers.\n\n"
            "LANDMARK PRECEDENT:\n"
            "- Vineeta Sharma v. Rakesh Sharma (2020) 9 SCC 1 (3-Judge Constitutional Bench of Supreme Court): Held that daughters have equal coparcenary rights by birth under Section 6 HSA from 1956 onwards, regardless of whether the father was alive on September 9, 2005. Coparcenary right is conferred by birth and cannot be defeated by prior oral family partitions unless registered before 20th December 2004."
        ),
        (
            "FAMILY SCENARIO: MUTUAL CONSENT DIVORCE, ALIMONY & CHILD CUSTODY",
            "FACTUAL MATRIX & DISPUTE: A husband and wife have lived separately for more than one year due to temperamental incompatibility. "
            "Disputes arise over permanent alimony, division of joint assets, and child custody.\n\n"
            "LEGAL STANDING & PROCEDURAL RESOLUTION:\n"
            "1. Section 13B Hindu Marriage Act, 1955: Divorce by mutual consent. First motion followed by second motion after 6-month statutory period.\n"
            "   - Waiver of 6-Month Cooling Period: Under Supreme Court landmark Amardeep Singh v. Harveen Kaur (2017), the 6-month period under Section 13B(2) is directory, not mandatory. Courts can waive cooling period if mediation fails and settlement is complete.\n"
            "2. Section 25 Hindu Marriage Act, 1955: Permanent alimony and maintenance. The court evaluates gross earnings, lifestyle, assets, and liabilities of both spouses.\n"
            "3. Child Custody & Guardianship:\n"
            "   - Sections 7, 17 Guardians and Wards Act, 1890 & Section 6 Hindu Minority and Guardianship Act, 1956.\n"
            "   - Welfare of the Child Principle (Gaurav Nagpal v. Sumedha Nagpal, Supreme Court): The paramount consideration in custody is not the legal rights of parents, but the best physical, moral, and psychological welfare of the child.\n"
            "   - Presumption: Natural custody of a child under 5 years belongs ordinarily to the mother."
        ),
        (
            "FAMILY SCENARIO: SENIOR CITIZENS NEGLECT & ILLEGAL PROPERTY TRANSFER",
            "FACTUAL MATRIX & DISPUTE: Elderly parents transfer ancestral or self-acquired home to their son on the condition of care and food. "
            "After title transfer, the son and daughter-in-law mistreat, starve, and attempt to evict the elderly parents.\n\n"
            "LEGAL STANDING & WHO IS IN THE RIGHT: The elderly parents are entirely in the right. The law renders such conditional transfers void.\n\n"
            "STATUTORY SECTIONS SUPPORTING THE PARENTS:\n"
            "1. Section 23 Maintenance and Welfare of Parents and Senior Citizens Act, 2007: Transfer of property to be void in certain circumstances. Where a senior citizen has transferred property by gift or otherwise, subject to the condition that the transferee shall provide basic amenities, and the transferee fails, the transfer of property is deemed fraudulent and declared void by the Maintenance Tribunal.\n"
            "2. Section 4 & 5 Senior Citizens Act, 2007: Monthly maintenance up to statutory limits, enforceable through summary proceedings within 90 days.\n"
            "3. Section 125(1)(d) CrPC / Section 144 BNSS: Mandatory maintenance orders against adult children having sufficient means.\n"
            "4. Landmark Precedent: S. Vanitha v. Deputy Commissioner (2020) Supreme Court: Harmonized Senior Citizens Act with Domestic Violence Act, upholding protection of parents from harassment in their self-acquired homes."
        ),
    ]

def build_property_civil_data():
    return [
        (
            "PROPERTY SCENARIO: ILLEGAL LAND ENCROACHMENT, BOUNDARY DISPUTE & TRESPASS",
            "FACTUAL MATRIX & DISPUTE: A neighbor or trespasser illegally knocks down boundary pillars, occupies agricultural or residential plot, "
            "or constructs an unauthorized wall on vacant land belonging to a registered owner.\n\n"
            "LEGAL STANDING & WHO IS IN THE RIGHT: The registered titleholder is legally in the right. The trespasser commits both a civil tort and cognizable criminal offences.\n\n"
            "STATUTORY SECTIONS SUPPORTING THE OWNER:\n"
            "1. Criminal Remedies:\n"
            "   - Section 441 & 447 IPC / Section 329 BNS: Criminal Trespass. Whoever enters into or upon property in possession of another with intent to commit an offence or intimidate/insult/annoy.\n"
            "   - Section 427 IPC / Section 324 BNS: Mischief causing damage to property.\n"
            "   - Section 145 CrPC / Section 164 BNSS: Executive Magistrate powers to decide immediate possession and prevent breach of peace.\n"
            "2. Civil Remedies:\n"
            "   - Section 5 & 6 Specific Relief Act, 1963: Recovery of specific immovable property. Under Section 6, any person dispossessed without due process of law can file summary suit within 6 months of dispossession irrespective of title disputes.\n"
            "   - Section 38 Specific Relief Act, 1963: Perpetual Injunction restraining trespasser from interfering with peaceful possession.\n"
            "   - Order XXXIX Rules 1 & 2 CPC: Immediate temporary status-quo or ad-interim injunction order.\n"
            "   - Demarcation & Revenue Survey: Application before local Tehsildar/Collector under State Land Revenue Code for official police-assisted boundary demarcation."
        ),
        (
            "PROPERTY SCENARIO: TENANT NON-PAYMENT, HOLDING OVER & ILLEGAL EVICTION",
            "FACTUAL MATRIX & DISPUTE: A residential or commercial tenant stops paying rent for months after the registered lease expires. "
            "The landlord cuts off water/power or locks the gate to force the tenant out. Tenant claims rights, landlord claims eviction.\n\n"
            "LEGAL STANDING & RIGHTS:\n"
            "1. Tenant's Default: The tenant has no legal right to remain without paying rent. Landlord has right to possession and mesne profits.\n"
            "2. Landlord's Illegal Acts: A landlord CANNOT take the law into their own hands. Cutting off electricity, water, or locking premises without court order is illegal under Rent Control Acts and constitutes criminal wrongful restraint under Section 339 IPC / Section 126 BNS.\n"
            "3. Lawful Procedure for Landlord:\n"
            "   - Section 106 Transfer of Property Act, 1882: Mandatory 15-day (residential) or 6-month (agricultural/manufacturing) Notice to Quit.\n"
            "   - Civil Suit for Eviction & Recovery of Arrears of Rent under Rent Control Act / Transfer of Property Act.\n"
            "   - Claim for Mesne Profits: Compensation under Order XX Rule 12 CPC for unauthorized use and occupation from date of expiry of tenancy.\n"
            "   - Landmark Precedent: Ramesh Chand Ardawatiya v. Anil Panjwani (2003) Supreme Court: Even a trespasser or unauthorized occupant in settled possession cannot be dispossessed by force; eviction must occur through due process of law."
        ),
        (
            "PROPERTY SCENARIO: BUILDER DELAY, NON-DELIVERY & FLAT BUYER RIGHTS",
            "FACTUAL MATRIX & DISPUTE: A homebuyer pays 90% of the flat consideration. The builder promises possession in 3 years but fails "
            "to deliver after 6 years, citing construction delays and demanding extra escalation charges.\n\n"
            "LEGAL STANDING & WHO IS IN THE RIGHT: The homebuyer is in the right. Unilateral delay and one-sided clauses constitute unfair trade practice and breach of statutory duty.\n\n"
            "STATUTORY SECTIONS SUPPORTING THE BUYER:\n"
            "1. Section 18 Real Estate (Regulation and Development) Act, 2016 (RERA): If builder fails to complete or give possession in accordance with agreement for sale, buyer has absolute right to:\n"
            "   - Full refund of paid amount with interest at prescribed rate (SBI MCLR + 2%); OR\n"
            "   - Monthly interest for every month of delay till handover of lawful possession.\n"
            "2. Consumer Protection Act, 2019 (Sections 34, 47, 58): Consumer Commission complaint for deficiency in service and unfair trade practice.\n"
            "3. Insolvency and Bankruptcy Code, 2016 (IBC Section 7): Homebuyers are recognized as Financial Creditors.\n"
            "4. Landmark Precedent: Pioneer Urban Land and Infrastructure v. Govindan Raghavan (2019) Supreme Court: One-sided terms in builder-buyer agreement cannot be enforced against homebuyer; buyer cannot be compelled to wait indefinitely for possession."
        ),
    ]

def build_financial_fraud_data():
    return [
        (
            "FINANCIAL SCENARIO: CHEQUE BOUNCE (SECTION 138 NEGOTIABLE INSTRUMENTS ACT)",
            "FACTUAL MATRIX & DISPUTE: A debtor or business partner issues a signed cheque of Rs 10 Lakhs towards repayment of a friendly loan, "
            "goods supplied, or commercial services. The cheque bounces upon presentation with bank remarks 'Funds Insufficient' or 'Account Closed'.\n\n"
            "LEGAL STANDING & WHO IS IN THE RIGHT: The payee (creditor) is legally in the right. The drawer is criminally liable under the NI Act.\n\n"
            "STATUTORY TIMELINE & PROCEDURE UNDER SECTION 138 NI ACT:\n"
            "1. Step 1: Cheque Presentation: Cheque must be presented within validity period (3 months from date of issue).\n"
            "2. Step 2: Statutory Legal Notice: Upon receipt of Bank Return Memo, payee must issue a formal Legal Demand Notice in writing to drawer within 30 days.\n"
            "3. Step 3: 15-Day Cure Period: The notice must demand payment within 15 days of receipt of notice.\n"
            "4. Step 4: Criminal Complaint (Section 142 NI Act): If drawer fails to pay within 15 days, cause of action arises on 16th day. Complaint must be filed within 30 days before Judicial Magistrate having jurisdiction where payee maintains bank account.\n"
            "5. Section 138 Penalties: Imprisonment up to 2 years, or fine up to twice the cheque amount, or both.\n"
            "6. Section 143A NI Act: Court can order drawer to deposit Interim Compensation up to 20% of the cheque amount during trial.\n"
            "7. Presumptions under Sections 118 & 139 NI Act: Law presumes cheque was issued for discharge of a legally enforceable debt (rebuttable presumption).\n"
            "8. Landmark Precedents:\n"
            "- Dashrath Rupsingh Rathod v. State of Maharashtra (2014) & 2015 NI Act Amendment: Jurisdiction lies where payee's bank account is maintained.\n"
            "- Bir Singh v. Mukesh Kumar (2019) Supreme Court: Even if cheque details are filled by another person, signed cheque attracts Section 139 presumption."
        ),
        (
            "FINANCIAL SCENARIO: BUSINESS FRAUD, CHEATING & RECOVERY OF MONEY",
            "FACTUAL MATRIX & DISPUTE: A party induces an investor or merchant to transfer funds based on false representations of high returns "
            "or delivery of goods, then absconds or refuses to repay, claiming it is merely a civil breach of contract.\n\n"
            "LEGAL STANDING & STATUTORY INGREDIENTS:\n"
            "1. Cheating vs Breach of Contract:\n"
            "   - Mere breach of contract: Remediable civilly under Section 73 Indian Contract Act 1872.\n"
            "   - Criminal Cheating (Section 420 IPC / Section 318(4) BNS): Arises when dishonest intention (mens rea) existed AT THE VERY INCEPTION of the transaction (Hridaya Ranjan Prasad Verma v. State of Bihar, Supreme Court).\n"
            "2. Section 405 & 406 IPC / Section 316 BNS: Criminal Breach of Trust. Misappropriation of property entrusted to a person.\n"
            "3. Civil Remedies for Money Recovery:\n"
            "   - Order XXXVII Civil Procedure Code, 1908: Summary Suit for recovery of debt based on written contract, bill of exchange, or promissory note.\n"
            "   - Commercial Courts Act, 2015: Commercial suit with pre-institution mandatory mediation.\n"
            "   - Order XXXVIII Rule 5 CPC: Attachment before judgment of defendant's property to prevent siphon off of assets."
        ),
        (
            "FINANCIAL SCENARIO: CYBER FRAUD, OTP THEFT & IDENTITY IMPERSONATION",
            "FACTUAL MATRIX & DISPUTE: An online scammer calls posing as bank customer service, steals OTP, and siphons funds via UPI, "
            "or creates a duplicate social media profile to extort money from friends.\n\n"
            "LEGAL STANDING & STATUTORY PROVISIONS:\n"
            "1. Information Technology Act, 2000:\n"
            "   - Section 66C: Identity theft by fraudulently making use of electronic signature, password, or unique identification feature.\n"
            "   - Section 66D: Cheating by personation by using computer resource. Punishment up to 3 years and fine.\n"
            "2. Indian Penal Code & BNS:\n"
            "   - Section 419 IPC / Section 319 BNS: Cheating by personation.\n"
            "   - Section 420 IPC / Section 318(4) BNS: Cheating and dishonestly inducing delivery of property.\n"
            "3. Immediate Action Plan (Golden Hour Protocol):\n"
            "   - Dial 1930 (National Cyber Crime Helpline) or lodge complaint on cybercrime.gov.in within golden hour to freeze fraudulent bank accounts.\n"
            "   - RBI Circular on Zero Liability of Customer (2017): Customer liability is ZERO if unauthorized transaction occurs due to third-party breach and customer notifies bank within 3 working days."
        ),
    ]

def build_accidents_general_exceptions_data():
    return [
        (
            "CRIMINAL SCENARIO: ROAD ACCIDENT (RASH & NEGLIGENT DRIVING VS MOTOR CLAIMS)",
            "FACTUAL MATRIX & DISPUTE: A speeding vehicle jumps a red light and hits a pedestrian or two-wheeler, causing severe injuries or death. "
            "Driver flees the scene (hit and run).\n\n"
            "LEGAL STANDING & PROSECUTION PROVISIONS:\n"
            "1. Criminal Liability of Accused Driver:\n"
            "   - Section 279 IPC / Section 281 BNS: Rash driving or riding on a public way so as to endanger human life.\n"
            "   - Section 337 & 338 IPC / Section 125 BNS: Causing hurt or grievous hurt by endangering life or personal safety of others.\n"
            "   - Section 304A IPC / Section 106(1) BNS: Causing death by negligence not amounting to culpable homicide.\n"
            "   - Section 106(2) BNS (Hit and Run): Failure to report accident to police officer or magistrate immediately attracts enhanced punishment up to 10 years imprisonment.\n"
            "2. Victim & Family Civil Remedies (Motor Accident Claims Tribunal - MACT):\n"
            "   - Section 166 Motor Vehicles Act, 1988: Claim petition for compensation against driver, owner, and insurance company.\n"
            "   - Computation of Compensation (Sarla Verma v. DTC & National Insurance v. Pranay Sethi, Supreme Court): Multiplier method applied to victim's income, future prospects (40-50%), loss of consortium, funeral expenses, and loss of estate. Insurance company strictly liable to pay."
        ),
        (
            "CRIMINAL SCENARIO: RIGHT OF PRIVATE DEFENCE (SELF-DEFENCE OF BODY & PROPERTY)",
            "FACTUAL MATRIX & DISPUTE: An individual is ambushed at night by armed intruders threatening murder or rape. "
            "The defender strikes back with a weapon, causing severe injury or death to the assailant. Accused claims self-defence.\n\n"
            "LEGAL STANDING & STATUTORY EXCEPTION:\n"
            "1. Section 96 IPC / Section 34 BNS: Things done in private defence. Nothing is an offence which is done in the exercise of the right of private defence.\n"
            "2. Section 97 IPC / Section 35 BNS: Right of private defence extends to defence of own body and body of any other person, and property (movable or immovable) against theft, robbery, mischief, or criminal trespass.\n"
            "3. Section 100 IPC / Section 38 BNS: When Right of Private Defence of Body Extends to Causing Death:\n"
            "   - Reasonable apprehension of death;\n"
            "   - Reasonable apprehension of grievous hurt;\n"
            "   - Act with the intention of committing rape;\n"
            "   - Act with intention of gratifying unnatural lust;\n"
            "   - Act with intention of kidnapping or abducting;\n"
            "   - Act with intention of wrongfully confining a person under circumstances where public authorities cannot be accessed.\n"
            "4. Section 103 IPC / Section 41 BNS: Private defence of property causing death (Robbery, house-breaking by night, mischief by fire).\n"
            "5. Section 99 IPC / Section 37 BNS: Acts against which there is no right of private defence. Must not inflict more harm than necessary for the purpose of defence.\n"
            "6. Landmark Precedent: Darshan Singh v. State of Punjab (2010) Supreme Court: Formulated 10 cardinal principles of private defence; a person facing imminent peril cannot be expected to weigh strikes in golden scales."
        ),
    ]

def generate_all_scenario_datasets():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    files_to_generate = [
        ("family_and_matrimonial_disputes_scenarios.pdf", build_family_disputes_data()),
        ("property_land_and_civil_disputes_scenarios.pdf", build_property_civil_data()),
        ("financial_fraud_cheque_bounce_scenarios.pdf", build_financial_fraud_data()),
        ("criminal_accidents_and_general_exceptions_scenarios.pdf", build_accidents_general_exceptions_data()),
    ]

    for fname, sections in files_to_generate:
        pdf_path = DATA_DIR / fname
        pdf_bytes = create_pdf_binary(sections)
        pdf_path.write_bytes(pdf_bytes)
        print(f"[SCENARIO DATASET] Created: {fname} ({len(pdf_bytes)} bytes, {len(sections)} scenario pages)")

if __name__ == "__main__":
    generate_all_scenario_datasets()
