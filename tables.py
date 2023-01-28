school = {
    "Cavell": ["Claim"],
    "Master": ["Austin1975", "Wittgenstein2009"],
    "Most cited": [
        "Burge2010",
        "Davidson2013",
        "Dummett1973",
        "Fodor1983",
        "Frege1948",
        "Kripke1980",
        "Lewis2002",
        "Putnam2004",
        "Quine2013",
        "Russell1967",
        "Williamson2002",
        "Wright1992",
    ],
    "Anti-teorethical": [
        "Anscombe",
        "Baier1991",
        "Diamond1995",
        "Foot2002",
        "MacIntyre2007",
        "McDowell1994",
        "Murdoch2013",
        "Williams2011",
        "Winch1990",
    ],
}

print("\\begin{center}\n\\begin{tabular}{|r l l|}")
print("\\hline")
print("Author & Title & Category \\\\")
print("\\hline")
for cat in school.keys():
    for bib in school[cat]:
        print("\\citeauthor{" + bib + "} & \\citetitle{" + bib + "} & " + cat + " \\\\")
print("\\hline")
print("\\end{tabular}\n\\end{center}")


year = {
    "must_we_mean_what_we_say": 1969,
    "the_claim_of_reason_1": "1972, 1979",
    "the_senses_of_walden_1": "1972, 1980",
    "the_world_viewed_1": "1971, 1979",
    "pursuits_of_happiness": 1981,
    "themes_out_of_school": 1984,
    "a_pitch_of_philosophy": 1994,
    "cities_of_words": 2004,
    "conditions_handsome_and_unhandsome": 1990,
    "contesting_tears": 1996,
    "in_quest_of_the_ordinary": 1988,
    "philosophical_passages": 1995,
    "this_new_yet_unapproachable_america": 1988,
    "little_did_i_know": 2010,
    "philosophy_the_day_after": 2005,
}

bibs = {
    "must_we_mean_what_we_say": "Must",
    "the_claim_of_reason_1": "Claim",
    "the_senses_of_walden_1": "Senses",
    "the_world_viewed_1": "World",
    "pursuits_of_happiness": "Pursuits",
    "themes_out_of_school": "Themes",
    "a_pitch_of_philosophy": "aPitch",
    "cities_of_words": "Cities",
    "conditions_handsome_and_unhandsome": "Conditions",
    "contesting_tears": "Contesting",
    "in_quest_of_the_ordinary": "inQuest",
    "philosophical_passages": "Philosophical",
    "this_new_yet_unapproachable_america": "thisNew",
    "little_did_i_know": "Little",
    "philosophy_the_day_after": "Philosophy",
}

print("\\begin{center}\n\\begin{tabular}{|r l l|}")
print("\\hline")
print("Title & 1st and enlarged Editions & Used Edition \\\\")
print("\\hline")
for bib in bibs.keys():
    print(
        "\\citetitle{"
        + bibs[bib]
        + "} & \\ "
        + str(year[bib])
        + " & \\citeyear{"
        + bibs[bib]
        + "} \\\\"
    )
print("\\hline")
print("\\end{tabular}\n\\end{center}")
