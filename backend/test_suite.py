import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.scenario_engine import match_story_scenario
from backend.statutory_engine import match_statutory_section

test_queries = [
    ('family_cruelty_dowry', 'My husband and in-laws are beating me and demanding gold and cash'),
    ('property_partition_daughters', 'Father died without will and my brothers are refusing to give me share in ancestral land'),
    ('cheque_bounce_138', 'A client gave me a cheque of 5 lakhs for goods delivered and the cheque bounced with insufficient funds'),
    ('land_encroachment_trespass', 'Neighbor built a boundary wall encroaching 3 feet into my registered land'),
    ('tenant_landlord_eviction', 'Tenant stopped paying rent for 6 months and refuses to vacate my flat'),
    ('divorce_custody_maintenance', 'Me and my wife want mutual divorce and settle child custody'),
    ('builder_delay_rera', 'Builder took 80% money and delayed possession by 3 years'),
    ('cyber_financial_fraud', 'Someone called impersonating bank manager and stole money through OTP'),
    ('accident_negligent_driving', 'A speeding truck hit my car and caused severe injuries'),
    ('private_defence_assault', 'Someone attacked me with knife and I hit them back with a stick to protect myself'),
    ('conflicting_wills_inheritance_probate', 'My grandfather left two conflicting wills, one unregistered to me and another registered to uncle'),
    ('police_fir_refusal_inaction', 'Police officer at thana refused to register FIR for phone snatching'),
    ('landlord_security_deposit_refund', 'Landlord is refusing to refund my security deposit after I vacated the flat'),
    ('wrongful_termination_unpaid_salary', 'Company fired me without notice and withheld my 2 months salary and relieving letter'),
    ('consumer_ecommerce_fraud', 'I ordered an iPhone from Flipkart and received soap in the box, and customer care is refusing refund'),
    ('medical_negligence_malpractice', 'Doctor left a surgical sponge inside patient during operation'),
    ('cyber_blackmail_sextortion_morphing', 'Someone is blackmailing me on Instagram threatening to leak morphed photos to contacts'),
    ('defamation_social_media_slander', 'Someone made false allegations calling me scammer and fraud in a public post on Facebook'),
    ('money_recovery_unpaid_loan', 'Friend borrowed 10 lakhs promissory note and refusing to return money'),
    ('property_document_forgery_fraud', 'Someone forged my father signature on a sale deed and fraudulently sold our land'),
    ('rti_inaction_pio_penalty', 'PIO failed to provide information under RTI after 30 days'),
    ('posh_workplace_harassment', 'Manager is sexually harassing woman at office and sending inappropriate messages'),
    ('senior_citizen_abuse_eviction', 'Son is beating and harassing elderly parents and trying to evict them from house'),
    ('extortion_threat_protection_money', 'Local goons threatening to kill me if I do not pay 50000 protection money every month'),
    ('illegal_arrest_custodial_violence', 'Police detained my brother for 2 days without warrant and without producing before magistrate'),
    ('neighbour_nuisance_illegal_construction', 'Neighbor running illegal generator causing extreme noise and vibration 24 hours'),
    ('dowry_death_unnatural', 'Married woman died under suspicious burn injuries within 2 years of marriage after dowry harassment'),
    ('kidnapping_abduction_ransom', 'Kidnapped child demanding 50 lakhs ransom or will kill'),
    ('hit_and_run_drunk_driving', 'Drunk driver hit pedestrian and fled the scene without helping'),
    ('cheque_bounce_defense_accused', 'Someone misused my blank security cheque given 3 years ago and filed false 138 case against me'),
    ('contested_divorce_cruelty_desertion', 'Husband cruelty and desertion for 3 years wanting contested divorce'),
    ('interim_maintenance_execution', 'Husband stopped paying the interim maintenance ordered by family court')
]

passed = 0
for expected, query in test_queries:
    res = match_story_scenario(query)
    matched = res['domain'] if res else None
    if matched == expected:
        passed += 1
    else:
        print(f"FAIL: Query: '{query}' -> Expected: {expected}, Got: {matched}")

print(f"Total Scenarios Tested: {len(test_queries)} | Passed: {passed}/{len(test_queries)}")

# Test statutory engine
statutory_tests = [
    ("what is ipc 300", ("300", "ipc")),
    ("what is ipc 302", ("302", "ipc")),
    ("what is ipc 420", ("420", "ipc")),
    ("what is ipc 498a", ("498a", "ipc")),
    ("tell me about article 21", ("21", "constitution")),
    ("what is article 19", ("19", "constitution")),
    ("what is section 138 of ni act", ("138", "special_act")),
    ("section 41a crpc", ("41a", "crpc")),
    ("what is section 154 crpc", ("154", "crpc")),
    ("what is section 438 crpc", ("438", "crpc")),
    ("what is section 482 crpc", ("482", "crpc")),
    ("what is section 378 ipc", ("378", "ipc")),
    ("what is section 405 ipc", ("405", "ipc")),
    ("what is section 503 ipc", ("503", "ipc")),
    ("what is section 463 ipc", ("463", "ipc")),
]

stat_passed = 0
for query, expected in statutory_tests:
    res = match_statutory_section(query)
    if res == expected:
        stat_passed += 1
    else:
        print(f"FAIL STATUTORY: Query: '{query}' -> Expected: {expected}, Got: {res}")

print(f"Total Statutory Tested: {len(statutory_tests)} | Passed: {stat_passed}/{len(statutory_tests)}")

# Test conversational multi-turn follow-ups
from backend.main import handle_conversational_followup, MessageItem

followup_tests = [
    {
        "history": [
            MessageItem(role="user", content="Police at the thana refused to register my FIR for snatching"),
            MessageItem(role="assistant", content="Lalita Kumari v. Govt of UP makes registration mandatory under Section 154 CrPC."),
        ],
        "query": "Which court should I go to?",
        "expected_keyword": "156(3)",
    },
    {
        "history": [
            MessageItem(role="user", content="Police at the thana refused to register my FIR for snatching"),
            MessageItem(role="assistant", content="Lalita Kumari v. Govt of UP makes registration mandatory under Section 154 CrPC."),
        ],
        "query": "What should I do next?",
        "expected_keyword": "154(3)",
    },
    {
        "history": [
            MessageItem(role="user", content="I vacated my flat and landlord is refusing to refund my security deposit"),
            MessageItem(role="assistant", content="Landlord cannot arbitrarily withhold deposit under Model Tenancy Act."),
        ],
        "query": "Can he deduct money for painting and wear and tear?",
        "expected_keyword": "CANNOT DEDUCT",
    },
    {
        "history": [
            MessageItem(role="user", content="Company fired me without notice and withheld my 2 months salary"),
            MessageItem(role="assistant", content="Under Section 73 of Contract Act, arbitrary termination without notice pay is void."),
        ],
        "query": "Can they withhold my relieving letter?",
        "expected_keyword": "CANNOT WITHHOLD",
    },
    {
        "history": [
            MessageItem(role="user", content="I ordered an iPhone from Flipkart and got soap in the box"),
            MessageItem(role="assistant", content="Under CPA 2019 delivering wrong item is unfair trade practice."),
        ],
        "query": "Where can I file the complaint online?",
        "expected_keyword": "edaakhil",
    },
    {
        "history": [
            MessageItem(role="user", content="Someone is blackmailing me with morphed photos on Instagram"),
            MessageItem(role="assistant", content="This violates Section 66E and 67A of IT Act."),
        ],
        "query": "Should I pay them money?",
        "expected_keyword": "NEVER PAY",
    },
    {
        "history": [
            MessageItem(role="user", content="Doctor left surgical sponge inside patient during operation"),
            MessageItem(role="assistant", content="Achutrao Haribhau Khodwa applies res ipsa loquitur."),
        ],
        "query": "Can police arrest the doctor immediately?",
        "expected_keyword": "Jacob Mathew",
    },
    {
        "history": [
            MessageItem(role="user", content="Someone made false allegations calling me a scammer on social media"),
            MessageItem(role="assistant", content="Section 499 IPC protects reputation as fundamental right under Art 21."),
        ],
        "query": "Can I get a gag order to stop him from posting?",
        "expected_keyword": "Order XXXIX",
    },
]

followup_passed = 0
for idx, tc in enumerate(followup_tests, start=1):
    res = handle_conversational_followup(query=tc["query"], history=tc["history"], role="advocate")
    if not res:
        print(f"FAIL followup {idx}: Query '{tc['query']}' returned None")
        continue
    text, citations = res
    if tc["expected_keyword"].lower() in text.lower():
        followup_passed += 1
    else:
        print(f"FAIL followup {idx}: Keyword '{tc['expected_keyword']}' not in response for query '{tc['query']}'")

print(f"Total Follow-ups Tested: {len(followup_tests)} | Passed: {followup_passed}/{len(followup_tests)}")

if passed == len(test_queries) and stat_passed == len(statutory_tests) and followup_passed == len(followup_tests):
    print("ALL 55 ENGINE & FOLLOW-UP TESTS PASSED WITH 100% ACCURACY!")
    sys.exit(0)
else:
    sys.exit(1)
