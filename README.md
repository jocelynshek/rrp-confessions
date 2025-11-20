This tool automatically downloads publicly available documents from the  [Jurisdicción Especial para la Paz (JEP)](https://www.jep.gov.co/macrocasos/) website in Colombia.  It visits **Cases 01–11**, saves the HTML pages and linked PDFs, extracts readable text, and organizes everything for later qualitative analysis.

When you run the script, it will:
1. Visit each case page on the JEP Macrocasos website (Case 01 → Case 11).  
2. Download the main page and any linked PDFs.  
3. Extract text from each document.  
4. Save everything neatly into folders:  
   - `data/html` → saved webpages  
   - `data/pdfs` → downloaded PDFs  
   - `data/texts` → extracted text files  
   - `data/all_macrocasos_text.txt` → one big text file for searching  
   - `jep_all_macrocasos.csv` → summary index of all files  

## To install (only once):
- **Python 3.9 or newer** (the programming language)
- **VS Code** (a program to open and run the script)
- A few small Python libraries used by the crawler

## Step-by-step setup (first time only)

### 1. Install Python

Go to [python.org/downloads](https://www.python.org/downloads/), download the latest version for your computer.  

### 2. Install VS Code
Download from [code.visualstudio.com](https://code.visualstudio.com).  
Open it once installed.

### 3. Clone project from GitHub into VS Code
Copy this repository link: https://github.com/jocelynshek/rrp-confessions
In VS Code, open the View → Command Palette → Git: Clone command
(or press Ctrl + Shift + P / Cmd + Shift + P and type “Git: Clone”).

Paste the link when asked.
Choose where you’d like the folder saved (for example, Desktop).
When it finishes, VS Code will ask:
“Would you like to open the cloned repository?” → click Open!

### 4. Open a terminal inside VS Code

In the top menu: **View → Terminal**.  
A panel opens at the bottom: this is where you’ll type commands.

### 5. Create a virtual environment
This keeps all the software for this project in its own safe place. In the terminal, type:
python -m venv myenv
source myenv/bin/activate

We want to see (myenv) at the beginning of the prompt!

### 6. Install directories
pip install -r requirements.txt

Wait for the installation to finish: you should see lines mentioning requests, beautifulsoup4, lxml, and pdfminer.six.

## Running program
In jep-scrape.ipynb, click the play button (triangle) on the left of the first chunk of code! It also has notes if you want to read through.

The program will print which page it’s working on (you’ll see messages like “Crawling Case 03…”), download files into the data/ folder, and create jep_all_macrocasos.csv and data/all_macrocasos_text.txt when finished.
Note that this will probably take 10-20 minutes!

### Files
After the script finishes, open the folder data/:
Folder / File &	What it contains
data/html:	saved web pages
data/pdfs:	downloaded PDF documents
data/texts:	text extracted from PDFs and pages
data/all_macrocasos_text.txt:	all text combined (searchable)
jep_all_macrocasos.csv:	summary index of URLs and saved paths

These can be searched, coded, or uploaded into MAXQDA for qualitative analysis.

## Keyword tool
This tool helps identify which downloaded JEP documents contain specific Spanish keywords or phrases related to sexual violence and abuse. Then you can review thoes files manually.
The tool looks through all text files created by the crawler in `data/texts/` then searches for a list of keywords (the one we are making together). To run, in jep-scrape.ipynb, click the play button on the second chunk of code!
This will a summary spreadsheet called **`keyword_hits.csv`** in your main project folder, showing:
- The file name (find the corresponding one in data/texts/)
- Which keywords were found
- A short text snippet for context

Errors come up or you have any questions? Ask me on WhatsApp or use Google/ChatGPT to troubleshoot!
