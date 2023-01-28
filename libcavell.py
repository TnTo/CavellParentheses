# pylint disable=anomalous-backslash-in-string

import re
import os
from glob import glob
from unidecode import unidecode
from itertools import chain

from nltk.tokenize import word_tokenize
from nltk import FreqDist

from nltk.downloader import download as nltk_download

nltk_download("stopwords")
nltk_download("punkt")

from nltk.corpus import stopwords as sw

stopwords = set(sw.words("english"))

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

from nltk.stem.wordnet import WordNetLemmatizer

lemma = WordNetLemmatizer()


def load_text(dir, suffix="", corpus=False, as_list=False):
    text_dict = {}
    if suffix:
        suffix = "_" + suffix
    for file in glob(dir + "/*.txt"):
        if as_list:
            text_dict[file[(len(dir) + 1) : -(4 + len(suffix))]] = (
                open(file).read().splitlines()
            )
        else:
            text_dict[file[(len(dir) + 1) : -(4 + len(suffix))]] = open(file).read()
    if corpus:
        return get_corpus(text_dict, as_list=as_list)
    else:
        return text_dict


def get_corpus(text_dict, as_list=False):
    if as_list:
        return {"corpus": list(chain.from_iterable(text_dict.values()))}
    else:
        return {"corpus": "\n".join(text_dict.values())}


def clean(text, title="", output_dir=None, output_suffix="clean"):
    text = unidecode(text)
    text = re.sub(r"[^A-Za-z0-9()\[\]<>.,:;'!\?\"\-\s]*", "", text)
    text = re.sub("\t", " ", text)
    text = re.sub(r"[ ]+", " ", text)
    text = re.sub(r"\n\s+\n", "\n", text)
    text = re.sub(r"\n-\n", "\n", text)
    text = re.sub(r"-\n", "-", text)
    text = re.sub(r"[-]+", "-", text)
    text = re.sub(r"\n[0-9\s\-]+\n", "\n", text)
    text = re.sub(r"[A-Z ]{7,}", "", text)
    text = re.sub(r"\n+", r"\n", text)
    if output_dir:
        if output_suffix:
            output_suffix = "_" + output_suffix
        file = open(output_dir + "/" + title + output_suffix + ".txt", "w")
        file.write(text)
        file.close()
    return text


def extract_brackets(
    text,
    title="",
    brackets_type=all,
    dot=False,
    output_dir=None,
    output_suffix="brackets",
):
    regex = ""
    round_regex = "\([^()]*(?:\([^()]*\)[^()]*)*\)"
    square_regex = "\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]"
    if dot == True:
        regex = regex + "[\.\?\!]\s*("
    if brackets_type == "round":
        regex = regex + round_regex
    elif brackets_type == "square":
        regex = regex + square_regex
    else:
        regex = regex + round_regex + "|" + square_regex
    if dot == True:
        regex = regex + ")"
    regex = re.compile(regex)

    brackets = re.findall(regex, text)
    brackets = [br for br in brackets if not re.search(r"^[^A-OQ-Za-oq-z]*$", br)]
    brackets = [br for br in brackets if not re.search(r"^[\(\[][CRcr][\)\]]$", br)]
    brackets = [br for br in brackets if not re.search(r"^[\(\[][ivlx]{2,}[\)\]]$", br)]
    brackets = [
        br
        for br in brackets
        if not re.search(
            r"^[\(\[][^A-Za-z]*[B-HJ-RT-Zb-hj-rt-z]{1}[^A-Za-z]*[\)\]]$", br
        )
    ]
    brackets = [re.sub(r"\n", " ", br) for br in brackets]

    if output_dir:
        if output_suffix:
            output_suffix = "_" + output_suffix
        file = open(output_dir + "/" + title + output_suffix + ".txt", "w")
        for br in brackets:
            file.write(br + "\n")
        file.close()
    return brackets


def discard_brackets(
    text, title="", brackets_type=all, output_dir=None, output_suffix="no_brackets"
):
    head_regex = None
    mid_regex = None
    tail_regex = None

    if brackets_type == "round":
        head_regex = r"^[^()]*\("
        mid_regex = r"\)[^()]*\("
        tail_regex = r"\)[^()]*$"
    elif brackets_type == "square":
        head_regex = r"^[^\[\]]*\["
        mid_regex = r"\][^\[\]]*\["
        tail_regex = r"\][^\[\]]*$"
    else:
        head_regex = r"^[^()\[\]]*[(\[]"
        mid_regex = r"[)\]][^()\[\]]*[(\[]"
        tail_regex = r"[)\]][^()\[\]]*$"

    no_brackets = (
        re.findall(head_regex, text)
        + re.findall(mid_regex, text)
        + re.findall(tail_regex, text)
    )
    no_brackets = [re.sub(r"\n", " ", br) for br in no_brackets]

    if output_dir:
        if output_suffix:
            output_suffix = "_" + output_suffix
        file = open(output_dir + "/" + title + output_suffix + ".txt", "w")
        for br in no_brackets:
            file.write(br + "\n")
        file.close()
    return no_brackets


def find_error(text, title="", output_dir=None, output_suffix="errors"):
    errors = re.findall(r"\)[^(]*\)|\([^)]\(|\][^\[]\]|\[[^\]]\[", text)
    errors = [re.sub(r"\n", " ", err) for err in errors]

    if output_dir:
        if output_suffix:
            output_suffix = "_" + output_suffix
        if len(errors) > 0:
            file = open(output_dir + "/" + title + output_suffix + ".txt", "w")
            for err in errors:
                file.write(err + "\n")
            file.close()
    return errors


def tokenize(
    text,
    do_filter=True,
    skip_stopwords=True,
    do_stem=False,
    do_lem=False,
    keep_punctation=False,
):
    tkns = word_tokenize(text)
    if do_filter:
        if keep_punctation:
            tkns = map(lambda tkn: re.sub(r"[^a-z\?\!\.\,\;]+", "", tkn.lower()), tkns)
            tkns = filter(
                lambda tkn: re.search(r"^.*[a-oq-z\?\!\.\,\;]+.*$", tkn), tkns
            )
        else:
            tkns = map(lambda tkn: re.sub(r"[^a-z]+", "", tkn.lower()), tkns)
            tkns = filter(lambda tkn: re.search(r"^.*[a-oq-z]+.*$", tkn), tkns)
        tkns = filter(lambda tkn: not re.search(r"^[ivxl]{2,}$", tkn), tkns)
        if keep_punctation:
            tkns = filter(lambda tkn: not re.search(r"^[^ia\?\!\.\,\;]{1}$", tkn), tkns)
        else:
            tkns = filter(lambda tkn: not re.search(r"^[^ia]{1}$", tkn), tkns)
        tkns = list(tkns)
    if skip_stopwords:
        tkns = [tkn for tkn in tkns if tkn not in stopwords]
    if do_lem:
        tkns = list(map(lemma.lemmatize, tkns))
    if do_stem:
        tkns = list(map(stemmer.stem, tkns))
    return tkns


def freq(tkns, skip_stopwords=True):
    tot = len(tkns)
    if skip_stopwords:
        tkns = [tkn for tkn in tkns if tkn not in stopwords]
    fq = FreqDist(tkns).items()
    fq = [[item[0], item[1], item[1] / tot] for item in fq]
    fq.sort(key=lambda x: x[1], reverse=True)
    return fq


if __name__ == "__main__":
    texts = load_text("txt")
    for title in texts:
        clean(texts[title], title=title, output_dir="txt/clean")
    texts = load_text("txt/clean", suffix="clean")
    for title in texts:
        print(title)
        extract_brackets(texts[title], title=title, output_dir="txt/brackets")
        extract_brackets(
            texts[title],
            title=title,
            dot=True,
            output_dir="txt/dot_brackets",
            output_suffix="dot_brackets",
        )
        discard_brackets(texts[title], title=title, output_dir="txt/no_brackets")
        find_error(texts[title], title=title, output_dir="txt/errors")
