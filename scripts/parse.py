from xml.etree import ElementTree as ET
import glob
from joblib import Parallel, delayed
import pandas as pd

def toiParse(x):
    xmlstring = open(x).read().strip()
    recid    = ET.fromstring(xmlstring).find('RecordID')
    recid    = recid.text.strip() if recid is not None else None
    prqid    = ET.fromstring(xmlstring).find('URLDocView')
    prqid    = prqid.text.strip() if prqid is not None else None
    dt       = ET.fromstring(xmlstring).find('AlphaPubDate')
    dt       = dt.text.strip() if dt is not None else None
    title    = ET.fromstring(xmlstring).find('RecordTitle')
    title    = title.text.strip() if title is not None else None
    fulltext = ET.fromstring(xmlstring).find('FullText')
    fulltext = fulltext.text.strip() if fulltext is not None else None
    return {'id': recid, 'proquestId': prqid,
            'date': dt, 'title' : title, 'text': fulltext}

######################################################################
# paths
root = "/home/users/apoorval/aa_home/ToI/"

######################################################################
# dry run
# toiParse(xmls[5555])
# res = [toiParse(xmls[1234]), toiParse(xmls[4321])]
# pd.DataFrame(res).info()

######################################################################
# first zip
xmls1 = glob.glob(root + 'raw/xml1/' + "*.xml")
# parallelise across 16 cores
res = Parallel(n_jobs = 16)(delayed(toiParse)(x) for x in xmls1)
# convert to dataframe
df = pd.DataFrame(res)
# write
df.to_csv(root + "outData/ToIData1.csv")

######################################################################

xmls2 = glob.glob(root + 'raw/xml2/' + "*.xml")
# parallelise across 16 cores
res = Parallel(n_jobs = 16)(delayed(toiParse)(x) for x in xmls2)
# convert to dataframe
df = pd.DataFrame(res)
# write
df.to_csv(root + "outData/ToIData2.csv")

######################################################################

xmls3 = glob.glob(root + 'raw/xml3/' + "*.xml")
# parallelise across 16 cores
res = Parallel(n_jobs = 16)(delayed(toiParse)(x) for x in xmls3)
# convert to dataframe
df = pd.DataFrame(res)
# write
df.to_csv(root + "outData/ToIData3.csv")

######################################################################

xmls4 = glob.glob(root + 'raw/xml4/' + "*.xml")
# parallelise across 16 cores
res = Parallel(n_jobs = 16)(delayed(toiParse)(x) for x in xmls4)
# convert to dataframe
df = pd.DataFrame(res)
# write
df.to_csv(root + "outData/ToIData4.csv")

######################################################################
