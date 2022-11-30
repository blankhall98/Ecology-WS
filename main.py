##########################
#PROJECT MANAGER: DANIEL ÁVILA
#SOFTWARE DEVELOPER: JONATAN BLANK
#TEAM: CENTRO MEXICANO DE ECOLOGÍA INDUSTRIAL
##########################

#PYTHON PACKAGES
'''
STEPS:
1. Read "http://sinat.semarnat.gob.mx/Gaceta/aniosgaceta" and download PDF files for all years available
2. Read PDF files and obtain unique project code
3. Create database with projects most relevant information
4. Use the unique project code to access ____________ and obtain _____________
5. Save all information in relational database
'''

##########
# STEP 1
# Note: PDF files will be downloaded at ./raw_data/PDF/
##########

from scripts import download_semarnat_pdfs
#run function that downloads pdfs
download_semarnat_pdfs()
