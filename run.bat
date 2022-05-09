CLS
ECHO OFF
SET HOME=%CD%
SET CD_=CD src
%CD_%
SET callpy=python main.py
%callpy%
ECHO DONE ECHO. && ECHO. && PAUSE
