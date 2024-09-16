Composer Attribution of Renaissance Motets (Iberian Polyphony around 1500): MIDIs and Extracted Features
Rodríguez-García, Esperanza; McKay, Cory

This distribution includes MIDI files used in the experiments described in the "Composer Attribution of Renaissance Motets: A Case Study Using Statistical Features and Machine Learning" chapter of the book The Anatomy of Iberian Polyphony around 1500. Multi-part motets have been separated out into separate MIDI files. We edited the files for consistency, which included adjusting elements that could interfere with encoding rhythm consistently (e.g. standardized rhythmic value rates, eliminating fermatas, etc.).

The MIDI files in the nonIb_noMB group were taken from the Josquin Research Project (JRP), who have kindly granted us permission to re-publish them here with our modifications. These are redistributed with a "CC BY-SA 4.0" license: https://github.com/josquin-research-project/jrp-scores/blob/master/LICENSE.txt. The Iberian MIDI files were produced from editions created by The Anatomy of Late 15th- and Early 16th-Century Iberian Polyphonic Music project (https://iberianpolyphonicmusic.wordpress.com), and are included here after our modifications, with permission. We digitised the nonIb_MBonly MIDI files ourselves using Sibelius. All these files are distributed under a "CC BY-SA 4.0" license" license (https://creativecommons.org/licenses/by-sa/4.0/). The included "Catalogue.pdf" file outlines the contents of this corpus in its entirety.

This distribution also includes the "Renaissance-safe" features extracted using jSymbolic 2.2 (http://jmir.sourceforge.net) from the MIDI encodings included here. Details on all the features extracted with the software are available in the jSymbolic manual (http://jmir.sourceforge.net/manuals/jSymbolic_manual/home.html). These are presented as follows:

- FeatureDefinitions.xml: Descriptions of all extracted features, encoded in ACE XML 1.0, as output directly by jSymbolic. This file does not include any feature values (these are found in the FeatureValues.xml file).

- FeatureValues.xml: Extracted feature values, encoded in ACE XML 1.0, as output directly by jSymbolic. The features are described in the FeatureDefinitions.xml file. Class values are implied by the folder containing each MIDI file.

- FeatureValues_BasicCSV: Extracted feature values encoded in a CSV file, as output directly by jSymbolic (with complete file paths truncated). Class values are implied by the folder containing each MIDI file.

- FeatureValues_HumanReadable.xlsx: Extracted features formatted into a human-readable Microsoft Excel file. Group averages and standard deviations have been added to the bottom, and the "Length_In_Breves" feature is added in a column at the right (it is included separately because it is not calculated directly by jSymbolic 2.2).

- FeatureValues_WekaReady.csv: Extracted feature values encoded in a CSV file in a format readable by Weka (https://www.cs.waikato.ac.nz/ml/weka/). Class values have been added in a column on the right, and file paths have been removed, as required by Weka.
