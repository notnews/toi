## The Life and Times of The Times of India






### Scripts

* [Parse ToI](scripts/0_parse.py)

fields

Version
RecordID
DateTimeStamp
ActionCode
RecordTitle
PublicationID
PublicationTitle (eg-The Times of India (1861-current)
Qualifier (eg-mumbai, india)
Publisher (eg-Bennett, Coleman &amp; Company Limited)
AlphaPubDate
NumericPubDate
SourceType (eg-historical newspapers)
ObjectType (eg-Feature)
ObjectType (eg-Article)
ContribRole (eg-Author)
OriginalForm (eg-Meena Iyer TNN)
LanguageCode (eg-ENG)
StartPage (eg-9)
URLDocView (eg- proquest url link)
HasFullText (eg-true)
Abstract
FullText
  

* [Basic Analyses](scripts/01_basic.R)
	1. number of articles per issue (by pub_date/year/month/weekday--weekend)
	2. number of words per article/title over time
	3. number of classified ads (on startpage == 1)
	4. articles by contributor w/ TNN (rest are presumably sourced via AP etc.)
	5. number of ads (on startpage == 1)
	6. gender, caste etc. of contributors -- histogram of top 50 surnames
	7. number of contributors per article
	8. US vs. USSR/Russia etc.
	9. matrimonial ads: "caste no bar", 'fair complexion', etc.

* [NER](02_ner.R)

* [NER analyses](03_ner_analyses.R)
	1. Histogram of top 50 people covered.
	2. Histogram of top 50 places covered
	3. Gender of people mentioned
	
* [Annotation]()
	1. editorial/news
	2. news/not news
	3. gov vs. not in ads
	4. episodic'---x happened vs. 'thematic' --- more detailed/contextual piece
	5. local/national/foreign news
