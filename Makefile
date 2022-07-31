# Make the figures in ./$(FIG_DIR)/
FIG_DIR := ./figures
SCRIPTS_DIR := ./scripts
DATA_DIR := ./data
LF_DATA_DIR := ../toi-lf
LANGUAGE=python
EXECUTE_JUPYTERNB = cd $(SCRIPTS_DIR); $(LANGUAGE) utilities/run-ipynb.py $(<F) -q

NER_DATA := $(LF_DATA_DIR)/entity_type_year.csv.gz $(LF_DATA_DIR)/entity_type_agg.csv.gz \
			$(DATA_DIR)/toi_top1000_gpe.csv $(DATA_DIR)/toi_top1000_persons.csv


DATA_COVERAGE := data_coverage1838to1899 data_coverage1900to1949 data_coverage1950to2008
EDITORIALSCOMMENTARIES_IMAGES_CLASSIFIED := editorialscommentaries images classified_ads
LEXRICHNESS := text_number_of_words text_number_of_uniquewords text_lex_mtld
NUM_ARTICLES := number_articles_qtr number_articles_dow
TITLELENGTH := $(FIG_DIR)/titlelength.png $(FIG_DIR)/titlelength.pdf
MINORITY := minority_yearly_muslim minority_yearly_women minority_yearly_caste
PERSONPLACES := top50_persons top50_gpe 

DATA_COVERAGE := $(patsubst %, $(FIG_DIR)/%.png, $(DATA_COVERAGE)) $(patsubst %, $(FIG_DIR)/%.pdf, $(DATA_COVERAGE))
EDITORIALSCOMMENTARIES_IMAGES_CLASSIFIED := $(patsubst %, $(FIG_DIR)/%.png, $(EDITORIALSCOMMENTARIES_IMAGES_CLASSIFIED)) $(patsubst %, $(FIG_DIR)/%.pdf, $(EDITORIALSCOMMENTARIES_IMAGES_CLASSIFIED))
LEXRICHNESS := $(patsubst %, $(FIG_DIR)/%.png, $(LEXRICHNESS)) $(patsubst %, $(FIG_DIR)/%.pdf, $(LEXRICHNESS))
NUM_ARTICLES := $(patsubst %, $(FIG_DIR)/%.png, $(NUM_ARTICLES)) $(patsubst %, $(FIG_DIR)/%.pdf, $(NUM_ARTICLES))
MINORITY := $(patsubst %, $(FIG_DIR)/%.png, $(MINORITY)) $(patsubst %, $(FIG_DIR)/%.pdf, $(MINORITY))
PERSONPLACES := $(patsubst %, $(FIG_DIR)/%.png, $(PERSONPLACES)) $(patsubst %, $(FIG_DIR)/%.pdf, $(PERSONPLACES))
ALL_PLOTS := $(DATA_COVERAGE) $(EDITORIALSCOMMENTARIES_IMAGES_CLASSIFIED) $(LEXRICHNESS) $(NUM_ARTICLES) \
			$(TITLELENGTH) $(MINORITY) $(PERSONPLACES)

all: # Make all plots
all: figdir setup $(ALL_PLOTS)

$(DATA_COVERAGE): # Plots data coverage
$(DATA_COVERAGE): $(SCRIPTS_DIR)/data_coverage.ipynb $(DATA_DIR)/data_coverage.csv
	$(EXECUTE_JUPYTERNB)

$(EDITORIALSCOMMENTARIES_IMAGES_CLASSIFIED): # plot editorialcommentaries, images, and classifieds trends
$(EDITORIALSCOMMENTARIES_IMAGES_CLASSIFIED): $(SCRIPTS_DIR)/editorialscommentaries_images_classified.ipynb $(DATA_DIR)/editorialscommentaries_images_classified.csv
	$(EXECUTE_JUPYTERNB)

$(LEXRICHNESS): # Plot text and lexical richness trends
$(LEXRICHNESS): $(SCRIPTS_DIR)/lexicalrichness.ipynb $(DATA_DIR)/toi_textstat.csv.gz
	$(EXECUTE_JUPYTERNB)

$(NUM_ARTICLES): # Plot number of articles
$(NUM_ARTICLES): $(SCRIPTS_DIR)/number_of_articles.ipynb $(DATA_DIR)/number_articles_qtr.csv $(DATA_DIR)/number_articles_dow.csv
	$(EXECUTE_JUPYTERNB)

$(TITLELENGTH): # Plot title length
$(TITLELENGTH): $(SCRIPTS_DIR)/titlelength.ipynb $(DATA_DIR)/titlelength.csv
	$(EXECUTE_JUPYTERNB)

$(MINORITY): # Plot minority distributions
$(MINORITY): $(SCRIPTS_DIR)/plot-yearly-minority-dist.ipynb $(DATA_DIR)/toi_yearly_minority_dist.csv
	$(EXECUTE_JUPYTERNB)	

$(PERSONPLACES): # Plot top 50 persons and PERSONPLACES
$(PERSONPLACES): $(SCRIPTS_DIR)/top-people-places.ipynb $(DATA_DIR)/toi_top1000_gpe.csv $(DATA_DIR)/toi_top1000_persons.csv
	$(EXECUTE_JUPYTERNB)

$(NER_DATA): # Parse NER data from TOI
$(NER_DATA): $(SCRIPTS_DIR)/get_entity_type_year.ipynb $(LF_DATA_DIR)/ner/
	$(EXECUTE_JUPYTERNB) -t 100000000


.DEFAULT_GOAL := all

.PHONY: setup clean figdir help 

setup: # installs requirements
setup: requirements.txt
	@pip install -r $^

clean: # Purge all output files
	rm -f $(ALL_PLOTS) 

help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

figdir: # Make the build directory if it doesn't exist
figdir:
	mkdir -p $(FIG_DIR)