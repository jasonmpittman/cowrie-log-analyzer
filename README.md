# Cowrie Log Analyzer
Cowrie Log Analzer (CLA) is a Python\TKinter program which analyzes cowrie honeypot json log files and shows useful research information.

Two things makes CLA different than other cowrie log analyzers. The first is the notion of history. CLA retains parsed data in persistent database storage. The second is the notion of search. 

## Input
CLA consumes cowrie JSON log files. The optimal and expected operation is to consume a single JSON.

## IP Addresses
CLA captures source IP address and source IP port.   

## Messages
CLA captures and deconstructs *messages*. The message types CLA targets are:
   1. login attempt  
      a. usernames  
      b. passwords  
   2. CMD
   3.

### Data Analysis
CLA offers two types of data analysis: text and graph.

#### Text Analysis Output:
1. Top 10 source IP Addresses
2. Top 10 attempted usernames
3. Top 10 attempted passwords
4. Top 10 attempted username & password pairs
5. Top 10 downloaded file object (name)
5. Top 10 source countries (geoip lookup on source IP)

Overall--
1. Most common source IP (frequency)
2. Most common username (frequency)
3. Most common password (frequency)
4. Most common username & password pair (frequency)
5. Most common source country

## Artifacts
CLA tracks file downloads but does not *download* artifacts.

## Output
CLA generates text and graphical output. The text output is simple and displayed in the program GUI. The graphical output consists of basic charts (e.g., line, histogram) that can be exported.

## Storage
Concurrently, CLA persists data to a sqlite3 database. 
