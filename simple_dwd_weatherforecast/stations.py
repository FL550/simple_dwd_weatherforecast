stations = """
id    ICAO name                 nb.    el.     elev 
===== ---- -------------------- ------ ------- -----
EW002 ---- Beveringen            53.10   12.13    71 Brandenburg
EW003 ---- Calvoerde             52.25   11.19    55 Sachsen-Anhalt
EW004 ---- Dahlem-Berg           50.23    6.28   600 Nordrhein-Westfalen
EW005 ---- Delitzsch             51.30   12.23    99 Sachsen
EW006 ---- Emden                 53.20    7.09     0 Niedersachsen
EW007 ---- Foehr                 54.44    8.35     0 Schleswig-Holstein
EW008 ---- Freiamt               48.10    7.38   678 Baden-Württemberg
EW009 ---- Goosefeld             54.25    9.49    45 Schleswig-Holstein
EW010 ---- Hagen-Dahl            51.18    7.34   409 Nordrhein-Westfalen
EW011 ---- Hilkenbrook           52.59    7.42     7 Niedersachsen
EW012 ---- Kaiser-Wilhelm-Koog   53.56    8.57     0 Schleswig-Holstein
EW013 ---- Kroppach              50.41    7.43   358 Rheinland-Pfalz
EW015 ---- Podelzig              52.28   14.31    47 Brandenburg
EW016 ---- Rakow                 54.03   11.37     0 Mecklenburg-Vorpommern
EW017 ---- Rosenberg             49.27    9.29   359 Baden-Württemberg
EW018 ---- Rothwesten            51.23    9.32   287 Hessen
EW019 ---- Ruegen                54.30   13.20    11 Mecklenburg-Vorpommern
EW020 ---- St. Peter-Ording      54.19    8.38     0 Schleswig-Holstein
EW021 ---- Steinlah              52.04   10.20   161 Niedersachsen
EW022 ---- Steinsdorf            50.35   11.29   537 Thüringen
EW024 ---- Wangerland            53.42    7.50     0 Niedersachsen
EW025 ---- Wasbek                54.05    9.54    17 Schleswig-Holstein
EW026 ---- Weissenburg           49.02   11.04   606 Bayern
EW027 ---- Westfehmarn           54.31   11.03     0 Schleswig-Holstein
EW028 ---- Wuennenberg           51.34    8.46   370 Nordrhein-Westfalen
EW029 ---- Wusterhusen           54.06   13.37    24 Mecklenburg-Vorpommern
EW030 ---- Zapfendorf            50.00   10.56   370 Bayern
EW031 ---- EW-Lindenberg         52.10   14.07    73 Brandenburg
EW032 ---- Cabauw                52.22    5.20     0 Provinz Flevoland
EW034 ---- EW-Hamburg            53.31   10.06     0 Hamburg
EW035 ---- FINO1                 54.01    6.35     0 
EW036 ---- FINO2                 55.01   13.09     0 
EW037 ---- FINO3                 55.07    7.06     0 
EW038 ---- EW-Risoe              55.41   12.05     0 Region Sjælland
EW039 ---- EW-Roedeser-Berg      51.22    9.12   385 Hessen
10004 ---- UFS TW EMS            54.10    6.21     0 
10007 ---- UFS DEUTSCHE BUCHT    54.10    7.27     0 
10015 ---- HELGOLAND             54.11    7.54     4 
10020 ---- LIST/SYLT             55.01    8.25    26 Schleswig-Holstein
10022 EDXK LECK                  54.48    8.57     7 Schleswig-Holstein
10028 ---- ST. PETER ORDING      54.20    8.36     5 
10033 ETGG FLENSBURG             54.50    9.30    27 Schleswig-Holstein
10035 ---- SCHLESWIG             54.32    9.33    47 Schleswig-Holstein
10037 ETNS SCHLESWIG-JAGEL       54.28    9.31    22 Schleswig-Holstein
10038 ETNH HOHN                  54.19    9.32    10 Schleswig-Holstein
10042 ---- OLPENITZ              54.40   10.02     4 Schleswig-Holstein
10044 ---- LEUCHTTURM KIEL       54.30   10.17     5 
10046 EDHK KIEL-H.               54.23   10.09    28 Schleswig-Holstein
10055 ---- WESTERMARKELSDORF     54.32   11.04     3 Schleswig-Holstein
10091 ---- ARKONA                54.41   13.26    42 Mecklenburg-Vorpommern
10093 ---- PUTBUS                54.22   13.29    40 Mecklenburg-Vorpommern
10097 ---- GREIFSWALDER OIE      54.15   13.55    12 Mecklenburg-Vorpommern
10113 ---- NORDERNEY             53.43    7.09    11 
10122 ETNJ JEVER                 53.32    7.53     7 Niedersachsen
10126 ETNT WITTMUNDHAVEN         53.33    7.40     8 Niedersachsen
10129 ---- BREMERHAVEN           53.32    8.35     7 Bremen
10130 ---- ELPERSBUETTEL         54.04    9.01     3 Schleswig-Holstein
10131 ---- CUXHAVEN              53.52    8.42     5 Niedersachsen
10136 ETMN NORDHOLZ              53.46    8.40    23 Niedersachsen
10139 ---- BREMERVOERDE          53.30    9.10     3 Niedersachsen
10142 ETHI ITZEHOE               54.00    9.35    25 Schleswig-Holstein
10146 ---- QUICKBORN             53.44    9.53    13 Schleswig-Holstein
10147 EDDH HAMBURG-FU.           53.38   10.00    16 Hamburg
10150 ---- DOERNICK              54.10   10.21    26 Schleswig-Holstein
10152 ---- PELZERHAKEN           54.05   10.53     1 
10156 EDHL LUEBECK               53.49   10.42    14 Schleswig-Holstein
10161 ---- BOLTENHAGEN           54.00   11.12    15 
10162 ---- SCHWERIN              53.39   11.23    59 Mecklenburg-Vorpommern
10168 ---- GOLDBERG              53.36   12.06    58 Mecklenburg-Vorpommern
10170 ---- WARNEMUENDE           54.11   12.05     4 Mecklenburg-Vorpommern
10172 ETNL LAAGE                 53.55   12.17    42 Mecklenburg-Vorpommern
10180 ---- BARTH                 54.20   12.43     7 Mecklenburg-Vorpommern
10184 ---- GREIFSWALD            54.06   13.24     2 Mecklenburg-Vorpommern
10193 ---- UECKERMUENDE          53.45   14.04     1 Mecklenburg-Vorpommern
10200 ---- EMDEN-FLUGPLATZ       53.23    7.14     0 Niedersachsen
10215 EDWH OLDENBURG             53.11    8.10    11 Niedersachsen
10224 EDDW BREMEN                53.03    8.48     3 Bremen
10235 ---- SOLTAU                52.58    9.48    76 Niedersachsen
10238 ETGB BERGEN-HOHNE          52.49    9.56    70 Niedersachsen
10246 ETHS FASSBERG              52.55   10.11    75 Niedersachsen
10249 ---- BOIZENBURG            53.24   10.41    45 Mecklenburg-Vorpommern
10253 ---- LUECHOW               52.58   11.08    17 Niedersachsen
10261 ---- SEEHAUSEN             52.54   11.44    21 Sachsen-Anhalt
10264 ---- MARNITZ               53.19   11.56    81 Mecklenburg-Vorpommern
10267 ---- KYRITZ                52.56   12.25    40 Brandenburg
10268 ---- WAREN                 53.31   12.40    70 Mecklenburg-Vorpommern
10270 ---- NEURUPPIN             52.54   12.49    38 Brandenburg
10281 ETNU TROLLENHAGEN          53.36   13.18    71 Mecklenburg-Vorpommern
10282 ---- FELDBERG/MECKLENBURG  53.19   13.25   115 Mecklenburg-Vorpommern
10289 ---- GRUENOW               53.19   13.56    56 Brandenburg
10291 ---- ANGERMUENDE           53.02   14.00    56 Brandenburg
10305 ---- LINGEN                52.31    7.19    22 Niedersachsen
10306 ETHE RHEINE-BENTLAGE       52.18    7.23    40 Nordrhein-Westfalen
10309 ---- AHAUS                 52.05    6.57    46 Nordrhein-Westfalen
10315 EDDG MUENSTER/OSNABR.      52.08    7.42    48 Nordrhein-Westfalen
10320 ETUO GUETERSLOH            51.55    8.18    72 Nordrhein-Westfalen
10321 ETND DIEPHOLZ              52.35    8.21    39 Niedersachsen
10325 ---- BAD SALZUFLEN         52.06    8.45   135 Nordrhein-Westfalen
10334 ETNW WUNSTORF              52.27    9.26    57 Niedersachsen
10335 ETHB BUECKEBURG            52.17    9.05    70 Niedersachsen
10338 EDDV HANNOVER              52.28    9.41    56 Niedersachsen
10343 ETHC CELLE                 52.36   10.01    39 Niedersachsen
10348 ---- BRAUNSCHWG.           52.18   10.27    81 Niedersachsen
10356 ---- UMMENDORF             52.10   11.11   162 Sachsen-Anhalt
10359 ---- GARDELEGEN            52.31   11.24    47 Sachsen-Anhalt
10361 EDBM MAGDEBURG             52.07   11.35    79 Sachsen-Anhalt
10365 ---- GENTHIN               52.23   12.10    35 Sachsen-Anhalt
10368 ---- WIESENBURG            52.07   12.28   187 Brandenburg
10376 ---- BARUTH                52.04   13.30    55 Brandenburg
10379 ---- POTSDAM               52.23   13.04    99 Brandenburg
10381 ---- BERLIN-DAHLEM         52.28   13.18    58 Berlin
10382 EDDT BERLIN-TEGEL          52.34   13.19    37 Berlin
10384 EDDI BERLIN-TEMPELHOF      52.28   13.24    50 Berlin
10385 EDDB BERLIN-BRANDENBURG    52.23   13.31    47 Brandenburg
10389 ---- BERLIN-ALEX.          52.31   13.25    37 Berlin
10393 ---- LINDENBERG            52.13   14.07   112 Brandenburg
10396 ---- MANSCHNOW             52.33   14.33    12 Brandenburg
10400 EDDL DUESSELDORF           51.18    6.46    45 Nordrhein-Westfalen
10404 ETGY KALKAR                51.44    6.16    27 Nordrhein-Westfalen
10410 ---- ESSEN                 51.24    6.58   161 Nordrhein-Westfalen
10418 ---- LUEDENSCHEID          51.15    7.39   387 Nordrhein-Westfalen
10424 ---- WERL                  51.35    7.53    85 Nordrhein-Westfalen
10427 ---- K.ASTEN               51.11    8.29   839 Nordrhein-Westfalen
10430 ---- BAD LIPPSPRINGE       51.47    8.50   157 Nordrhein-Westfalen
10433 ---- LUEDGE                51.52    9.16   258 Nordrhein-Westfalen
10435 ---- WARBURG               51.30    9.07   236 Nordrhein-Westfalen
10438 ---- KASSEL                51.18    9.27   231 Hessen
10439 ETHF FRITZLAR              51.07    9.17   172 Hessen
10442 ---- ALFELD                51.58    9.48   148 Niedersachsen
10444 ---- GOETTINGEN            51.30    9.57   175 Niedersachsen
10449 ---- LEINEFELDE            51.24   10.19   356 Thüringen
10452 ---- BRAUNLAGE             51.44   10.36   607 Niedersachsen
10453 ---- BROCKEN               51.48   10.37  1142 Sachsen-Anhalt
10454 ---- WERNIGERODE           51.51   10.46   234 Sachsen-Anhalt
10458 ---- HARZGERODE            51.39   11.08   404 Sachsen-Anhalt
10460 ---- ARTERN                51.23   11.18   164 Thüringen
10466 ---- HALLE                 51.31   11.57    96 Sachsen-Anhalt
10469 EDDP LEIPZIG/SCHKEUDITZ    51.25   12.14   141 Sachsen
10471 ---- LEIPZIG               51.19   12.25   141 Sachsen
10474 ---- WITTENBERG            51.53   12.39   105 Sachsen-Anhalt
10476 ETSH HOLZDORF              51.46   13.11    79 Brandenburg
10480 ---- OSCHATZ               51.18   13.06   150 Sachsen
10488 EDDC DRESDEN               51.08   13.45   230 Sachsen
10490 ---- DOBERLUG-KIRCHHAIN    51.39   13.35    97 Brandenburg
10496 ETCO COTTBUS               51.47   14.19    69 Brandenburg
10499 EDBX GOERLITZ              51.10   14.57   237 Sachsen
10500 ETNG GEILENKIRCHEN         50.58    6.03    90 Nordrhein-Westfalen
10502 ETNN NOERVENICH            50.50    6.40   118 Nordrhein-Westfalen
10506 ---- NUERBURG-BARWEILER    50.22    6.52   485 Rheinland-Pfalz
10513 EDDK KOELN/BONN            50.52    7.10    91 Nordrhein-Westfalen
10516 ---- KO-FALKENST.KASERNE   50.22    7.35    84 Rheinland-Pfalz
10519 ---- BONN-ROLEBER          50.44    7.12   159 Nordrhein-Westfalen
10526 EDKS B.MARIENBG.           50.40    7.58   547 Rheinland-Pfalz
10532 ---- GIESSEN               50.36    8.39   203 Hessen
10534 ---- HOHERODSKOPF (VOGELS  50.31    9.13   743 Hessen
10540 ---- EISENACH              51.00   10.22   312 Thüringen
10542 ---- BAD HERSFELD          50.51    9.44   272 Hessen
10544 ---- WASSERKUPPE           50.30    9.57   921 Hessen
10548 ---- MEININGEN             50.34   10.23   450 Thüringen
10552 ---- SCHMUECKE             50.39   10.46   937 Thüringen
10554 EDDE ERFURT                50.59   10.58   315 Thüringen
10557 ---- NEUHAUS A.R.          50.30   11.08   845 Thüringen
10564 ---- SCHLEIZ               50.34   11.48   501 Thüringen
10565 ---- OSTERFELD             51.05   11.56   246 Sachsen-Anhalt
10567 ---- GERA                  50.53   12.08   311 Thüringen
10569 ---- PLAUEN                50.29   12.08   386 Sachsen
10574 ---- CARLSFELD             50.26   12.37   897 Sachsen
10577 ---- CHEMNITZ              50.48   12.52   418 Sachsen
10578 ---- FICHTELBERG           50.26   12.57  1213 Sachsen
10579 ---- MARIENBERG            50.39   13.09   639 Sachsen
10582 ---- ZINNWALD-G.           50.44   13.45   877 Sachsen
10591 ---- LICHTENHAIN           50.56   14.13   321 Sachsen
10609 ---- TRIER                 49.45    6.40   265 Rheinland-Pfalz
10613 ETSB BUECHEL               50.10    7.04   478 Rheinland-Pfalz
10615 ---- DEUSELBACH            49.46    7.03   481 Rheinland-Pfalz
10616 EDFH HAHN                  49.57    7.16   502 Rheinland-Pfalz
10618 EDRG IDAR-OBERSTEIN        49.42    7.20   376 Rheinland-Pfalz
10628 ---- GEISENHEIM            49.59    7.57   118 Hessen
10635 ---- KL.FELDBG./TS.        50.13    8.27   805 Hessen
10637 EDDF FRANKFURT/M           50.03    8.36   111 Hessen
10641 ---- OFFENBACH-WETTERPARK  50.05    8.47   119 Hessen
10646 ---- NEUHUETTEN/SPESSART   50.01    9.26   340 Bayern
10648 ---- MICHELSTADT-V.        49.43    9.06   453 Hessen
10655 ---- WUERZBURG             49.46    9.58   268 Bayern
10658 ---- KISSINGEN             50.12   10.05   262 Bayern
10671 ---- COBURG                50.17   10.59   322 Bayern
10675 ---- BAMBERG               49.53   10.55   243 Bayern
10685 ---- HOF                   50.19   11.53   567 Bayern
10686 ---- WUNSIEDEL-SCHOENBRUN  50.02   11.58   622 Bayern
10688 ---- WEIDEN                49.40   12.11   438 Bayern
10704 ---- BERUS                 49.16    6.41   363 Saarland
10706 ---- THOLEY                49.29    7.03   396 Saarland
10708 EDDR SAARBRUECKEN          49.13    7.07   322 Saarland
10724 ---- WEINBIET              49.23    8.07   553 Rheinland-Pfalz
10729 ---- MANNHEIM              49.31    8.33    96 Baden-Württemberg
10733 ---- WAIBSTADT             49.18    8.54   237 Baden-Württemberg
10736 ---- MUEHLACKER            48.58    8.52   244 Baden-Württemberg
10738 EDDS STUTTGART-ECHT.       48.41    9.13   396 Baden-Württemberg
10739 ---- STUTTGART-SCHN.       48.50    9.12   314 Baden-Württemberg
10742 ---- OEHRINGEN             49.12    9.31   276 Baden-Württemberg
10743 ETHN NIEDERSTETTEN         49.24    9.58   468 Baden-Württemberg
10756 ---- FEUCHTWANGEN          49.10   10.22   475 Bayern
10761 ---- WEISSENBURG-EMETZH.   49.01   10.56   439 Bayern
10763 EDDN NUERNBERG             49.30   11.03   318 Bayern
10765 ETHR ROTH                  49.13   11.06   388 Bayern
10771 ---- KUEMMERSBRUCK         49.26   11.54   419 Bayern
10776 ---- REGENSBURG            49.03   12.06   365 Bayern
10777 ---- GELBELSEE             48.57   11.26   539 Bayern
10782 ---- WALDMUENCHEN          49.24   12.41   499 Bayern
10788 ---- STRAUBING             48.50   12.34   350 Bayern
10791 ---- GR.ARBER              49.07   13.08  1446 Bayern
10796 ---- ZWIESEL               49.02   13.14   612 Bayern
10803 ---- FREIBURG              48.01    7.50   236 Baden-Württemberg
10805 EDTL LAHR                  48.22    7.50   156 Baden-Württemberg
10815 ---- FREUDENST.            48.27    8.25   797 Baden-Württemberg
10818 ---- KLIPPENECK            48.06    8.45   973 Baden-Württemberg
10827 ETGZ MESSSTETTEN           48.11    9.00   920 Baden-Württemberg
10836 ---- STOETTEN              48.40    9.52   734 Baden-Württemberg
10837 ETHL LAUPHEIM              48.13    9.55   538 Baden-Württemberg
10838 ---- ULM                   48.23    9.57   567 Baden-Württemberg
10850 ---- HARBURG               48.48   10.42   502 Bayern
10852 EDMA AUGSBURG              48.26   10.56   463 Bayern
10853 ETSN NEUBURG/DONAU         48.43   11.13   380 Bayern
10856 ETSL LECHFELD              48.11   10.51   555 Bayern
10857 ETSA LANDSBERG             48.04   10.54   623 Bayern
10860 ETSI INGOLSTADT            48.43   11.32   367 Bayern
10863 ---- WEIHENSTEPHAN         48.24   11.42   470 Bayern
10865 ---- MUENCHEN STADT        48.08   11.33   520 Bayern
10870 EDDM MUENCHEN-FL.          48.22   11.48   453 Bayern
10872 ---- GOTTFRIEDING          48.40   12.32   350 Bayern
10875 ---- MUEHLDORF             48.17   12.30   406 Bayern
10895 ---- FUERSTENZELL          48.33   13.21   476 Bayern
10908 ---- FELDBERG/S.           47.53    8.00  1486 Baden-Württemberg
10929 EDTZ KONSTANZ              47.41    9.11   443 Baden-Württemberg
10945 ---- LEUTKIRCH-HERLAZHFN.  47.48   10.02   672 Baden-Württemberg
10946 EDMK KEMPTEN               47.43   10.20   705 Bayern
10948 ---- OBERSTDORF            47.24   10.17   810 Bayern
10954 ETHA ALTENSTADT            47.50   10.52   739 Bayern
10961 ---- ZUGSPITZE             47.25   10.59  2960 Tirol
10962 ---- HOHENPEISS.BG         47.48   11.01   977 Bayern
10963 ---- GARMISCH              47.29   11.04   719 Bayern
10980 ---- WENDELSTEIN           47.42   12.01  1832 Bayern
10982 ---- CHIEMING              47.53   12.32   549 Bayern
01311 ENBR BERGEN                60.18    5.13    50 Vestland
01338 ---- VANGSNES              61.10    6.39    51 Vestland
01347 ENSG SOGNDAL               61.09    7.08   497 Vestland
01384 ENGM OSLO/GARDERMOEN       60.12   11.06   201 Viken
01385 ---- HAMAR-STAVSBERG       60.49   11.04   221 Innlandet
01403 ---- UTSIRA FYR            59.18    4.52    55 Rogaland
01415 ENZV STAVANGER             58.53    5.38     9 Rogaland
01452 ENCN KRISTIANSAND          58.12    8.05    17 Agder
01481 ---- MELSOM                59.14   10.21    26 Vestfold og Telemark
01488 ENFB OSLO/FORNEBU          59.54   10.37    16 Viken
01492 ---- OSLO-BLINDERN         59.57   10.43    94 Oslo
01493 ---- SARPSBORG             59.17   11.07    54 Viken
01494 ENRY RYGGE                 59.23   10.47    53 Viken
02418 ESSQ KARLSTAD              59.22   13.28    46 Värmlands län
02458 ESCM UPPSALA               59.53   17.36    21 Uppsala län
02464 ESKN STOCKHOLM             59.21   17.57    15 Stockholms län
02469 ---- TULLINGE              59.11   17.55    45 Stockholms län
02476 ---- FLODA                 59.03   16.24    32 Södermanlands län
02490 ---- SVANBERGA             59.50   18.38    15 Stockholms län
02493 ---- SOEDERARM             59.45   19.24    15 
02500 ---- NORDKOSTER            58.54   11.00    33 Västra Götalands län
02505 ---- MASESKAR              58.06   11.20    16 Västra Götalands län
02513 ---- GOETEBORG             57.42   12.00     5 Västra Götalands län
02520 ESIB SATENAS               58.26   12.43    54 Västra Götalands län
02550 ESGJ JONKOPING             57.46   14.05   226 Jönköpings län
02559 ---- GLADHAMMAR            57.43   16.27    35 Kalmar län
02562 ESCF LINKOPING             58.24   15.31    93 Östergötlands län
02574 ---- NORRKOPING            58.35   16.09    34 Östergötlands län
02590 ESSV VISBY                 57.40   18.21    51 Gotlands län
02603 ---- BROEN                 56.52   12.40    47 Hallands län
02607 ESDB ANGELHOLM             56.18   12.51    20 Skåne län
02611 ESHH HELSINGBORG           56.02   12.46    43 Skåne län
02616 ---- FALSTERBO             55.23   12.49     3 Skåne län
02628 ---- HANO                  56.01   14.51    60 
02635 ---- MALMO                 55.34   13.04    20 Skåne län
02636 ESMS MALMO/STURUP          55.33   13.22   106 Skåne län
02664 ESDF RONNEBY               56.16   15.17    58 Blekinge län
02670 ESMQ KALMAR                56.41   16.18     6 Kalmar län
02680 ---- HOBURG                56.55   18.09    40 Gotlands län
02944 EFTP TAMPERE               61.25   23.35   112 Pirkanmaa
02952 EFPO PORI                  61.28   21.48    13 Satakunta
02958 ---- LAPPEENRANTA          61.03   28.12   101 Südkarelien
02965 ---- LAHTI                 60.58   25.38    83 Päijät-Häme
02966 EFUT UTTI                  60.54   26.56   100 Kymenlaakso
02972 EFTU TURKU                 60.31   22.16    47 Varsinais-Suomi
02974 EFHK HELSINKI/VANTAA       60.19   24.58    51 Uusimaa
02982 ---- HANKO                 59.46   22.57     6 Uusimaa
03005 ---- LERWICK               60.08   -1.11    82 
03017 EGPA KIRKWALL              58.57   -2.54    26 
03026 EGPO STORNOWAY             58.13   -6.19     9 
03041 ---- AONACH MOR            56.49   -4.58  1130 Schottland
03044 ---- ALTNAHARRA            58.17   -4.27    81 Schottland
03063 ---- AVIEMORE              57.12   -3.50   228 Schottland
03065 ---- CAIRNGORM             57.07   -3.38  1245 Schottland
03066 EGQK KINLOSS               57.39   -3.34     6 Schottland
03068 EGQS LOSSIEMOUTH           57.43   -3.19    13 
03075 EGPC WICK                  58.27   -3.05    39 
03091 EGPD ABERDEEN              57.12   -2.13    65 
03100 EGPU TIREE                 56.30   -6.53    12 
03132 ---- WEST FREUGH           54.52   -4.56    11 England
03136 ---- PRESTWICK/RNAS        55.31   -4.35    26 Schottland
03158 ---- CHARTERHALL           55.43   -2.23   112 
03162 ---- ESKDALEMUIR           55.19   -3.12   242 Schottland
03171 EGQL LEUCHARS              56.23   -2.52    12 
03204 EGNS ISLE OF MAN/ROUAL.    54.05   -4.38    17 
03220 ---- CARLISLE              54.56   -2.58    28 
03257 EGXE LEEMING               54.18   -1.32    40 England
03261 ---- DISHFORTH AIRFIELD    54.08   -1.25    36 England
03265 EGXZ TOPCLIFFE             54.12   -1.23    25 England
03266 EGXU LINTON-ON-OUSE        54.03   -1.15    16 England
03275 ---- LOFTUS SAMOS          54.20   -0.31   158 
03292 ---- BRIDLINGTON           54.06   -0.10    15 
03302 EGOV VALLEY                53.15   -4.32    11 Wales
03313 ---- RHYL                  53.16   -3.31    77 England
03321 EGNR HAWARDEN              53.10   -2.59    10 England
03354 EGRW NOTTINGHAM/MET        53.00   -1.15   117 England
03377 ---- WADDINGTON            53.11    0.31    68 
03379 EGYD CRANWELL              53.02   -0.30    67 
03385 ---- DONNA NOOK            53.29    0.05     8 England
03405 ---- ABERDARON             52.47   -4.44    95 Wales
03414 EGOS SHAWBURY              52.48   -2.40    76 England
03462 EGXT WITTERING             52.37   -0.28    84 England
03482 EGYM MARHAM                52.39    0.34    23 England
03502 EGUC ABERPORTH             52.08   -4.34   133 Wales
03503 ---- TRAWSCOED             52.21   -3.57    63 England
03520 EGBS SHOBDON               52.15   -2.53    99 England
03560 EGVW BEDFORD               52.13   -0.29    85 England
03590 EGUW WATTISHAM             52.07    0.58    87 England
03604 ---- MILFORD HAVEN         51.43   -5.03    44 Wales
03628 EGTG BRISTOL/FILTON        51.31   -2.35    59 England
03647 ---- LITTLE RISSINGTON     51.52   -1.41   215 England
03649 EGVN BRIZE NORTON          51.45   -1.35    88 England
03672 EGWU NORTHOLT              51.33   -0.25    38 England
03707 EGDC CHIVENOR              51.05   -4.09     6 England
03740 EGDL LYNEHAM               51.30   -1.59   145 England
03743 ---- LARKHILL              51.12   -1.48   132 England
03768 ---- FARNBOROUGH           51.17    0.46    65 England
03772 EGLL LONDON                51.29   -0.27    24 
03781 ---- KENLEY                51.18   -0.05   170 England
03797 EGMH MANSTON               51.21    1.21    44 England
03803 ---- SCILLY                49.55   -6.18    31 
03808 ---- CAMBORNE              50.13   -5.20    87 
03809 EGDR CULDROSE              50.05   -5.15    78 
03827 EGDB PLYMOUTH              50.21   -4.07    50 England
03853 ---- YEOVILTON             51.00   -2.39    23 England
03862 EGHH BOURNEMOUTH/HURN      50.47   -1.50    11 
03866 ---- ST.CATHERINE'S POINT  50.35   -1.18    16 
03882 ---- HERSTMONCEUX          50.53    0.19    52 England
03894 EGJB GUERNSEY              49.26   -2.36   101 Normandie
03895 EGJJ JERSEY-AIRPORT        49.13   -2.12    84 
03903 EGAB ST. ANGELO            54.24   -7.39    47 Nordirland
03917 EGAA BELFAST               54.39   -6.13    81 Nordirland
03953 ---- VALENTIA              51.56  -10.15    25 Niedersachsen
03955 EICK CORK AIRPORT          51.51   -8.29   153 
03962 EINN SHANNON               52.42   -8.55    14 County Kilkenny
03969 EIDW DUBLIN                53.26   -6.15    68 
03971 ---- MULLINGAR             53.32   -7.22   100 County Meath
03976 ---- BELMULLET             54.14  -10.00     9 Schleswig-Holstein
03980 ---- MALIN HEAD            55.22   -7.20    20 
06030 EKYT ALBORG                57.06    9.52     3 Region Nordjylland
06041 ---- SKAGEN                57.46   10.39     3 
06052 ---- THYBORON              56.42    8.13     2 Region Midtjylland
06060 EKKA KARUP                 56.18    9.07    52 Region Midtjylland
06070 EKAH TIRSTRUP              56.18   10.37    25 Region Midtjylland
06080 EKEB ESBJERG               55.31    8.33    29 Region Syddanmark
06104 EKBI BILLUND               55.44    9.09    70 Region Syddanmark
06110 EKSP SKRYDSTRUP            55.14    9.16    43 Region Syddanmark
06119 ---- KEGNAES               54.51    9.59    17 
06120 EKOD ODENSE                55.28   10.20    17 Region Syddanmark
06169 ---- GNIBEN                56.00   11.17    14 
06170 EKRK KOEBENHAVN/ROSKILDE   55.35   12.08    44 Region Sjælland
06180 EKCH KOPENHAGEN            55.38   12.40     5 Region Hovedstaden
06190 EKRN ROENNE/BORNH.         55.04   14.45    16 Region Hovedstaden
06210 EHVB VALKENBURG            52.11    4.25     0 Südholland
06235 EHKD KOOY                  52.55    4.47     0 Nordholland
06240 EHAM AMSTERDAM             52.18    4.46    -4 Nordholland
06242 EHVL VLIELAND              53.15    4.55    11 
06260 EHDB DE BILT               52.06    5.11     2 Utrecht
06270 EHLW LEEUWARDEN            53.13    5.46     1 Friesland
06275 EHDL DEELEN                52.04    5.53    48 Gelderland
06279 EHHO HOOGEVEEN             52.44    6.31    12 Drenthe
06280 EHGG GRONINGEN             53.08    6.35     4 Drenthe
06290 EHTW TWENTHE               52.16    6.54    35 Provinz Overijssel
06310 ---- VLISSINGEN            51.26    3.36     8 
06330 ---- HOEK V.HOLL.          51.59    4.07    12 Südholland
06344 EHRD ROTTERDAM             51.57    4.27    -5 Südholland
06350 EHGR GILZE RIJEN           51.34    4.56    11 Nordbrabant
06370 EHEH EINDHOVEN             51.27    5.25    23 Nordbrabant
06375 EHVK VOLKEL                51.39    5.42    22 Nordbrabant
06380 EHBK MAASTRICHT            50.55    5.47   114 Limburg
06407 EBOS OOSTENDE              51.12    2.52     4 Flämische Region
06431 ---- GENT                  51.11    3.49    10 Flämische Region
06449 EBCI CHARLEROI             50.28    4.27   187 Wallonische Region
06450 EBAW ANTWERPEN             51.12    4.28    12 Flämische Region
06451 EBBR BRUESSEL              50.54    4.32    55 Flämische Region
06456 EBFS FLORENNES             50.14    4.40   279 Wallonische Region
06458 EBBE BEAUVECHAIN           50.45    4.46   105 Wallonische Region
06476 EBSH ST.HUBERT             50.02    5.24   563 Wallonische Region
06478 EBLG BIERSET               50.39    5.27   178 Wallonische Region
06479 EBBL KLEINE BROGEL         51.10    5.28    55 Flämische Region
06490 EBSP SPA/LA SAUVENIERE     50.29    5.55   470 Wallonische Region
06496 EBLB ELSENBORN             50.28    6.11   564 Wallonische Region
06590 ELLX LUXEMBURG             49.37    6.13   376 Distrikt Luxemburg
06601 ---- BASEL                 47.32    7.35   316 Basel-Landschaft
06604 LSGN NEUCHATEL             47.00    6.57   485 Neuenburg
06605 ---- CHASSERAL             47.08    7.03  1599 Bern
06606 ---- CRESSIER              47.03    7.04   431 Neuenburg
06609 ---- MOLESON               46.33    7.01  1972 Freiburg
06610 ---- PAYERNE               46.49    6.57   490 Waadt
06612 LSGC LA CHAUX DE FONDS     47.05    6.48  1018 Neuenburg
06616 ---- FAHY                  47.25    6.56   596 Bourgogne-Franche-Comté
06619 ---- LA FRETAZ             46.50    6.35  1202 Waadt
06620 LSPF SCHAFFHAUSEN          47.41    8.37   437 Schaffhausen
06621 ---- GUETTINGEN            47.36    9.17   440 Thurgau
06623 ---- SALEN-REUTENEN        47.39    9.01   718 Thurgau
06624 ---- HALLAU                47.42    8.28   419 Schaffhausen
06625 ---- FRIBOURG POSIEUX      46.46    7.07   646 Freiburg
06626 ---- GOESGEN (KKW)         47.22    7.58   380 Solothurn
06628 ---- PLAFFEIEN-OBERSCH.    46.45    7.16  1042 Freiburg
06629 ---- MUEHLEBERG / STOCKER  46.57    7.17   775 Bern
06631 ---- BERN-LIEBEFELD        46.56    7.25   565 Bern
06632 ---- GRENCHEN              47.11    7.25   430 Solothurn
06633 ---- BUCHS-SUHR            47.23    8.05   387 Aargau
06635 ---- KOPPIGEN              47.07    7.36   484 Bern
06636 ---- MUEHLEBERG (KKW)      46.58    7.17   480 Bern
06637 ---- MEIRINGEN             46.45    8.07   589 Bern
06638 ---- LANGNAU I.E.          46.56    7.48   745 Bern
06639 ---- NAPF                  47.00    7.56  1406 Bern
06641 ---- MOEHLIN               47.34    7.53   344 Aargau
06643 ---- WYNAU                 47.15    7.47   422 Bern
06645 ---- RUENENBERG            47.26    7.53   611 Basel-Landschaft
06646 ---- BEZNAU                47.33    8.14   325 Aargau
06648 ---- EGOLZWIL              47.11    8.00   521 Luzern
06650 ---- LUZERN                47.01    8.18   456 Luzern
06651 ---- SCHUEPFHEIM           46.57    8.01   742 Luzern
06655 ---- ENGELBERG             46.49    8.25  1036 Obwalden
06657 ---- GISWIL                46.57    8.11   475 Obwalden
06659 ---- PILATUS               46.59    8.15  2106 Nidwalden
06660 ---- ZUERICH (TOWN/VILLE)  47.23    8.34   556 Zürich
06664 ---- RECKENHOLZ            47.26    8.31   444 Zürich
06666 ---- LEIBSTADT (KKW)       47.36    8.11   341 Aargau
06669 ---- LAEGERN               47.29    8.24   868 Zürich
06670 LSZH ZUERICH               47.29    8.32   436 Zürich
06672 ---- ALTDORF               46.52    8.38   449 Uri
06673 ---- WAEDENSwl             47.13    8.41   463 Zürich
06674 ---- CHAM                  47.11    8.28   443 Zug
06675 ---- EINSIEDELN            47.08    8.45   910 Schwyz
06676 ---- OBERAEGERI            47.08    8.36   724 Zug
06679 ---- TAENIKON              47.28    8.54   536 Thurgau
06680 ---- SAENTIS               47.15    9.21  2502 Appenzell Innerrhoden
06681 ---- ST.GALLEN             47.26    9.24   779 Sankt Gallen
06682 ---- ELM                   46.55    9.11   958 Glarus
06683 ---- SCHMERIKON            47.13    8.56   408 Sankt Gallen
06685 ---- GLARUS                47.02    9.04   515 Glarus
06687 ---- QUINTEN               47.08    9.13   419 Sankt Gallen
06688 ---- CRAP MASEGN           46.51    9.11  2480 Graubünden
06689 ---- HOERNLI               47.22    8.57  1144 Zürich
06693 ---- EBNAT-KAPPEL          47.16    9.07   623 Sankt Gallen
06700 LSGG GENF                  46.15    6.08   420 Genf
06702 ---- LA DOLE               46.25    6.06  1670 Waadt
06704 ---- BIERE                 46.31    6.21   684 Waadt
06705 ---- CHANGINS              46.24    6.14   430 Waadt
06711 ---- PULLY                 46.31    6.40   461 Waadt
06712 ---- AIGLE                 46.20    6.55   381 Wallis
06717 ---- GRAND-ST-BERNARD      45.52    7.10  2472 Wallis
06720 LSGS SION                  46.13    7.20   482 Wallis
06722 ---- EVOLENE-VILLAZ        46.07    7.31  1825 Wallis
06724 ---- MONTANA               46.19    7.29  1508 Wallis
06727 ---- VISP                  46.18    7.51   639 Wallis
06730 ---- JUNGFRAUJOCH          46.29    8.02  3580 Wallis
06734 LSMI INTERLAKEN            46.40    7.52   580 Bern
06735 ---- ADELBODEN             46.30    7.34  1320 Bern
06744 ---- GRIMSEL-HOSPIZ        46.34    8.20  1980 Bern
06745 ---- ULRICHEN              46.30    8.18  1346 Wallis
06748 LSEZ ZERMATT               46.02    7.45  1638 Wallis
06750 ---- GUETSCH               46.39    8.37  2287 Uri
06751 ---- ROBIEI                46.27    8.31  1898 Tessin
06753 ---- PIOTTA                46.31    8.41  1007 Tessin
06756 ---- COMPROVASCO           46.28    8.56   575 Tessin
06759 ---- CIMETTA               46.12    8.48  1672 Tessin
06760 ---- LOCARNO-MONTI         46.10    8.47   367 Tessin
06762 LSZL LOCARNO               46.10    8.53   197 Tessin
06770 ---- LUGANO                46.00    8.58   273 Tessin
06771 ---- STABIO                45.51    8.56   353 Tessin
06778 ---- BUFFALORA             46.39   10.16  1968 Graubünden
06780 ---- WEISSFLUHJOCH         46.50    9.48  2690 Graubünden
06782 ---- DISENTIS              46.42    8.51  1190 Graubünden
06783 ---- SAN BERNARDINO        46.28    9.11  1639 Graubünden
06784 ---- DAVOS                 46.49    9.51  1590 Graubünden
06786 ---- CHUR                  46.52    9.32   556 Graubünden
06791 ---- CORVATSCH             46.25    9.49  3315 Graubünden
06792 LSXM SAMEDAN               46.32    9.53  1709 Graubünden
06793 ---- VALBELLA              46.45    9.33  1569 Graubünden
06794 ---- ROBBIA                46.21   10.04  1078 Graubünden
06795 ---- PIZ MARTEGNAS         46.35    9.32  2670 Graubünden
06796 ---- STA. MARIA VAL MUEST  46.36   10.26  1383 Graubünden
06798 ---- SCOULS                46.48   10.16  1298 Graubünden
06799 ---- NALUNS / SCHLIVERA    46.49   10.16  2400 Graubünden
06990 ---- VADUZ FL.             47.08    9.31   460 Vaduz
07002 ---- BOULOGNE              50.44    1.36    70 Hauts-de-France
07005 LFOI ABBEVILLE             50.08    1.50    70 Hauts-de-France
07015 LFQQ LILLE                 50.34    3.06    48 Hauts-de-France
07017 LFQI CAMBRAI               50.13    3.09    77 Hauts-de-France
07020 ---- LA HAGUE              49.43   -1.56     3 
07024 LFRC CHERBOURG             49.39   -1.28   139 
07027 LFRK CAEN                  49.11   -0.27    67 Normandie
07028 LFOH LA HEVE               49.31    0.04   100 Normandie
07037 LFOP ROUEN                 49.23    1.11   157 Normandie
07038 LFOE EVREUX                49.01    1.13   132 Normandie
07040 ---- DIEPPE                49.56    1.06    33 Normandie
07055 LFOB BEAUVAIS              49.28    2.07   106 Hauts-de-France
07061 LFOW SAINT-QUENTIN         49.49    3.12    98 Hauts-de-France
07070 LFSR REIMS                 49.18    4.02    91 Grand Est
07075 LFQV CHARLEVILLE           49.47    4.38   149 Grand Est
07090 LFSF METZ                  49.05    6.08   190 Grand Est
07100 LFEC OUESSANT              48.28   -5.08    35 
07110 LFRB BREST                 48.27   -4.25    99 Bretagne
07120 LFRT ST.BRIEUC             48.32   -2.51   136 Normandie
07125 LFRD DINARD APT            48.35   -2.04    58 Bretagne
07130 LFRN RENNES                48.04   -1.44    37 Pays de la Loire
07133 ---- POINTE DU ROC         48.50   -1.37    37 Normandie
07139 LFOF ALENCON               48.26    0.06   144 Normandie
07143 LFOR CHARTRES              48.28    1.31   155 Centre
07149 LFPO PARIS                 48.44    2.24    89 Île-de-France
07157 LFPG PARIS CH.D.GAULLE     49.01    2.32   108 Île-de-France
07168 LFQB TROYES                48.20    4.01   112 Grand Est
07169 LFSI ST. DIZIER            48.38    4.54   139 Grand Est
07180 LFSN NANCY                 48.41    6.13   229 Grand Est
07190 LFST STRASSBURG            48.33    7.38   153 Grand Est
07200 ---- PENMARCH              47.48   -4.22     6 Bretagne
07201 LFRQ QUIMPER               47.58   -4.10    92 Bretagne
07205 LFRH LANN BIHOUE           47.46   -3.27    42 Bretagne
07222 LFRS NANTES                47.10   -1.36    27 Pays de la Loire
07235 LFRM LE MANS               47.57    0.12    52 Pays de la Loire
07240 LFOT TOURS                 47.27    0.43   108 Centre
07249 LFOJ ORLEANS               47.59    1.47   125 Centre
07255 LFLD BOURGES               47.04    2.22   161 Centre
07260 LFQG NEVERS                47.00    3.06   175 Bourgogne-Franche-Comté
07265 LFLA AUXERRE               47.48    3.33   207 Bourgogne-Franche-Comté
07280 LFSD DIJON                 47.16    5.05   219 Bourgogne-Franche-Comté
07288 LFSA BESANCON              47.15    5.59   307 Bourgogne-Franche-Comté
07299 LFSB BASEL-MLH.            47.36    7.31   270 Grand Est
07306 LFRI LA ROCHE-SUR-YON      46.42   -1.23    90 Nouvelle-Aquitaine
07315 ---- LA ROCHELLE           46.09   -1.09     4 Nouvelle-Aquitaine
07335 LFBI POITIERS              46.35    0.18   120 Nouvelle-Aquitaine
07354 LFLX CHATEAUROUX           46.52    1.43   155 Centre
07379 LFLN SAINT-YAN.            46.25    4.01   242 Bourgogne-Franche-Comté
07385 LFLM MACON                 46.18    4.48   216 Bourgogne-Franche-Comté
07434 LFBL LIMOGES               45.52    1.11   402 Nouvelle-Aquitaine
07460 LFLC CLERMONT              45.47    3.10   329 Auvergne-Rhône-Alpes
07475 LFMH ST. ETIENNE           45.32    4.18   402 Auvergne-Rhône-Alpes
07480 LFLY LYON/BRON             45.43    4.57   200 Auvergne-Rhône-Alpes
07481 LFLL LYON/SATOLAS          45.44    5.05   248 Auvergne-Rhône-Alpes
07486 LFLS GRENOBLE              45.22    5.20   384 Auvergne-Rhône-Alpes
07491 LFLB CHAMBERY - AIX        45.39    5.53   235 Auvergne-Rhône-Alpes
07497 ---- BOURG-ST-M            45.37    6.46   865 Auvergne-Rhône-Alpes
07510 LFBD BORDEAUX              44.50   -0.42    49 Nouvelle-Aquitaine
07558 LFCM MILLAU                44.07    3.01   715 Okzitanien
07577 LFLQ MONTELIMAR            44.35    4.44    73 Auvergne-Rhône-Alpes
07579 LFMO ORANGE                44.08    4.50    53 Provence-Alpes-Côte d'Azur
07588 LFMX ST.AUBAN              44.04    6.00   457 Provence-Alpes-Côte d'Azur
07600 ---- SOCOA                 43.24   -1.41    24 Nouvelle-Aquitaine
07602 LFBZ BIARRITZ              43.28   -1.32    69 Nouvelle-Aquitaine
07610 ---- PAU                   43.23   -0.25   185 Okzitanien
07621 LFBT TARBES/OSSUN          43.11    0.00   364 Okzitanien
07622 LFDH AUCH                  43.41    0.36   121 Okzitanien
07630 LFBO TOULOUSE              43.38    1.22   152 Okzitanien
07635 LFMK CARCASSONNE           43.13    2.19   126 Okzitanien
07638 ---- BEZIER-VIAS           43.18    3.24    16 Okzitanien
07643 LFMT MONTPELLIER           43.35    3.58     3 Okzitanien
07645 LFME NIMES/COURBESSAC      43.52    4.24    59 Okzitanien
07648 LFMY SALON                 43.36    5.06    59 Provence-Alpes-Côte d'Azur
07650 LFML MARSEILLE             43.27    5.13     5 
07667 LFTH HYERES/ALMANARRE      43.06    6.09     3 Provence-Alpes-Côte d'Azur
07670 ---- PORQUEROLLES          43.00    6.14   143 Provence-Alpes-Côte d'Azur
07675 LFMC LE LUC                43.23    6.23    80 Provence-Alpes-Côte d'Azur
07684 LFMD CANNES                43.33    6.57     3 Provence-Alpes-Côte d'Azur
07690 LFMN NIZZA                 43.39    7.12     4 
07747 LFMP PERPIGNAN             42.44    2.52    43 Okzitanien
07754 LFKC CALVI                 42.32    8.48    46 Korsika
07761 LFKJ AJACCIO               41.55    8.48     6 Korsika
07770 ---- PERTUSATO / CORSICA   41.22    9.11   105 Korsika
07780 LFKF FIGARI                41.30    9.06    26 Korsika
07785 ---- CAP CORSE             43.00    9.22   111 Korsika
07790 LFKB BASTIA                42.33    9.29    10 Korsika
08001 LECO LA CORUNA             43.22   -8.25    58 Galicien
08014 ---- GIJON                 43.32   -5.38     3 
08015 LEOV OVIEDO                43.21   -5.52   335 Kantabrien
08021 LEXJ SANTANDER/PARAYAS     43.26   -3.49     6 
08023 ---- SANTANDER             43.29   -3.48    52 
08025 LEBB BILBAO                43.18   -2.56    42 Nouvelle-Aquitaine
08027 ---- SAN SEBASTIAN/IGUEL.  43.18   -2.03   258 Autonome Gemeinschaft Baskenland
08029 LESO SAN SEBASTIAN/FUENT.  43.21   -1.48     5 Nouvelle-Aquitaine
08042 LEST SANTIAGO              42.54   -8.26   370 Galicien
08045 LEVX VIGO/PEINADOR         42.13   -8.38   264 Galicien
08055 LELN LEON                  42.35   -5.39   926 Kastilien und León
08075 ---- BURGOS-VILLAFRIA      42.22   -3.38   894 La Rioja
08080 ---- VITORIA OBSERVATORI   42.52   -2.44   513 Navarra
08140 LEVD VALLADOLID            41.43   -4.51   849 Kastilien und León
08141 ---- VALLADOLID            41.39   -4.46   735 Kastilien und León
08160 LEZG ZARAGOZA              41.40   -1.01   263 Aragonien
08171 ---- LERIDA                41.37    0.38   203 Katalonien
08175 LERS REUS                  41.09    1.10    71 Katalonien
08181 LEBL BARCELONA             41.17    2.04     4 Katalonien
08184 LEGE GERONA/COST.BRAVA     41.54    2.46   143 Katalonien
08202 LESA SALAMANCA/MATACAN     40.57   -5.30   793 Kastilien und León
08221 LEMD MADRID/BARAJAS        40.27   -3.33   609 Kastilien-La Mancha
08272 ---- TOLEDO BUENAVISTA     39.53   -4.03   451 Kastilien-La Mancha
08280 LEAB ALBACETE/LOS LLANOS   38.57   -1.51   702 Land Valencia
08284 LEVC VALENCIA              39.30   -0.28    69 
08286 LECN CASTELLON DE LA PLAN  39.57    0.04    36 
08306 LEPA PALMA                 39.33    2.44     4 Balearische Inseln
08314 LEMH MENORCA               39.52    4.14    87 Balearische Inseln
08330 LEBZ BADAJOZ/TALAVERA      38.53   -6.49   185 Extremadura
08360 LEAL ALICANTE              38.17   -0.33    43 
08373 LEIB IBIZA                 38.52    1.23    17 Balearische Inseln
08383 ---- HUELVA                37.17   -6.55    19 Andalusien
08391 ---- SEVILLA/SAN PABLO     37.25   -5.53    34 Andalusien
08397 LEMO MORON DE LA FRONTERA  37.09   -5.37    87 Andalusien
08410 LEBA CORDOBA               37.51   -4.51    90 Andalusien
08419 LEGR GRANADA/AEROPUERTO    37.11   -3.47   567 Andalusien
08430 ---- MURCIA                38.00   -1.10    61 Land Valencia
08433 LELC MURCIA/SAN JAVIER     37.47   -0.48     5 
08451 LEJR JEREZ DE LA FRONTERA  36.45   -6.04    27 Andalusien
08482 LEMG MALAGA                36.40   -4.29    16 
08487 LEAM ALMERIA               36.51   -2.23    15 
08495 LXGB GIBRALTAR             36.09   -5.21     5 
08532 LPST SINTRA/GRANJA         38.50   -9.20   134 Distrikt Santarém
08540 LPMR MONTE REAL            39.50   -8.53    52 Distrikt Castelo Branco
08541 ---- SINES (MONTES CHAOS)  37.57   -8.50    98 Andalusien
08545 LPPR PORTO                 41.14   -8.41    69 Distrikt Bragança
08546 ---- PORTO/SERRA DO PILAR  41.08   -8.36    93 Distrikt Viseu
08548 LPCO COIMBRA/CERVACHE      40.09   -8.28   179 Distrikt Castelo Branco
08551 ---- VIANA DO CASTELO      41.38   -8.48    48 Distrikt Bragança
08554 LPFR FARO                  37.01   -7.58     7 Andalusien
08562 ---- BEJA                  38.01   -7.52   246 Extremadura
08567 LPVR VILA REAL             41.16   -7.43   561 Kastilien und León
08571 ---- PORTALEGRE            39.17   -7.25   467 Extremadura
08579 ---- LISBOA/GAGO COUTINHO  38.46   -9.08   104 Distrikt Santarém
11001 ---- WOLFSEGG              48.06   13.40   660 Oberösterreich
11008 ---- ROHRBACH              48.34   14.00   602 Oberösterreich
11010 LOWL LINZ FL.              48.14   14.11   298 Oberösterreich
11012 ---- KREMSMUENSTER         48.03   14.08   382 Oberösterreich
11015 ---- FREISTADT             48.30   14.30   549 Oberösterreich
11018 ---- AMSTETTEN             48.06   14.54   266 Niederösterreich
11019 ---- ALLENSTEIG            48.41   15.22   599 Niederösterreich
11020 ---- ZWETTL                48.37   15.12   505 Niederösterreich
11021 ---- LITSCHAU              48.57   15.02   559 Niederösterreich
11022 ---- RETZ                  48.46   15.57   320 Niederösterreich
11030 LOXT TULLN                 48.19   16.07   175 Niederösterreich
11032 ---- POYSDORF              48.40   16.38   202 Niederösterreich
11034 ---- WIEN/CITY             48.12   16.22   171 Wien
11035 ---- WIEN/HOHE WARTE       48.15   16.22   195 Wien
11036 LOWW WIEN FL.              48.07   16.34   183 Niederösterreich
11040 ---- WIEN/UNTERLAA         48.07   16.25   201 Niederösterreich
11053 ---- RIED IM INNKREIS      48.13   13.29   431 Oberösterreich
11055 ---- SCHAERDING            48.28   13.26   314 Bayern
11060 ---- LINZ                  48.18   14.17   262 Oberösterreich
11070 ---- KREMS                 48.25   15.37   203 Niederösterreich
11075 ---- LANGENLOIS            48.28   15.42   204 Niederösterreich
11078 ---- LILIENFELD/TARSCHBER  48.02   15.35   681 Niederösterreich
11082 ---- GUMPOLDSKIRCHEN       48.02   16.17   219 Niederösterreich
11101 ---- BREGENZ               47.30    9.45   424 Vorarlberg
11105 ---- FELDKIRCH             47.16    9.37   438 Vorarlberg
11109 ---- ST.ANTON AM ARLBERG   47.08   10.16  1289 Tirol
11110 ---- GALZIG                47.08   10.14  2080 Tirol
11112 ---- LANDECK               47.09   10.34   785 Tirol
11120 LOWI INNSBRUCK FL.         47.16   11.21   581 Tirol
11128 ---- BRENNER               47.07   11.26  1450 Tirol
11130 LOIK KUFSTEIN              47.35   12.10   493 Tirol
11140 ---- LOFER                 47.35   12.42   629 Salzburg
11141 ---- BISCHOFSHOFEN         47.24   13.13   543 Salzburg
11144 ---- ZELL A.SEE            47.20   12.48   766 Salzburg
11146 ---- SONNBLICK             47.03   12.57  3105 Kärnten
11148 ---- ST.MICHAEL/LUNGAU     47.06   13.39  1094 Salzburg
11149 ---- OBERTAUERN            47.15   13.34  1743 Salzburg
11150 LOWS SALZBURG FL.          47.48   13.00   430 Salzburg
11154 ---- GMUNDEN               47.55   13.48   424 Oberösterreich
11156 ---- BAD ISCHL             47.43   13.38   469 Oberösterreich
11157 LOXA AIGEN/ENNS            47.32   14.08   638 Steiermark
11165 LOXZ ZELTWEG               47.12   14.45   677 Steiermark
11170 ---- LUNZ                  47.51   15.04   614 Niederösterreich
11174 ---- ST.MICHAEL            47.20   15.00   580 Steiermark
11182 LOXN WIENER NEUSTADT       47.50   16.13   285 Niederösterreich
11190 ---- EISENSTADT            47.51   16.32   184 Burgenland
11192 ---- KLEINZICKEN           47.12   16.20   267 Burgenland
11194 ---- NEUSIEDL AM SEE       47.57   16.51   135 Burgenland
11201 ---- SILLIAN               46.45   12.25  1081 Tirol
11204 LOKL LIENZ                 46.50   12.48   659 Tirol
11212 ---- VILL.ALPE             46.36   13.40  2140 Kärnten
11213 ---- VILLACH               46.37   13.52   495 Kärnten
11231 LOWK KLAGENFURT FL.        46.39   14.20   448 Kärnten
11240 LOWG GRAZ FL.              47.00   15.26   340 Steiermark
11248 ---- BAD RADKERSBURG       46.41   15.59   208 Gornja Radgona
11270 ---- DELLACH IM DRAUTAL    46.44   13.05   625 Kärnten
11292 ---- LASSNITZHOEHE         47.05   15.35   524 Steiermark
11308 ---- WARTH                 47.15   10.11  1475 Vorarlberg
11312 ---- GALTUER               46.58   10.11  1584 Tirol
11350 ---- SALZBURG              47.47   13.03   423 Salzburg
11354 ---- BAD GOISERN           47.39   13.37   502 Oberösterreich
11355 ---- WINDISCHGARSTEN       47.44   14.20   596 Oberösterreich
11357 ---- ST. WOLFGANG          47.44   13.27   537 Salzburg
11380 ---- REICHENAU/RAX         47.42   15.50   486 Niederösterreich
11406 ---- EGER                  50.04   12.24   483 Karlovarský kraj
11414 LKKV KARLSBAD              50.12   12.55   606 Karlovarský kraj
11423 ---- PRIMDA                49.40   12.41   742 Plzeňský kraj
11438 ---- TUSIMICE              50.23   13.20   322 Ústecký kraj
11450 ---- PLZEN (AUT. STATION)  49.45   13.21   331 Plzeňský kraj
11457 ---- CHURANOV              49.04   13.37  1122 Jihočeský kraj
11487 ---- KOCELOVICE            49.28   13.50   519 Jihočeský kraj
11502 ---- AUSSIG                50.41   14.02   375 Ústecký kraj
11509 ---- DOKSANY               50.28   14.10   158 Ústecký kraj
11518 LKPR PRAG FL.              50.06   14.15   380 Středočeský kraj
11520 ---- PRAG                  50.01   14.27   304 Prag
11538 ---- TEMELIN               49.12   14.21   500 Jihočeský kraj
11567 ---- PRAHA (KBELI AIRP.)   50.07   14.33   285 Prag
11603 LKLB LIBEREC               50.46   15.01   405 Liberecký kraj
11624 ---- CASLAV                49.57   15.23   242 Středočeský kraj
11628 ---- KRAMOLIN-KOSETICE     49.35   15.05   534 Kraj Vysočina
11643 ---- PEC POD SNEZKOU       50.40   15.45   816 Královéhradecký kraj
11652 LKPD PARDUBICE             50.01   15.44   225 Pardubický kraj
11659 ---- PRIBYSLAW             49.35   15.46   533 Kraj Vysočina
11679 ---- USTI NAD ORLICI       49.59   16.26   402 Pardubický kraj
11683 ---- SVRATOUCH             49.44   16.02   733 Pardubický kraj
11692 ---- NAMEST NAD OSLAVOU    49.10   16.07   473 Kraj Vysočina
11693 ---- DUKOVANY              49.06   16.08   400 Kraj Vysočina
11698 ---- KUCHAROVICE           48.53   16.05   334 Jihomoravský kraj
11710 ---- LUKA                  49.39   16.57   513 Olomoucký kraj
11723 LKTB BRUENN                49.09   16.42   238 Jihomoravský kraj
11774 ---- HOLESOV               49.19   17.34   224 Zlínský kraj
11782 LKMT OSTRAVA/MOSNOV        49.41   18.07   257 Moravskoslezský kraj
11787 ---- LYSA HORA/RIESENGEB.  49.33   18.27  1324 Moravskoslezský kraj
11816 LZIB BRATISLAVA            48.10   17.12   132 Bratislavský kraj
11819 ---- JASLOVSKE BOHUNICE    48.29   17.40   176 Trnavský kraj
11826 LZPP PIESTANY              48.37   17.50   164 Trnavský kraj
11855 ---- NITRA                 48.17   18.08   135 Nitriansky kraj
11856 ---- MOCHOVCE              48.17   18.27   261 Nitriansky kraj
11858 ---- HURBANOVO             47.52   18.12   115 Nitriansky kraj
11867 ---- PRIEVIDZA             48.46   18.36   260 Trenčiansky kraj
11880 ---- DUDINCE               48.10   18.52   139 Banskobystrický kraj
11903 LZSL SLIAC                 48.39   19.09   314 Banskobystrický kraj
11927 ---- LUCENEC               48.20   19.44   214 Banskobystrický kraj
11933 ---- STREBSKE PLESO        49.07   20.05  1354 Prešovský kraj
11934 LZTT POPRAD/T.             49.04   20.15   694 Prešovský kraj
11938 ---- TELGART               48.51   20.11   901 Banskobystrický kraj
11968 LZKZ KOSICE                48.40   21.13   230 Košický kraj
11976 ---- STROPKOV,TISINEC      49.13   21.39   216 Prešovský kraj
11978 ---- MILHOSTOV             48.40   21.44   105 Košický kraj
11993 LZKC KAMENICA NAD C.       48.56   22.00   176 Prešovský kraj
12105 ---- KOSZALIN              54.12   16.09    33 Woiwodschaft Westpommern
12120 ---- LEBA                  54.45   17.32     2 Woiwodschaft Pommern
12135 ---- HEL                   54.36   18.49     1 Woiwodschaft Pommern
12160 EPEL ELBLAG                54.10   19.26    40 Woiwodschaft Ermland-Masuren
12185 ---- KETRZYN               54.04   21.22   107 Woiwodschaft Ermland-Masuren
12195 EPSU SUWALKI               54.08   22.57   184 Woiwodschaft Podlachien
12200 ---- SWINEMUENDE           53.55   14.15     5 Woiwodschaft Westpommern
12205 ---- STETTIN               53.24   14.37     1 Woiwodschaft Westpommern
12210 ---- RESKO                 53.46   15.25    51 Woiwodschaft Westpommern
12230 EPPI PILA                  53.08   16.45    72 Großpolen
12235 ---- CHOJNICE              53.42   17.33   172 Woiwodschaft Pommern
12250 EPTO TORUN                 53.02   18.35    69 Woiwodschaft Kujawien-Pommern
12270 ---- MLAWA                 53.06   20.22   147 Woiwodschaft Masowien
12280 EPMJ MIKOLAJKI             53.47   21.35   127 Woiwodschaft Ermland-Masuren
12295 EPBK BIALYSTOK             53.06   23.10   148 Woiwodschaft Podlachien
12300 ---- GORZOW WLKP           52.44   15.17    71 Drossen
12310 ---- SLUBICE               52.21   14.36    21 Drossen
12330 EPPO POSEN                 52.25   16.50    86 Großpolen
12345 ---- KOLO                  52.12   18.40   115 Großpolen
12360 EPPL PLOCK                 52.35   19.44   106 Woiwodschaft Masowien
12375 EPWA WARSCHAU              52.10   20.58   106 Woiwodschaft Masowien
12385 ---- SIEDLCE               52.15   22.15   152 Woiwodschaft Masowien
12400 EPZG ZIELONA GORA          51.56   15.32   192 Drossen
12415 ---- LEGNICA BARTOSZOW     51.12   16.12   122 Woiwodschaft Niederschlesien
12418 EPLS LESZNO                51.50   16.32    91 Großpolen
12424 EPWR WROCLAW II            51.06   16.53   120 Woiwodschaft Niederschlesien
12435 ---- KALISZ                51.47   18.05   137 Großpolen
12455 ---- WIELUN                51.13   18.33   199 Woiwodschaft Łódź
12465 EPLL LODZ                  51.44   19.24   187 Woiwodschaft Łódź
12469 ---- SULEJOW               51.21   19.52   188 Woiwodschaft Łódź
12488 ---- KOZIENICE             51.34   21.33   123 Woiwodschaft Masowien
12495 EPLR LUBLIN RADAWIEC       51.13   22.24   238 Woiwodschaft Lublin
12500 EPJG JELENIA GORA          50.54   15.48   342 Woiwodschaft Niederschlesien
12510 ---- SNIEZKA               50.44   15.44  1604 Královéhradecký kraj
12520 ---- KLODZKO               50.26   16.37   356 Woiwodschaft Niederschlesien
12530 ---- OPOLE                 50.40   17.58   163 Oppeln
12540 ---- RACIBORZ              50.04   18.11   206 Woiwodschaft Schlesien
12550 EPCH CZESTOCHOWA           50.49   19.06   293 Woiwodschaft Schlesien
12560 EPKM KATOWICE              50.14   19.02   284 Woiwodschaft Schlesien
12566 EPKK KRAKOW                50.05   19.48   237 Woiwodschaft Kleinpolen
12570 EPKA KIELCE                50.49   20.42   260 Heiligkreuz
12580 EPRZ RZESZOW-JASIONKA      50.06   22.03   200 Woiwodschaft Karpatenvorland
12585 ---- SANDOMIERZ            50.42   21.43   217 Heiligkreuz
12600 EPBA BIELSKO-BIALA         49.48   19.00   398 Woiwodschaft Schlesien
12625 ---- ZAKOPANE              49.18   19.58   857 Woiwodschaft Kleinpolen
12660 EPNL NOWY SACZ             49.37   20.42   292 Woiwodschaft Kleinpolen
12690 ---- LESKO                 49.28   22.21   420 Woiwodschaft Karpatenvorland
12766 ---- JOSVAFO               48.29   20.32   305 Borsod-Abaúj-Zemplén
12772 LHMC MISKOLC               48.05   20.46   232 Borsod-Abaúj-Zemplén
12805 ---- SOPRON                47.41   16.36   233 Győr-Moson-Sopron
12815 ---- MOSONMAGYAROVAR       47.53   17.17   121 Győr-Moson-Sopron
12822 ---- GYOR                  47.43   17.41   116 Győr-Moson-Sopron
12825 LHPA PAPA                  47.12   17.30   145 Wesprim
12830 ---- VESZPREM              47.04   17.50   280 Wesprim
12843 ---- BUDAPEST/LORINC       47.26   19.11   138 Budapest
12846 ---- AGARD                 47.11   18.37   105 Weißenburg
12882 LHDC DEBRECEN              47.29   21.36   110 Hajdú-Bihar
12910 ---- SZENTGOTTHARD         46.55   16.19   312 Eisenburg
12922 ---- SARMELLEK             46.41   17.10   124 Komitat Zala
12925 ---- NAGYKANIZSA           46.27   16.58   139 Komitat Zala
12935 ---- SIOFOK                46.55   18.03   108 Komitat Somogy
12942 LHPP PECS/POGANY           46.00   18.14   201 Komitat Baranya
12970 LHKE KECSKEMET             46.55   19.45   113 Bács-Kiskun
12982 LHUD SZEGED                46.15   20.06    82 Csongrád
12992 LHBC BEKESCSABA            46.41   21.10    88 Békés
13168 ---- NOVI SAD              45.20   19.51    86 Wojwodina
13262 ---- LOZNICA               44.33   19.14   121 
13269 ---- VALJEVO               44.19   19.55   176 
13272 ---- BEOGRAD/SURCIN        44.49   20.17    96 
13274 LYBE BELGRAD               44.48   20.28   132 
13278 ---- KRAGUJEVAC            44.02   20.56   185 
13295 ---- NEGOTIN               44.14   22.33    44 
13367 ---- ZLATIBOR              43.44   19.43  1029 
13376 LYKT KRALJEVO              43.42   20.42   217 
13378 ---- KOPAONIK              43.17   20.48  1713 
13388 LYNI NIS                   43.20   21.54   202 
13389 ---- LESKOVAC              42.59   21.57   232 
13455 ---- HERCEGNOVI            42.27   18.33    10 Herceg Novi Municipality
13462 LYTI PODGORICA/GOLUBOBCI   42.22   19.15    33 Großgemeinde Podgorica
13489 ---- VRANJE                42.33   21.55   433 
13586 LWSK SKOPJE                41.58   21.39   238 Municipality of Ilinden
13600 ---- SHKODRA               42.06   19.32    43 Qark Shkodra
13610 ---- KUKES                 42.02   20.25   354 Qark Kukës
13611 ---- DURRES                41.18   19.27    15 
13615 LATI TIRANA                41.20   19.47    89 Qark Tirana
14014 LJLJ LJUBLJANA/BRNIK       46.13   14.29   364 Kranj
14026 LJMB MARIBOR/SLIVNICA      46.29   15.41   264 Administrative unit Maribor
14236 ---- ZAGREB/GRIC           45.49   15.58   157 Zagreb
14241 LDZA ZAGREB/PLESO          45.44   16.04   106 Gespanschaft Zagreb
14256 ---- BILOGORA              45.53   17.12   262 Gespanschaft Virovitica-Podravina
14280 ---- OSIJEK-CEPIN          45.30   18.34    89 Gespanschaft Osijek-Baranja
14307 LDPL PULA                  44.54   13.55    63 Gespanschaft Istrien
14317 LDRI RIJEKA                45.13   14.35    85 Primorje-Gorski
14330 ---- GOSPIC                44.33   15.22   564 Gespanschaft Lika-Senj
14431 ---- ZADAR                 44.06   15.21    82 Zadar
14442 ---- KNIN                  44.02   16.12   255 Gespanschaft Šibenik-Knin
14444 LDSP SPLIT/RESNIK          43.32   16.18    21 Gespanschaft Split-Dalmatien
14445 ---- SPLIT/MARJAN          43.30   16.26   122 
14474 LDDU DUBROVNIK             42.34   18.16   164 Gespanschaft Dubrovnik-Neretva
14528 LQBI BIHAC                 44.49   15.53   250 Föderation Bosnien und Herzegowina
14537 ---- SANSKI MOST           44.46   16.42   154 Föderation Bosnien und Herzegowina
14542 ---- BANJA LUKA            44.47   17.13   153 Republika Srpska
14543 ---- JAJCE                 44.21   17.16   430 Föderation Bosnien und Herzegowina
14544 ---- BUGOJNO               44.04   17.28   562 Föderation Bosnien und Herzegowina
14549 ---- ZENICA                44.13   17.54   345 Föderation Bosnien und Herzegowina
14554 ---- GRADACAC              44.53   18.26   136 Föderation Bosnien und Herzegowina
14557 ---- TUZLA                 44.33   18.42   305 Föderation Bosnien und Herzegowina
14640 LQLV LIVNO                 43.50   17.01   724 Föderation Bosnien und Herzegowina
14648 LQMO MOSTAR                43.21   17.48    99 Föderation Bosnien und Herzegowina
14650 ---- IVAN SEDLO            43.46   18.02   970 Föderation Bosnien und Herzegowina
14652 ---- BJELASNICA            43.43   18.16  2067 Föderation Bosnien und Herzegowina
14654 ---- SARAJEVO-BEJELAVE     43.52   18.26   630 Föderation Bosnien und Herzegowina
15020 ---- BOTOSANI              47.44   26.39   161 Kreis Botoșani
15080 LROD ORADEA                47.02   21.54   136 Kreis Bihor
15120 LRCL CLUJ-NAPOCA           46.47   23.34   410 Kreis Cluj
15145 LRTM TIRGU MURES           46.32   24.32   309 Kreis Mureș
15150 LRBC BACAU                 46.32   26.55   184 Barchau
15200 LRAR ARAD                  46.08   21.21   116 Kreis Arad
15235 ---- FAGARAS               45.51   24.59   428 Kreis Brașov
15247 LRTR TIMISOARA             45.46   21.15    86 Kreis Timiș
15260 LRSB SIBIU                 45.48   24.09   443 Hermannstadt
15302 ---- PREDEAL               45.30   25.35  1090 Kreis Brașov
15338 ---- ORAVITA               45.02   21.41   200 Kreis Caraș-Severin
15420 LRBS BUKAREST              44.30   26.08    90 Kreis Ilfov
15421 LROP BUKAREST/OTOPENI      44.33   26.06    95 Kreis Ilfov
15480 ---- CONSTANTA             44.13   28.39    13 Kreis Constanța
15552 LBWN VARNA                 43.12   27.55    41 Oblast Warna
15614 LBSF SOFIA                 42.39   23.23   588 Oblast Sofia-Stadt
15655 LBBG BURGAS                42.29   27.29    16 
16008 LIVE RESCHENPASS           46.37   10.32  1459 Trentino-Südtirol
16020 LIPB BOZEN                 46.28   11.20   241 Trentino-Südtirol
16021 LIVR PASSO ROLLE           46.18   11.47  2004 Trentino-Südtirol
16022 LIVP PAGANELLA             46.09   11.02  2125 Trentino-Südtirol
16033 LIVD DOBBIACO              46.44   12.13  1222 Trentino-Südtirol
16036 LIPA AVIANO                46.02   12.36   128 Friaul-Julisch Venetien
16040 LIVO TARVISIO              46.30   13.35   777 Friaul-Julisch Venetien
16045 LIPI UDINE/RIVOLTO         45.59   13.02    51 Friaul-Julisch Venetien
16052 LIMH PIAN ROSA             45.56    7.42  3480 Aostatal
16054 ---- AOSTA                 45.44    7.21   547 Aostatal
16059 LIMF TURIN                 45.13    7.39   301 Piemont
16066 LIMC MILANO/MALPENSA       45.37    8.44   234 Lombardei
16076 LIME BERGAMO               45.40    9.42   238 Lombardei
16080 LIML MAILAND               45.26    9.17   107 Lombardei
16084 LIMS PIACENZA              44.55    9.44   134 Emilia-Romagna
16088 LIPL BRESCIA/GHEDI         45.25   10.17   102 Lombardei
16090 LIPX VERONA                45.23   10.52    67 Venetien
16105 LIPZ VENEDIG               45.30   12.20     2 Venetien
16110 LIVT TRIEST                45.39   13.45     8 
16117 ---- CUNEO LEVALDIGI       44.33    7.38   385 Piemont
16120 LIMJ GENUA                 44.25    8.51     2 Ligurien
16125 ---- SARZANA/LUNI          44.05    9.59     9 Ligurien
16130 ---- PARMA                 44.49   10.18    50 Emilia-Romagna
16138 LIPF FERRARA               44.50   11.37    10 Emilia-Romagna
16140 LIPE BOLOGNA               44.32   11.18    36 Emilia-Romagna
16146 LIVM PUNTA MARINA          44.27   12.18     2 
16147 LIPK FORLI                 44.12   12.04    27 Emilia-Romagna
16149 LIPR RIMINI                44.02   12.37    12 Emilia-Romagna
16158 LIRP PISA-S.GIUSTO         43.41   10.23     2 Toskana
16170 LIRQ FLORENZ               43.48   11.12    40 Toskana
16191 LIPY FALCONARA             43.37   13.22    12 Marken
16206 LIRS GROSSETO              42.45   11.04     5 Toskana
16219 LIRK MONTE TERMINILLO      42.28   12.59  1874 Latium
16226 ---- L'AQUILA              42.23   13.20   668 Abruzzen
16230 LIBP PESCARA               42.26   14.12    10 Abruzzen
16242 LIRF ROM                   41.48   12.14     2 Latium
16244 ---- FROSINONE             41.38   13.18   180 Latium
16245 LIRE PRATICA DI MARE       41.39   12.26     6 Latium
16252 LIBS CAMPOBASSO            41.34   14.39   793 Molise
16261 ---- AMENDOLA              41.32   15.43    57 Apulien
16270 LIBD BARI                  41.08   16.47    34 Apulien
16280 LIQZ PONZA                 40.55   12.57   184 
16289 LIRN NEAPEL                40.51   14.18    88 Kampanien
16292 LIRI PONTECAGNANO          40.37   14.55    38 Kampanien
16294 LIQC CAPRI                 40.33   14.12   160 Kampanien
16320 LIBR BRINDISI              40.39   17.57    15 Apulien
16325 ---- MARINA DI GINOSA      40.25   16.53     1 Apulien
16362 LICA LAMEZIA TERME         38.54   16.15    15 Kalabrien
16405 LICJ PALERMO               38.11   13.06    21 Sizilien
16420 LICF MESSINA               38.12   15.33    59 Sizilien
16422 LICR REGGIO CALABRIA       38.04   15.39    11 Kalabrien
16429 LICT TRAPANI/BIRGI         37.55   12.30     7 Sizilien
16434 LICX PRIZZI                37.43   13.26  1034 Sizilien
16453 ---- GELA                  37.05   14.13    18 Sizilien
16460 LICC CATANIA               37.28   15.03    11 Sizilien
16464 ---- SIRACUSA /SICI        37.04   15.17     1 Sizilien
16531 LIEO OLBIA/COSTA SMERALDA  40.54    9.31    11 Sardinien
16549 ---- CARLOFORTE / ISOLA    39.08    8.19    11 
16550 ---- CAPO BELLAVISTA       39.56    9.43   138 
16560 LIEE CAGLIARI              39.15    9.03     4 Sardinien
16597 LMML MALTA                 35.51   14.29    91 
16606 ---- SERRAI                41.04   23.34    33 Decentralized Administration of Macedonia and Thrace
16622 LGTS THESSALONIKI          40.31   22.58     8 Decentralized Administration of Macedonia and Thrace
16624 ---- CHRYSOUPOLI           40.59   24.36     5 Decentralized Administration of Macedonia and Thrace
16627 LGAL ALEXANDROUPOLI        40.51   25.55     7 Decentralized Administration of Macedonia and Thrace
16632 LGKZ KOZANI                40.18   21.47   634 Dezentralisierte Verwaltung von Epirus und Westmakedonien
16641 LGKR KORFU                 39.37   19.55     2 Decentralized Administration of Peloponnese, Western Greece and the Ionian
16642 LGID IOANNINA NATIONAL     39.42   20.49   483 Dezentralisierte Verwaltung von Epirus und Westmakedonien
16648 LGLR LARISSA               39.38   22.25    74 Decentralized Administration of Thessaly and Central Greece
16650 LGLM LIMNOS                39.55   25.14     5 Decentralized Administration of the Aegean
16667 LGMT MYTILINI/AIRPORT      39.04   26.36     3 
16675 ---- STYLIS LAMIA          38.54   22.24   144 Decentralized Administration of Thessaly and Central Greece
16682 LGAD ANDRAVIDA             37.55   21.17    10 Decentralized Administration of Peloponnese, Western Greece and the Ionian
16684 LGSY SKYROS                38.58   24.29    27 Decentralized Administration of Thessaly and Central Greece
16685 LGKF KEFALHNIA             38.07   20.30    19 Decentralized Administration of Peloponnese, Western Greece and the Ionian
16706 LGHI CHIOS                 38.20   26.08     5 Decentralized Administration of the Aegean
16710 LGTP TRIPOLIS/INTL         37.32   22.24   644 Decentralized Administration of Peloponnese, Western Greece and the Ionian
16716 LGAT ATHEN                 37.54   23.44    28 Attika
16723 LGSM SAMOS                 37.42   26.55     2 Decentralized Administration of the Aegean
16726 LGKL KALAMATA              37.04   22.01     6 Decentralized Administration of Peloponnese, Western Greece and the Ionian
16732 LGNX NAXOS                 37.06   25.23     9 Decentralized Administration of the Aegean
16741 LGPA PAROS                 37.01   25.08    76 Decentralized Administration of the Aegean
16742 LGKO KOS                   36.47   27.04   129 Decentralized Administration of the Aegean
16743 LGKC KYTHIRA               36.17   23.01   167 Attika
16746 LGSA SOUDA/AIRPORT         35.29   24.07   146 
16749 LGRP RHODOS                36.24   28.05     4 Decentralized Administration of the Aegean
16754 LGIR HERAKLION             35.20   25.11    37 Kreta
16759 ---- TYMBAKION             35.00   24.45     7 Kreta
16765 LGKP KARPATHOS             35.31   27.15     6 
17022 LTAS ZONGULDAK             41.27   31.48   137 Zonguldak
17024 ---- INEBOLU               41.59   33.47    64 
17026 LTCM SINOP                 42.02   35.10    32 Sinop
17030 ---- SAMSUN                41.17   36.18     4 Samsun
17031 ---- CARSAMBA/SAMSUN       41.15   36.33     5 Samsun
17050 ---- EDIRNE                41.40   26.34    48 Edirne
17056 ---- TEKIRDAG              40.59   27.33     3 Tekirdağ
17060 LTBA ISTANBUL              40.58   28.49    48 Istanbul
17070 ---- BOLU                  40.44   31.36   743 Bolu
17090 LTAR SIVAS                 39.45   37.01  1285 Sivas
17116 LTBE BURSA                 40.11   29.04   100 Bursa
17128 LTAC ANKARA                40.07   32.59   953 Ankara
17195 LTAU KAYSERI/ERKILET       38.49   35.26  1055 Kayseri
17219 LTBJ IZMIR/ADNAN MENDERE   38.16   27.09   125 Izmir
17240 LTBM ISPARTA               37.45   30.33   997 Isparta
17244 LTAN KONYA                 37.58   32.33  1032 Konya
17260 LTAJ GAZIANTEP             37.05   37.22   705 Gaziantep
17290 LTBV BODRUM                37.02   27.26    26 
17295 LTBS MUGLA/DALAMAN         36.42   28.47     7 Muğla
17300 LTAI ANTALYA               36.42   30.44    50 
17350 LTAG ADANA                 37.00   35.25    73 Adana
17600 LCPH PAPHOS AIRPORT        34.43   32.29    11 Bezirk Paphos
17601 LCRA AKROTIRI              34.35   32.59    23 Akrotiri und Dekelia
17609 LCLK LARNAKA               34.53   33.38     2 Bezirk Larnaka
26038 EETN TALLIN                59.25   24.48    44 Kreis Harju
26063 ULLI ST.PETERSBURG         59.58   30.18     4 Sankt Petersburg
26115 ---- RISTNA                58.55   22.04     9 Kreis Hiiu
26242 EETU TARTU                 58.18   26.44    68 Kreis Tartu
26298 ---- BOLOGOE               57.54   34.03   188 Oblast Twer
26314 ---- VENTSPILS             57.24   21.32     2 Ventspils
26406 EVLA LIEPAJA               56.29   21.01     7 City of Liepāja
26422 EVRA RIGA                  56.58   24.04     3 Riga
26509 EYKL KLAIPEDA              55.42   21.09    10 Bezirk Klaipėda
26524 EYSA SIAULIAI              55.56   23.19   106 Bezirk Šiauliai
26554 ---- VERKHNEDVINSK         55.49   27.56   132 Wizebskaja Woblasz
26629 ---- KAUNAS POCIUNAI       54.53   23.50    76 Bezirk Kaunas
26659 ---- LEPEL                 54.53   28.42   174 Wizebskaja Woblasz
26666 UMII VITEBSK               55.10   30.13   176 Wizebskaja Woblasz
26702 UMKK KOENIGSBERG           54.42   20.37    27 Oblast Kaliningrad
26730 EYVI VILNIUS               54.38   25.17   189 Bezirk Vilnius
26825 UMMG GRODNO                53.36   24.03   134 Hrodsenskaja Woblasz
26850 UMMM MINSK                 53.52   27.32   234 Minskaja Woblasz
26863 UMOO MOGILEV YERM.         53.57   30.04   192 Mahiljouskaja Woblasz
26887 ---- KOSTUCKOVICHI         53.22   32.04   168 Mahiljouskaja Woblasz
33008 UMBB BREST                 52.07   23.41   142 Breszkaja Woblasz
33027 ---- ZHITCKOVICHI          52.13   27.52   138 Homelskaja Woblasz
33041 UMGG GOMEL                 52.24   30.57   125 Homelskaja Woblasz
33261 ---- KONOTOP               51.14   33.12   144 Sumy
33345 UKKK KIEW                  50.24   30.27   179 Kyiv city
33526 ---- IVANO-FRANKIVSK       48.56   24.42   275 Iwano-Frankiwsk
33791 ---- KRYVYI RIH            48.02   33.13   123 Oblast Dnipropetrowsk
33815 LUKK KISHINEV/KICHINAU     47.01   28.59   173 Rajon Criuleni
33837 UKOO ODESSA                46.29   30.38    64 Odessa
33990 ---- JALTA                 44.30   34.10    14 
34300 UKHH KHARKIV               49.58   36.08   154 Oblast Charkiw
34504 UKDD DNIPROPETROVSK        48.36   34.58   141 Oblast Dnipropetrowsk
40007 OSAP ALEPPO                36.20   37.13   425 Aleppo
40080 OSDI DAMASCUS              33.25   36.31   608 Gouvernement Rif Dimaschq
40100 OLBA BEIRUT                33.49   35.29    29 
40180 LLBG TEL AVIV              32.00   34.54    40 Zentralbezirk
40199 LLET EILAT                 29.33   34.57    12 Südbezirk
40270 OJAM AMMAN                 31.59   35.59   778 Gouvernement Amman
40272 OJAI AMMAN/QUENN ALIA      31.40   35.58   721 Gouvernement Amman
60101 GMTT TANGER                35.44   -5.54    19 
60115 GMFO OUJDA                 34.47   -1.56   468 Saida
60135 GMME RABAT                 34.03   -6.46    84 Fès-Meknès
60141 GMFF FES-SAIS              33.56   -4.59   579 Oriental
60150 GMFM MEKNES                33.53   -5.32   576 Fès-Meknès
60155 GMMC CASABLANCA            33.34   -7.40    62 Rabat-Salé-Kénitra
60156 GMMN CASABLANCA/MOHAMED    33.22   -7.35   200 Rabat-Salé-Kénitra
60230 GMMX MARRAKECH             31.37   -8.02   468 Marrakesch-Safi
60252 GMAD AGADIR/AL MASSIRA     30.20   -9.24    74 Souss-Massa
60338 ---- MELILLA               35.17   -2.57    47 Ain Temouchent
60360 DABB ANNABA                36.50    7.49     3 Annaba
60390 DAAG ALGIER                36.43    3.15    25 Algier
60419 DABC CONSTANTINE           36.17    6.37   694 Constantine
60475 DABS TEBESSA               35.25    8.07   821 Tebessa
60490 DAOO ORAN/ES SENIA         35.38   -0.36    90 Relizane
60566 DAUG GHARDAIA              32.24    3.48   468 Ghardaia
60571 DAOR BECHAR                31.30   -2.15   809 Bechar
60590 DAUE EL-GOLEA              30.34    2.52   397 Ghardaia
60710 DTKA TABARKA               36.57    8.45    21 Gouvernement Jendouba
60715 DTTA TUNIS                 36.50   10.14     5 Gouvernement Tunis
60725 DTTN JENDOUBA              36.29    8.48   143 Gouvernement Jendouba
60735 DTTK KAIROUAN              35.40   10.06    60 Gouvernement Kairouan
60740 DTMB MONASTIR/HABIB BOUR   35.45   10.45     2 Gouvernement Monastir
60750 DTTX SFAX EL-MAOU          34.43   10.41    21 sfaks
60760 DTTZ TOZEUR                33.55    8.06    87 Gouvernement Tozeur
60765 DTTG GABES                 33.53   10.06     4 Gabès
60769 DTTJ DJERBA                33.35   10.47     6 
62010 HLLT TRIPOLI               32.40   13.09    81 Tripolis
62019 HLRF SIRTE                 31.12   16.35    13 Munizip Surt
62053 HLLB BENGHAZI              32.06   20.16   131 Munizip Bengasi
62305 ---- SALLUM PLATEAU        31.34   25.07     6 Gouvernement Matruh
62306 HEMM MERSA MATRUH          31.20   27.13    25 Gouvernement Matruh
62318 HEAX ALEXANDRIA/NOUZHA     31.12   29.57    -2 Gouvernement al-Iskandariyya
62332 HEPS PORT SAID             31.17   32.14     1 Gouvernement Bur Saʿid
62366 HECA KAIRO                 30.08   31.24    64 Gouvernement Al-Qahira
A051  ---- WEESBY                54.50    9.09    22 Schleswig-Holstein
A112  ---- WRIXUM/FOEHR          54.42    8.32     8 Schleswig-Holstein
A138  ---- BORDELUM              54.38    8.56     8 Schleswig-Holstein
A159  ---- EGGEBEK               54.38    9.22    17 Schleswig-Holstein
A160  ---- FLENSBURG (SCHAEFERH  54.46    9.23    41 Schleswig-Holstein
A173  ---- SATRUP                54.41    9.38    35 Schleswig-Holstein
A191  ---- WAGERSROTT            54.40    9.48    40 Schleswig-Holstein
A201  ---- HALLIG HOOGE          54.34    8.31     4 Schleswig-Holstein
A216  ---- STRUCKLAHNUNGSHOERN   54.30    8.48     7 
A226  ---- HATTSTEDT             54.32    9.03     5 Schleswig-Holstein
A345  ---- GROSS WITTENSEE       54.24    9.46    15 Schleswig-Holstein
A351  ---- ERFDE                 54.18    9.19    18 Schleswig-Holstein
A397  ---- GROSSENBRODE          54.22   11.05     3 Schleswig-Holstein
A411  ---- KREMPEL               54.19    9.01     2 Schleswig-Holstein
A443  ---- OSTENFELD (RENDSBURG  54.19    9.48    14 Schleswig-Holstein
A473  ---- KOEHN                 54.21   10.27    40 Schleswig-Holstein
A480  ---- PUTLOS                54.19   10.48     5 
A481  ---- HOHWACHT              54.19   10.40    10 Schleswig-Holstein
A505  ---- BUESUM                54.07    8.52     3 
A536  ---- HAALE                 54.10    9.33    26 Schleswig-Holstein
A653  ---- PADENSTEDT (PONY-PAR  54.01    9.56    17 Schleswig-Holstein
A699  ---- TRAVEMUENDE           53.58   10.53     2 Schleswig-Holstein
A752  ---- WEDDELBROOK           53.54    9.50    18 Schleswig-Holstein
A762  ---- WITTENBORN            53.55   10.14    38 Schleswig-Holstein
A791  ---- SCHWARTAU,BAD -GROSS  53.56   10.42    26 Schleswig-Holstein
A940  ---- SPRENGE               53.41   10.22    55 Schleswig-Holstein
A981  ---- GRAMBEK               53.34   10.41    27 Schleswig-Holstein
B006  ---- HIDDENSEE-VITTE       54.35   13.06     1 
B040  ---- DARSSER ORT (SWN)     54.28   12.30     4 Mecklenburg-Vorpommern
B085  ---- SAGARD                54.31   13.32     5 Mecklenburg-Vorpommern
B158  ---- STEINHAGEN-NEGAST     54.15   13.03    16 Mecklenburg-Vorpommern
B203  ---- BASTORF-KAEGSDORF (S  54.08   11.40    51 Mecklenburg-Vorpommern
B258  ---- TRIBSEES              54.05   12.47     7 Mecklenburg-Vorpommern
B308  ---- KIRCHDORF/POEL        54.00   11.26    12 Mecklenburg-Vorpommern
B320  ---- GERSDORF              54.05   11.45    52 Mecklenburg-Vorpommern
B334  ---- GROSS LUESEWITZ       54.04   12.20    40 Mecklenburg-Vorpommern
B365  ---- SUEDERHOLZ-NEUENDORF  54.06   13.09     5 Mecklenburg-Vorpommern
B382  ---- KARLSHAGEN            54.06   13.50     1 Mecklenburg-Vorpommern
B482  ---- GROSS KIESOW-SCHLAGT  54.01   13.30    34 Mecklenburg-Vorpommern
B488  ---- ANKLAM                53.50   13.41     9 Mecklenburg-Vorpommern
B511  ---- GREVESMUEHLEN         53.50   11.10    25 Mecklenburg-Vorpommern
B525  ---- VENTSCHOW             53.47   11.34    43 Mecklenburg-Vorpommern
B531  ---- BAUMGARTEN            53.49   11.53    52 Mecklenburg-Vorpommern
B544  ---- PARUM                 53.49   12.07    10 Mecklenburg-Vorpommern
B556  ---- TETEROW               53.46   12.33    38 Mecklenburg-Vorpommern
B587  ---- RATHEBUR              53.44   13.47    10 Mecklenburg-Vorpommern
B629  ---- GOLDENBOW             53.32   11.46    52 Mecklenburg-Vorpommern
B670  ---- FRIEDLAND             53.39   13.32    22 Mecklenburg-Vorpommern
B687  ---- ROTHEMUEHL            53.36   13.49    23 Mecklenburg-Vorpommern
B710  ---- DODOW                 53.30   11.00    34 Mecklenburg-Vorpommern
B728  ---- NEUSTADT-GLEWE-FRIED  53.27   11.34    35 Mecklenburg-Vorpommern
B747  ---- PLAU AM SEE           53.27   12.15    66 Mecklenburg-Vorpommern
B766  ---- GROSS LUKOW           53.32   13.01    54 Mecklenburg-Vorpommern
B818  ---- REDEFIN               53.21   11.12    16 Mecklenburg-Vorpommern
B853  ---- RECHLIN               53.20   12.43    62 Mecklenburg-Vorpommern
B898  ---- GRAMBOW-SCHWENNENZ    53.23   14.22    50 Mecklenburg-Vorpommern
B926  ---- MALK GOEHREN          53.13   11.22    31 Mecklenburg-Vorpommern
B951  ---- KRUEMMEL              53.16   12.43    64 Mecklenburg-Vorpommern
C720  ---- HAMBURG-NEUWIEDENTH.  53.29    9.54     3 Hamburg
E006  ---- BORKUM-SUEDERSTRASSE  53.35    6.40    12 Niedersachsen
E008  ---- BORKUM-FLUGPLATZ      53.36    6.42     3 Niedersachsen
E025  ---- DORNUM                53.39    7.26     1 Niedersachsen
E031  ---- SPIEKEROOG (SWN)      53.46    7.40    14 
E043  ---- WANGERLAND-HOOKSIEL   53.39    8.05     8 
E067  ---- LANGEN-HOLSSEL, KREI  53.42    8.38    13 Niedersachsen
E078  ---- STEINAU,KR.CUXHAVEN   53.42    8.53     1 Niedersachsen
E082  ---- FREIBURG/ELBE         53.50    9.15     2 Niedersachsen
E087  ---- LAMSTEDT              53.38    9.06    25 Niedersachsen
E091  ---- DROCHTERSEN           53.43    9.23     1 Niedersachsen
E095  ---- RUTHENSTROM           53.43    9.25     7 Niedersachsen
E099  ---- MITTELNKIRCHEN-HOHEN  53.33    9.37     1 Niedersachsen
E103  ---- NORDEN-LEYBUCHTPOLDE  53.30    7.07     1 Niedersachsen
E145  ---- BUTJADINGEN-INTE      53.29    8.24     1 Niedersachsen
E158  ---- BEVERSTEDT            53.26    8.48     3 Niedersachsen
E200  ---- BOCKHORN-GRABSTEDE    53.22    7.58    11 Niedersachsen
E207  ---- DOLLART-KANALPOLDER   53.14    7.13     2 Niedersachsen
E212  ---- MOORMERLAND-NEERMOOR  53.19    7.26     0 Niedersachsen
E229  ---- WESTERSTEDE           53.15    7.56     7 Niedersachsen
E232  ---- OVELGOENNE            53.23    8.27     2 Niedersachsen
E234  ---- RASTEDE               53.15    8.13    16 Niedersachsen
E235  ---- BRAKE                 53.21    8.30     1 Niedersachsen
E246  ---- SCHWANEWEDE-NEUENKIR  53.13    8.31     1 Bremen
E254  ---- WORPSWEDE-HUETTENBUS  53.17    8.59     7 Niedersachsen
E277  ---- KOENIGSMOOR           53.14    9.39    40 Niedersachsen
E297  ---- BLECKEDE-WALMSBURG    53.14   10.51    12 Niedersachsen
E298  ---- WENDISCH EVERN        53.13   10.28    62 Niedersachsen
E335  ---- HUDE/OLDENBURG        53.07    8.25     4 Niedersachsen
E342  ---- OTTERSBERG-OTTERSTED  53.08    9.09    17 Niedersachsen
E355  ---- ROTENBURG (WÜMME)     53.08    9.20    32 Niedersachsen
E364  ---- HEESLINGEN-WIERSDORF  53.18    9.20    27 Niedersachsen
E387  ---- ZERNIEN               53.04   10.53    83 Niedersachsen
E426  ---- GROSSENKNETEN-AHL.    52.55    8.13    42 Niedersachsen
E438  ---- BASSUM                52.52    8.42    40 Niedersachsen
E445  ---- SCHWARME              52.54    9.03    12 Niedersachsen
E451  ---- VERDEN-DAUELSEN       52.57    9.14    21 Niedersachsen
E475  ---- UELZEN                52.56   10.32    50 Niedersachsen
E501  ---- TWIST-HEBELERMEER     52.45    7.05    19 Niedersachsen
E513  ---- GROSS BERSSEN         52.46    7.29    27 Niedersachsen
E525  ---- LOENINGEN             52.43    7.45    22 Niedersachsen
E545  ---- BARNSTORF             52.42    8.29    37 Niedersachsen
E564  ---- FRANKENFELD-HEDERN    52.46    9.24    18 Niedersachsen
E571  ---- FALLINGBOSTEL, BAD    52.51    9.41    70 Niedersachsen
E586  ---- SCHARNHORST-MARWEDE   52.44   10.21    72 Niedersachsen
E601  ---- RINGE-GROSSRINGE      52.36    6.54    13 Niedersachsen
E626  ---- ALFHAUSEN             52.29    7.55    65 Niedersachsen
E651  ---- KIRCHDORF, KREIS DIE  52.36    8.51    34 Niedersachsen
E652  ---- NIENBURG              52.40    9.13    25 Niedersachsen
E659  ---- REHBURG-LOCCUM        52.26    9.08    60 Niedersachsen
E662  ---- ESSEL                 52.41    9.39    28 Niedersachsen
E667  ---- NEUSTADT AM RUEBENBE  52.30    9.29    40 Niedersachsen
E672  ---- WEDEMARK-ELZE         52.35    9.44    39 Niedersachsen
E673  ---- CELLE (STADT)         52.37   10.04    38 Niedersachsen
E688  ---- UETZE                 52.27   10.11    60 Niedersachsen
E691  ---- WITTINGEN-VORHOP      52.39   10.40    72 Niedersachsen
E704  ---- BENTHEIM, BAD         52.18    7.08    50 Niedersachsen
E727  ---- ROTHENFELDE, BAD      52.06    8.11    95 Niedersachsen
E732  ---- HAMELN                52.05    9.23    68 Niedersachsen
E738  ---- RINTELN-VOLKSEN       52.08    9.07   212 Nordrhein-Westfalen
E739  ---- HAMELN-HASTENBECK     52.05    9.24    77 Niedersachsen
E744  ---- BARSINGHAUSEN-HOHENB  52.19    9.26   110 Niedersachsen
E748  ---- SALZHEMMENDORF-LAUEN  52.05    9.33   175 Niedersachsen
E755  ---- HANNOVER-HERRENHAUSE  52.24    9.40    50 Niedersachsen
E756  ---- HANNOVER-KIRCHRODE    52.22    9.49    57 Niedersachsen
E762  ---- LEHRTE-SIEVERSHAUSEN  52.22   10.08    66 Niedersachsen
E764  ---- SPRINGE               52.12    9.33    98 Niedersachsen
E792  ---- SUEPPLINGEN           52.14   10.55   129 Niedersachsen
E799  ---- CREMLINGEN-DESTEDT    52.15   10.43   160 Niedersachsen
E805  ---- OTTENSTEIN            51.57    9.24   295 Niedersachsen
E818  ---- BEVERN                51.51    9.30   110 Niedersachsen
E835  ---- EIMEN-VORWOHLE        51.53    9.44   265 Niedersachsen
E839  ---- MORINGEN-LUTTERBECK   51.43    9.50   240 Niedersachsen
E857  ---- NORTHEIM-STOECKHEIM   51.45    9.57   109 Niedersachsen
E858  ---- NORTHEIM-IMBSHAUSEN   51.46   10.02   212 Niedersachsen
E864  ---- SEESEN                51.54   10.11   186 Niedersachsen
E871  ---- LIEBENBURG-OTHFRESEN  52.01   10.24   187 Niedersachsen
E884  ---- LANGELSHEIM-ASTFELD   51.56   10.21   210 Niedersachsen
E897  ---- BAD HARZBURG          51.54   10.34   201 Niedersachsen
E902  ---- BODENFELDE-AMELITH    51.42    9.31   258 Niedersachsen
E944  ---- HERZBERG              51.38   10.22   238 Niedersachsen
E950  ---- HERZBERG-LONAU        51.41   10.21   340 Niedersachsen
E955  ---- LAUTERBERG,BAD-BARTO  51.36   10.28   305 Niedersachsen
E970  ---- DRANSFELD-OSSENFELD   51.32    9.48   317 Niedersachsen
F020  ---- MEYENBURG             53.18   12.18    98 Brandenburg
F050  ---- UCKERLAND-KARLSTEIN   53.26   13.49    40 Brandenburg
F069  ---- HOHENREINKENDORF      53.14   14.20    46 Brandenburg
F105  ---- LENZEN/ELBE           53.06   11.29    20 Brandenburg
F108  ---- KARSTAEDT/PRIGNITZ    53.10   11.45    32 Brandenburg
F125  ---- KUHBIER               53.09   12.05    63 Brandenburg
F143  ---- WITTSTOCK-ROTE MÜHLE  53.11   12.30    66 Brandenburg
F151  ---- MENZ                  53.06   13.03    77 Brandenburg
F172  ---- MITTENWALDE/UCKERMAR  53.11   13.39    72 Brandenburg
F178  ---- NEURUPPIN-GUEHLEN GL  53.03   12.45    89 Brandenburg
F191  ---- PASSOW                53.09   14.06    12 Brandenburg
F199  ---- BERKHOLZ-MEYENBURG    53.03   14.15    14 Brandenburg
F210  ---- PERLEBERG             53.06   11.52    40 Brandenburg
F263  ---- ZEHDENICK             52.58   13.20    51 Brandenburg
F280  ---- FRIEDRICHSWALDE       53.01   13.43    75 Brandenburg
F305  ---- KLESSEN               52.44   12.30    38 Brandenburg
F325  ---- KREMMEN-GROSS ZIETHE  52.44   13.01    46 Brandenburg
F338  ---- MARWITZ (WASSERWERK)  52.40   13.11    33 Brandenburg
F361  ---- HECKELBERG            52.45   13.51    82 Brandenburg
F385  ---- WUSTROW               52.46   14.13     6 Brandenburg
F419  ---- WUSTERWITZ            52.22   12.23    36 Brandenburg
F431  ---- BERGE                 52.37   12.47    40 Brandenburg
F448  ---- STAAKEN               52.32   13.07    31 Berlin
F451  ---- AHRENSFELDE           52.35   13.34    60 Brandenburg
F470  ---- STRAUSBERG            52.35   13.56    81 Brandenburg
F475  ---- MUENCHEBERG           52.31   14.08    63 Brandenburg
F518  ---- BRANDENBURG/HAVEL     52.25   12.34    31 Brandenburg
F520  ---- GROSS KREUTZ          52.24   12.48    31 Brandenburg
F545  ---- THYROW                52.15   13.14    43 Brandenburg
F598  ---- POHLITZ               52.11   14.34    70 Brandenburg
F620  ---- BRUECK-GOEMNIGK       52.10   12.44    52 Brandenburg
F635  ---- FELGENTREU            52.06   13.00    48 Brandenburg
F660  ---- MUENCHEHOFE           52.09   13.50    44 Brandenburg
F681  ---- NEU MADLITZ           52.22   14.15    46 Brandenburg
F695  ---- COSCHEN               52.01   14.44    40 Brandenburg
F707  ---- LANGENLIPSDORF        51.55   13.05    91 Brandenburg
F736  ---- HOHENBUCKO            51.46   13.28   131 Brandenburg
F742  ---- LUEBBEN-BLUMENFELDE   51.56   13.53    57 Brandenburg
F757  ---- BISCHDORF, KREIS OBE  51.48   13.58    78 Brandenburg
F770  ---- LIEBEROSE             51.59   14.18    47 Brandenburg
F878  ---- GRAUSTEIN             51.34   14.29   139 Brandenburg
F925  ---- ELSTERWERDA           51.27   13.30    90 Brandenburg
F951  ---- KLETTWITZ             51.33   13.53   128 Brandenburg
G002  ---- BERLIN-BUCH           52.38   13.30    60 Berlin
G005  ---- BERLIN-MARZAHN        52.33   13.34    60 Berlin
G006  ---- BERLIN-KANISWALL      52.24   13.44    33 Berlin
H009  ---- WESTERKAPPELN         52.17    7.52    92 Nordrhein-Westfalen
H012  ---- RAHDEN-VARL           52.27    8.35    41 Nordrhein-Westfalen
H027  ---- PETERSHAGEN           52.23    9.01    43 Nordrhein-Westfalen
H058  ---- STEINFURT-BURGSTEINF  52.08    7.19    70 Nordrhein-Westfalen
H061  ---- HOERSTEL              52.15    7.39    46 Nordrhein-Westfalen
H081  ---- ESPELKAMP-ISENSTEDT   52.21    8.39    65 Nordrhein-Westfalen
H119  ---- COESFELD              51.58    7.09    87 Nordrhein-Westfalen
H142  ---- LIENEN-KATTENVENNE    52.07    7.52    55 Nordrhein-Westfalen
H145  ---- OSTBEVERN-SCHIRLHEID  52.01    7.51    55 Nordrhein-Westfalen
H170  ---- ENGER                 52.09    8.31   128 Nordrhein-Westfalen
H174  ---- BIELEFELD-DEPPENDORF  52.04    8.27   105 Nordrhein-Westfalen
H203  ---- KLEVE                 51.46    6.06    46 Nordrhein-Westfalen
H212  ---- DAHLEM-SCHMIDTHEIM    50.25    6.34   573 Nordrhein-Westfalen
H235  ---- REKEN-GROSS REKEN     51.49    7.05    59 Nordrhein-Westfalen
H247  ---- LUEDINGHAUSEN-BROCH.  51.46    7.31    59 Nordrhein-Westfalen
H257  ---- DRENSTEINFURT         51.46    7.45    72 Nordrhein-Westfalen
H261  ---- HARSEWINKEL           51.59    8.13    63 Nordrhein-Westfalen
H265  ---- GUETERSLOH/EMS        51.56    8.19    70 Nordrhein-Westfalen
H281  ---- LAGE, KREIS LIPPE-HO  51.57    8.46   154 Nordrhein-Westfalen
H311  ---- XANTEN                51.42    6.24    20 Nordrhein-Westfalen
H330  ---- HALTERN (WASSERWERK)  51.44    7.12    41 Nordrhein-Westfalen
H333  ---- OLFEN                 51.42    7.21    49 Nordrhein-Westfalen
H361  ---- BECKUM-UNTERBERG      51.43    8.04   120 Nordrhein-Westfalen
H372  ---- DELBRUECK             51.47    8.34    88 Nordrhein-Westfalen
H376  ---- SALZKOTTEN            51.43    8.35    93 Nordrhein-Westfalen
H377  ---- LIPPSTADT-BOEKENFOER  51.38    8.24    92 Nordrhein-Westfalen
H391  ---- BRAKEL                51.42    9.10   145 Nordrhein-Westfalen
H401  ---- GELDERN-WALBECK       51.30    6.14    40 Nordrhein-Westfalen
H411  ---- BORKEN/WESTFALEN      51.52    6.53    48 Nordrhein-Westfalen
H419  ---- DUISBURG-BAERL        51.31    6.42    25 Nordrhein-Westfalen
H420  ---- DINSLAKEN             51.35    6.47    53 Nordrhein-Westfalen
H432  ---- BOCHUM                51.29    7.16   101 Nordrhein-Westfalen
H443  ---- WALTROP-ABDINGHOF     51.36    7.24    68 Nordrhein-Westfalen
H450  ---- FROENDENBERG-HOHENHE  51.29    7.47   240 Nordrhein-Westfalen
H460  ---- SASSENDORF, BAD-BEUS  51.33    8.11   171 Nordrhein-Westfalen
H475  ---- RUETHEN               51.30    8.26   361 Nordrhein-Westfalen
H477  ---- WUENNENBERG-EILERN    51.33    8.47   312 Nordrhein-Westfalen
H492  ---- BORGENTREICH          51.34    9.14   206 Nordrhein-Westfalen
H512  ---- NETTETAL-HUELST       51.18    6.12    45 Nordrhein-Westfalen
H522  ---- TOENISVORST           51.17    6.27    37 Nordrhein-Westfalen
H542  ---- GEVELSBERG-OBERB.     51.20    7.21   205 Nordrhein-Westfalen
H543  ---- BRECKERFELD-WENGEBER  51.15    7.28   440 Nordrhein-Westfalen
H547  ---- BUCHENHOFEN           51.14    7.06   130 Nordrhein-Westfalen
H568  ---- NEUENRADE-BLINTROP    51.17    7.51   296 Nordrhein-Westfalen
H572  ---- ARNSBERG-NEHEIM       51.28    7.59   159 Nordrhein-Westfalen
H573  ---- ARNSBERG-MUESCHEDE    51.25    8.01   278 Nordrhein-Westfalen
H579  ---- ESLOHE                51.16    8.10   325 Nordrhein-Westfalen
H581  ---- WARSTEIN-HIRSCHBERG   51.26    8.16   331 Nordrhein-Westfalen
H591  ---- BRILON-THÜLEN         51.25    8.39   457 Nordrhein-Westfalen
H606  ---- HEINSBERG-SCHLEIDEN   51.02    6.06    57 Nordrhein-Westfalen
H612  ---- REICHSHOF-ECKENHAGEN  50.59    7.41   348 Nordrhein-Westfalen
H635  ---- DORMAGEN-ZONS         51.07    6.51    36 Nordrhein-Westfalen
H641  ---- SOLINGEN-HOHENSCHEID  51.08    7.06   154 Nordrhein-Westfalen
H655  ---- WIPPERFUERTH-GARDEWE  51.10    7.25   360 Nordrhein-Westfalen
H658  ---- MEINERZHAGEN-REDLEND  51.05    7.38   380 Nordrhein-Westfalen
H669  ---- ATTENDORN-NEULISTERN  51.07    7.53   311 Nordrhein-Westfalen
H678  ---- LENNESTADT-THETEN     51.08    8.02   286 Nordrhein-Westfalen
H681  ---- SCHMALLENBERG-SELLIN  51.13    8.16   443 Nordrhein-Westfalen
H695  ---- MEDEBACH-BERGE        51.10    8.43   380 Nordrhein-Westfalen
H718  ---- JUELICH (KLAERANLAGE  50.56    6.21    76 Nordrhein-Westfalen
H721  ---- BEDBURG-WEILER HOHEN  51.01    6.31   101 Nordrhein-Westfalen
H755  ---- OVERATH-BOEKE         50.58    7.17   221 Nordrhein-Westfalen
H768  ---- MOENCHENGLADBACH-HIL  51.08    6.22    77 Nordrhein-Westfalen
H777  ---- WENDEN-DOERNSCHEID    50.56    7.51   418 Nordrhein-Westfalen
H791  ---- BERLEBURG, BAD-ARFEL  51.01    8.26   436 Nordrhein-Westfalen
H795  ---- BAD BERLEBURG-STÜNZE  50.59    8.22   610 Nordrhein-Westfalen
H827  ---- NIDEGGEN-SCHMIDT      50.40    6.25   370 Nordrhein-Westfalen
H862  ---- NEUNKIRCHEN-SEELSCHE  50.51    7.22   195 Nordrhein-Westfalen
H883  ---- SIEGEN (KLÄRANLAGE)   50.51    8.00   263 Nordrhein-Westfalen
H884  ---- BIRKELBACH            51.01    8.16   541 Nordrhein-Westfalen
H889  ---- BURBACH-WUERGENDORF   50.45    8.08   413 Nordrhein-Westfalen
H908  ---- MONSCHAU-KALTERHERBE  50.31    6.12   535 Wallonische Region
H932  ---- WEILERSWIST-LOMMERSU  50.43    6.48   146 Nordrhein-Westfalen
H981  ---- KALL-SISTIG           50.30    6.32   505 Nordrhein-Westfalen
J702  ---- PERL-NENNIG           49.32    6.23   152 Saarland
J709  ---- MERZIG                49.27    6.38   171 Saarland
J728  ---- WEISKIRCHEN/SAAR      49.33    6.49   380 Saarland
J731  ---- NOHFELDEN-GONNESWEIL  49.33    7.04   403 Saarland
J812  ---- SCHMELZ-HUETTERSDORF  49.25    6.50   223 Saarland
J815  ---- NEUNKIRCHEN-WELLESW.  49.21    7.14   236 Saarland
J846  ---- HOMBURG/SAAR          49.20    7.21   235 Saarland
J908  ---- SAARBRUECKEN-BURBACH  49.15    6.56   190 Saarland
K017  ---- HILGENROTH            50.44    7.39   295 Rheinland-Pfalz
K026  ---- WALLMENROTH           50.47    7.50   172 Rheinland-Pfalz
K038  ---- BAD NEUENAHR-AHRWEIL  50.32    7.05   111 Rheinland-Pfalz
K057  ---- HUEMMERICH            50.34    7.29   328 Rheinland-Pfalz
K081  ---- HACHENBURG/WESTERWAL  50.40    7.48   322 Rheinland-Pfalz
K132  ---- SINZIG                50.33    7.15    60 Rheinland-Pfalz
K170  ---- HOEHR-GRENZHAUSEN     50.26    7.40   241 Rheinland-Pfalz
K172  ---- SELTERS, WESTERWALDK  50.31    7.44   239 Rheinland-Pfalz
K191  ---- WESTERBURG/RHLPF.     50.33    7.58   355 Rheinland-Pfalz
K210  ---- SCHNEIFELFORSTHAUS    50.17    6.25   657 Rheinland-Pfalz
K212  ---- ROTH BEI PRUEM        50.18    6.23   593 Rheinland-Pfalz
K219  ---- LISSENDORF            50.19    6.37   407 Rheinland-Pfalz
K230  ---- RODDER                50.24    6.51   512 Rheinland-Pfalz
K240  ---- KALTENBORN, HOHE ACH  50.24    7.00   570 Rheinland-Pfalz
K259  ---- POLCH, KR. MAYEN-KOB  50.18    7.19   235 Rheinland-Pfalz
K272  ---- NASSAU (KLAERANLAGE)  50.19    7.47    80 Rheinland-Pfalz
K282  ---- MONTABAUR             50.26    7.49   253 Rheinland-Pfalz
K290  ---- EPPENROD/BORNBACH     50.24    7.56   300 Rheinland-Pfalz
K295  ---- HOLZHEIM BEI DIEZ     50.21    8.03   155 Rheinland-Pfalz
K300  ---- WINTERSPELT           50.14    6.12   426 Rheinland-Pfalz
K308  ---- LAUPERATH-SCHEIDCHEN  50.05    6.19   517 Rheinland-Pfalz
K310  ---- PRUEM-WATZERATH       50.11    6.22   386 Rheinland-Pfalz
K317  ---- WEISSENSEIFEN         50.09    6.33   530 Rheinland-Pfalz
K318  ---- DENSBORN              50.08    6.36   308 Rheinland-Pfalz
K322  ---- KIRCHWEILER           50.14    6.45   570 Rheinland-Pfalz
K326  ---- OBERSTADTFELD         50.10    6.46   421 Rheinland-Pfalz
K339  ---- STROHN                50.07    6.55   390 Rheinland-Pfalz
K354  ---- KAIL                  50.11    7.14   290 Rheinland-Pfalz
K380  ---- OBERBACHHEIM          50.15    7.45   328 Rheinland-Pfalz
K381  ---- SINGHOFEN (KLAERANLA  50.16    7.49   220 Rheinland-Pfalz
K386  ---- NASTÄTTEN             50.12    7.52   268 Rheinland-Pfalz
K419  ---- OLSDORF               49.56    6.23   305 Rheinland-Pfalz
K428  ---- BITBURG               49.59    6.32   359 Rheinland-Pfalz
K431  ---- MEISBURG              50.06    6.40   523 Rheinland-Pfalz
K440  ---- MANDERSCHEID          50.06    6.48   413 Rheinland-Pfalz
K446  ---- WITTLICH              49.58    6.56   147 Rheinland-Pfalz
K463  ---- BLANKENRATH           50.02    7.18   417 Rheinland-Pfalz
K475  ---- LINGERHAHN (WWV RLP)  50.06    7.34   482 Rheinland-Pfalz
K501  ---- KIRCHBERG, RHEIN-HUN  49.56    7.23   393 Rheinland-Pfalz
K509  ---- NEWEL                 49.49    6.35   365 Rheinland-Pfalz
K511  ---- SPEICHER              49.56    6.38   325 Rheinland-Pfalz
K515  ---- ZEMMER (FORSTHAUS MU  49.52    6.42   293 Rheinland-Pfalz
K517  ---- BEUREN (HOCHWALD)     49.44    6.55   505 Rheinland-Pfalz
K531  ---- BERNKASTEL-KUES       49.55    7.04   120 Rheinland-Pfalz
K533  ---- KLEINICH, KR. BERNKA  49.54    7.11   438 Rheinland-Pfalz
K539  ---- BRUCHWEILER, KR. BIR  49.48    7.14   545 Rheinland-Pfalz
K557  ---- SEESBACH, KR. BAD KR  49.51    7.33   394 Rheinland-Pfalz
K568  ---- BAD KREUZNACH         49.51    7.51   100 Rheinland-Pfalz
K584  ---- MAINZ (ZDF)           49.58    8.13   195 Rheinland-Pfalz
K589  ---- HAHNHEIM              49.52    8.14   120 Rheinland-Pfalz
K611  ---- TRIER-ZEWEN           49.44    6.37   132 Rheinland-Pfalz
K612  ---- TRIER-IRSCH           49.44    6.42   228 Rheinland-Pfalz
K633  ---- HUETTGESWASEN         49.44    7.08   650 Rheinland-Pfalz
K650  ---- KIRN                  49.47    7.29   181 Rheinland-Pfalz
K666  ---- BAYERFELD-STECKWEILE  49.42    7.50   310 Rheinland-Pfalz
K685  ---- ALZEY                 49.44    8.07   215 Rheinland-Pfalz
K699  ---- WORMS                 49.36    8.22    88 Rheinland-Pfalz
K701  ---- KIRF-BEUREN           49.33    6.27   325 Rheinland-Pfalz
K711  ---- OBERZERF              49.35    6.41   370 Rheinland-Pfalz
K744  ---- KUSEL (KLAERANLAGE)   49.32    7.26   215 Rheinland-Pfalz
K747  ---- HENSCHTAL             49.28    7.25   250 Rheinland-Pfalz
K755  ---- EINOELLEN             49.37    7.39   303 Rheinland-Pfalz
K761  ---- DOERRMOSCHEL-FELSBER  49.36    7.44   442 Rheinland-Pfalz
K762  ---- RUPPERTSECKEN         49.39    7.53   461 Rheinland-Pfalz
K764  ---- HOMBERG-SCHOENBORNER  49.38    7.30   411 Rheinland-Pfalz
K767  ---- ENKENBACH             49.32    7.53   300 Rheinland-Pfalz
K784  ---- GRUENSTADT            49.34    8.11   160 Rheinland-Pfalz
K863  ---- KAISERSLAUTERN        49.26    7.44   270 Rheinland-Pfalz
K866  ---- TRIPPSTADT-NEUHOF     49.21    7.48   348 Rheinland-Pfalz
K881  ---- BAD DUERKHEIM         49.28    8.12   107 Rheinland-Pfalz
K918  ---- ZWEIBRUECKEN (KLAERA  49.15    7.20   225 Rheinland-Pfalz
K925  ---- PIRMASENS             49.11    7.36   390 Rheinland-Pfalz
K969  ---- RUELZHEIM             49.10    8.18   105 Rheinland-Pfalz
K984  ---- HIRSCHTHAL            49.03    7.45   205 Rheinland-Pfalz
K986  ---- BUNDENTHAL            49.05    7.50   210 Rheinland-Pfalz
K988  ---- BAD BERGZABERN        49.06    8.00   252 Rheinland-Pfalz
L021  ---- TRENDELBURG           51.35    9.26   133 Hessen
L031  ---- WESTERTAL-LIPPOLDSB.  51.37    9.35   176 Hessen
L071  ---- LIEBENAU-HAUEDA       51.29    9.15   162 Hessen
L101  ---- WILLINGEN/HOCHSAUERL  51.17    8.35   588 Hessen
L113  ---- KORBACH-RHENA         51.17    8.48   458 Hessen
L121  ---- TWISTETAL-MUEHLHAUS.  51.20    8.55   295 Hessen
L125  ---- WALDECK-ALRAFT        51.15    8.58   300 Hessen
L130  ---- AROLSEN-LANDAU        51.21    9.05   265 Hessen
L131  ---- AROLSEN-VOLKHARDINGH  51.19    9.03   365 Hessen
L171  ---- WITZENHAUSEN-ZIEGENH  51.22    9.45   220 Hessen
L201  ---- BATTENBERG-HOF KARLS  51.04    8.32   590 Hessen
L215  ---- FRANKENBERG-GEISMAR   51.05    8.53   392 Hessen
L217  ---- BURGWALD-BOTTENDORF   51.02    8.49   293 Hessen
L222  ---- VOEHL-BUCHENBERG      51.10    8.52   380 Hessen
L245  ---- WABERN-HEBEL          51.04    9.23   203 Hessen
L271  ---- HESSISCH LICHTENAU-F  51.13    9.42   340 Hessen
L286  ---- SONTRA                51.03    9.55   365 Hessen
L291  ---- ESCHWEGE              51.11   10.04   170 Hessen
L292  ---- ESCHWEGE-ELTMANNSHAU  51.12    9.59   250 Hessen
L299  ---- HERLESHAUSEN-ARCHFEL  51.03   10.09   380 Hessen
L312  ---- WETTER/HESSEN-AMOENA  50.54    8.42   227 Hessen
L319  ---- COELBE                50.51    8.46   182 Hessen
L340  ---- GILSERBERG-MOISCHEID  50.58    9.03   340 Hessen
L355  ---- NEUKIRCHEN-HAUPTSCHW  50.54    9.24   500 Hessen
L409  ---- DRIEDORF              50.38    8.11   482 Hessen
L411  ---- DILLENBURG            50.44    8.16   314 Hessen
L442  ---- AMOENEBURG-RUEDIGHEI  50.47    8.57   210 Hessen
L463  ---- ALSFELD               50.45    9.15   305 Hessen
L464  ---- ALSFELD-EIFA          50.45    9.21   300 Hessen
L483  ---- HAUNETAL-WEHRDA       50.44    9.40   257 Hessen
L505  ---- WALDBRUNN-LAHR        50.31    8.08   280 Hessen
L511  ---- LOEHNBERG-OBERSH.     50.34    8.14   230 Hessen
L521  ---- ASSLAR KLEIN-ALTENST  50.35    8.28   200 Hessen
L555  ---- SCHOTTEN              50.30    9.07   265 Hessen
L561  ---- LAUTERTAL-HOERGENAU   50.35    9.17   522 Hessen
L582  ---- PETERSBERG-MARBACH    50.37    9.43   305 Hessen
L592  ---- TANN/RHOEN            50.38   10.01   395 Hessen
L602  ---- RUNKEL-ENNERICH       50.24    8.09   168 Hessen
L612  ---- WEILMUENSTER          50.26    8.23   183 Hessen
L617  ---- CAMBERG, BAD          50.17    8.18   244 Hessen
L631  ---- MUENZENBERG-GAMBACH   50.27    8.44   155 Hessen
L635  ---- BAD NAUHEIM           50.22    8.46   142 Hessen
L652  ---- GEDERN-SCHOENHAUSEN   50.24    9.12   407 Hessen
L678  ---- SCHLÜCHTERN-HEROLZ    50.21    9.33   230 Hessen
L685  ---- GREBENSTEIN           51.27    9.25   190 Hessen
L714  ---- HOHENSTEIN-BREITHARD  50.12    8.05   315 Hessen
L722  ---- WALDEMS-REINBORN      50.16    8.22   380 Hessen
L732  ---- HOMBURG, BAD (FILTER  50.15    8.34   255 Hessen
L744  ---- VILBEL, BAD-DORTELWE  50.13    8.45   125 Hessen
L751  ---- NIDDERAU-ERBSTADT     50.16    8.52   162 Hessen
L771  ---- GRUENDAU-BREITENBORN  50.16    9.11   258 Hessen
L773  ---- WAECHTERSBACH         50.15    9.17   138 Hessen
L781  ---- SODEN,BAD-SALMUENSTE  50.16    9.22   145 Hessen
L803  ---- RUEDESHEIM-PRESBERG   50.03    7.53   403 Hessen
L819  ---- WIESBADEN-BIEBRICH    50.03    8.14    90 Hessen
L821  ---- WIESBADEN-AURINGEN    50.08    8.19   263 Hessen
L829  ---- RAUNHEIM              50.00    8.26    89 Hessen
L850  ---- MUEHLHEIM/MAIN        50.08    8.49   102 Hessen
L865  ---- GROSS-GERAU-WALLERST  49.54    8.27    87 Hessen
L886  ---- DARMSTADT             49.53    8.41   162 Hessen
L891  ---- ROEDERMARK-OBER-RODE  49.59    8.50   137 Hessen
L892  ---- REINHARDSHAGEN-VAAKE  51.29    9.37   115 Hessen
L894  ---- SCHAAFHEIM-SCHLIERB.  49.55    8.58   155 Hessen
L926  ---- LAUTERTAL/ODENWALD-R  49.43    8.41   208 Hessen
L930  ---- REINHEIM              49.49    8.49   165 Hessen
L947  ---- MICHELSTADT           49.41    9.01   204 Hessen
L979  ---- BIRKENAU              49.34    8.42   172 Hessen
L988  ---- BEERFELDEN            49.34    8.58   450 Hessen
M031  ---- ELLRICH-WERNA         51.35   10.43   235 Thüringen
M056  ---- REINHOLTERODE         51.25   10.11   336 Thüringen
M146  ---- HELBEDUENDORF-KEULA   51.20   10.32   431 Thüringen
M225  ---- MÜHLHAUSEN-GÖRMAR     51.12   10.30   190 Thüringen
M259  ---- FREIENBESSINGEN       51.14   10.46   296 Thüringen
M281  ---- ETZLEBEN              51.16   11.11   134 Thüringen
M299  ---- OLBERSLEBEN           51.09   11.20   160 Thüringen
M301  ---- SUEDEICHSFELD-WENDEH  51.10   10.15   290 Thüringen
M348  ---- DACHWIG               51.04   10.52   173 Thüringen
M357  ---- ALPERSTEDT            51.06   11.03   158 Thüringen
M405  ---- MOORGRUND-GRAEFENDOR  50.51   10.15   283 Thüringen
M412  ---- HOERSELBERG-HAINICH-  51.01   10.31   290 Thüringen
M448  ---- WEIMAR-SCHOENDORF     51.01   11.21   325 Thüringen
M473  ---- CROSSEN/ELSTER-NICKE  50.59   12.00   272 Thüringen
M480  ---- MEUSELWITZ            51.03   12.18   173 Thüringen
M488  ---- TEGKWITZ              50.59   12.21   193 Thüringen
M500  ---- PONITZ                50.51   12.25   222 Thüringen
M520  ---- WALTERSHAUSEN         50.54   10.33   353 Thüringen
M552  ---- JENA (STERNWARTE)     50.56   11.35   155 Thüringen
M557  ---- BUCHA                 50.52   11.30   310 Thüringen
M565  ---- BOBECK                50.54   11.48   344 Thüringen
M620  ---- KLEINER INSELBERG     50.51   10.29   732 Thüringen
M640  ---- DREI GLEICHEN-MUEHLB  50.52   10.49   286 Thüringen
M651  ---- ILMTAL-DIENSTEDT      50.48   11.10   325 Thüringen
M691  ---- HARTH-POELLNITZ NEUN  50.46   11.59   340 Thüringen
M700  ---- GEISA                 50.43    9.57   280 Thüringen
M721  ---- SCHMALKALDEN          50.44   10.27   330 Thüringen
M732  ---- MARTINRODA            50.44   10.53   430 Thüringen
M756  ---- SCHWARZBURG           50.39   11.12   277 Thüringen
M765  ---- ROCKENDORF            50.41   11.31   280 Thüringen
M772  ---- SCHMIERITZ-WELTWITZ   50.44   11.50   340 Thüringen
M799  ---- GOETTENDORF           50.40   12.05   390 Thüringen
M805  ---- BIRX                  50.32   10.03   745 Thüringen
M833  ---- FRAUENWALD            50.36   10.51   768 Thüringen
M834  ---- SCHLEUSINGEN          50.31   10.46   399 Thüringen
M846  ---- KATZHUETTE            50.33   11.02   450 Thüringen
M909  ---- ROEMHILD-SUELZDORF    50.25   10.29   330 Thüringen
M927  ---- VEILSDORF             50.25   10.49   397 Thüringen
M938  ---- FRANKENBLICK-MENGERS  50.23   11.08   508 Thüringen
M945  ---- JUDENBACH-NEUENBAU    50.27   11.14   738 Thüringen
M965  ---- BAD LOBENSTEIN        50.27   11.38   500 Thüringen
M978  ---- HIRSCHBERG            50.24   11.49   446 Bayern
M998  ---- NEUHAUS-SCHIERSCHNIT  50.20   11.14   383 Thüringen
N104  ---- DIESDORF              52.45   10.53    65 Sachsen-Anhalt
N135  ---- WINTERFELD-SALLENTHI  52.45   11.15    35 Sachsen-Anhalt
N158  ---- BALLERSTEDT           52.44   11.43    35 Sachsen-Anhalt
N182  ---- SCHWARZHOLZ           52.45   11.59    30 Sachsen-Anhalt
N199  ---- SCHOLLENE             52.40   12.11    29 Sachsen-Anhalt
N214  ---- KOECKTE               52.31   11.08    59 Sachsen-Anhalt
N268  ---- GRIEBEN               52.25   11.58    38 Sachsen-Anhalt
N272  ---- DEMKER                52.31   11.51    36 Sachsen-Anhalt
N305  ---- BOESDORF              52.25   11.05    68 Sachsen-Anhalt
N315  ---- BORN                  52.22   11.28    66 Sachsen-Anhalt
N345  ---- ZIELITZ               52.18   11.40    52 Sachsen-Anhalt
N366  ---- BURG-BLUMENTHAL       52.19   11.50    39 Sachsen-Anhalt
N398  ---- DREWITZ BEI BURG      52.13   12.10    80 Sachsen-Anhalt
N426  ---- WEISSENFELS-WENGELSD  51.16   12.03    92 Sachsen-Anhalt
N435  ---- BOTTMERSDORF-KLEIN G  52.01   11.24    83 Sachsen-Anhalt
N440  ---- SCHACKENSLEBEN        52.12   11.25    95 Sachsen-Anhalt
N463  ---- KOENIGSBORN           52.08   11.47    52 Sachsen-Anhalt
N500  ---- BUEHNE-RIMBECK        52.00   10.38   100 Sachsen-Anhalt
N520  ---- PABSTORF              52.02   10.58   112 Sachsen-Anhalt
N532  ---- HECKLINGEN-GROSS BOE  51.53   11.28   104 Sachsen-Anhalt
N543  ---- WALTERNIENBURG-RONNE  51.58   11.55    52 Sachsen-Anhalt
N548  ---- BERNBURG/SAALE        51.49   11.43    84 Sachsen-Anhalt
N553  ---- BADEWITZ BEI ZERBST   52.01   12.10    82 Sachsen-Anhalt
N563  ---- DUEBEN                51.56   12.23    95 Sachsen-Anhalt
N566  ---- JESSNITZ              51.41   12.18    74 Sachsen-Anhalt
N587  ---- NAUNDORF BEI SEYDA    51.55   12.53   100 Sachsen-Anhalt
N601  ---- SCHIERKE              51.46   10.39   609 Sachsen-Anhalt
N616  ---- OBERHARZ AM BROCKEN   51.40   10.53   504 Sachsen-Anhalt
N620  ---- QUEDLINBURG           51.48   11.08   142 Sachsen-Anhalt
N632  ---- MEHRINGEN/ASL         51.44   11.31   107 Sachsen-Anhalt
N652  ---- KOETHEN (ANHALT)      51.45   12.01    76 Sachsen-Anhalt
N671  ---- KEMBERG-RADIS         51.45   12.31    94 Sachsen-Anhalt
N714  ---- SUEDHARZ-DIETERSDORF  51.32   11.03   440 Sachsen-Anhalt
N731  ---- MANSFELD-ANNARODE     51.33   11.24   321 Sachsen-Anhalt
N748  ---- QUERFURT-LODERSL.     51.23   11.33   204 Sachsen-Anhalt
N750  ---- SEEGEBIET MANSFELDER  51.33   11.42   154 Sachsen-Anhalt
N815  ---- BIBRA, BAD-ALTENRODA  51.14   11.35   267 Sachsen-Anhalt
N855  ---- FREYBURG/UNSTRUT-ZEU  51.14   11.50   140 Sachsen-Anhalt
N924  ---- KREIPITZSCH           51.06   11.43   246 Sachsen-Anhalt
N977  ---- ZEITZ                 51.03   12.09   170 Sachsen-Anhalt
O025  ---- BAD MUSKAU            51.34   14.42   125 Sachsen
O039  ---- SCHOENWOELKAU-BRINNI  51.31   12.26   101 Sachsen
O057  ---- KLITSCHEN BEI TORGAU  51.31   12.54    85 Sachsen
O099  ---- HAEHNICHEN-TREBUS     51.21   14.50   163 Sachsen
O141  ---- BELGERSHAIN           51.14   12.33   150 Sachsen
O182  ---- BOXBERG               51.24   14.34   125 Sachsen
O204  ---- MARKRANSTAEDT-GROSSL  51.19   12.10   118 Sachsen
O248  ---- HEYDA BEI RIESA       51.16   13.22   132 Sachsen
O251  ---- STRAUCH               51.22   13.35   128 Sachsen
O268  ---- SCHOENTEICHEN-CUNNER  51.19   14.03   166 Sachsen
O305  ---- PEGAU                 51.10   12.16   128 Sachsen
O322  ---- GRIMMA-KLEINBOTHEN    51.12   12.46   134 Sachsen
O348  ---- GARSEBACH BEI MEISSE  51.08   13.26   157 Sachsen
O384  ---- KUBSCHUETZ,KR.BAUTZ.  51.10   14.30   232 Sachsen
O457  ---- DRESDEN-STREHLEN      51.02   13.47   119 Sachsen
O458  ---- DRESDEN-HOSTERWITZ    51.01   13.51   114 Sachsen
O461  ---- PULSNITZ              51.12   14.01   270 Sachsen
O484  ---- SOHLAND/SPREE         51.04   14.26   290 Sachsen
O499  ---- OSTRITZ               51.02   14.56   213 Sachsen
O510  ---- ALTGERINGSWALDE       51.05   12.56   296 Sachsen
O536  ---- NOSSEN                51.03   13.18   308 Sachsen
O543  ---- WILSDRUFF-MOHORN      51.00   13.28   288 Sachsen
O566  ---- LOHMEN/SACHSEN        50.60   13.59   195 Sachsen
O580  ---- DUERRHENNERSDORF      51.03   14.37   332 Sachsen
O598  ---- BERTSDORF-HOERNITZ    50.54   14.45   270 Sachsen
O625  ---- FRANKENBERG-ALTENHAI  50.53   13.03   326 Sachsen
O660  ---- DIPPOLDISWALDE-REIN.  50.55   13.43   365 Sachsen
O708  ---- CRIMMITSCHAU-MANNICH  50.49   12.18   327 Sachsen
O725  ---- SANKT EGIDIEN-KUHSCH  50.48   12.38   321 Sachsen
O795  ---- ROSENTHAL-BIELATAL    50.50   14.04   460 Sachsen
O805  ---- LICHTENTANNE          50.41   12.26   353 Sachsen
O842  ---- DEUTSCHNEUDORF-BRUED  50.37   13.29   688 Sachsen
O846  ---- MARIENBERG-RUEBENAU   50.35   13.18   727 Sachsen
O868  ---- TREUEN                50.33   12.17   465 Sachsen
O877  ---- STUETZENGRUEN-HUNDSH  50.33   12.34   604 Sachsen
O882  ---- TANNENBERG            50.36   12.56   532 Sachsen
O888  ---- RASCHAU               50.31   12.50   507 Sachsen
O950  ---- WEISCHLITZ-HEINERSGR  50.23   12.00   517 Sachsen
O974  ---- KLINGENTHAL-KAMERUN   50.22   12.29   730 Sachsen
O980  ---- ELSTER, BAD-SOHL      50.16   12.17   560 Sachsen
O993  ---- ERLBACH-EUBABRUNN     50.18   12.23   565 Sachsen
P004  ---- OBERLEICHTERSBACH-MO  50.16    9.46   470 Bayern
P013  ---- SANDBERG              50.21   10.00   510 Bayern
P022  ---- OSTHEIM V.D. RHOEN    50.27   10.13   312 Bayern
P025  ---- NEUSTADT, BAD         50.18   10.11   230 Bayern
P029  ---- MASSBACH              50.11   10.16   326 Bayern
P032  ---- AUBSTADT              50.20   10.27   304 Bayern
P033  ---- BAD KOENIGSHOFEN      50.17   10.27   288 Bayern
P038  ---- SULZDORF AN DER LEDE  50.15   10.34   332 Bayern
P041  ---- RODACH (KLAERANLAGE)  50.20   10.48   300 Bayern
P048  ---- PFARRWEISACH-LOHR (P  50.09   10.42   270 Bayern
P051  ---- MEEDER-OTTOWIND       50.21   10.53   450 Bayern
P052  ---- NEUSTADT BEI COBURG   50.19   11.07   330 Bayern
P058  ---- ITZGRUND-HERRETH      50.08   10.56   367 Bayern
P062  ---- LUDWIGSSTADT-LAUENST  50.31   11.22   520 Bayern
P066  ---- KRONACH               50.15   11.19   312 Bayern
P068  ---- BURGKUNSTADT          50.09   11.14   276 Bayern
P071  ---- TEUSCHNITZ            50.24   11.23   633 Bayern
P073  ---- STEBEN, BAD           50.22   11.37   608 Bayern
P079  ---- LUDWIGSCHORGAST       50.07   11.34   336 Bayern
P086  ---- HELMBRECHTS           50.14   11.42   650 Bayern
P088  ---- STAMMBACH-QUERENBACH  50.09   11.44   598 Bayern
P095  ---- REHAU                 50.13   12.02   587 Bayern
P098  ---- SELB/OBERFRANKEN      50.12   12.09   609 Bayern
P099  ---- SELB-SPIELBERG        50.10   12.02   610 Bayern
P100  ---- KAHL (MAIN)           50.04    9.00   107 Bayern
P104  ---- HEINRICHSTHAL         50.04    9.21   450 Bayern
P106  ---- GROSSOSTHEIM          49.55    9.05   110 Bayern
P113  ---- LOHR/MAIN-HALSBACH    50.01    9.39   285 Bayern
P120  ---- GRAEFENDORF,KR.MAIN-  50.07    9.44   160 Bayern
P122  ---- HAMMELBURG            50.07    9.54   220 Bayern
P125  ---- ARNSTEIN-MUEDESHEIM   49.58    9.55   220 Bayern
P131  ---- SCHONUNGEN-MAINBERG   50.04   10.18   304 Bayern
P137  ---- KOLITZHEIM            49.55   10.14   230 Bayern
P141  ---- KOENIGSBERG/BAYERN-H  50.05   10.29   259 Bayern
P147  ---- OBERAURACH-FATSCHENB  49.55   10.36   426 Bayern
P148  ---- EBRACH                49.51   10.30   346 Bayern
P151  ---- RENTWEINSDORF-TREINF  50.04   10.49   258 Bayern
P158  ---- SCHESSLITZ-KOETTENSD  49.57   11.01   304 Bayern
P164  ---- THURNAU-TANNFELD      49.59   11.24   513 Bayern
P165  ---- STADELHOFEN           50.00   11.12   460 Bayern
P168  ---- AUFSESS-HOCHSTAHL     49.53   11.16   432 Bayern
P173  ---- PRESSECK              50.14   11.33   640 Bayern
P175  ---- HEINERSREUTH-VOLLHOF  49.58   11.31   350 Bayern
P179  ---- CREUSSEN-BUEHL        49.51   11.37   450 Bayern
P182  ---- FICHTELBERG/OBERFRA.  49.59   11.50   657 Bayern
P185  ---- WALDERSHOF-SCHAFBRUC  49.56   12.06   723 Bayern
P188  ---- KEMNATH               49.52   11.53   460 Bayern
P189  ---- PRESSATH-MUEHLBERG    49.47   12.02   595 Bayern
P190  ---- HOHENBERG/EGER        50.06   12.13   517 Bayern
P197  ---- MAEHRING              49.55   12.32   676 Bayern
P198  ---- TIRSCHENREUTH-LODERM  49.51   12.21   500 Bayern
P208  ---- AMORBACH-NEUDORF      49.39    9.16   420 Bayern
P212  ---- HASLOCH/MAIN (SCHIRR  49.47    9.28   130 Bayern
P222  ---- ALTERTHEIM-OBERALTER  49.44    9.46   300 Bayern
P228  ---- BUETTHARD             49.36    9.53   263 Bayern
P232  ---- KITZINGEN             49.44   10.11   188 Bayern
P233  ---- SCHWARZACH/MAIN (KLA  49.48   10.13   188 Bayern
P236  ---- MARKT BIBART          49.40   10.23   317 Bayern
P238  ---- GOLLHOFEN             49.35   10.12   308 Bayern
P243  ---- SCHLUESSELFELD (KLAE  49.45   10.39   290 Bayern
P249  ---- WILHELMSDORF/MITTELF  49.34   10.44   358 Bayern
P252  ---- ALTENDORF/OBERFRANKE  49.48   11.00   250 Bayern
P257  ---- MOEHRENDORF-KLSEE.    49.39   11.01   268 Bayern
P262  ---- GOESSWEINSTEIN        49.46   11.18   443 Bayern
P265  ---- GRAEFENBERG-KASBERG   49.40   11.14   506 Bayern
P266  ---- LAUF/PEGNITZ (KLAERA  49.30   11.16   310 Bayern
P270  ---- PLECH                 49.39   11.28   443 Bayern
P271  ---- PEGNITZ (KLAERANLAGE  49.44   11.33   420 Bayern
P280  ---- NEUSTADT AM KULM      49.49   11.52   452 Bayern
P287  ---- FREIHUNG-GROSSSCHOEN  49.34   11.53   493 Bayern
P292  ---- PLOESSBERG-LIEBENSTE  49.49   12.20   530 Bayern
P294  ---- FLOSSENBUERG          49.44   12.21   622 Bayern
P298  ---- WAIDHAUS-PFRENTSCH    49.37   12.29   499 Bayern
P299  ---- SCHOENSEE-DIETERSDOR  49.32   12.34   685 Bayern
P300  ---- SIMMERSHOFEN-ADELHOF  49.32   10.09   337 Bayern
P302  ---- BURGBERNHEIM          49.27   10.20   350 Bayern
P305  ---- ROTHENBURG OB DER TA  49.23   10.10   412 Bayern
P306  ---- COLMBERG-BINZWANGEN   49.23   10.22   434 Bayern
P308  ---- NEUBURG/KAMMEL-LANGE  48.19   10.23   495 Bayern
P310  ---- WINDSHEIM, BAD        49.31   10.25   310 Bayern
P317  ---- WEIHENZELL-GRUEB      49.20   10.36   474 Bayern
P318  ---- HERRIEDEN (KLAERANLA  49.14   10.30   420 Bayern
P319  ---- WEIDENBACH-WEIHERSCH  49.14   10.37   455 Bayern
P321  ---- LANGENZENN            49.30   10.47   370 Bayern
P327  ---- ROHR/MITTELFRANKEN-D  49.18   10.55   402 Bayern
P333  ---- NUERNBERG-NETZSTALL   49.26   11.15   368 Bayern
P337  ---- WENDELSTEIN-KLEINSCH  49.21   11.06   331 Bayern
P339  ---- FREYSTADT-OBERNDORF   49.11   11.23   436 Bayern
P343  ---- POMMELSBRUNN-MITTEL.  49.29   11.32   522 Bayern
P348  ---- NEUMARKT/OBERPFALZ    49.17   11.27   420 Bayern
P352  ---- EDELSFELD             49.35   11.42   535 Bayern
P354  ---- AMBERG-UNTERAMMERSR.  49.28   11.51   383 Bayern
P355  ---- ROELLBACH             49.46    9.15   239 Bayern
P356  ---- KASTL, KREIS AMBERG-  49.22   11.42   424 Bayern
P359  ---- SCHMIDMUEHLEN         49.17   11.55   453 Bayern
P362  ---- NABBURG (FLUSSMEISTE  49.27   12.11   366 Bayern
P363  ---- SCHMIDGADEN           49.25   12.05   416 Bayern
P366  ---- SCHWANDORF            49.20   12.05   356 Bayern
P370  ---- TRAUSNITZ-REISACH     49.32   12.17   465 Bayern
P372  ---- OBERVIECHTACH         49.27   12.26   596 Bayern
P374  ---- ALTENDORF             49.24   12.17   391 Bayern
P376  ---- NEUNBURG VORM WALD-E  49.22   12.27   420 Bayern
P379  ---- RODING-NEUBAEU        49.14   12.25   388 Bayern
P380  ---- RODING-WETTERFELD     49.13   12.32   373 Bayern
P382  ---- TREFFELSTEIN-WITZELS  49.24   12.36   470 Bayern
P389  ---- WEIDING, KREIS CHAM-  49.16   12.45   425 Bayern
P396  ---- NEUKIRCHEN BEI HEILI  49.15   12.58   460 Bayern
P405  ---- DINKELSBUEHL-OBERWIN  49.03   10.17   491 Bayern
P410  ---- BECHHOFEN/MITTELFRAN  49.10   10.36   425 Bayern
P411  ---- HAUNDORF-OBERERLBACH  49.11   10.49   449 Bayern
P417  ---- WASSERTRUEDINGEN (KL  49.02   10.36   420 Bayern
P418  ---- POLSINGEN-DOECKINGEN  48.56   10.45   510 Bayern
P420  ---- PLEINFELD-MANDLESMUE  49.07   10.58   380 Bayern
P422  ---- ROTHSEE BEI ALLERSBE  49.13   11.11   376 Bayern
P425  ---- THALMAESSING          49.05   11.13   417 Bayern
P433  ---- BERCHING              49.07   11.26   403 Bayern
P441  ---- PARSBERG/OBERPFALZ    49.09   11.41   549 Bayern
P444  ---- BERATZHAUSEN          49.06   11.48   463 Bayern
P448  ---- RIEDENBURG            48.57   11.44   363 Bayern
P449  ---- KELHEIM (KANALSCHLEU  48.55   11.51   350 Bayern
P451  ---- TEUBLITZ (KLAERANLAG  49.13   12.05   350 Bayern
P453  ---- NITTENAU-HARTING      49.10   12.17   430 Bayern
P460  ---- HAGELSTADT            48.54   12.13   364 Bayern
P463  ---- SCHORNDORF-KNOEBLING  49.10   12.37   399 Bayern
P466  ---- STALLWANG             49.03   12.38   390 Bayern
P467  ---- WIESENFELDEN-UTZENZE  49.02   12.33   680 Bayern
P468  ---- AHOLFING              48.57   12.28   330 Bayern
P472  ---- PRACKENBACH           49.07   12.49   588 Bayern
P477  ---- SANKT ENGLMAR         49.00   12.49   810 Bayern
P481  ---- LAM-LAMBACH           49.13   13.04   692 Bayern
P485  ---- LINDBERG-BUCHENAU     49.02   13.20   740 Bayern
P486  ---- TEISNACH              49.03   13.00   400 Bayern
P501  ---- REIMLINGEN            48.50   10.30   435 Bayern
P505  ---- AURA IM SINNGRUND     50.11    9.34   287 Bayern
P515  ---- DONAUWOERTH-OSTERWE.  48.44   10.45   434 Bayern
P517  ---- BISSINGEN (KLAERANLA  48.43   10.38   425 Bayern
P521  ---- TAGMERSHEIM-BLOSSENA  48.49   10.56   522 Bayern
P522  ---- EICHSTAETT-LANDERSH.  48.53   11.14   384 Bayern
P532  ---- KOESCHING             48.50   11.29   415 Bayern
P535  ---- INGOLSTADT (FLUSSMEI  48.46   11.27   360 Bayern
P542  ---- MARKT ERLBACH-MOSBA.  49.32   10.39   362 Bayern
P546  ---- SIEGENBURG (KLAERANL  48.46   11.51   380 Bayern
P548  ---- ELSENDORF-HORNECK     48.42   11.51   425 Bayern
P549  ---- GEISENFELD-EICHELBER  48.39   11.35   395 Bayern
P551  ---- LANGQUAID-OBERSCHNEI  48.52   12.02   378 Bayern
P557  ---- HOHENTHANN            48.39   12.05   470 Bayern
P568  ---- PILSTING-BAECKERMUEH  48.41   12.37   344 Bayern
P571  ---- BOGEN-PFELLING        48.53   12.45   345 Bayern
P572  ---- METTEN                48.51   12.55   313 Bayern
P576  ---- MOOS,KR. DEGGENDORF-  48.47   12.57   320 Bayern
P581  ---- KIRCHBERG/NIEDERBAYE  48.54   13.09   683 Bayern
P585  ---- OSTERHOFEN-THUNDORF   48.45   13.01   310 Bayern
P586  ---- SALDENBURG-ENTSCHENR  48.47   13.19   456 Bayern
P594  ---- GRAINERT-REHBERG      48.47   13.38   628 Bayern
P597  ---- BUECHLBERG-TANNOED    48.39   13.30   460 Bayern
P599  ---- SONNEN                48.41   13.44   847 Bayern
P602  ---- DILLINGEN-FRISTINGEN  48.33   10.34   419 Bayern
P606  ---- GUENZBURG             48.29   10.16   444 Bayern
P609  ---- ZUSMARSHAUSEN         48.25   10.36   443 Bayern
P611  ---- WERTINGEN             48.34   10.42   415 Bayern
P618  ---- DIEDORF/SCHWABEN-BIB  48.22   10.46   498 Bayern
P621  ---- RAIN AM LECH-WALLERD  48.37   11.00   462 Bayern
P626  ---- DASING (KLAERANLAGE)  48.23   11.03   460 Bayern
P627  ---- SCHROBENHAUSEN        48.33   11.17   409 Bayern
P629  ---- ALTOMUENSTER-MAISBRU  48.24   11.19   510 Bayern
P637  ---- SCHEYERN              48.30   11.27   481 Bayern
P639  ---- FAHRENZHAUSEN         48.22   11.34   458 Bayern
P642  ---- SCHWEITENKIRCHEN-SUE  48.31   11.39   499 Bayern
P645  ---- NANDLSTADT            48.31   11.50   475 Bayern
P655  ---- LANDSHUT-REITHOF      48.34   12.16   490 Bayern
P656  ---- VILSHEIM-MUENCHSDORF  48.27   12.09   450 Bayern
P658  ---- STEINKIRCHEN-HOFSTAR  48.23   12.06   485 Bayern
P659  ---- OBERSCHLEISSHEIM      48.15   11.33   484 Bayern
P661  ---- LOICHING              48.37   12.25   416 Bayern
P663  ---- MAMMING-SCHNEIDERBER  48.37   12.37   447 Bayern
P664  ---- MARKLKOFEN (BETRIEBS  48.34   12.34   400 Bayern
P666  ---- VILSBIBURG            48.27   12.20   461 Bayern
P668  ---- GANGKOFEN (KLAERANLA  48.26   12.34   434 Bayern
P669  ---- NEUMARKT-SANKT VEIT   48.22   12.31   440 Bayern
P672  ---- EICHENDORF            48.38   12.51   350 Bayern
P674  ---- FALKENBERG,KR.ROTTAL  48.29   12.44   472 Bayern
P677  ---- EGGENFELDEN           48.24   12.44   410 Bayern
P678  ---- WURMANNSQUICK-EGELSB  48.21   12.46   475 Bayern
P681  ---- ALDERSBACH-KRIESTORF  48.37   13.03   342 Bayern
P682  ---- EGING AM SEE-ROHRBAC  48.44   13.16   415 Bayern
P687  ---- PFARRKIRCHEN          48.26   13.00   378 Bayern
P688  ---- ROTTHALMUENSTER (LAN  48.22   13.12   387 Bayern
P689  ---- POCKING               48.24   13.19   323 Bayern
P697  ---- UNTERGRIESBACH-SCHAI  48.36   13.39   495 Bayern
P699  ---- UNTERGRIESBACH-GLOTZ  48.34   13.45   575 Bayern
P702  ---- WEISSENHORN-OBERREIC  48.19   10.12   500 Bayern
P718  ---- BREITENBRUNN-FUERBUC  48.08   10.22   610 Bayern
P724  ---- SCHWABMUENCHEN        48.12   10.44   538 Bayern
P732  ---- MERING (BAUHOF)       48.16   10.59   510 Bayern
P741  ---- MAISACH-GALGEN        48.12   11.12   530 Bayern
P760  ---- NASSENFELS            48.48   11.13   401 Bayern
P761  ---- ADELSDORF (KLAERANLA  49.43   10.55   260 Bayern
P764  ---- HAIMHAUSEN-OTTERSHAU  48.18   11.32   464 Bayern
P765  ---- ISEN-WESTACH          48.12   12.02   550 Bayern
P768  ---- EBERSBERG-HALBING     48.06   11.59   592 Bayern
P769  ---- FINSING (KRAFTWERK)   48.13   11.48   498 Bayern
P771  ---- DORFEN (KLAERANLAGE)  48.16   12.10   430 Bayern
P777  ---- JETTENBACH            48.11   12.23   403 Bayern
P781  ---- AMPFING (KLAERANLAGE  48.16   12.26   400 Bayern
P785  ---- TUESSLING             48.12   12.38   417 Bayern
P788  ---- TACHERTING-SPREIT     48.05   12.30   508 Bayern
P794  ---- SIMBACH/INN           48.16   13.02   360 Bayern
P803  ---- OTTOBEUREN            47.56   10.19   665 Bayern
P804  ---- ATTENKAM              47.53   11.22   672 Bayern
P811  ---- OBERSTAUFEN-THALKIRC  47.33   10.06   748 Bayern
P817  ---- KAUFBEUREN            47.52   10.36   716 Bayern
P818  ---- KRAFTISRIED           47.46   10.28   831 Bayern
P821  ---- BUCHLOE               48.02   10.44   626 Bayern
P824  ---- VILGERTSHOFEN-PFLUGD  47.58   10.55   685 Bayern
P825  ---- EBERFING              47.48   11.12   611 Bayern
P829  ---- STEINGADEN-LAUTERBAC  47.43   10.53   782 Bayern
P830  ---- OBERHACHING-LAUFZORN  48.01   11.33   604 Bayern
P831  ---- WIELENBACH            47.53   11.10   550 Bayern
P833  ---- DIESSEN/AMMERSEE-DET  47.58   11.01   658 Bayern
P846  ---- SCHAEFTLARN-KLOSTER   47.59   11.28   557 Bayern
P850  ---- UTTING-ACHSELSCHWANG  48.02   11.03   591 Bayern
P856  ---- HOLZKIRCHEN           47.53   11.42   685 Bayern
P860  ---- DEISENHOFEN, KREIS M  48.02   11.35   585 Bayern
P862  ---- FELDKIRCHEN-WESTERHA  47.56   11.54   517 Bayern
P870  ---- IRSCHENBERG-KASTHUB   47.49   11.52   715 Bayern
P873  ---- VOGTAREUTH (KLAERANL  47.57   12.10   464 Bayern
P874  ---- AMERANG-PFAFFING      48.01   12.18   515 Bayern
P875  ---- CHIEMSEE-HERRENCHIEM  47.52   12.24   536 Bayern
P877  ---- ROSENHEIM             47.53   12.08   444 Bayern
P881  ---- TROSTBERG             48.02   12.32   559 Bayern
P887  ---- SIGMARSZELL-ZEISERTS  47.35    9.45   507 Bayern
P892  ---- WAGING AM SEE         47.55   12.45   475 Bayern
P893  ---- TEISENDORF            47.51   12.50   496 Bayern
P894  ---- WAGING AM SEE-SCHNOE  47.58   12.46   470 Bayern
P903  ---- LINDAU (SWN)          47.32    9.41   397 
P904  ---- SIEGSDORF-HOELL       47.50   12.39   721 Bayern
P905  ---- WEILER-SIMMERBERG (K  47.34    9.54   600 Bayern
P908  ---- OBERREUTE             47.33    9.56   903 Bayern
P914  ---- IMMENSTADT-REUTE      47.36   10.12   960 Bayern
P915  ---- OBERSTDORF-ROHRMOOS   47.24   10.10  1067 Bayern
P916  ---- BALDERSCHWANG         47.28   10.06  1037 Bayern
P917  ---- SONTHOFEN (FLUSSMEIS  47.31   10.16   730 Bayern
P919  ---- MINDELHEIM            48.04   10.29   590 Bayern
P923  ---- MARKTOBERDORF-SULZSC  47.43   10.39   790 Bayern
P924  ---- OY-MITTELBERG-PETERS  47.38   10.23   872 Bayern
P927  ---- HINDELANG-UNTERJOCH   47.33   10.26  1015 Bayern
P929  ---- SCHWANGAU-HORN (LFW)  47.35   10.43   796 Bayern
P931  ---- BERNBEUREN-PRACHTSRI  47.44   10.45   936 Bayern
P934  ---- HALBLECH-TRAUCHGAU    47.39   10.48   780 Bayern
P936  ---- SEEG (KLAERANLAGE)    47.40   10.38   802 Bayern
P937  ---- ETTAL-LINDERHOF       47.34   10.58   940 Bayern
P942  ---- BAD KOHLGRUB          47.40   11.05   750 Bayern
P944  ---- OBERAMMERGAU          47.36   11.04   835 Bayern
P945  ---- SCHLEHDORF            47.39   11.19   609 Bayern
P946  ---- MEHRING, KR. ALTOETT  48.11   12.49   411 Bayern
P947  ---- KOCHEL-EINSIEDL (KRA  47.34   11.18   805 Bayern
P948  ---- Mittenwald-B.wiesen   47.29   11.16   983 Bayern
P949  ---- MITTENWALD/OBB.       47.26   11.16   923 Bayern
P950  ---- KRUEN                 47.30   11.17   873 Bayern
P956  ---- JACHENAU-TANNERN      47.38   11.31   720 Bayern
P957  ---- LENGGRIES (SYLVENSTE  47.35   11.33   737 Bayern
P958  ---- KREUTH-GLASHUETTE     47.37   11.39   897 Bayern
P960  ---- WAAKIRCHEN-DEMMELBER  47.45   11.42   815 Bayern
P962  ---- FEILNBACH, BAD        47.46   12.01   530 Bayern
P963  ---- ASSLING               47.59   12.00   500 Bayern
P965  ---- MIESBACH (KLAERANLAG  47.48   11.49   650 Bayern
P966  ---- OBERE FIRSTALM/SCHLI  47.40   11.51  1369 Bayern
P971  ---- BRANNENBURG-DEGERNDO  47.43   12.07   481 Bayern
P972  ---- TEISENDORF-BABING     47.50   12.49   590 Bayern
P973  ---- TEISENDORF-NEUKIRCHE  47.49   12.46   780 Bayern
P974  ---- ASCHAU-STEIN          47.44   12.18   680 Bayern
P975  ---- KIEFERSFELDEN         47.37   12.10   518 Bayern
P979  ---- SAMERBERG-GEISENKAM   47.47   12.13   687 Bayern
P981  ---- UNTERWOESSEN-HINTERW  47.43   12.28   647 Bayern
P982  ---- REIT IM WINKEL 2      47.41   12.28   685 Bayern
P983  ---- RUHPOLDING (KLAERANL  47.46   12.39   650 Bayern
P986  ---- INZELL                47.46   12.45   690 Bayern
P987  ---- GRASSAU               47.48   12.29   540 Bayern
P988  ---- ALTUSRIED-MUTHMANNSH  47.48   10.06   730 Bayern
P989  ---- TITTMONING            48.04   12.46   382 Oberösterreich
P990  ---- LAUFEN/OBB.-LEBENAU   47.57   12.54   430 Bayern
P991  ---- PIDING                47.46   12.55   458 Bayern
P994  ---- MARKTSCHELLENBERG     47.42   13.02   501 Bayern
P995  ---- RAMSAU-SCHWARZECK/SC  47.38   12.54  1088 Bayern
P996  ---- BERCHTESGADEN         47.38   13.00   600 Bayern
P997  ---- BERCHTESGADEN/JENNER  47.36   13.01   980 Bayern
Q027  ---- NECKARGEMUEND-KLEING  49.24    8.48   117 Baden-Württemberg
Q033  ---- KOENIGHEIM            49.37    9.36   225 Baden-Württemberg
Q047  ---- ELZTAL-RITTERSBACH    49.26    9.15   312 Baden-Württemberg
Q053  ---- WALLDUERN             49.35    9.24   404 Baden-Württemberg
Q055  ---- BUCHEN,KR.NECKAR-OD.  49.31    9.19   340 Baden-Württemberg
Q056  ---- BETZWEILER-WAELDE     48.23    8.29   538 Baden-Württemberg
Q059  ---- SECKACH               49.26    9.20   334 Baden-Württemberg
Q060  ---- STOCKACH              47.52    9.01   532 Baden-Württemberg
Q061  ---- NOTZINGEN             48.40    9.28   325 Baden-Württemberg
Q062  ---- FREUDENBERG/MAIN-BOX  49.46    9.24   193 Baden-Württemberg
Q066  ---- LAUDA-KOENIGSHOFEN-H  49.33    9.38   324 Baden-Württemberg
Q067  ---- WIESENSTEIG           48.34    9.38   565 Baden-Württemberg
Q076  ---- BAD MERGENTHEIM-NEUN  49.29    9.46   250 Baden-Württemberg
Q077  ---- SAULGAU,BAD           48.02    9.29   576 Baden-Württemberg
Q104  ---- WAGHAEUSEL-KIRRLACH   49.15    8.32   105 Baden-Württemberg
Q152  ---- MOECKMUEHL (LUBW)     49.18    9.22   170 Baden-Württemberg
Q165  ---- INGELFINGEN-STACHEN.  49.20    9.42   385 Baden-Württemberg
Q171  ---- KUPFERZELL-RECHBACH   49.15    9.40   354 Baden-Württemberg
Q218  ---- BRETTEN, KREIS KARLS  49.02    8.43   170 Baden-Württemberg
Q221  ---- EPPINGEN-ELSENZ       49.10    8.51   220 Baden-Württemberg
Q222  ---- KOENIGSBACH-STEIN, E  48.58    8.35   160 Baden-Württemberg
Q242  ---- OBERSULM-WILLSBACH    49.08    9.21   230 Baden-Württemberg
Q261  ---- WUESTENROT-OBERHEIMB  49.08    9.30   392 Baden-Württemberg
Q292  ---- KIRCHBERG-JAGST       49.11    9.59   426 Baden-Württemberg
Q293  ---- CRAILSHEIM (LUBW)     49.09   10.04   395 Baden-Württemberg
Q295  ---- STIMPFACH-WEIPERTSHO  49.05   10.07   453 Baden-Württemberg
Q318  ---- WILDBAD, BAD-CALMBAC  48.47    8.35   385 Baden-Württemberg
Q327  ---- HERRENALB, BAD (LUBW  48.48    8.27   350 Baden-Württemberg
Q332  ---- PFORZHEIM-ISPRINGEN   48.56    8.42   333 Baden-Württemberg
Q333  ---- BRUCHSAL-HEIDELSHEIM  49.07    8.38   130 Baden-Württemberg
Q334  ---- ABTSGMUEND-UNTERGROE  48.55    9.55   432 Baden-Württemberg
Q340  ---- VAIHINGEN/ ENZ        48.55    8.57   200 Baden-Württemberg
Q341  ---- SACHSENHEIM           48.57    9.04   250 Baden-Württemberg
Q351  ---- GROSSENLACH MANNENW.  49.01    9.36   523 Baden-Württemberg
Q358  ---- STUTTGART NECKARTAL   48.47    9.13   224 Baden-Württemberg
Q367  ---- WELZHEIM (LUBW)       48.52    9.39   470 Baden-Württemberg
Q375  ---- WINTERBACH/REMSTAL    48.48    9.30   241 Baden-Württemberg
Q378  ---- SCHWB.-GMND/WEILER    48.46    9.53   413 Baden-Württemberg
Q382  ---- ELLWANGEN-RINDELBACH  48.59   10.08   460 Baden-Württemberg
Q395  ---- LAUCHHEIM (BERGHOF)   48.53   10.14   503 Baden-Württemberg
Q404  ---- RHEINAU-MEMPRECHTSH.  48.40    8.00   131 Baden-Württemberg
Q408  ---- KEHL-ODELSHOFEN       48.33    7.53   141 Baden-Württemberg
Q409  ---- BAIERSBRONN-RUHESTEI  48.34    8.13   916 Baden-Württemberg
Q410  ---- HORNISGRINDE          48.37    8.12  1119 Baden-Württemberg
Q411  ---- BADEN-BADEN-GEROLDSA  48.44    8.15   240 Baden-Württemberg
Q412  ---- IHRINGEN              48.03    7.38   193 Baden-Württemberg
Q414  ---- FORBACH (LUBW)        48.40    8.21   304 Baden-Württemberg
Q424  ---- ENZKLOESTERLE         48.40    8.28   600 Baden-Württemberg
Q437  ---- NEUBULACH-OBERHAUGST  48.39    8.41   570 Baden-Württemberg
Q440  ---- RENNG. IHINGER-HOF    48.45    8.56   478 Baden-Württemberg
Q461  ---- BALTMANNSWEILER-HOHE  48.45    9.27   457 Baden-Württemberg
Q481  ---- BLUMBERG-RANDEN       47.49    8.35   818 Baden-Württemberg
Q485  ---- HERMARINGEN-ALLEWIND  48.37   10.16   468 Baden-Württemberg
Q491  ---- NATTHEIM-FLEINHEIM    48.42   10.18   530 Baden-Württemberg
Q511  ---- DURBACH-EBERSWEIER    48.30    8.00   196 Baden-Württemberg
Q518  ---- OHLSBACH              48.26    8.00   176 Baden-Württemberg
Q522  ---- BAIERSBRONN-MITTELTA  48.31    8.19   596 Baden-Württemberg
Q529  ---- RIPPOLDSAU, BAD       48.25    8.20   493 Baden-Württemberg
Q541  ---- NAGOLD                48.34    8.43   380 Baden-Württemberg
Q554  ---- ROTTENBURG-KIEBINGEN  48.28    8.58   360 Baden-Württemberg
Q571  ---- URACH, BAD            48.30    9.24   471 Baden-Württemberg
Q574  ---- WESTERHEIM            48.31    9.37   823 Baden-Württemberg
Q579  ---- MERKLINGEN            48.31    9.46   685 Baden-Württemberg
Q622  ---- WOLFACH               48.18    8.14   291 Baden-Württemberg
Q625  ---- SCHILTACH (LUBW)      48.18    8.18   310 Baden-Württemberg
Q637  ---- OBERNDORF/NECKAR      48.17    8.35   516 Baden-Württemberg
Q642  ---- HAIGERLOCH-WEILDORF   48.22    8.46   524 Baden-Württemberg
Q651  ---- HECHINGEN             48.23    8.59   522 Baden-Württemberg
Q655  ---- BURLADINGEN-HAUSEN    48.18    9.04   682 Baden-Württemberg
Q663  ---- HOHENSTEIN-BERNLOCH   48.21    9.20   740 Baden-Württemberg
Q671  ---- MÜNSINGEN-APFELSTETT  48.23    9.29   750 Baden-Württemberg
Q672  ---- BIRENBACH             48.45    9.39   348 Baden-Württemberg
Q679  ---- EHINGEN-KIRCHEN       48.17    9.38   594 Baden-Württemberg
Q702  ---- EMMENDINGEN-MUNDING.  48.08    7.50   203 Baden-Württemberg
Q703  ---- WEISWEIL-WALDECKHOF   48.11    7.42   173 Baden-Württemberg
Q711  ---- WINDEN                48.08    8.01   303 Baden-Württemberg
Q712  ---- ELZACH-FISNACHT       48.12    8.07   440 Baden-Württemberg
Q713  ---- HERRENBERG            48.36    8.51   430 Baden-Württemberg
Q715  ---- HASLACH IM KINZIGTAL  48.17    8.05   220 Baden-Württemberg
Q716  ---- SIMONSWALD-OBERSIMON  48.05    8.06   419 Baden-Württemberg
Q731  ---- ESCHBRONN-MARIAZELL   48.11    8.28   714 Baden-Württemberg
Q733  ---- ROTTWEIL              48.11    8.38   588 Baden-Württemberg
Q738  ---- VILLINGEN-SCHWENNING  48.03    8.28   720 Baden-Württemberg
Q739  ---- NEUHAUSEN OB ECK-UNT  47.57    9.00   663 Baden-Württemberg
Q751  ---- ALBSTADT-BADKAP       48.13    8.59   759 Baden-Württemberg
Q755  ---- SCHWENNINGEN, KREIS   48.06    9.00   835 Baden-Württemberg
Q762  ---- LANGENENSLINGEN-ITTE  48.12    9.20   777 Baden-Württemberg
Q763  ---- MENGEN-ENNETACH       48.03    9.19   567 Baden-Württemberg
Q771  ---- RIEDLINGEN            48.09    9.28   533 Baden-Württemberg
Q786  ---- BIBERACH AN DER RISS  48.06    9.48   604 Baden-Württemberg
Q788  ---- SIGMARINGEN-LAIZ      48.04    9.12   580 Baden-Württemberg
Q790  ---- DEGGENHAUSERTAL-AZEN  47.48    9.25   708 Baden-Württemberg
Q811  ---- BUCHENBACH            47.58    8.00   445 Baden-Württemberg
Q813  ---- BREITNAU              47.56    8.05  1001 Baden-Württemberg
Q822  ---- EISENBACH             47.58    8.16   976 Baden-Württemberg
Q823  ---- LENZKIRCH-RUHBUEHL    47.52    8.14   852 Baden-Württemberg
Q864  ---- PFULLENDORF           47.56    9.17   630 Baden-Württemberg
Q870  ---- DONAUESCHINGEN (LAND  47.58    8.31   680 Baden-Württemberg
Q873  ---- ALTSHAUSEN            47.56    9.33   570 Baden-Württemberg
Q879  ---- WEINGARTEN BEI RAVEN  47.48    9.37   440 Baden-Württemberg
Q885  ---- WALDSEE, BAD-REUTE    47.55    9.42   576 Baden-Württemberg
Q887  ---- MUELLHEIM             47.48    7.38   273 Baden-Württemberg
Q891  ---- ROT AN DER ROT-BUCH   47.58   10.01   690 Baden-Württemberg
Q902  ---- MALSBURG-MARZELL      47.46    7.43   708 Baden-Württemberg
Q903  ---- KANDERN-GUPF          47.42    7.35   362 Baden-Württemberg
Q909  ---- RHEINFELDEN           47.34    7.47   282 Baden-Württemberg
Q911  ---- TODTMOOS              47.44    8.00   781 Baden-Württemberg
Q913  ---- DOGERN                47.36    8.10   309 Baden-Württemberg
Q922  ---- UEHLINGEN-BIRKENDORF  47.45    8.19   760 Baden-Württemberg
Q925  ---- WEILHEIM-BIERBRONNEN  47.41    8.12   771 Baden-Württemberg
Q926  ---- WUTOESCHINGEN-OFTER.  47.41    8.23   398 Baden-Württemberg
Q942  ---- SINGEN                47.46    8.49   445 Baden-Württemberg
Q945  ---- GAILINGEN             47.42    8.44   450 Baden-Württemberg
Q946  ---- GOTTMADINGEN          47.44    8.48   438 Schaffhausen
Q951  ---- SIPPLINGEN (SWN)      47.48    9.06   705 Baden-Württemberg
Q976  ---- FRIEDRICHSHAFEN       47.39    9.29   394 Baden-Württemberg
Q978  ---- FRIEDRICHSHFN UNTER.  47.41    9.27   459 Baden-Württemberg
Q999  ---- WANGEN/ALLGAEU-UNTER  47.43    9.52   666 Baden-Württemberg
Z001  ---- GRAMAIS/OESTERREICH   47.16   10.32  1320 Tirol
Z002  ---- HINTERHORNBACH/OESTE  47.22   10.27  1100 Tirol
Z003  ---- UNTERGSCHWEND/OESTER  47.30   10.30  1040 Tirol
Z004  ---- ACHENKIRCH/OESTERREI  47.30   11.42   902 Tirol
01368 ENFG FAGERNES              61.00    9.18   822 Innlandet
01475 ENSN SKIEN                 59.11    9.34    41 Vestfold og Telemark
02378 ESNY SODERHAMN             61.16   17.06    26 Gävleborgs län
02404 ESKV ARVIKA                59.40   12.35    77 Värmlands län
02435 ---- BORLANGE              60.26   15.30   145 Dalarnas län
02460 ESSA STOCKHOLM/ARLANDA     59.39   17.55    37 Stockholms län
02481 ---- SALA                  59.55   16.41    57 Västmanlands län
02512 ESGP GOETEBORG             57.47   11.53    20 Västra Götalands län
02527 ESGG GOTEBORG/LANDVETTER   57.40   12.30   164 Västra Götalands län
02542 ---- HALLUM                58.19   13.02    70 Västra Götalands län
02566 ---- MALILLA               57.24   15.49    95 Kalmar län
02584 ---- GOTSKA SANDON         58.24   19.12    12 
02586 ---- HARSTENA              58.15   17.01     5 
02595 ---- ROMA/GOTLAND          57.33   18.26    35 Gotlands län
02604 ESMT HALMSTAD              56.41   12.50    31 Hallands län
02620 ---- TORUP                 56.58   13.04    85 Hallands län
02623 ---- HORBY                 55.52   13.40   114 Skåne län
02625 ---- SKILLINGE             55.29   14.19     4 
02641 ESMX VAXJO                 56.56   14.44   182 Kronobergs län
02648 ---- VAEXJOE               56.51   14.50   199 Kronobergs län
02651 ESMK KRISTIANSTAD          55.55   14.05    23 Skåne län
02970 EFMA MARIEHAMN             60.07   19.54     5 Åländer Land
02975 EFHF HELSINKI              60.15   25.03    17 Uusimaa
03059 EGPE INVERNESS             57.32   -4.03     9 Schottland
03094 ---- ROSEHEARTY            57.42   -2.07     4 
03114 ---- OBAN                  56.25   -5.28     4 Schottland
03135 EGPK PRESTWICK             55.30   -4.36    20 Schottland
03140 EGPF GLASGOW               55.52   -4.26     8 Schottland
03154 ---- DUMFRIES              55.03   -3.39    16 England
03160 EGPH EDINBURGH             55.57   -3.21    41 Schottland
03235 ---- BOLTSHOPE PARK        54.49   -2.05   434 England
03245 EGNT NEWCASTLE/AIRPORT     55.02   -1.41    81 
03246 ---- NEWCASTLE             55.02   -1.41    80 
03262 ---- TYNEMOUTH             55.01   -1.25    30 
03318 EGNH BLACKPOOL             53.46   -3.02    10 England
03334 EGCC MANCHESTER            53.21   -2.16    78 England
03347 EGRY LEEDS/MET             53.48   -1.33    47 England
03453 EGXJ COTTESMORE            52.44   -0.39   138 England
03492 EGSH NORWICH-W.C.          52.38    1.18    14 England
03495 EGYC COLTISHALL            52.46    1.21    20 England
03496 ---- HEMSBY                52.41    1.41    13 England
03499 ---- SM.KNOLL              52.43    2.18     5 
03534 EGBB BIRMINGHAM/AIRPORT    52.27   -1.45    93 England
03683 EGSS STANSTED              51.53    0.14   106 England
03715 EGFF CARDIFF-WALES         51.24   -3.21    67 England
03726 EGRD BRISTOL/MET.          51.28   -2.36    11 England
03776 EGKK LONDON/GATWICK        51.09   -0.11    62 England
03779 EGRB LONDON WEATHER CENT.  51.31   -0.06    43 England
03817 EGDG ST. MAWGAN            50.26   -5.00   103 England
03839 ---- EXETER APT            50.44   -3.25    30 England
03865 EGHI SOUTHAMPTON           50.54   -1.24     9 England
03890 ---- OXFORD                51.45   -1.16    68 England
03908 EGQB BALLYKELLY            55.04   -7.01     2 Nordirland
03914 ---- PORTRUSH              55.12   -6.39     8 
03930 EGGP LIVERPOOL             53.20   -2.52    26 England
03957 ---- ROSSLARE              52.15   -6.20    23 
03958 EGBE COVENTRY              52.22   -1.29    82 England
03960 EIKL KILKENNY              52.40   -7.16    63 County Carlow
03961 ---- CARLOW OAK PARK       52.51   -6.55    61 
06062 EKSV SKIVE                 56.33    9.10    23 Region Midtjylland
06078 ---- ANHOLT                56.42   11.33     7 Region Midtjylland
06141 ---- ABED                  54.50   11.20     8 Region Sjælland
06147 ---- VINDEBAEK KYST        54.53   12.11     3 Region Sjælland
06160 EKVL VAERLOESE             55.46   12.20    18 Region Hovedstaden
06174 ---- TESSEBOELLE           55.24   12.09    21 Region Sjælland
06250 EHTS TERSCHELLING          53.22    5.13    26 Friesland
06630 LSZB BERN                  46.55    7.30   510 Bern
06690 LSZR ALTENRHEIN            47.29    9.34   398 Sankt Gallen
06710 LSGL LAUSANNE              46.33    6.37   616 Waadt
06775 LSZA LUGANO                46.00    8.54   279 Tessin
06787 ---- ANDEER                46.37    9.25   989 Graubünden
06788 ---- HINTERRHEIN           46.31    9.11  1611 Graubünden
06790 ---- ST.MORITZ             46.30    9.51  1850 Graubünden
07173 ---- EPINAL                48.12    6.26   317 Grand Est
07197 LFSC COLMAR                47.55    7.24   211 Grand Est
07593 ---- BRIANCON              44.55    6.39  1328 Provence-Alpes-Côte d'Azur
07680 LFTU ST.RAPHAEL            43.25    6.45     2 Provence-Alpes-Côte d'Azur
07695 ---- CAP FERRAT            43.41    7.20   138 Provence-Alpes-Côte d'Azur
08009 ---- RIBADEO               43.32   -7.01    25 Asturien
08013 ---- AVILES/DIV.PAST       43.33   -5.55    10 
08040 ---- FISTERRA              42.56   -9.17    98 Galicien
08183 LELL SABADELL              41.31    2.07   148 Katalonien
08227 LETO MADRID                40.29   -3.27   607 Kastilien-La Mancha
08307 ---- POLLENSA              39.54    3.06     2 
08370 ---- JAVEA/YUNTAMIEN       38.47   -0.10    15 Land Valencia
08390 LEZL SEVILLA               37.22   -6.00     8 Andalusien
08432 ---- AGUILAS               37.25   -1.35    33 
08485 ---- MOTRIL/CLUB NAUTICO   36.43   -3.32     3 
08536 LPPT LISSABON              38.47   -9.08   114 Distrikt Santarém
08538 ---- SAGRES                37.00   -8.57    25 
08547 ---- AVEIRO                40.39   -8.44     8 Distrikt Guarda
10018 EDXW WESTERLAND            54.55    8.21    22 Schleswig-Holstein
10026 ---- HUSUM                 54.31    9.09    28 Schleswig-Holstein
10034 ETME EGGEBEK               54.38    9.21    20 Schleswig-Holstein
10063 ---- PUTTGARDEN            54.30   11.13     1 Schleswig-Holstein
10125 EDWI WILHELMSHAVEN         53.30    8.03     5 Niedersachsen
10143 ---- NEUMUENSTER           54.05    9.56    20 Schleswig-Holstein
10177 ---- TETEROW               53.46   12.37    50 Mecklenburg-Vorpommern
10181 EDCP PAROW                 54.22   13.05     4 Mecklenburg-Vorpommern
10203 ---- EMDEN                 53.21    7.12     5 Niedersachsen
10210 ---- FRIESOYTHE-ALTENOYTH  53.04    7.54     6 Niedersachsen
10218 ETNA AHLHORN               52.53    8.14    49 Niedersachsen
10234 ETGQ ROTENBURG             53.08    9.21    34 Niedersachsen
10272 ETGW WITTSTOCK             53.11   12.31    72 Brandenburg
10273 EDCJ BASEPOHL              53.44   12.56    53 Mecklenburg-Vorpommern
10277 ---- NEUGLOBSOW            53.09   13.02    62 Brandenburg
10280 ---- NEUBRANDENBURG        53.33   13.12    81 Mecklenburg-Vorpommern
10312 ---- BELM                  52.19    8.10   103 Niedersachsen
10314 ETNP HOPSTEN               52.20    7.33    39 Nordrhein-Westfalen
10317 ---- OSNABRUECK            52.15    8.03    95 Niedersachsen
10324 ---- MINDEN                52.19    8.51    59 Nordrhein-Westfalen
10326 EDLI BIELEFELD             51.58    8.33   138 Nordrhein-Westfalen
10401 ETUR BRUEGGEN              51.12    6.08    73 Nordrhein-Westfalen
10403 EDLN MOENCHENGLADBACH      51.14    6.30    37 Nordrhein-Westfalen
10405 EDLV NIEDERRHEIN           51.36    6.09    32 Nordrhein-Westfalen
10406 ---- BOCHOLT               51.50    6.32    21 Nordrhein-Westfalen
10416 EDLW DORTMUND              51.31    7.37   127 Nordrhein-Westfalen
10426 EDLP PADERBORN             51.37    8.37   213 Nordrhein-Westfalen
10432 ---- KOETERBERG            51.51    9.19   492 Nordrhein-Westfalen
10441 ---- SCHAUENBURG-ELGERSH.  51.17    9.22   317 Hessen
10457 ---- COCHSTEDT             51.51   11.25   162 Sachsen-Anhalt
10487 ---- DRESDEN-STADT         51.03   13.44   113 Sachsen
10492 ETHT COTTBUS/FLUGPLATZ     51.46   14.17    68 Brandenburg
10493 JORG PRESCHEN              51.40   14.38   100 Brandenburg
10495 ---- HOYERSWERDA           51.27   14.15   116 Sachsen
10501 ---- AACHEN                50.47    6.06   202 Nordrhein-Westfalen
10505 ---- AACHEN-ORSBACH        50.48    6.02   231 Nordrhein-Westfalen
10510 ---- NUERBURG              50.20    6.57   627 Rheinland-Pfalz
10514 ETHM MENDIG                50.22    7.19   182 Rheinland-Pfalz
10515 ---- KOBLENZ-BEND.         50.25    7.35   127 Rheinland-Pfalz
10517 ---- BONN-FRIESDORF        50.42    7.09    64 Nordrhein-Westfalen
10520 ---- ANDERNACH             50.26    7.26    75 Rheinland-Pfalz
10521 ---- ROTHAARGEBIRGE        50.56    8.12   635 Nordrhein-Westfalen
10535 ---- WAHLEN                50.49    9.08   349 Hessen
10536 EDEX FULDA                 50.33    9.39   305 Hessen
10537 ---- NEU-ULRICHSTEIN       50.45    9.01   350 Hessen
10546 ---- KALTENNORDHEIM        50.38   10.09   487 Thüringen
10555 ---- WEIMAR                50.59   11.19   264 Thüringen
10558 ---- SONNEBERG             50.23   11.11   626 Thüringen
10575 ---- AUE                   50.36   12.43   391 Sachsen
10617 ETGX TRABEN-TRARBACH       49.58    7.07   257 Rheinland-Pfalz
10633 ETOU WIESBADEN             50.03    8.20   140 Hessen
10640 EDZW OFFENBACH             50.07    8.44    98 Hessen
10645 ---- BREITSOL              49.54    9.26   585 Bayern
10677 EDQD BAYREUTH              49.59   11.38   488 Bayern
10684 EDQM HOF/FLUGHAFEN         50.17   11.51   585 Bayern
10714 EDRZ ZWEIBRUECKEN          49.13    7.24   345 Rheinland-Pfalz
10722 EDSB KARLSR./BADEN-BADEN   48.47    8.05   124 Baden-Württemberg
10727 ---- KARLSRUHE             49.02    8.22   112 Baden-Württemberg
10731 ---- RHEINSTETTEN          48.58    8.19   118 Baden-Württemberg
10735 ---- SINSHEIM              49.15    8.53   169 Baden-Württemberg
10747 ---- KAISERSBACH-CRONHUET  48.55    9.41   489 Baden-Württemberg
10755 ETEB ANSBACH               49.19   10.38   467 Bayern
10828 ---- SIGMARINGEN           48.06    9.15   645 Baden-Württemberg
10840 ---- ULM-MAEHRINGEN        48.27    9.55   593 Baden-Württemberg
10858 ETSF FUERSTENFELDBRUCK     48.12   11.16   519 Bayern
10893 ---- PASSAU                48.35   13.28   409 Bayern
10935 EDNY FRIEDRICHSHAFEN       47.40    9.31   416 Baden-Württemberg
10947 ETSM MEMMINGEN             47.59   10.14   634 Bayern
11028 ---- ST. POELTEN           48.12   15.37   282 Niederösterreich
11132 LOIJ ST.JOHANN/TIROL       47.31   12.27   670 Tirol
11134 ---- GERLOS                47.13   12.02  1250 Tirol
11143 LOWZ ZELL A.SEE FL.        47.18   12.47   753 Salzburg
11145 ---- BAD GASTEIN           47.07   13.08  1100 Salzburg
11172 LOGM MARIAZELL             47.46   15.19   875 Steiermark
11176 LOGK KAPFENBERG            47.28   15.20   515 Steiermark
11210 ---- MALLNITZ              46.59   13.11  1185 Kärnten
11245 ---- GLEICHENBERG          46.52   15.54   303 Steiermark
11295 ---- LEIBNITZ              46.47   15.33   271 Steiermark
11322 ---- MAYRHOFEN             47.10   11.51   647 Tirol
11448 ---- PILSEN                49.39   13.16   364 Plzeňský kraj
12150 EPGD DANZIG                54.23   18.28   135 Woiwodschaft Pommern
12555 EPKT KATOWICE/PYRZOWICE    50.29   19.05   303 Woiwodschaft Schlesien
12839 LHBP BUDAPEST/FERIHEGY     47.26   19.16   151 Komitat Pest
12840 ---- BUDAPEST              47.31   19.02   118 Budapest
13473 ---- PEC                   42.40   20.18   498 
13477 ---- PRIZREN               42.13   20.44   402 
13481 LYPR PRISTINA              42.39   21.09   573 
14301 ---- POREC                 45.14   13.36    15 Gespanschaft Istrien
14536 ---- PRIJEDOR              44.59   16.45   135 Republika Srpska
14551 ---- DOBOJ                 44.44   18.06   146 Republika Srpska
14653 LQSA SARAJEWO              43.49   18.20   510 Föderation Bosnien und Herzegowina
14655 ---- GACKO                 43.10   18.33   940 Republika Srpska
14658 ---- SOKOLAC               43.57   18.49   872 Republika Srpska
15481 LRCK KOGALNICEANU          44.20   28.26    97 
15625 LBPD PLOVDIV               42.08   24.45   179 Oblast Plowdiw
16072 LIMO MONTE BISBINO         45.52    9.04  1319 Lombardei
16085 ---- PORTO TORRES          40.50    8.23     6 Sardinien
16094 LIPT VICENZA               45.34   11.31    39 Venetien
16122 LIMG ALBENGA               44.03    8.07    45 Ligurien
16136 LIQD PASSO PORRETTA        44.01   11.00  1313
16164 LIQV VOLTERRA              43.24   10.52   555 Toskana
16181 LIRZ PERUGIA               43.05   12.30   208 Umbrien
16216 LIRV VITERBO               42.26   12.03   300 Latium
16239 LIRA ROMA-CIAMPINO         41.47   12.35   130 Latium
16300 LIBZ POTENZA               40.38   15.48   843 Basilikata
16350 LIBC CROTONE               39.00   17.04   155 Kalabrien
16538 LIEN FONNI                 40.07    9.15  1022 Sardinien
16666 LGMK MYKONOS               37.26   25.21   123 Decentralized Administration of the Aegean
16689 ---- PATRAS                38.15   21.44     1 
16699 LGTG ANAGRA                38.19   23.32   148 Decentralized Administration of Thessaly and Central Greece
16740 LGSO SIROS                 37.25   24.57    72 Decentralized Administration of the Aegean
16744 LGSR SANTORINI             36.25   25.26    40 Decentralized Administration of the Aegean
17117 LTBR BURSA/YENISEHIR       40.15   29.33   232 Bursa
17255 ---- KAHRAMANMARES         37.35   36.55   572 Kahramanmaraş
17610 LCNC NICOSIA               35.09   33.17   224 
26058 ---- NARVA                 59.23   28.07    30 Kreis Ida-Viru
26231 ---- PARNU-SAUGA           58.25   24.28    12 Kreis Pärnu
26346 ---- ALUKSNE               57.26   27.02   197 Bezirk Alūksne
26416 ---- SALDUS                56.41   22.30   112 Bezirk Saldus
26424 ---- DOBELE                56.37   23.19    42 Bezirk Dobele
26429 ---- BAUSKA                56.25   24.11    30 Bezirk Bauska
26502 EYPA PALANGA               55.58   21.06    10 Bezirk Klaipėda
26529 EYPN PANEVEZYS             55.44   24.25    57 Bezirk Panevėžys
26603 ---- NIDA                  55.18   21.00     2 Bezirk Klaipėda
26630 EYKA KAUNAS                54.58   24.05    78 Bezirk Kaunas
26636 ---- SVECIONYS             55.08   26.10   222 Bezirk Vilnius
26714 ---- MARIJAMPOLE           54.31   23.21    80 Bezirk Marijampolė
26846 ---- STOLBTSY              53.28   26.44   172 Minskaja Woblasz
26851 UMMS MINSK 2               53.52   27.32   231 Minskaja Woblasz
27613 UUEE MOSCOW/SHEREMETYEVO   55.58   37.25   191 Oblast Moskau
33347 UKBB KIEW/BORISPOL         50.20   30.58   121 Oblast Kiew
33846 ---- NIKOLAYEV MATVEYEVKA  47.03   31.55    49 Oblast Mykolajiw
33983 ---- KERCH                 45.22   36.24    46 
34712 ---- MARIUPOL WEST AIRP.   47.02   37.30    68 
40155 LLHA HAIFA                 32.48   35.02     8 Haifa
40184 LLJR JERUSALEM             31.47   35.13   757 Bezirk Jerusalem
40341 ---- AQABA (PORT)          29.29   34.59     2 Gouvernement Aqaba
60250 GMAA AGADIR/INEZGANE       30.23   -9.34    27 Souss-Massa
60535 DAFI DJELFA                34.20    3.23  1180 El Djelfa
62450 ---- SUEZ                  29.52   32.28     3 Gouvernement As-Suwais
62456 HETB TABA/RAS              29.36   34.47   749 Schimal Sina'
69679 KQUA RAJLOVAC              43.52   18.18   489 Föderation Bosnien und Herzegowina
K1060 ---- AURICH                53.27    7.28     4 Niedersachsen
K1083 ---- BORKUM                53.34    6.45     5 
K1091 ---- DOERPEN               52.59    7.22     6 Niedersachsen
K1115 ---- GELSENKIRCHEN         51.30    7.06    44 Nordrhein-Westfalen
K1140 ---- LOENINGEN             52.45    7.45    36 Niedersachsen
K1161 ---- BOCHUM                51.29    7.16   101 Nordrhein-Westfalen
K1170 ---- SOLINGEN              51.09    7.05   209 Nordrhein-Westfalen
K1171 ---- LEVERKUSEN            51.01    6.59    44 Nordrhein-Westfalen
K1174 ---- HEINSBERG             51.03    6.06    57 Nordrhein-Westfalen
K1176 ---- KLEVE                 51.46    6.06    46 Nordrhein-Westfalen
K1188 ---- DUISBURG              51.28    6.44    21 Nordrhein-Westfalen
K1407 ---- WYK/FOEHR             54.42    8.34     1 Schleswig-Holstein
K1445 ---- HEIDE/HOLSTEIN        54.13    9.06    12 Schleswig-Holstein
K1481 ---- ELSFLETH              53.14    8.28     1 Niedersachsen
K1484 ---- GLUECKSTADT           53.48    9.26     2 Schleswig-Holstein
K1489 ---- BUCHHOLZ I.D. NORDH.  53.21    9.56    77 Niedersachsen
K1511 ---- CLOPPENBURG           52.51    8.04    42 Niedersachsen
K1514 ---- MELLE                 52.12    8.21    72 Niedersachsen
K1520 ---- RAHDEN-VARL           52.27    8.34    42 Nordrhein-Westfalen
K1524 ---- HERFORD               52.08    8.41    77 Nordrhein-Westfalen
K1546 ---- HILDESHEIM            52.11    9.57    85 Niedersachsen
K1547 ---- HAMELN                52.07    9.20    66 Niedersachsen
K1550 ---- HOLZMINDEN            51.49    9.28   128 Niedersachsen
K1579 ---- MELSUNGEN             51.08    9.33   190 Hessen
K1584 ---- AROLSEN               51.23    9.03   220 Hessen
K1585 ---- ARNSBERG              51.23    8.04   218 Nordrhein-Westfalen
K1586 ---- WILLINGEN/UPLAND      51.18    8.36   580 Hessen
K1596 ---- FRANKENBERG/EDER      51.03    8.49   290 Hessen
K1597 ---- LENNESTADT-ALTENHUND  51.07    8.05   300 Nordrhein-Westfalen
K1599 ---- BAD BERLEBURG         50.59    8.22   610 Nordrhein-Westfalen
K1705 ---- OSTENFELD             54.19    9.48    15 Schleswig-Holstein
K2107 ---- VOELKLINGEN           49.16    6.52   220 Saarland
K2204 ---- JUELICH               50.55    6.25    91 Nordrhein-Westfalen
K2221 ---- KOELN (BOTAN.GART.)   50.58    6.58    45 Nordrhein-Westfalen
K2226 ---- EUSKIRCHEN            50.39    6.47   176 Nordrhein-Westfalen
K2245 ---- BAD NEUENAHR-AHRWL.   50.32    7.05   111 Rheinland-Pfalz
K2247 ---- NEUWIED-WOLLENDORF    50.27    7.26   121 Rheinland-Pfalz
K2259 ---- MAYEN                 50.20    7.14   230 Rheinland-Pfalz
K2265 ---- MANDERSCHEID          50.06    6.48   403 Rheinland-Pfalz
K2269 ---- BAD BERTRICH          50.04    7.01   160 Rheinland-Pfalz
K2270 ---- DAUN                  50.12    6.50   430 Rheinland-Pfalz
K2274 ---- BAD KREUZNACH         49.51    7.52   102 Rheinland-Pfalz
K2286 ---- WOLFSTEIN/PFALZ       49.35    7.37   200 Rheinland-Pfalz
K2288 ---- KAISERSLAUTERN        49.27    7.47   248 Rheinland-Pfalz
K2290 ---- PIRMASENS             49.13    7.35   280 Rheinland-Pfalz
K2301 ---- OFFENBURG             48.28    7.57   155 Baden-Württemberg
K2309 ---- KEHL                  48.35    7.49   137 Baden-Württemberg
K2360 ---- SCHAUINSLAND          47.55    7.55  1205 Baden-Württemberg
K2507 ---- MICHELSTADT           49.41    9.00   204 Hessen
K2561 ---- FRANKFURT/PALMENGAR.  50.08    8.39   107 Hessen
K2588 ---- BAD SCHWALBACH        50.08    8.04   320 Hessen
K2596 ---- DARMSTADT             49.53    8.41   162 Hessen
K2601 ---- SIEGEN                50.52    8.01   263 Nordrhein-Westfalen
K2611 ---- MARBURG               50.49    8.47   195 Hessen
K2613 ---- MAINZ                 49.59    8.16   125 Rheinland-Pfalz
K2614 ---- ALZEY                 49.45    8.07   166 Rheinland-Pfalz
K2630 ---- SCHLUECHTERN          50.21    9.31   212 Hessen
K2635 ---- WORMS                 49.38    8.23    91 Rheinland-Pfalz
K2637 ---- GELNHAUSEN            50.12    9.11   155 Hessen
K2644 ---- WALDEMS               50.16    8.21   400 Hessen
K2646 ---- LIMBURG               50.25    8.04   185 Hessen
K2649 ---- KOENIGSTEIN/TS.       50.11    8.29   388 Hessen
K2667 ---- BEERFELDEN            49.34    8.58   450 Hessen
K2671 ---- LOHR                  50.01    9.37   161 Bayern
K2679 ---- BAD MERGENTHEIM       49.29    9.46   250 Baden-Württemberg
K2688 ---- BAD BERGZABERN        49.07    8.00   252 Rheinland-Pfalz
K2689 ---- HEILBRONN             49.09    9.14   167 Baden-Württemberg
K2693 ---- HEIDELBERG            49.25    8.40   110 Baden-Württemberg
K2696 ---- PHILIPPSBURG (KKW)    49.15    8.27   100 Baden-Württemberg
K2701 ---- BADEN BADEN           48.46    8.15   218 Baden-Württemberg
K2706 ---- BAD HERRENALB         48.48    8.27   351 Baden-Württemberg
K2711 ---- PFORZHEIM             48.54    8.44   245 Baden-Württemberg
K2714 ---- LUDWIGSBURG           48.54    9.12   287 Baden-Württemberg
K2718 ---- KIRCHHEIM/TECK        48.40    9.25   289 Baden-Württemberg
K2719 ---- WELZHEIM              48.53    9.38   510 Baden-Württemberg
K2721 ---- MURRHARDT             48.58    9.34   344 Baden-Württemberg
K2724 ---- SCHWAEBISCH HALL      49.07    9.45   387 Baden-Württemberg
K2727 ---- SCHWAEB.GMUEND        48.47    9.48   415 Baden-Württemberg
K2729 ---- MERKLINGEN            48.30    9.42   747 Baden-Württemberg
K2735 ---- SCHONACH              48.08    8.12   904 Baden-Württemberg
K2736 ---- WOLFACH               48.18    8.14   265 Baden-Württemberg
K2739 ---- VILLINGEN SCHWENN.    48.03    8.28   720 Baden-Württemberg
K2753 ---- MUENSINGEN-APPELST.   48.23    9.29   750 Baden-Württemberg
K2757 ---- ROTTWEIL              48.11    8.38   588 Baden-Württemberg
K2760 ---- SIGMARINGEN           48.04    9.12   580 Baden-Württemberg
K2761 ---- BONNDORF              47.49    8.21   876 Baden-Württemberg
K2765 ---- BIBERACH              48.07    9.48   534 Baden-Württemberg
K2767 ---- TITISEE-NEUSTADT      47.54    8.10   860 Baden-Württemberg
K2778 ---- WALDSHUT              47.37    8.14   330 Baden-Württemberg
K2780 ---- DONAUESCHINGEN        47.57    8.30   677 Baden-Württemberg
K2786 ---- PFULLENDORF-BRUNNHS.  47.55    9.17   638 Baden-Württemberg
K2787 ---- UEBERLINGEN/BODENSEE  47.46    9.10   440 Baden-Württemberg
K2791 ---- RAVENSBURG            47.48    9.37   440 Baden-Württemberg
K2796 ---- LINDENBERG/ALLGAEU    47.36    9.53   760 Bayern
K2798 ---- STOCKACH              47.51    9.02   475 Baden-Württemberg
K2832 ---- TAUBERBISCHOFSHEIM    49.37    9.41   179 Baden-Württemberg
K2868 ---- REUTLINGEN-BETZING.   48.30    9.11   360 Baden-Württemberg
K2890 ---- RASTATT               48.52    8.11   116 Baden-Württemberg
K2913 ---- BOEBLINGEN            48.41    8.58   445 Baden-Württemberg
K2920 ---- HERRENBERG            48.36    8.53   431 Baden-Württemberg
K2923 ---- ROTTENBURG            48.29    8.57   342 Baden-Württemberg
K2932 ---- TUTTLINGEN            48.01    8.49   648 Baden-Württemberg
K3018 ---- ZINNOWITZ             54.05   13.54     2 Mecklenburg-Vorpommern
K3182 ---- BERNBURG/SAALE        51.50   11.43    81 Sachsen-Anhalt
K3187 ---- QUEDLINBURG           51.47   11.09   123 Sachsen-Anhalt
K3362 ---- BITTERFELD            51.38   12.19    80 Sachsen-Anhalt
K3382 ---- BAUTZEN               51.10   14.28   207 Sachsen
K3384 ---- MEISSEN               51.09   13.27   225 Sachsen
K3404 ---- SONDERSHAUSEN         51.22   10.54   201 Thüringen
K3406 ---- BAD FRANKENHAUSEN/KY  51.21   11.06   130 Thüringen
K3414 ---- RASTENBERG            51.11   11.25   200 Thüringen
K3822 ---- EUTIN                 54.08   10.35    50 Schleswig-Holstein
K3854 ---- BAD SEGEBERG          53.56   10.18    49 Schleswig-Holstein
K3869 ---- GRAMBECK              53.34   10.41    27 Schleswig-Holstein
K3883 ---- UELZEN                52.58   10.33    49 Niedersachsen
K3891 ---- LUENEBURG             53.16   10.26    11 Niedersachsen
K3910 ---- WOLFSBURG             52.27   10.46    56 Niedersachsen
K3924 ---- SALZGITTER            52.02   10.19   130 Niedersachsen
K3973 ---- BAD LAUTERBERG        51.38   10.29   300 Niedersachsen
K3982 ---- CLAUSTHAL-ZELLERFLD.  51.48   10.20   590 Niedersachsen
K3997 ---- ESCHWEGE              51.11   10.04   170 Hessen
K4036 ---- KRONACH               50.14   11.20   305 Bayern
K4042 ---- KULMBACH              50.06   11.27   330 Bayern
K4054 ---- SCHWEINFURT           50.04   10.13   240 Bayern
K4057 ---- KITZINGEN             49.44   10.12   230 Bayern
K4058 ---- EBRACH                49.51   10.29   360 Bayern
K4069 ---- GUNZENHSN.            49.08   10.45   413 Bayern
K4071 ---- SCHWABACH             49.20   11.01   343 Bayern
K4086 ---- FUERTH/BAYERN         49.29   10.58   313 Bayern
K4087 ---- ERLANGEN              49.37   11.00   270 Bayern
K4091 ---- UFFENHEIM             49.32   10.14   340 Bayern
K4093 ---- ROTHENBURG ODT.       49.23   10.11   406 Bayern
K4100 ---- ELLWANGEN/JAGST       48.58   10.08   443 Baden-Württemberg
K4102 ---- HEIDENHEIM            48.40   10.08   500 Baden-Württemberg
K4105 ---- NOERDLINGEN           48.51   10.30   425 Bayern
K4108 ---- EICHSTAETT            48.54   11.10   397 Bayern
K4116 ---- ALTOMUENSTER          48.23   11.15   502 Bayern
K4130 ---- KRUMBACH-EDENHAUSEN   48.15   10.25   520 Bayern
K4138 ---- ISNY                  47.41   10.03   712 Bayern
K4140 ---- OBERSTAUFEN           47.34   10.02   800 Bayern
K4149 ---- KAUFBEUREN            47.53   10.36   720 Bayern
K4157 ---- MITTENWALD            47.27   11.16   920 Bayern
K4169 ---- BAD TOELZ             47.47   11.33   640 Bayern
K4171 ---- EBERSBERG             48.05   11.57   570 Bayern
K4172 ---- HOLZKIRCHEN/OBB.      47.53   11.42   685 Bayern
K4179 ---- KREUTH                47.39   11.45   793 Bayern
K4181 ---- SCHLIERSEE            47.44   11.51   780 Bayern
K4185 ---- MAINBURG              48.39   11.48   413 Bayern
K4204 ---- JENA/STERNWARTE       50.56   11.35   155 Thüringen
K4244 ---- LOBENSTEIN            50.27   11.38   500 Thüringen
K4402 ---- FREIBERG              50.56   13.20   380 Sachsen
K4408 ---- BAD GOTTLEUBA         50.51   13.56   380 Sachsen
K4420 ---- GREIZ-DOELAU          50.37   12.10   270 Sachsen
K4473 ---- SELB                  50.10   12.08   535 Bayern
K4476 ---- TIRSCHENREUTH         49.53   12.21   515 Bayern
K4484 ---- OBERVIECHTACH         49.27   12.25   498 Bayern
K4488 ---- CHAM                  49.13   12.40   396 Bayern
K4501 ---- MALLERSDORF/NDB.      48.47   12.15   410 Bayern
K4503 ---- LANDSHUT              48.32   12.08   391 Bayern
K4514 ---- FREYUNG               48.48   13.33   645 Bayern
K4529 ---- WASSERBURG/INN        48.03   12.13   443 Bayern
K4531 ---- TROSTBERG             48.01   12.33   487 Bayern
K4533 ---- TRAUNSTEIN            47.52   12.39   596 Bayern
K4535 ---- BAD REICHENHALL       47.45   12.54   455 Bayern
K4536 ---- BERCHTESG.            47.38   13.01   550 Bayern
K4540 ---- REIT IM WINKL         47.40   12.29   675 Bayern
K4546 ---- BAYRISCHZELL          47.41   12.01   805 Bayern
K4570 ---- BROTJACKLRIEGEL       48.49   13.13  1016 Bayern
K9097 ---- DETMOLD               51.57    8.54   194 Nordrhein-Westfalen
N0101 ---- BALDERSCHWANG         47.28   10.06  1050 Bayern
N0113 ---- LINDAU                47.33    9.44   400 Bayern
N0121 ---- MONSCHAU              50.32    6.15   542 Nordrhein-Westfalen
N0122 ---- WANGEN/ALLGAEU        47.41    9.52   588 Baden-Württemberg
N0136 ---- BAD SCHUSSENRIED      48.00    9.40   576 Baden-Württemberg
N0139 ---- BAD WALDSEE           47.55    9.45   620 Baden-Württemberg
N0149 ---- MARKTREDW.            50.00   12.07   508 Bayern
N0151 ---- SCHLEIDEN-SCHOENES.   50.31    6.24   572 Nordrhein-Westfalen
N0153 ---- WARENDORF             51.57    8.01    53 Nordrhein-Westfalen
N0157 ---- RIEDLINGEN            48.09    9.28   538 Baden-Württemberg
N0159 ---- SAULGAU-BOLSTERN      47.59    9.28   640 Baden-Württemberg
N0171 ---- EHINGEN/DONAU         48.17    9.43   520 Baden-Württemberg
N0197 ---- GOTTMADINGEN          47.44    8.47   430 Baden-Württemberg
N0214 ---- BLUMBERG              47.51    8.32   707 Baden-Württemberg
N0224 ---- AHLEN                 51.47    7.52    70 Nordrhein-Westfalen
N0226 ---- DUEREN                50.48    6.29   127 Nordrhein-Westfalen
N0242 ---- HINDELANG/OSTRACHTAL  47.27   10.26   930 Bayern
N0253 ---- IMMENSTADT            47.33   10.13   731 Bayern
N0258 ---- ZELL I.WIES.-PFAFFB.  47.44    7.52   730 Baden-Württemberg
N0267 ---- LOERRACH              47.38    7.39   309 Baden-Württemberg
N0273 ---- LEUTKIRCH             47.50   10.01   655 Baden-Württemberg
N0283 ---- HEITERSHEIM           47.53    7.39   231 Baden-Württemberg
N0291 ---- BREISACH              48.02    7.35   192 Baden-Württemberg
N0304 ---- ERKELENZ              51.05    6.19    99 Nordrhein-Westfalen
N0311 ---- GUTACH/BR.            48.07    8.01   302 Baden-Württemberg
N0332 ---- MINDELHEIM            48.03   10.31   607 Bayern
N0352 ---- GERSTETTEN-DETTINGEN  48.36   10.07   582 Baden-Württemberg
N0359 ---- DISCHINGEN(EGAUWAS.)  48.41   10.22   460 Baden-Württemberg
N0406 ---- DINKELSBUEHL          49.04   10.20   444 Bayern
N0411 ---- SCHRAMBERG            48.13    8.23   502 Baden-Württemberg
N0429 ---- VIERSEN               51.15    6.22    60 Nordrhein-Westfalen
N0432 ---- BOPFINGEN             48.51   10.21   497 Baden-Württemberg
N0445 ---- DONAUWOERTH           48.43   10.47   405 Bayern
N0447 ---- STRAELEN              51.27    6.16    45 Nordrhein-Westfalen
N0462 ---- VECHTA                52.45    8.18    41 Niedersachsen
N0469 ---- OBERKIRCH             48.31    8.05   190 Baden-Württemberg
N0474 ---- WERTINGEN             48.34   10.41   430 Bayern
N0477 ---- ACHERN                48.38    8.03   138 Baden-Württemberg
N0505 ---- FUESSEN-WEISSENSEE    47.35   10.38   790 Bayern
N0514 ---- ANKUM                 52.33    7.53    62 Niedersachsen
N0527 ---- FORBACH-HERRENWIES    48.40    8.16   764 Baden-Württemberg
N0546 ---- HASELUENNE            52.40    7.29    17 Niedersachsen
N0548 ---- SONTRA                51.04    9.56   365 Hessen
N0554 ---- RINGGAU-RENDA         51.04   10.05   395 Hessen
N0586 ---- SCHWABMUENCHEN        48.11   10.46   555 Bayern
N0602 ---- MEPPEN                52.42    7.18    14 Niedersachsen
N0635 ---- WITZENHAUSEN-ZIEGH.   51.22    9.45   240 Hessen
N0645 ---- POETTMES-SCHORN       48.35   11.06   404 Bayern
N0674 ---- ABENSBERG-SANDHARL.   48.50   11.49   380 Bayern
N0677 ---- LANDAU/PFALZ          49.12    8.06   150 Rheinland-Pfalz
N0680 ---- GERMERSHEIM           49.13    8.23   106 Rheinland-Pfalz
N0717 ---- FRIESOYTHE            53.01    7.52     8 Niedersachsen
N0738 ---- UPLENGEN-STAPELERM.   53.21    7.51    14 Niedersachsen
N0751 ---- THALMAESSING          49.05   11.14   417 Bayern
N0753 ---- GREDING               49.03   11.22   425 Bayern
N0755 ---- SPEYER                49.21    8.25    99 Rheinland-Pfalz
N0761 ---- KRAICHTAL-GOCHSHEIM   49.06    8.45   170 Baden-Württemberg
N0763 ---- BEILNGRIES            49.02   11.28   370 Bayern
N0765 ---- LEER                  53.13    7.29     4 Niedersachsen
N0775 ---- RIEDENBURG            48.57   11.43   363 Bayern
N0778 ---- NEUSTADT/DONAU        48.52   11.46   360 Bayern
N0781 ---- KELHEIM               48.55   11.53   354 Bayern
N1012 ---- KALBACH               50.25    9.40   405 Hessen
N1026 ---- LOSSBURG              48.23    8.29   601 Baden-Württemberg
N1027 ---- GREBENHAIN            50.29    9.20   435 Hessen
N1033 ---- HORB                  48.27    8.41   389 Baden-Württemberg
N1038 ---- ALBSTADT-BURGFELDEN   48.14    8.56   911 Baden-Württemberg
N1040 ---- HEMMOOR               53.42    9.09     5 Niedersachsen
N1043 ---- BALINGEN              48.17    8.53   571 Baden-Württemberg
N1054 ---- HAIGERLOCH-HART       48.23    8.51   483 Baden-Württemberg
N1075 ---- TUEBINGEN             48.32    9.02   445 Baden-Württemberg
N1101 ---- BAERNAU               49.49   12.26   610 Bayern
N1107 ---- NEUFFEN               48.33    9.24   480 Baden-Württemberg
N1120 ---- ZITTAU                50.54   14.49   235 Sachsen
N1122 ---- NEUSTADT/WN-ALTENST.  49.43   12.10   400 Bayern
N1140 ---- GEISLINGEN            48.38    9.51   443 Baden-Württemberg
N1147 ---- GOEPPINGEN            48.43    9.37   361 Baden-Württemberg
N1150 ---- ROTENBURG/FULDA       50.59    9.44   200 Hessen
N1151 ---- KEMNATH               49.52   11.54   464 Bayern
N1156 ---- GUBEN                 51.56   14.42    46 Brandenburg
N1171 ---- SPANGENBERG           51.07    9.40   260 Hessen
N1201 ---- WALDMUENCHEN          49.23   12.43   510 Bayern
N1215 ---- WINTERBACH            48.48    9.29   280 Baden-Württemberg
N1245 ---- BACKNANG              48.57    9.26   291 Baden-Württemberg
N1265 ---- HOHENFELS             49.12   11.51   423 Bayern
N1319 ---- ALTENSTEIG-WART       48.37    8.39   586 Baden-Württemberg
N1323 ---- FRANKFURT/ODER        52.22   14.32    49 Brandenburg
N1325 ---- REGEN                 48.58   13.08   572 Bayern
N1333 ---- BISCHOFSMAIS          48.55   13.05   684 Bayern
N1336 ---- BAD LIEBENZELL        48.46    8.44   319 Baden-Württemberg
N1345 ---- VIECHTACH             49.05   12.54   455 Bayern
N1353 ---- LAM                   49.12   13.05   620 Bayern
N1354 ---- RENNINGEN             48.46    8.57   405 Baden-Württemberg
N1371 ---- FURTH IM WALD         49.18   12.50   392 Bayern
N1382 ---- FALKENSTEIN KR.CHAM   49.06   12.29   562 Bayern
N1401 ---- BOENNIGHEIM           49.02    9.05   228 Baden-Württemberg
N1429 ---- NEUKIRCHEN-SEIGHS.    50.55    9.21   380 Hessen
N1441 ---- SCHWALMSTADT          50.54    9.13   225 Hessen
N1461 ---- SANKT ENGLMAR         49.00   12.50   810 Bayern
N1475 ---- DEGGENDORF            48.50   12.57   313 Bayern
N1503 ---- AALEN                 48.51   10.06   418 Baden-Württemberg
N1528 ---- WUESTENROT            49.05    9.28   485 Baden-Württemberg
N1542 ---- EBERSWALDE            52.50   13.48    45 Brandenburg
N1551 ---- KUENZELSAU-MORSBACH   49.17    9.44   241 Baden-Württemberg
N1613 ---- CRAILSHEIM            49.08   10.05   417 Baden-Württemberg
N1622 ---- BLAUFELDEN            49.18    9.58   450 Baden-Württemberg
N1648 ---- MOECKMUEHL            49.18    9.21   176 Baden-Württemberg
N1712 ---- MOSBACH-DIEDESHEIM    49.21    9.06   140 Baden-Württemberg
N2028 ---- FRIEDEBURG-HORSTEN    53.27    7.56     3 Niedersachsen
N2032 ---- USLAR                 51.40    9.38   190 Niedersachsen
N2046 ---- MURNAU                47.40   11.14   622 Bayern
N2048 ---- KOCHEL                47.40   11.22   600 Bayern
N2076 ---- SAUERLACH             47.59   11.39   615 Bayern
N2103 ---- OBERAMMERGAU          47.36   11.05   873 Bayern
N2117 ---- WEILHEIM              47.51   11.09   568 Bayern
N2132 ---- GRUENSTADT            49.34    8.10   200 Rheinland-Pfalz
N2142 ---- DACHAU                48.15   11.27   483 Bayern
N2147 ---- STARNBERG             48.00   11.21   596 Bayern
N2159 ---- KIRCHHEIMBOLANDEN     49.40    8.01   230 Rheinland-Pfalz
N2171 ---- WOLFHAGEN             51.18    9.09   310 Hessen
N2173 ---- PASEWALK              53.30   14.00    10 Mecklenburg-Vorpommern
N2193 ---- LANDAU/ISAR           48.41   12.42   338 Bayern
N2202 ---- LALLING               48.50   13.06   353 Bayern
N2204 ---- HEPPENHEIM            49.39    8.38   101 Hessen
N2216 ---- BIBLIS                49.41    8.25    88 Hessen
N2219 ---- SEEHEIM-JUGENHEIM     49.45    8.38   132 Hessen
N2221 ---- GEISENHAUSEN          48.29   12.16   467 Bayern
N2222 ---- LAUTERTAL/ODW.        49.43    8.41   198 Hessen
N2228 ---- FRIEDLAND             53.41   13.34    14 Mecklenburg-Vorpommern
N2235 ---- HOFGEISMAR            51.30    9.23   162 Hessen
N2249 ---- OPPENHEIM             49.51    8.22    85 Rheinland-Pfalz
N2253 ---- EGING AM SEE          48.41   13.15   400 Bayern
N2254 ---- RUESSELSHEIM          49.59    8.27    87 Hessen
N2271 ---- SCHOENBERG/NDB.       48.50   13.20   550 Bayern
N2274 ---- SANKT OSWALD          48.53   13.25   754 Bayern
N2284 ---- MAUTH                 48.53   13.35   810 Bayern
N2311 ---- WILLEBADESSEN-BORL.   51.35    9.02   280 Nordrhein-Westfalen
N2336 ---- HOEXTER               51.47    9.24    93 Nordrhein-Westfalen
N2361 ---- OTTENSTEIN            51.57    9.25   270 Niedersachsen
N2362 ---- GRIMMEN               54.07   13.04    15 Mecklenburg-Vorpommern
N2372 ---- DEMMIN                53.55   13.03    17 Mecklenburg-Vorpommern
N2375 ---- EMMERTHAL-GROHNDE     52.01    9.25    80 Niedersachsen
N2386 ---- ANKLAM                53.51   13.41    12 Mecklenburg-Vorpommern
N2388 ---- DORFEN KR.ERDING      48.16   12.10   439 Bayern
N2395 ---- WOLGAST               54.03   13.47     8 Mecklenburg-Vorpommern
N2402 ---- NIEHEIM               51.48    9.07   230 Nordrhein-Westfalen
N2412 ---- WUSTERHUSEN           54.07   13.37    31 Mecklenburg-Vorpommern
N2431 ---- ASCHAU                47.46   12.20   620 Bayern
N2433 ---- BAD MUENDER           52.11    9.28   110 Niedersachsen
N2443 ---- RUHPOLDING-SEEHAUS    47.43   12.37   753 Bayern
N2446 ---- SASSNITZ-STAPHEL      54.29   13.34     4 Mecklenburg-Vorpommern
N2457 ---- BERGEN/RUEGEN         54.25   13.26    75 Mecklenburg-Vorpommern
N2475 ---- STRALSUND             54.18   13.04    13 Mecklenburg-Vorpommern
N2571 ---- TEISENDORF            47.51   12.49   500 Bayern
N2575 ---- BAD SUELZE            54.07   12.40     5 Mecklenburg-Vorpommern
N2583 ---- BURGHAUSEN            48.11   12.51   413 Bayern
N2603 ---- BODENKIRCHEN-AICH     48.26   12.24   464 Bayern
N2611 ---- EGGENFELDEN           48.24   12.47   400 Bayern
N2614 ---- PFARRKIRCHEN          48.26   12.56   410 Bayern
N2622 ---- PREROW A. DARSS       54.27   12.34     1 Mecklenburg-Vorpommern
N2626 ---- GRAAL-MUERITZ         54.15   12.16     6 Mecklenburg-Vorpommern
N2632 ---- POCKING               48.25   13.19   321 Bayern
N2704 ---- WALDKIRCHEN           48.43   13.36   625 Bayern
N2781 ---- BUETZOW-WOLKEN        53.51   12.01    10 Mecklenburg-Vorpommern
N2813 ---- BAD DOBERAN           54.07   11.54    15 Mecklenburg-Vorpommern
N2822 ---- RERIK                 54.07   11.37    18 
N2839 ---- WISMAR                53.53   11.26    26 Mecklenburg-Vorpommern
N3001 ---- SCHOEPPINGEN          52.06    7.15   100 Nordrhein-Westfalen
N3002 ---- MUENCHBERG            50.12   11.48   545 Bayern
N3003 ---- GEFREES               50.05   11.43   475 Bayern
N3007 ---- SCHWARZENBACH/SAALE   50.12   11.55   532 Bayern
N3029 ---- OERLINGHAUSEN         51.58    8.39   180 Nordrhein-Westfalen
N3035 ---- NAILA                 50.20   11.42   525 Bayern
N3041 ---- LICHTENFELS/OFR.      50.06   11.10   375 Bayern
N3047 ---- GEROLDSGRUEN-STEINB.  50.21   11.35   646 Bayern
N3049 ---- EMLICHHEIM            52.37    6.51    14 Niedersachsen
N3052 ---- PRESSECK              50.14   11.33   620 Bayern
N3053 ---- STEINBACH AM WALD     50.27   11.23   616 Bayern
N3060 ---- BAD BENTHEIM          52.18    7.10    45 Niedersachsen
N3102 ---- AHAUS                 52.04    7.01    52 Nordrhein-Westfalen
N3114 ---- COESFELD              51.57    7.11    84 Nordrhein-Westfalen
N3149 ---- EBERN-EYRICHSHOF      50.07   10.47   285 Bayern
N3206 ---- SULINGEN              52.41    8.49    48 Niedersachsen
N3233 ---- NEUMARKT OPF.         49.17   11.26   426 Bayern
N3240 ---- HOYA                  52.49    9.09    18 Niedersachsen
N3254 ---- OTTENDORF-OKRILLA     51.11   13.50   180 Sachsen
N3257 ---- PIRNA                 50.57   13.56   123 Sachsen
N3264 ---- BISCHOFSWERDA         51.08   14.11   300 Sachsen
N3265 ---- AUERBACH/OPF.         49.42   11.38   418 Bayern
N3303 ---- HERSBRUCK             49.30   11.24   332 Bayern
N3309 ---- LAUF/HEUCHLING        49.31   11.18   333 Bayern
N3312 ---- ALTDORF/OFR.          49.23   11.22   428 Bayern
N3334 ---- GRAEFENBERG           49.39   11.15   477 Bayern
N3360 ---- STADELHOFEN           50.00   11.12   476 Bayern
N3420 ---- FORCHHEIM/OFR.        49.43   11.03   257 Bayern
N3432 ---- NEUSTADT/AISCH-UNTN.  49.35   10.31   320 Bayern
N3462 ---- RIESA                 51.18   13.15   140 Sachsen
N3504 ---- HASSFURT              50.02   10.31   239 Bayern
N3533 ---- TORGAU                51.35   13.00    80 Sachsen
N3608 ---- KAMENZ                51.17   14.07   157 Sachsen
N3619 ---- HOYERSWERDA           51.26   14.15   135 Sachsen
N3666 ---- ELSTERWERDA           51.28   13.32    91 Brandenburg
N3685 ---- GRAEFENTONNA          51.04   10.44   207 Thüringen
N3727 ---- OBERWEISSENBRUNN      50.25    9.57   630 Bayern
N3729 ---- BISCHOFSHEIM/RHOEN    50.24   10.00   465 Bayern
N3754 ---- HAMMELBURG            50.07    9.54   184 Bayern
N3778 ---- BURGSINN              50.09    9.39   235 Bayern
N3833 ---- WEIBERSBRUNN          49.54    9.24   470 Bayern
N3924 ---- WEIKERSHEIM           49.28    9.57   370 Baden-Württemberg
N3951 ---- WERTHEIM-EICHEL       49.46    9.33   140 Bayern
N4002 ---- MUDAU-SCHLOSSAU       49.33    9.09   470 Baden-Württemberg
N4005 ---- AMORBACH              49.39    9.14   183 Bayern
N4032 ---- LUETZELBACH           49.46    9.05   274 Hessen
N4045 ---- ASCHAFFENBURG         49.59    9.07   110 Bayern
N4068 ---- GIFHORN               52.29   10.33    51 Niedersachsen
N4070 ---- DIEBURG               49.54    8.51   145 Hessen
N4116 ---- HANAU                 50.06    8.57   102 Hessen
N4123 ---- EIBENSTOCK(TALSP.)    50.32   12.36   546 Sachsen
N4161 ---- GOSLAR                51.55   10.26   266 Niedersachsen
N4162 ---- ZWICKAU               50.41   12.28   347 Sachsen
N4176 ---- ROTTACH-EGERN         47.41   11.46   747 Bayern
N4191 ---- ZWOENITZ              50.39   12.49   500 Sachsen
N4241 ---- NEU ANSPACH           50.18    8.30   375 Hessen
N4242 ---- WOLFENBUETTEL         52.10   10.31    88 Niedersachsen
N4248 ---- ROCHLITZ              51.03   12.49   185 Sachsen
N4253 ---- FRIEDBERG             50.20    8.45   158 Hessen
N4277 ---- LEHRE                 52.20   10.40    90 Niedersachsen
N4333 ---- BAD HOMBURG           50.15    8.34   255 Hessen
N4359 ---- LEHRTE                52.23    9.59    60 Niedersachsen
N4365 ---- ADELHEIDSDORF         52.33   10.03    41 Niedersachsen
N4377 ---- ANNABERG_BUCHHOLZ     50.35   13.00   630 Sachsen
N4414 ---- HALBERSTADT           51.54   11.03   110 Sachsen-Anhalt
N4426 ---- DOERNTHAL             50.44   13.20   558 Sachsen
N4464 ---- BRAUNSDORF            50.53   13.01   300 Sachsen
N4513 ---- GRIMMA                51.14   12.43   150 Sachsen
N4535 ---- BAD DUEBEN            51.36   12.35    89 Sachsen
N4561 ---- HERZBERG              51.40   10.21   230 Niedersachsen
N4601 ---- OSTERODE/HARZ         51.43   10.16   285 Niedersachsen
N4623 ---- NORTHEIM              51.43    9.59   121 Niedersachsen
N4639 ---- DESSAU                51.51   12.15    60 Sachsen-Anhalt
N4655 ---- BAD GANDERSHEIM       51.52   10.02   154 Niedersachsen
N4838 ---- ADENSTEDT             52.00    9.56   194 Niedersachsen
N4854 ---- SCHOENINGEN           52.08   10.57   170 Niedersachsen
N5015 ---- BARSINGHAUSEN         52.18    9.28   114 Niedersachsen
N5044 ---- INGELHEIM             49.59    8.04   135 Rheinland-Pfalz
N5056 ---- RUEDESHEIM            49.59    7.56   126 Hessen
N5111 ---- FREISEN/SAAR          49.33    7.15   465 Saarland
N5146 ---- SOHREN                49.56    7.18   430 Rheinland-Pfalz
N5149 ---- RHAUNEN               49.52    7.20   370 Rheinland-Pfalz
N5184 ---- SAALFELD              50.39   11.23   235 Thüringen
N5227 ---- KUSEL                 49.32    7.24   235 Rheinland-Pfalz
N5245 ---- LAUTERECKEN           49.39    7.36   158 Rheinland-Pfalz
N5250 ---- RUDOLSTADT            50.44   11.22   193 Thüringen
N5344 ---- STROMBERG/HUNSRUECK   49.57    7.47   300 Rheinland-Pfalz
N5346 ---- ILMENAU               50.41   10.54   498 Thüringen
N5374 ---- BINGEN-BUEDESHEIM     49.57    7.54    82 Rheinland-Pfalz
N5417 ---- NAUMBURG/SAALE        51.09   11.48   135 Sachsen-Anhalt
N5432 ---- MUEHLHAUSEN           51.12   10.30   190 Thüringen
N5446 ---- OBERWESEL             50.07    7.43   110 Rheinland-Pfalz
N5528 ---- ARNSTADT              50.51   10.58   267 Thüringen
N5537 ---- TAMBACH-DIETHARZ      50.48   10.37   470 Thüringen
N5570 ---- BAD TENNSTEDT         51.09   10.50   175 Thüringen
N5601 ---- SOEMMERDA             51.10   11.08   140 Thüringen
N5755 ---- NORDHAUSEN            51.31   10.48   247 Thüringen
N5791 ---- SANGERHAUSEN          51.29   11.19   185 Sachsen-Anhalt
N5872 ---- BAD DUERRENBERG       51.18   12.05   103 Sachsen-Anhalt
N5939 ---- ADORF                 50.19   12.16   450 Sachsen
N6016 ---- STEFFENBERG           50.51    8.28   338 Hessen
N6037 ---- ULRICHSTEIN           50.35    9.12   575 Hessen
N6067 ---- DELMENHORST           53.03    8.38    10 Niedersachsen
N6160 ---- BUTZBACH              50.28    8.40   238 Hessen
N6172 ---- WETZLAR               50.32    8.30   180 Hessen
N6197 ---- MEUSELWITZ            51.03   12.18   174 Thüringen
N6208 ---- DIETZHOELZTAL         50.51    8.20   355 Hessen
N6223 ---- HERBORN               50.41    8.18   238 Hessen
N6230 ---- OSTERHOLZ-SCHARMBECK  53.13    8.49     5 Niedersachsen
N6241 ---- MENGERSKIRCHEN        50.34    8.09   412 Hessen
N6250 ---- SCHMITTEN-TREISBERG   50.18    8.26   535 Hessen
N6257 ---- BORNA                 51.09   12.28   135 Sachsen
N6259 ---- WEILMUENSTER          50.26    8.23   210 Hessen
N6357 ---- QUERFURT              51.23   11.35   190 Sachsen-Anhalt
N6423 ---- BAD ZWISCHENAHN       53.12    8.00     7 Niedersachsen
N6435 ---- HETTSTEDT             51.39   11.31   159 Sachsen-Anhalt
N6553 ---- HASSELFELDE(WASSW.)   51.43   10.49   485 Sachsen-Anhalt
N6566 ---- ALTENBRAK             51.44   10.56   300 Sachsen-Anhalt
N6695 ---- OSCHERSLEBEN/BODE     52.01   11.14    80 Sachsen-Anhalt
N6813 ---- LINDAU/SACHS.-ANHALT  52.02   12.06    75 Sachsen-Anhalt
N6935 ---- HALDENSLEBEN          52.17   11.26    50 Sachsen-Anhalt
N7012 ---- BAD OLDESLOE          53.49   10.24    15 Schleswig-Holstein
N7029 ---- RATZEBURG             53.42   10.46    10 Schleswig-Holstein
N7040 ---- PRUEM                 50.13    6.25   465 Rheinland-Pfalz
N7060 ---- ARZFELD               50.05    6.16   497 Rheinland-Pfalz
N7075 ---- BITBURG               49.59    6.33   285 Rheinland-Pfalz
N7113 ---- NEUSTRELITZ           53.23   13.03    64 Mecklenburg-Vorpommern
N7134 ---- TRIPPSTADT            49.22    7.49   430 Rheinland-Pfalz
N7135 ---- TEMPLIN               53.07   13.31    60 Brandenburg
N7142 ---- ZEHDENICK             52.59   13.21    46 Brandenburg
N7182 ---- LOEBAU                51.06   14.41   249 Sachsen
N7239 ---- HERMESKEIL            49.39    6.56   530 Rheinland-Pfalz
N7244 ---- ECKERNFOERDE          54.27    9.51    25 Schleswig-Holstein
N7314 ---- WEISSWASSER           51.30   14.37   155 Sachsen
N7316 ---- MERZIG                49.27    6.38   171 Saarland
N7332 ---- SAARBURG              49.37    6.33   180 Rheinland-Pfalz
N7386 ---- FUERSTENWALDE/SPREE   52.21   14.04    38 Brandenburg
N7395 ---- STRAUSBERG            52.35   13.53    73 Brandenburg
N7411 ---- DAHME                 51.52   13.26    86 Brandenburg
N7417 ---- DAHLEM-KRONENBURG     50.22    6.29   480 Nordrhein-Westfalen
N7511 ---- TREUENBRIETZEN        52.06   12.53    59 Brandenburg
N7539 ---- WITTLICH              49.59    6.54   177 Rheinland-Pfalz
N7544 ---- LEHNIN                52.19   12.45    35 Brandenburg
N7608 ---- KASTELLAUN            50.04    7.27   425 Rheinland-Pfalz
N7622 ---- BURG B.MAGDEBURG      52.17   11.49    40 Sachsen-Anhalt
N7651 ---- ORANIENBURG           52.45   13.12    35 Brandenburg
N7659 ---- NAUEN                 52.37   12.52    35 Brandenburg
N7740 ---- FRIESACK              52.46   12.35    29 Brandenburg
N7744 ---- ALTENKIRCHEN          50.41    7.39   260 Rheinland-Pfalz
N7817 ---- PRITZWALK             53.09   12.10    70 Brandenburg
N7822 ---- BLANKENHEIM/AHRHUET.  50.24    6.44   400 Nordrhein-Westfalen
N7868 ---- STENDAL               52.34   11.53    34 Sachsen-Anhalt
N8032 ---- KIRCHEN/SIEG          50.48    7.54   300 Rheinland-Pfalz
N8044 ---- WEITERFELD            50.44    7.56   460 Rheinland-Pfalz
N8101 ---- WALDBROEL             50.52    7.37   295 Nordrhein-Westfalen
N8128 ---- SIEGBURG              50.48    7.12    63 Nordrhein-Westfalen
N8146 ---- GUMMERSBACH           51.01    7.35   250 Nordrhein-Westfalen
N8204 ---- BRUEHL                50.50    6.55    61 Nordrhein-Westfalen
N8232 ---- SALZWEDEL             52.52   11.09    23 Sachsen-Anhalt
N8261 ---- HITZACKER             53.09   11.02    28 Niedersachsen
N8307 ---- RADEVORMWALD          51.13    7.23   397 Nordrhein-Westfalen
N8322 ---- WUPPERTAL-BARMEN      51.16    7.11   197 Nordrhein-Westfalen
N8326 ---- HAGENOW               53.26   11.11    30 Mecklenburg-Vorpommern
N8331 ---- LUDWIGSLUST           53.20   11.30    30 Mecklenburg-Vorpommern
N8334 ---- WUPPERTAL-VOHW.       51.14    7.04   176 Nordrhein-Westfalen
N8346 ---- REMSCHEID             51.12    7.12   235 Nordrhein-Westfalen
N8349 ---- WERMELSKIRCHEN        51.08    7.14   280 Nordrhein-Westfalen
N8369 ---- BERG.NEUKIRCHEN       51.05    7.02   130 Nordrhein-Westfalen
N8381 ---- DORMAGEN              51.07    6.51    40 Nordrhein-Westfalen
N8403 ---- BAD MUENSTEREIFEL     50.33    6.46   320 Nordrhein-Westfalen
N8408 ---- SUDERBURG             52.54   10.26    70 Niedersachsen
N8421 ---- BAD BEVENSEN          53.05   10.34    32 Niedersachsen
N8424 ---- ERFTSTADT-BLIESHEIM   50.47    6.49   106 Nordrhein-Westfalen
N8439 ---- ZUELPICH              50.42    6.39   170 Nordrhein-Westfalen
N8481 ---- NEUSS                 51.11    6.42    39 Nordrhein-Westfalen
N8524 ---- TRITTAU               53.37   10.24    40 Schleswig-Holstein
N8527 ---- KREFELD               51.18    6.32    40 Nordrhein-Westfalen
N8566 ---- MESCHEDE/HENNE        51.20    8.16   348 Nordrhein-Westfalen
N8613 ---- SORPE                 51.22    7.58   294 Nordrhein-Westfalen
N8615 ---- HARSEFELD             53.27    9.30    32 Niedersachsen
N8623 ---- BRILON                51.25    8.39   457 Nordrhein-Westfalen
N8625 ---- STADERSAND            53.38    9.32     5 Niedersachsen
N8631 ---- RUETHEN               51.30    8.27   330 Nordrhein-Westfalen
N8634 ---- WARSTEIN              51.27    8.21   330 Nordrhein-Westfalen
N8653 ---- MOEHNE                51.30    8.04   232 Nordrhein-Westfalen
N8667 ---- BAD BRAMSTEDT         53.55    9.54    10 Schleswig-Holstein
N8686 ---- FROENDENBERG          51.28    7.44   121 Nordrhein-Westfalen
N8690 ---- BROKDORF              53.52    9.20     1 Schleswig-Holstein
N8716 ---- SCHWERTE              51.28    7.34   180 Nordrhein-Westfalen
N8723 ---- WINTERBERG-ALTASTBG.  51.12    8.28   782 Nordrhein-Westfalen
N8777 ---- OLPE                  51.02    7.51   305 Nordrhein-Westfalen
N8790 ---- BIGGE                 51.07    7.53   311 Nordrhein-Westfalen
N8825 ---- VERSE                 51.12    7.41   392 Nordrhein-Westfalen
N8829 ---- LUEDENSCHEID          51.13    7.38   444 Nordrhein-Westfalen
N8832 ---- ISERLOHN-RODEN        51.22    7.40   222 Nordrhein-Westfalen
N8864 ---- ENNEPETAL-MILSPE      51.18    7.19   280 Nordrhein-Westfalen
N8867 ---- SPROCKHOEVEL-HASSL.   51.20    7.17   270 Nordrhein-Westfalen
N8884 ---- HAGEN                 51.21    7.27   113 Nordrhein-Westfalen
N8947 ---- VELBERT-LANGENBERG    51.22    7.07   220 Nordrhein-Westfalen
N9030 ---- HERNE                 51.32    7.13    63 Nordrhein-Westfalen
N9067 ---- BOTTROP               51.33    6.57    38 Nordrhein-Westfalen
N9079 ---- OBERHAUSEN            51.31    6.49    33 Nordrhein-Westfalen
N9109 ---- MOERS                 51.27    6.39    26 Nordrhein-Westfalen
N9117 ---- HILDBURGHAUSEN        50.26   10.43   370 Thüringen
N9126 ---- SCHMIEDEFELD/RSTG.    50.37   10.49   720 Thüringen
N9154 ---- SUHL                  50.37   10.40   505 Thüringen
N9227 ---- WUENNENBERG           51.31    8.45   345 Nordrhein-Westfalen
N9228 ---- BAD SALZUNGEN         50.48   10.13   290 Thüringen
N9320 ---- DELBRUECK             51.46    8.33    97 Nordrhein-Westfalen
N9323 ---- WADERSLOH             51.46    8.16    92 Nordrhein-Westfalen
N9328 ---- RUHLA                 50.54   10.22   470 Thüringen
N9349 ---- GOTHA                 50.56   10.40   321 Thüringen
N9350 ---- SOEST                 51.34    8.07   110 Nordrhein-Westfalen
N9357 ---- EISENACH              50.59   10.22   240 Thüringen
N9401 ---- HAMM                  51.41    7.49    59 Nordrhein-Westfalen
N9413 ---- EILSLEBEN             52.09   11.13   140 Sachsen-Anhalt
N9446 ---- WALTROP               51.38    7.24    73 Nordrhein-Westfalen
N9530 ---- HALTERN               51.44    7.12    40 Nordrhein-Westfalen
N9538 ---- DORSTEN               51.40    6.59    33 Nordrhein-Westfalen
N9607 ---- WESEL-FLUEREN         51.42    6.35    25 Nordrhein-Westfalen
C0014 ---- HARSEWINKEL           51.58    8.13   119 Nordrhein-Westfalen
C0015 ---- STEINHAGEN            52.01    8.25   122 Nordrhein-Westfalen
C0073 ---- BIELEFELD/OLDENTRUP   52.01    8.37   100 Nordrhein-Westfalen
P0004 ---- AACHEN-RICHTERICH     50.49    6.03   240 Nordrhein-Westfalen
P0006 ---- BILLERBECK            51.58    7.17   127 Nordrhein-Westfalen
P0007 ---- TAUS                  49.26   12.54   428 Plzeňský kraj
P0008 ---- COMO                  45.47    9.05    62 Lombardei
P0009 ---- ARNHEIM               51.59    5.54    10 Gelderland
P0010 ---- LUETTICH              50.38    5.33    50 Wallonische Region
P0011 ---- MERAN                 46.40   11.09   324 Trentino-Südtirol
P0012 ---- LEIBSTADT             47.36    8.11   340 Aargau
P0013 ---- NEUSS-WEHL            51.08    6.41    60 Nordrhein-Westfalen
P0016 ---- GR.FELDBG./TS.        50.14    8.28   880 Hessen
P0017 ---- GROSS UMSTADT         49.52    8.56   168 Hessen
P0018 ---- MELIBOCUS             49.44    8.39   517 Hessen
P0019 ---- NIDDA                 50.25    9.01   190 Hessen
P0020 ---- VOGELSBERG            50.32    9.14   774 Hessen
P0021 ---- LAMBRECHT             49.22    8.04   176 Rheinland-Pfalz
P0022 ---- NEBELHORN             47.24   10.18  2224 Bayern
P0023 ---- KITZBUEHEL            47.26   12.22   870 Tirol
P0024 ---- RIVA D. GARDA         45.56   10.59   130 Trentino-Südtirol
P0025 ---- GEESTHACHT            53.25   10.20     0 Niedersachsen
P0026 EDHI FINKENWERDER          53.32    9.50     0 Hamburg
P0027 ---- BRUNSBUETTEL/SWA      53.54    9.08     0 Schleswig-Holstein
P0028 ---- HOECHSTADT            49.41   10.50   272 Bayern
P0029 ---- ISSUM                 51.32    6.25    35 Nordrhein-Westfalen
P0030 ---- OBERHAUSEN-STERKRADE  51.32    6.52    54 Nordrhein-Westfalen
P0031 ---- MUELHEIM/RUHR         51.26    6.53    38 Nordrhein-Westfalen
P0032 ---- SCHWELM               51.17    7.18   165 Nordrhein-Westfalen
P0033 ---- UNNA                  51.32    7.41    86 Nordrhein-Westfalen
P0034 ---- SCHWANDORF            49.20   12.07   372 Bayern
P0035 ---- WESTERBERG            47.46   12.37  1168 Bayern
P0036 ---- MUENSTER ZENTRUM      51.58    7.38    60 Nordrhein-Westfalen
P0037 ---- METALLEUROP           53.33    8.28    10 Niedersachsen
P0038 ---- COTTBUS/LUB           51.45   14.19    76 Brandenburg
P0039 ---- KOENIGS WUSTERH./LUB  52.18   13.38    48 Brandenburg
P0040 ---- POTSDAM-ZENTRUM/LUB   52.24   13.04    31 Brandenburg
P0041 ---- PREMNITZ/LUB          52.32   12.21    30 Brandenburg
P0042 ---- SCHWEDT/LUB           53.03   14.18     6 Brandenburg
P0043 ---- SENFTENBERG/LUB       51.31   14.00   103 Brandenburg
P0044 ---- SPREMBERG/LUB         51.34   14.23   100 Brandenburg
P0045 ---- WITTENBERGE/LUB       53.00   11.46    22 Brandenburg
P0050 ---- FALKENSTEIN/TAUNUS    50.11    8.28   550 Hessen
P0051 ---- DUELMEN               51.50    7.14    70 Nordrhein-Westfalen
P0053 ---- ANEMOLTER             52.30    9.05    39 Niedersachsen
P0054 ---- BORNUM AM HARZ        51.55   10.10   170 Niedersachsen
P0055 ---- ALTOETTING            48.16   12.38   372 Bayern
P0056 ---- LUPFEN                48.05    8.30   970 Baden-Württemberg
P0057 ---- GROSSER BEERBERG      50.40   10.45   980 Thüringen
P0058 ---- SANKT GALLENKIRCH     47.02    9.59   750 Vorarlberg
P0059 ---- MITTAGSSPITZE         47.18    9.53  2097 Vorarlberg
P0060 ---- PATSCHERKOFEL         47.13   11.29  2248 Tirol
P0061 ---- HUNDSTEIN             47.22   12.54  2116 Salzburg
P0062 ---- TRAUNKIRCHEN          47.48   13.48   500 Oberösterreich
P0063 ---- ULRICHSBERG           48.41   13.55  1000 Oberösterreich
P0064 ---- PLOECKENSTEIN         48.47   13.52  1378 Jihočeský kraj
P0065 ---- GROSSER HOELLENGOGEL  47.45   13.40  2000 Oberösterreich
P0066 ---- TUERNITZ              47.57   15.30   400 Niederösterreich
P0067 ---- HOELLENSTEIN/YBBS     47.45   14.45  1000 Niederösterreich
P0068 ---- HOCHSCHNEEBERG        47.45   15.50  2000 Niederösterreich
P0069 ---- KAMMSPITZ             47.29   13.51  2141 Steiermark
P0070 ---- CHATILLON             45.45    7.37   500 Aostatal
P0071 ---- MARGOZZO              45.58    8.27   700 Piemont
P0072 ---- MASERA                46.08    8.19   800 Piemont
P0073 ---- M.ZEDA                46.03    8.32  2100 Piemont
P0074 ---- SONDRIO               46.11    9.52   500 Lombardei
P0075 ---- LECCO                 45.51    9.23   400 Lombardei
P0076 ---- BRIXEN                46.43   11.40   600 Trentino-Südtirol
P0077 ---- ROLLEPASS             46.18   11.48  1800 Trentino-Südtirol
P0078 ---- CORTINA D'AMPEZZO     46.33   12.08  1300 Venetien
P0079 ---- PASO DI FALZAREGO     46.32   12.02  1850 Venetien
P0080 ---- ALBERTVILLE           45.40    6.24   500 Auvergne-Rhône-Alpes
P0081 ---- LE ROIGNAIS           45.39    6.43  3001 Auvergne-Rhône-Alpes
P0082 ---- CHAMONIX              45.55    6.52  1000 Auvergne-Rhône-Alpes
P0083 ---- ANNECY                45.54    6.07   500 Auvergne-Rhône-Alpes
P0084 ---- MT. BUET              46.01    6.53  3100 Auvergne-Rhône-Alpes
P0085 ---- CHORGES               44.33    6.16   600 Provence-Alpes-Côte d'Azur
P0086 ---- SERRE CHEVALIER       44.55    6.30  2700 Provence-Alpes-Côte d'Azur
P0087 ---- DIGNE                 44.05    6.14   700 Provence-Alpes-Côte d'Azur
P0088 ---- ANNOT                 43.58    6.42   600 Provence-Alpes-Côte d'Azur
P0089 ---- CROIX DE L ALPE       44.24    6.40  2590 Provence-Alpes-Côte d'Azur
P0091 ---- SIMPLONPASS           46.15    8.03  2000 Wallis
P0092 ---- MT. AUBERT            46.53    6.38  1339 Waadt
P0093 ---- LILLEHAMMER           61.06   10.27   500 Innlandet
P0095 ---- TORPO                 60.30    8.15  1000 Viken
P0096 ---- FINSE                 60.36    7.30  1500 Vestland
P0097 ---- SELJORD               59.30    8.40   300 Vestfold og Telemark
P0098 ---- LIFJELL               59.15    8.30   800 Vestfold og Telemark
P0099 ---- LJUBLJANA             46.04   14.39   400 Ljubljana
P0100 ---- BLED                  46.22   14.07   900 Radovljica
P0101 ---- OF-POST D1            49.12    8.24   259 Baden-Württemberg
P0102 ---- OF-POST D2            47.54    9.54   576 Baden-Württemberg
P0103 ---- OF-POST D3            48.42   12.30   462 Bayern
P0104 ---- OF-POST D4            50.24   10.42   441 Thüringen
P0105 ---- OF-POST D5            52.48    8.30    18 Niedersachsen
P0106 ---- OF-POST D6            51.42    8.00   192 Nordrhein-Westfalen
P0107 ---- OF-POST D7            51.18    9.48   317 Hessen
P0108 ---- OF-POST D8            53.12   12.12    60 Brandenburg
P0109 ---- OF-POST D9            51.36   13.30   115 Brandenburg
P0110 ---- OF-POST H1            49.58    8.48   214 Hessen
P0111 ---- OF-POST H2            50.21    8.22   281 Hessen
P0112 ---- OF-POST H3            50.57    9.06   356 Hessen
P0113 ---- OF-POST H4            50.57    9.45   351 Hessen
P0114 ---- OF-POST H5            50.27    9.12   318 Hessen
P0115 ---- LOIBLPASS             46.25   14.17  1500 Tržič
P0116 ---- NEUERN/NYRSKO         49.18   13.10   600 Plzeňský kraj
P0118 ---- PASO DI CAMPELLI      46.01   10.01  1890 Lombardei
P0119 ---- SCHMOELLN             53.18   14.05    20 Brandenburg
P0120 ---- HAMBURG-NEUENG.       53.25   10.14    10 Hamburg
P0121 ---- WENNIGSEN             52.16    9.39    30 Niedersachsen
P0122 ---- WIELEN                52.32    6.45    20 Niedersachsen
P0123 ---- LAUCHA                51.07   14.39   240 Sachsen
P0124 ---- TIMMENDORF/POEL       53.59   11.23    12 Mecklenburg-Vorpommern
P0125 ---- KRAGELUND             54.41    9.49    20 Schleswig-Holstein
P0126 ---- LINDEWITT             54.43    9.09    20 Schleswig-Holstein
P0127 ---- SOELLMNITZ            50.57   12.09   311 Thüringen
P0128 ---- PODELZIG              52.28   14.31    20 Brandenburg
P0129 ---- DELITZSCH-SELBEN      51.30   12.23   150 Sachsen
P0130 ---- KRUMMHOERN-LOQUARD    53.23    7.04    10 Niedersachsen
P0131 ---- KAISER-WILH.-KOOG     53.56    8.56     5 Schleswig-Holstein
P0132 ---- MESSMAST WHV          53.37    8.03    10 Niedersachsen
P0133 ---- MESSMAST OL           53.09    8.03    10 Niedersachsen
P0134 ---- MESSMAST EMD          53.23    7.10    10 Niedersachsen
P0135 ---- HILKENBROOK, NT       52.59    7.42    15 Niedersachsen
P0136 ---- VIENENBURG, MG        51.57   10.36   100 Niedersachsen
P0137 ---- SYKE-GESSEL, NTB      52.56    8.46    20 Niedersachsen
P0138 ---- HOHEGING, NT          52.54    8.07    15 Niedersachsen
P0139 ---- ALTENBEKEN, MG        51.44    8.56   300 Nordrhein-Westfalen
P0140 ---- RAPSHAGEN, NT         53.13   12.14    70 Brandenburg
P0141 ---- BASSENS               53.42    7.56     2 Niedersachsen
P0142 ---- TOSSENS               53.35    8.15     2 Niedersachsen
P0143 ---- WYBELSUMER POLDER     53.20    7.06     2 
P0144 ---- SCHUELP               54.14    8.55    20 Schleswig-Holstein
P0145 ---- HAMSWEHRUM            53.27    7.10    10 Niedersachsen
P0146 ---- PILSUM                53.29    7.20    10 Niedersachsen
P0147 ---- ASENDORF              52.45    9.00    40 Niedersachsen
P0148 ---- MENSLAGE              52.35    7.43    25 Niedersachsen
P0149 ---- GARLSTORF             53.14   10.00    80 Niedersachsen
P0150 ---- ST.PETER-ORDING       54.19    8.41     2 Schleswig-Holstein
P0151 ---- HALLIG HOOGE          54.34    8.32     2 Schleswig-Holstein
P0152 ---- PLOEN                 54.10   10.23    22 Schleswig-Holstein
P0153 ---- NORDW. FPN            55.00    6.27     0 
P0154 ---- WESTL. SYLT           55.00    7.18     0 
P0155 ---- BRUGGE                51.13    3.14     5 Flämische Region
P0157 ---- DIESSEN               47.57   11.06   500 Bayern
P0158 ---- CHIEMSEE              47.50   12.20   500 Bayern
P0159 ---- GMUND/TEGERNSEE       47.45   11.45   500 Bayern
P0160 ---- STEINBACH             47.50   13.15   500 Salzburg
P0161 ---- HALLSTATT             47.34   13.39   500 Oberösterreich
P0162 ---- SAN VIGILIO           46.42   11.56  1000 Trentino-Südtirol
P0163 ---- BELLAGIO              45.59    9.16   200 Lombardei
P0164 ---- DOMASO                46.09    9.21   200 Lombardei
P0165 ---- ISEO                  45.39   10.03   100 Lombardei
P0166 ---- LA SPEZIA             44.10    9.45     0 Ligurien
P0167 ---- LIVORNO               43.33   10.18     0 
P0168 ---- SAN REMO              43.48    7.46     0 Ligurien
P0169 ---- LEUCATE               42.50    3.05     0 
P0171 ---- TRIENT                46.06   11.09   194 Trentino-Südtirol
P0172 ---- MITROVICA             42.54   20.52   521 
P0173 ---- GNJILANE              42.28   21.29   500 
P0174 ---- LEISENWALD            50.19    9.10   371 Hessen
P0175 ---- ROSTOCK-STADT         54.05   12.08     9 Mecklenburg-Vorpommern
P0176 ---- BUERSTADT             49.38    8.27    90 Hessen
P0177 ---- WALD-MICHELBACH       49.34    8.50   330 Hessen
P0178 ---- BIEBESHEIM            49.47    8.28    90 Hessen
P0179 ---- BRENSBACH             49.46    8.51   200 Hessen
P0180 ---- GRUENBERG             50.37    8.58   273 Hessen
P0181 ---- STADTALLENDORF        50.50    9.01   300 Hessen
P0182 ---- LAUTERBACH            50.38    9.24   296 Hessen
P0183 ---- BURGHAUN              50.43    9.43   245 Hessen
P0184 ---- SCHLENKLENGSFELD      50.50    9.49   310 Hessen
P0185 ---- BAD EMSTAL            51.15    9.14   370 Hessen
P0186 ---- BAD BREISIG           50.31    7.18    53 Rheinland-Pfalz
P0187 ---- BETZDORF              50.47    7.53   186 Rheinland-Pfalz
P0188 ---- PUDERBACH             50.35    7.33   203 Rheinland-Pfalz
P0189 ---- ST.GOAR               50.09    7.43    80 Rheinland-Pfalz
P0190 ---- NASSAU/RHL.-PFALZ     50.19    7.47    90 Rheinland-Pfalz
P0191 ---- NASTAETTEN            50.12    7.52   268 Rheinland-Pfalz
P0192 ---- GEROLSTEIN            50.13    6.40   358 Rheinland-Pfalz
P0193 ---- HINTERWEIDENTHAL      49.12    7.45   350 Rheinland-Pfalz
P0194 ---- FREINSHEIM            49.30    8.13   100 Rheinland-Pfalz
P0195 ---- ROCKENHAUSEN          49.38    7.49   203 Rheinland-Pfalz
P0196 ---- EISENBERG             49.38    8.05   248 Rheinland-Pfalz
P0197 ---- WOERTH                49.48    9.09   105 Bayern
P0198 ---- MIESAU                49.24    7.26   236 Rheinland-Pfalz
P0199 ---- UETERSEN              53.41    9.39     5 Schleswig-Holstein
P0200 ---- LABOE                 54.24   10.15    34 Schleswig-Holstein
P0201 ---- SCHENEFELD            53.36    9.49    10 Schleswig-Holstein
P0202 ---- GLINDE                53.32   10.13    30 Schleswig-Holstein
P0203 ---- WITTINGEN             52.43   10.44    78 Niedersachsen
P0204 ---- HANNOV.MUENDEN        51.25    9.39   125 Niedersachsen
P0205 ---- PEINE                 52.19   10.13    67 Niedersachsen
P0206 ---- AMT NEUHAUS           53.17   10.55    20 Niedersachsen
P0207 ---- HODENHAGEN            52.46    9.35    25 Niedersachsen
P0208 ---- LANGWEDEL             52.58    9.12    20 Niedersachsen
P0209 ---- GLANDORF              52.05    7.59    64 Niedersachsen
P0210 ---- DAMME                 52.30    8.08    63 Niedersachsen
P0211 ---- LANGWARDEN            53.36    8.19     8 Niedersachsen
P0212 ---- PULHEIM               51.00    6.28    46 Nordrhein-Westfalen
P0213 ---- KERPEN                50.52    6.40   100 Nordrhein-Westfalen
P0214 ---- TROISDORF             50.50    7.10    50 Nordrhein-Westfalen
P0215 ---- MECKENHEIM/RHEINB.    50.37    7.02   180 Nordrhein-Westfalen
P0216 ---- LINNICH               50.59    6.15    67 Nordrhein-Westfalen
P0217 ---- ALDENHOVEN            50.54    6.17    70 Nordrhein-Westfalen
P0218 ---- MECHERNICH            50.35    6.39   300 Nordrhein-Westfalen
P0219 ---- WIESDORF              51.00    6.59    45 Nordrhein-Westfalen
P0220 ---- OPLADEN               51.01    7.00    57 Nordrhein-Westfalen
P0221 ---- SCHLEBUSCH            51.02    7.04   100 Nordrhein-Westfalen
P0222 ---- RHEINDORF             51.03    6.56    47 Nordrhein-Westfalen
P0223 ---- LEICHLINGEN           51.07    7.01   166 Nordrhein-Westfalen
P0224 ---- BAESWEILER            50.54    6.11   110 Nordrhein-Westfalen
P0225 ---- BERGHEIM              50.55    6.38    70 Nordrhein-Westfalen
P0226 ---- BERGISCH GLADBACH     50.59    7.07   162 Nordrhein-Westfalen
P0227 ---- KOENIGSWINTER         50.40    7.11    80 Nordrhein-Westfalen
P0228 ---- EITORF                50.46    7.26    89 Nordrhein-Westfalen
P0229 ---- REKEN                 51.50    7.02    70 Nordrhein-Westfalen
P0230 ---- ASCHEBERG             51.47    7.37    75 Nordrhein-Westfalen
P0231 ---- HALLE/NORD.WESTFALEN  52.04    8.22   105 Nordrhein-Westfalen
P0232 ---- HOLTE-STUKENBROCK     51.54    8.39   130 Nordrhein-Westfalen
P0233 ---- BUENDE                52.12    8.35    61 Nordrhein-Westfalen
P0234 ---- ERWITTE               51.37    8.20   106 Nordrhein-Westfalen
P0238 ---- LIMASSOL              34.40   33.03    40 Bezirk Limassol
P0239 ---- MARBELLA              36.31   -4.53    30 
P0240 ---- SAN FELIU             41.45    3.05    10 
P0241 ---- SAINT TROPEZ          43.16    6.39    20 Provence-Alpes-Côte d'Azur
P0242 ---- CERNOBBIO             45.50    9.05   400 Lombardei
P0243 ---- ISCHIA                40.44   13.57    80 
P0244 ---- PORTOFINO             44.18    9.12     5 Ligurien
P0245 ---- MADEIRA/FESTLAND      39.57   -8.02   500 Distrikt Castelo Branco
P0246 ---- KARTHAGO              36.54   10.16     3 Gouvernement Tunis
P0247 ---- WIESENSTEIG           48.32    9.37   756 Baden-Württemberg
P0248 ---- BESIGHEIM             49.00    9.09   202 Baden-Württemberg
P0249 ---- SCHORNDORF            48.47    9.31   328 Baden-Württemberg
P0250 ---- KRAUTHEIM             49.13    9.22   298 Baden-Württemberg
P0251 ---- SULZBACH-LAUFEN       48.34    9.30   360 Baden-Württemberg
P0252 ---- BILLIGHEIM            49.21    9.16   290 Baden-Württemberg
P0253 ---- LOSSBURG              48.43    8.45   347 Baden-Württemberg
P0254 ---- KIRCHZARTEN           47.58    7.57   388 Baden-Württemberg
P0255 ---- ENDINGEN              48.08    7.42   186 Baden-Württemberg
P0256 ---- OTTENHOEFEN           48.20    8.05   311 Baden-Württemberg
P0257 ---- SINGEN                47.45    8.49   450 Baden-Württemberg
P0258 ---- JESTETTEN             47.39    8.34   470 Baden-Württemberg
P0259 ---- TRUCHTELFINGEN        48.14    9.01   475 Baden-Württemberg
P0260 ---- ILLERIEDEN-DORNDORF   48.17   10.02   461 Baden-Württemberg
P0261 ---- GAMMERTINGEN          48.08    9.07   659 Baden-Württemberg
P0262 ---- WOLFRATSHAUSEN        47.50   11.25   577 Bayern
P0263 ---- PFAFFENHOFEN          48.18   11.18   428 Bayern
P0264 ---- BRUCKMUEHL            47.53   11.55   512 Bayern
P0265 ---- BUCH AM AMMERSEE      48.03   11.08   550 Bayern
P0266 ---- KUENZING              48.23   13.03   309 Bayern
P0267 ---- OBERNZENN             49.17   10.16   400 Bayern
P0268 ---- FISCHACH              48.10   10.23   490 Bayern
P0269 ---- LAUINGEN              48.20   10.15   439 Bayern
P0273 ---- HELMBRECHTS           50.14   11.43   617 Bayern
P0274 ---- BLIESRANDSBACH        49.10    7.05   250 Saarland
P0275 ---- HEUSWEILER            49.21    6.57   300 Saarland
P0276 ---- PERL                  49.28    6.23   270 Saarland
P0277 ---- WADERN                49.32    6.53   300 Saarland
P0278 ---- NEUNKIRCHEN/SAARLAND  49.12    7.06   224 Saarland
P0279 ---- SCHMELZ               49.26    6.51   230 Saarland
P0280 ---- NONNWEILER            49.36    6.39   420 Rheinland-Pfalz
P0281 ---- BERNAU/BRANDENBURG    52.40   13.34    67 Brandenburg
P0282 ---- HERZBERG/BRANDENBURG  51.42   13.14    81 Brandenburg
P0283 ---- TREBUS                52.25   14.04    15 Brandenburg
P0284 ---- LUEBBENAU             51.52   13.58    51 Brandenburg
P0285 ---- LUCKENWALDE           52.10   13.09    40 Brandenburg
P0286 ---- SATOW                 53.34   11.30    50 Mecklenburg-Vorpommern
P0288 ---- MEERANE               50.51   12.27   250 Sachsen
P0289 ---- KAEBSCHUETZTAL        51.10   13.23   150 Sachsen
P0290 ---- OPPACH                51.04   14.31   350 Sachsen
P0291 ---- DOEBELN               51.04   13.04   210 Sachsen
P0292 ---- WURZEN                51.22   12.44   124 Sachsen
P0293 ---- POESSNECK             50.40   11.33   250 Thüringen
P0295 ---- NIESKY                51.17   14.51   165 Sachsen
P0297 ---- DINGOLFING            48.45   12.33   360 Bayern
P0298 ---- ARLBERG               47.08   10.11  1793 Vorarlberg
P0299 ---- GROSSGLOCKNER         47.05   12.41  3797 Tirol
P0300 ---- DACHSTEIN             47.28   13.36  2995 Steiermark
P0301 ---- LICHTENBERG           48.25   14.15   926 Oberösterreich
P0302 ---- ZINKEN                47.20   14.45  2331 Steiermark
P0303 ---- WEINSBERG             48.24   15.06  1039 Niederösterreich
P0304 ---- KAISEREICHE           47.57   16.41   443 Burgenland
P0305 ---- SONNENBERG            47.53   16.29   484 Burgenland
P0306 ---- WANK                  47.30   11.08  1770 Bayern
P0307 ---- HOERNLE               47.38   11.04  1538 Bayern
P0308 ---- BRAUNECK              47.40   11.31  1545 Bayern
P0309 ---- HOCHFELLN             47.45   12.33  1665 Bayern
P0310 ---- PREDIGTSTUHL          47.42   12.52  1607 Bayern
P0311 ---- ANDERMATT             46.38    8.36  1500 Uri
P0312 ---- LINTHAL               46.55    9.00  1000 Glarus
P0314 ---- SAANEN-GSTAAD         46.30    7.16  1100 Bern
P0325 ---- ANDORRA               42.33    1.36  1500 Canillo
P0326 ---- WELVER                51.37    7.55   114 Nordrhein-Westfalen
P0327 ---- ISERLOHN              51.25    7.41   279 Nordrhein-Westfalen
P0328 ---- SIEDLINGHAUSEN        51.15    8.28   364 Nordrhein-Westfalen
P0329 ---- MARSBERG-POSTWEG      51.26    8.47   445 Nordrhein-Westfalen
P0330 ---- HORN                  51.53    8.57   210 Nordrhein-Westfalen
P0331 ---- GOEHL                 54.17   10.56    19 Schleswig-Holstein
P0332 ---- BISDORF               54.28   11.10     9 Schleswig-Holstein
P0333 ---- KHANIA                35.31   24.01    24 
P0346 ---- GETTORF               54.25    9.59    10 Schleswig-Holstein
P0347 ---- HARRISLEE             54.48    9.23    10 Schleswig-Holstein
P0348 ---- MALENTE               54.10   10.33    15 Schleswig-Holstein
P0349 ---- MARNE                 53.57    9.01     5 Schleswig-Holstein
P0350 ---- REINFELD              53.50   10.29    15 Schleswig-Holstein
P0351 ---- SCHOENBERG            54.24   10.22     5 Schleswig-Holstein
P0352 ---- TRAPPENKAMP           54.02   10.13    70 Schleswig-Holstein
P0353 ---- WESSELBUREN           54.13    8.55     5 Schleswig-Holstein
P0354 ---- MEISSNER              51.14    9.53   754 Hessen
P0355 ---- KLADRUM               53.33   11.47    50 Mecklenburg-Vorpommern
P0356 ---- RAKOW                 54.03   13.02    17 Mecklenburg-Vorpommern
P0357 ---- RAVENSBERG            53.59   11.42    12 Mecklenburg-Vorpommern
P0358 ---- ABLASS                51.13   12.57   150 Sachsen
P0359 ---- DORNA                 51.46   12.42   106 Sachsen-Anhalt
P0360 ---- WILLMERSDORF          52.40   13.41    67 Brandenburg
P0361 ---- HOCHHEIM              51.01   10.39   321 Thüringen
P0362 ---- IHLEWITZ              51.38   11.41   159 Sachsen-Anhalt
P0363 ---- NEUENFELD             53.25   14.01    10 Brandenburg
P0364 ---- OBHAUSEN              51.23   11.39   190 Sachsen-Anhalt
P0365 ---- KLETTWITZ             51.32   13.53   103 Brandenburg
P0366 ---- REICHENBACH           51.08   14.48   249 Sachsen
P0367 ---- ALPE D'HUEZ           45.05    6.04  1860 Auvergne-Rhône-Alpes
P0368 ---- COURCHEVEL            45.24    6.38  1550 Auvergne-Rhône-Alpes
P0369 ---- FLAINE                46.01    6.39  1600 Auvergne-Rhône-Alpes
P0370 ---- ISOLA 2000            44.08    7.12  2000 Provence-Alpes-Côte d'Azur
P0371 ---- MERIBEL               45.22    6.37  1400 Auvergne-Rhône-Alpes
P0372 ---- MORZINE               46.11    6.42  1000 Auvergne-Rhône-Alpes
P0373 ---- VAL D'ISERE           45.27    6.59  1850 Auvergne-Rhône-Alpes
P0374 ---- AHRNTAL               46.59   11.59   950 Trentino-Südtirol
P0375 ---- ARABBA                46.30   11.52  1602 Venetien
P0376 ---- BORMIO 2000           46.26   10.23  1225 Lombardei
P0377 ---- CERVINIA              45.56    7.35  2050 Aostatal
P0378 ---- COURMAYEUR            45.47    6.59  1224 Aostatal
P0379 ---- FOLGARIA              45.55   11.10   900 Trentino-Südtirol
P0380 ---- GOSSENSASS            46.56   11.26  1100 Trentino-Südtirol
P0381 ---- MADONNA DI CAMPIGLIO  46.14   10.49  1500 Trentino-Südtirol
P0383 ---- SCHNALSTAL            46.44   10.54  2000 Trentino-Südtirol
P0384 ---- ST.WALBURG            46.33   11.02  1100 Trentino-Südtirol
P0385 ---- DAMUELS               47.16    9.52  1428 Vorarlberg
P0386 ---- FILZMOOS              47.26   13.32  1055 Salzburg
P0387 ---- FULPMES               47.09   11.20   937 Tirol
P0388 ---- HINTERSEE             47.43   13.17   746 Salzburg
P0389 ---- KAUNERTALER GLETSCH.  47.00   10.47  3000 Tirol
P0390 ---- MATREI/OSTTIROL       47.00   12.32  1000 Tirol
P0391 ---- HOCHSOELDEN           47.04   10.54  1800 Tirol
P0392 ---- ST.JAKOB/DEFEREGGEN.  46.54   12.22  1495 Tirol
P0393 ---- TURRACHER HOEHE       46.54   13.52  1783 Kärnten
P0394 ---- WAGRAIN               47.20   13.17   830 Salzburg
P0395 ---- WOLFSBERG             46.47   14.59   463 Kärnten
P0397 ---- BRANAES               60.41   12.56   152 Värmlands län
P0399 ---- KLAEPPEN              61.10   13.13   350 Dalarnas län
P0401 ---- SAEFSEN               60.09   14.25   300 Dalarnas län
P0402 ---- GRINDELWALD           46.37    8.02  1034 Bern
P0403 ---- LENZERHEIDE           46.43    9.33  1500 Graubünden
P0405 ---- REJVIZ                50.13   17.18   770 Olomoucký kraj
P0406 ---- SPINDLERMUEHLE        50.43   15.37   700 Královéhradecký kraj
P0409 ---- MARSBERG-MEERHOF      51.32    8.50   371 Nordrhein-Westfalen
P0410 ---- BICKENDORF            50.02    6.30   389 Rheinland-Pfalz
P0411 ---- FLOMBORN              49.42    8.10   180 Rheinland-Pfalz
P0412 ---- SCHEID                50.29    6.30   334 Nordrhein-Westfalen
P0413 ---- NIEDER KOSTENZ        49.56    7.22   364 Rheinland-Pfalz
P0414 ---- KEHRIG                50.14    7.13   370 Rheinland-Pfalz
P0415 ---- WILDPOLDSRIED         47.47   10.26   891 Bayern
P0416 ---- RIBNITZ-DAMGARTEN     54.16   12.28     7 Mecklenburg-Vorpommern
P0417 ---- KUESTE JASMUND BODD.  54.30   13.30     3 
P0422 ---- SPAIN_NEW_01          38.50   -6.31   319 Extremadura
P0423 ---- SPAIN_NEW_02          43.15   -4.35   758 Kantabrien
P0424 ---- SPAIN_NEW_03          43.31   -5.53   178 
P0425 ---- SPAIN_NEW_04          40.30   -6.30   920 Kastilien und León
P0426 ---- SPAIN_NEW_05          39.30   -5.25   698 Kastilien-La Mancha
P0427 ---- SPAIN_NEW_06          42.50   -1.38   596 Nouvelle-Aquitaine
P0428 ---- SPAIN_NEW_07          38.50   -2.00   853 Kastilien-La Mancha
P0429 ---- SPAIN_NEW_08          42.41   -6.28   806 Kastilien und León
P0430 ---- BLIESDORF             52.41   14.10     5 Brandenburg
P0431 ---- WERBIG                51.56   13.12   110 Brandenburg
P0432 ---- ROSSAU                51.00   13.06   320 Sachsen
P0433 ---- GROSSMACKENSTEDT      52.59    8.39    13 Niedersachsen
P0434 ---- HASELUENNE KNN        52.43    7.32    26 Niedersachsen
P0435 ---- GRUEPPENBUEHREN       53.04    8.33    33 Niedersachsen
P0436 ---- ARRAS                 50.16    2.46    89 Hauts-de-France
P0437 ---- CALAIS                50.57    1.49     3 Hauts-de-France
P0439 ---- FINO1/PLATTFORM       54.05    6.35    10 
P0441 ---- LENGERICH             52.11    7.52    80 Nordrhein-Westfalen
P0442 ---- TEGELBERG             47.34   10.47  1720 Bayern
P0443 ---- PLATTERHOF            47.38   13.03   954 Bayern
P0444 ---- SCHOTTMALHORN         47.37   12.50  2042 Bayern
P0445 ---- FRANKFURT/ZEIL        50.06    8.41   100 Hessen
P0446 ---- ESSEN/BAHNHOF         51.27    7.01    72 Nordrhein-Westfalen
P0447 LFMQ LE CASTELLET          43.16    5.47   424 Provence-Alpes-Côte d'Azur
P0448 LTFJ SABIHA GOKCEN INTL.   40.54   29.19    95 Istanbul
P0449 LIQS AMPUGNANO             43.15   11.15   194 Toskana
P0450 ---- KISA                  58.06   15.48   132 Östergötlands län
P0451 ---- GOETA KANAL           58.36   15.54    74 Östergötlands län
P0452 ---- VAETTERN              58.18   14.36   111 
P0453 ---- HJAELMAREN            59.12   15.42    39 Örebro län
P0454 ---- KATRINEHOLM           59.06   16.30    61 Södermanlands län
P0455 ---- MALAEREN              59.24   17.12    35 Södermanlands län
P0456 ---- NORR MALAEREN         59.54   17.42    42 Uppsala län
P0457 ---- DALAELVEN             60.24   17.00    69 Gävleborgs län
P0458 ---- NORR HJAELMAREN       59.42   16.06    79 Västmanlands län
P0459 ---- SKYLLBERG             58.54   15.18   100 Örebro län
P0460 ---- SMALAND               57.24   15.06   235 Jönköpings län
P0461 ---- BORAS                 57.30   13.36   219 Jönköpings län
P0462 ---- ALLEBERG              58.12   13.30   171 Västra Götalands län
P0463 ---- TOERREBODA            58.48   14.24   126 Västra Götalands län
P0464 ---- VAENNERN              58.54   13.12    83 Värmlands län
P0465 ---- DEGERFORS             59.36   14.30   196 Örebro län
P0466 ---- BERGSLAGEN            60.00   15.12   217 Örebro län
P0467 ---- TIOMILASKOGEN         60.18   13.24   336 Värmlands län
P0468 ---- BORLAENGE             60.30   15.54   185 Dalarnas län
P0469 ---- GAESTRIKLAND          61.00   16.00   290 Dalarnas län
P0470 ---- SILJAN                60.54   14.48   205 Dalarnas län
P0471 ---- DALARNA               60.54   14.06   382 Dalarnas län
P0472 ---- NORRA DALARNA         61.18   14.42   452 Dalarnas län
P0473 ---- AESNEN                56.36   14.48   160 Kronobergs län
P0474 ---- BOLMEN                56.54   13.24   168 Hallands län
P0475 ---- NORRA SKANE           56.06   13.36   131 Skåne län
P0476 ---- WITTIGHAUSEN          49.38    9.50   270 Baden-Württemberg
P0477 ---- ENERTRAG              53.16   14.02   100 Brandenburg
P0478 EGLC LONDON/CITY INTL      51.29   -0.03     5 England
P0481 ---- WITTEN                51.26    7.20   104 Nordrhein-Westfalen
P0482 ---- OLBERNHAU             50.39   13.20   460 Sachsen
P0483 ---- ROSSKOPF              48.00    7.54   737 Baden-Württemberg
P0484 ---- HOLZSCHLAEGERMATTE    47.55    7.53  1000 Baden-Württemberg
P0487 ---- SDL.FLUSS LITANI      33.08   35.24   800 Gouvernement Nabatäa
P0488 ---- BERGSTEDT             53.40   10.07    26 Hamburg
P0489 ---- HAMBURG INNENSTADT    53.33    9.59     8 Hamburg
P0490 ---- HUERTH                50.53    6.52    60 Nordrhein-Westfalen
P0491 ---- HATTINGEN             51.24    7.11   150 Nordrhein-Westfalen
P0492 ---- VILLARD DE LANS       45.04    5.33  1050 Auvergne-Rhône-Alpes
P0493 ---- ALAGNA                45.50    7.56  1150 Piemont
P0494 ---- ZINAL                 46.07    7.38  1670 Wallis
P0495 ---- CHAMPERY              46.11    6.53  1050 Wallis
P0496 ---- FIESCH                46.24    8.08  1050 Wallis
P0497 ---- MELCHSEE-FRUTT        46.46    8.16  1920 Obwalden
P0498 ---- MAURACH               47.25   11.45   930 Tirol
P0499 ---- SEDRUN                46.41    8.46  1400 Graubünden
P0500 ---- BERTIKOW              53.18   14.01    74 Brandenburg
P0501 ---- LANGEN-TRECHOW        53.54   11.56    25 Mecklenburg-Vorpommern
P0502 ---- HOHEN PRITZ           53.38   11.54    65 Mecklenburg-Vorpommern
P0503 ---- WERDER                53.30   12.00    59 Mecklenburg-Vorpommern
P0504 ---- BERSTELAND-NIEWITZ    51.56   13.47    53 Brandenburg
P0505 ---- MORBACH               49.49    7.07   428 Rheinland-Pfalz
P0506 ---- LUENNE                52.25    7.26    36 Niedersachsen
P0507 ---- HEIDEN                51.49    6.57    70 Nordrhein-Westfalen
P0508 ---- BERGLICHT             49.47    6.58   401 Rheinland-Pfalz
P0509 ---- SASSENBERG            51.59    8.03    60 Nordrhein-Westfalen
P0510 ---- SCHELKLINGEN          48.28    9.43   750 Baden-Württemberg
P0511 ---- SCHEID_2              50.20    6.25   560 Nordrhein-Westfalen
P0512 ---- HAARSTRANG            51.31    8.14   250 Nordrhein-Westfalen
P0513 ---- NEUKIRCHEN            51.04   10.20   227 Thüringen
P0514 ---- RAUSCHWITZ            51.00   11.46   318 Thüringen
P0515 ---- SCHILBACH             50.30   11.52   539 Thüringen
P0516 ---- SCHOENEWALDE          52.01   12.49   148 Brandenburg
P0518 ---- RAGUSA                36.55   14.43   507 Sizilien
P0521 ---- LOVIISA               60.27   26.13     1 Uusimaa
P0523 LFBU BRIE-CHAMPNIERS       45.43    0.13   122 Nouvelle-Aquitaine
P0524 ---- TONNAY CHARENTE       45.56   -0.53    14 Nouvelle-Aquitaine
P0525 ---- GAETA                 41.12   13.34     1 
P0527 ---- SAN CARLOS D.RAPITA   40.37    0.35     1 Katalonien
P0529 ---- TREGUIER              48.47   -3.14    41 
P0531 ---- PORTO EMPEDOCLE       37.17   13.32     7 
P0532 ---- GARCHING              48.16   11.41   463 Bayern
P0533 ---- GUNDREMMINGEN         48.31   10.24   433 Bayern
P0534 ---- ESSENBACH             48.36   12.18   392 Bayern
P0535 ---- IMATRA                61.10   28.45    67 Südkarelien
P0536 ---- MALLAIG               57.00   -5.50    19 Schottland
P0537 ---- PORTREE               57.25   -6.11    14 Schottland
P0538 ---- ULLAPOOL              57.54   -5.10    14 Schottland
P0540 ---- GALLIPOLI             40.04   17.59    12 
P0541 ---- PORTO AZZURRO         42.46   10.24    12 Toskana
P0543 ---- UUSIKAUPUNKI          60.48   21.25    10 Varsinais-Suomi
P0544 ---- BEAUVAIS              49.01   -1.11   111 Normandie
P0545 ---- ASTI                  44.54    8.13   122 Piemont
P0546 ---- EGERSUND              58.27    6.01    27 Rogaland
P0547 ---- ADRA                  36.45   -3.01     8 Andalusien
P0548 ---- BANBURY               52.04   -1.20   107 England
P0549 ---- BLACKBURN             53.45   -2.29   123 England
P0550 ---- LA CIOTAT             43.10    5.36     3 Provence-Alpes-Côte d'Azur
P0551 ---- LA PALMA              37.23   -6.33    95 Andalusien
P0552 ---- MELILLI               37.11   15.08   278 Sizilien
P0553 ---- VIVERO                42.53   -6.14  1389 Kastilien und León
P0554 ---- COSENZA               39.18   16.15   243 Kalabrien
P0555 ---- SASSARI               40.44    8.34   203 Sardinien
P0556 ---- GUARDA                40.32   -7.16  1014 Kastilien und León
P0557 ---- LINARES               38.05   -3.38   411 Kastilien-La Mancha
P0559 ---- OBER-BEERBACH         49.46    8.41   340 Hessen
P0560 ---- ERFURT-STADT          50.59   11.02   200 Thüringen
P0561 ---- HAMBACH               50.24    7.59   260 Rheinland-Pfalz
P0563 EGGW LONDON LUTON          51.52    0.22   160 England
P0564 EGNX EAST MIDLANDS         52.49   -1.20    93 England
P0567 UUWW MOSKVA/VNUKOVO        56.00   37.17   203 Oblast Moskau
P0570 LFRV VANNES MEUCON         47.43   -2.44   134 Pays de la Loire
P0571 LGAV ATHINAI-ELEFTHERIOS   37.56   23.56    94 Attika
P0572 EEEI AMARI                 59.16   24.13    20 Kreis Harju
P0573 EEKE KURESSAARE            58.14   22.31     2 
W3011 ---- WESTL.AGADIR          29.56  -11.27     0 Munizip Nalut
W3212 ---- CANARIS-E             32.00  -12.00     0 Munizip al-Dschabal al-Gharbi
W3409 ---- CANARIS-NE            34.00   -9.00     0 
W3602 ---- ALBORAN               36.02   -2.16     0 
W3604 ---- ALBORAN-W             35.45   -4.15     0 
W3607 ---- WESTL.GIBR.           36.00   -6.37     0 
W3609 ---- CABO S.VICENTE        36.29   -9.00     0 
W3701 ---- SDL.CARTAGENA         37.00   -1.15     0 
W3811 ---- WESTL.LISSABON        38.01  -11.20     0 
W4010 ---- WESTL.PORT.           39.33  -10.25     0 
W4211 ---- SDL.FINISTERRE        41.32  -10.52     0 
W4402 ---- GOLF BIARRITZ         44.00   -2.12     0 
W4410 ---- FINISTERRE            43.31   -9.49     0 Galicien
W4504 ---- SUDGASCOGNE           45.00   -3.31     0 
W4505 ---- NDL.GIJON             44.36   -5.08     0 
W4606 ---- BISKAYA               46.22   -5.41     0 
W4703 ---- NORDGASCOGNE          46.37   -3.24     0 
W4807 ---- SOLE                  48.00   -7.00     0 
W5001 ---- ENGL.KAN.-E           49.58   -1.13     0 
W5003 ---- LYME BAY              50.15   -3.00     0 
W5004 ---- ENGL.KAN.-W           49.34   -4.04     0 
W5011 ---- FASTNET               50.27  -10.33     0 Thüringen
W5105 ---- LUNDY                 51.29   -4.31     0 Wales
W5108 ---- SUEDL.IRL.            50.52   -7.44     0 
W5306 ---- IRISCHE SEE           53.15   -5.38     0 Wales
W5501 ---- TYNE                  55.00   -0.45     0 
W5506 ---- NORTH CHANNEL         55.15   -5.31     0 Schottland
W5602 ---- FORTH                 56.29   -1.31     0 
W5607 ---- INISHTRAHULL          55.36   -7.00     0 
W5611 ---- NWL.IRLAND            55.56  -10.53     0 
W5708 ---- SDL.HEBRIDEN          56.31   -7.50     0 Schottland
W5802 ---- CROMARTY              58.12   -2.00     0 
W5808 ---- HEBRIDEN              57.56   -8.09     0 
W5906 ---- NDL.HEBRIDEN          58.44   -5.35     0 
W6003 ---- PENTLANDS             59.41   -3.07     0 
W6006 ---- FAROER                60.25   -5.34     0 
W6010 ---- 60NORD10WEST          59.53  -10.02     0 Viken
W6102 ---- SHETLANDS             60.53   -1.35     0 
E2935 ---- GOLF AKABA-N          29.15   34.50     0 
E3231 ---- PORT-SAID             32.02   31.13     0 
E3234 ---- ISRAEL                31.51   34.16     0 
E3328 ---- SE-KRITIKO            33.00   27.31     0 
E3331 ---- DELTA                 33.07   31.21     0 
E3420 ---- SW-KRITIKO            34.10   20.20     0 
E3424 ---- SUEDL.KRETA           34.02   23.40     0 
E3512 ---- OESTL.DJERBA          35.00   11.30     0 
E3514 ---- MELITA-SE             35.00   13.30     0 
E3517 ---- SIDRA                 34.37   16.41     0 
E3519 ---- OESTL.TUNIS           34.51   18.41     0 
E3526 ---- KRETA-SE              34.35   26.10     0 
E3530 ---- RHODOS/ZYP.           34.58   30.25     0 
E3534 ---- CRUSADE-N             35.17   34.28     0 
E3613 ---- TUNIS                 36.11   12.34     0 
E3623 ---- KITHIRASEE            35.42   22.31     0 
E3624 ---- WEST CRETAN           36.00   24.29     0 
E3625 ---- AEGAEIS-S.            36.16   25.27     0 
E3627 ---- KARPATHIO             36.02   26.41     0 
E3629 ---- KASTELORIZO           35.34   28.30     0 
E3631 ---- TAURUS-W              36.29   30.56     0 
E3634 ---- TAURUS-E              36.00   34.00     0 
E3700 ---- PALOS                 37.00    0.00     0 
E3701 ---- CABRERA-W             37.28    1.14     0 
E3703 ---- ALGER-W               37.15    3.15     0 
E3712 ---- PANTELLERIA           37.00   12.00     0 
E3719 ---- ION.MEER              37.22   19.10     0 
E3721 ---- S-IONIANSEA           37.10   21.02     0 
E3724 ---- AEGAEIS-SW.           37.00   24.00     0 
E3727 ---- KOS                   37.00   27.00     0 Decentralized Administration of the Aegean
E3803 ---- CABRERA               38.29    3.00     0 
E3805 ---- ALGIER                37.47    4.59     0 
E3807 ---- ANNABA                37.57    7.10     0 
E3809 ---- SUEDL.SARD.           37.57    9.22     0 
E3811 ---- TUNISIE-E             38.00   11.10     0 
E3817 ---- BOOT-S                37.39   17.08     0 
E3825 ---- CENTRAL AEGEAN        38.00   25.00     0 
E3826 ---- SAMOSSEE              37.54   26.12     0 
E3901 ---- BALEARES-SW           39.01    0.56     0 
E3904 ---- BALEAREN              39.26    3.40     0 
E3905 ---- CABRERA-E             39.24    5.01     0 
E3915 ---- LIPARI-SE             38.31   15.00     0 
E3918 ---- BOOT                  38.48   18.00     0 
E3920 ---- ION.MEER-N.           39.00   19.31     0 
E3925 ---- AEGAEIS-N.            39.00   25.16     0 
E4007 ---- SARDAIGNE-S           39.31    7.29     0 
E4011 ---- CARBONARA             39.34   11.13     0 
E4013 ---- CIRCEO-S              40.15   13.00     0 
E4014 ---- LIPARI                39.31   14.00     0 
E4023 ---- AEGAEIS-NW.           39.45   23.00     0 
E4026 ---- THRAKICO              40.15   26.00     0 
E4028 ---- MARMARA               40.29   28.29     0 
E4103 ---- BALEARES-NE           40.48    2.43     0 
E4104 ---- MINORQUE              40.31    4.00     0 
E4107 ---- WESTL.KOR/S           41.25    6.57     0 
E4111 ---- TYRRH.MEER            41.28   10.31     0 
E4119 ---- STR.OTRANTO           40.45   19.00     0 
E4204 ---- GOLFE-LION            42.10    4.28     0 
E4208 ---- CORSE                 41.31    8.15     0 
E4212 ---- CIRCEO-N              41.31   12.00     0 
E4216 ---- NDL.BARI              42.00   16.29     0 
E4218 ---- ADRIA-SUED            41.58   17.46     0 
E4229 ---- SCHW.MEER1            41.52   28.51     0 
E4236 ---- SCHW.MEER7            42.00   36.00     0 
E4304 ---- LION                  42.31    3.45     0 
E4307 ---- SDL.PROVENCE          42.45    6.31     0 
E4309 ---- LIGUR.MEER            43.16    9.17     0 
E4310 ---- ELBA                  42.45   10.00     0 
E4316 ---- ZENTR.ADRIA           43.00   15.31     0 
E4329 ---- SCHW.MEER2            42.43   29.14     0 
E4413 ---- ADRIA-NORD            44.07   13.05     0 
E4414 ---- OESTL.ANCONA          43.30   14.12     0 
E4430 ---- SCHW.MEER3            43.34   29.39     0 
E4435 ---- SCHW.MEER6            43.51   35.15     0 
E4513 ---- GOLF-VENEDIG          45.00   13.00     0 
E4514 ---- SDL.PULA              44.31   14.00     0 
E4515 ---- RAB                   44.36   14.30     0 
E4531 ---- SCHW.MEER4            45.16   30.32     0 
E4637 ---- SCHW.MEER5            46.19   36.58     0 
E5000 ---- STR.DOVER             50.29    0.29     0 
E5101 ---- THEMSE                51.14    1.29     0 
E5203 ---- RHEINMUENDG.          52.00    3.00     0 
E5204 ---- IJMUIDEN              52.31    3.31     0 
E5303 ---- HUMBER                53.16    2.36     0 
E5304 ---- NORDSEE1              53.49    4.33     0 
E5305 ---- IJSSELMEER            52.42    5.24     0 
E5307 ---- OSTFR. KUESTE         53.45    7.00     0 
E5311 ---- LUEB. BUCHT           54.06   11.12     0 
E5312 ---- NDL.POEL              54.15   11.45     0 
E5344 ---- BALTRUM               53.44    7.23     0 Niedersachsen
E5401 ---- HUMBER-W              53.31    1.00     0 
E5403 ---- DOGGER-SUED           54.00    3.00     0 
E5404 ---- NORDSEE2              54.35    4.18     0 
E5405 ---- WESTFR.KUESTE         53.50    5.15     0 
E5406 ---- DT.BUCHT              54.26    5.42     0 
E5407 ---- POS.FPN               54.29    7.22     0 
E5408 ---- WANGEROOGE            53.56    7.46     0 
E5409 ---- ELBEMUENDUNG          54.00    8.06     0 
E5411 ---- KIELER BUCHT          54.31   10.43     0 
E5412 ---- WESTL.OSTS.           54.29   12.23     0 
E5413 ---- WESTL.RUEGEN          54.34   13.00     0 
E5414 ---- BODDENGEW. OST        54.18   14.00     0 
E5416 ---- SUEDL.OSTS.           54.22   15.43     0 
E5502 ---- DOGGER                55.11    2.10     0 
E5504 ---- ENTENSCHN.            55.19    3.52     0 
E5506 ---- NORDSEE3              55.30    5.58     0 
E5507 ---- NORDW.SYLT            55.28    7.17     0 
E5508 ---- NORDFR.KUE.           54.42    8.00     0 
E5510 ---- FLENSB.FOER.          54.48   10.12     0 
E5511 ---- BELTE/SUND            55.30   10.44     0 
E5512 ---- FEHMARNBELT           54.36   11.18     0 
E5513 ---- NDL.RUEGEN            55.00   13.24     0 
E5517 ---- OESTL.BORNHOLM        55.29   16.31     0 
E5519 ---- NDL.DANZIG            55.12   19.00     0 
E5543 ---- ISET-MEER22           54.37   12.38     0 
E5606 ---- FISCHER-SUED          56.29    6.15     0 
E5611 ---- KATTEGAT              56.29   10.46     0 Region Midtjylland
E5612 ---- NDL.MOEN              55.12   12.45     0 
E5613 ---- KATTEGAT-S            56.00   11.42     0 
E5614 ---- HANOE-BUCHT-W         55.30   14.29     0 
E5615 ---- NDL.BORNHOLM          55.45   15.15     0 
E5616 ---- KALMAR-SUND-S         56.12   16.12     0 
E5618 ---- SE-OSTSEE             56.11   17.50     0 
E5620 ---- WESTL.KLAIPEDA        56.00   20.00     0 
E5702 ---- FORTIES               57.08    1.40     0 
E5705 ---- FISCHER               57.22    5.17     0 
E5709 ---- SKAGERRAK             57.28    8.57     0 
E5711 ---- KATTTEGAT-N           57.15   11.29     0 
E5805 ---- UTSIRA-SUED           58.21    5.08     0 
E5807 ---- KAP LINDESNES         58.00    6.42     0 Agder
E5810 ---- NWL.SKAGEN            58.12   10.00     0 
E5811 ---- SKAGERRAK-E           58.00   11.00     0 
E5818 ---- WESTL.GOTLAND         57.31   17.31     0 
E5820 ---- ZENTR.OSTS.           57.58   20.11     0 
E5824 ---- RIGAI.MEERB.          57.45   23.30     0 
E5902 ---- VIKING-S              58.45    1.31     0 
E5910 ---- OSLOFJORD             58.45   10.29     0 
E5917 ---- SDL.STOCKHOLM         58.30   17.29     0 
E5919 ---- OESTL.STOCKHOLM       59.00   19.00     0 
E5922 ---- WESTL.OESEL           58.45   21.31     0 
E6001 ---- VIKING                60.05    0.47     0 
E6005 ---- UTSIRA-NORD           60.20    4.47     0 Vestland
E6019 ---- SDL.ALAND             59.42   17.18     0 Uppsala län
E6021 ---- NOERDL.OSTS.          59.56   20.54     0 Åländer Schären
E6024 ---- FINN.MEERB.-W         59.36   24.00     0 
E6026 ---- FINN.MEERB.           60.00   26.00     0 
E6104 ---- UTVAR                 61.00    4.00     0 
E6118 ---- BOTTENSEE-SW          61.00   17.36     0 
E6120 ---- ALANDSEE              60.45   19.31     0 
E6131 ---- LADOGA SEE            61.00   31.30     0 Republik Karelien
E7708 ---- GLOBAL1               54.30    6.22     0 
A338  ---- BREKENDORFER MOOR     54.25    9.36    25 Schleswig-Holstein
A492  ---- OLDENBURG I.H.        54.16   10.53     0 Schleswig-Holstein
A512  ---- HEIDE                 54.10    9.04     9 Schleswig-Holstein
A652  ---- PADENSTEDT            54.02    9.55    15 Schleswig-Holstein
B335  ---- KAVELSDORF            54.00   12.13    40 Mecklenburg-Vorpommern
B742  ---- LINSTOW               53.37   12.23    62 Mecklenburg-Vorpommern
C316  ---- MARMSTORF             53.26    9.56    75 Hamburg
E136  ---- ZETEL                 53.27    8.01     3 Niedersachsen
E267  ---- BOCKEL                53.12    9.18    26 Niedersachsen
E402  ---- DOERPEN               52.58    7.19     8 Niedersachsen
E427  ---- AHLHORN               52.54    8.10    40 Niedersachsen
E460  ---- VORM WITZENBRUCH      52.59    9.54    73 Niedersachsen
E482  ---- HOHENZETHEN           53.03   10.50    79 Niedersachsen
E653  ---- WIETZEN               52.43    9.05    55 Niedersachsen
E726  ---- NEMDEN                52.13    8.12   130 Niedersachsen
E735  ---- HATTENDORF            52.14    9.16   200 Niedersachsen
E777  ---- WATENSTEDT            52.09   10.22   103 Niedersachsen
E790  ---- WOLFSBURG (SUEDWEST)  52.24   10.41    82 Niedersachsen
E798  ---- HELMSTEDT             52.15   10.58   110 Niedersachsen
E877  ---- CLAUSTHAL-ZELLERFELD  51.47   10.21   585 Niedersachsen
E885  ---- WESTERODE             51.54   10.33   205 Niedersachsen
E923  ---- SCHLOCHAU             51.43    9.56   145 Niedersachsen
E972  ---- MOLLENFELDE           51.25    9.51   265 Niedersachsen
F136  ---- KARSTEDTSHOF          53.06   12.29    70 Brandenburg
F283  ---- JOACHIMSTHAL          52.57   13.49    70 Brandenburg
F461  ---- RUEDERSDORF           52.28   13.46    50 Brandenburg
F537  ---- FAHLHORST             52.18   13.11    35 Brandenburg
F618  ---- FLAEMING              52.02   12.36   110 Brandenburg
F863  ---- HAENCHEN              51.43   14.16    69 Brandenburg
F945  ---- RUHLAND               51.28   13.52   110 Brandenburg
H069  ---- LADBERGEN             52.07    7.42    55 Nordrhein-Westfalen
H075  ---- HABICHTSWALD          52.14    7.52   130 Nordrhein-Westfalen
H097  ---- STEINEGGE-EXTER       52.09    8.48   201 Nordrhein-Westfalen
H228  ---- KALTENBACH            51.47    6.58    64 Nordrhein-Westfalen
H267  ---- BECKUMER BERG         51.47    8.03   142 Nordrhein-Westfalen
H308  ---- SONSBECK              51.36    6.21    25 Nordrhein-Westfalen
H379  ---- LOHME-ALME            51.38    8.44   163 Nordrhein-Westfalen
H423  ---- ALTENESSEN            51.30    6.58    46 Nordrhein-Westfalen
H456  ---- OSTOENNER BACH        51.32    7.59   135 Nordrhein-Westfalen
H483  ---- OTTENSGRUND           51.34    8.45   350 Nordrhein-Westfalen
H528  ---- HOLZBUETTGEN          51.13    6.39    39 Nordrhein-Westfalen
H545  ---- OBERBARMEN            51.19    7.16   299 Nordrhein-Westfalen
H554  ---- NAHMER                51.19    7.34   360 Nordrhein-Westfalen
H556  ---- ROELVEDER MUEHLE      51.17    7.36   410 Nordrhein-Westfalen
H605  ---- GUEDDERATH            51.08    6.26    50 Nordrhein-Westfalen
H642  ---- REMSCHEID-LENNEP      51.11    7.15   345 Nordrhein-Westfalen
H663  ---- SICHTER               51.09    7.41   530 Nordrhein-Westfalen
H744  ---- KOELN-STAMMHEIM       50.59    6.59    43 Nordrhein-Westfalen
H746  ---- MOITZFELD             50.58    7.11   133 Nordrhein-Westfalen
H775  ---- ECKENHAGEN            50.58    7.43   445 Nordrhein-Westfalen
H810  ---- KREUZ AACHEN          50.48    6.10   155 Nordrhein-Westfalen
H933  ---- WISSKIRCHEN           50.38    6.43   211 Nordrhein-Westfalen
H993  ---- BLANKENHEIM           50.28    6.42   550 Nordrhein-Westfalen
J721  ---- LOESTERBACH SUED      49.37    6.56   482 Rheinland-Pfalz
J907  ---- GOLDENE BREMM         49.13    6.58   224 Saarland
K040  ---- ESCH                  50.34    7.03   268 Rheinland-Pfalz
K100  ---- KLEIN-ALTENDORF       50.37    6.59   150 Nordrhein-Westfalen
K101  ---- STEINBORN             50.04    6.37   529 Rheinland-Pfalz
K130  ---- SINZIG                50.32    7.11   206 Rheinland-Pfalz
K164  ---- KANNENBAECKER LAND    50.27    7.44   300 Rheinland-Pfalz
K169  ---- GRENZAU               50.27    7.39   300 Rheinland-Pfalz
K250  ---- MAYEN                 50.19    7.14   275 Rheinland-Pfalz
K265  ---- OCHTENDUNG            50.20    7.25   314 Rheinland-Pfalz
K266  ---- MOSELTALBRUECKE       50.19    7.29   204 Rheinland-Pfalz
K268  ---- MUENSTERMAIFELD       50.16    7.21   178 Rheinland-Pfalz
K315  ---- STRICKSCHEID          50.09    6.19   470 Rheinland-Pfalz
K341  ---- LAUBACHER HOEHE       50.14    7.04   564 Rheinland-Pfalz
K436  ---- WIERSDORF             50.00    6.27   296 Rheinland-Pfalz
K442  ---- DREIS-BRUECK          50.16    6.47   470 Rheinland-Pfalz
K445  ---- FLUSSBACH             50.01    6.56   331 Rheinland-Pfalz
K471  ---- SIMMERN-WAHLBACH      50.00    7.36   445 Rheinland-Pfalz
K480  ---- LAUDERT               50.05    7.37   530 Rheinland-Pfalz
K481  ---- WAHLBACH              50.00    7.35   436 Rheinland-Pfalz
K510  ---- MERZKIRCHEN           49.34    6.28   369 Rheinland-Pfalz
K560  ---- MEDDERSHEIM           49.47    7.37   150 Rheinland-Pfalz
K562  ---- WIESWEILER            49.38    7.35   180 Rheinland-Pfalz
K571  ---- BINGEN-GAULSHEIM      49.58    7.58    88 Rheinland-Pfalz
K582  ---- MAINZ (DLR)           49.58    8.14   153 Rheinland-Pfalz
K587  ---- WOERRSTADT            49.51    8.09   150 Rheinland-Pfalz
K588  ---- ROMMERSHEIM           49.49    8.07   238 Rheinland-Pfalz
K597  ---- NIERSTEIN             49.52    8.20   169 Rheinland-Pfalz
K598  ---- DIEMHEIM              49.51    8.19   202 Rheinland-Pfalz
K610  ---- AVELSBACH             49.45    6.42   248 Rheinland-Pfalz
K620  ---- KANZERN               49.40    6.35   216 Rheinland-Pfalz
K621  ---- WITTLICH              49.58    6.52   197 Rheinland-Pfalz
K623  ---- ZELTINGEN             49.57    7.02   212 Rheinland-Pfalz
K630  ---- DIENSTWEILER          49.38    7.12   461 Rheinland-Pfalz
K642  ---- NIEDERWOERSSESBACH    49.46    7.20   302 Rheinland-Pfalz
K670  ---- PLEISWEILER-OBERHOFE  49.07    8.01   197 Rheinland-Pfalz
K672  ---- SCHWEIGHOFEN          49.02    7.59   159 Rheinland-Pfalz
K677  ---- FREIMERSHEIM          49.43    8.04   270 Rheinland-Pfalz
K695  ---- EICH                  49.45    8.23    89 Rheinland-Pfalz
K732  ---- HAHNWEILER            49.35    7.14   536 Rheinland-Pfalz
K768  ---- SCHORLENBERG          49.28    7.55   412 Rheinland-Pfalz
K787  ---- LEINIGER BERG         49.32    8.07   292 Rheinland-Pfalz
K795  ---- FRANKENTHAL           49.33    8.21    95 Rheinland-Pfalz
K862  ---- MORLAUTERN            49.28    7.46   320 Rheinland-Pfalz
K880  ---- HERXHEIMWEYHER        49.10    8.15   144 Rheinland-Pfalz
K882  ---- STEINWEILER           49.07    8.07   132 Rheinland-Pfalz
K886  ---- WEIERHOF              49.38    8.02   194 Rheinland-Pfalz
K887  ---- NEUSTADT/WEINSTRASSE  49.22    8.12   141 Rheinland-Pfalz
K892  ---- SCHIFFERSTADT         49.25    8.21   102 Rheinland-Pfalz
K963  ---- LUSTADT               49.15    8.17   116 Rheinland-Pfalz
L112  ---- VASBECK               51.23    8.54   340 Hessen
L119  ---- HOF LAUTERBACH, VOEH  51.13    8.56   350 Hessen
L160  ---- LUTTERBERG            51.22    9.38   395 Niedersachsen
L242  ---- AM SCHARFENSTEIN      51.11    9.24   245 Hessen
L267  ---- ALHEIM                51.03    9.42   281 Hessen
L282  ---- OBERHONE              51.10   10.00   180 Hessen
L283  ---- DOMAENE VOGELSBURG    51.09   10.01   220 Hessen
L284  ---- HESSENRING            51.11   10.02   238 Hessen
L353  ---- ALSFELD               50.45    9.15   304 Hessen
L379  ---- EICHHOF               50.50    9.41   200 Hessen
L414  ---- HAIGER                50.45    8.13   320 Hessen
L474  ---- RIMBERG               50.48    9.29   490 Hessen
L542  ---- HOMBERG-OHM           50.39    9.00   330 Hessen
L585  ---- FULDA                 50.32    9.41   255 Hessen
L637  ---- T/R WETTERAU          50.21    8.42   250 Hessen
L641  ---- ECHZELL SCHWALHEIM    50.24    8.54   130 Hessen
L648  ---- ALTENSTADT            50.19    8.56   184 Hessen
L684  ---- THALAUBACH            50.26    9.45   370 Hessen
L687  ---- FORSTHAUS             50.23    9.44   475 Hessen
L716  ---- IDSTEIN               50.13    8.15   365 Hessen
L838  ---- FRANKFURT             50.05    8.35    97 Hessen
L841  ---- FRANKFURT WESTEND     50.08    8.40   124 Hessen
L857  ---- WALDSCHNEISE HANAU    50.02    8.56   125 Hessen
L858  ---- MARKOEBEL             50.14    8.57   156 Hessen
L889  ---- ROSSDORF DARMSTADT    49.51    8.47   180 Hessen
L912  ---- ALLMENDFELD           49.46    8.31    90 Hessen
L959  ---- RHEINBR.MANNHEIM      49.32    8.25   100 Rheinland-Pfalz
L962  ---- HEPPENHEIM            49.38    8.37    95 Hessen
L985  ---- BUCHHALDE             49.34    8.58   430 Hessen
M403  ---- HOERSCHEL             51.01   10.13   300 Thüringen
M524  ---- BOXBERG               50.53   10.39   348 Thüringen
M575  ---- GERAER BERG           50.54   12.02   305 Thüringen
M774  ---- LEUBSDORF             50.42   11.51   420 Thüringen
M888  ---- SCHLEIZ               50.33   11.47   528 Thüringen
N013  ---- ROSSLA                51.30   11.20   100 Sachsen-Anhalt
N443  ---- IRXLEBEN              52.11   11.27   122 Sachsen-Anhalt
N567  ---- VOCKERODE             51.52   12.21    70 Sachsen-Anhalt
N642  ---- PLOETZKAU/SAALE       51.43   11.41    95 Sachsen-Anhalt
N793  ---- ZOERBIG               51.36   12.11    97 Sachsen-Anhalt
N891  ---- ELSTER-SAALE-KANAL    51.21   12.11   115 Sachsen-Anhalt
N992  ---- OSTERFELD             51.01   11.56   298 Thüringen
O013  ---- BERBERSDORF           50.40   12.50   300 Sachsen
O215  ---- WALDSTEINBERG         51.18   12.35   136 Sachsen
O252  ---- SCHOENBORN            51.19   13.43   174 Sachsen
O372  ---- BURKAUER BERG         51.10   14.07   328 Sachsen
O451  ---- DRESDEN-PILLNITZ      51.00   13.53   115 Sachsen
O454  ---- DRESDEN/FLUGHAFEN     51.09   13.54   220 Sachsen
O459  ---- ZELLWALD              51.02   13.16   301 Sachsen
O862  ---- MARIENHOEHE           50.36   12.23   486 Sachsen
O863  ---- AUE                   50.35   12.43   387 Sachsen
O951  ---- HEINERSGRUEN          50.24   11.59   561 Sachsen
P017  ---- OBERTHULBA            50.12    9.56   320 Bayern
P082  ---- SAALEBRUECKE          50.21   11.52   464 Bayern
P101  ---- KAHL                  50.04    9.01   116 Bayern
P116  ---- HASELTAL              49.53    9.26   420 Bayern
P134  ---- SCHWEINFURT           50.01   10.13   214 Bayern
P159  ---- HIRSCHAID             49.49   11.01   268 Bayern
P166  ---- THURNAU               50.01   11.21   498 Bayern
P235  ---- BUERGSTADT            49.42    9.17   210 Bayern
P254  ---- RANDERSACKER          49.45    9.59   185 Bayern
P264  ---- ROEDELSEE             49.43   10.15   240 Bayern
P267  ---- HIENBERG              49.36   11.22   539 Bayern
P289  ---- NAABBRUECKE           49.35   12.08   391 Bayern
P291  ---- WALDNAAB              49.47   12.10   458 Bayern
P332  ---- ZOLLHAUS              49.24   11.07   346 Bayern
P353  ---- VILSTAL               49.24   11.54   397 Bayern
P401  ---- ZUMHAUS               49.13   10.15   462 Bayern
P438  ---- GELBELSEE             48.57   11.26   521 Bayern
P452  ---- TB EICHELBERG         49.12   12.07   415 Bayern
P533  ---- KOESCHINGER FORST     48.51   11.27   450 Bayern
P547  ---- SIEGENBURG            48.42   11.48   400 Bayern
P555  ---- MALLERSDORF-PFB       48.47   12.11   404 Bayern
P573  ---- DEGGENAU              48.48   12.58   320 Bayern
P575  ---- NEUSLING              48.42   12.54   345 Bayern
P589  ---- GALGENBERG            48.38   13.18   510 Bayern
P632  ---- HOLLEDAU SUED         48.33   11.36   477 Bayern
P738  ---- SCHOEFFELDING         48.04   10.58   650 Bayern
P748  ---- OBERPFAFFENHOFEN      48.06   11.18   570 Bayern
P755  ---- ASCHHEIM              48.13   11.41   495 Bayern
P801  ---- MEMMINGEN             47.58   10.08   615 Bayern
P805  ---- ALLGAEUER TOR         47.52   10.17   720 Bayern
P866  ---- SEEHAMMER SEE         47.52   11.51   690 Bayern
P869  ---- DETTENDORF            47.49   12.00   500 Bayern
P878  ---- STREITHEIM            48.25   10.40   490 Bayern
P910  ---- HELLENGERST           47.40   10.12   947 Bayern
P912  ---- SULZBERG              47.41   10.19   730 Bayern
P941  ---- GROSSWEIL             47.40   11.15   680 Bayern
P977  ---- OBERAUDORF            47.40   12.11   470 Bayern
Q006  ---- SECKENHEIM            49.27    8.33   100 Baden-Württemberg
Q068  ---- HOLZSPITZE            49.27    9.33   370 Baden-Württemberg
Q208  ---- KARLSRUHE             49.00    8.27   170 Baden-Württemberg
Q241  ---- SULMTAL               49.10    9.15   180 Baden-Württemberg
Q247  ---- BESIGHEIM             48.59    9.11   300 Baden-Württemberg
Q290  ---- WOLFSKOPF             49.11   10.03   440 Baden-Württemberg
Q348  ---- ENGELBERG             48.48    9.02   450 Baden-Württemberg
Q441  ---- AK STUTTGART          48.43    9.05   500 Baden-Württemberg
Q444  ---- STUTTGART RWY4        48.40    9.11   363 Baden-Württemberg
Q561  ---- METZINGEN             48.32    9.16   362 Baden-Württemberg
Q585  ---- NW-HR09               48.31    9.45   710 Baden-Württemberg
Q597  ---- NW-HR02               48.28   10.04   550 Baden-Württemberg
Q740  ---- BALINGEN-BRONNHPTN.   48.16    8.49   619 Baden-Württemberg
Q848  ---- GEISINGEN             47.56    8.39   672 Baden-Württemberg
Q904  ---- DREIECK WEIL          47.37    7.35   240 Baden-Württemberg
Q988  ---- GRUB                  47.39    9.45   540 Baden-Württemberg
X001  ---- SWIS-PUNKT            51.10    9.30   160 Hessen
X002  ---- SWIS-PUNKT            50.10    6.40   300 Rheinland-Pfalz
X003  ---- SWIS-PUNKT            50.10    6.20   500 Rheinland-Pfalz
X004  ---- SWIS-PUNKT            51.20    7.40   700 Nordrhein-Westfalen
X005  ---- SWIS-PUNKT            51.00    7.10   100 Nordrhein-Westfalen
X006  ---- SWIS-PUNKT            51.00    7.20   300 Nordrhein-Westfalen
X007  ---- SWIS-PUNKT            51.00    7.30   500 Nordrhein-Westfalen
X008  ---- SWIS-PUNKT            48.31    9.45   900 Baden-Württemberg
X009  ---- SWIS-PUNKT            50.55    7.00   100 Nordrhein-Westfalen
X010  ---- SWIS-PUNKT            50.50    6.10   100 Nordrhein-Westfalen
X011  ---- SWIS-PUNKT            51.40   11.46   300 Sachsen-Anhalt
X012  ---- SWIS-PUNKT            50.40    6.40   100 Nordrhein-Westfalen
X013  ---- SWIS-PUNKT            50.45    7.50   500 Rheinland-Pfalz
X014  ---- SWIS-PUNKT            50.25    9.45   700 Hessen
X015  ---- SWIS-PUNKT            50.15    8.20   500 Hessen
X016  ---- SWIS-PUNKT            49.27    8.34   300 Baden-Württemberg
X017  ---- SWIS-PUNKT            49.10    9.15   300 Baden-Württemberg
X018  ---- SWIS-PUNKT            47.39    9.46   700 Baden-Württemberg
X019  ---- SWIS-PUNKT            48.30    8.08   300 Baden-Württemberg
X020  ---- SWIS-PUNKT            48.30    8.09   500 Baden-Württemberg
X021  ---- SWIS-PUNKT            48.30    8.10   700 Baden-Württemberg
X022  ---- SWIS-PUNKT            48.30    8.11   900 Baden-Württemberg
X023  ---- SWIS-PUNKT            48.30    8.12  1100 Baden-Württemberg
X024  ---- SWIS-PUNKT            50.20   10.00   700 Bayern
X025  ---- SWIS-PUNKT            50.15   11.40   700 Bayern
X026  ---- SWIS-PUNKT            53.20   13.40   100 Brandenburg
X027  ---- SWIS-PUNKT            49.30   12.38   700 Bayern
X028  ---- SWIS-PUNKT            51.15    9.50   700 Hessen
X029  ---- SWIS-PUNKT            47.45   12.45   900 Bayern
X030  ---- SWIS-PUNKT            47.45   12.30  1100 Bayern
X031  ---- SWIS-PUNKT            50.22   12.28   700 Sachsen
X032  ---- SWIS-PUNKT            52.30   11.30   100 Sachsen-Anhalt
X033  ---- SWIS-PUNKT            51.15   11.00   100 Thüringen
X034  ---- SWIS-PUNKT            51.40   12.40    90 Sachsen-Anhalt
X035  ---- SWIS-PUNKT            51.20   13.15    70 Sachsen
X036  ---- SWIS-PUNKT            51.40   10.31   900 Niedersachsen
X037  ---- SWIS-PUNKT            51.50   10.40   700 Sachsen-Anhalt
X038  ---- SWIS-PUNKT            49.50    7.10   700 Rheinland-Pfalz
X039  ---- SWIS-PUNKT            50.40   10.45   700 Thüringen
X040  ---- SWIS-PUNKT            50.30   11.00   900 Thüringen
X042  ---- SWIS-PUNKT            49.30    8.20   100 Rheinland-Pfalz
X043  ---- SWIS-PUNKT            50.15    7.50   300 Rheinland-Pfalz
X044  ---- SWIS-PUNKT            50.15    7.51   500 Rheinland-Pfalz
X045  ---- SWIS-PUNKT            52.30   13.20   100 Berlin
X046  ---- SWIS-PUNKT            51.30   11.20   300 Sachsen-Anhalt
X047  ---- SWIS-PUNKT            50.15    7.50   700 Rheinland-Pfalz
X048  ---- SWIS-PUNKT            50.40   10.22   275 Thüringen
X049  ---- SWIS-PUNKT            50.28   10.45   475 Thüringen
X050  ---- SWIS-PUNKT            53.50   13.30    50 Mecklenburg-Vorpommern
X051  ---- SWIS-PUNKT            51.30   11.21   500 Sachsen-Anhalt
X052  ---- SWIS-PUNKT            50.05    8.00   700 Hessen
X053  ---- SWIS-PUNKT            49.40    8.50   300 Hessen
X054  ---- SWIS-PUNKT            50.20   10.00   900 Bayern
X055  ---- SWIS-PUNKT            49.30   11.50   700 Bayern
X056  ---- SWIS-PUNKT            50.00   12.00   900 Bayern
X057  ---- SWIS-PUNKT            47.40   10.30  1000 Bayern
X058  ---- SWIS-PUNKT            49.30   12.30   900 Bayern
X059  ---- SWIS-PUNKT            49.00   13.09   900 Bayern
X060  ---- SWIS-PUNKT            49.00   13.10  1000 Bayern
X087  ---- SWIS-PUNKT            51.45   10.30   500 Niedersachsen
X088  ---- SWIS-PUNKT            51.40   10.30   700 Niedersachsen
X089  ---- SWIS-PUNKT            47.37    7.36   500 Baden-Württemberg
X090  ---- SWIS-PUNKT            49.40   10.30   500 Bayern
X091  ---- SWIS-PUNKT            50.10   11.40   300 Bayern
X093  ---- SWIS-PUNKT            49.02   13.18   700 Bayern
X095  ---- SWIS-PUNKT            50.25   12.30   700 Sachsen
X096  ---- SWIS-PUNKT            51.00   14.40   500 Sachsen
X097  ---- SWIS-PUNKT            51.47   10.40   900 Sachsen-Anhalt
X098  ---- SWIS-PUNKT            51.40   10.41  1100 Sachsen-Anhalt
X099  ---- SWIS-PUNKT            50.28   12.51   900 Sachsen
X100  ---- SWIS-PUNKT            51.40   12.40   100 Sachsen-Anhalt
X101  ---- SWIS-PUNKT            48.21   11.47   450 Bayern
X102  ---- SWIS-PUNKT            49.30   11.05   320 Bayern
X103  ---- SWIS-PUNKT            52.23   13.31    50 Brandenburg
X104  ---- SWIS-PUNKT            52.34   13.17    40 Berlin
X105  ---- SWIS-PUNKT            52.28   13.24    53 Berlin
X106  ---- SWIS-PUNKT            53.38    9.59    11 Hamburg
X107  ---- SWIS-PUNKT            53.03    8.47     3 Bremen
X109  ---- SWIS-PUNKT            52.08    7.41    51 Nordrhein-Westfalen
X110  ---- SWIS-PUNKT            51.17    6.45    39 Nordrhein-Westfalen
X111  ---- SWIS-PUNKT            50.52    7.09    84 Nordrhein-Westfalen
X112  ---- SWIS-PUNKT            49.13    7.07   351 Saarland
X113  ---- SWIS-PUNKT            50.58   10.57   344 Thüringen
X114  ---- SWIS-PUNKT            50.02    8.34   109 Hessen
X115  ---- SWIS-PUNKT            51.45    9.34   500 Niedersachsen
X116  ---- SWIS-PUNKT            50.31    2.37    28 Hauts-de-France
X117  EDAC SWIS-PUNKT            50.59   12.30   209 Thüringen
X118  EDMA SWIS-PUNKT            48.25   10.56   504 Bayern
X119  EDQD SWIS-PUNKT            49.59   11.38   530 Bayern
X120  EDVE SWIS-PUNKT            52.19   10.33    92 Niedersachsen
X121  EDWB SWIS-PUNKT            53.30    8.34     3 Niedersachsen
X122  EDBC SWIS-PUNKT            51.51   11.25   198 Sachsen-Anhalt
X123  EDTD SWIS-PUNKT            47.58    8.31   742 Baden-Württemberg
X124  EDLW SWIS-PUNKT            51.31    7.37   135 Nordrhein-Westfalen
X125  EDFE SWIS-PUNKT            49.58    8.39   128 Hessen
X126  EDWE SWIS-PUNKT            53.23    7.13     0 Niedersachsen
X127  EDNY SWIS-PUNKT            47.40    9.31   449 Baden-Württemberg
X128  EDFH SWIS-PUNKT            49.57    7.16   548 Rheinland-Pfalz
X129  EDHI SWIS-PUNKT            53.32    9.50     3 Hamburg
X130  EDAH SWIS-PUNKT            53.53   14.09    24 Mecklenburg-Vorpommern
X131  EDQM SWIS-PUNKT            50.17   11.51   640 Bayern
X132  EDSB SWIS-PUNKT            48.47    8.05   136 Baden-Württemberg
X133  EDVK SWIS-PUNKT            51.24    9.22   302 Hessen
X134  EDHK SWIS-PUNKT            54.23   10.09    33 Schleswig-Holstein
X135  EDTL SWIS-PUNKT            48.22    7.50   169 Baden-Württemberg
X136  EDWD SWIS-PUNKT            53.09    8.37    67 Niedersachsen
X137  EDHL SWIS-PUNKT            53.48   10.43    17 Schleswig-Holstein
X138  EDBM SWIS-PUNKT            52.04   11.38    89 Sachsen-Anhalt
X139  EDFM SWIS-PUNKT            49.28    8.31   103 Baden-Württemberg
X140  EDLN SWIS-PUNKT            51.14    6.30    41 Nordrhein-Westfalen
X141  EDLV SWIS-PUNKT            51.36    6.08    35 Nordrhein-Westfalen
X142  EDMO SWIS-PUNKT            48.05   11.17   635 Bayern
X143  EDLP SWIS-PUNKT            51.37    8.37   232 Nordrhein-Westfalen
X144  ETNL SWIS-PUNKT            53.55   12.17    46 Mecklenburg-Vorpommern
X145  EDTY SWIS-PUNKT            49.07    9.47   436 Baden-Württemberg
X146  EDOP SWIS-PUNKT            53.25   11.47    50 Mecklenburg-Vorpommern
X147  EDGS SWIS-PUNKT            50.43    8.05   651 Nordrhein-Westfalen
X148  EDMS SWIS-PUNKT            48.54   12.31   349 Bayern
X149  EDXW SWIS-PUNKT            54.54    8.20     8 Schleswig-Holstein
X150  EDWI SWIS-PUNKT            53.30    8.03     5 Niedersachsen
X151  EDRZ SWIS-PUNKT            49.13    7.24   377 Rheinland-Pfalz
X200  ---- SWIS-PUNKT            47.34    9.59   900 Bayern
X201  ---- SWIS-PUNKT            47.21   10.20   900 Bayern
X202  ---- SWIS-PUNKT            47.40   10.52   900 Bayern
X203  ---- SWIS-PUNKT            47.33   10.22  1100 Bayern
X204  ---- SWIS-PUNKT            47.35   10.53  1100 Bayern
X205  ---- SWIS-PUNKT            47.32   11.13  1100 Bayern
X206  ---- SWIS-PUNKT            47.39   11.20   500 Bayern
X207  ---- SWIS-PUNKT            47.46   12.27   500 Bayern
X208  ---- SWIS-PUNKT            47.35   11.20   900 Bayern
X209  ---- SWIS-PUNKT            47.46   12.22   900 Bayern
X210  ---- SWIS-PUNKT            47.39   13.00   900 Bayern
X211  ---- SWIS-PUNKT            47.39   11.28  1100 Bayern
X212  ---- SWIS-PUNKT            47.45   12.21  1100 Bayern
X213  ---- SWIS-PUNKT            47.32   13.00  1100 Bayern
X214  ---- SWIS-PUNKT            47.54   11.22   700 Bayern
X215  ---- SWIS-PUNKT            48.40   10.47   300 Bayern
X216  ---- SWIS-PUNKT            49.35   10.56   500 Bayern
X217  ---- SWIS-PUNKT            48.50   11.08   500 Bayern
X218  ---- SWIS-PUNKT            48.55   11.31   500 Bayern
X219  ---- SWIS-PUNKT            47.58   12.21   700 Bayern
X220  ---- SWIS-PUNKT            47.51   12.40   700 Bayern
X221  ---- SWIS-PUNKT            48.34   12.43   300 Bayern
X222  ---- SWIS-PUNKT            48.44   11.57   500 Bayern
X223  ---- SWIS-PUNKT            48.34   12.43   500 Bayern
X224  ---- SWIS-PUNKT            48.59   10.46   700 Bayern
X225  ---- SWIS-PUNKT            49.02   11.04   700 Bayern
X226  ---- SWIS-PUNKT            49.25   11.39   700 Bayern
X227  ---- SWIS-PUNKT            49.29   12.01   700 Bayern
X228  ---- SWIS-PUNKT            47.57    8.59   700 Baden-Württemberg
X229  ---- SWIS-PUNKT            48.44    9.57   700 Baden-Württemberg
X230  ---- SWIS-PUNKT            47.58    8.41   900 Baden-Württemberg
X231  ---- SWIS-PUNKT            48.15    9.05   900 Baden-Württemberg
X232  ---- SWIS-PUNKT            48.30    9.34   900 Baden-Württemberg
X233  ---- SWIS-PUNKT            48.06    9.23   500 Baden-Württemberg
X234  ---- SWIS-PUNKT            49.32   10.43   300 Bayern
X235  ---- SWIS-PUNKT            49.15   10.53   500 Bayern
X236  ---- SWIS-PUNKT            49.36   11.57   500 Bayern
X237  ---- SWIS-PUNKT            49.44   12.05   500 Bayern
X238  ---- SWIS-PUNKT            49.43    9.30   300 Baden-Württemberg
X239  ---- SWIS-PUNKT            49.21    8.48   100 Baden-Württemberg
X240  ---- SWIS-PUNKT            49.21    8.56   300 Baden-Württemberg
X241  ---- SWIS-PUNKT            48.29    8.53   500 Baden-Württemberg
X242  ---- SWIS-PUNKT            48.55    9.46   500 Baden-Württemberg
X243  ---- SWIS-PUNKT            49.54    9.43   300 Bayern
X244  ---- SWIS-PUNKT            50.14   10.26   500 Bayern
X245  ---- SWIS-PUNKT            50.00   10.39   500 Bayern
X246  ---- SWIS-PUNKT            49.52   10.29   500 Bayern
X247  ---- SWIS-PUNKT            49.36   10.18   500 Bayern
X248  ---- SWIS-PUNKT            49.59    9.02   100 Bayern
X249  ---- SWIS-PUNKT            50.00    9.15   100 Bayern
X250  ---- SWIS-PUNKT            49.52    9.14   300 Bayern
X251  ---- SWIS-PUNKT            50.23   10.11   300 Bayern
X252  ---- SWIS-PUNKT            50.28   10.14   300 Bayern
X253  ---- SWIS-PUNKT            49.37    9.05   500 Bayern
X254  ---- SWIS-PUNKT            50.20    9.45   500 Bayern
X255  ---- SWIS-PUNKT            50.31   10.11   500 Bayern
X256  ---- SWIS-PUNKT            50.21    9.49   700 Bayern
X257  ---- SWIS-PUNKT            50.19    9.53   700 Bayern
X258  ---- SWIS-PUNKT            50.29   10.04   700 Bayern
X259  ---- SWIS-PUNKT            50.31   10.05   700 Bayern
X260  ---- SWIS-PUNKT            50.19    9.54   900 Bayern
X261  ---- SWIS-PUNKT            50.22    9.57   900 Bayern
X262  ---- SWIS-PUNKT            50.30   10.03   900 Bayern
X263  ---- SWIS-PUNKT            50.31   10.04   900 Bayern
X264  ---- SWIS-PUNKT            49.49    8.44   300 Hessen
X265  ---- SWIS-PUNKT            49.35    8.46   300 Hessen
X266  ---- SWIS-PUNKT            49.50    8.59   300 Hessen
X267  ---- SWIS-PUNKT            49.42    8.47   500 Hessen
X268  ---- SWIS-PUNKT            49.35    8.48   500 Hessen
X269  ---- SWIS-PUNKT            49.39    9.04   500 Hessen
X270  ---- SWIS-PUNKT            49.40    8.54   500 Hessen
X271  ---- SWIS-PUNKT            48.48    8.28   500 Baden-Württemberg
X272  ---- SWIS-PUNKT            48.12    8.04   500 Baden-Württemberg
X273  ---- SWIS-PUNKT            47.50    7.47   500 Baden-Württemberg
X274  ---- SWIS-PUNKT            48.44    8.38   700 Baden-Württemberg
X275  ---- SWIS-PUNKT            48.14    8.26   700 Baden-Württemberg
X276  ---- SWIS-PUNKT            48.41    8.25   900 Baden-Württemberg
X277  ---- SWIS-PUNKT            47.48    7.48   900 Baden-Württemberg
X278  ---- SWIS-PUNKT            47.47    7.46  1100 Baden-Württemberg
X279  ---- SWIS-PUNKT            47.47    8.09  1100 Baden-Württemberg
X280  ---- SWIS-PUNKT            48.05    8.09  1100 Baden-Württemberg
X281  ---- SWIS-PUNKT            47.34    7.44   300 Baden-Württemberg
X282  ---- SWIS-PUNKT            47.37    8.19   300 Baden-Württemberg
X283  ---- SWIS-PUNKT            47.37    7.50   500 Baden-Württemberg
X284  ---- SWIS-PUNKT            49.07    7.56   300 Rheinland-Pfalz
X285  ---- SWIS-PUNKT            49.17    8.02   500 Rheinland-Pfalz
X286  ---- SWIS-PUNKT            49.09    7.35   500 Rheinland-Pfalz
X287  ---- SWIS-PUNKT            49.28    6.32   300 Saarland
X288  ---- SWIS-PUNKT            49.32    6.44   500 Saarland
X289  ---- SWIS-PUNKT            49.35    6.58   500 Saarland
X290  ---- SWIS-PUNKT            49.32    7.02   500 Saarland
X291  ---- SWIS-PUNKT            49.53    8.04   300 Rheinland-Pfalz
X292  ---- SWIS-PUNKT            49.44    7.39   300 Rheinland-Pfalz
X293  ---- SWIS-PUNKT            49.37    7.16   500 Rheinland-Pfalz
X294  ---- SWIS-PUNKT            49.39    7.27   500 Rheinland-Pfalz
X295  ---- SWIS-PUNKT            49.33    7.32   500 Rheinland-Pfalz
X296  ---- SWIS-PUNKT            49.37    7.55   500 Rheinland-Pfalz
X297  ---- SWIS-PUNKT            47.45    7.36   300 Baden-Württemberg
X298  ---- SWIS-PUNKT            50.10    7.34   500 Rheinland-Pfalz
X299  ---- SWIS-PUNKT            49.40    6.49   700 Rheinland-Pfalz
X300  ---- SWIS-PUNKT            49.40    7.01   700 Rheinland-Pfalz
X301  ---- SWIS-PUNKT            49.55    7.36   700 Rheinland-Pfalz
X302  ---- SWIS-PUNKT            49.43    7.08   700 Rheinland-Pfalz
X303  ---- SWIS-PUNKT            50.25    7.04   500 Rheinland-Pfalz
X304  ---- SWIS-PUNKT            50.42    6.29   300 Nordrhein-Westfalen
X305  ---- SWIS-PUNKT            50.38    6.33   300 Nordrhein-Westfalen
X306  ---- SWIS-PUNKT            50.32    6.20   500 Nordrhein-Westfalen
X307  ---- SWIS-PUNKT            50.35    6.29   500 Nordrhein-Westfalen
X308  ---- SWIS-PUNKT            50.34    7.12   100 Rheinland-Pfalz
X309  ---- SWIS-PUNKT            50.17    7.41   300 Rheinland-Pfalz
X310  ---- SWIS-PUNKT            50.18    8.00   300 Rheinland-Pfalz
X311  ---- SWIS-PUNKT            50.14    7.56   500 Rheinland-Pfalz
X312  ---- SWIS-PUNKT            50.08    7.50   500 Rheinland-Pfalz
X313  ---- SWIS-PUNKT            50.14    7.42   500 Rheinland-Pfalz
X314  ---- SWIS-PUNKT            50.12    7.46   500 Rheinland-Pfalz
X315  ---- SWIS-PUNKT            50.05    7.52   300 Hessen
X316  ---- SWIS-PUNKT            50.08    8.23   300 Hessen
X317  ---- SWIS-PUNKT            50.10    7.56   500 Hessen
X318  ---- SWIS-PUNKT            50.06    8.02   500 Hessen
X319  ---- SWIS-PUNKT            50.23    8.32   500 Hessen
X320  ---- SWIS-PUNKT            50.30    8.10   300 Hessen
X321  ---- SWIS-PUNKT            50.50    8.39   300 Hessen
X322  ---- SWIS-PUNKT            50.32    8.43   300 Hessen
X323  ---- SWIS-PUNKT            50.35    7.20   300 Rheinland-Pfalz
X324  ---- SWIS-PUNKT            50.28    7.56   300 Rheinland-Pfalz
X325  ---- SWIS-PUNKT            50.26    7.44   500 Rheinland-Pfalz
X326  ---- SWIS-PUNKT            50.35    7.50   500 Rheinland-Pfalz
X327  ---- SWIS-PUNKT            50.40    8.04   500 Rheinland-Pfalz
X328  ---- SWIS-PUNKT            51.24    8.16   500 Nordrhein-Westfalen
X329  ---- SWIS-PUNKT            51.18    8.33   700 Nordrhein-Westfalen
X330  ---- SWIS-PUNKT            51.04    8.28   700 Nordrhein-Westfalen
X331  ---- SWIS-PUNKT            51.57    9.07   300 Nordrhein-Westfalen
X333  ---- SWIS-PUNKT            50.45    7.16   100 Nordrhein-Westfalen
X334  ---- SWIS-PUNKT            50.56    7.25   300 Nordrhein-Westfalen
X335  ---- SWIS-PUNKT            51.17    7.27   500 Nordrhein-Westfalen
X336  ---- SWIS-PUNKT            51.10    7.29   500 Nordrhein-Westfalen
X337  ---- SWIS-PUNKT            51.04    7.34   500 Nordrhein-Westfalen
X338  ---- SWIS-PUNKT            50.59    7.43   500 Nordrhein-Westfalen
X339  ---- SWIS-PUNKT            51.32    9.28   300 Hessen
X340  ---- SWIS-PUNKT            51.04    8.59   500 Hessen
X341  ---- SWIS-PUNKT            50.54    9.25   500 Hessen
X342  ---- SWIS-PUNKT            50.40    9.50   500 Hessen
X343  ---- SWIS-PUNKT            51.17    8.34   700 Hessen
X344  ---- SWIS-PUNKT            51.17    8.40   700 Hessen
X345  ---- SWIS-PUNKT            51.00    9.04   700 Hessen
X346  ---- SWIS-PUNKT            50.15    9.36   300 Hessen
X347  ---- SWIS-PUNKT            50.26    9.24   500 Hessen
X348  ---- SWIS-PUNKT            50.33    9.57   500 Hessen
X349  ---- SWIS-PUNKT            50.08    9.25   500 Hessen
X350  ---- SWIS-PUNKT            50.29    9.15   700 Hessen
X351  ---- SWIS-PUNKT            50.30    9.54   700 Hessen
X352  ---- SWIS-PUNKT            50.34   10.01   700 Hessen
X353  ---- SWIS-PUNKT            51.52    9.08   100 Nordrhein-Westfalen
X354  ---- SWIS-PUNKT            51.38    9.22   100 Nordrhein-Westfalen
X355  ---- SWIS-PUNKT            51.32    9.11   100 Nordrhein-Westfalen
X356  ---- SWIS-PUNKT            51.35    9.15   300 Nordrhein-Westfalen
X357  ---- SWIS-PUNKT            51.49    9.16   300 Nordrhein-Westfalen
X358  ---- SWIS-PUNKT            51.48    9.50   100 Niedersachsen
X359  ---- SWIS-PUNKT            51.52    9.38   300 Niedersachsen
X360  ---- SWIS-PUNKT            51.22    9.36   300 Niedersachsen
X361  ---- SWIS-PUNKT            51.31   10.03   300 Niedersachsen
X362  ---- SWIS-PUNKT            51.39   10.38   500 Niedersachsen
X363  ---- SWIS-PUNKT            51.41   10.30   500 Niedersachsen
X364  ---- SWIS-PUNKT            51.46   10.17   500 Niedersachsen
X365  ---- SWIS-PUNKT            51.49   10.30   700 Niedersachsen
X366  ---- SWIS-PUNKT            51.51   10.22   700 Niedersachsen
X367  ---- SWIS-PUNKT            51.40   10.25   700 Niedersachsen
X368  ---- SWIS-PUNKT            51.47   10.33   900 Niedersachsen
X369  ---- SWIS-PUNKT            51.47   10.29   900 Niedersachsen
X370  ---- SWIS-PUNKT            51.44   10.25   900 Niedersachsen
X371  ---- SWIS-PUNKT            51.44   10.31   900 Niedersachsen
X372  ---- SWIS-PUNKT            51.56   10.47   100 Sachsen-Anhalt
X373  ---- SWIS-PUNKT            51.52   11.11   100 Sachsen-Anhalt
X374  ---- SWIS-PUNKT            51.27   11.04   100 Sachsen-Anhalt
X375  ---- SWIS-PUNKT            51.42   11.13   300 Sachsen-Anhalt
X376  ---- SWIS-PUNKT            51.34   11.13   300 Sachsen-Anhalt
X377  ---- SWIS-PUNKT            51.29   11.01   300 Sachsen-Anhalt
X378  ---- SWIS-PUNKT            51.50   10.38   500 Sachsen-Anhalt
X379  ---- SWIS-PUNKT            51.34   11.01   500 Sachsen-Anhalt
X380  ---- SWIS-PUNKT            51.41   10.42   500 Sachsen-Anhalt
X381  ---- SWIS-PUNKT            51.49   10.35   700 Sachsen-Anhalt
X382  ---- SWIS-PUNKT            51.47   10.42   700 Sachsen-Anhalt
X383  ---- SWIS-PUNKT            51.45   10.38   700 Niedersachsen
X384  ---- SWIS-PUNKT            51.47   10.39   700 Sachsen-Anhalt
X389  ---- SWIS-PUNKT            51.44   11.37   100 Sachsen-Anhalt
X390  ---- SWIS-PUNKT            51.33   11.51   100 Sachsen-Anhalt
X391  ---- SWIS-PUNKT            51.39   11.26   300 Sachsen-Anhalt
X392  ---- SWIS-PUNKT            51.32   11.20   300 Sachsen-Anhalt
X393  ---- SWIS-PUNKT            51.20   11.27   300 Sachsen-Anhalt
X394  ---- SWIS-PUNKT            51.15   11.44   300 Sachsen-Anhalt
X395  ---- SWIS-PUNKT            50.24   10.29   300 Thüringen
X396  ---- SWIS-PUNKT            50.16   10.46   300 Thüringen
X397  ---- SWIS-PUNKT            50.43   10.01   500 Thüringen
X398  ---- SWIS-PUNKT            50.23   11.06   500 Thüringen
X399  ---- SWIS-PUNKT            50.21   11.18   300 Bayern
X400  ---- SWIS-PUNKT            50.09   11.30   300 Bayern
X401  ---- SWIS-PUNKT            50.02   11.38   300 Bayern
X402  ---- SWIS-PUNKT            50.15   11.23   300 Bayern
X403  ---- SWIS-PUNKT            50.19   11.24   500 Bayern
X404  ---- SWIS-PUNKT            50.06   11.41   500 Bayern
X405  ---- SWIS-PUNKT            50.05   11.53   700 Bayern
X406  ---- SWIS-PUNKT            49.55   12.07   700 Bayern
X407  ---- SWIS-PUNKT            50.11   12.03   700 Bayern
X408  ---- SWIS-PUNKT            49.53   12.02   900 Bayern
X409  ---- SWIS-PUNKT            49.54   12.05   900 Bayern
X410  ---- SWIS-PUNKT            50.01   11.52   900 Bayern
X411  ---- SWIS-PUNKT            49.20   12.18   500 Bayern
X412  ---- SWIS-PUNKT            49.44   12.22   700 Bayern
X413  ---- SWIS-PUNKT            49.32   12.24   700 Bayern
X414  ---- SWIS-PUNKT            49.29   12.36   700 Bayern
X415  ---- SWIS-PUNKT            49.43   12.24   900 Bayern
X416  ---- SWIS-PUNKT            49.30   12.37   900 Bayern
X417  ---- SWIS-PUNKT            49.19   12.47   900 Bayern
X418  ---- SWIS-PUNKT            49.30   12.34   900 Bayern
X419  ---- SWIS-PUNKT            49.07   12.17   500 Bayern
X420  ---- SWIS-PUNKT            48.40   13.31   500 Bayern
X421  ---- SWIS-PUNKT            49.02   12.33   700 Bayern
X422  ---- SWIS-PUNKT            48.58   12.50   700 Bayern
X423  ---- SWIS-PUNKT            49.03   13.11   900 Bayern
X424  ---- SWIS-PUNKT            48.48   13.45   900 Bayern
X426  ---- SWIS-PUNKT            48.49   13.41  1100 Bayern
X427  ---- SWIS-PUNKT            48.57   13.34  1100 Bayern
X428  ---- SWIS-PUNKT            50.32   11.58   500 Sachsen
X429  ---- SWIS-PUNKT            50.20   12.06   700 Sachsen
X430  ---- SWIS-PUNKT            50.21   12.24   700 Sachsen
X431  ---- SWIS-PUNKT            50.28   12.26   700 Sachsen
X432  ---- SWIS-PUNKT            50.29   12.45   700 Sachsen
X433  ---- SWIS-PUNKT            50.45   13.39   700 Sachsen
X434  ---- SWIS-PUNKT            50.27   12.45   900 Sachsen
X435  ---- SWIS-PUNKT            50.27   12.55   900 Sachsen
X436  ---- SWIS-PUNKT            50.32   13.10   900 Sachsen
X437  ---- SWIS-PUNKT            51.22   14.52   100 Sachsen
X438  ---- SWIS-PUNKT            50.45   13.05   500 Sachsen
X439  ---- SWIS-PUNKT            50.50   10.24   700 Thüringen
X440  ---- SWIS-PUNKT            50.44   10.44   700 Thüringen
X441  ---- SWIS-PUNKT            50.44   10.35   900 Thüringen
X442  ---- SWIS-PUNKT            50.42   10.41   900 Thüringen
X443  ---- SWIS-PUNKT            50.55   12.22   300 Thüringen
X444  ---- SWIS-PUNKT            50.49   11.23   500 Thüringen
X445  ---- SWIS-PUNKT            50.44   11.10   500 Thüringen
X446  ---- SWIS-PUNKT            50.38   11.36   500 Thüringen
X447  ---- SWIS-PUNKT            50.38   12.03   500 Thüringen
X448  ---- SWIS-PUNKT            51.14   11.33   300 Sachsen-Anhalt
X449  ---- SWIS-PUNKT            51.09   11.38   300 Sachsen-Anhalt
X450  ---- SWIS-PUNKT            51.00   12.09   300 Sachsen-Anhalt
X451  ---- SWIS-PUNKT            51.03   11.07   100 Thüringen
X452  ---- SWIS-PUNKT            51.03   10.38   300 Thüringen
X453  ---- SWIS-PUNKT            50.56   10.30   300 Thüringen
X454  ---- SWIS-PUNKT            51.23   10.05   300 Thüringen
X455  ---- SWIS-PUNKT            51.58   12.22   100 Sachsen-Anhalt
X456  ---- SWIS-PUNKT            51.55   12.10   100 Sachsen-Anhalt
X457  ---- SWIS-PUNKT            51.37   12.22   100 Sachsen-Anhalt
X458  ---- SWIS-PUNKT            51.14   11.55   100 Sachsen-Anhalt
X459  ---- SWIS-PUNKT            51.09   12.07   100 Sachsen-Anhalt
X460  ---- SWIS-PUNKT            52.20    7.43   100 Nordrhein-Westfalen
X461  ---- SWIS-PUNKT            52.16    8.36   300 Nordrhein-Westfalen
X462  ---- SWIS-PUNKT            50.53    6.07   100 Nordrhein-Westfalen
X463  ---- SWIS-PUNKT            50.53    6.20   100 Nordrhein-Westfalen
X464  ---- SWIS-PUNKT            50.46    6.26   100 Nordrhein-Westfalen
X465  ---- SWIS-PUNKT            53.22    8.24   100 Niedersachsen
X466  ---- SWIS-PUNKT            52.22    8.00   100 Niedersachsen
X467  ---- SWIS-PUNKT            52.15   12.22   100 Brandenburg
X468  ---- SWIS-PUNKT            51.59   12.57   100 Brandenburg
X469  ---- SWIS-PUNKT            51.58   13.25   100 Brandenburg
X470  ---- SWIS-PUNKT            52.35   11.05   100 Sachsen-Anhalt
X471  ---- SWIS-PUNKT            51.20   12.56   100 Sachsen
X472  ---- SWIS-PUNKT            50.59   14.13   500 Sachsen
X473  ---- SWIS-PUNKT            51.03   14.16   500 Sachsen
X474  ---- SWIS-PUNKT            51.04   14.32   500 Sachsen
X475  ---- SWIS-PUNKT            51.08   14.37   500 Sachsen
X476  ---- SWIS-PUNKT            51.44    9.28   500 Niedersachsen
X477  ---- SWIS-PUNKT            51.48    9.33   500 Niedersachsen
X478  ---- SWIS-PUNKT            51.47    9.36   500 Niedersachsen
06678 ---- BISCHOFSZELL          47.30    9.14   470 Thurgau
06647 ---- WUERENLINGEN          47.32    8.14   334 Aargau
10124 ---- LEUCHTTURM A. WESER   53.51    8.07    32 
10271 ---- NEURUPPIN-ALT RUPPIN  52.57   12.51    50 Brandenburg
10308 ---- NORDHORN              52.33    7.10    24 Niedersachsen
10619 ---- BAUMHOLDER            49.37    7.21   442 Rheinland-Pfalz
11113 ---- NAUDERS               46.53   10.30  1330 Tirol
11127 ---- OBERGURGL             46.52   11.01  1941 Tirol
11138 ---- ALPINZENTRUM RUDOL.   47.08   12.38  2317 Salzburg
11155 ---- FEUERKOGEL            47.49   13.43  1618 Oberösterreich
11173 ---- FISCHBACH             47.27   15.39  1034 Steiermark
11221 ---- KOEFLACH              47.04   15.05   463 Steiermark
11232 ---- FEISTRITZ             46.34   14.46   532 Kärnten
11252 ---- VIRGEN (OSTTIROL)     47.00   12.27  1212 Tirol
11255 ---- KOETSCHACH            46.41   13.00   722 Kärnten
11272 ---- SPITTAL/DRAU (TAWES)  46.47   13.29   542 Kärnten
11280 ---- MURAU                 47.07   14.11   814 Steiermark
11285 ---- DEUTSCHLANDSBERG      46.49   15.14   354 Steiermark
11290 ---- GRAZ (UNIVERSITAET)   47.05   15.27   367 Steiermark
11310 ---- ISCHGL                46.59   10.19  2327 Tirol
11314 ---- REUTTE AUTOM.         47.30   10.43   842 Tirol
11340 ---- SCHMITTENHOEHE        47.20   12.44  1956 Salzburg
11390 ---- HARTBERG              47.17   15.59   330 Steiermark
12399 ---- TERESPOL              52.05   23.37   136 Woiwodschaft Lublin
13457 ---- TIVAT                 42.24   18.44   139 Kotor Municipality
13459 ---- NIKSIC                42.46   18.57   143 Nikšić Municipality
13461 ---- BAR                   42.06   19.05   142 
13463 ---- PODGORICA             42.26   19.17   154 Großgemeinde Podgorica
26144 ---- LOGEVA                58.45   26.25   130 Kreis Jõgeva
26215 EEKE ARENSBURG             58.13   22.31     3 
26258 ---- PSKOV                 57.49   28.20   132 Oblast Pskow
26425 ---- JELGAVA               56.33   23.58   134 Bezirk Jelgava
26544 ---- DAUGAVPILS            55.52   26.37   134 Daugavpils
26657 ---- DOKSICY               54.53   27.45   135 Wizebskaja Woblasz
26695 ---- LEPEL                 55.10   34.24   135 Oblast Smolensk
26759 ---- BORISOV               54.16   28.30   135 Minskaja Woblasz
26763 ---- ORSHA                 54.30   30.27   133 Wizebskaja Woblasz
26774 ---- OGORKI                54.18   30.57   132 Mahiljouskaja Woblasz
26781 ---- SMOLENSK              54.45   32.04   132 Oblast Smolensk
26832 ---- LIDA                  53.54   25.19   131 Hrodsenskaja Woblasz
26898 ---- BRYANSK               53.15   34.19   132 Oblast Brjansk
26941 ---- BARANOVICHI           53.08   25.58   139 Breszkaja Woblasz
26951 ---- SLUTSK                53.03   27.33   132 Minskaja Woblasz
26961 ---- BOBRUISK              53.13   29.08   135 Mahiljouskaja Woblasz
26966 ---- ZHLOBIN               52.54   30.03   134 Homelskaja Woblasz
27402 ---- TVER                  56.53   35.52   130 Oblast Twer
33019 ---- PINSK                 52.07   26.07   133 Breszkaja Woblasz
33036 ---- MOZYR                 52.02   29.12   133 Homelskaja Woblasz
33088 ---- SARNY                 51.19   26.37   131 Riwne
33124 ---- BRAGIN                51.48   30.15   133 Homelskaja Woblasz
33135 ---- CHERNIGOV             51.27   31.12   136 Tschernihiw
33177 ---- VLADIMIR-VOLYNSKIJ    50.50   24.21   145 Wolhynien
33187 ---- LUTSK                 50.43   25.24   133 Wolhynien
33275 ---- SUMY                  50.52   34.45   130 Sumy
33301 ---- ROVNO                 50.36   26.09   131 Riwne
33317 ---- SHEPETIVKA            50.10   27.02   137 Oblast Chmelnyzkyj
33325 ---- ZHYTOMYR              50.17   28.40   136 Schytomyr
33393 ---- LIVIV                 49.48   23.58   143 Oblast Lwiw
33415 ---- TERNOPOL              49.32   25.41   148 Ternopil
33466 ---- MIRONOVKA             49.39   31.05   136 Oblast Kiew
33506 ---- POLTAVA               49.37   34.33   135 Poltawa
33562 ---- VINNITSA              49.15   28.36   148 Winnyzja
33614 ---- SVETLOVODSK           49.04   33.15   137 Kirowohrad
33631 ---- UZHGOROD              48.38   22.16   134 Transkarpatien
33658 ---- CHERNOVTSY            48.16   25.58   136 Oblast Tscherniwzi
33664 ---- BRICENI               48.21   27.05   131 Rajon Briceni
33745 ---- BALTI                 47.47   27.57   129 Bălți
33749 ---- BRAVICEA              47.22   28.26   134 Rajon Călărași
33761 ---- LYUBASHEVKA           47.51   30.16   139 Odessa
33821 ---- DUBASARI              47.17   29.08   135 Rajon Dubăsari
33829 ---- TIRASPOL              46.52   29.36   128 Transnistrien
33883 ---- KOMRAT                46.18   28.38   129 Gagausien
33885 ---- CAHUL                 45.53   28.14   132 Rajon Cahul
33889 ---- IZMAIL                45.22   28.51   133 Odessa
33896 ---- SARATA                46.01   29.40   129 Odessa
33902 ---- KHERSON               46.44   32.43   133 Cherson
33934 ---- DZHANKOI              45.43   34.23    13 
33946 ---- SIMFEROPOL            45.02   33.58   142 
33994 ---- AYVOVE                44.44   33.39    41 
34415 ---- IZYUM                 49.11   37.17   131 Oblast Charkiw
34615 ---- VOLNOVAKHA            47.37   37.29   267 Oblast Donezk
40025 ---- LATAKIA               35.24   35.56    48 Latakia
40030 ---- HAMA                  35.07   36.45   301 Hama
40253 ---- BAQURA                32.38   35.37  -170 Irbid
40255 ---- IRBID                 32.33   35.51   619 Irbid
40256 ---- WADI RAYAN            32.24   35.35  -200 Irbid
40257 ---- RAS MUNEEF            32.22   35.45  1150 Gouvernement Adschlun
40260 ---- H-5 SAFAWI            32.12   37.08   674 Gouvernement Mafraq
40265 ---- MAFRAQ                32.22   36.15   683 Gouvernement Mafraq
40267 ---- WADI DHULAIL          32.09   36.17   580 Gouvernement Mafraq
40268 ---- SALT                  32.02   35.44   915 Gouvernement al-Balqa
40275 ---- QATRANEH              31.15   36.07   768 Gouvernement Karak
40280 ---- JERICHO               31.52   35.30  -275 
40285 ---- DEIR ALLA             32.13   35.37  -224 Gouvernement al-Balqa
40288 ---- AL AZRAQ              31.50   36.49   527 Gouvernement Zarqa
40292 ---- ER RABBAH             31.16   35.45   920 Gouvernement Karak
40296 ---- GHOR EL SAFI          31.02   35.28  -350 Gouvernement Karak
40298 ---- TAFILEH               30.47   35.43  1200 Gouvernement at-Tafila
40300 ---- SHOUBAK               30.31   35.32  1365 Gouvernement Maʿan
40305 ---- JAFER                 30.17   36.09   853 Gouvernement Maʿan
40310 ---- MA'AN                 30.10   35.47  1069 Gouvernement Maʿan
40340 ---- AQABA AIRPORT         29.33   35.00    51 Gouvernement Aqaba
F9400 OJ38 ZARQA AIRPORT         32.02   36.09   732 Gouvernement Zarqa
F9401 ---- LOD IL                32.35   35.35   568 Irbid
F9434 ---- RUKLA                 55.03   24.24    80 Bezirk Kaunas
F9435 ---- HALLE DIESELSTR. HKW  51.28   12.00   105 Sachsen-Anhalt
F9501 ---- BOCHUM UMSPWK.        51.28    7.11    82 Nordrhein-Westfalen
F9502 ---- EISERFELD UMSPWK.     50.51    7.59   226 Nordrhein-Westfalen
F9503 ---- GUNDELFINGEN UMSPWK.  48.31   10.23   436 Bayern
F9504 ---- HANEKENFÄHR UMSPWK.   52.29    7.18    27 Niedersachsen
F9505 ---- HOHENECK UMSPWK.      48.55    9.12   275 Baden-Württemberg
F9506 ---- KÜHMOOS UMSPWK.       47.36    7.57   736 Baden-Württemberg
F9507 ---- LEUPOLZ UMSPWK.       47.44   10.22   721 Bayern
F9508 ---- MITTELBEXBACH UMSPWK  49.22    7.14   363 Saarland
F9509 ---- NIEDERSTEDEM UMSPWK.  49.55    6.29   233 Rheinland-Pfalz
F9510 ---- RHEINAU UMSPWK.       49.26    8.33   106 Baden-Württemberg
F9511 ---- ROMMERSKIRCHEN UMSPW  51.01    6.42    87 Nordrhein-Westfalen
F9512 ---- URBERACH UMSPWK.      49.59    8.46   177 Hessen
F9513 ---- WEIßENTURM UMSPWK.    50.24    7.27   141 Rheinland-Pfalz
F9514 ---- WESTERKAPPELN UMSPWK  52.17    7.53    80 Nordrhein-Westfalen
F9515 ---- GRONAU WEST           51.19    7.17    36 Nordrhein-Westfalen
F9516 ---- SOONWALD WEST 1       50.20    7.30   237 Rheinland-Pfalz
F9517 ---- SOONWALD WEST 2       49.59    7.47   294 Rheinland-Pfalz
F9518 ---- SOONWALD WEST 3       50.19    7.30    73 Rheinland-Pfalz
F9519 ---- SOONWALD WEST 4       49.56    7.49   262 Rheinland-Pfalz
F9520 ---- WONNEGAU WEST 1       49.52    7.54   102 Rheinland-Pfalz
F9521 ---- WONNEGAU WEST 2       47.54    8.20   811 Baden-Württemberg
F9522 ---- WONNEGAU WEST 3       49.45    8.11   198 Rheinland-Pfalz
F9523 ---- WONNEGAU WEST 4       49.47    8.08   181 Rheinland-Pfalz
F9524 ---- WONNEGAU WEST 5       49.55    7.49   177 Rheinland-Pfalz
F9525 ---- BRAUWEILER WEST 1     50.52    6.50    90 Nordrhein-Westfalen
F9526 ---- BRAUWEILER WEST 2     50.59    6.48    56 Nordrhein-Westfalen
F9527 ---- WALBERBERG WEST       50.51    6.53   116 Nordrhein-Westfalen
F9528 ---- VILLE OST 1           50.53    6.54    57 Nordrhein-Westfalen
F9529 ---- VILLE OST 2           50.56    6.49    60 Nordrhein-Westfalen
F9530 ---- KUGELBERG O. / W. 1   49.13    8.50   240 Baden-Württemberg
F9531 ---- KUGELBERG O. / W. 2   48.58    9.10   258 Baden-Württemberg
F9532 ---- KUGELBERG O. / W. 3   49.34    8.32   112 Hessen
F9533 ---- KUGELBERG O. / W. 4   49.24    8.37   106 Baden-Württemberg
F9534 ---- KUGELBERG O. / W. 5   49.04    9.02   190 Baden-Württemberg
F9535 ---- KUGELBERG O. / W. 6   49.31    8.34   102 Baden-Württemberg
F9536 ---- KUGELBERG O. / W. 7   49.14    8.45   166 Baden-Württemberg
F9537 ---- KUGELBERG O. / W. 8   49.00    9.07   271 Baden-Württemberg
F9600 ---- HEINERSCHEID          50.05    6.04   522 Diekirch
N9608 ---- RENA                  61.11   11.22   255 Innlandet
N9610 ---- WEIßENFELS            51.12   11.58   100 Sachsen-Anhalt
P0576 ---- BLANKENBURG / HARZ    51.49   10.57   220 Sachsen-Anhalt
P0577 ---- BLEICHERODE           51.26   10.36   270 Thüringen
P0578 ---- HERMSDORF / THUER.    50.53   11.51   345 Thüringen
P0600 ---- VELBERT               51.20    7.03   249 Nordrhein-Westfalen
P0601 ---- WEGBERG               51.09    6.17    68 Nordrhein-Westfalen
P0602 ---- GLADBECK              51.35    6.58    64 Nordrhein-Westfalen
P0603 ---- CALW                  48.43    8.45   418 Baden-Württemberg
P0604 ---- HAGEN-HOHENLIMBURG    51.21    7.34   131 Nordrhein-Westfalen
P0605 ---- ENNEPETALSPERRE       51.14    7.25   309 Nordrhein-Westfalen
P0606 ---- SCHMALLENBERG         51.09    8.17   381 Nordrhein-Westfalen
P0607 ---- MARSBERG              51.27    8.51   250 Nordrhein-Westfalen
P0608 ---- LANGENAU              48.30   10.07   461 Baden-Württemberg
P0609 ---- HARDHEIM              49.37    9.29   271 Baden-Württemberg
P0610 ---- WRIEZEN               52.43   14.08    35 Brandenburg
P0616 ---- SUEDLOHN              51.57    6.54    52 Nordrhein-Westfalen
P0617 ---- WETTRINGEN            52.13    7.21    48 Nordrhein-Westfalen
P0618 ---- HAFTENKAMP            52.32    6.55    17 Niedersachsen
P0619 ---- ENNIGERLOH            51.51    8.02   104 Nordrhein-Westfalen
P0620 ---- SCHWARTENBERG         52.50    7.06    13 Niedersachsen
P0621 ---- BERDEL                51.57    7.47    60 Nordrhein-Westfalen
P0622 ---- FREREN                52.29    7.32    37 Niedersachsen
P0624 ---- SCHIRL                52.01    7.53    55 Nordrhein-Westfalen
P0625 ---- DOERENTHE             52.13    7.39    45 Nordrhein-Westfalen
P0626 ---- RIESENBECK            52.14    7.36    44 Nordrhein-Westfalen
P0627 ---- BEVERGERN             52.16    7.36    45 Nordrhein-Westfalen
P0628 ---- MAEKEL                52.41    8.29    35 Niedersachsen
P0629 ---- TEMMING               52.01    7.25    72 Nordrhein-Westfalen
P0630 ---- HOHENHOLTE            52.00    7.27    70 Nordrhein-Westfalen
P0631 ---- OSTBEVERN             52.03    7.51    55 Nordrhein-Westfalen
P0632 ---- OSTBEVERN/BROCK       52.04    7.54    55 Nordrhein-Westfalen
P0633 ---- OSTBEVERN/UEBERWAS.   52.01    7.51    55 Nordrhein-Westfalen
P0634 ---- BOHMTE                52.23    8.18    45 Niedersachsen
P0635 ---- LEMFOERDE             52.29    8.23    40 Niedersachsen
P0636 ---- LENGERICH             52.34    7.32    26 Niedersachsen
P0637 ---- MERZEN                52.28    7.46    52 Niedersachsen
P0638 ---- NEUENKIRCHEN          52.23    7.52    54 Niedersachsen
P0639 ---- TWIST                 52.38    7.07    20 Niedersachsen
P0640 ---- NORDHORN              52.29    7.03    20 Niedersachsen
P0642 ---- BUTENDI1              55.01    7.46     0 
P0643 ---- GODEWIN1              54.03    7.02     0 
P0644 ---- GODEWIN2              54.03    7.02     0 
P0645 ---- NORDONE1              53.59    6.49     0 
P0646 ---- SANDBAN1              55.11    6.52     0 
P0647 ---- NORGRUE1              53.50    8.10     0 
P0648 ---- VEJAMAT1              54.19    5.52     0 
P0649 ---- WIKINGR1              54.50   14.04     0 
E273  ---- ROSENGARTEN-KLECKEN   53.22    9.57    82 Niedersachsen
G201  ---- BIRKENMOOR            50.19   10.53   320 Bayern
G202  ---- HOHENROTH             50.19   10.10   300 Bayern
G204  ---- MARIA-BILDHAUSEN      50.17   10.18   320 Bayern
G205  ---- MARKERSREUTH          50.13   11.49   556 Bayern
G207  ---- POPPENHOLZ            50.11   11.27   420 Bayern
G208  ---- EBERTSHAUSEN          50.08   10.21   350 Bayern
G210  ---- BAD STAFFELSTEIN      50.07   11.00   258 Bayern
G211  ---- SCHOELLKRIPPEN        50.06    9.15   206 Bayern
G213  ---- BRAUNERSGRUEN         50.05   12.06   590 Bayern
G214  ---- KOESLAU               50.04   10.40   400 Bayern
G216  ---- GROSSZIEGENFELD       50.01   11.10   480 Bayern
G219  ---- WIESENGIECH           49.58   10.59   280 Bayern
G220  ---- STEINFELD             49.57    9.40   300 Bayern
G222  ---- GROSSOSTHEIM          49.56    9.03   129 Bayern
G223  ---- WADENBRUNN            49.55   10.14   235 Bayern
G225  ---- MISTELBACH            49.54   11.30   410 Bayern
G226  ---- AUFSESS               49.54   11.14   450 Bayern
G228  ---- KEMNATH               49.53   11.53   507 Bayern
G229  ---- SELIGENSTADT          49.51   10.06   281 Bayern
G231  ---- VEITSHOECHHEIM        49.50    9.53   220 Bayern
G235  ---- KONNERSREUTH          49.50   12.15   540 Bayern
G237  ---- SCHWARZENAU           49.48   10.13   200 Bayern
G240  ---- GERBRUNN              49.47   10.01   320 Bayern
G241  ---- HELMSTADT             49.45    9.43   280 Bayern
G243  ---- BAMMERSDORF           49.45   11.04   295 Bayern
G244  ---- RANDERSACKER          49.45    9.59   185 Bayern
G246  ---- IPHOFEN               49.43   10.16   350 Bayern
G247  ---- BUERGSTADT            49.43    9.17   210 Bayern
G249  ---- HOECHSTADT A.D. AISC  49.42   10.51   265 Bayern
G250  ---- DIETZHOF              49.42   11.10   363 Bayern
G253  ---- HILTPOLTSTEIN         49.40   11.19   520 Bayern
G255  ---- HEPPDIEL              49.40    9.22   335 Bayern
G256  ---- EUERHAUSEN            49.37    9.57   310 Bayern
G258  ---- EDELSFELD             49.35   11.42   528 Bayern
G259  ---- SOELLITZ              49.32   12.14   550 Bayern
G261  ---- KAUBENHEIM            49.32   10.28   300 Bayern
G262  ---- NEUHERBERG            49.31   10.17   380 Bayern
G265  ---- GREIMERSDORF          49.28   10.50   320 Bayern
G270  ---- ANFELDEN              49.25   10.24   454 Bayern
G271  ---- WULLNHOF              49.23   12.36   510 Bayern
G273  ---- IRRENLOHE             49.23   12.06   363 Bayern
G274  ---- BONNHOF               49.22   10.47   400 Bayern
G276  ---- HARTENHOF             49.20   11.35   530 Bayern
G277  ---- KITZENRIED            49.18   12.25   470 Bayern
G279  ---- SCHATTENHOF           49.18   10.59   389 Bayern
G280  ---- SOMMERTSHOF           49.16   11.40   549 Bayern
G283  ---- ROECKERSBUEHL         49.14   11.22   422 Bayern
G285  ---- POESING               49.14   12.34   380 Bayern
G286  ---- OBERSTEINBACH         49.13   10.57   390 Bayern
G294  ---- EISERSZELL            49.03   12.36   617 Bayern
G295  ---- EIERSDORF             49.03   11.50   537 Bayern
G297  ---- FRANKENHOFEN          49.02   10.28   440 Bayern
G298  ---- SARCHING              49.01   12.14   330 Bayern
G300  ---- STEINACH              48.59   12.37   350 Bayern
G301  ---- KOEFERING             48.57   12.12   350 Bayern
G303  ---- KIRCHBERG IM WALD     48.54   13.11   624 Bayern
G306  ---- WALLERSTEIN           48.53   10.30   420 Bayern
G307  ---- KALTENBERG            48.51   12.03   420 Bayern
G309  ---- SANDHARLANDEN         48.50   11.49   370 Bayern
G313  ---- UTTENKOFEN            48.49   12.51   323 Bayern
G315  ---- NEUHOF                48.46   10.47   518 Bayern
G318  ---- BURGHEIM              48.42   11.01   390 Bayern
G321  ---- FEISTENAICH           48.42   12.20   460 Bayern
G322  ---- NEUSLING              48.42   12.53   345 Bayern
G324  ---- KRINGELL              48.41   13.30   450 Bayern
G325  ---- KARLSHULD             48.40   11.20   377 Bayern
G327  ---- STADELHOF             48.39   11.37   384 Bayern
G328  ---- DIETRICHSDORF         48.37   11.51   500 Bayern
G330  ---- STEINBEISSEN          48.36   12.44   380 Bayern
G331  ---- EDELSHAUSEN           48.36   11.17   400 Bayern
G333  ---- HUELL                 48.36   11.41   465 Bayern
G334  ---- FRAUENRIEDHAUSEN      48.36   10.24   440 Bayern
G337  ---- KINZESBERG            48.35   13.41   564 Bayern
G339  ---- SCHOENBRUNN           48.34   12.12   385 Bayern
G340  ---- AINERTSHOFEN          48.31   11.05   470 Bayern
G342  ---- WEISSINGEN            48.27   10.09   455 Bayern
G343  ---- ENGERSDORF            48.27   12.38   460 Bayern
G345  ---- HALDENWANG            48.27   10.28   510 Bayern
G346  ---- JETZENDORF            48.26   11.25   505 Bayern
G348  ---- BUERG                 48.25   12.10   490 Bayern
G352  ---- BAERNAU               48.23   13.23   310 Bayern
G354  ---- ROTTHALMUENSTER       48.22   13.12   360 Bayern
G355  ---- FRANKENDORF           48.21   11.59   455 Bayern
G357  ---- FRIEDING              48.20   12.50   480 Bayern
G358  ---- GROSSBERGHOFEN        48.19   11.19   508 Bayern
G360  ---- EICHENRIED            48.16   11.47   475 Bayern
G363  ---- DUERABUCH             48.16   11.13   520 Bayern
G364  ---- RESCHENBERG           48.14   10.21   560 Bayern
G367  ---- ASEN                  48.11   12.12   595 Bayern
G369  ---- SCHWABMUENCHEN        48.11   10.47   556 Bayern
G372  ---- KIRCHHEIM             48.11   10.28   536 Bayern
G373  ---- FORSTING              48.10   12.34   450 Bayern
G375  ---- GUT HUELL             48.06   11.20   580 Bayern
G376  ---- BERGHAM               48.05   12.15   487 Bayern
G378  ---- OSTERSEEON            48.04   11.55   560 Bayern
G384  ---- NILLING               48.02   12.49   390 Bayern
G385  ---- ROTHENFELD            47.58   11.13   690 Bayern
G387  ---- LAUTRACH              47.54   10.07   610 Bayern
G391  ---- OBERSOECHERING        47.45   11.13   671 Bayern
G394  ---- SCHOENAU              47.35    9.41   441 Bayern
G396  ---- STREITELSFINGEN       47.34    9.43   483 Bayern
G397  ---- SCHWAND               47.34    9.39   520 Bayern
H176  ---- KALLETAL NIEDERMEIEN  52.04    8.57   310 Nordrhein-Westfalen
H250  ---- SENDENHORST_N         51.50    7.53    65 Nordrhein-Westfalen
H316  ---- RAESFELD KA           51.45    6.48    42 Nordrhein-Westfalen
H375  ---- LICHTENAU             51.37    8.54   304 Nordrhein-Westfalen
H566  ---- MENDEN_LENDRINGSEN    51.24    7.50   170 Nordrhein-Westfalen
H764  ---- ROTHE FURTH           51.05    7.19   230 Nordrhein-Westfalen
H789  ---- BREITENBACHTALSPERRE  50.59    8.05   410 Nordrhein-Westfalen
H813  ---- ESCHWEILER N          50.49    6.18   130 Nordrhein-Westfalen
H840  ---- BORNHEIM EICHENKAMP   50.47    7.01    57 Nordrhein-Westfalen
H910  ---- SIMMERATH N           50.38    6.18   460 Nordrhein-Westfalen
J623  ---- DIFFERTEN             49.14    6.46   251 Saarland
J736  ---- BALTERSWEILER         49.29    7.10   289 Saarland
J739  ---- BACHEM                49.30    6.42   220 Saarland
J927  ---- RIESWEILER            49.08    7.19   314 Grand Est
K060  ---- MAROTH                50.35    7.41   285 Rheinland-Pfalz
K082  ---- HERDORF               50.46    7.58   483 Rheinland-Pfalz
K099  ---- LIEBENSCHEID          50.42    8.05   560 Rheinland-Pfalz
K242  ---- ADENAU                50.26    7.06   593 Rheinland-Pfalz
K376  ---- GONDERSHAUSEN         50.10    7.30   388 Rheinland-Pfalz
K399  ---- BERGHAUSEN            50.16    8.00   372 Rheinland-Pfalz
K418  ---- KÖRPERICH-GAYTALPARK  49.56    6.15   290 Rheinland-Pfalz
K450  ---- NEEF                  50.05    7.08   133 Rheinland-Pfalz
K550  ---- ENTENPFUHL            49.54    7.35   610 Rheinland-Pfalz
K552  ---- GAUCHSBERG            49.52    7.41   399 Rheinland-Pfalz
K626  ---- HERMESKEIL            49.42    7.02   650 Rheinland-Pfalz
K748  ---- MARTINSHÖHE           49.22    7.28   411 Rheinland-Pfalz
K756  ---- FRANKELBACH           49.31    7.39   417 Rheinland-Pfalz
K931  ---- HORTENKOPF            49.16    7.50   606 Rheinland-Pfalz
K996  ---- SCHAIDT               49.03    8.05   136 Rheinland-Pfalz
L244  ---- GUDENSBERG            51.10    9.22   220 Hessen
L314  ---- ANGELBURG-FRECHENHAU  50.49    8.26   435 Hessen
L391  ---- BEBRA                 50.58    9.47   192 Hessen
L543  ---- GRÜNBERG              50.35    8.59   314 Hessen
L562  ---- FREIENSTEINAU         50.26    9.24   430 Hessen
L595  ---- GERSFELD_(RHÖN)-DALH  50.25    9.50   667 Hessen
L643  ---- NIDDA-KLÄRANLAGE      50.24    8.59   132 Hessen
L731  ---- USINGEN               50.21    8.32   320 Hessen
L769  ---- FREIGERICHT-HORBACH   50.08    9.10   198 Hessen
L918  ---- LORSCH-KLÄRANLAGE     49.40    8.34    92 Hessen
M439  ---- BERKA, BAD (FLUGPLAT  50.54   11.16   303 Thüringen
N769  ---- LAUCHSTAEDT, BAD      51.23   11.53   118 Sachsen-Anhalt
Q824  ---- DACHSBERG-WOLPADINGE  47.42    8.07   880 Baden-Württemberg
X479  ---- MIDDELHAGEN           54.20   13.42    19 Mecklenburg-Vorpommern
X480  ---- BLANDOW               54.34   13.35    48 Mecklenburg-Vorpommern
X481  ---- BOHLENDORF            54.36   13.17     7 Mecklenburg-Vorpommern
X482  ---- GNOIEN                53.58   12.42    19 Mecklenburg-Vorpommern
X483  ---- HOEXTER               51.47    9.24    93 Nordrhein-Westfalen
X484  ---- HOGFGEISMAR           51.30    9.23   162 Hessen
X485  ---- BEVERN                51.52    9.30   110 Niedersachsen
X486  ---- ORANIENBURG-STADT     52.45   13.15    35 Brandenburg
Z901  ---- HOERMOOS              47.30   10.00  1280 Bayern
Z902  ---- HOCHGRATBAHN          47.30   10.04  1720 Bayern
Z904  ---- KANZELWAND            47.20   10.12  1960 Vorarlberg
Z905  ---- FELLHORN              47.20   10.13  1610 Bayern
Z907  ---- NEBELHORN             47.25   10.21  2200 Bayern
Z908  ---- NEBELHORN-KOBLAT      47.25   10.21  2070 Bayern
Z909  ---- SCHWARZENBERG         47.26   10.25  1355 Bayern
Z910  ---- TEGELBERG-RUECKEN     47.33   10.47  1680 Bayern
Z911  ---- TEGELBERGBAHN         47.34   10.47  1720 Bayern
Z912  ---- TEGELBERG             47.34   10.47  1710 Bayern
Z914  ---- ZUGSPITZPLATT         47.24   10.59  2420 Bayern
Z916  ---- PUERSCHLING           47.36   10.59  1370 Bayern
Z917  ---- OSTERFELDER           47.26   11.04  1800 Bayern
Z919  ---- KRANZBERG             47.27   11.14  1300 Bayern
Z920  ---- MARCHKLAMM TAL        47.24   11.16   900
Z921  ---- MARCHKLAMM            47.24   11.17  1600 Tirol
Z922  ---- BRUNNSTEINSPITZE      47.24   11.17  2030 Tirol
Z923  ---- LINDERSPITZE-RINNE    47.26   11.18  2300 Tirol
Z924  ---- LINDERSPITZE          47.26   11.18  2340 Tirol
Z925  ---- FAHRENBERG            47.36   11.19  1575 Bayern
Z926  ---- HERZOGSTANDBAHN       47.36   11.19  1625 Bayern
Z928  ---- SCHROEDELSTEIN        47.40   11.31  1485 Bayern
Z929  ---- BRAUNECK              47.40   11.31  1550 Bayern
Z931  ---- BRECHERSPITZE         47.41   11.52  1600 Bayern
Z932  ---- SPITZINGSEE           47.40   11.53  1100 Bayern
Z934  ---- WENDELSTEIN-SOIN      47.42   12.01  1580 Bayern
Z936  ---- MOESLARNALM           47.45   12.21  1450 Bayern
Z937  ---- KAMPENWAND            47.45   12.21  1520 Bayern
Z939  ---- DUERRNBACHHORN        47.40   12.36  1580 Bayern
Z940  ---- RAUSCHBERG            47.44   12.41  1635 Bayern
Z942  ---- WARTSTEINKOPF         47.39   12.48  1755 Bayern
Z943  ---- REITERALPE            47.39   12.48  1670 Bayern
Z944  ---- WARTSTEINHUETTE       47.39   12.49  1615 Bayern
Z946  ---- KUEHROINT             47.34   12.58  1420 Bayern
Z947  ---- FUNTENSEETAUERN       47.29   12.58  2520 Bayern
Z948  ---- HOELLGRABEN           47.37   13.00   660 Bayern
Z949  ---- JENNER                47.35   13.01  1200 Bayern
01001 ENJA JAN MAYEN             70.56   -8.40    10 
01025 ---- TROMSOE               69.41   18.55    10 Troms og Finnmark
01028 ENBJ BJORNOYA              74.31   19.01    16 Spitzbergen
01049 ENAT ALTA LUFTHAVN         69.59   23.22     3 Troms og Finnmark
01052 ENHF HAMMERFEST            70.40   23.40    81 Troms og Finnmark
01089 ENKR KIRKENES              69.44   29.54    91 Troms og Finnmark
01092 ---- MAKKAUR FYR           70.42   30.05     9 Troms og Finnmark
01152 ENBO BODOE                 67.16   14.22    13 Nordland
01180 ---- HARSTAD               68.48   16.32    45 Troms og Finnmark
01210 ENAL ALESUND AIRP          62.34    6.07    22 Møre og Romsdal
01223 ENKB KRISTIANSUND          63.07    7.50    44 Møre og Romsdal
01238 ---- FOKSTUA 2             62.07    9.17   973 Innlandet
01241 ENOL ORLAND                63.42    9.36     7 Trøndelag
01271 ENVA TRONDHEIM             63.28   10.55    17 Trøndelag
01290 ENNM NAMSOS                64.28   11.35     2 Trøndelag
01366 ---- SOGNEFJELL            61.34    8.00  1415 Innlandet
01380 ---- VENABU                61.39   10.07   940 Innlandet
02049 ESNG GALLIVARE APT         67.09   20.39   359 Norrbottens län
02120 ---- KVIKKJOKK             66.57   17.44   320 Norrbottens län
02128 ESPD GUNNARN               64.58   17.42   278 Västerbottens län
02186 ESPA LULEA                 65.33   22.08    17 Norrbottens län
02196 ---- HAPARANDA             65.50   24.09     5 Lappland
02226 ESPC FROSON                63.12   14.30   376 Jämtlands län
02284 ---- JAERNAESKLUBB         63.26   19.41     6 
02286 ESNU UMEA                  63.48   20.17     7 Västerbottens län
02324 ESND SVEG                  62.02   14.22   360 Jämtlands län
02355 ---- KUGGOEREN AMOS        61.42   17.31     9 Gävleborgs län
02366 ESNN TIMRA/MIDLANDA        62.31   17.27     3 Västernorrlands län
02752 ---- KRISTIINANKAUPUNGIN   62.12   21.10     2 
02807 EFIV IVALO                 68.37   27.25   147 Lappland
02830 EFKT KITTILA               67.42   24.51   196 Lappland
02836 EFSO SODANKYLA             67.22   26.39   179 Lappland
02847 ---- ROVANIEMI             66.30   25.43    85 Lappland
02869 EFKS KUUSAMO               65.58   29.11   262 Nordösterbotten
02876 ---- OULU                  65.00   25.24     3 
02897 EFKI KAJAANI               64.17   27.41   143 Kainuu
02911 EFVA VAASA                 63.03   21.46     5 Österbotten
02915 ---- VIITASAARI            63.05   25.52   132 Mittelfinnland
02917 EFKU KUOPIO                63.01   27.48    98 Nordsavo
02929 EFJO JOENSUU APT           62.40   29.38   119 Nordkarelien
02935 EFJY JYVASKYLA             62.24   25.41   141 Mittelfinnland
02947 ---- MIKKELI               61.44   27.18   138 Südsavo
02948 EFSA SAVONLINNA            61.57   28.57    95 Südsavo
04018 BIKF KEFLAVIK              63.58  -22.36    52 
04030 BIRK REYKJAVIK             64.08  -21.54    54 
04048 BIVM VESTMANNAEYJAR        63.24  -20.17   118 
04063 BIAR AKUREYRI              65.41  -18.05    23 Norrbottens län
04097 ---- DALATANGI             65.16  -13.35     9 Nordland
04231 BGSF SONDRESTROMFJORD      67.01  -50.42    50 Autonomer Kreis der Nenzen
04250 ---- GODTHAB NUUK          64.10  -51.45    80 Republik Komi
04270 BGBW NARSARSUAQ            61.09  -45.26     4 Oblast Wologda
04330 BGDB DANEBORG              74.18  -20.13    44 
04339 BGSC SCORESBYSUND          70.29  -21.58    65 Troms og Finnmark
04360 BGAM TASIILAQ              65.36  -37.38    50 
04361 BGKK KULUSUK               65.34  -37.08    35 
06011 ---- FAROEER               62.01   -6.46    54 
08501 LPFL FLORES/AZOREN         39.27  -31.08    28 Eskişehir
08505 LPHR AZOREN                38.31  -28.43    40 Manisa
08509 LPLA LAJES/AZOREN          38.46  -27.06    52 Izmir
08515 LPAZ SANTA MARIA           36.58  -25.10   100 
08521 LPFU FUNCHAL               32.41  -16.46    58 
08589 ---- CAP VERDEN/PRAIA      14.54  -23.31    27 Schamal Darfur
08594 GVAC SAL                   16.44  -22.57    54 Ennedi-Massiv
17038 LTCG TRABZON               41.00   39.43    35 Trabzon
17096 LTCE ERZURUM               39.55   41.16  1756 Erzurum
17170 LTCI VAN                   38.27   43.19  1669 Van
17280 LTCC DIYARBAKIR            37.53   40.12   687 Diyarbakır
20674 ---- OSTROV DIKSON         73.30   80.24    47 
21824 UEST TIKSI                 71.35  128.55     7 
22113 ULMM MURMANSK              68.58   33.03    51 
22550 ULAA ARCHANGELSK           64.35   40.30    13 Oblast Archangelsk
22583 ---- KOJNAS                64.45   47.39    63 Oblast Archangelsk
22802 ---- SORTAVALA             61.43   30.43    19 Republik Karelien
22820 ULPP PETROSK               61.49   34.16   110 Republik Karelien
23074 ---- DUDINKA               69.24   86.10    19 Region Krasnojarsk
23256 USDT TAZOVSKOE             67.28   78.44     8 Autonomer Kreis der Jamal-Nenzen
23330 USDD SALEHARD              66.32   66.40    16 Autonomer Kreis der Jamal-Nenzen
23472 UOTT TURUHANSK             65.47   87.56    38 Region Krasnojarsk
23631 USHB BEREZOVO              63.56   65.03    32 Autonomer Kreis der Chanten und Mansen/Jugra
23734 ---- OKTJABRSKOE           62.27   66.03    72 Autonomer Kreis der Chanten und Mansen/Jugra
23804 UUYY SYKTYVKAR             61.40   50.51   116 Republik Komi
23849 ---- SURGUT                61.15   73.30    56 Autonomer Kreis der Chanten und Mansen/Jugra
24125 ---- OLENEK                68.30  112.26   220 
24266 ---- VERHOJANSK            67.33  133.23   137 Oblast Murmansk
24688 ---- OJMJAKON              63.15  143.09   741 Oblast Archangelsk
24959 UEEE JAKUTSK               62.01  129.43   101 Nordkarelien
27051 ULWT TOTMA                 59.53   42.45   134 Oblast Wologda
27113 ---- CEREPOVEC             59.15   37.58   114 Oblast Wologda
27459 UWGG NIZHNY NOVGOROD       56.14   43.47    78 Oblast de Níjni Novgorod
27595 UWKD KAZAN                 55.36   49.17   116 Tatarstan
27612 UUUU MOSKAU                55.45   37.34   156 Moskau
27719 ---- TULA                  54.14   37.37   165 Oblast Tula
27730 ---- RYAZAN                54.38   39.42   158 Oblast Rjasan
27962 ---- PENZA                 53.07   45.01   174 Oblast Pensa
28076 ---- DEMJANSKOE            59.36   69.17    57 Oblast Tjumen
28382 ---- UST-ISIM              57.41   71.11    62 Oblast Omsk
28440 USSS EKATERINBURG          56.48   60.38   237 Oblast Swerdlowsk
28698 UNOO OMSK                  55.01   73.23   122 Oblast Omsk
28722 UWUU UFA                   54.43   55.50   104 Baschkortostan
28807 UWWW SAMARA                53.15   50.27    40 Oblast Samara
28952 UAUU KUSTANAI              53.13   63.37   156 Qostanai
29122 ---- KARGASOK              59.03   80.57    59 Oblast Tomsk
29430 ---- TOMSK                 56.28   84.58   130 Oblast Tomsk
29570 UNKL KRASNOJARSK           56.02   92.45   276 Region Krasnojarsk
29838 UNBB BARNAUL               53.26   83.31   184 Region Altai
29846 UNWW NOVOKUZNETSK          53.49   86.53   308 Oblast Kemerowo
30054 UERT VITIM                 59.27  112.35   190 Värmlands län
30253 UIKB BODAJBO               57.51  114.14   275 
30309 UIBB BRATSK                56.17  101.45   416 
30433 ---- NIZHNEANGARSK         55.47  109.33   487 Region Midtjylland
30521 ---- ZHIGALOVO             54.48  105.13   426 
30710 UIII IRKUTSK               52.16  104.21   485 
30731 ---- GORJACINSK            52.59  108.17   488 Niedersachsen
30758 UIAA CHITA                 52.05  113.29   671 Brandenburg
31088 UHOO OKHOTSK               59.22  143.12     6 Oblast Wologda
31300 ---- ZEJA                  53.42  127.18   229 Minskaja Woblasz
31478 ---- SOFIJSKIJ PRIISK      52.16  133.59   902 Oblast Brjansk
31735 UHHH HABAROVSK             48.31  135.10    76 Oblast Dnipropetrowsk
31960 UHWW VLADIVOSTOK           43.07  131.54   138 
32053 ---- NOGLIKI               51.55  143.08    34 Oblast Saratow
32150 UHSS JUZHNO-SAKHALINSK     46.57  142.43    24 Oblast Rostow
32215 ---- SEVERO-KURILSK        50.41  156.08    23 Aktobe
32389 ---- KLJUCHI               56.19  160.50    29 Oblast Swerdlowsk
32408 UHPK UST'KAMCHATSK         56.13  162.43    27 Oblast Kurgan
34123 UUOO VORONEZ               51.42   39.13   149 Oblast Woronesch
34152 ---- BALASHOV              51.33   43.09   154 Oblast Saratow
34519 UKCC DONETSK               48.04   37.46   224 Oblast Donezk
34560 URWW VOLGOGRAD             48.47   44.22   134 Oblast Wolgograd
34880 URWA ASTRAHAN              46.17   48.03   -23 Oblast Astrachan
34929 URKK KRASNODAR             45.01   39.09    29 Region Krasnodar
35108 UARR URALSK                51.15   51.17    37 Westkasachstan
35121 UWOO ORENBURG              51.41   55.06   117 Oblast Orenburg
35188 ---- TSELINOGRAD           51.07   71.22   342 
35229 UATT AKTJUBINSK            50.17   57.09   219 Aktobe
35358 ---- TORGAI                49.38   63.30   123 Qostanai
35394 UAKK KARAGANDA             49.48   73.09   553 Qaraghandy
35746 ---- ARAL'SK               46.47   61.39    62 Qysylorda
36870 UAAA ALMA-ATA              43.14   76.56   847 
37171 ---- SOTSCHI               43.27   39.54    16 
37228 ---- WLADIKAVKAZ           43.03   44.39   703 Nordossetien-Alanien
37788 UDYZ YEREVAN ZVARTNOTS     40.09   44.23   854 Armawir
37864 UBBB BAKU/BINA             40.27   50.04    -6 
38353 ---- BISHKEK               42.51   74.32   756 Gebiet Tschüi
38457 UTTT TASCHKENT             41.16   69.16   428 
38507 ---- KRASNOVODSK           40.03   53.00    89 Balkan welaýaty
38545 ---- DARGANATA             40.28   62.17   143 Lebap welaýaty
38696 UTSS SAMARKAND             39.34   66.57   724 Samarkand
38836 UTDD DUSHANBE              38.33   68.47   800 Der Republik unterstellte Bezirke
38880 UTAA ASHKHABAD             37.58   58.20   228 Ashgabat
38927 UTST TERMEZ                37.14   67.16   310 Provinz Surxondaryo
38954 ---- KHOROG                37.30   71.30  2077 Badachschan
40061 OSPR PALMYRA               34.33   38.18   408 Gouvernement Homs
40362 OERF RAFHA                 29.37   43.29   449 Al-Hudud asch-schamaliyya
40375 OETB TABUK                 28.23   36.36   778 Provinz Tabuk
40416 OEDR DHAHRAN INTL          26.16   50.09    26 asch-Scharqiyya
40430 OEMA AL MADINAH            24.33   39.42   654 Provinz Medina
40437 OERK RIAD INT.AIRPORT      24.56   46.43   614 Provinz Riad
40438 OERY RIYADH                24.42   46.44   635 Provinz Riad
40582 OKBK KUWAIT                29.13   47.59    55 Gouvernement Al Farwaniya
40704 OITQ AHAR                  38.26   47.04  1390 Ost-Aserbaidschan
40719 OIGG RASHT                 37.12   49.38    37 Gilan
40745 OIMM MASHHAD               36.16   59.38   989 Razavi-Chorasan
40747 OICS SANANDAJ              35.20   47.00  1373 Kurdestan
40754 OIII TEHERAN               35.41   51.21  1204 Teheran
40762 DIMH TORBAT-HEYDARIEH      35.16   59.13  1333 Razavi-Chorasan
40766 OICC KERMANSHAH            34.16   47.07  1320 Kermānschāh
40768 ---- HAMEDAN               34.52   48.32  1749 Hamadan
40794 OIAS SAFI-ABAD DEZFUL      32.16   48.26    82 Chuzestan
40800 OIFM ESFAHAN               32.28   51.43  1550 Isfahan
40835 OIAH GACH SARAN DU GUNBA.  30.26   50.46   699 Kohgiluye und Boyer Ahmad
40848 OISS SHIRAZ                29.32   52.35  1486 Fars
40854 OIKM BAM                   29.06   58.24  1067 Kerman
40875 OIKB BANDARABBASS          27.13   56.22    10 Hormozgan
40911 OAMS MAZAR-I-SHARIF        36.42   67.12   378 Balch
40948 OAKB KABUL/AIRPORT         34.33   69.13  1791 Kabul
41024 OEJN JEDDAH/KING ABDUL     21.42   39.11    15 Provinz Mekka
41030 ---- MAKKAH                21.26   39.46   240 Provinz Mekka
41150 OBBI BAHREIN-INT.AIRP.     26.16   50.39     2 Gouvernement Muharraq
41170 OTBD DOHA-INT.AIRPORT      25.15   51.34    11 Doha
41184 OMRK RAS AL KHAIMAH        25.37   55.56    31 Ra’s al-Chaima
41194 OMDB DUBAI                 25.15   55.20     8 Dubai
41196 OMSJ SHARJAH               25.20   55.31    35 Schardscha
41217 OMAA ABU DHABI/INTL.       24.26   54.39    27 Abu Dhabi
41218 OMAL AL AIN AIRPORT        24.16   55.36   265 Abu Dhabi
41240 OOKB KHASAB                26.13   56.14     3 
41242 ---- DIBBA                 25.37   56.15    20 Musandam
41244 OOBR BURAIMI               24.14   55.47   299 Abu Dhabi
41246 OOSH SOHAR MAJIS           24.28   56.38     4 Schamal al-Batina
41253 ---- RUSTAQ                23.24   57.25   322 Dschanub al-Batina
41254 OOSQ SAIQ                  23.04   57.39  1755 ad-Dachiliyya
41255 ---- NIZWA                 22.51   57.32   492 ad-Dachiliyya
41256 OOMS SEEB-INT.AIRPORT      23.35   58.17    15 Maskat
41257 ---- SAMAIL                23.18   57.56   414 ad-Dachiliyya
41258 ---- QABOOS PORT           23.38   58.34     4 
41262 OOFD FAHUD                 22.21   56.29   170 az-Zahira
41263 ---- BAHLA                 22.59   57.18   589 ad-Dachiliyya
41264 ---- ADAM                  22.23   57.31   285 ad-Dachiliyya
41265 ---- IBRA                  22.44   58.30   469 Asch-Scharqiyya
41267 ---- QALHAT                22.39   59.24    12 Asch-Scharqiyya
41268 OOSR SUR                   22.32   59.29    14 Dschanub asch-Scharqiyya
41275 ---- QARN ALAM             21.22   57.03   139 ad-Dachiliyya
41288 OOMA MASIRAH               20.40   58.54    19 Dschanub asch-Scharqiyya
41304 OONR MARMUL                18.08   55.11   269 Dhofar
41312 ---- RAYSUT PORT           16.55   53.55    33 Dhofar
41314 OOTH THUMRAIT              17.40   54.02   467 Dhofar
41315 ---- QAIROON HAIRITI       17.15   54.05   878 Dhofar
41316 OOSA SALALAH               17.02   54.05    20 Dhofar
41404 OYSN SANA'A                15.31   44.11  2206 Gouvernement Sanaa
41431 OYHD HODEIDAH              14.45   42.59   115 Gouvernement al-Hudaida
41466 OYTZ TAIZ                  13.41   44.08  1402 Gouvernement Ta'izz
41480 OYAA ADEN                  12.40   45.02     3 
41494 OYSQ SOCOTRA               12.38   53.54    47 Gouvernement Hadramaut
41571 OPRN ISLAMABAD             33.37   73.06   507 Punjab
41620 OPZB ZHOB                  31.21   69.28  1405 Belutschistan
41640 OPLH LAHORE CITY           31.33   74.20   214 Punjab
41696 OPKL KALAT                 29.02   66.35  2015 Belutschistan
41749 OPNH NAWABSHAH             26.15   68.22    37 Sindh
41780 OPKC KARACHI               24.54   67.08    21 Sindh
41923 VGTJ DHAKA                 23.46   90.23     8 Dhaka
41950 ---- BARISAL               22.45   90.22     3 Barishal
41978 VGEG CHITTAGONG            22.16   91.49     4 Chittagong
42182 VIDD NEW DELHI/SAFDARJUNG  28.35   77.12   211 Delhi
42260 VIAG AGRA                  27.09   77.58   168 Uttar Pradesh
42348 VIJP JAIPUR/SANGANER       26.49   75.48   385 Rajasthan
42369 VILK LUCKNOW               26.45   80.53   122 Uttar Pradesh
42475 VIAL ALLAHABAD/BAMHRAULI   25.27   81.44    97 Uttar Pradesh
42809 VECC CALCUTTA              22.39   88.27     4 Westbengalen
42867 ---- NAGPUR SONEGAON       21.06   79.03   308 Maharashtra
43003 VABB BOMBAY AIRPORT        19.07   72.51     8 Maharashtra
43128 VOHY HYDERABAD AIRPORT     17.27   78.28   530 Telangana
43279 VOMM MADRAS                13.00   80.11    10 Tamil Nadu
43296 VOBG BANGALORE             12.57   77.38   888 Karnataka
43371 ---- THIRUVANANTHAPURAM     8.29   76.57    60 Kerala
43450 ---- KATUNAYAKE             7.10   79.53     8 Westprovinz
43466 VCBI COLOMBO                6.54   79.52     7 Westprovinz
43467 VCCC RATMALANA              6.49   79.53     5 Westprovinz
43555 VRMM MALE                   4.12   73.32     2 Malé
43599 VRGN GAN                   -0.41   73.09     2 
44275 ---- BAYANBULAG            46.50   98.05  2255 Bajanchongor
44292 ZMUB ULAAN-BAATOR          47.55  106.52  1307 Grand Est
44434 ---- POKHARA               28.12   83.59   827 Gandaki
44438 ---- BHAIRAWA AIRPORT      27.31   83.27   109 Lumbini
44454 VNKT KATHMANDU             27.42   85.22  1337 Bagmati
45007 VHHH HONGKONG              22.20  114.11     5 Agadez
45011 VMMC MACAO                 22.12  113.32    57 Agadez
47008 ---- CHONGJIN              41.47  129.49    42 
47016 ---- HYESAN                41.24  128.10   715 Istanbul
47041 ---- HAMHEUNG              39.56  127.33    15 Balıkesir
47050 ---- ANJU                  39.37  125.39    34 
47055 ---- WONSAN                39.11  127.26    35 Izmir
47058 ZKPY PYONGYANG             39.02  125.47    36 
47101 ---- CHUNCHON              37.54  127.44    74 Aydın
47105 ---- KANGNUNG              37.45  128.53    27 Denizli
47106 RKSB TONGHAE/RADAR         37.30  129.08    40 Denizli
47108 RKSL SEOUL                 37.34  126.58    86 
47114 ---- WONJU                 37.20  127.57   149 Muğla
47127 ---- CHUNGJU               36.58  127.57   113 
47133 RKTD TAEJON                36.18  127.24    77 
47136 ---- ANDONG                36.33  128.43   139 
47138 ---- POHANG                36.02  129.23     6 
47143 RKTT TAEGU                 35.53  128.37    58 
47146 RKTC CHONJU                35.49  127.09    54 
47152 ---- ULSAN                 35.33  129.19    32 
47156 ---- KWANGJU               35.10  126.53    70 
47189 ---- SOGWIPO               33.14  126.34    52 
47407 ---- ASAHIKAWA             43.46  142.22   116 Karatschai-Tscherkessien
47412 RJCO SAPPORO               43.03  141.20    17 
47430 ---- HAKODATE              41.49  140.45    43 
47575 ---- AOMORI / HONSHU       40.49  140.46     3 Rize
47584 ---- MORIOKA               39.42  141.10   155 Erzurum
47590 ---- SENDAI                38.16  140.54    39 Diyarbakır
47598 ---- ONAHAMA               36.57  140.54     3 Al-Hasaka
47604 ---- NIIGATA               37.55  139.03     2 Şanlıurfa
47610 ---- NAGANO                36.40  138.12   418 Aleppo
47618 ---- MATSUMOTO             36.15  137.58   610 Aleppo
47662 RJTD TOKYO NARITA          35.41  139.46     5 Gouvernement Deir ez-Zor
47746 ---- TOTTORI / HONSHU      35.29  134.14    15 
47765 ---- HIROSHIMA             34.24  132.28    53 
47772 ---- OSAKA                 34.41  135.31    23 
47807 ---- FUKUOKA               33.35  130.23     3 
47815 RJFO OITA                  33.14  131.37     5 
47827 ---- KAGOSHIMA             31.33  130.33     4 
47830 ---- MIYAZAKI              31.55  131.25     6 
47893 ---- KOCHI                 33.34  133.32     1 
47895 ---- TOKUSHIMA / SHIKOKU   34.04  134.35     6 
48042 ---- MANDALAY              21.59   96.06    74 Mandalay-Division
48062 VYSW SITTWE                20.08   92.53     4 Rakhaing-Staat
48097 ---- YANGON                16.46   96.10    14 Rangun
48327 VTCC CHIANG MAI            18.47   98.59   312 Chiang Mai
48429 VTBS BANGKOK/SUVARNABHUMI  13.41  100.46     2 Sahel
48455 ---- BANGKOK               13.44  100.34     3 Sahel
48456 VTBD BANGKOK/DON MUANG     13.55  100.36     4 Tillabéri
48461 ---- PHATTHAYA             12.55  100.52    59 Est
48475 ---- HUA HIN               12.35   99.57     5 Prachuap Khiri Khan
48550 ---- KOH SAMUI              9.27  100.02     4 Northern Region
48564 VTSP PHUKET                 7.53   98.24     2 Phuket
48569 ---- HAT YAI                6.55  100.26    27 Volta Region
48601 WMKP PENANG-BAYANLEPAS      5.18  100.15     3 
48620 ---- SITIAWAN               4.13  100.42     7 
48647 WMKK KUALA LUMPUR           3.07  101.33    27 
48657 ---- KUANTAN                3.37  103.13    18 
48698 WSSS SINGAPUR               1.22  103.59     5 
48820 VVNB HANOI                 21.01  105.48     6 Tamanrasset
48855 VVDN DA NANG               16.02  108.11     7 Agadez
48900 VVTS SAIGON                10.49  106.40     5 Kaduna
48930 ---- LUANG-PRABANG         19.53  102.08   305 Region Kidal
48940 ---- VIENTIANE             17.57  102.34   171 Region Gao
48966 ---- SIEMREAP              13.22  103.51    15 Dosso
48991 VDPP PHNOM-PENH/POCHENT.   11.33  104.51    10 Kebbi
50774 ---- YICHUN (NORTH)        47.43  128.54   232 Rajon Rezina
50854 ---- ANDA                  46.23  125.19   150 Kreis Harghita
50953 ZYHB HARBIN                45.45  126.46   143 Kreis Vrancea
51463 ZWWW URUMQI                43.47   87.37   919 Xinjiang
51709 ZWSH KASHI                 39.28   75.59  1291 Xinjiang
51730 ---- ALAR                  40.30   81.03  1013 Xinjiang
51765 ---- TIKANLIK              40.38   87.42   847 Xinjiang
51818 ---- PISHAN                37.37   78.17  1376 Xinjiang
52436 ---- YUMENZHEN             40.16   97.02  1527 Gansu
52495 ---- BAYAN MOD             40.45  104.30  1329 
52866 ---- XINING                36.37  101.46  2262 
52889 ZLLL LANZHOU               36.03  103.53  1518 Bouira
53487 ZBDT DATONG                40.06  113.20  1069 
53513 ---- LINHE                 40.46  107.24  1041 
53698 ---- SHIJIAZHUANG          38.15  114.25    81 
53959 ---- YUNCHENG              35.02  111.01   376 
54102 ZBXH XILINHOT              43.57  116.04   991 Gespanschaft Šibenik-Knin
54161 ---- CHANGCHUNG            43.54  125.13   231 Kreis Teleorman
54218 ZBCF CHIFENG               42.16  118.58   572 Gemeinde Bar
54324 ---- CHAOYANG              41.33  120.27   167 Qark Dibra
54342 ---- SHENYANG              41.46  123.26    43 Blagoewgrad
54423 ---- CHENGDE               40.58  117.55   374 
54471 ---- YINGKOU               40.40  122.12     4 Decentralized Administration of Macedonia and Thrace
54497 ---- DANDONG               40.05  124.20    14 
54511 ZBAA PEKING                39.56  116.17    55 Kalabrien
54527 ---- TIANJIN               39.06  117.10     5 
54662 ZYTL DALIAN                38.54  121.38    97 Decentralized Administration of Thessaly and Central Greece
54753 ---- LONGKOU               37.37  120.19     5 
54823 ZSTN JINAN                 36.36  117.03   169 
54843 ---- WEIFANG               36.42  119.05    31 
54857 ZSQD QUINGDAO              36.04  120.20    77 
55472 ---- XAINZA                30.57   88.38  4670 Autonomes Gebiet Tibet
55578 ---- XIGAZE                29.15   88.53  3837 Autonomes Gebiet Tibet
55591 ---- LHASA                 29.40   91.08  3650 Autonomes Gebiet Tibet
56187 ---- WENJIANG              30.42  103.50   541 Ghardaia
56196 ---- MIANYANG              31.28  104.41   472 Ouargla
56571 ---- XICHANG               27.54  102.16  1599 Tamanrasset
56778 ZPPP KUNMING/WUJIABA       25.01  102.41  1892 Tamanrasset
57025 ---- FENGXIANG             34.31  107.25   781 Tebessa
57036 ---- XI'AN                 34.18  108.56   398 Gouvernement Gafsa
57083 ZHCC ZHENGZHOU             34.43  113.39   111 
57245 ---- ANKANG                32.43  109.02   291 Gouvernement Kebili
57411 ---- NANCHONG              30.48  106.05   310 Ouargla
57461 ---- YICHANG               30.42  111.18   134 Munizip Nalut
57494 ---- WUHAN                 30.37  114.08    23 Munizip Misrata
57516 ---- CHONGQING             29.31  106.29   351 Illizi
57598 ---- YINING                29.02  114.35   147 Munizip al-Dschufra
57662 ---- CHANGDE               29.03  111.41    35 Munizip Nalut
57687 ---- CHANGSHA              28.14  112.52    68 Ash Shati
57793 ---- YICHUN                27.48  114.23   129 Ash Shati
57816 ZUGY GUIYANG               26.29  106.39  1222 Illizi
57957 ---- GUILIN                25.20  110.18   166 Munizip Ghat
57972 ---- CHENZHOU              25.48  113.02   185 Murzuk
58027 ZSXZ XUZHOU                34.17  117.09    42 
58040 ---- GANYU                 34.51  119.08    10 
58221 ZSBB BENGBU                32.57  117.22    22 
58238 ZSNJ NANJING               31.44  118.51    12 
58362 ZSPD SHANGHAI PUDONG       31.24  121.28     8 Munizip al-Mardsch
58424 ---- ANQING                30.32  117.03    20 Munizip Surt
58457 ZSHC HANGZHOU              30.14  120.10    43 Munizip al-Wahat
58477 ---- DINGHAI               30.02  122.07    37 Munizip al-Wahat
58527 ZSJD JINGDEZHEN            29.18  117.12    60 Munizip al-Dschufra
58752 ---- RUI'AN                27.47  120.39    38 Munizip al-Wahat
58847 ---- FUZHOU                26.05  119.17     9 Kufra-Oasen
58968 RCTP TAIBEI                25.02  121.31     9 Kufra-Oasen
59046 ---- LIUZHOU               24.21  109.24    97 Illizi
59134 ZSAM XIAMEN                24.29  118.05   139 Murzuk
59211 ---- BAISE                 23.54  106.36   175 Tamanrasset
59287 ZGGG GUANGZHOU             23.08  113.19     8 Agadez
59316 ---- SHANTOU               23.21  116.40     4 Murzuk
59431 ZGNN NANNING               22.49  108.21   126 Tamanrasset
59493 ZGSZ SHENZHEN HUANGTIAN    22.38  113.49     4 Agadez
59644 ---- BEIHAI                21.29  109.06    16 Agadez
59658 ZGZJ ZHANJIANG             21.13  110.24    28 Agadez
59663 ---- YANGJIANG             21.52  111.58    22 Agadez
59758 ZGHK HAIKOU                20.02  110.21    24 Agadez
59948 ---- YA XIAN               18.14  109.31     7 Agadez
60005 GCLA LA PALMA              28.37  -17.45    29 Munizip al-Dschufra
60015 GCXO TENERIFE NORTE        28.28  -16.19   632 Munizip al-Dschufra
60020 ---- SANTA CRUZ DE TENE.   28.27  -16.15    35 Munizip al-Dschufra
60025 GCTS TENERIFE SUR          28.03  -16.34    64 Munizip al-Dschufra
60030 GCLP LAS PALMAS            27.56  -15.23    24 Ash Shati
60035 GCFV FUERTEVENTURA         28.27  -13.52    22 Ash Shati
60040 GCRR LANZAROTE             28.57  -13.36    14 Ash Shati
60630 DAUI IN-SALAH              27.14    2.30   268 Tamanrasset
60680 DAAT TAMANRASSET           22.47    5.31  1378 Tamanrasset
61024 DRZA AGADEZ                16.58    7.59   501 Agadez
61052 DRRN NIAMEY/DIORI HAMANI   13.29    2.10   223 Niger
61291 GABS BAMAKO                12.32   -7.57   380 Region Sikasso
61415 GQPP NOUADHIBOU            20.56  -17.02     5 Region Tibesti
61442 GQNN NOUAKCHOTT            18.06  -15.57     2 Region Tibesti
61641 GOOY DAKAR                 14.44  -17.30    27 Region Barh El Gazel
61701 GBYD BANJUL/YUNDUM         13.21  -16.48    36 Region Barh El Gazel
61766 GGOV BISSAU                11.53  -15.39    39 Region Chari-Baguirmi
61832 GUCY CONAKRY/GBESSIA        9.34  -13.37    26 Nord
61856 GFLL FREETOWN               8.37  -13.12    25 Nord
61901 ---- ST. HELENA           -15.56   -5.04   435 Timbuktu
61902 FHAW ASCENSION             -7.58  -14.24    86 Provinz Zaire
61967 FJDG DIEGO GARCIA          -7.18   72.24     1 
61980 FMEE SAINT-DENIS          -20.53   55.31    21 al-Wusta
61988 FIMR RODRIGUES            -19.41   63.25    58 
61990 FIMP PLAISANCE            -20.26   57.40    55 al-Wusta
62259 ---- TAZERBO               25.48   21.08   260 Kufra-Oasen
62405 HELX LUXOR                 25.40   32.42    93 Aswan
62414 HESN ASSUAN                23.58   32.47   192 Aswan
62423 ---- FARAFRA               27.03   27.59    82 Al-Wadi al-dschadid
62463 HEGN HURGHADA              27.09   33.43    16 Al-Bahr al-ahmar
62641 HSPN PORT SUDAN            19.35   37.13     3 al-Bahr al-ahmar
62721 HSSS KHARTOUM              15.36   32.33   382 al-Chartum
62730 HSKA KASSALA               15.28   36.24   500 Kassala
62760 HSFS EL FASHER             13.37   25.20   730 Schamal Darfur
62790 HSNL NYALA                 12.03   24.53   655 Dschanub Darfur
62941 HSSJ JUBA                   4.52   31.36   460 Central Equatoria
63125 HDAM DJIBOUTI              11.33   43.09    13 Dschibuti
63170 HCMH HARGEISA               9.30   44.05  1326 Woqooyi Galbeed
63175 HCMV BURAO                  9.31   45.34  1032 Togdheer
63450 HAAB ADDIS ABABA            8.59   38.48  2324 Addis Abeba
63471 HADR DIREDAWA               9.36   41.51  1260 Dire Dawa
63658 HUSO SOROTI                 1.43   33.37  1123 Eastern Region
63705 HUEN ENTEBBE                0.03   32.27  1155 Zentraluganda
63710 HKKR KERICHO               -0.22   35.21  2184 Uasin Gishu County
63733 HIMU MUSOMA                -1.30   33.48  1147 Eastern Region
63740 HKJK NAIROBI               -1.19   36.55  1624 Murang'a County
63791 HTKJ KILIMANJARO AIRPORT   -3.25   37.04   891 Kajiado County
63820 HKMO MOMBASA               -4.02   39.37    57 Mombasa County
63870 HTZA ZANZIBAR/KISAUNI      -6.13   39.13    15 Unguja Kaskazini
63894 HTDA DAR ES SALAAM AIRP.   -6.52   39.12    55 
63980 FSIA SEYCHELLES INT.       -4.40   55.31     3 
64005 FZEA MBANDAKA               0.03   18.16   345 Équateur
64210 FZAA KINSHASA/NDJILI       -4.23   15.26   309 Brazzaville
64220 ---- KINSHASA              -4.22   15.15   445 Brazzaville
64387 HRYR KIGALI                -1.58   30.07  1491 Western Region
64390 HBBA BUJUMBURA             -3.19   29.19   782 Cibitoke
64400 FCPP POINTE-NOIRE          -4.49   11.54    17 
64450 FCBB BRAZZAVILLE           -4.15   15.15   319 Brazzaville
64500 FOOL LIBREVILLE             0.27    9.25    12 Ästuar
64650 FEFF BANGUI                 4.24   18.31   365 Erzbistum Bangui
64700 FTTJ NDJAMENA              12.08   15.02   295 Erzbistum N’Djaména
64756 FTTC ABECHE                13.51   20.51   549 Wadai
64910 FKKD DOUALA                 4.00    9.44    10 Littoral
65046 DNKN KANO                  12.03    8.32   476 Kano
65082 DNMA MAIDUGURI             11.51   13.05   354 Borno
65125 DNAA ABUJA                  9.15    7.00   344 Federal Capital Territory
65201 DNMM LAGOS/IKEJA            6.35    3.20    40 Lagos
65344 DBBB COTONOU                6.21    2.23     5 Littoral
65387 DXXX LOME                   6.10    1.15    20 Region Maritime
65401 DGLN NAVRONGO              10.54   -1.06   203 Upper East Region
65472 DGAA ACCRA                  5.36   -0.10    68 
65503 DFFD OUAGADOUGOU           12.21   -1.31   316 Centre-Est
65528 DIOD ODIENNE                9.30   -7.34   434 Savanes
65545 DIBU BONDOUKOU              8.03   -2.47   369 Brong-Ahafo Region
65548 DIMN MAN                    7.23   -7.31   339 Sassandra-Marahoué
65557 ---- GAGNOA                 6.08   -5.57   205 Lagunes
65562 DIDK DIMBOKRO               6.39   -4.42    92 Comoé
65578 DIAP ABIDJAN                5.15   -3.56     7 Western Region
66160 FNLU LUANDA                -8.51   13.14    74 Provinz Zaire
67002 ---- HAHAYA AIRPORT       -11.32   43.16    29 
67009 ---- DIEGO-SUAREZ         -12.21   49.18   114
67027 FMNM MAJUNGA              -15.40   46.21    26 Gouvernement Ma'rib
67083 FMMI ANTANANARIVO         -18.48   47.29  1279 Nadschran
67113 FMMH MAHANORO             -19.50   48.48     5 asch-Scharqiyya
67137 FMSF FIANARANTSOA         -21.27   47.06  1115 Provinz Riad
67237 FQNP NAMPULA              -15.06   39.17   438 Debub
67295 FQCH CHIMOIO              -19.07   33.28   731 Nahr an-Nil
67315 FQVL VILANCULOS           -22.06   35.19    20 
67323 FQIN INHAMBANE            -23.52   35.23    14 Al-Bahr al-ahmar
67341 FQMA MAPUT0/MAVALANE      -25.55   32.34    39 Al-Wadi al-dschadid
67561 FLND NDOLA                -13.00   28.39  1269 Schamal Kurdufan
67586 ---- LILONGWE             -13.47   33.46  1229 Sannar
67665 FLLS LUSAKA               -15.19   28.27  1152 Schamal Kurdufan
67693 FWCL CHILEKA              -15.41   34.58   766 Kassala
67743 FLLI LIVINGSTONE          -17.49   25.49   985 Schamal Darfur
67761 ---- KARIBA               -16.31   28.53   518 Schamal Kurdufan
67775 ---- HARARE-KUTSAGA       -17.55   31.08  1479 asch-Schamaliyya
67843 FVFA VICTORIA FALLS       -18.06   25.51  1061 Schamal Darfur
67853 ---- HWANGE NATIONAL PARK -18.38   27.00  1079 Schamal Darfur
67964 ---- BULAWAYO             -20.09   28.37  1343 asch-Schamaliyya
67975 ---- MASVINGO             -20.04   30.52  1094 asch-Schamaliyya
68010 ---- OKAUKUEJO            -19.11   15.55  1102 Region Tibesti
68029 ---- KASANE               -17.49   25.09   968 Schamal Darfur
68032 FBMN MAUN                 -19.59   23.25   945 Kufra-Oasen
68104 FYRK WALVIS BAY           -22.53   14.26     7 Murzuk
68110 ---- WINDHUK              -22.34   17.06  1728 Region Tibesti
68112 FYWH WINDHOEK HOSEA INTL. -22.29   17.28  1719 Region Tibesti
68174 FAPI PIETERSBURG          -23.50   29.25  1228 Al-Wadi al-dschadid
68212 ---- HARDAP               -24.32   17.56  1108 Murzuk
68240 FBSK GABORONE AIRPORT     -24.13   25.55  1005 Al-Wadi al-dschadid
68262 ---- PRETORIA EENDRACHT   -25.45   28.11  1308 Al-Wadi al-dschadid
68296 ---- SKUKUZA              -24.59   31.36   263 Al-Wadi al-dschadid
68300 FYLZ LUDERITZ/DIAZ POINT  -26.38   15.06    23 Murzuk
68312 FYKT KEETMANSHOOP         -26.32   18.07  1067 Munizip al-Dschufra
68368 FAOR JOHANNESBURG         -26.08   28.14  1694 Al-Wadi al-dschadid
68438 FAKM KIMBERLEY            -28.48   24.46  1204 al-Butnan
68442 FABL BLOEMFONTEIN         -29.06   26.18  1354 Gouvernement Matruh
68461 FABM BETHLEHEM AIRPORT    -28.15   28.20  1686 Al-Dschiza
68513 ---- KOINGNAAS            -30.12   17.17    99 Munizip Surt
68523 ---- BRANDVLEI            -30.28   20.29   923 Munizip al-Wahat
68558 ---- BARKLY EAST          -30.56   27.36  1816 Gouvernement Matruh
68588 FADN DURBAN               -29.58   30.57     8 Al-Dschiza
68647 FAQT QUEENSTOWN           -31.55   26.53  1098 
68727 ---- BEAUFORT WEST        -32.21   22.33   902 Munizip Darna
68816 FACT KAPSTADT             -33.59   18.36    42 
68842 FAPE PORT ELIZABETH       -33.59   25.36    60 
68858 FAEL EAST LONDON          -33.02   27.50   125 
68906 FAGE GOUGH ISLAND         -40.21   -9.53    54 Distrikt Viseu
68916 ---- CAPE POINT           -34.21   18.30   208 
68928 FAMO MOSSEL BAY           -34.11   22.09    59 
68992 ---- BOUVET ISLAND        -54.24    3.18    28 
68994 FAME MARION ISLAND        -46.53   37.52    22 
70026 PABR BARROW/W.POST W.ROG.  71.18 -156.47    13 
70200 PAOM NOME                  64.30 -165.26     6 Autonomer Kreis der Chanten und Mansen/Jugra
70219 PABE BETHEL AK             60.47 -161.48    40 Oblast Swerdlowsk
70261 PAFA FAIRBANKS/INT.        64.49 -147.52   132 Oblast Archangelsk
70273 PANC ANCHORAGE INT.        61.10 -150.01    37 Republik Komi
70308 PASN ST.PAUL               57.09 -170.13    10 Oblast Tjumen
70361 PAYA YAKUTAT               59.31 -139.40    11 Oblast Wologda
70381 PAJN JUNEAU                58.22 -134.35     5 Oblast Nowgorod
71060 CWOA CAMSELL RIVER N.W.T.  65.37 -118.07   230 Norrbottens län
71066 ---- HIGH LEVEL,ALTA.      58.37 -117.10   338 
71078 CYYL LYNN LAKE MAN.        56.52 -101.05   357 
71090 CYCY CLYDE N.W.T.          70.29  -68.31    25 Autonomer Kreis der Jamal-Nenzen
71122 ---- BANFF,ALTA.           51.12 -115.33  1397 Woiwodschaft Niederschlesien
71123 CYEG EDMONTON INT.         53.18 -113.35   715 Brandenburg
71260 CYAM SAULT STE.MARIE ONT.  46.29  -84.30   187 Xinjiang
71395 CYHZ HALIFAX INT.          44.53  -63.31   145 Qysylorda
71474 ---- CLINTON,B.C.          51.09 -121.30  1057 Woiwodschaft Masowien
71515 CYHD DRYDEN                49.50  -92.45   413 Uws
71601 CYAW HALIFAX               44.38  -63.30    51 Qysylorda
71621 CYTR TRENTON               44.07  -77.32    85 Almaty
71622 CYFD BRANTFORD             43.02  -81.09   278 Xinjiang
71624 CYYZ TORONTO               43.40  -79.38   173 Almaty
71627 CYUL MONTREAL DORVAL       45.28  -73.45    31 Schambyl
71628 CYOW OTTAWA                45.19  -75.40   116 Almaty
71700 CYFC FREDERICTON           45.52  -66.32    17 Qysylorda
71707 CYQY SYDNEY,N.S.           46.10  -60.03    56 Qysylorda
71714 CYQB QUEBEC,QUE.           46.48  -71.23    70 Qaraghandy
71727 CYBG BAGOTVILLE            48.20  -71.00   159 Qaraghandy
71731 CYYB NORTH BAY             46.21  -79.26   358 Almaty
71749 CYQT THUNDER BAY ONT.      48.22  -89.19   199 Bajan-Ölgii
71801 CYYT ST.JOHNS NEUFUNDL.    47.37  -52.44   134 Atyrau
71803 CYQX GANDER                48.57  -54.34   151 Aktobe
71809 CYDF DEER LAKE NF.         49.13  -57.24    17 Aktobe
71811 CYZV SEPT-ILES QUE.        50.13  -66.16    55 Qostanai
71815 CYJT STEPHENVILLE NFLD.    48.32  -58.33     8 Aktobe
71816 CYYR GOOSE BAY NF.         53.19  -60.25    46 Chelyabinskaya Oblast
71827 CYGL LA GRANDE RIVIERE     53.38  -77.42   195 Oblast Nowosibirsk
71828 CYKL SCHEFFERVILLE QUE.    54.48  -66.49   522 Oblast Kurgan
71849 CYVZ DEER LAKE             49.55  -97.14   239 Tuwa
71852 CYWG WINNIPEG INT.AIRPORT  49.54  -97.14   239 Tuwa
71863 CYQR REGINA SASK.          50.26 -104.40   577 Wallonische Region
71869 CYPA PRINCE ALBERT SASK.   53.13 -105.40   428 Friesland
71877 CYYC CALGARY               51.07 -114.01  1077 Sachsen
71892 CYVR VANCOUVER             49.11 -123.10     3 Oblast Lwiw
71893 CYQQ COMOX B.C.            49.43 -124.54    24 Oblast Lwiw
71909 CYFB IQALUIT               63.45  -68.33    34 Autonomer Kreis der Chanten und Mansen/Jugra
71911 CYUS SHEPHERD BAY          68.49  -93.26    51 Region Krasnojarsk
71913 CYYQ CHURCHILL             58.44  -94.04    28 Region Krasnojarsk
71924 CYRB RESOLUTE              74.43  -94.59    40 Region Krasnojarsk
71925 CYCB CAMBRIDGE BAY N.W.T.  69.06 -105.08    25 
71926 CYBK BAKER LAKE N.W.T.     64.18  -96.05    18 Region Krasnojarsk
71934 CYSM FORT SMITH            60.01 -111.57   203 Innlandet
71957 CYEV INUVIK                68.18 -133.29    59 Oblast Murmansk
71966 ---- DAWSON,Y.T.           64.03 -139.08   370 Oblast Archangelsk
72201 KEYW KEY WEST              24.33  -81.45     2 Madhya Pradesh
72202 KMIA MIAMI                 25.49  -80.17     3 Uttar Pradesh
72203 KPBI WEST PALM BEACH       26.41  -80.07     6 Uttar Pradesh
72205 KMCO ORLANDO /JETPORT      28.26  -81.19    29 Lumbini
72206 KJAX JACKSONVILLE          30.30  -81.42     9 Autonomes Gebiet Tibet
72208 KCHS CHARLESTON            32.54  -80.02    14 Autonomes Gebiet Tibet
72211 KTPA TAMPA                 27.58  -82.32     8 Lumbini
72214 KTLH TALLAHASSEE           30.23  -84.22    25 Autonomes Gebiet Tibet
72218 KAGS AUGUSTA BUSH FLD.     33.22  -81.58    44 Autonomes Gebiet Tibet
72219 KATL ATLANTA GA.           33.39  -84.25   312 Autonomes Gebiet Tibet
72223 KMOB MOBILE/BATES F. AL.   30.41  -88.15    66 Autonomes Gebiet Tibet
72226 KMXF MONTGOMERY            32.18  -86.24    67 Autonomes Gebiet Tibet
72231 KMSY NEW ORLEANS           29.59  -90.15     1 Autonomes Gebiet Tibet
72243 KIAH HOUSTON TX.           29.58  -95.21    30 Autonomes Gebiet Tibet
72250 KBRO BROWNSVILLE/TX.       25.55  -97.25     7 Kachin-Staat
72253 KSAT SAN ANTONIO INT.      29.32  -98.28   247 Autonomes Gebiet Tibet
72254 KAUS AUSTIN                30.18  -97.42   193 Autonomes Gebiet Tibet
72259 KDFW DALLAS                32.54  -97.02   182 Qinghai
72261 KDLF DEL RIO               29.22 -100.55   310 Adrar
72266 KABI ABILENE/MUN. 18.      32.25  -99.41   542 Sichuan
72267 KLBB LUBBOCK 18.           33.39 -101.49   996 El Bayadh
72270 KELP EL PASO INT.          31.48 -106.24  1206 Ouargla
72274 KTUS TUCSON INT.           32.07 -110.56   802 Munizip Nalut
72278 KPHX PHOENIX AZ.           33.26 -112.01   344 
72290 KSAN SAN DIEGO/LINGBERG    32.44 -117.10     5 
72295 KLAX LOS ANGELES           33.56 -118.24    38 
72304 ---- CAPE HATTERAS, NC.    35.16  -75.33     2 
72306 KRDU RALEIGH/DURHAM NC.    35.52  -78.47   132 
72308 KORF NORFOLK/INT.,VA.      36.54  -76.12     8 Xinjiang
72314 KCLT CHARLOTTE/DOUG. NC    35.13  -80.56   228 Autonomes Gebiet Tibet
72315 ---- ASHEVILLE/MUN.,NC.    35.26  -82.33   659 Autonomes Gebiet Tibet
72327 KBNA NASHVILLE INT.        36.07  -86.41   180 Autonomes Gebiet Tibet
72334 KMEM MEMPHIS               35.03  -90.00   101 Qinghai
72340 KLIT NORTH LITTLE ROCK     34.50  -92.15   165 Qinghai
72351 KSPS WICHITA FALLS 18.     33.58  -98.29   309 Qinghai
72353 KOKC OKLAHOMA CITY         35.23  -97.36   395 Qinghai
72365 KABQ ALBUQUERQUE INT.      35.03 -106.37  1631 Khenchela
72370 ---- KINGMAN/MOHAVE,AZ.    35.16 -113.57  1050 
72374 ---- WINSLOW               35.01 -110.44  1505 sfaks
72376 ---- FLAGSTAFF AZ.         35.14 -111.49  2192 
72386 KLAS LAS VEGAS/MCCARRAN    36.05 -115.10   662 
72389 KFAT FRESNO/AIR TERM.      36.46 -119.43   100 
72403 KIAD WASHINGTON/DULLES     38.57  -77.27    95 Xinjiang
72405 KDCA WASHINGTON            38.51  -77.02     5 Xinjiang
72406 KBWI BALTIMORE             39.11  -76.40    48 Xinjiang
72407 KACY ATLANTIC CITY INT.    39.27  -74.34    21 Xinjiang
72408 KPHL PHILADELPHIA INT.     39.53  -75.15     4 Xinjiang
72411 KROA ROANOKE/MUN. VA.      37.19  -79.58   358 Xinjiang
72421 KCVG CINCINNATI OH.        39.03  -84.40   271 Xinjiang
72423 KSDF LOUISVILLE/STAND.KY.  38.11  -85.44   151 Xinjiang
72434 KSTL ST. LOUIS             38.45  -90.22   174 Xinjiang
72438 KIND INDIANAPOLIS IN/W.C.  39.44  -86.16   246 Xinjiang
72446 KMCI KANSAS CITY           39.17  -94.45   316 Gansu
72451 KDDC DODGE CITY/MUN.KS.    37.46  -99.58   791 Qinghai
72476 ---- GRAND JUNCTION,CO.    39.07 -108.32  1481 Sardinien
72487 ---- CALIENTE,NV.          37.37 -114.31  1335 Sizilien
72488 KRNO RENO                  39.30 -119.47  1344 
72492 KSCK STOCKTON METRO. CA.   37.54 -121.15     8 Decentralized Administration of Peloponnese, Western Greece and the Ionian
72494 KSFO SAN FRANCISCO         37.37 -122.23     6 Decentralized Administration of Peloponnese, Western Greece and the Ionian
72502 KEWR NEWARK                40.42  -74.10     5 Dschalalabat
72503 KLGA NEW YORK              40.46  -73.54     7 Dschalalabat
72509 KBOS BOSTON MA.            42.22  -71.02     6 Gebiet Talas
72519 KSYR SYRACUSE/HANCOCK NY.  43.07  -76.07   124 Almaty
72520 KPIT PITTSBURGH INT.       40.30  -80.13   367 Xinjiang
72524 KCLE CLEVELAND             41.25  -81.52   241 Xinjiang
72528 KBUF BUFFALO INT.,NY.      42.56  -78.44   220 Almaty
72530 KORD CHICAGO               41.59  -87.54   203 Xinjiang
72537 KDTW DETROIT               42.14  -83.20   195 Xinjiang
72546 KDSM DES MOINES/MUN. IA.   41.32  -93.39   294 Xinjiang
72547 KDBQ DUBUQUE/MUN. IA.      42.24  -90.42   328 Xinjiang
72564 KCYS CHEYENNE WY.          41.09 -104.49  1876 
72565 KDEN DENVER INT.           39.52 -104.40  1656 
72570 ---- CRAIG-MOFFAT,CO.      40.30 -107.32  1915 
72572 KSLC SALT LAKE CITY        40.47 -111.58  1288 
72594 KEKA EUREKA CA.            40.48 -124.10    13 Decentralized Administration of Macedonia and Thrace
72606 KPWM PORTLAND INT.         43.39  -70.19    23 Schambyl
72617 KBTV BURLINGTON/INT. VT.   44.28  -73.09   104 Schambyl
72640 KMKE MILWAUKEE             42.57  -87.54   220 Xinjiang
72658 KMSP MINNEAPOLIS           44.53  -93.13   256 Xinjiang
72662 KRAP RAPID CITY            44.03 -103.04   970 Okzitanien
72681 KBOI BOISE/MUN. ID.        43.34 -116.13   871 Gespanschaft Split-Dalmatien
72698 KPDX PORTLAND/INT. OR.     45.36 -122.36    12 Eisenmarkt
72734 KCIU SAULT STE.MARIE MI.   46.28  -84.22   218 Xinjiang
72745 KDLH DULUTH INT.           46.50  -92.11   436 Chowd-Aimag
72753 KFAR FARGO/HECTOR F. ND.   46.54  -96.48   274 Dsawchan-Aimag
72764 KBIS BISMARCK/MUN. ND.     46.46 -100.45   511 Nouvelle-Aquitaine
72779 KFCA KALISPELL,MT.         48.18 -114.16   906 Oberösterreich
72781 KYKM YAKIMA WA.            46.34 -120.32   332 Csongrád
72785 KGEG SPOKANE/INT. WA.      47.38 -117.32   721 Győr-Moson-Sopron
72793 KSEA SEATTLE               47.27 -122.18   130 Kreis Bihor
74486 KJFK NEW YORK JOHN F.K.    40.39  -73.47     4 Dschalalabat
76225 MMCU CHIHUAHUA             28.38 -106.05  1435 Illizi
76405 MMLP LA PAZ (MEX.)         24.16 -110.25    18 Illizi
76548 MMTM TAMPICO               22.13  -97.51     9 Shan-Staat
76612 MMGL GUADALAJARA           20.40 -103.23  1551 Tamanrasset
76644 MMMD AEROP.INT. MERIDA     20.59  -89.39     9 
76654 MMZO MANZANILLO,COL.       19.03 -104.19     3 Agadez
76680 ---- MEXICO CITY           19.24  -99.11  2309 Chiang Mai
76692 ---- VERACRUZ              19.09  -96.07    16 Bago-Division
76743 MMVA VILLAHERMOSA          17.59  -92.56    16 
76805 MMAA ACAPULCO              16.50  -99.56     3 Sukhothai
78016 TXKF BERMUDA NAVAL         32.22  -64.41     6 Helmand
78073 MYNN NASSAU                25.03  -77.28     3 Madhya Pradesh
78224 MUHA HAVANNA               22.59  -82.24    75 Chhattisgarh
78229 MUVR VARADERO              23.08  -81.17     3 Madhya Pradesh
78264 MUCU SANTIAGO DE CUBA      19.58  -75.51    55 Maharashtra
78325 ---- CASA BLANCA           23.09  -82.20    50 Chhattisgarh
78344 ---- CIENFUEGOS            22.08  -80.27    42 Madhya Pradesh
78388 MKJS MONT.BAY-SANGSTER     18.30  -77.55     1 Telangana
78397 MKJP KINGSTON              17.56  -76.47     3 Maharashtra
78439 MTPP PORT AU PRINCE        18.34  -72.18    31 
78458 MDPP PUERTO PLATA          19.45  -70.34     5 
78460 MDST SANTIAGO INT.         19.28  -70.42   183 
78479 MDPC PUNTA CANA            18.34  -68.22    12 
78485 MDSD LAS AMERICAS          18.26  -69.40    18 
78486 MDSO SANTO DOMINGO         18.26  -69.53    14 
78526 TJSJ SAN JUAN              18.26  -66.00     3 
78583 MZBZ BELIZE AIRPORT        17.32  -88.18     5 
78641 MGGT GUATEMALA AEROPUERTO  14.35  -90.31  1489 
78720 MHTG TEGUCIGALPA           14.03  -87.13  1007 
78741 MNMG MANAGUA SANDINO APT   12.09  -86.10    56 
78760 ---- PUNTARENAS             9.58  -84.50     5 
78762 MROC JUAN SANTAMARIA       10.00  -84.13   920 
78767 MRLM PUERTO LIMON          10.00  -83.03     5 
78774 ---- LIBERIA               10.37  -85.26    80 
78792 MPTO PANAMA TOCUMEN APT     9.03  -79.22    45 
78866 TNCM ST. MAARTEN           18.03  -63.07     4 
78897 TFFR LE RAIZET,GUADELOUPE  16.16  -61.31    11 
78925 TFFF LE LAMENTIN           14.36  -61.00     5 
78948 TLPL HEWANORRA AIRPORT     13.45  -60.57     3 
78954 TBPB GRANTLEY ADAMS        13.04  -59.29    50 
78958 TGPY GRENADA               12.00  -61.47     6 
78962 TTCP CROWN POINT           11.09  -60.50     3 
78970 TTPP TRINIDAD PIARCO INT.  10.36  -61.21    17 
78982 TNCA QUEEN BEATRIX-AIRP.   12.30  -70.01     3 
78988 TNCC HATO-AIRPORT          12.12  -68.58     9 
78990 TNCB FLAMINGO,BONAIRE      12.09  -68.17     6 
80022 SKCG CARTAGENA/RAFAEL NU.  10.27  -75.31     1 
80028 SKBQ BARRANQUILLA/ER.COR.  10.53  -74.47    14 
80110 SKMD MEDELLIN/OLAYA         6.13  -75.36  1490 
80112 SKRG RIO NEGRO/J.M.CORDO.   6.08  -75.26  2140 
80222 SKBO BOGOTA                 4.43  -74.09  2547 
80259 SKCL CALI/ALFONSO B.        3.33  -76.23   961 
80407 SVMC MARACAIBO             10.43  -71.44    66 
80415 SVMI CARACAS AEROPUERTO    10.36  -66.59    43 
80416 ---- CARACAS               10.30  -66.53   835 
80421 SVMG MARGARITA INTL.       10.55  -63.58    24 
80438 ---- MERIDA/VENEZUELA       8.36  -71.11  1479 
80472 SVVA VALENCIA              10.10  -67.56   430 
81001 ---- GEORGETOWN             6.48  -58.09     1 
81002 SYTM TIMEHRI/GUYANA         6.30  -58.15    28 
81405 SOCA CAYENNE/FR.GUYANA      4.50  -52.22     8 
81408 SOOG GEORGES DE L'OYAPOCK   3.53  -51.48     6 
82022 SBBV BOA VISTA              2.50  -60.42   140 
82193 SBBE BELEM/INTL.           -1.23  -48.29    16 
82332 SBEG MANAUS                -3.09  -59.59    84 
82579 SBTE TERESINA/INTL.        -5.03  -42.49    86 
82599 SBNT NATAL AEROPORTO       -5.55  -35.15    52 Manyara
82824 SBPV PORTO VELHO           -8.46  -63.55   102 
82899 SBRF RECIFE/INTL.          -8.08  -34.55    19 Iringa
82993 SBMO MACEIO                -9.31  -35.47   117 Iringa
83096 ---- ARACAJU              -10.55  -37.03     9 Amhara
83248 SBSV SALVADOR BAHIA       -12.54  -38.20     6 Amhara
83362 SBCY CUIABA/INTL.         -15.39  -56.06   187 
83378 SBBR BRASILIA/INTL.       -15.52  -47.56  1061 Gouvernement Hadramaut
83423 ---- GOIANIA              -16.41  -49.17   747 Gouvernement Hadramaut
83437 SBMK MONTES CLAROS        -16.43  -43.52   646 Gouvernement Sa'da
83483 ---- PIRAPORA             -17.20  -44.57   505 al-Dschauf
83579 SBAX ARAXA                -19.34  -46.56  1004 Provinz Riad
83698 SBCP CAMPOS               -21.45  -41.20    11 Provinz Mekka
83746 SBGL GALEAO (RIO/INTL.)   -22.49  -43.15     6 Provinz Riad
83766 ---- LONDRINA             -23.23  -51.11   566 asch-Scharqiyya
83780 SBSP SAO PAULO            -23.37  -46.39   802 Provinz Riad
83827 SBFI FOZ DO IGUACU AERP.  -25.31  -54.35   180 
83899 SBFL FLORIANOPOLIS AERP.  -27.40  -48.33     5 asch-Scharqiyya
83971 SBPA PORTO ALEGRE/INTL.   -30.00  -51.11     3 Fars
84008 ---- SAN CRISTOBAL         -0.54  -89.36     6 
84071 SEQU QUITO                 -0.08  -78.29  2794 
84203 SEGU GUAYAQUIL             -2.09  -79.53     4 
84377 ---- IQUITOS               -3.45  -73.15   125 
84401 SPUR PIURA                 -5.11  -80.36    49 
84628 SPJC LIMA                 -12.00  -77.07    12 Karnataka
84686 SPZO CUZCO                -13.33  -71.59  3248 
84735 ---- JULIACA              -15.29  -70.09  3826 
85201 SLLP LA PAZ/ALTO          -16.31  -68.11  4058 
85223 SLCB COCHABAMBA           -17.25  -66.11  2548 
85242 SLOR ORURO                -17.58  -67.04  3072 
85245 SLCZ SANTA CRUZ/EL TROMP. -17.48  -63.11   418 
85442 SCFA ANTOFAGASTA          -23.26  -70.26   135 Gujarat
85469 SCIP OSTERINSEL           -27.09 -109.25    51 Illizi
85574 ---- PUDAHUEL             -33.23  -70.47   474 Khyber Pakhtunkhwa
85577 SCEL SANTIAGO             -33.26  -70.41   520 Khyber Pakhtunkhwa
85682 SCIE CONCEPCION           -36.46  -73.04    12 Khyber Pakhtunkhwa
85799 SCTE PUERT0 MONTT         -41.26  -73.06    90 Dschalalabat
85874 SCBA BALMACEDA            -45.55  -71.42   522 Schambyl
85934 SCCI PUNTA ARENAS         -53.00  -70.51    37 Aqmola
85972 SCDR KAP HOORN            -56.36  -68.43    42 Oblast Tjumen
86218 SGAS ASUNCION             -25.16  -57.38   101 
86580 SUMU MONTEVID. CARRASCO   -34.50  -56.00    33 Semnan
87046 SASJ JUJUY AERO           -24.23  -65.05   921 
87222 SANC CATAMARCA AERO       -28.36  -65.46   454 Belutschistan
87289 SARL PASO DE LOS LIBRES   -29.41  -57.09    69 Kerman
87344 SACO CORDOBA/ARGENTINIEN  -31.19  -64.13   484 Helmand
87418 SAME MENDOZA AERO         -32.50  -68.47   705 Paktika
87506 SAMM MALARGUE AERO        -35.30  -69.35  1426 Baglan
87509 SAMR SAN RAFAEL AERO      -34.35  -68.24   745 Wardak
87576 SAEZ BUENOS AIRES AERO    -34.49  -58.32    20 Razavi-Chorasan
87585 SABE BUENOS AIRES         -34.35  -58.29    24 Razavi-Chorasan
87623 SAZR SANTA ROSA           -36.34  -64.16   190 Mary welaýaty
87692 SAZM MAR DEL PLATA        -37.56  -57.35    18 Nord-Chorasan
87750 SAZB BAHIA BLANCA         -38.44  -62.10    75 Lebap welaýaty
87765 SAZS BARILOCHE AERO       -41.09  -71.10   845 Provinz Namangan
87803 SAVE ESQUEL AERO          -42.56  -71.09   789 Schambyl
87860 SAVC COMODORO RINADAVIA   -45.47  -67.30    58 Südkasachstan
87938 SAWH USHUAIA              -54.48  -68.19    16 Nordkasachstan
88889 SFAL FALKLANDS            -51.49  -58.27    74 Baschkortostan
88903 ---- GRYTVIKEN            -54.17  -36.30     3 Oblast Tula
91165 PHLI LIHUE,KAUAI           21.59 -159.21    45 Dschanub asch-Scharqiyya
91182 PHNL HONOLULU              21.21 -157.56     2 ad-Dachiliyya
91190 PHOG KAHULUI,MAUI          20.54 -156.26    18 al-Wusta
91285 PHTO HILO/GEN.,LYMAN.      19.43 -155.04     9 Dhofar
91334 ---- TRUK,CAROLINE IS.      7.28  151.51     2 
91348 PTPN PONAPE                 6.58  158.13    37 
91366 PKWA KWAJALEIN/BUCHOLZ      8.44  167.44     2 
91517 YGGG HONIARA               -9.25  159.58    55 
91568 ---- ANEITYUM             -20.14  169.46     6 
91574 ---- CHESTERFIELD         -19.58  158.31     3 
91592 ---- NOUMEA               -22.17  166.27    69 
91680 NFFN NANDI (FIDSCHI)      -17.45  177.27    13 Karnataka
91753 NLWW HIHIFO               -13.14 -176.10    23 Karnataka
91765 ---- PAGO PAGO/INT.AIRP.  -14.20 -170.43     3 
91843 ---- RAROTONGA            -21.12 -159.49     7 
91925 NTMN ATUONA                -9.48 -139.02    51 Pwani
91938 NTAA TAHITI               -17.33 -149.37     2 Gouvernement Hadramaut
91961 ---- PITCAIRN ISLAND      -25.04 -130.06   264 Al-Wadi al-dschadid
92004 AYWK WEWAK W.O.            -3.35  143.40     4 
93110 ---- AUCKLAND AERO        -37.01  174.48     7 
93245 ---- TAUPO                -38.45  176.05   407 Xinjiang
93439 ---- WELLINGTON           -41.20  174.48    13 Gebiet Naryn
93615 ---- HOKITIKA             -42.43  170.59    45 Schambyl
93781 ---- CHRISTCHURCH AERO    -43.29  172.32    37 Schambyl
93831 NZQN QUEENSTOWN/INTL.     -45.01  168.44   358 Südkasachstan
93845 ---- INVERCARGILL         -46.25  168.19     2 Qaraghandy
94120 YPDN DARWIN               -12.24  130.52    31 Schamal Kurdufan
94131 ---- TINDAL               -14.31  132.23   134 an-Nil al-abyad
94203 YBRM BROOME AIRPORT       -17.57  122.13    17 Ennedi-Massiv
94238 ---- TENNANT CREEK AIRPOR -19.39  134.11   375 al-Bahr al-ahmar
94287 YBCS CAIRNS AIRPORT       -16.53  145.45     3 al-Dschauf
94294 YBTL TOWNSVILLE           -19.15  146.46     5 Nadschran
94300 YCAR CARNARVON AIRPORT    -24.52  113.40     4 Murzuk
94312 YPPD PORT HEDLAND         -20.22  118.38     9 Region Borkou
94326 YBAS ALICE SPRINGS        -23.48  133.54   537 Al-Bahr al-ahmar
94346 ---- LONGREACH AIRPORT    -23.26  144.17   192 Provinz Riad
94374 YBRK ROCKHAMPTON          -23.23  150.29    14 asch-Scharqiyya
94403 YGEL GERALDTON            -28.48  114.42    35 Munizip al-Dschufra
94461 ---- GILES (M.O.)         -25.02  128.18   580 Al-Wadi al-dschadid
94578 YBBN BRISBANE             -27.23  153.06     4 Fars
94604 ---- BUNBURY              -33.22  115.38     3 
94608 YPPH PERTH                -31.57  115.52    19 
94637 YPKG KALGOORLIE BOULDER   -30.47  121.27   367 Munizip al-Wahat
94653 ---- CEDUNA (AIRPORT M.O. -32.08  133.42    15 
94672 YPAD ADELAIDE             -34.56  138.31     6 Gouvernement Homs
94691 YBHI BROKEN HILL/INTL.    -32.00  141.28   292 Al-Anbar
94767 YSSY SYDNEY AIRPORT       -33.57  151.11     6 Isfahan
94791 YSCH COFFS HARBOUR        -30.19  153.07     6 Fars
94802 YABA ALBANY AIRPORT       -34.56  117.48    71 
94866 YMML MELBOURNE AIRPORT    -37.40  144.50   132 West-Aserbaidschan
94926 YSCB CANBERRA             -35.18  149.11   575 Hamadan
94975 ---- HOBART               -42.50  147.29     4 Dagestan
94995 YLHI LORD HOWE ISLAND     -31.32  159.04     5 Süd Chorasan
94998 ---- MACQUARIE ISLAND     -54.30  158.56     6 Baschkortostan
95448 YLST LEINSTER             -27.51  120.42   497 Munizip al-Wahat
95492 ---- THAGOMINDAH          -27.59  143.49   132 Hail
96001 WIAA SABANG                 5.52   95.19   126 Aceh
96011 WITT BANDA ACEH/BL.BINTG.   5.31   95.25    21 Aceh
96035 ---- MEDAN                  3.34   98.41    25 Sumatera Utara
96163 ---- PADANG/TABING         -0.53  100.21     3 
96315 ---- BRUNEI AIRPORT         4.56  114.56    22 Mambéré-Kadéï
96413 ---- KUCHING                1.29  110.20    27 Zentral-Süd
96471 ---- KOTA KINABALU          5.56  116.03     3 Ouham-Pendé
96491 ---- SANDAKAN               5.54  118.04    12 Ouham
96741 ---- JAKARTA               -6.07  106.52     2 
96749 WIII JAKARTA SOEKARNO      -6.07  106.39     8 
96933 WRSP SURABAYA/PERAK        -7.13  112.43     3 Provinz Zaire
96995 ---- CHRISTMAS ISLAND     -10.27  105.41   279 Niger
96996 ---- COCOS ISLAND AIRP.   -12.11   96.50     3 
97014 ---- MENADO/DR.SAM RATU.    1.32  124.55    80 Orientale
97180 ---- UJUNG PANDANG/HASAN.  -5.04  119.33    14 Bandundu
97230 WRRR DENPASAR-NGURAHRAI    -8.45  115.10     1 Uíge
97260 ---- SUMBAWA BESAR         -8.26  117.25     3 Bandundu
97390 WPXL DILLI/AIRPORT         -8.34  125.34     6 Katanga
98328 ---- BAGUIO                16.24  120.36  1500 Ennedi-Massiv
98425 RPLL MANILA                14.35  120.59    13 Region Wadi Fira
98429 ---- NINOY AQUINO/INTL.    14.30  121.00    14 Region Wadi Fira
98431 ---- CALAPAN               13.25  121.11    39 Wadai
98536 ---- ROMBLON               12.35  122.17    46 Region Sila
98618 ---- PUERTO PRINCESA        9.45  118.44    14 Region Moyen-Chari
98644 ---- TAGBILARAN             9.36  123.51     7 Dschanub Darfur
98646 ---- MACTAN                10.19  123.59    23 Dschanub Darfur
98753 ---- DAVAO                  7.08  125.39    17 Obermbomou
01149 ---- BASMOEN               66.20   14.06    34 Nordland
01194 ---- NARVIK                68.28   17.30    17 Nordland
01215 ---- HJELVIG (MYRBO)       62.37    7.14    35 Møre og Romsdal
02086 ---- LAINIO                67.46   22.21   315 Norrbottens län
02096 ---- PAJALA                67.12   23.23   165 Norrbottens län
02267 ---- ORNSKOLDSVIK          63.18   18.41    24 Västernorrlands län
02293 ESNS SKELLEFTEHAMN         64.38   21.05    46 Västerbottens län
02810 EFET ENONTEKIO             68.22   23.36   306 Lappland
02912 ---- VAASA                 63.06   21.35     4 Österbotten
04072 ---- FAGURHOLSMYRI         63.53  -16.39    46 Västernorrlands län
04094 ---- NUPUR                 64.42  -14.06    25 Jämtlands län
08513 ---- PONTA DELGADA         37.45  -25.40    35 
27615 UUDD MOSKAU/DOMODEDOVO     55.25   37.46   200 Oblast Moskau
28225 USPP PERM                  57.57   56.12   170 Region Perm
28429 ---- OKTJABRSKI            56.31   57.12   229 Region Perm
28642 USCC CELJABINSK-BLANDINO   55.18   61.32   230 Chelyabinskaya Oblast
28900 ---- SAMARA/KURUMOCH       53.30   50.09   145 Oblast Samara
29634 UNNT NOVOSIBIRSK           55.02   82.54   162 Oblast Nowosibirsk
34267 ---- DANILOVKA             50.22   44.07   102 Oblast Wolgograd
34731 URRR ROSTOV-NA-DONU        47.15   39.49    78 Oblast Rostow
35138 UWOR ORSK (SOUTH APT)      51.04   58.36   285 Oblast Orenburg
37235 ---- GROZNYJ               43.21   45.41   163 Tschetschenien
37260 ---- SUHUMI                42.52   41.08    13 
37549 UGTB TBILISI               41.41   44.57   490 Tbilisi
37789 UGEE YEREVAN               40.09   44.24   865 Armawir
40608 ORBM MOSUL                 36.19   43.09   223 Ninawa
40616 ---- ERBIL                 36.09   44.00   414 Arbil
40623 ---- SULAIMANIYA           35.33   45.27   853 Sulaimaniyya
40650 ORBS BAGHDAD               33.14   44.14    34 Al-Anbar
40689 ORMM BASRAH                30.34   47.47     2 Basra
40904 OAFZ FAIZABAD              37.07   70.31  1200 Badachschan
40913 OAUZ KUNDUZ                36.40   68.55   433 Kundus
40914 ---- BAGHLAN               36.05   68.39   550 Baglan
40922 OAMN MIMANA                35.56   64.46   815 Faryab
40938 ---- HERAT                 34.13   62.13   964 Herat
40990 ---- KANDAHAR              31.30   65.51  1010 Kandahar
41020 ---- JEDDAH (PORT)         21.24   39.12    10 Provinz Mekka
41216 ---- ABU DHABI             24.26   54.28     5 Abu Dhabi
41641 OPLA LAHORE AIRPORT        31.31   74.24   216 Punjab
41947 ---- KHULNA                22.47   89.32     4 Khulna
42042 VISR SRINAGAR              33.59   74.47  1664 
42181 VIDP NEU DELHI             28.34   77.07   220 Delhi
42295 ---- DARJEELING            27.03   88.16  2127 Westbengalen
42647 VAAH AHMEDABAD INTL        23.04   72.37    58 Gujarat
43057 ---- BOMBAY                18.54   72.49    10 
43194 VAGO GOA-DABOLIM           15.23   73.49    42 Goa
43372 VOTV TRIVANDRUM AIRPORT     8.28   76.57     4
47110 RKSS SEOUL AIRPORT         37.33  126.48    18 
47113 RKSI INCHEON/INTL.         37.28  126.26     7 
47153 RKPK PUSAN                 35.11  128.56     4 
47166 RKJM MOKPO                 34.45  126.23     4 
47182 RKPC CHEJU INT'L AIRPORT   33.31  126.30    36 
47545 RJSK AKITA AIRPORT         39.37  140.13    93 Erzincan
47569 RJSS SENDAI AIRPORT        38.08  140.55     1 Diyarbakır
47588 ---- YAMAGATA              38.15  140.21   153 Diyarbakır
47595 ---- FUKUSHIMA             37.45  140.28    69 Diyarbakır
47607 RJNT TOYAMA                36.42  137.12    17 Kilis
47616 ---- FUKUI                 36.03  136.14     7 Hatay
47635 RJNN NAGOYA AIRPORT        35.15  136.56    14 Hama
47670 ---- YOKOHAMA              35.26  139.39    39 Gouvernement Deir ez-Zor
47671 RJTT TOKYO INTERNATIONAL   35.33  139.46     6 Gouvernement Deir ez-Zor
47686 RJAA TOKYO AIRPORT         35.46  140.23    41 Gouvernement Deir ez-Zor
47687 ---- TOKIO                 35.38  139.51     5 Gouvernement Deir ez-Zor
47721 ---- FUJI AB               35.19  138.52   680 Gouvernement Homs
47759 ---- KYOTO                 35.01  135.44    41 
47768 ---- OKAYAMA / HONSHU      34.39  133.55    18 
47771 RJBB OSAKA AIRPORT         34.47  135.27    12 
47789 RJOA HIROSHIMA AIRPORT     34.26  132.55   331 
47819 ---- KUMAMOTO              32.49  130.43    39 
47836 RJFC YAKUSHIMA             30.22  130.40    37 Al-Minufiyya
47855 RJFU NAGASAKI AIRPORT      32.55  129.55     2 
47930 ---- NAHA                  26.11  127.39     3 Al-Wadi al-dschadid
48070 ---- MONGHSAT              20.33   99.16   572 Shan-Staat
48600 ---- LANGKAWI               6.20   99.44     8 Kedah
48618 ---- KUALA TRENGGANU        5.23  103.06     6 
48625 ---- IPOH                   4.34  101.06    39 
48632 ---- CAMERON HIGHLANDS      4.28  101.22  1545 
48694 WSAP PAYA LEBAR             1.21  103.54    20 
54543 ---- SHANHAIGUAN           39.58  119.48    12 
54774 ---- WEIHAI                37.30  122.07    61 Decentralized Administration of Peloponnese, Western Greece and the Ionian
58259 ---- NANTONG               32.06  120.52     1 Munizip al-Mardsch
58334 ---- WUHU                  31.20  118.21    16 
58343 ---- CHANGZHOU             31.46  119.57    15 Munizip Bengasi
58367 ZSSS SHANGHAI              31.24  121.28     8 Munizip al-Mardsch
59368 ---- XINGANG               23.06  121.22    37 Kufra-Oasen
59554 RCKH GAOXIONG              22.37  120.16    33 Kufra-Oasen
61214 GAKL KIDAL                 18.26    1.21   458 Region Kidal
61223 GATB TOMBOUCTOU            16.43   -3.00   263 Timbuktu
61226 GAGO GAO                   16.16   -0.03   265 Region Gao
61984 ---- SAINT-PIERRE         -21.20   55.29    52 az-Zahira
62460 HESH SHARM EL SHEIKH       27.58   34.23    49 Dschanub Sina
63021 HHAS ASMARA                15.17   38.55  2325 Maekel
63023 HHMS MASSAWA               15.37   39.27    10 Semienawi Kayih Bahri
63270 HCMK KISIMAYU              -0.22   42.26    10 Jubbada Hoose
63789 HTAR ARUSHA                -3.24   36.37  1387 Arusha
64008 FZEN BASANKUSU              1.13   19.48   360 Équateur
64950 FKYS YAOUNDE/NSIMALEN       3.50   11.31   751 Zentral
65660 GLRB MONROVIA/ROBERTS       6.15  -10.21     8 Nord-Ouest
68190 ---- PHALABORWA           -23.56   31.09   427 Al-Wadi al-dschadid
68239 ---- POMFRET              -25.50   23.32  1182 Kufra-Oasen
68476 ---- LADYSMITH            -28.34   29.46  1100 Al-Minya
70272 PAED ANCHORAGE ELMENDORF   61.15 -149.48    65 Republik Komi
71620 CYGK KINGSTON              44.13  -76.36    93 Almaty
71716 CZBF BATHURST              46.54  -71.30   168 Qaraghandy
71888 ---- JASPER,ALTA.          52.53 -118.04  1061 Woiwodschaft Kujawien-Pommern
71932 ---- UXBRIDGE WEST ON      44.06  -79.10   325 Almaty
72216 ---- ALBANY                31.32  -84.11    60 Autonomes Gebiet Tibet
72228 KBHM BIRMINGHAM-SHUTTLESW  33.33  -86.46   198 Autonomes Gebiet Tibet
72237 KRSW FORT MYERS            26.32  -81.45     9 Uttar Pradesh
72242 KGLS GALVESTON             29.18  -94.48     2 Autonomes Gebiet Tibet
72287 KONT ONTARIO INT.          34.03 -117.36   287 
72388 KSJC SAN JOSE INT.         37.22 -121.56    18 Decentralized Administration of Peloponnese, Western Greece and the Ionian
72466 KCOS COLORADO SPRINGS      38.49 -104.43  1873 
72467 KASE ASPEN                 39.13 -106.52  2382 
72469 ---- DENVER                39.45 -104.52  1625 
72482 KSMF SACRAMENTO INT.       38.42 -121.35     7 Decentralized Administration of Peloponnese, Western Greece and the Ionian
72493 KOAK OAKLAND INT.          37.45 -122.13     4 Decentralized Administration of Peloponnese, Western Greece and the Ionian
72512 KIAG NIAGARA FALLS         43.06  -78.57   180 Almaty
72522 KMDT HARRISBURG INT.       40.12  -76.46    94 Xinjiang
72527 KAGC PITTSBURGH/ALLEGH.    40.21  -79.56   382 Xinjiang
72554 KOFF OMAHA/OFFUTT AFB.     41.07  -95.54   315 Gansu
72568 KJAC JACKSON HOLE          43.36 -110.44  1964 Toskana
72610 KBGR BANGOR INT.           44.48  -68.50    59 Südkasachstan
72613 ---- MOUNT WASHINGTON NH.  44.16  -71.18  1909 Schambyl
72670 ---- CODY/MUN.WY.          44.31 -109.01  1551 Ligurien
72775 KGTF GREAT FALLS MT.       47.29 -111.22  1118 Bayern
76394 MMMY MONTERREY             25.52 -100.14   448 Adrar
76595 MMUN CANCUN                21.01  -86.51    10 Odisha
76679 MMMX MEXICO INT.           19.26  -99.05  2243 Chiang Mai
78118 MBJT TURKS ISLAND          21.27  -71.09    10 Gujarat
78119 MBSC SOUTH CAICOS          21.31  -71.32     4 Gujarat
78258 MUHG HOLGUIN               20.48  -76.19   106 Maharashtra
78315 MUPR PINAR DEL RIO         22.25  -83.41    41 Chhattisgarh
78337 MUTD TRINIDAD              21.47  -79.59    54 Madhya Pradesh
78339 MUOC CIEGO DE AVILA        22.31  -78.27     2 Madhya Pradesh
78373 ---- CIUDAD HABANA         22.58  -82.23    78 Chhattisgarh
78409 MTCH CAP-HAITIEN           19.45  -72.11     2 
78447 MTCA LES CAYES             18.11  -73.44     1 Maharashtra
78470 MDSJ SAN JUAN D.L. MAGUA.  18.49  -71.18   415 
78475 MDLR LA ROMANA             18.25  -68.56     8 
78547 TISX ST. CROIX             17.42  -64.48    17 
78550 TUPJ BEEF ISLAND,TORTOLA   18.27  -64.32     4 
78555 TIST ST. THOMAS            18.20  -64.58     3 
78662 ---- SAN SALVADOR          13.43  -89.12   698 
78666 MSLP SAN SALVADOR AIRPORT  13.26  -89.03    25 
78861 TAPA COOLIDGE FIELD        17.07  -61.47    10 
78899 TFFM MARIE GALANTE         15.52  -61.16     5 
78946 ---- CASTRIES              14.02  -61.01    55 
82099 SBMQ MACAPA                 0.03  -51.04    17 
82191 ---- BELEM                 -1.27  -48.28    10 
82397 SBFZ FORTALEZA             -3.46  -38.36    26 Kitui County
82900 ---- RECIFE CURADO         -8.03  -34.55     7 Iringa
82915 SBRB RIO BRANCO            -9.58  -67.48   143 
83377 ---- BRASILIA             -15.47  -47.56  1158 Gouvernement Hadramaut
83583 SBBH BELO HORIZONTE       -19.51  -43.57   785 Provinz Asir
83611 SBCG CAMPO GRANDE/INTL.   -20.27  -54.37   583 asch-Scharqiyya
83648 ---- VITORIA              -20.19  -40.20     8 Provinz Mekka
83721 SBKP CAMPINAS-VIRACOPOS   -23.01  -47.09   661 Provinz Riad
83743 ---- RIO DE JANEIRO       -22.55  -43.10     5 Provinz Riad
83773 ---- AVARE                -23.06  -48.55   793 asch-Scharqiyya
83779 SBGR SAO PAULO/INTL.      -23.26  -46.28   750 Provinz Riad
83782 ---- SANTOS               -23.56  -46.20    14 Provinz Riad
83842 ---- CURITIBA             -25.26  -49.16   923 asch-Scharqiyya
83920 ---- SAO JOAQUIM          -28.17  -49.55  1402 
83968 SBCO PORTO ALEGRE CANOAS  -29.57  -51.09     8 Fars
85445 SCLE LA ESCONDIDA         -24.17  -69.08  3136 Sindh
86570 SUPE PUNTA DEL ESTE       -34.55  -54.55    20 Semnan
87839 ---- FARO PUNTA DELGADA   -42.46  -63.38    56 Provinz Navoiy
87903 ---- LAGO ARGENTINO AERO  -50.20  -72.18   223 Qaraghandy
91217 PGUM GUAM MARIANA IS.      13.33  144.50   110 Gouvernement Lahidsch
91530 ANAU NAURU INT.            -0.32  166.55     6 
91663 ---- SAVUSAVU AIRPORT     -16.48  179.20     3 Telangana
91930 NTTB BORA-BORA            -16.27 -151.45     4 al-Mahra
93119 NZAA AUCKLAND             -37.01  174.48     7 
93308 NZNP NEW PLYMOUTH         -39.01  174.11    28 Xinjiang
93436 NZWN WELLINGTON AIRPORT   -41.20  174.48    12 Gebiet Naryn
93780 NZCH CHRISTCHURCH         -43.29  172.33    38 Schambyl
93890 ---- DUNEDIN              -45.56  170.12     1 Schambyl
94035 AYPY PORT MORESBY          -9.26  147.13    42 
94387 YBUD BUNDABERG (BINGERA)  -24.54  152.19    27 
94463 ---- CURTIN SPRINGS       -25.19  131.45   488 Al-Wadi al-dschadid
94564 ---- RAINBOW BEACH        -25.55  153.06    10 
94587 ---- TABULAM              -28.45  152.27   555 Fars
94669 ---- PORT PIRIE           -33.11  138.01     3 Gouvernement Rif Dimaschq
94743 ---- MOUNT BOYCE AWS.     -33.37  150.16  1080 Isfahan
94768 ---- SYDNEY               -33.51  151.12    39 Isfahan
94774 ---- NEWCASTLE            -32.55  151.47    33 Isfahan
94828 YPOD PORTLAND             -38.19  141.28    82 Batman
94868 ---- MELBOURNE            -37.49  144.58    31 West-Aserbaidschan
94969 ---- LAUNCESTON           -41.25  147.07     5 
95367 YBMK MACKAY               -21.10  149.11     6 asch-Scharqiyya
96059 ---- PRAPAT-SIBISAMONT.     2.10   98.56  1200 Sumatera Utara
96747 WIIH JAKARTA HALIM P.      -6.15  106.54    30 
96853 ---- JOGYAKARTA/ADISUC.    -7.47  110.26   107 
97240 ---- AMPENAN               -8.32  116.04     3 Uíge
97290 ---- ENDEH                 -8.48  121.36     3 Westkasai
98748 ---- CAGAYAN DE ORO         8.29  124.38     5 Western Bahr el Ghazal
99953 ---- LONGBOAT KEY          27.23  -82.38     8 Uttar Pradesh
P0001 ---- INSEL BORACAY         11.59  121.55     4 Region Sila
P0002 ---- CHITWAN-PARK          27.35   84.10   150 Bagmati
P0003 ---- MAURITIUS STRAND     -20.18   57.30     0 al-Wusta
P0005 ---- STR.V.MOZAMBIQUE     -16.00   42.00     0 
P0014 ---- PALM SPRINGS (CF.)    33.45 -116.24   125 
P0015 ---- PUERTO VALLARTA       20.30 -105.15     5 Tamanrasset
P0046 ---- TORAJA-LAND           -2.59  119.54  1200 Équateur
P0047 ---- BANAUE/NORD-LUZON     17.01  121.00  1800 Ennedi-Massiv
P0048 ---- TONGARIO NATIONALP.  -39.15  175.30  1500 Xinjiang
P0049 ---- MOUNT COOK NAT.PARK  -43.35  170.15  2000 Schambyl
P0052 ---- ARBIL                 36.12   44.01   400 Arbil
P0094 ---- RONDESLOTTET          61.56    9.52  2178 Innlandet
P0315 ---- ARGUINEGUIN           27.45  -15.39    15 Ash Shati
P0316 ---- OGDEN                 41.14 -111.59   902 
P0317 ---- PARK CITY             40.39 -111.30  2117 
P0318 ---- HEBER CITY            40.31 -111.25  1670 
P0319 ---- PROVO                 40.15 -111.40  1388 
P0320 ---- SUEDL. ISLAS MARIAS   21.00 -107.00     0 Tamanrasset
P0321 ---- WESTL. LOS ANGELES    32.00 -119.00     0 
P0322 ---- WESTL. DAVENPORT      37.00 -123.00     0 Decentralized Administration of Peloponnese, Western Greece and the Ionian
P0323 ---- WESTL. ENSENADA       48.00 -130.00     0 Odessa
P0324 ---- OBERER SEE            47.13  -86.23     0 Xinjiang
P0337 ---- SAN PEDRO DE MACORIS  18.30  -69.18     5 
P0338 ---- S.FRANCI. DE MACORIS  19.19  -70.15   116 
P0339 ---- CONCEPCION D.L. VEGA  19.13  -70.31    71 
P0340 ---- GONAIVES              19.27  -72.41     6 
P0342 ---- NATIONALPARK JARAGUA  17.37  -71.25     0 
P0343 ---- NAT.PK. MTE. CHRISTI  19.52  -71.39     0 
P0344 ---- NAT.PK. LOS HAITISES  19.05  -69.36     0 
P0345 ---- NT.P.SIERRA BAHORUCO  18.15  -71.40     0 
P0396 ---- ARE                   63.23   13.12   371 Jämtlands län
P0398 ---- FUNAESDALEN           62.30   12.36   582 Jämtlands län
P0400 ---- RIKSGRAENSEN          68.26   18.09   400 Norrbottens län
P0407 ---- BEAR MOUNTAIN         35.11 -118.37  2000 
P0408 ---- VAIL                  39.38 -106.22  2400 
P0418 ---- SULEJA                 9.02    7.27   480 Federal Capital Territory
P0479 OIIE TEHERAN/IMAM KHOMEI.  35.25   51.09  1008 Teheran
P0480 RJGG CHUBU CENTRAIR        34.51  136.48     4 Gouvernement Homs
P0485 ---- LOLENGI                0.09   21.00   380 Équateur
P0486 ---- OHARA                 35.14  140.23    20 Gouvernement Deir ez-Zor
P0517 ---- USINSK                66.00   57.33    78 Republik Komi
P0519 ---- JINING / SHANDONG     35.24  116.34    44 
P0520 ---- SAO SEBASTIAO         -9.56  -36.33   228 Morogoro
P0522 ---- RAAHE                 64.41   24.29     5 Nordösterbotten
P0526 ---- KOGALYM               62.14   74.32    77 Autonomer Kreis der Chanten und Mansen/Jugra
P0528 ---- SAO LUIZ             -24.06  -53.14   360 
P0530 ---- KOKKOLA               63.50   23.08    13 Mittelösterbotten
P0539 ---- VARKAUS               62.19   27.52    77 Nordsavo
P0542 ---- QUANZHOU              25.56  111.04   158 Munizip Ghat
P0558 ---- SUBIC                 14.52  120.14    20 Region Wadi Fira
P0562 ZYTX SHENYANG / TAOXIAN    41.34  123.28    60 Blagoewgrad
P0565 ZBTJ TIANJIN               39.06  117.10     5 
P0566 UACC ASTANA                51.07   71.22   347 
P0568 MMTO TOLUCA, MEX.          19.16  -99.41  2720 Lampang
P0569 KSFB ORLANDO / SANFORD A.  28.46  -81.15    17 Sudurpashchim Province
P0574 UKCW LUHANSK               48.25   39.23   194 Luhansk
P0575 CYMM FORT MCMURRAY ALTA.   56.39 -111.13   369 
W1164 ---- ISLA MARGARITA        11.00  -64.00     0 
W1261 ---- LEEW.ISLANDS-S        12.00  -61.00     0 
W1560 ---- LEEW.ISLANDS-N        15.00  -60.00     0 
W1655 ---- 16N55W                16.00  -55.00     0 
W1724 ---- KAP VERDEN            17.24  -24.29     0 Schamal Darfur
W1843 ---- 18N43W                18.00  -43.00     0 Provinz Asir
W1862 ---- WINDW.INSELN-E        18.00  -62.00     0 
W1965 ---- WINDW.INSELN-W        19.00  -65.00     0 
W2030 ---- 20N30W                20.00  -30.00     0 asch-Schamaliyya
W2180 ---- TRINIDAD/KUBA         21.00  -80.00     0 Maharashtra
W2476 ---- BAHAMAS               24.00  -76.00     0 Madhya Pradesh
W2520 ---- SWL.KANAREN           25.00  -20.00     0 Kufra-Oasen
W2617 ---- SDL.TENERIFFA         26.18  -16.44     0 Munizip al-Dschufra
W2778 ---- GRAND BAHAMA          27.00  -78.00     0 Uttar Pradesh
W2814 ---- SDL.FUERTEVENTURA     27.31  -13.52     0 Ash Shati
W2918 ---- NDL.LA PALMA          29.00  -18.00     0 Munizip Surt
W3015 ---- CANARIS-SUED          30.00  -15.00     0 Munizip Surt
W3417 ---- NDL.MADEIRA           34.00  -17.00     0 
W4215 ---- GEBIET 41             41.47  -15.28     0 Apulien
W4235 ---- GEBIET 43             42.21  -35.19     0 
W4325 ---- GEBIET 42             42.58  -24.49     0 Lowetsch
W4346 ---- GEBIET 44             42.52  -45.49     0 Tschetschenien
W4652 ---- GEBIET 50             45.41  -52.22     0 
W4715 ---- GEBIET 46             47.04  -14.42     0 Steiermark
W4726 ---- GEBIET 47             47.00  -25.42     0 Kreis Harghita
W4835 ---- GEBIET 48             47.31  -35.22     0 Saporischschja
W4845 ---- GEBIET 49             48.13  -45.21     0 Oblast Astrachan
W5215 ---- GEBIET 51             52.08  -15.08     0 Drossen
W5244 ---- GEBIET 54             52.25  -44.22     0 Oblast Pensa
W5325 ---- GEBIET 52             53.03  -25.10     0 
W5335 ---- GEBIET 53             52.53  -35.25     0 Oblast Orjol
W5353 ---- GEBIET 55             53.17  -52.50     0 Oblast Orenburg
W5413 ---- WESTL.IRLAND          53.39  -12.37     0 Mecklenburg-Vorpommern
W5646 ---- GEBIET 59             56.28  -45.35     0 Oblast de Níjni Novgorod
W5716 ---- GEBIET 56             57.22  -15.42     0 Kalmar län
W5720 ---- POSITION L            57.00  -20.00     0 
W5735 ---- GEBIET 58             57.01  -35.29     0 Oblast Twer
W5755 ---- GEBIET 60             57.11  -55.12     0 Region Perm
W5812 ---- WESTL.HEBRIDEN        57.34  -12.03     0 Västra Götalands län
W5825 ---- GEBIET 57             57.56  -24.53     0 Bezirk Mazsalaca
W5843 ---- KAP FARVELL           58.05  -43.28     0 Oblast Kostroma
W5922 ---- PENTL-FARV2           59.02  -21.43     0 
W6015 ---- PENTL-FARV1           60.00  -15.00     0 Örebro län
W6031 ---- PENTL-FARV3           60.28  -31.13     0 Oblast Leningrad
W6050 ---- SW-GROENLAND          60.16  -49.59     0 Republik Komi
W6138 ---- SE-GROENLAND          61.11  -38.30     0 Oblast Archangelsk
W6458 ---- DAVISSTR1             64.00  -58.00     0 Republik Komi
W6531 ---- DOHRNBANK             64.45  -30.33     0 Republik Karelien
W7041 ---- SUEDL.NANTUCKET IS.   41.00  -70.00     0 Taschkent
W7060 ---- DAVISSTR2             70.00  -60.00     0 Autonomer Kreis der Nenzen
W9853 ---- WINNIPEG-SEE          53.00  -98.00     0 Tuwa
E2834 ---- ROTES MEER            27.32   34.04     0 
E2835 ---- GOLF AKABA-S          28.25   34.35     0 
E6204 ---- SVINOY                62.20    4.23     0 
E6220 ---- BOTTENSEE             62.00   19.31     0 
E6300 ---- 63NORD00OST           63.04    0.07     0 
E6319 ---- BOTTENSEE-NW          62.48   18.48     0 
E6407 ---- FROYABANKEN           64.00    7.00     0 
E6421 ---- QUARK                 63.30   21.00     0 
E6524 ---- BOTTENWIEK            65.00   23.31     0 
E6602 ---- POSITION M            66.00    2.00     0 
E6609 ---- HALTENBANK            65.31    8.35     0 
E6914 ---- LOFOTEN               68.33   14.03     0 Nordland
E7225 ---- NORDKAP               72.09   25.17     0 
E7520 ---- BAERENINSEL           74.39   19.43     0 Spitzbergen
S4450 ---- ATLANTIK SUED1       -44.00  -50.00     0 
S4659 ---- ATLANTIK SUED2       -46.00  -59.00     0 Qysylorda
01008 ENSB SVALBARD              78.15   15.28    29 Spitzbergen
04320 BGDH DANMARKSHAVN          76.46  -18.40    11 Spitzbergen
20087 ---- OSTROV GOLOMJANNYJ    79.33   90.37     8 Region Krasnojarsk
71917 CWEU EUREKA UA N.W.T.      79.59  -85.56    10 
89002 ---- NEUMAYER             -70.40   -8.15    50 
89055 SAWB MARAMBIO             -64.14  -56.43   198 Republik Komi
89059 SCBO BERNARDO O'HIGGINS   -63.19  -57.54    10 Republik Komi
89512 ---- NOVOLAZAREVSKAJA     -70.46   11.50   119 
89532 ---- SYOWA                -69.00   39.35    18 
89564 ---- MAWSON               -67.36   62.53    10 Autonomer Kreis der Nenzen
89592 ---- MIRNYJ               -66.33   93.01    40 Region Krasnojarsk
89611 ---- CASEY                -66.17  110.31    40 
89642 AFDU DUMONT D'URVILLE     -66.40  140.01    41 Oblast Murmansk
89042 ---- SIGNY ISLAND         -60.43  -45.36     6 Oblast Wologda
89542 ---- MOLODEZNAYA          -67.40   45.51    40 
E7707 ---- SPITZBERGEN           76.58    7.19     0 
01059 ENNA BANAK/LAKSELV (AFB)   70.04   24.59     8 Troms og Finnmark
01112 ENBN BRONNOYSUND/BRONNOY   65.27   12.13     8 Nordland
23073 ---- NORILSK               69.24   88.04   126 Region Krasnojarsk
23205 ---- NAR?JAN-MAR           67.38   53.01   139 Autonomer Kreis der Nenzen
23226 ---- VORKUTA               67.30   63.58   133 Republik Komi
25913 ---- MAGADAN               59.33  150.47   132 Oblast Kirow
27199 ---- KIROV                 58.34   49.34   134 Oblast Kirow
27333 ---- KOSTROMA              57.44   40.47   136 Oblast Kostroma
28224 ---- PERM                  57.60   56.20   131 Region Perm
28411 ---- IZHEVSK               56.50   53.27   131 Udmurtische Republik
28506 ---- YELABUGA              55.46   52.03   135 Tatarstan
28676 ---- PETROPAVLOVSK         54.48   69.07   139 Nordkasachstan
34122 ---- VORONEZ               51.39   39.15   149 Oblast Woronesch
34172 ---- SARATOW               51.33   46.02   111 Oblast Saratow
34467 ---- VOLGOGRAD             48.47   44.20   133 Oblast Wolgograd
34691 ---- NOVYY USHTOGAN        47.54   48.48   137 Atyrau
34949 ---- STAVROPOL             45.07   42.05   451 Region Stawropol
35078 ---- ATBASAR               51.49   68.22   134 Aqmola
35671 ---- ZHEZKAZGAN            47.48   67.43   133 Qaraghandy
35700 ---- GUR?YEV               47.07   51.50   147 Atyrau
35796 ---- BALKHASH              46.53   75.00   129 Qaraghandy
36003 ---- PAVLODAR              52.18   76.56   131 Pawlodar
36428 ---- ULKEN NARYN           49.12   84.31   133 Ostkasachstan
36639 ---- URZHAR                47.07   81.37   132 Ostkasachstan
36821 ---- BAKANAS               44.50   76.16   134 Almaty
36859 ---- PANFILOV              44.10   80.04   136 Almaty
36927 ---- BALYKTSCHY (RYBACHE)  42.28   76.11   137 Gebiet Yssykköl
36974 ---- NARYN                 41.26   76.00   129 Gebiet Naryn
36985 UCFP KARAKOLKA             41.29   77.24  3080 Gebiet Yssykköl
37006 ---- NOVOROSSIJSK          44.43   37.51   136 Region Krasnodar
37177 ---- GAGRY                 43.15   40.16     7 
37272 ---- TKVARCHELI            42.50   41.40   266 
37279 ---- ZUGDIDI               42.31   41.53   134 Mingrelien und Oberswanetien
37308 ---- AMBROLAURI            42.32   43.08   136 Ratscha-Letschchumi und Niederswanetien
37395 ---- KUTAISI               42.15   42.38   135 Imeretien
37416 ---- CHINVALY              42.14   43.59   871 
37437 ---- DUSHETI               42.05   44.42   128 Mzcheta-Mtianeti
37514 ---- AKHALTSIKHE           41.39   43.00   139 Samzche-Dschawachetien
37531 ---- GORI                  41.60   44.07   132 Innerkartlien
37545 ---- TBILISI (TIFLIS)      41.45   44.46   140 Tbilisi
37566 ---- SAGAREDZO             41.44   45.20   806 Kachetien
37575 ---- ZAKATALY              41.34   46.40   132 
37609 ---- ASHOTSK               41.02   43.53   136 Schirak
37621 ---- BOLNISI               41.27   44.34   134 Niederkartlien
37651 UDSG SHIRAKI               41.25   46.15   801 Kachetien
37673 ---- KHACHMAZ              41.25   48.53   142 
37675 ---- KUBA                  41.22   48.31   131 
37686 ---- GYUMRI                40.46   43.51   145 Schirak
37693 ---- STEPANAVAN            41.00   44.24   140 Lori
37699 ---- APARAN                40.32   44.23   136 Aragazotn
37704 ---- VANADZOR              40.50   44.26   148 Lori
37711 ---- IDZHEVAN              40.52   45.09   136 Tawusch
37717 ---- SEVAN LAKE            40.34   45.00   138 Gegharkunik
37735 ---- GYANDJA               40.43   46.25   147 
37747 ---- YEVLAKH               40.38   47.09   133 
37749 ---- GEOKCHAY              40.39   47.45   127 
37756 ---- MARAZA                40.32   48.56   134 
37759 ---- SUMGAIT               40.38   48.38   134 
37785 ---- ASHTARAK              40.17   44.21   137 Aragazotn
37787 ---- ARMAVIR               40.08   43.54   149 Armawir
37871 ---- ARTASHAT              39.56   44.31   135 Ararat
37893 ---- AGDAM                 39.59   46.56   131 
37895 ---- STEPANAKERT           39.49   46.45   131 
37897 ---- SISIAN                39.30   46.02   134 Sjunik
37905 ---- ZHDANOVSK             39.46   47.45   149 
37959 ---- KAFAN                 39.12   46.27   133 
37972 ---- BILASUVAR             39.28   48.33   131 
37985 ---- LENKORAN?             38.44   48.50   142 
38062 ---- KYZYL-ORDA            44.51   65.30   129 Qysylorda
38111 ---- AKTAU                 43.38   51.11   138 Mangghystau
38141 ---- ZHASLYK               43.53   57.53   133 Karakalpakistan
38178 ---- AKBAYTAL              43.09   64.20   132 Provinz Navoiy
38232 ---- AK-KUDUK              42.58   54.06   129 Mangghystau
38264 ---- NUKUS CITY            42.29   59.37    77 Karakalpakistan
38328 ---- SHYMKENT (CHIMKENT)   42.19   69.42   131 Südkasachstan
38343 ---- KULAN                 42.57   72.45   125 Schambyl
38345 ---- TALAS                 42.31   72.13   133 Gebiet Talas
38388 ---- EKEZHE                41.02   57.46   133 Daşoguz
38392 ---- DASHOGUZ (TASHAUZ)    41.45   59.49   130 Daşoguz
38396 ---- URGENCH               41.35   60.39   131 Choresmien
38413 ---- TAMDYBULAK            41.44   64.37   137 Provinz Navoiy
38462 ---- PSKEM                 41.54   70.22   128 Taschkent
38511 ---- CHAGYL                40.47   55.20   134 Balkan welaýaty
38567 ---- NAVOI                 40.08   65.21   128 Provinz Navoiy
38579 ---- DZHIZAK               40.07   67.50   134 Provinz Jizzax
38583 ---- SYRDAR?YA             40.49   68.41   142 Provinz Sirdaryo
38599 ---- KHUDJAND              40.13   69.42   152 Sughd
38611 ---- NAMANGAN              40.59   71.35   474 Provinz Namangan
38613 ---- DZHALAL-ABAD          40.55   72.57   136 Dschalalabat
38616 ---- KARA-SUU              40.42   72.54   126 Osch
38618 ---- FERGANA               40.23   71.45   130 Provinz Fargʻona
38656 ---- YERBENT               39.19   58.36   129 Ahal welaýaty
38683 ---- BUHARA (BUKHARA)      39.47   64.29   130 Buchara
38687 ---- CHARDZHOU             39.05   63.36   132 Lebap welaýaty
38705 ---- PENDZHIKENT           39.30   67.36   130 Sughd
38713 ---- URA-TYUBE             39.54   68.59   132 Sughd
38750 ---- ESENGULY              37.28   53.58   159 Balkan welaýaty
38763 ---- SERDAR                38.59   56.17   159 Balkan welaýaty
38812 ---- KARSHI                38.48   65.46   127 Provinz Qashqadaryo
38851 ---- RASHT                 39.00   70.18   139 Der Republik unterstellte Bezirke
38856 ---- DARVAZ                38.28   70.47   129 Berg-Badachschan
38869 ---- IRHT                  38.10   72.38   132 Berg-Badachschan
38875 ---- KARAKUL?              39.01   73.33   138 Berg-Badachschan
38895 ---- MARY (BAYRAM-ALI)     37.36   62.11   133 Mary welaýaty
38911 ---- KERKI                 37.50   65.12   128 Lebap welaýaty
38933 ---- KURGAN-TYUBE          37.49   68.47   139 Chatlon
38947 ---- PYANDZH               37.15   69.05   134 Chatlon
38974 ---- SERAKHS               36.32   61.13   135 Ahal welaýaty
38987 ---- KUSHKA                35.17   62.21   130 Mary welaýaty
40001 ---- KAMISHLI              37.03   41.13   455 Al-Hasaka
40016 ---- HASSAKAH              36.30   40.45   307 Al-Hasaka
40039 ---- RAQQA                 35.56   39.01   245 Ar Raqqa
40045 ---- DEIR AZ ZAWR          35.19   40.09   215 Gouvernement Deir ez-Zor
40250 ---- H-4 IRWAISHED         32.30   38.12   683 Gouvernement Mafraq
40415 OEDF DAMMAM (KING FAHD IN  26.26   49.48    13 asch-Scharqiyya
47642 RJTY YOKOTA AIR BASE       35.45  139.21   141 Ar Raqqa
47808 RJFF FUKUOKA AIRPORT       33.35  130.27     9 
61202 GATS TESSALIT              20.15    0.59   494 Region Kidal
61265 GAMB MOPTI                 14.31   -4.05   276 Region Mopti
62771 ---- EL OBEID              13.10   30.14   574 Schamal Kurdufan
62810 ---- KADUGLI               11.00   29.43   499 Dschanub Kurdufan
62840 HSSM MALAKAL                9.33   31.39   387 Upper Nile
63451 HAHM HARAR MEDA             8.44   38.57  1900 Oromia
64810 ---- MALABO / BIOKO ISL.    3.45    8.46    50 Nordbioko
65510 DFOO BOBO DIOULASSO        11.10   -4.20   461 Hauts-Bassins
69777 KQTI TAJI (BAGDAD AIRPT.)  37.16   42.24   300 Şırnak
72204 KMLB ORLANDO MELBOURNE I.  28.06  -80.39    11 Uttar Pradesh
72356 KTUL TULSA (INT. AIRP.)    36.12  -95.53   207 Qinghai
72401 KRIC RICHMOND (BYRD AIRPO  37.31  -77.19    51 Xinjiang
72508 KBDL HARTFORD/BRADLEY INT  41.56  -72.41    53 Gebiet Talas
72543 KRFD ROCKFORD GREATER ROC  42.12  -89.06   224 Xinjiang
72677 KBIL BILLINGS (LOGAN INT.  45.48 -108.33  1092 Piemont
74783 KFLL FORT LAUDERDALE       26.04  -80.09    35 Uttar Pradesh
82240 SWPI PARINTINS             -2.37  -56.44    29 
82244 SBSN SANTARÉM              -2.25  -54.48    72 
82280 SBSL SÃO LUIZ              -2.32  -44.18    51 
82288 SBPB PARNAÍBA              -2.54  -41.44     5 Jubbada Hoose
82317 SBTF TEFÉ                  -3.22  -64.42    47 
82353 SBHT ALTAMIRA              -3.13  -52.13    74 
82400 SBFN FERNANDO DE NORONHA   -3.51  -32.25    56 Mwanza
82411 SBTT TABATINGA             -4.15  -69.56    85 
82425 SWKO COARI                 -4.05  -63.09    46 
82444 SBIH ITAITUBA              -4.15  -56.00    33 
82562 SBMA MARABÁ                -5.22  -49.08    95 
82564 SBIZ IMPERATRIZ            -5.32  -47.29   123 
82567 SBCJ CARAJAS               -6.07  -50.00   621 
82591 SBMS MOSSORO/DIX SEPT R.   -5.12  -37.22    23 Manyara
82598 SBSG NATAL                 -5.46  -35.12    45 Manyara
82610 SWEI EIRUNEPÉ              -6.40  -69.52   104 
82640 SBEK JACAREACANGA          -6.14  -57.47    98 
82659 SWGN ARAGUAÍNA             -7.06  -48.12   229 
82795 SBKG CAMPINA GRANDE        -7.14  -35.54   548 Dodoma
82798 SBJP JOÃO PESSOA           -7.06  -34.51     7 Singida
82965 SBAT ALTA FLORESTA         -9.52  -56.06   288 
82984 SBPL PETROLINA             -9.22  -40.34   375 
82986 SBUF PAULO AFONSO          -9.24  -38.13   253 Lindi
83065 SBPJ PALMAS               -10.17  -48.22   236 Sanaag
83095 SBAR ARACAJÚ              -10.59  -37.04     8 Amhara
83208 SBVH VILHENA              -12.42  -60.06   612 
83221 SDIY FEIRA DE SANTANA     -12.12  -38.58   232 Amhara
83242 SBLE LENÇÓIS              -12.33  -41.23   439 Afar
83344 SBQV VITÓRIA DA CONQUISTA -14.53  -40.48   875 
83349 SBIL ILHEUS               -14.49  -39.02     4 Debub
83359 SBBW BARRA DO GARÇAS      -15.52  -52.23   350 
83410 SBRD RONDONÓPOLIS         -16.28  -54.35   284 
83424 SBGO GOIÂNIA              -16.38  -49.13   747 Gouvernement Hadramaut
83460 SBPS PORTO SEGURO         -16.26  -39.05    51 Semienawi Kayih Bahri
83470 SWLC RIO VERDE            -17.55  -50.55   727 Gouvernement Hadramaut
83525 SBUL UBERLÂNDIA           -18.53  -48.14   945 Nadschran
83531 SNPD PATOS DE MINAS       -18.31  -46.26   940 Nadschran
83543 SBGV GOVERNADOR VALADARES -18.51  -41.56   263 Provinz Asir
83552 SBCR CORUMBÁ              -19.01  -57.40   130 al-Wusta
83576 SBUR UBERABA              -19.46  -47.58   808 asch-Scharqiyya
83618 SBTG TRÊS LAGOAS          -20.47  -51.42   313 asch-Scharqiyya
83635 SNDV DIVINÓPOLIS          -20.10  -44.52   789 Provinz Riad
83649 SBVT VITÓRIA              -20.15  -40.17     3 Provinz Mekka
83652 SBRP RIBEIRÃO PRETO       -21.08  -47.46   549 Provinz Riad
83659 SBDO DOURADOS             -22.14  -54.49   452 asch-Scharqiyya
83672 SBAU ARAÇATUBA            -21.12  -50.26   397 asch-Scharqiyya
83692 SBJF JUIZ DE FORA         -21.46  -43.22   939 Provinz Mekka
83703 SBPP PONTA PORA AEROPORTO -22.33  -55.42   660 az-Zahira
83716 SBDN PRESIDENTE PRUDENTE  -22.07  -51.23   436 asch-Scharqiyya
83719 SBCB CABO FRIO            -22.59  -42.02     7 Provinz Mekka
83722 SBBU BAURU/AREALVA        -22.21  -49.03   615 asch-Scharqiyya
83726 SDSC SAO CARLOS           -21.59  -47.53   856 asch-Scharqiyya
83755 SBRJ SANTOS DUMONT        -22.55  -43.10     3 Provinz Riad
83767 SBMG MARINGÁ              -23.25  -51.57   542 asch-Scharqiyya
83768 SBLO LONDRINA             -23.20  -51.08   569 asch-Scharqiyya
83809 SBSJ SÃO JOSÉ DOS CAMPOS  -23.14  -45.52   646 Provinz Riad
83818 SBST SANTOS AEROPORTO     -23.56  -46.18     3 Provinz Riad
83828 SBTD TOLEDO               -24.41  -53.42   562 
83837 SSZW PONTA GROSSA         -25.06  -50.10   868 asch-Scharqiyya
83840 SBCT CURITIBA             -25.32  -49.11   911 asch-Scharqiyya
83883 SBCH CHAPECO              -27.05  -52.38   687 
83891 SBLJ LAGES                -27.48  -50.20   937 
83905 SBJV JOINVILLE            -26.13  -48.48     5 asch-Scharqiyya
83914 SBPF PASSO FUNDO          -28.15  -52.24   684 Fars
83926 SBNF NAVEGANTES           -26.53  -48.39     5 asch-Scharqiyya
83928 SBUG URUGUAIANA           -29.47  -57.02    74 Kerman
83937 SBSM SANTA MARIA          -29.43  -53.42    85 Fars
83942 SBCX CAXIAS DO SUL        -29.12  -51.12   751 Buschehr
83981 SBBG BAGE/GUSTAVO KRAEMER -31.23  -54.07   180 Yazd
83985 SBPK PELOTAS              -31.47  -52.25    13 Isfahan
85244 SLVR SANTA CRUZ- VIRU     -17.39  -63.08   373 
86622 SSKW CACOAL               -11.27  -61.26   210 
86626 SBSI SINOP                -11.59  -55.34   371 
86645 SBSO SORRISO              -12.33  -55.43   380 
86652 SNBR BARREIRAS            -12.07  -45.02   470 
86676 SNVB VALENÇA              -13.21  -39.08   105 Tigray
86816 SBBT BARRETOS/CHAFEI AMS. -20.35  -48.36   578 asch-Scharqiyya
87155 SARE RESISTENCIA AIRPORT  -27.27  -59.03    52 Sistan und Belutschistan
87480 SAAR ROSARIO              -32.55  -60.47    25 Farah
89004 ---- SANAE-AWS            -71.40   -2.50   815 
89574 ---- PROGRESS             -69.23   76.23    14 Autonomer Kreis der Jamal-Nenzen
F9402 SBCA CASCAVEL             -25.00  -53.30   754 
F9403 SBCD CACADOR              -26.47  -50.56  1014 
F9404 SBCM CRICIÚMA             -28.44  -49.26    28 
F9405 SBCN CALDAS NOVAS         -17.44  -48.37   685 Gouvernement Hadramaut
F9406 SBDB BONITO               -21.23  -56.46   360 ad-Dachiliyya
F9407 SBGU GUARAPUAVA           -25.23  -51.13  1065 ar-Rayyan
F9408 SBIP IPATINGA             -19.28  -42.29   239 Provinz Asir
F9409 SBJA JAGUARUNA            -28.41  -48.04    37 Gouvernement Ahmadi
F9410 SBJI JI-PARANÁ            -10.52  -61.51   182 
F9411 SBJU JUAZEIRO DO NORTE     -7.13  -39.16   409 Dar es Salam
F9412 SBML MARILIA              -22.12  -49.56   647 asch-Scharqiyya
F9413 SBNM SANTO ÂNGELO         -28.17  -54.10   322 Fars
F9414 SBSR SÃO JOSÉ D. R. PRETO -20.49  -49.24   544 asch-Scharqiyya
F9415 SBTB PORTO DE TROMBETAS    -1.29  -56.24    88 
F9416 SBTC UNA                  -15.21  -39.00     6 Maekel
F9417 SBVG VAG                  -21.35  -45.28   923 Provinz Riad
F9418 SNTF TEIXEIRA DE FREITAS  -17.32  -39.41   105 
F9419 SSVV POLO TURISTICO        -2.54  -40.22     8 Garissa County
F9420 SULS MALDONADO            -34.51  -55.06    29 Semnan
F9421 SBCF BELO HORIZONTE AIRP. -19.20  -43.58   828 Provinz Asir
F9422 SBZM JUIZ DE FORA         -21.31  -43.10   411 Provinz Mekka
F9423 KAFW FORT WORTH-ALLIANCE,  32.59  -97.19   220 Qinghai
F9424 SBAE BAURU/AREALVA APT.    22.09  -49.04   594 asch-Scharqiyya
F9425 SBAC ARACATI               -4.34  -37.48    36 Taita-Taveta County
F9426 SBJE CRUZ/ARISTON PESSOA   -2.54  -40.21    73 Garissa County
F9427 SBME MACAE                -22.20  -41.46     3 Provinz Mekka
F9428 SBPG PONTA GROSSA         -25.11  -50.09   789 asch-Scharqiyya
F9429 SBPO PATO BRANCO          -26.13  -52.42   822 
F9430 SBAQ ARARAQUARA           -21.48  -48.08   711 asch-Scharqiyya
F9431 SSUM UMUARAMA             -23.48  -53.19   475 Abu Dhabi
F9432 SSPB PATO BRANCO AIRPORT  -26.13  -52.42   822 
F9433 SBVC GLAUBER DE ANDRADE   -15.54  -40.55   894 
N9609 ---- ABYEI                  9.36   28.26   400 
P0611 VGHS DHAKA ZIA INTL.       23.50   90.24     9 Dhaka
P0612 VOBL BANGALURU             13.11   77.42   889 Karnataka
P0613 VOCI COCHIN                10.09   76.24     9 Kerala
P0614 VOCL CALICUT               11.08   75.57   104 Kerala
P0615 VOHS HYDERABAD             17.15   78.25   500 Telangana
P0641 HAGM GAMBELLA               9.51   34.35   526 Benishangul-Gumuz
P0650 GOBD DIASS-THIES AIRPORT   14.40  -17.04    88 Region Barh El Gazel
89014 ---- NORDENSKIOLD BASE    -73.03  -13.23   495 
89022 ---- HALLEY               -75.27  -26.13    30 
89504 ---- TROLL                -72.01    2.32  1277 
89507 ---- KOHNEN               -75.00    0.00  2892 
89606 ---- VOSTOK               -78.27  106.52  342 
"""