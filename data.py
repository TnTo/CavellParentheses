from cavell import (
    select_corpus,
    tokenize_dict,
    brackets_ratio,
    correlation,
    count_and_frequency,
    significantly_different,
    brackets_length,
)
import pandas as pd
from numpy import nan

# Correct titles and names
names = {
    "austin": "Austin",
    "wittgenstein": "Wittgenstein",
    "cavell": "Cavell",
    "burge": "Burge",
    "davidson": "Davidson",
    "dummett": "Dummett",
    "fodor": "Fodor",
    "frege": "Frege",
    "kripke": "Kripke",
    "lewis": "Lewis",
    "quine": "Quine",
    "russell": "Russell",
    "williamson": "Williamson",
    "wright": "Wright",
    "anscombe": "Anscombe",
    "baier": "Baier",
    "diamond": "Diamond",
    "foot": "Foot",
    "macintyre": "MacIntyre",
    "mcdowell": "McDowell",
    "murdoch": "Murdoch",
    "putnam": "Putnam",
    "williams": "Williams",
    "winch": "Winch",
    "must_we_mean_what_we_say": "Must We Mean What We Say?",
    "the_claim_of_reason": "The Claim of Reason",
    "the_senses_of_walden": "The Senses of Walden",
    "the_world_viewed": "The World Viewed",
    "the_claim_of_reason_1": "The Claim of Reason (1972)",
    "the_senses_of_walden_1": "The Senses of Walden (1972)",
    "the_world_viewed_1": "The World Viewed (1971)",
    "disowning_knowledge_in_seven_plays_of_shakespeare": "Disowning Knowledge",
    "disowning_knowledge_in_seven_plays_of_shakespeare_2": "Disowning Knowledge (1987)",
    "pursuits_of_happiness": "Pursuits of Happiness",
    "themes_out_of_school": "Themes Out of School",
    "the_claim_of_reason_2": "The Claim of Reason (1979)",
    "the_senses_of_walden_2": "The Senses of Walden (1981)",
    "the_world_viewed_2": "The World Viewed (1979)",
    "a_pitch_of_philosophy": "A Pitch of Philosophy",
    "cities_of_words": "Cities of Words",
    "conditions_handsome_and_unhandsome": "Conditions Handsome and Unhandsome",
    "contesting_tears": "Contesting Tears",
    "disowning_knowledge_in_seven_plays_of_shakespeare_3": "Disowning Knowledge (2003)",
    "disowning_knowledge_in_seven_plays_of_shakespeare_pref": "Disowning Knowledge (Preface)",
    "emersons_trascendental": "Emerson's Transcendental Etudes",
    "in_quest_of_the_ordinary": "In Quest of the Ordinary",
    "philosophical_passages": "Philosophical Passages",
    "this_new_yet_unapproachable_america": "This New Yet Unapproachable America",
    "little_did_i_know": "Little Did I Know",
    "cavell_on_film": "Cavell on Film",
    "philosophy_the_day_after": "Philosophy the Day after Tomorrow",
    "corpus": "corpus",
}


### List of brackets in Benchmark
df_brackets_benchmark = pd.DataFrame()
brackets = select_corpus(id="Benchmark", suffix="brackets", as_list=True)
for title in brackets.keys():
    title_brackets = pd.DataFrame(brackets[title], columns=["brackets"])
    title_brackets["author"] = title
    df_brackets_benchmark = df_brackets_benchmark.append(title_brackets)
df_brackets_benchmark["author"] = df_brackets_benchmark["author"].apply(
    lambda x: names[x]
)
df_brackets_benchmark.to_csv("data/benchmark_brackets.csv", index=False)

### List of brackets in Cavell
df_brackets_cavell = pd.DataFrame()
brackets = {
    **select_corpus(id="CavellTime", suffix="brackets", as_list=True),
    **select_corpus(id="Cavell", suffix="brackets", as_list=True),
}
for title in brackets.keys():
    title_brackets = pd.DataFrame(brackets[title], columns=["brackets"])
    title_brackets["title"] = title
    df_brackets_cavell = df_brackets_cavell.append(title_brackets)
df_brackets_cavell["title"] = df_brackets_cavell["title"].apply(lambda x: names[x])
df_brackets_cavell.to_csv("data/cavell_brackets.csv", index=False)


### List of brackets after .?! in Cavell
df_dot_brackets_cavell = pd.DataFrame()
brackets = {
    **select_corpus(id="CavellTime", suffix="dot_brackets", as_list=True),
    **select_corpus(id="Cavell", suffix="dot_brackets", as_list=True),
}
for title in brackets:
    title_brackets = pd.DataFrame(brackets[title], columns=["brackets"])
    title_brackets["title"] = title
    df_dot_brackets_cavell = df_dot_brackets_cavell.append(title_brackets)
df_dot_brackets_cavell["title"] = df_dot_brackets_cavell["title"].apply(
    lambda x: names[x]
)
df_dot_brackets_cavell.to_csv("data/cavell_dot_brackets.csv", index=False)


### brackets ratio and similarity in Benchmark
### length of text, numbers of brackets and length of brackets


benchmark_corpus_token = tokenize_dict(
    select_corpus(id="Benchmark", suffix="clean"), skip_stopwords=False
)
benchmark_corpus_brackets_token = tokenize_dict(
    select_corpus(id="Benchmark", suffix="brackets"), skip_stopwords=False
)
benchmark_corpus_dot_brackets_token = tokenize_dict(
    select_corpus(id="Benchmark", suffix="dot_brackets"), skip_stopwords=False
)

df_brackets_benchmark = pd.DataFrame()
brackets_benchmark = select_corpus(id="Benchmark", suffix="brackets", as_list=True)
for author in brackets_benchmark.keys():
    author_brackets = pd.DataFrame(brackets_benchmark[author], columns=["brackets"])
    author_brackets["author"] = author
    df_brackets_benchmark = df_brackets_benchmark.append(author_brackets)

benchmark_corpus_len = {}
for author in benchmark_corpus_token:
    benchmark_corpus_len[author] = len(benchmark_corpus_token[author])

brackets_lengths_benchmark = brackets_length(
    tokenize_dict(
        select_corpus(id="Benchmark", suffix="brackets", as_list=True),
        as_list=True,
        skip_stopwords=False,
    )
)
for author in brackets_lengths_benchmark:
    brackets_lengths_benchmark[author] = [brackets_lengths_benchmark[author]]

school = {
    "Master": ["austin", "wittgenstein"],
    "Cavell": ["cavell"],
    "Most cited analytical": [
        "burge",
        "davidson",
        "dummett",
        "fodor",
        "frege",
        "kripke",
        "lewis",
        "putnam",
        "quine",
        "russell",
        "williamson",
        "wright",
    ],
    "Anti-teorethical": [
        "anscombe",
        "baier",
        "diamond",
        "foot",
        "macintyre",
        "mcdowell",
        "murdoch",
        "williams",
        "winch",
    ],
}

df_benchmark = (
    pd.merge(
        pd.DataFrame.from_dict(
            brackets_ratio(benchmark_corpus_token, benchmark_corpus_brackets_token),
            orient="index",
            columns=["brackets_ratio"],
        )
        .reset_index()
        .rename(columns={"index": "author"}),
        pd.DataFrame.from_dict(
            brackets_ratio(benchmark_corpus_token, benchmark_corpus_dot_brackets_token),
            orient="index",
            columns=["dot_brackets_ratio"],
        )
        .reset_index()
        .rename(columns={"index": "author"}),
        how="outer",
        on="author",
    )
    .merge(
        pd.DataFrame.from_dict(
            correlation(
                count_and_frequency(benchmark_corpus_token, skip_stopwords=True),
                count_and_frequency(
                    benchmark_corpus_brackets_token, skip_stopwords=True
                ),
            ),
            orient="index",
            columns=["r2", "pvalue"],
        )
        .reset_index()
        .rename(columns={"index": "author"}),
        how="outer",
        on="author",
    )
    .sort_values("brackets_ratio")
    .merge(
        pd.DataFrame.from_dict(school, orient="index")
        .reset_index()
        .melt(id_vars=["index"], value_name="author")
        .dropna()
        .drop(columns="variable")
        .rename(columns={"index": "school"}),
        how="left",
        on="author",
    )
    .merge(
        df_brackets_benchmark.groupby("author")
        .size()
        .to_frame()
        .rename(columns={0: "n_brackets"}),
        how="outer",
        on="author",
    )
    .merge(
        pd.DataFrame.from_dict(benchmark_corpus_len, orient="index", columns=["length"])
        .reset_index()
        .rename(columns={"index": "author"}),
        how="outer",
        on="author",
    )
    .merge(
        pd.DataFrame.from_dict(
            brackets_lengths_benchmark, orient="index", columns=["brackets_length"]
        )
        .reset_index()
        .rename(columns={"index": "author"}),
        how="outer",
        on="author",
    )
)

df_benchmark["author"] = df_benchmark["author"].apply(lambda x: names[x])

df_benchmark.to_csv("data/benchmark.csv", index=False)


### brackets ratio and similarity in Cavell
### length of text, numbers of brackets and length of brackets


cavell_corpus_token = tokenize_dict(
    select_corpus(id="CavellAll", suffix="clean"), skip_stopwords=False
)
cavell_corpus_brackets_token = tokenize_dict(
    select_corpus(id="CavellAll", suffix="brackets"), skip_stopwords=False
)
cavell_corpus_dot_brackets_token = tokenize_dict(
    select_corpus(id="CavellAll", suffix="dot_brackets"), skip_stopwords=False
)

df_brackets_cavell = pd.DataFrame()
brackets_cavell = select_corpus(id="CavellAll", suffix="brackets", as_list=True)
for title in brackets_cavell.keys():
    title_brackets = pd.DataFrame(brackets_cavell[title], columns=["brackets"])
    title_brackets["title"] = title
    df_brackets_cavell = df_brackets_cavell.append(title_brackets)

cavell_corpus_len = {}
for title in cavell_corpus_token:
    cavell_corpus_len[title] = len(cavell_corpus_token[title])

brackets_lengths_cavell = brackets_length(
    tokenize_dict(
        select_corpus(id="CavellAll", suffix="brackets", as_list=True),
        as_list=True,
        skip_stopwords=False,
    )
)
for title in brackets_lengths_cavell:
    brackets_lengths_cavell[title] = [brackets_lengths_cavell[title]]

period = {
    "1958-1972": [
        "must_we_mean_what_we_say",
        "the_claim_of_reason_1",
        "the_senses_of_walden_1",
        "the_world_viewed_1",
    ],
    "1983-1987": [
        # 'disowning_knowledge_in_seven_plays_of_shakespeare_2',
        "pursuits_of_happiness",
        "themes_out_of_school",
        "the_claim_of_reason_2",
        "the_senses_of_walden_2",
        "the_world_viewed_2",
    ],
    "1988-2004": [
        "a_pitch_of_philosophy",
        "cities_of_words",
        "conditions_handsome_and_unhandsome",
        "contesting_tears",
        # 'disowning_knowledge_in_seven_plays_of_shakespeare_3',
        # 'disowning_knowledge_in_seven_plays_of_shakespeare_pref',
        # 'emersons_trascendental',
        "in_quest_of_the_ordinary",
        "philosophical_passages",
        "this_new_yet_unapproachable_america",
    ],
    "2005-2010": [
        "little_did_i_know",
        "philosophy_the_day_after",
        #'cavell_on_film'
    ],
    "divided": ["the_senses_of_walden", "the_world_viewed", "the_claim_of_reason"],
}

year = {
    "must_we_mean_what_we_say": 1969,
    "the_claim_of_reason_1": 1972,
    "the_claim_of_reason": 1972,
    "the_senses_of_walden_1": 1972,
    "the_senses_of_walden": 1972,
    "the_world_viewed_1": 1971,
    "the_world_viewed": 1971,
    # 'disowning_knowledge_in_seven_plays_of_shakespeare_2':1987,
    # 'disowning_knowledge_in_seven_plays_of_shakespeare':1987,
    "pursuits_of_happiness": 1981,
    "themes_out_of_school": 1984,
    "the_claim_of_reason_2": 1979,
    "the_senses_of_walden_2": 1981,
    "the_world_viewed_2": 1979,
    "a_pitch_of_philosophy": 1994,
    "cities_of_words": 2004,
    "conditions_handsome_and_unhandsome": 1990,
    "contesting_tears": 1996,
    # 'disowning_knowledge_in_seven_plays_of_shakespeare_3':2003,
    # 'disowning_knowledge_in_seven_plays_of_shakespeare_pref':2003,
    # 'emersons_trascendental':2003,
    "in_quest_of_the_ordinary": 1988,
    "philosophical_passages": 1995,
    "this_new_yet_unapproachable_america": 1988,
    "little_did_i_know": 2010,
    "philosophy_the_day_after": 2005,
    # 'cavell_on_film':2005
}

df_cavell = (
    pd.merge(
        pd.DataFrame.from_dict(
            brackets_ratio(cavell_corpus_token, cavell_corpus_brackets_token),
            orient="index",
            columns=["brackets_ratio"],
        )
        .reset_index()
        .rename(columns={"index": "title"}),
        pd.DataFrame.from_dict(
            brackets_ratio(cavell_corpus_token, cavell_corpus_dot_brackets_token),
            orient="index",
            columns=["dot_brackets_ratio"],
        )
        .reset_index()
        .rename(columns={"index": "title"}),
        how="outer",
        on="title",
    )
    .merge(
        pd.DataFrame.from_dict(
            correlation(
                count_and_frequency(cavell_corpus_token, skip_stopwords=True),
                count_and_frequency(cavell_corpus_brackets_token, skip_stopwords=True),
            ),
            orient="index",
            columns=["r2", "pvalue"],
        )
        .reset_index()
        .rename(columns={"index": "title"}),
        how="outer",
        on="title",
    )
    .sort_values("brackets_ratio")
    .merge(
        pd.DataFrame.from_dict(period, orient="index")
        .reset_index()
        .melt(id_vars=["index"], value_name="title")
        .dropna()
        .drop(columns="variable")
        .rename(columns={"index": "period"}),
        how="left",
        on="title",
    )
    .merge(
        pd.DataFrame.from_dict(year, orient="index", columns=["year"])
        .reset_index()
        .rename(columns={"index": "title"}),
        how="left",
        on="title",
    )
    .sort_values("year")
    .merge(
        df_brackets_cavell.groupby("title")
        .size()
        .to_frame()
        .rename(columns={0: "n_brackets"}),
        how="outer",
        on="title",
    )
    .merge(
        pd.DataFrame.from_dict(cavell_corpus_len, orient="index", columns=["length"])
        .reset_index()
        .rename(columns={"index": "title"}),
        how="outer",
        on="title",
    )
    .merge(
        pd.DataFrame.from_dict(
            brackets_lengths_cavell, orient="index", columns=["brackets_length"]
        )
        .reset_index()
        .rename(columns={"index": "title"}),
        how="outer",
        on="title",
    )
)

df_cavell["title"] = df_cavell["title"].apply(lambda x: names[x])

df_cavell.to_csv("data/cavell.csv", index=False)


### Frequency analysis in Benchmark
word_dict_benchmark = significantly_different(
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="Benchmark", suffix="brackets"),
                **select_corpus(id="Benchmark", suffix="brackets", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="Benchmark", suffix="clean"),
                **select_corpus(id="Benchmark", suffix="clean", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    pvalue=0.5,
)

df_significance_benchmark = pd.concat(
    [
        pd.merge(
            pd.DataFrame.from_dict(
                word_dict_benchmark[title]["greater"], orient="index"
            )
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_in"}),
            pd.DataFrame.from_dict(word_dict_benchmark[title]["less"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_out"}),
            how="outer",
            on="word",
        )
        .merge(
            pd.DataFrame.from_dict(word_dict_benchmark[title]["count"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "count"}),
            how="outer",
            on="word",
        )
        .assign(title=title)
        for title in word_dict_benchmark
    ]
)[["title", "word", "pvalue_in", "pvalue_out", "count"]]


df_significance_benchmark = pd.concat(
    [
        df_significance_benchmark[["title", "word", "count", "pvalue_in"]]
        .dropna()
        .assign(more_or_less="More")
        .rename(columns={"pvalue_in": "pvalue"}),
        df_significance_benchmark[["title", "word", "count", "pvalue_out"]]
        .dropna()
        .assign(more_or_less="Less")
        .rename(columns={"pvalue_out": "pvalue"}),
    ]
)

df_significance_benchmark = (
    df_significance_benchmark.merge(
        df_significance_benchmark[df_significance_benchmark.title == "corpus"].rename(
            columns={
                "more_or_less": "in_corpus",
                "pvalue": "in_corpus_pvalue",
                "count": "in_corpus_count",
            }
        )[["word", "in_corpus_count", "in_corpus_pvalue", "in_corpus"]],
        how="left",
        on="word",
    )
    .rename(columns={"title": "author"})
    .sort_values(["author", "more_or_less", "pvalue"], ascending=[True, False, True])
)

df_significance_benchmark["author"] = df_significance_benchmark["author"].apply(
    lambda x: names[x]
)

df_significance_benchmark[
    (df_significance_benchmark["count"] > 0)
    & (df_significance_benchmark["pvalue"] <= 0.1)
].to_csv("data/benchmark_frequency.csv", index=False)

df_significance_benchmark[
    ["in_corpus", "in_corpus_pvalue", "in_corpus_count"]
] = df_significance_benchmark[
    ["in_corpus", "in_corpus_pvalue", "in_corpus_count"]
].apply(
    lambda x: pd.Series(list(x))
    if ((x.in_corpus_pvalue <= 0.01) and (x.in_corpus_count >= 10))
    else pd.Series(["", nan, nan]),
    axis=1,
)

with pd.ExcelWriter("data/interesting_benchmark.xlsx") as writer1:
    df_significance_benchmark[
        (df_significance_benchmark.author == "corpus")
        & (df_significance_benchmark["count"] >= 10)
        & (df_significance_benchmark["pvalue"] <= 0.01)
    ].merge(
        df_significance_benchmark[df_significance_benchmark.author != "corpus"].pivot(
            index="word", columns="author", values="more_or_less"
        ),
        how="left",
        on="word",
    ).drop(
        ["in_corpus", "in_corpus_pvalue", "in_corpus_count"], axis=1
    ).to_excel(
        writer1, sheet_name="corpus", index=False
    )
    for author in df_significance_benchmark.author.unique():
        if author != "corpus":
            df_significance_benchmark[
                (df_significance_benchmark.author == author)
                & (df_significance_benchmark["count"] >= 10)
                & (df_significance_benchmark["pvalue"] <= 0.01)
            ].to_excel(
                writer1,
                sheet_name=author.replace(":", "")
                .replace("?", "")
                .replace("(", "")
                .replace(")", "")
                .replace(",", ""),
                index=False,
            )

### Frequency analysis in Cavell

word_dict_others = significantly_different(
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="Others", suffix="brackets"),
                **select_corpus(id="Others", suffix="brackets", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="Others", suffix="clean"),
                **select_corpus(id="Others", suffix="clean", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    pvalue=0.5,
)

df_significance_others = pd.concat(
    [
        pd.merge(
            pd.DataFrame.from_dict(word_dict_others[title]["greater"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_in"}),
            pd.DataFrame.from_dict(word_dict_others[title]["less"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_out"}),
            how="outer",
            on="word",
        )
        .merge(
            pd.DataFrame.from_dict(word_dict_others[title]["count"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "count"}),
            how="outer",
            on="word",
        )
        .assign(title=title)
        for title in word_dict_others
    ]
)[["title", "word", "pvalue_in", "pvalue_out", "count"]]


df_significance_others = pd.concat(
    [
        df_significance_others[["title", "word", "count", "pvalue_in"]]
        .dropna()
        .assign(more_or_less="More")
        .rename(columns={"pvalue_in": "pvalue"}),
        df_significance_others[["title", "word", "count", "pvalue_out"]]
        .dropna()
        .assign(more_or_less="Less")
        .rename(columns={"pvalue_out": "pvalue"}),
    ]
)

df_significance_others = df_significance_others[
    df_significance_others.title == "corpus"
].rename(
    columns={
        "more_or_less": "in_benchmark",
        "pvalue": "in_benchmark_pvalue",
        "count": "in_benchmark_count",
    }
)[
    ["word", "in_benchmark_count", "in_benchmark_pvalue", "in_benchmark"]
]

word_dict_cavell = significantly_different(
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="CavellAll", suffix="brackets"),
                **select_corpus(id="Cavell", suffix="brackets", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="CavellAll", suffix="clean"),
                **select_corpus(id="Cavell", suffix="clean", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    pvalue=0.5,
)

df_significance_cavell = pd.concat(
    [
        pd.merge(
            pd.DataFrame.from_dict(word_dict_cavell[title]["greater"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_in"}),
            pd.DataFrame.from_dict(word_dict_cavell[title]["less"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_out"}),
            how="outer",
            on="word",
        )
        .merge(
            pd.DataFrame.from_dict(word_dict_cavell[title]["count"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "count"}),
            how="outer",
            on="word",
        )
        .assign(title=title)
        for title in word_dict_cavell
    ]
)[["title", "word", "pvalue_in", "pvalue_out", "count"]]


df_significance_cavell = pd.concat(
    [
        df_significance_cavell[["title", "word", "count", "pvalue_in"]]
        .dropna()
        .assign(more_or_less="More")
        .rename(columns={"pvalue_in": "pvalue"}),
        df_significance_cavell[["title", "word", "count", "pvalue_out"]]
        .dropna()
        .assign(more_or_less="Less")
        .rename(columns={"pvalue_out": "pvalue"}),
    ]
)

df_significance_cavell = (
    df_significance_cavell.merge(
        df_significance_cavell[df_significance_cavell.title == "corpus"].rename(
            columns={
                "more_or_less": "in_corpus",
                "pvalue": "in_corpus_pvalue",
                "count": "in_corpus_count",
            }
        )[["word", "in_corpus_count", "in_corpus_pvalue", "in_corpus"]],
        how="left",
        on="word",
    )
    .merge(
        df_significance_others,
        how="left",
        on="word",
    )
    .sort_values(["title", "more_or_less", "pvalue"], ascending=[True, False, True])
)

df_significance_cavell["title"] = df_significance_cavell["title"].apply(
    lambda x: names[x]
)

df_significance_cavell[
    (df_significance_cavell["count"] > 0) & (df_significance_cavell["pvalue"] <= 0.1)
].to_csv("data/cavell_frequency.csv", index=False)

df_significance_cavell[
    ["in_corpus", "in_corpus_pvalue", "in_corpus_count"]
] = df_significance_cavell[["in_corpus", "in_corpus_pvalue", "in_corpus_count"]].apply(
    lambda x: pd.Series(list(x))
    if ((x.in_corpus_pvalue <= 0.01) and (x.in_corpus_count >= 10))
    else pd.Series(["", nan, nan]),
    axis=1,
)
df_significance_cavell[
    ["in_benchmark", "in_benchmark_pvalue", "in_benchmark_count"]
] = df_significance_cavell[
    ["in_benchmark", "in_benchmark_pvalue", "in_benchmark_count"]
].apply(
    lambda x: pd.Series(list(x))
    if ((x.in_benchmark_pvalue <= 0.01) and (x.in_benchmark_count >= 10))
    else pd.Series(["", nan, nan]),
    axis=1,
)

with pd.ExcelWriter("data/interesting_cavell.xlsx") as writer2:
    df_significance_cavell[
        (df_significance_cavell.title == "corpus")
        & (df_significance_cavell["count"] >= 10)
        & (df_significance_cavell["pvalue"] <= 0.01)
    ].merge(
        df_significance_cavell[df_significance_cavell.title != "corpus"].pivot(
            index="word", columns="title", values=["more_or_less", "in_corpus"]
        ),
        how="left",
        on="word",
    ).drop(
        ["in_corpus", "in_corpus_pvalue", "in_corpus_count"], axis=1
    ).to_excel(
        writer2, sheet_name="corpus", index=False
    )
    for title in df_significance_cavell.title.unique():
        if title != "corpus":
            df_significance_cavell[
                (df_significance_cavell.title == title)
                & (df_significance_cavell["count"] >= 10)
                & (df_significance_cavell["pvalue"] <= 0.01)
            ].to_excel(
                writer2,
                sheet_name=title.replace(":", "")
                .replace("?", "")
                .replace("(", "")
                .replace(")", "")
                .replace(",", ""),
                index=False,
            )

### Frequency analysis in brackets after .?!

# from brackets
word_dict_dot = significantly_different(
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="CavellAll", suffix="dot_brackets"),
                **select_corpus(id="Cavell", suffix="dot_brackets", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="CavellAll", suffix="brackets"),
                **select_corpus(id="Cavell", suffix="brackets", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    pvalue=0.5,
)

df_significance_dot = pd.concat(
    [
        pd.merge(
            pd.DataFrame.from_dict(word_dict_dot[title]["greater"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_in"}),
            pd.DataFrame.from_dict(word_dict_dot[title]["less"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_out"}),
            how="outer",
            on="word",
        )
        .merge(
            pd.DataFrame.from_dict(word_dict_dot[title]["count"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "count"}),
            how="outer",
            on="word",
        )
        .assign(title=title)
        for title in word_dict_dot
    ]
)[["title", "word", "pvalue_in", "pvalue_out", "count"]]


df_significance_dot = pd.concat(
    [
        df_significance_dot[["title", "word", "count", "pvalue_in"]]
        .dropna()
        .assign(more_or_less_brackets="More")
        .rename(columns={"pvalue_in": "pvalue_brackets"}),
        df_significance_dot[["title", "word", "count", "pvalue_out"]]
        .dropna()
        .assign(more_or_less_brackets="Less")
        .rename(columns={"pvalue_out": "pvalue_brackets"}),
    ]
)

# from text
word_dict_dot_t = significantly_different(
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="CavellAll", suffix="dot_brackets"),
                **select_corpus(id="Cavell", suffix="dot_brackets", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    count_and_frequency(
        tokenize_dict(
            {
                **select_corpus(id="CavellAll", suffix="clean"),
                **select_corpus(id="Cavell", suffix="clean", corpus=True),
            },
            skip_stopwords=False,
            keep_punctation=True,
        ),
        skip_stopwords=False,
    ),
    pvalue=0.5,
)

df_significance_dot_t = pd.concat(
    [
        pd.merge(
            pd.DataFrame.from_dict(word_dict_dot_t[title]["greater"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_in"}),
            pd.DataFrame.from_dict(word_dict_dot_t[title]["less"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "pvalue_out"}),
            how="outer",
            on="word",
        )
        .merge(
            pd.DataFrame.from_dict(word_dict_dot_t[title]["count"], orient="index")
            .reset_index()
            .rename(columns={"index": "word", 0: "count"}),
            how="outer",
            on="word",
        )
        .assign(title=title)
        for title in word_dict_dot
    ]
)[["title", "word", "pvalue_in", "pvalue_out", "count"]]


df_significance_dot_t = pd.concat(
    [
        df_significance_dot_t[["title", "word", "pvalue_in"]]
        .dropna()
        .assign(more_or_less_text="More")
        .rename(columns={"pvalue_in": "pvalue_text"}),
        df_significance_dot_t[["title", "word", "pvalue_out"]]
        .dropna()
        .assign(more_or_less_text="Less")
        .rename(columns={"pvalue_out": "pvalue_text"}),
    ]
)

df_significance_dot = df_significance_dot.merge(
    df_significance_dot_t, how="outer", on=["title", "word"]
)

df_significance_dot = df_significance_dot.merge(
    df_significance_dot[df_significance_dot.title == "corpus"].rename(
        columns={
            "more_or_less_brackets": "in_corpus_brackets",
            "pvalue_brackets": "in_corpus_brackets_pvalue",
            "more_or_less_text": "in_corpus_text",
            "pvalue_text": "in_corpus_text_pvalue",
            "count": "in_corpus_count",
        }
    )[
        [
            "word",
            "in_corpus_count",
            "in_corpus_brackets_pvalue",
            "in_corpus_brackets",
            "in_corpus_text_pvalue",
            "in_corpus_text",
        ]
    ],
    how="left",
    on="word",
).sort_values(
    ["title", "more_or_less_brackets", "pvalue_brackets"], ascending=[True, False, True]
)

df_significance_dot["title"] = df_significance_dot["title"].apply(lambda x: names[x])

df_significance_dot = df_significance_dot.merge(
    df_significance_cavell[["word", "title", "count", "pvalue", "more_or_less"]].rename(
        columns={
            "more_or_less": "in_brackets",
            "pvalue": "in_brackets_pvalue",
            "count": "in_brackets_count",
        }
    ),
    how="left",
    on=["word", "title"],
)

df_significance_dot[
    (df_significance_dot["count"] > 0)
    & (
        (df_significance_dot["pvalue_text"] <= 0.1)
        | (df_significance_dot["pvalue_brackets"] <= 0.1)
    )
].to_csv("data/cavell_dot_frequency.csv", index=False)

df_significance_dot[
    ["in_corpus_brackets", "in_corpus_brackets_pvalue", "in_corpus_count"]
] = df_significance_dot[
    ["in_corpus_brackets", "in_corpus_brackets_pvalue", "in_corpus_count"]
].apply(
    lambda x: pd.Series(list(x))
    if ((x.in_corpus_brackets_pvalue <= 0.01) and (x.in_corpus_count >= 10))
    else pd.Series(["", nan, nan]),
    axis=1,
)
df_significance_dot[
    ["in_corpus_text", "in_corpus_text_pvalue", "in_corpus_count"]
] = df_significance_dot[
    ["in_corpus_text", "in_corpus_text_pvalue", "in_corpus_count"]
].apply(
    lambda x: pd.Series(list(x))
    if ((x.in_corpus_text_pvalue <= 0.01) and (x.in_corpus_count >= 10))
    else pd.Series(["", nan, nan]),
    axis=1,
)
df_significance_dot[
    ["in_brackets", "in_brackets_pvalue", "in_brackets_count"]
] = df_significance_dot[
    ["in_brackets", "in_brackets_pvalue", "in_brackets_count"]
].apply(
    lambda x: pd.Series(list(x))
    if ((x.in_brackets_pvalue <= 0.01) and (x.in_brackets_count >= 10))
    else pd.Series(["", nan, nan]),
    axis=1,
)

with pd.ExcelWriter("data/interesting_dot_cavell.xlsx") as writer3:
    df_significance_dot[
        (df_significance_dot.title == "corpus")
        & (df_significance_dot["count"] >= 10)
        & (
            (df_significance_dot["pvalue_text"] <= 0.01)
            | (df_significance_dot["pvalue_brackets"] <= 0.01)
        )
    ].merge(
        df_significance_dot[df_significance_dot.title != "corpus"].pivot(
            index="word",
            columns="title",
            values=["more_or_less_brackets", "more_or_less_text", "in_brackets"],
        ),
        how="left",
        on="word",
    ).drop(
        [
            "in_corpus_brackets",
            "in_corpus_text",
            "in_corpus_brackets_pvalue",
            "in_corpus_text_pvalue",
            "in_corpus_count",
        ],
        axis=1,
    ).to_excel(
        writer3, sheet_name="corpus", index=False
    )
    for title in df_significance_dot.title.unique():
        if title != "corpus":
            df_significance_dot[
                (df_significance_dot.title == title)
                & (df_significance_dot["count"] >= 10)
                & (
                    (df_significance_dot["pvalue_text"] <= 0.01)
                    | (df_significance_dot["pvalue_brackets"] <= 0.01)
                )
            ].to_excel(
                writer3,
                sheet_name=title.replace(":", "")
                .replace("?", "")
                .replace("(", "")
                .replace(")", "")
                .replace(",", ""),
                index=False,
            )
