@echo off
set /p start_num="Ingrese el numero de inicio: "
set /p end_num="Ingrese el numero final: "

set /a num=%start_num%

:loop
if %num% gtr %end_num% (
    goto :eof
) else (
    mkdir %num%
    set /a num+=1
    goto :loop
)
