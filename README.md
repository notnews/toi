## The Life and Times of The Times of India

Using the Proquest Times of India Corpus spanning 18XX--2008, we shed light on a slew of interesting questions. 

### Scripts

* [Parse ToI](scripts/01_parse_toi.ipynb)
  Parse XML to CSV. Here's the [data dictionary](data_dictionary.md)

* [Basic Analyses](scripts/01_basic.R)
	1. number of articles per issue (by pub_date/year/month/weekday--weekend)
	2. number of words per article/title over time
	3. number (proportion) of articles by contributor w/ TNN (rest are presumably sourced via AP etc. but good to groupby)
	4. gender, religion etc. of contributors -- histogram of top 50 names, surnames using [naampy]() and [pranaam]()
	5. number of contributors per article
 	6. number of editorial/news

* [NER](02_ner.R)

* [NER analyses](03_ner_analyses.R)
	1. Histogram of top 50 people covered.
	2. Histogram of top 50 places covered
	3. Gender, religion of people mentioned using [naampy]() and [pranaam]()

* Other Ideas
	1. number of classified ads (on startpage == 1)
	2. number of ads (on startpage == 1)
	3. US vs. USSR/Russia etc.
	4. matrimonial ads: "caste no bar", 'fair complexion', etc.
	5. Need Annotation
		* news/not news
		* gov vs. not in ads
		* episodic'---x happened vs. 'thematic' --- more detailed/contextual piece
		* local/national/foreign news
