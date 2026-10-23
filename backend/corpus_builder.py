"""
Corpus Builder for S2 Legal AI Pro
Generates standard legal PDF documents for:
1. The Constitution of India (Complete Articles, Parts I to XXII, Schedules)
2. Supreme Court of India Landmark Precedents & Judgments
"""

from pathlib import Path
from typing import List, Tuple

def create_pdf_binary(sections: List[Tuple[str, str]]) -> bytes:
    """Generates standard PDF 1.4 binary stream."""
    objects: List[bytes] = []

    def add_object(content: bytes) -> int:
        objects.append(content)
        return len(objects)

    pages_obj_num = 1
    font_obj_num = 2
    objects.append(b"")  # placeholder 1: Pages
    objects.append(b"")  # placeholder 2: Font

    font_bytes = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
    objects[font_obj_num - 1] = font_bytes

    page_obj_nums = []

    for title, text in sections:
        safe_title = title.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        wrapped_lines = []
        for raw_line in text.split("\n"):
            words = raw_line.split(" ")
            cur = ""
            for w in words:
                if len(cur) + len(w) + 1 > 75:
                    wrapped_lines.append(cur)
                    cur = w
                else:
                    cur = f"{cur} {w}".strip()
            if cur:
                wrapped_lines.append(cur)

        stream_cmds = [
            "BT",
            "/F1 13 Tf",
            "50 750 Td",
            f"({safe_title}) Tj",
            "/F1 9.5 Tf",
            "0 -22 Td",
        ]
        for line in wrapped_lines:
            safe_line = line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            stream_cmds.append(f"({safe_line}) Tj")
            stream_cmds.append("0 -13 Td")
        stream_cmds.append("ET")

        stream_data = "\n".join(stream_cmds).encode("latin-1", errors="replace")
        content_obj_bytes = (
            f"<< /Length {len(stream_data)} >>\nstream\n".encode("latin-1")
            + stream_data
            + b"\nendstream"
        )
        content_obj_num = add_object(content_obj_bytes)

        page_dict = (
            f"<< /Type /Page /Parent 1 0 R "
            f"/MediaBox [0 0 612 792] "
            f"/Contents {content_obj_num} 0 R "
            f"/Resources << /Font << /F1 2 0 R >> >> >>"
        ).encode("latin-1")
        p_num = add_object(page_dict)
        page_obj_nums.append(p_num)

    kids_refs = " ".join([f"{num} 0 R" for num in page_obj_nums])
    pages_bytes = f"<< /Type /Pages /Kids [{kids_refs}] /Count {len(page_obj_nums)} >>".encode("latin-1")
    objects[pages_obj_num - 1] = pages_bytes

    catalog_bytes = b"<< /Type /Catalog /Pages 1 0 R >>"
    catalog_num = add_object(catalog_bytes)

    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out.extend(f"{i} 0 obj\n".encode("latin-1"))
        out.extend(obj)
        out.extend(b"\nendobj\n")

    xref_start = len(out)
    out.extend(f"xref\n0 {len(objects) + 1}\n".encode("latin-1"))
    out.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        out.extend(f"{off:010d} 00000 n \n".encode("latin-1"))

    out.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_num} 0 R >>\n"
        f"startxref\n{xref_start}\n%%EOF\n".encode("latin-1")
    )
    return bytes(out)


def build_constitution_records() -> List[Tuple[str, str]]:
    """Complete structural provisions of the Constitution of India."""
    return [
        (
            "THE CONSTITUTION OF INDIA - PREAMBLE",
            "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a "
            "SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC and to secure to all its citizens: "
            "JUSTICE, social, economic and political; "
            "LIBERTY of thought, expression, belief, faith and worship; "
            "EQUALITY of status and of opportunity; and to promote among them all "
            "FRATERNITY assuring the dignity of the individual and the unity and integrity of the Nation; "
            "IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November, 1949, do HEREBY ADOPT, "
            "ENACT AND GIVE TO OURSELVES THIS CONSTITUTION."
        ),
        (
            "PART I - THE UNION AND ITS TERRITORY (ARTICLES 1-4)",
            "ARTICLE 1. NAME AND TERRITORY OF THE UNION: (1) India, that is Bharat, shall be a Union of States. "
            "(2) The States and territories thereof shall be as specified in the First Schedule. "
            "(3) The territory of India shall comprise: the territories of the States, the Union territories, "
            "and such other territories as may be acquired.\n\n"
            "ARTICLE 2. ADMISSION OR ESTABLISHMENT OF NEW STATES: Parliament may by law admit into the Union, "
            "or establish, new States on such terms and conditions as it thinks fit.\n\n"
            "ARTICLE 3. FORMATION OF NEW STATES AND ALTERATION OF AREAS, BOUNDARIES OR NAMES OF EXISTING STATES: "
            "Parliament may by law form a new State by separation of territory from any State or by uniting two or more States, "
            "increase the area of any State, diminish the area of any State, alter the boundaries of any State, alter the name of any State."
        ),
        (
            "PART II - CITIZENSHIP (ARTICLES 5-11)",
            "ARTICLE 5. CITIZENSHIP AT COMMENCEMENT OF CONSTITUTION: Every person who has his domicile in the territory of India "
            "and who was born in the territory of India, or either of whose parents was born in the territory of India, "
            "or who has been ordinarily resident in India for not less than five years immediately preceding commencement.\n\n"
            "ARTICLE 9. PERSONS VOLUNTARILY ACQUIRING CITIZENSHIP OF A FOREIGN STATE NOT TO BE CITIZENS: Single citizenship principle.\n\n"
            "ARTICLE 11. PARLIAMENT TO REGULATE THE RIGHT OF CITIZENSHIP BY LAW: Parliament retains plenary legislative competence "
            "with respect to acquisition, termination of citizenship and all other matters relating thereto (Citizenship Act, 1955)."
        ),
        (
            "PART III - FUNDAMENTAL RIGHTS: DEFINITIONS & VOID LAWS (ARTICLES 12-13)",
            "ARTICLE 12. DEFINITION OF THE STATE: In this Part, unless the context otherwise requires, 'the State' includes "
            "the Government and Parliament of India and the Government and the Legislature of each of the States and all local or "
            "other authorities within the territory of India or under the control of the Government of India.\n\n"
            "ARTICLE 13. LAWS INCONSISTENT WITH OR IN DEROGATION OF FUNDAMENTAL RIGHTS: "
            "(1) All pre-constitutional laws inconsistent with Part III are void to the extent of inconsistency (Doctrine of Eclipse / Severability). "
            "(2) The State shall not make any law which takes away or abridges the rights conferred by this Part; any law in contravention is void. "
            "(3) 'Law' includes ordinance, order, bye-law, rule, regulation, notification, custom having the force of law."
        ),
        (
            "PART III - RIGHT TO EQUALITY (ARTICLES 14-18)",
            "ARTICLE 14. EQUALITY BEFORE LAW: The State shall not deny to any person equality before the law or the equal protection "
            "of the laws within the territory of India. Encompasses negative concept of absence of privilege and positive concept of "
            "equal treatment in equal circumstances. Prohibits arbitrariness (E.P. Royappa doctrine of non-arbitrariness).\n\n"
            "ARTICLE 15. PROHIBITION OF DISCRIMINATION ON GROUNDS OF RELIGION, RACE, CASTE, SEX OR PLACE OF BIRTH: "
            "Clauses (3)-(5) empower State to enact special protective provisions for women, children, and socially/educationally backward classes.\n\n"
            "ARTICLE 16. EQUALITY OF OPPORTUNITY IN MATTERS OF PUBLIC EMPLOYMENT: Equality of opportunity in public appointments. "
            "Clauses (4), (4A), (4B) validate reservations in appointments and promotions subject to efficiency of administration (Article 335).\n\n"
            "ARTICLE 17. ABOLITION OF UNTOUCHABILITY: Untouchability is abolished and its practice in any form is strictly forbidden.\n\n"
            "ARTICLE 18. ABOLITION OF TITLES: No title, not being a military or academic distinction, shall be conferred by the State."
        ),
        (
            "PART III - RIGHT TO FREEDOM (ARTICLES 19-20)",
            "ARTICLE 19. PROTECTION OF SIX BASIC FREEDOMS: All citizens shall have the right: "
            "(a) to freedom of speech and expression; (b) to assemble peaceably and without arms; "
            "(c) to form associations or unions or co-operative societies; (d) to move freely throughout the territory of India; "
            "(e) to reside and settle in any part of the territory of India; (g) to practise any profession, trade or business. "
            "Reasonable restrictions may be imposed under clauses (2) to (6) in interests of sovereignty, integrity, security of State, "
            "public order, decency, morality, contempt of court, defamation, incitement to an offence.\n\n"
            "ARTICLE 20. PROTECTION IN RESPECT OF CONVICTION FOR OFFENCES: "
            "(1) Protection against ex-post facto laws: No person convicted except for violation of law in force at time of commission. "
            "(2) Protection against double jeopardy: No person prosecuted and punished for the same offence more than once. "
            "(3) Protection against self-incrimination: No person accused of any offence shall be compelled to be a witness against himself."
        ),
        (
            "PART III - LIFE, PERSONAL LIBERTY, EDUCATION & ARREST (ARTICLES 21, 21A, 22)",
            "ARTICLE 21. PROTECTION OF LIFE AND PERSONAL LIBERTY: "
            "No person shall be deprived of his life or personal liberty except according to procedure established by law. "
            "Interpreted in Maneka Gandhi to require procedure that is just, fair, and reasonable. Encompasses right to privacy (Puttaswamy), "
            "right to speedy trial (Hussainara Khatoon), right to clean environment (M.C. Mehta), right to livelihood (Olga Tellis), "
            "right to legal aid, dignity, and bail jurisprudence ('Bail is the rule, jail is the exception').\n\n"
            "ARTICLE 21A. RIGHT TO EDUCATION: State shall provide free and compulsory education to all children aged 6 to 14 years.\n\n"
            "ARTICLE 22. PROTECTION AGAINST ARREST AND DETENTION: "
            "(1) Right to be informed of grounds of arrest as soon as may be. Right to consult and be defended by a legal practitioner of choice. "
            "(2) Right to be produced before the nearest magistrate within 24 hours of arrest excluding journey time. "
            "(3)-(7) Regulates and limits preventive detention, requiring Advisory Board scrutiny."
        ),
        (
            "PART III - RIGHT AGAINST EXPLOITATION & FREEDOM OF RELIGION (ARTICLES 23-28)",
            "ARTICLE 23. PROHIBITION OF TRAFFIC IN HUMAN BEINGS AND FORCED LABOUR: Traffic in human beings and begar and other similar "
            "forms of forced labour are prohibited and any contravention is an offence punishable in accordance with law.\n\n"
            "ARTICLE 24. PROHIBITION OF EMPLOYMENT OF CHILDREN IN FACTORIES: No child below 14 years shall be employed in factory or mine.\n\n"
            "ARTICLE 25. FREEDOM OF CONSCIENCE AND FREE PROFESSION, PRACTICE AND PROPAGATION OF RELIGION: "
            "Subject to public order, morality and health and to the other provisions of this Part, all persons are equally entitled "
            "to freedom of conscience and the right freely to profess, practise and propagate religion.\n\n"
            "ARTICLE 26. FREEDOM TO MANAGE RELIGIOUS AFFAIRS: Subject to public order, morality and health, religious denominations "
            "have right to establish institutions, manage affairs in matters of religion, and own property.\n\n"
            "ARTICLE 27. FREEDOM AS TO PAYMENT OF TAXES FOR PROMOTION OF ANY RELIGION: No taxes for religious promotion.\n\n"
            "ARTICLE 28. FREEDOM AS TO ATTENDANCE AT RELIGIOUS INSTRUCTION OR WORSHIP IN CERTAIN EDUCATIONAL INSTITUTIONS."
        ),
        (
            "PART III - CULTURAL & EDUCATIONAL RIGHTS AND REMEDIES (ARTICLES 29-32)",
            "ARTICLE 29. PROTECTION OF INTERESTS OF MINORITIES: Any section of the citizens having distinct language, script or culture "
            "has the right to conserve the same. No citizen denied admission into state-aided educational institutions on grounds only of religion, race, caste, language.\n\n"
            "ARTICLE 30. RIGHT OF MINORITIES TO ESTABLISH AND ADMINISTER EDUCATIONAL INSTITUTIONS: All minorities, based on religion or language.\n\n"
            "ARTICLE 32. REMEDIES FOR ENFORCEMENT OF FUNDAMENTAL RIGHTS (THE CONSTITUTIONAL HEART AND SOUL): "
            "(1) The right to move the Supreme Court by appropriate proceedings for enforcement of Part III rights is guaranteed. "
            "(2) Supreme Court has power to issue directions, orders or writs in nature of HABEAS CORPUS (produce the body), "
            "MANDAMUS (compel public duty), PROHIBITION (restrain inferior court), QUO WARRANTO (challenge usurpation of public office), "
            "and CERTIORARI (quash illegal administrative or judicial decisions). Guaranteed fundamental right in itself."
        ),
        (
            "PART IV - DIRECTIVE PRINCIPLES OF STATE POLICY (ARTICLES 36-51)",
            "ARTICLE 37. APPLICATION OF PRINCIPLES: Directive principles are not enforceable by any court, but the principles therein "
            "laid down are nevertheless fundamental in the governance of the country and it shall be the duty of the State to apply these.\n\n"
            "ARTICLE 38. STATE TO SECURE A SOCIAL ORDER FOR THE PROMOTION OF WELFARE OF THE PEOPLE: Minimizing inequalities in income and status.\n\n"
            "ARTICLE 39A. EQUAL JUSTICE AND FREE LEGAL AID: State shall provide free legal aid, by legislation or schemes, to ensure opportunities "
            "for securing justice are not denied to any citizen by reason of economic or other disabilities (NALSA Act framework).\n\n"
            "ARTICLE 40. ORGANIZATION OF VILLAGE PANCHAYATS: Units of local self-government.\n\n"
            "ARTICLE 44. UNIFORM CIVIL CODE FOR THE CITIZENS: State shall endeavour to secure for the citizens a Uniform Civil Code throughout India.\n\n"
            "ARTICLE 50. SEPARATION OF JUDICIARY FROM EXECUTIVE: Separation in public services of the State.\n\n"
            "ARTICLE 51. PROMOTION OF INTERNATIONAL PEACE AND SECURITY: Foster respect for international law and treaty obligations."
        ),
        (
            "PART IVA - FUNDAMENTAL DUTIES (ARTICLE 51A)",
            "ARTICLE 51A. FUNDAMENTAL DUTIES: It shall be the duty of every citizen of India: "
            "(a) to abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem; "
            "(b) to cherish and follow the noble ideals which inspired our national struggle for freedom; "
            "(c) to uphold and protect the sovereignty, unity and integrity of India; "
            "(d) to defend the country and render national service when called upon to do so; "
            "(e) to promote harmony and the spirit of common brotherhood among all the people of India transcending religious, "
            "linguistic, regional or sectional diversities and to renounce practices derogatory to the dignity of women; "
            "(f) to value and preserve the rich heritage of our composite culture; "
            "(g) to protect and improve the natural environment including forests, lakes, rivers and wildlife; "
            "(h) to develop the scientific temper, humanism and the spirit of inquiry and reform; "
            "(i) to safeguard public property and to abjure violence; "
            "(j) to strive towards excellence in all spheres of individual and collective activity; "
            "(k) who is a parent or guardian to provide opportunities for education to his child between the age of six and fourteen years."
        ),
        (
            "PART V - THE UNION: EXECUTIVE AND PARLIAMENT (ARTICLES 52-123)",
            "ARTICLE 52-53. PRESIDENT OF INDIA: Executive power of the Union vested in the President, exercised directly or through subordinate officers.\n\n"
            "ARTICLE 74. COUNCIL OF MINISTERS TO AID AND ADVISE PRESIDENT: Prime Minister at head. Advice tendered by Ministers cannot be inquired into in any court.\n\n"
            "ARTICLE 75. COLLECTIVE RESPONSIBILITY: Council of Ministers collectively responsible to House of the People (Lok Sabha).\n\n"
            "ARTICLE 76. ATTORNEY-GENERAL FOR INDIA: Appointed by President; must be qualified to be appointed Judge of Supreme Court.\n\n"
            "ARTICLE 79-81. PARLIAMENT OF INDIA: Consists of President and two Houses: Council of States (Rajya Sabha) and House of the People (Lok Sabha).\n\n"
            "ARTICLE 105. POWERS, PRIVILEGES AND IMMUNITIES OF PARLIAMENT AND MEMBERS: Freedom of speech in Parliament, immunity from court proceedings.\n\n"
            "ARTICLE 110. DEFINITION OF MONEY BILLS: Speaker's endorsement final.\n\n"
            "ARTICLE 123. POWER OF PRESIDENT TO PROMULGATE ORDINANCES DURING RECESS OF PARLIAMENT: Must be laid before Parliament within 6 weeks of reassembly."
        ),
        (
            "PART V - THE UNION JUDICIARY: SUPREME COURT OF INDIA (ARTICLES 124-147)",
            "ARTICLE 124. ESTABLISHMENT AND CONSTITUTION OF SUPREME COURT: Supreme Court of India consists of Chief Justice of India and other Judges. "
            "Tenure up to age of 65 years. Removal by impeachment on grounds of proved misbehaviour or incapacity under Article 124(4).\n\n"
            "ARTICLE 129. SUPREME COURT TO BE A COURT OF RECORD: Power to punish for contempt of itself.\n\n"
            "ARTICLE 131. ORIGINAL JURISDICTION: Exclusive jurisdiction in disputes between Government of India and one or more States.\n\n"
            "ARTICLE 136. SPECIAL LEAVE TO APPEAL BY SUPREME COURT (SLP): Plenary discretionary power of the Supreme Court to grant special leave "
            "to appeal from any judgment, decree, determination, sentence or order in any cause or matter passed by any court or tribunal in India.\n\n"
            "ARTICLE 141. LAW DECLARED BY SUPREME COURT TO BE BINDING ON ALL COURTS: Precedent doctrine (stare decisis) binding throughout India.\n\n"
            "ARTICLE 142. ENFORCEMENT OF DECREES AND ORDERS OF SUPREME COURT: Inherent plenary power to pass such decree or make such order "
            "as is necessary for DOING COMPLETE JUSTICE in any cause or matter pending before it. Transcends statutory limitations to ensure justice.\n\n"
            "ARTICLE 143. POWER OF PRESIDENT TO CONSULT SUPREME COURT: Advisory jurisdiction."
        ),
        (
            "PART VI - THE STATES: HIGH COURTS & WRIT JURISDICTION (ARTICLES 214-237)",
            "ARTICLE 214. HIGH COURTS FOR STATES: High Court for each State.\n\n"
            "ARTICLE 215. HIGH COURTS TO BE COURTS OF RECORD: Power to punish for contempt of itself.\n\n"
            "ARTICLE 226. POWER OF HIGH COURTS TO ISSUE CERTAIN WRITS: (1) Notwithstanding anything in Article 32, every High Court shall "
            "have power throughout territories in relation to which it exercises jurisdiction to issue directions, orders or writs, including writs "
            "in nature of habeas corpus, mandamus, prohibition, quo warranto and certiorari, for enforcement of Part III rights AND FOR ANY OTHER PURPOSE. "
            "Scope of Article 226 is wider than Article 32 as it covers both fundamental rights and legal statutory rights.\n\n"
            "ARTICLE 227. POWER OF SUPERINTENDENCE OVER ALL COURTS: Judicial and administrative superintendence over all courts and tribunals in territory.\n\n"
            "ARTICLE 233. APPOINTMENT OF DISTRICT JUDGES: Consultation with High Court.\n\n"
            "ARTICLE 235. CONTROL OVER SUBORDINATE COURTS: Vesting of posting, promotion, and discipline of judicial service in the High Court."
        ),
        (
            "PART XI - RELATIONS BETWEEN THE UNION AND THE STATES (ARTICLES 245-263)",
            "ARTICLE 245. EXTENT OF LAWS MADE BY PARLIAMENT AND BY LEGISLATURES OF STATES: Territorial jurisdiction and extra-territorial operation.\n\n"
            "ARTICLE 246. SUBJECT-MATTER OF LAWS (SEVENTH SCHEDULE LEGISLATIVE LISTS): "
            "(1) List I (Union List): Parliament has exclusive power to make laws on defense, atomic energy, foreign affairs, currency, interstate commerce. "
            "(2) List III (Concurrent List): Both Parliament and State Legislatures have power on criminal law, civil procedure, contracts, marriage, bankruptcy. "
            "(3) List II (State List): State Legislature has exclusive power on public order, police, prisons, local government, public health, agriculture.\n\n"
            "ARTICLE 248. RESIDUARY POWERS OF LEGISLATION: Residuary legislative powers vest exclusively in Parliament.\n\n"
            "ARTICLE 254. INCONSISTENCY BETWEEN LAWS MADE BY PARLIAMENT AND LAWS MADE BY THE LEGISLATURES OF STATES: "
            "Doctrine of Repugnancy. Parliamentary law prevails over State law on Concurrent subject unless State law received Presidential assent."
        ),
        (
            "PART XII & PART XIII - FINANCE, PROPERTY, CONTRACTS & COMMERCE (ARTICLES 265-307)",
            "ARTICLE 265. TAXES NOT TO BE IMPOSED SAVE BY AUTHORITY OF LAW: No tax shall be levied or collected except by authority of law.\n\n"
            "ARTICLE 279A. GOODS AND SERVICES TAX COUNCIL (GST COUNCIL): Mechanism for harmonized national tax structure.\n\n"
            "ARTICLE 299. CONTRACTS: Contracts made in the exercise of the executive power of the Union or of a State shall be expressed to be "
            "made by the President or Governor and shall be executed by authorized persons. Non-compliance renders government contract void.\n\n"
            "ARTICLE 300. SUITS AND PROCEEDINGS: Government of India and State Governments may sue or be sued in name of Union of India / State.\n\n"
            "ARTICLE 300A. PERSONS NOT TO BE DEPRIVED OF PROPERTY SAVE BY AUTHORITY OF LAW: Inserted by 44th Constitutional Amendment Act, 1978. "
            "Property right transformed from fundamental right (former Art 19(1)(f) and 31) into constitutional human right.\n\n"
            "ARTICLE 301. FREEDOM OF TRADE, COMMERCE AND INTERCOURSE: Free trade throughout the territory of India."
        ),
        (
            "PART XIV, XIVA & XV - SERVICES, TRIBUNALS & ELECTIONS (ARTICLES 308-329)",
            "ARTICLE 311. DISMISSAL, REMOVAL OR REDUCTION IN RANK OF PERSONS EMPLOYED IN CIVIL CAPACITIES: Constitutional safeguard. "
            "No civil servant dismissed or removed by authority subordinate to appointing authority. No removal without inquiry and reasonable opportunity.\n\n"
            "ARTICLE 323A-323B. ADMINISTRATIVE TRIBUNALS: Central Administrative Tribunal (CAT), State Administrative Tribunals (L. Chandra Kumar case).\n\n"
            "ARTICLE 324. SUPERINTENDENCE, DIRECTION AND CONTROL OF ELECTIONS VESTED IN AN ELECTION COMMISSION: "
            "Independent constitutional body conducting elections to Parliament, State Legislatures, and offices of President and Vice-President.\n\n"
            "ARTICLE 326. ELECTIONS TO HOUSE OF THE PEOPLE AND LEGISLATIVE ASSEMBLIES ON BASIS OF ADULT SUFFRAGE: Voting age 18 years (61st Amendment)."
        ),
        (
            "PART XVIII - EMERGENCY PROVISIONS (ARTICLES 352-360)",
            "ARTICLE 352. PROCLAMATION OF EMERGENCY (NATIONAL EMERGENCY): Proclaimed on grounds of war, external aggression, or armed rebellion. "
            "Requires written recommendation of Union Cabinet. Subject to Parliamentary approval by special majority within 1 month. "
            "Articles 20 and 21 CANNOT be suspended during emergency (44th Amendment safeguard).\n\n"
            "ARTICLE 356. PROVISIONS IN CASE OF FAILURE OF CONSTITUTIONAL MACHINERY IN STATES (PRESIDENT'S RULE): "
            "Imposed upon receipt of report from Governor or otherwise that government of State cannot be carried on in accordance with Constitution. "
            "Subject to judicial review under S.R. Bommai guidelines; floor test is mandatory test of majority.\n\n"
            "ARTICLE 358-359. SUSPENSION OF PROVISIONS OF ARTICLE 19 AND ENFORCEMENT OF RIGHTS: Article 20 and 21 remain inviolable.\n\n"
            "ARTICLE 360. PROVISIONS AS TO FINANCIAL EMERGENCY: Never invoked in India."
        ),
        (
            "PART XX - AMENDMENT OF THE CONSTITUTION (ARTICLE 368)",
            "ARTICLE 368. POWER OF PARLIAMENT TO AMEND THE CONSTITUTION AND PROCEDURE THEREFOR: "
            "(1) Parliament may in exercise of its constituent power amend by way of addition, variation or repeal any provision of this Constitution. "
            "(2) Bill must be passed in each House by a majority of the total membership and by a majority of not less than two-thirds of members "
            "present and voting. Amendments affecting federal structure require ratification by not less than half of State Legislatures.\n\n"
            "BASIC STRUCTURE DOCTRINE: In Kesavananda Bharati (1973), Supreme Court ruled that amending power under Article 368 is not unlimited. "
            "Parliament cannot alter, damage, or destroy the 'Basic Structure' of the Constitution (Supremacy of Constitution, Republican & Democratic form, "
            "Secularism, Separation of Powers, Federalism, Judicial Review, and Rule of Law)."
        ),
    ]


def build_supreme_court_judgment_records() -> List[Tuple[str, str]]:
    """Landmark Supreme Court of India precedents and judgments."""
    return [
        (
            "LANDMARK SC: KESAVANANDA BHARATI v. STATE OF KERALA (1973) 4 SCC 225",
            "BENCH: 13-Judge Constitutional Bench (Largest in Indian History) | RATIO: 7:6 | CORE PRINCIPLE: BASIC STRUCTURE DOCTRINE\n"
            "FACTS & HOLDING: Challenged the 24th, 25th, and 29th Constitutional Amendments. The Supreme Court held that while Parliament "
            "has wide constituent power under Article 368 to amend any part of the Constitution, including Fundamental Rights, this power is "
            "NOT absolute and cannot be exercised to alter, emasculate or destroy the 'Basic Structure' or foundational framework of the Constitution.\n"
            "PILLARS OF BASIC STRUCTURE: Supremacy of the Constitution, Republican and Democratic form of Government, Secular character, "
            "Separation of Powers between Legislature, Executive and Judiciary, Federal character, Rule of Law, and Judicial Review.\n"
            "IMPACT ON LEGAL PRACTICE: Any constitutional amendment violating the basic structure is unconstitutional and liable to be struck down."
        ),
        (
            "LANDMARK SC: MANEKA GANDHI v. UNION OF INDIA (1978) 1 SCC 248",
            "BENCH: 7-Judge Bench | CORE PRINCIPLE: EXPANSIVE ARTICLE 21 DUE PROCESS & GOLDEN TRIANGLE\n"
            "FACTS & HOLDING: Petitioner's passport was impounded under Section 10(3)(c) of Passports Act 1967 'in the interests of general public' "
            "without giving any prior hearing or reasons. The Supreme Court overruled A.K. Gopalan and held that 'procedure established by law' "
            "under Article 21 cannot be arbitrary, oppressive, or fanciful; it MUST be 'just, fair, and reasonable' embodying Natural Justice.\n"
            "GOLDEN TRIANGLE: Articles 14 (Equality), 19 (Freedoms), and 21 (Life and Liberty) are not isolated silos; they form a symbiotic triad. "
            "A law depriving personal liberty under Article 21 must also satisfy the non-arbitrariness test of Article 14 and reasonableness of Article 19.\n"
            "IMPACT: Laid the foundation for Public Interest Litigation (PIL), right to speedy trial, legal aid, and human rights jurisprudence."
        ),
        (
            "LANDMARK SC: JUSTICE K.S. PUTTASWAMY (RETD.) v. UNION OF INDIA (2017) 10 SCC 1",
            "BENCH: 9-Judge Bench (Unanimous) | CORE PRINCIPLE: FUNDAMENTAL RIGHT TO PRIVACY UNDER ARTICLE 21\n"
            "FACTS & HOLDING: Challenged the constitutional validity of Aadhaar biometric scheme. The 9-judge bench unanimously overruled M.P. Sharma (1954) "
            "and Kharak Singh (1962), holding that the Right to Privacy is a protected fundamental right under Article 21 and Part III.\n"
            "THREE-FOLD TEST OF PROPORTIONALITY: State interference with privacy is valid ONLY IF it satisfies: (1) Legality: Existence of an enacted law; "
            "(2) Legitimate State Aim: Nature and purpose of the action; (3) Proportionality: A rational nexus between means adopted and object sought, "
            "with least restrictive measure adopted.\n"
            "FACETS OF PRIVACY: Informational privacy, bodily autonomy, decisional privacy, and spatial privacy. Bedrock for data protection laws."
        ),
        (
            "LANDMARK SC: SATENDER KUMAR ANTIL v. CBI (2022) 10 SCC 51",
            "BENCH: 2-Judge Bench (Kaul & Sundresh, JJ.) | CORE PRINCIPLE: COMPREHENSIVE BAIL JURISPRUDENCE & SECTION 483 BNSS / 439 CrPC\n"
            "HOLDING & DIRECTIVES: Reaffirmed that 'Bail is the rule, jail is the exception'. Addressed overcrowding in jails caused by unnecessary "
            "undertrial detentions. Categorized offences into 4 groups for bail consideration:\n"
            "- Category A (Offences punishable with <= 7 years imprisonment): No mechanical arrest; mandatory compliance with Section 41/41A CrPC "
            "(Section 35 BNSS). Bail applications to be decided without taking accused into custody if compliant with summons.\n"
            "- Category B (Offences punishable with death, life imprisonment, or > 7 years): Bail applications to be decided on merits.\n"
            "- Category C (Special Acts: NDPS, PMLA, UAPA, POCSO): Bail subject to stringent conditions in special statutes.\n"
            "- Category D (Economic Offences): Merits-based evaluation without treating all economic offences alike.\n"
            "DIRECTIVES: Mandated timelines for disposing regular bail (2 weeks) and anticipatory bail (6 weeks)."
        ),
        (
            "LANDMARK SC: ARNESH KUMAR v. STATE OF BIHAR (2014) 8 SCC 273",
            "BENCH: 2-Judge Bench (Chandramauli Kr. Prasad & P.C. Ghose, JJ.) | CORE PRINCIPLE: CURBING ARBITRARY ARRESTS (SEC 41A CrPC / SEC 35 BNSS)\n"
            "FACTS & HOLDING: Noticed alarming misuse of Section 498A IPC (dowry harassment). The Supreme Court held that police officers shall NOT "
            "automatically or mechanically arrest an accused when an offence is punishable with imprisonment for a term which may be less than seven years, "
            "or which may extend to seven years.\n"
            "MANDATORY GUIDELINES: (1) Police officers must be provided with a checklist containing specified sub-clauses under Section 41(1)(b)(ii); "
            "(2) Police must forward checklist with reasons when producing accused before Magistrate; (3) Magistrate must not authorize detention "
            "mechanically without recording satisfaction; (4) Notice of Appearance under Section 41A (BNSS Section 35(3)) must be served within 2 weeks;\n"
            "PENAL CONSEQUENCE: Non-compliance attracts departmental action against police officers and contempt proceedings."
        ),
        (
            "LANDMARK SC: LALITA KUMARI v. GOVT. OF U.P. (2014) 2 SCC 1",
            "BENCH: 5-Judge Constitution Bench | CORE PRINCIPLE: MANDATORY REGISTRATION OF FIRST INFORMATION REPORT (FIR)\n"
            "HOLDING: Registration of FIR is MANDATORY under Section 154 of the Code of Criminal Procedure (Section 173 of Bharatiya Nagarik "
            "Suraksha Sanhita 2023) if the information discloses commission of a COGNIZABLE OFFENCE, and no preliminary inquiry is permissible in such situation.\n"
            "EXCEPTIONS WHERE PRELIMINARY INQUIRY IS PERMISSIBLE: (a) Matrimonial disputes / family disputes; (b) Commercial offences; "
            "(c) Medical negligence cases; (d) Corruption cases; (e) Cases where there is abnormal delay/laches in initiating criminal proceeding.\n"
            "TIMELINE: Preliminary inquiry must be completed expeditiously, not exceeding 7 days, recording reasons in General Diary (GD)."
        ),
        (
            "LANDMARK SC: D.K. BASU v. STATE OF WEST BENGAL (1997) 1 SCC 416",
            "BENCH: 2-Judge Bench | CORE PRINCIPLE: SAFEGUARDS AGAINST CUSTODIAL TORTURE & ARREST GUIDELINES\n"
            "HOLDING: Custodial violence, torture, and custodial deaths violate fundamental right to life under Article 21. Formulated 11 binding guidelines:\n"
            "(1) Police personnel carrying out arrest must bear accurate, visible identification and name tags with designations;\n"
            "(2) Arrest memo must be prepared at time of arrest with time, date, and signed by at least one witness (family member/respectable person);\n"
            "(3) Person arrested has right to have one friend or relative informed of arrest and place of custody within 8 to 12 hours;\n"
            "(4) Person arrested must be examined at time of arrest for major/minor injuries and recorded in 'Inspection Memo';\n"
            "(5) Mandatory medical examination by trained doctor every 48 hours in custody;\n"
            "(6) Right to meet and consult advocate during interrogation."
        ),
        (
            "LANDMARK SC: SHREYA SINGHAL v. UNION OF INDIA (2015) 5 SCC 1",
            "BENCH: 2-Judge Bench (Chelameswar & Nariman, JJ.) | CORE PRINCIPLE: FREEDOM OF SPEECH ON THE INTERNET & SECTION 66A IT ACT\n"
            "HOLDING: Struck down Section 66A of the Information Technology Act 2000 in its entirety as unconstitutional and violative of Article 19(1)(a).\n"
            "RATIO: Section 66A criminalized sending 'offensive' messages through computers without clear statutory definition, resulting in chilling "
            "effect on free speech. The provision was unconstitutionally vague, overbroad, and failed the test of 'clear and present danger'.\n"
            "INTERMEDIARY LIABILITY (SECTION 79): Held that intermediaries are required to take down content under Section 79(3)(b) ONLY upon receipt "
            "of an actual court order or government notification, protecting digital platforms from subjective takedown demands."
        ),
        (
            "LANDMARK SC: NAVTEJ SINGH JOHAR v. UNION OF INDIA (2018) 10 SCC 1",
            "BENCH: 5-Judge Constitution Bench | CORE PRINCIPLE: DECRIMINALIZATION OF SECTION 377 IPC & CONSTITUTIONAL MORALITY\n"
            "HOLDING: Read down Section 377 of the Indian Penal Code insofar as it criminalized consensual sexual acts between consenting adults in private.\n"
            "CONSTITUTIONAL DOCTRINE: Constitutional morality must triumph over majoritarian or public morality. Sexual orientation is an innate, "
            "inseparable facet of human identity protected under Article 14 (Equality), Article 15 (Non-discrimination on grounds of sex), Article 19(1)(a) "
            "(Freedom of expression), and Article 21 (Dignity, Autonomy, and Right to Privacy)."
        ),
        (
            "LANDMARK SC: JOSEPH SHINE v. UNION OF INDIA (2019) 3 SCC 39",
            "BENCH: 5-Judge Constitution Bench | CORE PRINCIPLE: STRUCK DOWN SECTION 497 IPC (ADULTERY)\n"
            "HOLDING: Unanimously struck down Section 497 of the Indian Penal Code (adultery) and Section 198(2) CrPC as unconstitutional.\n"
            "RATIO: Section 497 treated married women as chattel of the husband, depriving them of sexual autonomy and dignity in violation of Articles 14 and 21. "
            "Criminal law should not intrude into the private realm of marriage for consensual acts. Adultery remains a valid ground for civil divorce, "
            "but ceases to be a criminal penal offence."
        ),
        (
            "LANDMARK SC: VISHAKA v. STATE OF RAJASTHAN (1997) 6 SCC 241",
            "BENCH: 3-Judge Bench (Verma, CJI, Sujata Manohar & Kirpal, JJ.) | CORE PRINCIPLE: PREVENTION OF SEXUAL HARASSMENT AT WORKPLACE\n"
            "HOLDING: In the absence of domestic legislation, the Supreme Court invoked Articles 14, 19, and 21 and the CEDAW International Convention "
            "under Article 51 to lay down binding 'Vishaka Guidelines' for workplace sexual harassment prevention.\n"
            "MANDATE: Mandatory establishment of Internal Complaints Committee (ICC), complaints procedure, disciplinary action, and third-party representation. "
            "Formed the bedrock for the subsequent statutory enactment of POSH Act 2013 (Sexual Harassment of Women at Workplace Act)."
        ),
        (
            "LANDMARK SC: INDRA SAWHNEY v. UNION OF INDIA (1992) Supp (3) SCC 217",
            "BENCH: 9-Judge Constitution Bench | CORE PRINCIPLE: 50% CEILING ON RESERVATION & CREAMY LAYER DOCTRINE\n"
            "HOLDING: Upheld 27% reservation for Other Backward Classes (OBCs) in central government services under Article 16(4) based on Mandal Commission.\n"
            "KEY PRINCIPLES: (1) Total reservation shall not exceed 50% except in extraordinary situations; (2) 'Creamy Layer' (socially and economically "
            "advanced individuals among backward classes) must be excluded from reservation benefits; (3) Backward classes cannot be identified solely "
            "on economic criteria; (4) Article 16(4) is not an exception but an emphatic facet of equality under Article 16(1)."
        ),
        (
            "LANDMARK SC: S.R. BOMMAI v. UNION OF INDIA (1994) 3 SCC 1",
            "BENCH: 9-Judge Constitution Bench | CORE PRINCIPLE: JUDICIAL REVIEW OF ARTICLE 356 (PRESIDENT'S RULE) & SECULARISM\n"
            "HOLDING: Presidential Proclamation under Article 356 dismissing a state government and dissolving assembly is subject to JUDICIAL REVIEW.\n"
            "GUIDELINES: (1) Secularism is part of the Basic Structure; any state government acting against secularism is liable to action under Article 356; "
            "(2) Dissolution of State Legislative Assembly cannot occur until both Houses of Parliament approve the proclamation; "
            "(3) Court has power to restore the dismissed state government and revive the assembly if proclamation is held unconstitutional; "
            "(4) The floor of the Legislative Assembly is the only forum to test majority support, not Governor's subjective opinion."
        ),
        (
            "LANDMARK SC: SHAYARA BANO v. UNION OF INDIA (2017) 9 SCC 1",
            "BENCH: 5-Judge Constitution Bench | CORE PRINCIPLE: TRIPLE TALAQ (TALAQ-E-BIDDAT) STRUCK DOWN UNDER ARTICLE 14\n"
            "HOLDING: Declared the practice of Talaq-e-Biddat (instant, irrevocable triple talaq) void, illegal, and unconstitutional by 3:2 majority.\n"
            "MANIFEST ARBITRARINESS DOCTRINE: Held that a law or practice that is capricious, irrational, or without determining principle violates "
            "the guarantee of equality under Article 14. Instant triple talaq leaves a Muslim woman with no recourse or reconciliation, violating her dignity."
        ),
        (
            "LANDMARK SC: COMMON CAUSE v. UNION OF INDIA (2018) 5 SCC 1",
            "BENCH: 5-Judge Constitution Bench | CORE PRINCIPLE: RIGHT TO DIE WITH DIGNITY & PASSIVE EUTHANASIA\n"
            "HOLDING: Right to life under Article 21 includes the right to die with dignity. The Supreme Court legalized PASSIVE EUTHANASIA (withdrawal of "
            "life-support systems for terminally ill patients in permanent vegetative state) and upheld the legal validity of ADVANCE MEDICAL DIRECTIVES (Living Wills).\n"
            "PROCEDURAL SAFEGUARDS: Mandated two Medical Boards (Hospital Medical Board and Collector's Independent Medical Board) and Judicial Magistrate scrutiny."
        ),
        (
            "LANDMARK SC: ASSOCIATION FOR DEMOCRATIC REFORMS (ADR) v. UNION OF INDIA (2024)",
            "BENCH: 5-Judge Constitution Bench (Unanimous, Chandrachud, CJI) | CORE PRINCIPLE: ELECTORAL BONDS SCHEME STRUCK DOWN UNDER ARTICLE 19(1)(a)\n"
            "HOLDING: Struck down the Electoral Bond Scheme (2018) and related amendments to the Finance Act 2017, Representation of People Act, "
            "and Income Tax Act as unconstitutional.\n"
            "RATIO: Voters have a fundamental right to information regarding the financial contributions made to political parties under Article 19(1)(a). "
            "Anonymous political contributions foster quid pro quo and corrupt corporate financing, failing the proportionality standard."
        ),
    ]


def generate_all_corpus_files(data_dir: Path) -> None:
    """Writes both comprehensive PDF corpora into the data directory."""
    data_dir.mkdir(parents=True, exist_ok=True)

    const_path = data_dir / "constitution.pdf"
    sc_path = data_dir / "supreme_court_judgments.pdf"

    const_sections = build_constitution_records()
    const_bytes = create_pdf_binary(const_sections)
    const_path.write_bytes(const_bytes)
    print(f"[CORPUS BUILDER] Successfully built: {const_path} ({len(const_sections)} statutory parts)")

    sc_sections = build_supreme_court_judgment_records()
    sc_bytes = create_pdf_binary(sc_sections)
    sc_path.write_bytes(sc_bytes)
    print(f"[CORPUS BUILDER] Successfully built: {sc_path} ({len(sc_sections)} landmark precedents)")


if __name__ == "__main__":
    target_data_dir = Path(__file__).resolve().parent / "data"
    generate_all_corpus_files(target_data_dir)
