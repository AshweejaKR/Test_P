CLS
ECHO OFF
SET HOME=%CD%
REM CALL %HOME%\Env.bat
SET callpy=python setup.py
%callpy%
ECHO. && ECHO. && PAUSE
