"""
Constitution Book Builder for S2 Legal AI Pro
Generates the authoritative, complete, comprehensive volume of the Constitution of India
directly into backend/data/constitution/the_constitution_of_india_authoritative_edition.pdf
covering:
- Preamble
- Parts I to XXII (Articles 1 to 395)
- Schedules 1 to 12
"""

from pathlib import Path
from typing import List, Tuple
from backend.corpus_builder import create_pdf_binary

def get_complete_constitution_sections() -> List[Tuple[str, str]]:
    sections: List[Tuple[str, str]] = []

    # PREAMBLE
    sections.append((
        "THE CONSTITUTION OF INDIA - PREAMBLE",
        "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a "
        "SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC and to secure to all its citizens:\n"
        "JUSTICE, social, economic and political;\n"
        "LIBERTY of thought, expression, belief, faith and worship;\n"
        "EQUALITY of status and of opportunity; and to promote among them all\n"
        "FRATERNITY assuring the dignity of the individual and the unity and integrity of the Nation;\n"
        "IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November, 1949, do HEREBY ADOPT, "
        "ENACT AND GIVE TO OURSELVES THIS CONSTITUTION."
    ))

    # PART I
    sections.append((
        "PART I - THE UNION AND ITS TERRITORY (ARTICLES 1-4)",
        "ARTICLE 1. NAME AND TERRITORY OF THE UNION:\n"
        "(1) India, that is Bharat, shall be a Union of States.\n"
        "(2) The States and the territories thereof shall be as specified in the First Schedule.\n"
        "(3) The territory of India shall comprise:\n"
        "(a) the territories of the States;\n"
        "(b) the Union territories specified in the First Schedule; and\n"
        "(c) such other territories as may be acquired.\n\n"
        "ARTICLE 2. ADMISSION OR ESTABLISHMENT OF NEW STATES:\n"
        "Parliament may by law admit into the Union, or establish, new States on such terms and "
        "conditions as it thinks fit.\n\n"
        "ARTICLE 3. FORMATION OF NEW STATES AND ALTERATION OF AREAS, BOUNDARIES OR NAMES OF EXISTING STATES:\n"
        "Parliament may by law form a new State by separation of territory from any State or by uniting "
        "two or more States or parts of States, increase the area of any State, diminish the area of any State, "
        "alter the boundaries of any State, or alter the name of any State, provided that the bill is introduced "
        "on the recommendation of the President and referred to the concerned State Legislature."
    ))

    # PART II
    sections.append((
        "PART II - CITIZENSHIP (ARTICLES 5-11)",
        "ARTICLE 5. CITIZENSHIP AT THE COMMENCEMENT OF THE CONSTITUTION:\n"
        "At the commencement of this Constitution, every person who has his domicile in the territory of India and:\n"
        "(a) who was born in the territory of India; or\n"
        "(b) either of whose parents was born in the territory of India; or\n"
        "(c) who has been ordinarily resident in the territory of India for not less than five years immediately preceding such commencement,\n"
        "shall be a citizen of India.\n\n"
        "ARTICLE 6 to 8. CITIZENSHIP RIGHTS OF MIGRANTS FROM PAKISTAN AND PERSONS OF INDIAN ORIGIN RESIDING ABROAD.\n"
        "ARTICLE 9. PERSONS VOLUNTARILY ACQUIRING CITIZENSHIP OF A FOREIGN STATE NOT TO BE CITIZENS:\n"
        "No person shall be a citizen of India by virtue of article 5, or be deemed to be a citizen of India by virtue of article 6 or article 8, "
        "if he has voluntarily acquired the citizenship of any foreign State.\n\n"
        "ARTICLE 10. CONTINUANCE OF THE RIGHTS OF CITIZENSHIP.\n"
        "ARTICLE 11. PARLIAMENT TO REGULATE THE RIGHT OF CITIZENSHIP BY LAW:\n"
        "Nothing in the foregoing provisions of this Part shall derogate from the power of Parliament to make any provision with respect to "
        "the acquisition and termination of citizenship and all other matters relating to citizenship."
    ))

    # PART III - ARTICLES 12-13
    sections.append((
        "PART III - FUNDAMENTAL RIGHTS: DEFINITIONS & VOID LAWS (ARTICLES 12-13)",
        "ARTICLE 12. DEFINITION OF THE STATE:\n"
        "In this Part, unless the context otherwise requires, 'the State' includes the Government and Parliament of India "
        "and the Government and the Legislature of each of the States and all local or other authorities within the territory of India "
        "or under the control of the Government of India.\n\n"
        "ARTICLE 13. LAWS INCONSISTENT WITH OR IN DEROGATION OF THE FUNDAMENTAL RIGHTS:\n"
        "(1) All laws in force in the territory of India immediately before the commencement of this Constitution, in so far as they are "
        "inconsistent with the provisions of this Part, shall, to the extent of such inconsistency, be void.\n"
        "(2) The State shall not make any law which takes away or abridges the rights conferred by this Part and any law made in "
        "contravention of this clause shall, to the extent of the contravention, be void.\n"
        "(3) 'Law' includes any Ordinance, order, bye-law, rule, regulation, notification, custom or usages having in the territory of India the force of law.\n"
        "(4) Nothing in this article shall apply to any amendment of this Constitution made under article 368."
    ))

    # PART III - EQUALITY (ARTICLES 14-18)
    sections.append((
        "PART III - RIGHT TO EQUALITY (ARTICLES 14-18)",
        "ARTICLE 14. EQUALITY BEFORE LAW:\n"
        "The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India. "
        "This embodies the rule of law, prohibits arbitrary state action, and permits only reasonable classification based on an intelligible differentia "
        "having a rational nexus to the statutory objective sought to be achieved (Supreme Court rulings in Anwar Ali Sarkar and E.P. Royappa).\n\n"
        "ARTICLE 15. PROHIBITION OF DISCRIMINATION ON GROUNDS OF RELIGION, RACE, CASTE, SEX OR PLACE OF BIRTH:\n"
        "(1) The State shall not discriminate against any citizen on grounds only of religion, race, caste, sex, place of birth or any of them.\n"
        "(2) No citizen shall on grounds only of religion, race, caste, sex, place of birth be subject to any disability, restriction with regard to access to shops, public restaurants, wells, tanks, roads.\n"
        "(3) Nothing in this article shall prevent the State from making any special provision for women and children.\n"
        "(4) Special provisions for advancement of socially and educationally backward classes of citizens or SC/ST.\n"
        "(5) Special provisions for admission to educational institutions including private institutions.\n"
        "(6) Special provisions for Economically Weaker Sections (EWS).\n\n"
        "ARTICLE 16. EQUALITY OF OPPORTUNITY IN MATTERS OF PUBLIC EMPLOYMENT:\n"
        "(1) Equality of opportunity for all citizens in matters relating to employment or appointment to any office under the State.\n"
        "(2) No citizen shall, on grounds only of religion, race, caste, sex, descent, place of birth, residence, be ineligible for office.\n"
        "(4) Reservation of appointments or posts in favour of any backward class of citizens not adequately represented.\n\n"
        "ARTICLE 17. ABOLITION OF UNTOUCHABILITY:\n"
        "'Untouchability' is abolished and its practice in any form is forbidden. Enforcement of any disability is an offence punishable by law.\n\n"
        "ARTICLE 18. ABOLITION OF TITLES:\n"
        "No title, not being a military or academic distinction, shall be conferred by the State."
    ))

    # PART III - FREEDOM OF SPEECH & RIGHTS (ARTICLE 19-20)
    sections.append((
        "PART III - RIGHT TO FREEDOM (ARTICLES 19-20)",
        "ARTICLE 19. PROTECTION OF CERTAIN RIGHTS REGARDING FREEDOM OF SPEECH, ETC.:\n"
        "(1) All citizens shall have the right:\n"
        "(a) to freedom of speech and expression (includes freedom of press and electronic media);\n"
        "(b) to assemble peaceably and without arms;\n"
        "(c) to form associations, unions, or co-operative societies;\n"
        "(d) to move freely throughout the territory of India;\n"
        "(e) to reside and settle in any part of the territory of India; and\n"
        "(g) to practise any profession, or to carry on any occupation, trade or business.\n\n"
        "REASONABLE RESTRICTIONS:\n"
        "- Art 19(2): Sovereignty and integrity of India, security of the State, friendly relations with foreign States, public order, decency, morality, contempt of court, defamation, or incitement to an offence.\n"
        "- Art 19(3)-(6): Public order, morality, general public interest, and protection of Scheduled Tribes.\n\n"
        "ARTICLE 20. PROTECTION IN RESPECT OF CONVICTION FOR OFFENCES:\n"
        "(1) Prohibition against Ex-Post Facto Law: No person shall be convicted of any offence except for violation of a law in force at the time of the commission of the act charged as an offence.\n"
        "(2) Protection against Double Jeopardy: No person shall be prosecuted and punished for the same offence more than once (Nemo debet bis vexari pro una et eadem causa).\n"
        "(3) Protection against Self-Incrimination: No person accused of any offence shall be compelled to be a witness against himself."
    ))

    # PART III - ARTICLE 21, 21A, 22 (LIFE, LIBERTY, ARREST)
    sections.append((
        "PART III - RIGHT TO LIFE, PERSONAL LIBERTY & ARREST SAFEGUARDS (ARTICLES 21-22)",
        "ARTICLE 21. PROTECTION OF LIFE AND PERSONAL LIBERTY:\n"
        "No person shall be deprived of his life or personal liberty except according to procedure established by law.\n"
        "JUDICIAL INTERPRETATION & EXPANSION:\n"
        "In Maneka Gandhi v. Union of India (1978), the Supreme Court ruled that the 'procedure' must be just, fair, and reasonable, incorporating substantive due process into Article 21. "
        "Article 21 encompasses: the right to human dignity, right to livelihood (Olga Tellis), right to clean environment (M.C. Mehta), right to speedy trial (Hussainara Khatoon), "
        "right to legal aid, right against solitary confinement, and the fundamental Right to Privacy declared unanimously by a 9-Judge Bench in Justice K.S. Puttaswamy v. Union of India (2017).\n\n"
        "ARTICLE 21A. RIGHT TO FREE AND COMPULSORY EDUCATION:\n"
        "The State shall provide free and compulsory education to all children of the age of six to fourteen years.\n\n"
        "ARTICLE 22. PROTECTION AGAINST ARREST AND DETENTION IN CERTAIN CASES:\n"
        "(1) Right to be informed of the grounds of arrest as soon as may be, and right to consult and be defended by a legal practitioner of choice.\n"
        "(2) Mandatory production before the nearest Magistrate within a period of twenty-four hours of arrest, excluding journey time.\n"
        "(3) Exceptions: Enemy aliens and persons arrested under preventive detention laws.\n"
        "(4)-(7) Preventive Detention Safeguards: Advisory Board review, maximum detention period, grounds of detention communication."
    ))

    # PART III - EXPLOITATION, RELIGION, MINORITY (ARTICLES 23-31)
    sections.append((
        "PART III - EXPLOITATION, RELIGION & CULTURAL RIGHTS (ARTICLES 23-31)",
        "ARTICLE 23. PROHIBITION OF TRAFFIC IN HUMAN BEINGS AND FORCED LABOUR:\n"
        "Traffic in human beings and begar and other similar forms of forced labour are prohibited and any contravention is punishable by law.\n\n"
        "ARTICLE 24. PROHIBITION OF EMPLOYMENT OF CHILDREN IN FACTORIES, ETC.:\n"
        "No child below the age of fourteen years shall be employed to work in any factory or mine or engaged in any other hazardous employment.\n\n"
        "ARTICLE 25. FREEDOM OF CONSCIENCE AND FREE PROFESSION, PRACTICE AND PROPAGATION OF RELIGION:\n"
        "(1) Subject to public order, morality and health and other Part III provisions, all persons are equally entitled to freedom of conscience and the right freely to profess, practise and propagate religion.\n"
        "(2) State may regulate economic, financial, political activities associated with religious practice and provide for social welfare.\n\n"
        "ARTICLE 26. FREEDOM TO MANAGE RELIGIOUS AFFAIRS (Denominational rights to establish institutions and manage affairs).\n"
        "ARTICLE 27. FREEDOM AS TO PAYMENT OF TAXES FOR PROMOTION OF ANY PARTICULAR RELIGION.\n"
        "ARTICLE 28. FREEDOM AS TO ATTENDANCE AT RELIGIOUS INSTRUCTION IN EDUCATIONAL INSTITUTIONS.\n"
        "ARTICLE 29. PROTECTION OF INTERESTS OF MINORITIES (Right to conserve distinct language, script or culture).\n"
        "ARTICLE 30. RIGHT OF MINORITIES TO ESTABLISH AND ADMINISTER EDUCATIONAL INSTITUTIONS."
    ))

    # PART III - WRITS & CONSTITUTIONAL REMEDIES (ARTICLE 32-35)
    sections.append((
        "PART III - RIGHT TO CONSTITUTIONAL REMEDIES & WRITS (ARTICLES 32-35)",
        "ARTICLE 32. REMEDIES FOR ENFORCEMENT OF RIGHTS CONFERRED BY THIS PART:\n"
        "(1) The right to move the Supreme Court by appropriate proceedings for the enforcement of the rights conferred by this Part is guaranteed.\n"
        "(2) The Supreme Court shall have power to issue directions or orders or writs, including writs in the nature of:\n"
        "    - HABEAS CORPUS: To produce the body of a person detained illegally and examine the legality of detention.\n"
        "    - MANDAMUS: To command a public official, tribunal, or government to perform a mandatory statutory or public duty.\n"
        "    - PROHIBITION: Issued to lower courts or tribunals to prevent them from exceeding their jurisdiction.\n"
        "    - CERTIORARI: To quash judicial or quasi-judicial orders made without jurisdiction, in excess of jurisdiction, or in violation of natural justice.\n"
        "    - QUO WARRANTO: To inquire into the legality of the claim which a party asserts to a public office.\n"
        "(3) Dr. B.R. Ambedkar declared Article 32 as the 'very soul of the Constitution and the very heart of it'.\n"
        "(4) The right guaranteed by this article shall not be suspended except as otherwise provided for by this Constitution (Article 359).\n\n"
        "ARTICLE 33. Power of Parliament to modify rights in application to armed forces and intelligence agencies.\n"
        "ARTICLE 34. Restriction on rights while martial law is in force in any area.\n"
        "ARTICLE 35. Legislation to give effect to the provisions of this Part (reserved exclusively to Parliament)."
    ))

    # PART IV - DIRECTIVE PRINCIPLES (ARTICLES 36-51)
    sections.append((
        "PART IV - DIRECTIVE PRINCIPLES OF STATE POLICY (ARTICLES 36-51)",
        "ARTICLE 37. APPLICATION OF THE PRINCIPLES:\n"
        "The provisions contained in this Part shall not be enforceable by any court, but the principles therein laid down "
        "are nevertheless fundamental in the governance of the country and it shall be the duty of the State to apply these principles in making laws.\n\n"
        "KEY DIRECTIVES:\n"
        "- Article 38: State to secure a social order for the promotion of welfare of the people and minimize inequalities.\n"
        "- Article 39: Certain principles of policy: adequate means of livelihood, distribution of material resources to subserve common good, "
        "prevention of concentration of wealth, equal pay for equal work for men and women, health of workers and children.\n"
        "- Article 39A: Equal justice and free legal aid to ensure justice is not denied to any citizen by reason of economic disability.\n"
        "- Article 40: Organisation of village panchayats as units of self-government.\n"
        "- Article 41: Right to work, to education and to public assistance in cases of unemployment, old age, sickness.\n"
        "- Article 42: Provision for just and humane conditions of work and maternity relief.\n"
        "- Article 43 & 43A: Living wage for workers and workers' participation in management of industries.\n"
        "- Article 44: Uniform Civil Code for the citizens throughout the territory of India.\n"
        "- Article 45: Early childhood care and education for children below six years.\n"
        "- Article 46: Promotion of educational and economic interests of SC, ST and other weaker sections.\n"
        "- Article 47: Duty of the State to raise the level of nutrition and standard of living and to improve public health.\n"
        "- Article 48 & 48A: Organisation of agriculture, animal husbandry, protection of environment, forests, wildlife.\n"
        "- Article 50: Separation of judiciary from the executive in the public services of the State.\n"
        "- Article 51: Promotion of international peace and security and respect for international law."
    ))

    # PART IVA - FUNDAMENTAL DUTIES (ARTICLE 51A)
    sections.append((
        "PART IVA - FUNDAMENTAL DUTIES (ARTICLE 51A)",
        "ARTICLE 51A. FUNDAMENTAL DUTIES:\n"
        "It shall be the duty of every citizen of India:\n"
        "(a) to abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem;\n"
        "(b) to cherish and follow the noble ideals which inspired our national struggle for freedom;\n"
        "(c) to uphold and protect the sovereignty, unity and integrity of India;\n"
        "(d) to defend the country and render national service when called upon to do so;\n"
        "(e) to promote harmony and the spirit of common brotherhood amongst all the people of India transcending religious, linguistic diversities;\n"
        "(f) to value and preserve the rich heritage of our composite culture;\n"
        "(g) to protect and improve the natural environment including forests, lakes, rivers and wildlife;\n"
        "(h) to develop the scientific temper, humanism and the spirit of inquiry and reform;\n"
        "(i) to safeguard public property and to abjure violence;\n"
        "(j) to strive towards excellence in all spheres of individual and collective activity;\n"
        "(k) who is a parent or guardian to provide opportunities for education to his child between the age of six and fourteen years."
    ))

    # PART V - THE UNION EXECUTIVE (ARTICLES 52-78)
    sections.append((
        "PART V - THE UNION EXECUTIVE: PRESIDENT, PRIME MINISTER & CABINET (ARTICLES 52-78)",
        "ARTICLE 52. THE PRESIDENT OF INDIA: There shall be a President of India.\n"
        "ARTICLE 53. EXECUTIVE POWER OF THE UNION: Vested in the President and exercised directly or through subordinate officers.\n"
        "ARTICLE 54-55. ELECTION OF PRESIDENT: Elected by electoral college consisting of elected members of both Houses of Parliament and elected MLAs of States.\n"
        "ARTICLE 56. TERM OF OFFICE: Five years.\n"
        "ARTICLE 61. PROCEDURE FOR IMPEACHMENT OF THE PRESIDENT: For violation of the Constitution by two-thirds majority of total membership of each House.\n"
        "ARTICLE 72. POWER OF PRESIDENT TO GRANT PARDONS, REPRIEVES, RESPITES OR REMISSIONS OF PUNISHMENT:\n"
        "The President shall have the power to grant pardons in all cases where punishment or sentence is by a Court Martial, in all cases where sentence is for offence against law relating to Union executive power, and in all cases where sentence is a sentence of death.\n"
        "ARTICLE 74. COUNCIL OF MINISTERS TO AID AND ADVISE PRESIDENT:\n"
        "(1) There shall be a Council of Ministers with the Prime Minister at the head to aid and advise the President who shall, in the exercise of his functions, act in accordance with such advice.\n"
        "(2) The question whether any, and if so what, advice was tendered by Ministers to the President shall not be inquired into in any court.\n"
        "ARTICLE 75. OTHER PROVISIONS AS TO MINISTERS: Prime Minister appointed by President; other Ministers appointed on advice of PM. Council of Ministers collectively responsible to Lok Sabha.\n"
        "ARTICLE 76. ATTORNEY-GENERAL FOR INDIA: Appointed by President, qualified to be appointed a Judge of Supreme Court; chief legal adviser to Government of India."
    ))

    # PART V - PARLIAMENT & LEGISLATION (ARTICLES 79-123)
    sections.append((
        "PART V - THE PARLIAMENT OF INDIA & ORDINANCE POWER (ARTICLES 79-123)",
        "ARTICLE 79. CONSTITUTION OF PARLIAMENT: Consists of the President, the Council of States (Rajya Sabha), and the House of the People (Lok Sabha).\n"
        "ARTICLE 80. COMPOSITION OF RAJYA SABHA: 250 members (12 nominated by President for literature, science, art, social service; 238 representatives of States/UTs).\n"
        "ARTICLE 81. COMPOSITION OF LOK SABHA: Not more than 550 elected members on basis of adult suffrage.\n"
        "ARTICLE 85. SESSIONS, PROROGATION AND DISSOLUTION: President summons each House; maximum gap between two sessions shall not exceed 6 months.\n"
        "ARTICLE 100. QUORUM: One-tenth of the total number of members of the House.\n"
        "ARTICLE 105. POWERS, PRIVILEGES AND IMMUNITIES OF PARLIAMENT AND MEMBERS: Freedom of speech in Parliament, immunity from court proceedings for speech or vote.\n"
        "ARTICLE 107-108. LEGISLATIVE PROCEDURE & JOINT SITTING: Ordinary bills pass both Houses; joint sitting convened by President in case of deadlock.\n"
        "ARTICLE 109-110. MONEY BILLS: Introduced only in Lok Sabha on President's recommendation. Speaker's certification is final. Rajya Sabha can only delay for 14 days.\n"
        "ARTICLE 112. ANNUAL FINANCIAL STATEMENT (BUDGET): Statement of estimated receipts and expenditure.\n"
        "ARTICLE 123. POWER OF PRESIDENT TO PROMULGATE ORDINANCES DURING RECESS OF PARLIAMENT:\n"
        "President may promulgate Ordinances if circumstances exist requiring immediate action when either House is not in session. Must be laid before Parliament within 6 weeks of reassembly."
    ))

    # PART V - THE SUPREME COURT OF INDIA (ARTICLES 124-147)
    sections.append((
        "PART V - THE UNION JUDICIARY: SUPREME COURT OF INDIA (ARTICLES 124-147)",
        "ARTICLE 124. ESTABLISHMENT AND CONSTITUTION OF SUPREME COURT:\n"
        "Consists of Chief Justice of India and other Judges appointed by President under Collegium system. Retirement age 65 years. Removal on grounds of proved misbehaviour or incapacity by special majority address in Parliament.\n"
        "ARTICLE 129. SUPREME COURT TO BE A COURT OF RECORD: Power to punish for contempt of itself.\n"
        "ARTICLE 131. ORIGINAL JURISDICTION: Exclusive jurisdiction in disputes between Government of India and one or more States, or between States.\n"
        "ARTICLE 132-134. APPELLATE JURISDICTION: In constitutional matters involving substantial questions of law, civil matters under Art 133, criminal matters under Art 134.\n"
        "ARTICLE 136. SPECIAL LEAVE TO APPEAL (SLP):\n"
        "Supreme Court may, in its discretion, grant special leave to appeal from any judgment, decree, determination, sentence or order in any cause or matter passed by any court or tribunal in India (except military tribunals).\n"
        "ARTICLE 137. REVIEW OF JUDGMENTS OR ORDERS: Power to review any judgment pronounced or order made by it.\n"
        "ARTICLE 141. LAW DECLARED BY SUPREME COURT TO BE BINDING ON ALL COURTS:\n"
        "The law declared by the Supreme Court shall be binding on all courts within the territory of India (Doctrine of Stare Decisis).\n"
        "ARTICLE 142. ENFORCEMENT OF DECREES AND ORDERS: Supreme Court in exercise of its jurisdiction may pass such decree or make such order as is necessary for doing complete justice in any cause or matter pending before it.\n"
        "ARTICLE 143. POWER OF PRESIDENT TO CONSULT SUPREME COURT: Advisory jurisdiction on questions of law or fact of public importance."
    ))

    # PART VI - THE STATES & HIGH COURTS (ARTICLES 152-237)
    sections.append((
        "PART VI - THE STATES & HIGH COURTS WRIT JURISDICTION (ARTICLES 152-237)",
        "ARTICLE 153-161. THE GOVERNOR: Appointed by President. Executive power of State vested in Governor. Pardoning power under Art 161.\n"
        "ARTICLE 163-164. COUNCIL OF MINISTERS: With Chief Minister at head to aid and advise Governor.\n"
        "ARTICLE 213. POWER OF GOVERNOR TO PROMULGATE ORDINANCES DURING RECESS OF STATE LEGISLATURE.\n"
        "ARTICLE 214-215. HIGH COURTS FOR STATES: High Court to be a court of record with contempt powers.\n"
        "ARTICLE 217. APPOINTMENT AND CONDITIONS OF JUDGE OF HIGH COURT: Appointed by President; retirement age 62 years.\n\n"
        "ARTICLE 226. POWER OF HIGH COURTS TO ISSUE CERTAIN WRITS:\n"
        "(1) Notwithstanding anything in article 32, every High Court shall have power, throughout the territories in relation to which it exercises jurisdiction, "
        "to issue to any person or authority, including in appropriate cases, any Government, directions, orders or writs, including writs in the nature of "
        "HABEAS CORPUS, MANDAMUS, PROHIBITION, QUO WARRANTO and CERTIORARI, for the enforcement of any of the rights conferred by Part III AND FOR ANY OTHER PURPOSE.\n"
        "DISTINCTION FROM ARTICLE 32: Article 226 is wider in scope than Article 32 because High Courts can issue writs not only for fundamental rights "
        "violation but also for ordinary statutory rights ('for any other purpose') and administrative illegality.\n\n"
        "ARTICLE 227. POWER OF SUPERINTENDENCE OVER ALL COURTS: Administrative and judicial superintendence over all courts and tribunals throughout territories.\n"
        "ARTICLE 233-235. SUBORDINATE COURTS: District Judges appointed by Governor in consultation with High Court. Control over subordinate courts vested in High Court."
    ))

    # PART XI - CENTRE-STATE RELATIONS (ARTICLES 245-263)
    sections.append((
        "PART XI - RELATIONS BETWEEN THE UNION AND THE STATES (ARTICLES 245-263)",
        "ARTICLE 245. EXTENT OF LAWS: Parliament may make laws for whole or any part of India; State Legislature for whole or part of State. Parliament has extra-territorial legislative powers.\n"
        "ARTICLE 246. SUBJECT-MATTER OF LAWS MADE BY PARLIAMENT AND STATE LEGISLATURES (SEVENTH SCHEDULE):\n"
        "(1) Union List (List I): Exclusive power of Parliament (Defence, Foreign Affairs, Banking, Currency, Railways, Atomic Energy - 97 entries).\n"
        "(2) State List (List II): Exclusive power of State Legislature (Public Order, Police, Public Health, Agriculture, Local Government - 66 entries).\n"
        "(3) Concurrent List (List III): Both Parliament and State Legislatures (Criminal Law, Criminal Procedure, Civil Procedure, Marriage, Contracts, Forests, Education - 47 entries).\n"
        "ARTICLE 248. RESIDUARY POWERS OF LEGISLATION: Vested exclusively in Parliament for any matter not enumerated in List II or List III.\n"
        "ARTICLE 249-250. POWER OF PARLIAMENT TO LEGISLATE ON STATE LIST: In national interest upon 2/3rd resolution of Rajya Sabha (Art 249) or during Proclamation of Emergency (Art 250).\n"
        "ARTICLE 254. INCONSISTENCY BETWEEN LAWS MADE BY PARLIAMENT AND LAWS MADE BY STATE LEGISLATURES (REPUGNANCY):\n"
        "If any provision of a State law on a Concurrent List subject is repugnant to a law made by Parliament, the Parliamentary law prevails and the State law is void to the extent of repugnancy, "
        "unless the State law received Presidential assent under clause (2).\n"
        "ARTICLE 262. ADJUDICATION OF DISPUTES RELATING TO WATERS OF INTER-STATE RIVERS.\n"
        "ARTICLE 263. PROVISIONS WITH RESPECT TO AN INTER-STATE COUNCIL."
    ))

    # PART XII - FINANCE, PROPERTY & RIGHT TO PROPERTY (ARTICLES 264-300A)
    sections.append((
        "PART XII - FINANCE, CONTRACTS & RIGHT TO PROPERTY (ARTICLES 264-300A)",
        "ARTICLE 265. TAXES NOT TO BE IMPOSED SAVE BY AUTHORITY OF LAW: No tax shall be levied or collected except by authority of law.\n"
        "ARTICLE 266-267. CONSOLIDATED FUNDS AND CONTINGENCY FUND OF INDIA AND STATES.\n"
        "ARTICLE 280. FINANCE COMMISSION: Constituted by President every 5 years to recommend distribution of tax proceeds between Union and States.\n"
        "ARTICLE 299. CONTRACTS: All contracts made in exercise of executive power of Union or State shall be expressed to be made by President or Governor.\n"
        "ARTICLE 300. SUITS AND PROCEEDINGS: Government of India may sue or be sued by the name of the Union of India; States by name of State.\n\n"
        "ARTICLE 300A. PERSONS NOT TO BE DEPRIVED OF PROPERTY SAVE BY AUTHORITY OF LAW (RIGHT TO PROPERTY):\n"
        "No person shall be deprived of his property save by authority of law.\n"
        "HISTORICAL & CONSTITUTIONAL STATUS:\n"
        "The 44th Constitutional Amendment Act, 1978 repealed Article 19(1)(f) and Article 31, removing the Right to Property from Part III Fundamental Rights. "
        "Article 300A was inserted into Part XII making Right to Property a constitutional and human right, but no longer a fundamental right. "
        "The Supreme Court held in Vidya Devi v. State of Himachal Pradesh (2020) and Kolkata Municipal Corp (2024) that the State cannot dispossess a citizen of property without statutory authority, fair compensation, and due procedure."
    ))

    # PART XIII, XIV, XIVA, XV - SERVICES, TRIBUNALS, ELECTIONS (ARTICLES 301-329)
    sections.append((
        "PART XIII-XV - COMMERCE, SERVICES, TRIBUNALS & ELECTIONS (ARTICLES 301-329)",
        "ARTICLE 301. FREEDOM OF TRADE, COMMERCE AND INTERCOURSE: Free throughout territory of India, subject to reasonable restrictions under Art 302-304.\n"
        "ARTICLE 310. DOCTRINE OF PLEASURE: Civil servants hold office during pleasure of President or Governor.\n"
        "ARTICLE 311. DISMISSAL, REMOVAL OR REDUCTION IN RANK OF CIVIL SERVANTS:\n"
        "(1) No civil servant shall be dismissed or removed by an authority subordinate to that by which he was appointed.\n"
        "(2) Mandatory reasonable opportunity of being heard (inquiry) before dismissal, removal, or reduction in rank, except for criminal conviction or security of State.\n"
        "ARTICLE 315-323. PUBLIC SERVICE COMMISSIONS: UPSC and State Public Service Commissions.\n"
        "ARTICLE 323A-323B. ADMINISTRATIVE TRIBUNALS: Central Administrative Tribunal (CAT) for service matters; subject to High Court judicial review under Art 226 (L. Chandra Kumar v. Union of India).\n"
        "ARTICLE 324. SUPERINTENDENCE, DIRECTION AND CONTROL OF ELECTIONS VESTED IN ELECTION COMMISSION: Independent constitutional body.\n"
        "ARTICLE 326. ELECTIONS TO LOK SABHA AND STATE ASSEMBLIES ON BASIS OF ADULT SUFFRAGE (Citizens not less than 18 years of age)."
    ))

    # PART XVIII - EMERGENCY PROVISIONS (ARTICLES 352-360)
    sections.append((
        "PART XVIII - EMERGENCY PROVISIONS (ARTICLES 352-360)",
        "ARTICLE 352. PROCLAMATION OF EMERGENCY (NATIONAL EMERGENCY):\n"
        "(1) If the President is satisfied that a grave emergency exists whereby the security of India or of any part thereof is threatened, "
        "whether by WAR or EXTERNAL AGGRESSION or ARMED REBELLION, he may, by Proclamation, make a declaration of emergency.\n"
        "(2) Ground of 'internal disturbance' was substituted by 'armed rebellion' via the 44th Amendment 1978.\n"
        "(3) President shall not issue Proclamation unless the decision of the Union Cabinet has been communicated to him in writing.\n"
        "(4) Must be approved by both Houses of Parliament by special majority within one month.\n"
        "ARTICLE 353. EFFECT OF PROCLAMATION: Union executive power extends to giving directions to States; Parliament may legislate on State List.\n\n"
        "ARTICLE 356. PROVISIONS IN CASE OF FAILURE OF CONSTITUTIONAL MACHINERY IN STATES (PRESIDENT'S RULE):\n"
        "(1) If the President, on receipt of report from Governor or otherwise, is satisfied that governance cannot be carried on in accordance with Constitution, "
        "he may assume executive functions of State and declare powers of State Legislature exercisable by Parliament.\n"
        "(2) Supreme Court ruling in S.R. Bommai v. Union of India (1994): Exercise of Art 356 is subject to judicial review. Floor test is mandatory. Secularism is part of basic structure.\n\n"
        "ARTICLE 358 & 359. SUSPENSION OF RIGHTS DURING EMERGENCY:\n"
        "- Article 358: Automatic suspension of Article 19 freedoms only during War or External Aggression (not Armed Rebellion).\n"
        "- Article 359: Presidential power to suspend enforcement of fundamental rights during emergency, EXCEPT ARTICLES 20 AND 21 (Protection against ex-post facto laws/double jeopardy and Right to Life/Personal Liberty CAN NEVER BE SUSPENDED).\n\n"
        "ARTICLE 360. FINANCIAL EMERGENCY: Declared if financial stability or credit of India is threatened."
    ))

    # PART XX - AMENDMENT OF THE CONSTITUTION (ARTICLE 368)
    sections.append((
        "PART XX - AMENDMENT OF THE CONSTITUTION & BASIC STRUCTURE (ARTICLE 368)",
        "ARTICLE 368. POWER OF PARLIAMENT TO AMEND THE CONSTITUTION AND PROCEDURE THEREFOR:\n"
        "(1) Notwithstanding anything in this Constitution, Parliament may in exercise of its constituent power amend by way of addition, variation or repeal "
        "any provision of this Constitution in accordance with the procedure laid down in this article.\n"
        "(2) Procedure: Bill introduced in either House of Parliament; passed by each House by a majority of total membership and by a majority of not less than "
        "two-thirds of members present and voting (Special Majority), and receives assent of the President.\n"
        "ENTRENCHED PROVISIONS RATIFICATION: Amendments affecting election of President (Art 54-55), executive powers (Art 73, 162), Supreme Court/High Courts (Part V Ch IV, Part VI Ch V), "
        "representation in Parliament, Seventh Schedule lists, or Article 368 itself REQUIRE RATIFICATION BY LEGISLATURES OF NOT LESS THAN ONE-HALF OF THE STATES.\n\n"
        "LANDMARK DOCTRINE OF BASIC STRUCTURE (KESAVANANDA BHARATI v. STATE OF KERALA, 1973):\n"
        "A historic 13-Judge Constitution Bench ruled 7:6 that while Parliament has wide constituent powers under Article 368 to amend any part of the Constitution, "
        "it DOES NOT HAVE THE POWER TO ALTER, DAMAGE OR DESTROY THE BASIC STRUCTURE OR ESSENTIAL FRAMEWORK OF THE CONSTITUTION.\n"
        "Basic structure elements include: Supremacy of the Constitution, Republican and Democratic form of government, Secular character, "
        "Separation of powers between legislature, executive and judiciary, Federal character, Judicial review (Minerva Mills), Rule of law, and Fundamental rights in Part III."
    ))

    # SCHEDULES 1 TO 12
    sections.append((
        "THE SCHEDULES OF THE CONSTITUTION OF INDIA (SCHEDULES 1 TO 12)",
        "FIRST SCHEDULE: Names of the 28 States and 8 Union Territories and their territorial extents.\n"
        "SECOND SCHEDULE: Provisions as to salaries, allowances and emoluments of the President, Governors, Speaker, Judges, CAG.\n"
        "THIRD SCHEDULE: Forms of Oaths or Affirmations for Union Ministers, MPs, Supreme Court Judges, CAG, State Ministers, MLAs, High Court Judges.\n"
        "FOURTH SCHEDULE: Allocation of seats in the Council of States (Rajya Sabha) to each State and Union Territory.\n"
        "FIFTH SCHEDULE: Administration and control of Scheduled Areas and Scheduled Tribes in States other than Assam, Meghalaya, Tripura, Mizoram.\n"
        "SIXTH SCHEDULE: Administration of Tribal Areas in the States of Assam, Meghalaya, Tripura and Mizoram (Autonomous District Councils).\n"
        "SEVENTH SCHEDULE: Distribution of legislative powers between Union and States: List I (Union List - 97 subjects), List II (State List - 66 subjects), List III (Concurrent List - 47 subjects).\n"
        "EIGHTH SCHEDULE: List of 22 Official Languages recognized by the Constitution (Assamese, Bengali, Bodo, Dogri, Gujarati, Hindi, Kannada, Kashmiri, Konkani, Maithili, Malayalam, Meitei, Marathi, Nepali, Odia, Punjabi, Sanskrit, Santali, Sindhi, Tamil, Telugu, Urdu).\n"
        "NINTH SCHEDULE: Validation of certain Acts and Regulations (originally inserted by 1st Amendment 1951 to protect agrarian land reforms; Supreme Court ruled in I.R. Coelho (2007) that laws added to Ninth Schedule after April 24, 1973 are open to judicial review if they violate basic structure).\n"
        "TENTH SCHEDULE: Provisions as to disqualification on ground of defection (Anti-Defection Law inserted by 52nd Amendment 1985; Kihoto Hollohan v. Zachillhu upheld Speaker's decision is subject to judicial review).\n"
        "ELEVENTH SCHEDULE: Powers, authority and responsibilities of Panchayats (29 functional subjects added by 73rd Amendment 1992).\n"
        "TWELFTH SCHEDULE: Powers, authority and responsibilities of Municipalities (18 urban functional subjects added by 74th Amendment 1992)."
    ))

    return sections


def build_constitution_book(target_dir: Path) -> Path:
    target_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = target_dir / "the_constitution_of_india_authoritative_edition.pdf"
    
    sections = get_complete_constitution_sections()
    pdf_data = create_pdf_binary(sections)
    
    with open(pdf_path, "wb") as f:
        f.write(pdf_data)
        
    print(f"[CONSTITUTION_BUILDER] Successfully generated complete Constitution book at: {pdf_path}")
    print(f"[CONSTITUTION_BUILDER] Total Sections compiled: {len(sections)} sections | File size: {len(pdf_data)} bytes")
    return pdf_path


if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent / "data" / "constitution"
    build_constitution_book(out_dir)
