# Comparison groups
The benchmark groups used are:
* the whole corpus of other authors at once (used as benchmark for Cavell’s books)
* the whole corpus of other authors plus \citetitle{Claim} at once (used as benchmark for each of the book of the other authors)
* the whole corpus of Cavell’s book at once (used as benchmark for each Cavell’s book)
* the content of all the parentheses (used as benchmark for the content of the parentheses after a mark in Cavell’s books, individually and all at once)


# Dataset

Description of the dataset

## {benchmark,cavell}.csv
Measures as defined in paper for each text (and for the corpus all at once)

**author**: the author which the row is referred to. See the paper for the list of books considered. *benchmark* only

**title**: the Cavell's book the row is referred to, and eventually which part of the book. *cavell* only

**brackets&#95;ratio**: measure of the quantity of brackets in the text, as defined in paper.

**dot&#95;brackets&#95;ratio**: measure of the quantity of brackets after {.?!} in the text, as defined in paper.

**r2**: pearson coefficient between brackets frequency of words and all text frequency

**pvalue**: H0: r2 = 0

**school**: school to which the author belongs. *benchmark* only

**period**: period in which the book was published. *cavell* only

**year**: year in which the book was published. *cavell* only

**n&#95;brackets**: number of brackets

**lenght**: lenght of text measured in tokens

**brackets&#95;length**: list of the lenght of each bracket, measured in tokens

## {benchmark,cavell,cavell&#95;dot}&#95;brackets.csv
List of brackets (or brackets after {.?!} for *cavell&#95;dot*)

**brackets**: the bracket

**author**: identifier for the text in which the bracket appears. *benchmark* only

**title**: : identifier for the text in which the bracket appears. *{cavell,cavell&#95;dot}* only

## {benchmark,cavell,cavell&#95;dot}&#95;frequency.csv
Results of binomial test to compare frequency inside and outside brackets (pvalue <= 0.1)

**author**: identifier for the text in which the bracket appears. *benchmark* only

**title**: : identifier for the text in which the bracket appears. *{cavell,cavell&#95;dot}* only

**word**: word analyzed

**count**: occurrences of *word* inside the brackets (or brackets after {.?!} for *cavell&#95;dot*)

**pvalue**: pvalue of the binomial test against the frequency in the whole text (or inside all the brackets for *cavell&#95;dot*)

**more&#95;or&#95;less**: which tail of the test has been considered (i.e if the word is {more,less} frequent inside the brackets than in the whole text)

**in&#95;corpus**: if the word is significantly {more,less} frequent in the test performed on the entire corpus (i.e. all other authors' books plus the claim of reason for*benchmark*, all cavell's book considered (not only the "part" one) for *cavell*, all brackets from all cavell's book considered (not only the "part" one) for *cavell&#95;dot*)

**in&#95;benchmark**: if the word is significantly {more,less} frequent in the test performed on all other authors' books. *cavell* only

**in&#95;brackets**: if the word is significantly {more,less} frequent in the test performed on all cavell's book considered (not only the "part" one). *cavell&#95;dot* only

**{in&#95;corpus,in&#95;benchmark,in&#95;brackets}&#95;pvalue**: relative p-value

**{in&#95;corpus,in&#95;benchmark,in&#95;brackets}&#95;count**: relative count

## interesting&#95;{benchmark,cavell,dot&#95;cavell}.xlsx
{benchmark,cavell,cavell&#95;dot}&#95;frequency.csv pivoted wrt *{author,text}* with pvalue <= 0.01 amd count >= 10