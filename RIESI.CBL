       IDENTIFICATION DIVISION.
       PROGRAM-ID. RIESI.
       DATA DIVISION.
           WORKING-STORAGE SECTION.
               01 FROG PIC A(50).
               01 RIBBIT PIC A(50).
       PROCEDURE DIVISION.
           ACCEPT FROG.
           MOVE FUNCTION UPPER-CASE(FROG) TO RIBBIT.
           IF RIBBIT = "RIESI"
               DISPLAY RIBBIT
           ELSE
               DISPLAY "NOT RIESI"
           .
