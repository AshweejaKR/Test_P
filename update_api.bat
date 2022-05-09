CLS
@ECHO OFF
@SET HOME=%CD%
REM CALL %HOME%\Env.bat
SET callpy=python update_api.py
%callpy%
ECHO. && ECHO. && PAUSE
