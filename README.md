# Cowrie Log Analyzer
Cowrie Log Analzer (CLA) is a Python\TKinter program which analyzes cowrie honeypot json log files and shows useful research information.

What makes CLA different than other cowrie log analyzers is the notion of history. CLA retains analysis in persistent storage

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

### Other

## Artifacts
CLA tracks file downloads but does not *download* artifacts.

## Output
CLA generates text and graphical output. The text output is simple and displayed in the program GUI. The graphical output consists of basic charts (e.g., line, histogram) that can be exported.

Concurrently, CLA persists data to storage.
