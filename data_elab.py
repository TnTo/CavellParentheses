# %%
import pandas as pd

pd.set_option("display.latex.multicolumn", True)

# %%
dfs = pd.read_excel("data/interesting_benchmark.xlsx", sheet_name=None)

latex = ""

for author in dfs:
    if author not in ["corpus", "Cavell"]:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[author][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        cols[0] = " "
        df.columns = pd.MultiIndex.from_product([[author], cols])
        if len(df) > 0:
            latex += df.to_latex(
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"List of significant words in parentheses for {author}",
                label=f"tab:{author}",
                column_format="rrll",
                longtable=True,
                position="h",
                multicolumn=True,
            )
        latex += "\n"
with open("paper/bench_tables.tex", "w") as f:
    f.write(latex)


#%%
# Fodor

dfs = pd.read_excel("data/interesting_benchmark.xlsx", sheet_name=None)

for author in ["Fodor"]:
    if True:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[author][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        df = df[df.pvalue < 10e-8]
        df = df[df.more_or_less == "More"]
        cols[0] = " "
        df.columns = pd.MultiIndex.from_product([[author], cols])
        if len(df) > 0:
            df.to_latex(
                f"paper/{author}.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"List of significant words in parentheses for {author}. More (frequent) refer to the frequences inside the parentheses compared to the whole text.",
                label=f"tab:{author}_short",
                column_format="rrll",
                longtable=True,
                position="t",
                multicolumn=True,
            )

for author in ["Putnam"]:
    if True:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[author][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        df = df[df.pvalue < 10e-10]
        df = df[df.more_or_less == "More"]
        cols[0] = " "
        df.columns = pd.MultiIndex.from_product([[author], cols])
        if len(df) > 0:
            df.to_latex(
                f"paper/{author}.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"List of significant words in parentheses for {author}. More (frequent) refer to the frequences inside the parentheses compared to the whole text.",
                label=f"tab:{author}_short",
                column_format="rrll",
                longtable=True,
                position="t",
                multicolumn=True,
            )

for author in ["Dummett"]:
    if True:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[author][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        df = df[
            df.word.isin(
                [
                    "fn",
                    "bound",
                    "relations",
                    "number",
                    "term",
                    "functions",
                    "singular",
                    "variable",
                    "category",
                    "operator",
                ]
            )
        ]
        df = df[df.more_or_less == "More"]
        cols[0] = " "
        df.columns = pd.MultiIndex.from_product([[author], cols])
        if len(df) > 0:
            df.to_latex(
                f"paper/{author}.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"List of chosen significant words in parentheses for {author}. More (frequent) refer to the frequences inside the parentheses compared to the whole text.",
                label=f"tab:{author}_short",
                column_format="rrll",
                longtable=True,
                position="t",
                multicolumn=True,
            )

# %%
dfs = pd.read_excel("data/interesting_cavell.xlsx", sheet_name=None)

latex = ""

for title in dfs:
    if title not in ["corpus"]:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[title][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        cols[0] = " "
        df.columns = pd.MultiIndex.from_product([[title], cols])
        if len(df) > 0:
            latex += df.to_latex(
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"List of significant words in parentheses in {title}",
                label=f"tab:{title}",
                column_format="rrll",
                longtable=True,
                position="ht",
                multicolumn=True,
            )
        latex += "\n"
    else:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[title][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        cols[0] = " "
        df.columns = cols
        if len(df) > 0:
            df.to_latex(
                "paper/cavell_corpus_table.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"List of significant words in parentheses for Cavell's corpus",
                label=f"tab:CavellCorpus",
                column_format="rrll",
                longtable=True,
                position="h",
                multicolumn=True,
            )

with open("paper/cavell_tables.tex", "w") as f:
    f.write(latex)

# %%
# Interisting a lot
dfs = pd.read_excel("data/interesting_cavell.xlsx", sheet_name=None)

latex = ""

for title in ["corpus"]:
    if True:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[title][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        df = df[df.more_or_less == "More"]
        cols[0] = " "
        df.columns = cols
        if len(df) > 0:
            df.to_latex(
                "paper/intint.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"List of words significantly more frequent in parentheses for Cavell's corpus, which are not significantly more frequent in parentheses for benchmark corpus",
                label=f"tab:Phil",
                column_format="rrll",
                longtable=True,
                position="h",
                multicolumn=True,
            )


# %%
# example
# Used
dfs = pd.read_excel("data/interesting_cavell.xlsx", sheet_name=None)

latex = ""

for title in ["corpus"]:
    if True:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[title][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        df = df[df.more_or_less == "More"]
        df = df[
            df.word.isin(
                [
                    "e.g.",
                    "i.e.",
                    "example",
                    "as",
                    "like",
                ]
            )
        ]
        cols[0] = " "
        df.columns = cols
        if len(df) > 0:
            df.to_latex(
                "paper/example.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"Count and significance p-value for expressions which introduce an example significantly more frequent in parentheses for Cavell's corpus",
                label=f"tab:example",
                column_format="rrll",
                longtable=False,
                position="h",
                multicolumn=True,
            )

# %%
# conj
# Used
dfs = pd.read_excel("data/interesting_cavell.xlsx", sheet_name=None)

latex = ""

for title in ["corpus"]:
    if True:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[title][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        df = df[df.more_or_less == "More"]
        df = df[
            df.word.isin(
                [
                    "or",
                    "though",
                    "perhaps",
                    "as",
                    "?",
                    ",",
                    "except",
                    "hence",
                    "in",
                    "like",
                    "unless",
                    "later",
                    "explicitly",
                    "anyway",
                    "here",
                    "notably",
                    "not",
                    "especially",
                    "doubtless",
                    "grammatically",
                ]
            )
        ]
        cols[0] = " "
        df.columns = cols
        if len(df) > 0:
            df.to_latex(
                "paper/conj.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"Count and significance p-value for conjunctions, prepositions, adverbs and punctation significantly more frequent in parentheses for Cavell's corpus",
                label=f"tab:conj",
                column_format="rrll",
                longtable=False,
                position="h",
                multicolumn=True,
            )

# %%
# phil
# Used
dfs = pd.read_excel("data/interesting_cavell.xlsx", sheet_name=None)

latex = ""

for title in ["corpus"]:
    if True:
        cols = [
            "more_or_less",
            "word",
            "count",
            "pvalue",
        ]
        df = dfs[title][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "pvalue": float,
                "more_or_less": str,
            }
        )
        df = df[df.more_or_less == "More"]
        df = df[
            df.word.isin(
                [
                    "thoreau",
                    "hegel",
                    "heidegger",
                    "nietzsche",
                    "wittgenstein",
                    "descartes",
                    "kant",
                    "emerson",
                    "kripke",
                    "moore",
                    "hume",
                    "austin",
                    "dewey",
                    "luther",
                    "lacan",
                    "lewis",
                    "hyppolytus",
                ]
            )
        ]
        cols[0] = " "
        df.columns = cols
        if len(df) > 0:
            df.to_latex(
                "paper/phil.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption=f"Count and significance p-value for philosophers' names significantly more frequent in parentheses for Cavell's corpus",
                label=f"tab:Phil",
                column_format="rrll",
                longtable=False,
                position="h",
                multicolumn=True,
            )

# %%
dfs = pd.read_excel("data/interesting_dot_cavell.xlsx", sheet_name=None)

latex = ""

for title in dfs:
    if title in ["corpus"]:
        cols = [
            "word",
            "count",
            "more_or_less_brackets",
            "more_or_less_text",
        ]
        df = dfs[title][cols]
        df = df.astype(
            {
                "word": str,
                "count": int,
                "more_or_less_brackets": str,
                "more_or_less_text": str,
            }
        )
        cols[2] = "vs_brackets"
        cols[3] = "vs_text"
        df.columns = cols
        if len(df) > 0:
            df.to_latex(
                "paper/cavell_dot_corpus_table.tex",
                index=False,
                na_rep="",
                float_format="%.2e",
                caption="List of significant words in parentheses after a mark for Cavell's corpus",
                label="tab:CavellDotCorpus",
                column_format="rrll",
                longtable=True,
                position="h",
                multicolumn=True,
            )

with open("paper/cavell_dot_tables.tex", "w") as f:
    f.write(latex)

# %%
