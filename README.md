# Cowrie Log Analyzer
Cowrie Log Analzer (CLA) is a Python\TKinter program which analyzes cowrie honeypot json log files and shows useful research information.

Two things makes CLA different than other cowrie log analyzers. The first is the notion of history. CLA retains parsed data in persistent database storage. The second is the notion of search.

## Input
CLA consumes cowrie JSON log files. The optimal and expected operation is to consume a single JSON.

## IP Addresses
CLA captures source IP address and source IP port.   

## Messages
CLA captures and deconstructs *messages*. The message types CLA targets are:
   1. login attempt [cowrie.login.success]  
      a. usernames  
      b. passwords  

   2. commands [cowrie.command.input]  
      a. single command or single line sequential command input  
      b. sequential command input exploded

   3. downloads [cowrie.session.file_download]  
      a. url  
      b. destination file  

   4. session duration [cowrie.session.connect -> cowrie.session.closed]  
      a. session id (session)  
      b. session duration (time in seconds)

### Data Analysis
CLA offers two types of data analysis: text and graph.

#### Text Analysis Output:
**Top Tens**
1. Top 10 source IP Addresses
2. Top 10 attempted usernames
3. Top 10 attempted passwords
4. Top 10 attempted username & password pairs
5. Top 10 downloaded file object (name)
6. Top 10 source countries (geoip lookup on source IP)
7. Top 10 session durations

**Overall**
1. Most common source IP (frequency)
2. Most common username (frequency)
3. Most common password (frequency)
4. Most common username & password pair (frequency)
5. Most common source country
6. Longest session duration

#### Graph Analysis Output:
**Histograms**
1. Source IP addresses by frequency (top ten)
2. Source countries by frequency (top ten)
3. Session duration by duration (top ten)

## Artifacts
CLA tracks file downloads but does not *download* artifacts.

## Output
CLA generates text and graphical output. The text output is simple and displayed in the program GUI. The graphical output consists of basic charts (e.g., line, histogram) that can be exported.

## Storage
Concurrently, CLA persists data to a sqlite3 database. The schema is as follows:

#### Main Database
- id: Integer
- type: Text
- ip address: Text
- username: Text
- password: Text
- filename: Text
- country: Text
- duration: Real
- date/time: datetime
- message: Text

#### Commands Database
- Foreign id: Integer
- Command: String

#### Country Database
##### This site or product includes IP2Location LITE data available from http://www.ip2location.com.

- ip_from: Integer
- ip_to: Integer
- country_code: Text
- country_name: Text
