#%%
import pandas as pd
import numpy as np
import matplotlib

# matplotlib.use("pgf")
# matplotlib.rcParams.update(
#    {
#        "pgf.texsystem": "pdflatex",
#        "font.family": "serif",
#        "text.usetex": True,
#        "pgf.rcfonts": False,
#    }
# )
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text

sns.set_style("whitegrid")
sns.set_context(context="paper", font_scale=1.25)

#%%
plt.clf()

df = pd.read_csv("data/benchmark.csv")
df = df.sort_values(by="brackets_ratio", ascending=False)
df.brackets_length = df.brackets_length.apply(eval)
df = df.rename(
    columns={
        "brackets_ratio": "parentheses_ratio",
        "dot_brackets_ratio": "dot_parentheses_ratio",
        "n_brackets": "n_parentheses",
        "brackets_length": "parentheses_length",
    }
)

school_palette = {
    "Most cited analytical": "tab:red",
    "Anti-teorethical": "tab:blue",
    "Master": "tab:green",
    "Cavell": "tab:orange",
}

#%%
g = sns.pairplot(
    df,
    x_vars=["parentheses_ratio", "dot_parentheses_ratio", "r2"],
    y_vars=["author"],
    hue="school",
    height=5,
    aspect=0.6,
    diag_kind=None,
    markers=["H", "s", "o", "D"],
    plot_kws={"s": 50},
    palette=school_palette,
)
g._legend.remove()
g.add_legend(
    bbox_to_anchor=(0.37, 0.24),
    frameon=True,
    label_order=["Cavell", "Master", "Anti-teorethical", "Most cited analytical"],
)
g._legend.set_title(None)
g.axes.flatten()[0].set_ylabel("")
plt.tight_layout()
plt.savefig("paper/benchmark.pdf")
# plt.show()

#%%
df["normalized_parentheses_number"] = df["n_parentheses"] / df["length"]
g = sns.pairplot(
    df,
    x_vars=["length", "n_parentheses", "normalized_parentheses_number"],
    y_vars=["author"],
    hue="school",
    height=5,
    aspect=0.6,
    diag_kind=None,
    markers=["H", "s", "o", "D"],
    plot_kws={"s": 50},
    palette=school_palette,
)
g._legend.remove()
g.add_legend(
    loc="center left",
    bbox_to_anchor=(0.85, 0.25),
    frameon=True,
    label_order=["Cavell", "Master", "Anti-teorethical", "Most cited analytical"],
)
g._legend.set_title(None)
g.axes.flatten()[0].set_ylabel("")
plt.tight_layout()
plt.savefig("paper/benchmark2b.pdf", bbox_inches="tight")

#%%
g = sns.pairplot(
    df,
    x_vars=["length", "n_parentheses"],
    y_vars=["author"],
    hue="school",
    height=5,
    aspect=0.6,
    diag_kind=None,
    markers=["H", "s", "o", "D"],
    plot_kws={"s": 50},
    palette=school_palette,
)
g._legend.remove()
g.add_legend(
    loc="center left",
    bbox_to_anchor=(0.85, 0.25),
    frameon=True,
    label_order=["Cavell", "Master", "Anti-teorethical", "Most cited analytical"],
)
g._legend.set_title(None)
g.axes.flatten()[0].set_ylabel("")
plt.tight_layout()
plt.savefig("paper/benchmark2.pdf", bbox_inches="tight")

#%%
fig, ax = plt.subplots(figsize=(9, 5))
bp = sns.boxplot(
    y="author",
    x="parentheses_length",
    data=df.explode("parentheses_length"),
    hue="school",
    palette=school_palette,
    fliersize=3,
    width=0.7,
    dodge=False,
)
bp.set(xlim=(-1, None))
bp.set_ylabel("")
# bp.set(xscale="log")
# bp.set_xticklabels(bp.get_xticklabels(), rotation=-80)
# df.explode("parentheses_length").boxplot(by="author", column="parentheses_length")
plt.tight_layout()
plt.savefig("paper/benchmark3.pdf")

#%%
fig, ax = plt.subplots(figsize=(9, 5))
bp = sns.boxplot(
    y="author",
    x="parentheses_length",
    data=df.explode("parentheses_length"),
    hue="school",
    palette=school_palette,
    fliersize=3,
    width=0.7,
    dodge=False,
)
bp.set(xlim=(-1, 30))
bp.set_ylabel("")
# bp.set(xscale="log")
# bp.set_xticklabels(bp.get_xticklabels(), rotation=-80)
# df.explode("parentheses_length").boxplot(by="author", column="parentheses_length")
ax.legend_.remove()
plt.tight_layout()
plt.savefig("paper/benchmark4.pdf")

#%%
plt.clf()

df2 = pd.read_csv("data/cavell.csv")
df2 = df2.sort_values(by=["year", "title"], ascending=[False, True])
df2.brackets_length = df2.brackets_length.apply(eval)
df2 = df2.rename(
    columns={
        "brackets_ratio": "parentheses_ratio",
        "dot_brackets_ratio": "dot_parentheses_ratio",
        "n_brackets": "n_parentheses",
        "brackets_length": "parentheses_length",
    }
)


#%%
g = sns.pairplot(
    df2,
    x_vars=["parentheses_ratio", "dot_parentheses_ratio", "r2"],
    y_vars=["title"],
    height=5,
    aspect=0.9,
    diag_kind=None,
    plot_kws={"s": 30},
)
g.axes.flatten()[0].set_ylabel("")
plt.tight_layout()
plt.savefig("paper/time.pdf")
# plt.show()


#%%
g = sns.pairplot(
    df2,
    x_vars=["length", "n_parentheses"],
    y_vars=["title"],
    height=5,
    aspect=0.9,
    diag_kind=None,
    plot_kws={"s": 30},
)
g.axes.flatten()[0].set_ylabel("")
plt.tight_layout()
plt.savefig("paper/time2.pdf")

#%%
fig, ax = plt.subplots(figsize=(9, 5))
bp = sns.boxplot(
    y="title",
    x="parentheses_length",
    data=df2.explode("parentheses_length"),
    fliersize=3,
    width=0.7,
    dodge=False,
    color="tab:blue",
)
bp.set(xlim=(-1, None))
bp.set_ylabel("")
# bp.set(xscale="log")
# bp.set_xticklabels(bp.get_xticklabels(), rotation=-80)
# df.explode("parentheses_length").boxplot(by="author", column="parentheses_length")
plt.tight_layout()
plt.savefig("paper/time3.pdf")

#%%
fig, ax = plt.subplots(figsize=(9, 5))
bp = sns.boxplot(
    y="title",
    x="parentheses_length",
    data=df2.explode("parentheses_length"),
    fliersize=3,
    width=0.7,
    dodge=False,
    color="tab:blue",
)
bp.set(xlim=(-1, 50))
bp.set_ylabel("")
# bp.set(xscale="log")
# bp.set_xticklabels(bp.get_xticklabels(), rotation=-80)
# df.explode("parentheses_length").boxplot(by="author", column="parentheses_length")
# ax.legend_.remove()
plt.tight_layout()
plt.savefig("paper/time4.pdf")


#

# %%
