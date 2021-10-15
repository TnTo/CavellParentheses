# pylint disable=abstract-class-instantiated

from libcavell import load_text, tokenize, freq, stopwords, get_corpus

from tabulate import tabulate
from scipy import stats
import pandas as pd
import numpy as np
from contextlib import redirect_stdout
import csv
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
import re


def select_corpus(id="Cavell", suffix="", corpus=False, as_list=False):
    if suffix:
        text_dict = load_text("txt/" + suffix, suffix=suffix, as_list=as_list)
    else:
        text_dict = load_text("txt", as_list=as_list)
    if id == "Cavell":
        titles = [
            "contesting_tears",
            "cities_of_words",
            "pursuits_of_happiness",
            "little_did_i_know",
            # 'emersons_trascendental',
            "must_we_mean_what_we_say",
            # 'disowning_knowledge_in_seven_plays_of_shakespeare',
            "a_pitch_of_philosophy",
            "this_new_yet_unapproachable_america",
            "the_senses_of_walden",
            "the_world_viewed",
            "the_claim_of_reason",
            "in_quest_of_the_ordinary",
            "themes_out_of_school",
            "philosophy_the_day_after",
            "conditions_handsome_and_unhandsome",
            # 'cavell_on_film'
            "philosophical_passages",
        ]
        text_dict = {title: text_dict[title] for title in titles}
    elif id == "Benchmark":
        titles = [
            "burge",
            "fodor",
            "foot",
            "wittgenstein",
            "anscombe",
            "baier",
            "dummett",
            "macintyre",
            "frege",
            "williamson",
            "the_claim_of_reason",
            "wright",
            "diamond",
            "mcdowell",
            "austin",
            "quine",
            "russell",
            "lewis",
            "kripke",
            "davidson",
            "putnam",
            "winch",
            "murdoch",
            "williams",
        ]
        text_dict = {title: text_dict[title] for title in titles}
        text_dict["cavell"] = text_dict["the_claim_of_reason"]
        text_dict.pop("the_claim_of_reason")
    elif id == "Others":
        titles = [
            "burge",
            "fodor",
            "foot",
            "wittgenstein",
            "anscombe",
            "baier",
            "dummett",
            "macintyre",
            "frege",
            "williamson",
            "wright",
            "diamond",
            "mcdowell",
            "austin",
            "quine",
            "russell",
            "lewis",
            "kripke",
            "davidson",
            "putnam",
            "winch",
            "murdoch",
            "williams",
        ]
        text_dict = {title: text_dict[title] for title in titles}
    elif id == "CavellTime":
        titles = [
            "must_we_mean_what_we_say",
            "the_claim_of_reason_1",
            "the_senses_of_walden_1",
            "the_world_viewed_1",
            "disowning_knowledge_in_seven_plays_of_shakespeare_2",
            "pursuits_of_happiness",
            "themes_out_of_school",
            "the_claim_of_reason_2",
            "the_senses_of_walden_2",
            "the_world_viewed_2",
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
            "little_did_i_know",
            # 'cavell_on_film',
            "philosophy_the_day_after",
        ]
        text_dict = {title: text_dict[title] for title in titles}
    elif id == "r2_an":
        titles = ["fodor", "dummett", "kripke", "davidson"]
        text_dict = {title: text_dict[title] for title in titles}
    elif id == "r2_sim":
        titles = ["wittgenstein", "diamond", "austin", "putnam"]
        text_dict = {title: text_dict[title] for title in titles}
    elif id == "CavellAll":
        titles = [
            "must_we_mean_what_we_say",
            "the_claim_of_reason",
            "the_senses_of_walden",
            "the_world_viewed",
            "the_claim_of_reason_1",
            "the_senses_of_walden_1",
            "the_world_viewed_1",
            # 'disowning_knowledge_in_seven_plays_of_shakespeare',
            # 'disowning_knowledge_in_seven_plays_of_shakespeare_2',
            "pursuits_of_happiness",
            "themes_out_of_school",
            "the_claim_of_reason_2",
            "the_senses_of_walden_2",
            "the_world_viewed_2",
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
            "little_did_i_know",
            # 'cavell_on_film',
            "philosophy_the_day_after",
        ]
        text_dict = {title: text_dict[title] for title in titles}
    elif id == "all":
        pass
    else:
        print("ID unknown")
    if corpus:
        return get_corpus(text_dict, as_list=as_list)
    else:
        return text_dict


def tokenize_dict(text_dict, as_list=False, *args, **kwargs):
    if not as_list:
        return {title: tokenize(text_dict[title], **kwargs) for title in text_dict}
    else:
        return {
            title: [tokenize(bracket, **kwargs) for bracket in text_dict[title]]
            for title in text_dict
        }


def brackets_ratio(text_tkn_dict, brackets_tkn_dict):
    ratio = {}
    for title in text_tkn_dict:
        ratio[title] = len(brackets_tkn_dict[title]) / len(text_tkn_dict[title])
    return ratio


def brackets_length(brackets_tkn_dict_list):
    lenghts = {}
    for title in brackets_tkn_dict_list:
        lenghts[title] = [len(bracket) for bracket in brackets_tkn_dict_list[title]]
    return lenghts


def count_and_frequency(text_tkn_dict, **kwargs):
    text_freq_dict = {}
    for title in text_tkn_dict:
        text_freq_dict[title] = {
            item[0]: [item[1], item[2]] for item in freq(text_tkn_dict[title], **kwargs)
        }
    return text_freq_dict


def correlation(text_freq_dict_x, text_freq_dict_y):
    correlation = {}
    for title in set(text_freq_dict_x.keys()) & set(text_freq_dict_y.keys()):
        count1 = []
        count2 = []
        for word in set(text_freq_dict_x[title].keys()) | set(
            text_freq_dict_y[title].keys()
        ):
            if (
                word in text_freq_dict_x[title].keys()
                and word in text_freq_dict_y[title].keys()
            ):
                count1.append(text_freq_dict_x[title][word][0])
                count2.append(text_freq_dict_y[title][word][0])
            elif word in text_freq_dict_x[title].keys():
                count1.append(text_freq_dict_x[title][word][0])
                count2.append(0)
            else:
                count1.append(0)
                count2.append(text_freq_dict_y[title][word][0])
        correlation[title] = stats.pearsonr(np.array(count1), np.array(count2))
    return correlation


def significantly_different(text_freq_dict_test, text_freq_dict_true, pvalue=0.05):
    significantly = {}
    for title in set(text_freq_dict_test.keys()) & set(text_freq_dict_true.keys()):
        data = {}
        tot_test = 0
        for word in set(text_freq_dict_test[title].keys()) | set(
            text_freq_dict_true[title].keys()
        ):
            if (
                word in text_freq_dict_test[title].keys()
                and word in text_freq_dict_true[title].keys()
            ):
                data[word] = {
                    "count_test": text_freq_dict_test[title][word][0],
                    "freq_true": text_freq_dict_true[title][word][1],
                }
                tot_test += text_freq_dict_test[title][word][0]
            elif word in text_freq_dict_test[title].keys():
                data[word] = {
                    "count_test": text_freq_dict_test[title][word][0],
                    "freq_true": 0.0,
                }
                tot_test += text_freq_dict_test[title][word][0]
            else:
                data[word] = {
                    "count_test": 0,
                    "freq_true": text_freq_dict_true[title][word][1],
                }
        greater = {}
        less = {}
        for word in data:
            greater[word] = stats.binom_test(
                data[word]["count_test"],
                n=tot_test,
                p=data[word]["freq_true"],
                alternative="greater",
            )
            less[word] = stats.binom_test(
                data[word]["count_test"],
                n=tot_test,
                p=data[word]["freq_true"],
                alternative="less",
            )
        greater = sorted(greater.items(), key=lambda item: item[1])
        less = sorted(less.items(), key=lambda item: item[1])
        greater = {word: value for (word, value) in greater if value <= pvalue}
        less = {word: value for (word, value) in less if value <= pvalue}
        count = {
            word: data[word]["count_test"]
            for word in set(greater.keys()) | set(less.keys())
        }
        significantly[title] = {"greater": greater, "less": less, "count": count}
    return significantly


def time_analysis():
    time_corpus_token = tokenize_dict(
        select_corpus(id="CavellTime", suffix="clean"), skip_stopwords=False
    )
    time_corpus_brackets_token = tokenize_dict(
        select_corpus(id="CavellTime", suffix="brackets"), skip_stopwords=False
    )
    time_corpus_dot_brackets_token = tokenize_dict(
        select_corpus(id="CavellTime", suffix="dot_brackets"), skip_stopwords=False
    )

    period = {
        "1958-1972": [
            "must_we_mean_what_we_say",
            "the_claim_of_reason_1",
            "the_senses_of_walden_1",
            "the_world_viewed_1",
        ],
        "1983-1987": [
            # "disowning_knowledge_in_seven_plays_of_shakespeare_2",
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
            # "disowning_knowledge_in_seven_plays_of_shakespeare_3",
            # "disowning_knowledge_in_seven_plays_of_shakespeare_pref",
            # "emersons_trascendental",
            "in_quest_of_the_ordinary",
            "philosophical_passages",
            "this_new_yet_unapproachable_america",
        ],
        "2005-2010": [
            "little_did_i_know",
            "philosophy_the_day_after",
            # "cavell_on_film",
        ],
    }

    year = {
        "must_we_mean_what_we_say": 1969,
        "the_claim_of_reason_1": 1972,
        "the_senses_of_walden_1": 1972,
        "the_world_viewed_1": 1971,
        # "disowning_knowledge_in_seven_plays_of_shakespeare_2": 1987,
        "pursuits_of_happiness": 1981,
        "themes_out_of_school": 1984,
        "the_claim_of_reason_2": 1979,
        "the_senses_of_walden_2": 1980,
        "the_world_viewed_2": 1979,
        "a_pitch_of_philosophy": 1994,
        "cities_of_words": 2004,
        "conditions_handsome_and_unhandsome": 1990,
        "contesting_tears": 1996,
        # "disowning_knowledge_in_seven_plays_of_shakespeare_3": 2003,
        # "disowning_knowledge_in_seven_plays_of_shakespeare_pref": 2003,
        # "emersons_trascendental": 2003,
        "in_quest_of_the_ordinary": 1988,
        "philosophical_passages": 1995,
        "this_new_yet_unapproachable_america": 1988,
        "little_did_i_know": 2010,
        "philosophy_the_day_after": 2005,
        # "cavell_on_film": 2005,
    }

    df = (
        pd.merge(
            pd.DataFrame.from_dict(
                brackets_ratio(time_corpus_token, time_corpus_brackets_token),
                orient="index",
                columns=["brackets_ratio"],
            )
            .reset_index()
            .rename(columns={"index": "title"}),
            pd.DataFrame.from_dict(
                brackets_ratio(time_corpus_token, time_corpus_dot_brackets_token),
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
                    count_and_frequency(time_corpus_token, skip_stopwords=True),
                    count_and_frequency(
                        time_corpus_brackets_token, skip_stopwords=True
                    ),
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
        .sort_values("year", ascending=False)
    )

    g = sns.pairplot(
        df,
        x_vars=["brackets_ratio", "dot_brackets_ratio", "r2"],
        y_vars=["title"],
        hue="period",
        hue_order=["1958-1972", "1983-1987", "1988-2004", "2005-2010"],
        height=5,
        diag_kind=None,
    )
    g._legend.remove()
    plt.tight_layout()
    plt.savefig("plot/time.pdf")

    return df


def benchmark_analysis():
    benchmark_corpus_token = tokenize_dict(
        select_corpus(id="Benchmark", suffix="clean"), skip_stopwords=False
    )
    benchmark_corpus_brackets_token = tokenize_dict(
        select_corpus(id="Benchmark", suffix="brackets"), skip_stopwords=False
    )
    benchmark_corpus_dot_brackets_token = tokenize_dict(
        select_corpus(id="Benchmark", suffix="dot_brackets"), skip_stopwords=False
    )

    school = {
        "master": ["austin", "wittgenstein"],
        "cavell": ["cavell"],
        "most cited analytical": [
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
        "anti-teorethical": [
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

    df = (
        pd.merge(
            pd.DataFrame.from_dict(
                brackets_ratio(benchmark_corpus_token, benchmark_corpus_brackets_token),
                orient="index",
                columns=["brackets_ratio"],
            )
            .reset_index()
            .rename(columns={"index": "author"}),
            pd.DataFrame.from_dict(
                brackets_ratio(
                    benchmark_corpus_token, benchmark_corpus_dot_brackets_token
                ),
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
        .sort_values("brackets_ratio", ascending=False)
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
    )

    # https://github.com/mwaskom/seaborn/issues/1865 for order
    # https://seaborn.pydata.org/generated/seaborn.scatterplot.html for ci ?
    g = sns.pairplot(
        df,
        x_vars=["brackets_ratio", "dot_brackets_ratio", "r2"],
        y_vars=["author"],
        hue="school",
        height=5,
        diag_kind=None,
    )
    g._legend.remove()
    plt.tight_layout()
    plt.savefig("plot/benchmark.pdf")

    return df


def significance_analysis(
    pvalue, min_count, corpus="Cavell", out="", dot_brackets=False, folder=""
):
    if dot_brackets:
        dot = "dot_"
    else:
        dot = ""
    word_dict = significantly_different(
        count_and_frequency(
            tokenize_dict(
                {
                    **select_corpus(id=corpus, suffix=dot + "brackets"),
                    **select_corpus(id=corpus, suffix=dot + "brackets", corpus=True),
                },
                skip_stopwords=False,
                keep_punctation=True,
            ),
            skip_stopwords=False,
        ),
        count_and_frequency(
            tokenize_dict(
                {
                    **select_corpus(id=corpus, suffix="clean"),
                    **select_corpus(id=corpus, suffix="clean", corpus=True),
                },
                skip_stopwords=False,
                keep_punctation=True,
            ),
            skip_stopwords=False,
        ),
        pvalue=pvalue,
    )

    df = pd.concat(
        [
            pd.merge(
                pd.DataFrame.from_dict(word_dict[title]["greater"], orient="index")
                .reset_index()
                .rename(columns={"index": "word", 0: "pvalue_in"}),
                pd.DataFrame.from_dict(word_dict[title]["less"], orient="index")
                .reset_index()
                .rename(columns={"index": "word", 0: "pvalue_out"}),
                how="outer",
                on="word",
            )
            .merge(
                pd.DataFrame.from_dict(word_dict[title]["count"], orient="index")
                .reset_index()
                .rename(columns={"index": "word", 0: "count"}),
                how="outer",
                on="word",
            )
            .assign(title=title)
            for title in word_dict
        ]
    )[["title", "word", "pvalue_in", "pvalue_out", "count"]]

    df = pd.concat(
        [
            df[["title", "word", "count", "pvalue_in"]]
            .dropna()
            .assign(more_or_less="More")
            .rename(columns={"pvalue_in": "pvalue"}),
            df[["title", "word", "count", "pvalue_out"]]
            .dropna()
            .assign(more_or_less="Less")
            .rename(columns={"pvalue_out": "pvalue"}),
        ]
    )

    df = df.merge(
        df[df.title == "corpus"].rename(columns={"more_or_less": "in_corpus"})[
            ["word", "in_corpus"]
        ],
        how="left",
        on="word",
    ).sort_values(["title", "more_or_less", "pvalue"], ascending=[True, False, True])

    with pd.ExcelWriter(folder + "interesting" + out + ".xlsx") as writer:
        df[(df.title == "corpus") & (df["count"] > min_count)].merge(
            df[df.title != "corpus"].pivot(
                index="word", columns="title", values="more_or_less"
            ),
            how="left",
            on="word",
        ).drop("in_corpus", axis=1).to_excel(writer, sheet_name="corpus", index=False)
        for title in df.title.unique():
            if title != "corpus":
                df[(df.title == title) & (df["count"] > (min_count / 5))].to_excel(
                    writer, sheet_name=title, index=False
                )

    return df


def lenght_plot(corpus="Cavell"):
    data_cavell = brackets_length(
        tokenize_dict(
            select_corpus(id=corpus, suffix="brackets", as_list=True),
            as_list=True,
            skip_stopwords=False,
        )
    )

    for title in data_cavell:
        sns.distplot(data_cavell[title], hist=False, kde=True, label=title)

    plt.legend()
    plt.show()


def brackets_position():
    text = select_corpus(suffix="clean")
    regex = re.compile(
        r"\([^()]*(?:\([^()]*\)[^()]*)*\)|\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]"
    )
    in_brackets = {}
    for title in text:
        in_brackets[title] = [0] * len(text[title])
        for m in re.finditer(regex, text[title]):
            in_brackets[title][m.start(0) : m.end(0)] = [1] * (m.end(0) - m.start(0))
        plt.plot(in_brackets[title], "b+", ms=0.1)
        plt.title(title)
        plt.show()


if __name__ == "__main__":

    # brackets_position()

    benchmark_analysis()
    time_analysis()
    # significance_analysis(0.05, 0)
    # significance_analysis(0.05, 0, corpus="Benchmark", out="_others")
    # significance_analysis(
    #    0.05, 0, corpus="Benchmark", out="_others_dot", dot_brackets=True
    # )

    # lenght_plot()
    # lenght_plot(corpus="Benchmark")
