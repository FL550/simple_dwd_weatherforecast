stations = """
TABLE St 99999 99991 gmos 99892 99891 ecmda 99791 gmeda
clu   CofX  id    ICAO name                 nb.    el.     elev  Hmod-H type
===== ----- ===== ---- -------------------- ------ ------- ----- ------ ----
99803     8 EW002 ---- Beveringen            53.10   12.13    71        LAND
99804     8 EW003 ---- Calvoerde             52.25   11.19    55        LAND
99805     8 EW004 ---- Dahlem-Berg           50.23    6.28   600        LAND
99806     8 EW005 ---- Delitzsch             51.30   12.23    99        LAND
99807     8 EW006 ---- Emden                 53.20    7.09     0        KUES
99808     8 EW007 ---- Foehr                 54.44    8.35     0        KUES
99809     8 EW008 ---- Freiamt               48.10    7.38   678        LAND
99810     8 EW009 ---- Goosefeld             54.25    9.49    45        LAND
99811     8 EW010 ---- Hagen-Dahl            51.18    7.34   409        LAND
99812     8 EW011 ---- Hilkenbrook           52.59    7.42     7        LAND
99801     8 EW012 ---- Kaiser-Wilhelm-Koog   53.56    8.57     0        KUES
99802     8 EW013 ---- Kroppach              50.41    7.43   358        LAND
99803     8 EW015 ---- Podelzig              52.28   14.31    47        LAND
99804     8 EW016 ---- Rakow                 54.03   11.37     0        KUES
99805     8 EW017 ---- Rosenberg             49.27    9.29   359        LAND
99806     8 EW018 ---- Rothwesten            51.23    9.32   287        LAND
99807     8 EW019 ---- Ruegen                54.30   13.20    11        KUES
99808     8 EW020 ---- St. Peter-Ording      54.19    8.38     0        KUES
99809     8 EW021 ---- Steinlah              52.04   10.20   161        LAND
99810     8 EW022 ---- Steinsdorf            50.35   11.29   537        LAND
99811     8 EW024 ---- Wangerland            53.42    7.50     0        KUES
99812     8 EW025 ---- Wasbek                54.05    9.54    17        LAND
99801     8 EW026 ---- Weissenburg           49.02   11.04   606        LAND
99802     8 EW027 ---- Westfehmarn           54.31   11.03     0        KUES
99803     8 EW028 ---- Wuennenberg           51.34    8.46   370        LAND
99804     8 EW029 ---- Wusterhusen           54.06   13.37    24        LAND
99805     8 EW030 ---- Zapfendorf            50.00   10.56   370        LAND
99806    16 EW031 ---- EW-Lindenberg         52.10   14.07    73        LAND
99807    24 EW032 ---- Cabauw                52.22    5.20     0        LAND
99808    16 EW034 ---- EW-Hamburg            53.31   10.06     0        LAND
99809     8 EW035 ---- FINO1                 54.01    6.35     0        MEER
99810    16 EW036 ---- FINO2                 55.01   13.09     0        MEER
99811    16 EW037 ---- FINO3                 55.07    7.06     0        MEER
99812     8 EW038 ---- EW-Risoe              55.41   12.05     0        KUES
99801    24 EW039 ---- EW-Roedeser-Berg      51.22    9.12   385        LAND
99804   307 01311 ENBR BERGEN                60.18    5.13    50    -11 KUES
99805   292 01338 ---- VANGSNES              61.10    6.39    51    252 LAND
99808   434 01384 ENGM OSLO/GARDERMOEN       60.12   11.06   201     18 LAND
99809   135 01385 ---- HAMAR-STAVSBERG       60.49   11.04   221    -31 LAND
99810   342 01403 ---- UTSIRA FYR            59.19    4.52    55    -55 MEER
99811   331 01415 ENZV STAVANGER             58.53    5.38     9     11 KUES
99812   227 01452 ENCN KRISTIANSAND          58.12    8.05    17     14 KUES
99801   135 01481 ---- MELSOM                59.14   10.21    26    -14 KUES
99802   127 01488 ENFB OSLO/FORNEBU          59.54   10.37    16     32 KUES
99803   465 01492 ---- OSLO-BLINDERN         59.56   10.43    94     27 KUES
99804   238 01493 ---- SARPSBORG             59.17   11.07    54     15 LAND
99805   331 01494 ENRY RYGGE                 59.23   10.47    53    -37 KUES
99802   164 02418 ESSQ KARLSTAD              59.22   13.28    46     11 LAND
99803   351 02458 ESCM UPPSALA               59.53   17.36    21      7 LAND
99804   164 02460 ESSA STOCKHOLM/ARLANDA     59.39   17.55    37    -12 LAND
99805   164 02464 ESKN STOCKHOLM             59.21   17.57    15      2 LAND
99806   246 02469 ---- TULLINGE              59.11   17.55    45     12 LAND
99807   310 02476 ---- FLODA                 59.04   16.23    32     18 LAND
99808   369 02490 ---- SVANBERGA             59.50   18.38    15      3 LAND
99809   252 02493 ---- SOEDERARM             59.45   19.25    15    -15 KUES
99810   292 02500 ---- NORDKOSTER            58.53   11.00    33      1 KUES
99811   292 02505 ---- MASESKAR              58.05   11.20    16      1 KUES
99812   254 02513 ---- GOETEBORG             57.42   12.00     5     26 KUES
99801   460 02520 ESIB SATENAS               58.26   12.43    54      1 LAND
99802   164 02550 ESGJ JONKOPING             57.46   14.05   226      6 LAND
99803   307 02559 ---- GLADHAMMAR            57.43   16.27    35     26 KUES
99804   461 02562 ESCF LINKOPING             58.24   15.31    93     -8 LAND
99805   310 02574 ---- NORRKOPING            58.35   16.09    35      1 LAND
99806   310 02590 ESSV VISBY                 57.40   18.21    51    -26 KUES
99807   164 02607 ESDB ANGELHOLM             56.18   12.51    20      0 KUES
99808   254 02611 ESHH HELSINGBORG           56.02   12.46    43    -24 KUES
99809   402 02616 ---- FALSTERBO             55.23   12.49     3      7 KUES
99810   292 02628 ---- HANO                  56.01   14.51    60    -41 LAND
99811   246 02635 ---- MALMO                 55.34   13.04    20     -5 KUES
99812   164 02636 ESMS MALMO/STURUP          55.33   13.22   106    -57 LAND
99801   465 02664 ESDF RONNEBY               56.16   15.17    58     -2 LAND
99802   164 02670 ESMQ KALMAR                56.41   16.18     6      8 KUES
99803   230 02944 EFTP TAMPERE               61.25   23.35   112      2 LAND
99806   230 02958 ---- LAPPEENRANTA          61.03   28.12   101    -29 LAND
99807   247 02965 ---- LAHTI                 60.58   25.38    83     13 LAND
99808   230 02966 EFUT UTTI                  60.54   26.56   100    -25 LAND
99809   402 02974 EFHK HELSINKI/VANTAA       60.19   24.58    51    -19 LAND
99810   124 02982 ---- HANKO                 59.46   22.57     5     -6 KUES
99811   454 03005 ---- LERWICK               60.08   -1.11    82    -45 KUES
99812   235 03017 EGPA KIRKWALL              58.57   -2.54    26      4 KUES
99801   258 03026 EGPO STORNOWAY             58.13   -6.19     9     41 KUES
99802   275 03044 ---- ALTNAHARRA            58.17   -4.26    81     76 LAND
99803   285 03063 ---- AVIEMORE              57.13   -3.50   228    110 LAND
99804    45 03065 ---- CAIRNGORM             57.07   -3.38  1245   -521 BERG
99805   275 03066 EGQK KINLOSS               57.39   -3.34     6     11 LAND
99806   421 03068 EGQS LOSSIEMOUTH           57.43   -3.19    13      4 KUES
99807   203 03075 EGPC WICK                  58.27   -3.05    39     -8 KUES
99808   275 03091 EGPD ABERDEEN              57.12   -2.13    65     37 KUES
99809   235 03100 EGPU TIREE                 56.30   -6.53    12     -8 KUES
99810   203 03132 ---- WEST FREUGH           54.52   -4.56    11      6 KUES
99811   235 03136 ---- PRESTWICK/RNAS        55.31   -4.35    26     25 KUES
99812   275 03158 ---- CHARTERHALL           55.43   -2.23   112     41 LAND
99801   490 03162 ---- ESKDALEMUIR           55.19   -3.12   242    -12 LAND
99802   235 03171 EGQL LEUCHARS              56.23   -2.52    12     -1 KUES
99803   453 03204 EGNS ISLE OF MAN/ROUAL.    54.05   -4.38    17    132 KUES
99804    84 03220 ---- CARLISLE              54.56   -2.58    28     17 LAND
99805   490 03257 EGXE LEEMING               54.18   -1.32    40     26 LAND
99806   243 03265 EGXZ TOPCLIFFE             54.12   -1.23    25     10 LAND
99807   431 03266 EGXU LINTON-ON-OUSE        54.03   -1.15    16     18 LAND
99808   203 03275 ---- LOFTUS SAMOS          54.20   -0.31   158     -2 LAND
99809   154 03292 ---- BRIDLINGTON           54.05   -0.11    15     37 KUES
99810   450 03302 EGOV VALLEY                53.15   -4.32    11     16 KUES
99811   160 03313 ---- RHYL                  53.16   -3.31    77     -3 KUES
99812   125 03318 EGNH BLACKPOOL             53.46   -3.02    10     -5 KUES
99801   275 03321 EGNR HAWARDEN              53.10   -2.59    10      7 LAND
99802   285 03354 EGRW NOTTINGHAM/MET        53.00   -1.15   117    -11 LAND
99803   493 03377 ---- WADDINGTON            53.10    0.31    68    -64 LAND
99804   418 03379 EGYD CRANWELL              53.02   -0.30    67     -8 LAND
99805   102 03385 ---- DONNA NOOK            53.29    0.05     8     12 KUES
99806   142 03405 ---- ABERDARON             52.47   -4.44    95    -69 KUES
99807   490 03414 EGOS SHAWBURY              52.48   -2.40    76     -1 LAND
99808   275 03462 EGXT WITTERING             52.37   -0.28    84    -33 LAND
99809   461 03482 EGYM MARHAM                52.39    0.34    23     -5 LAND
99810   235 03502 EGUC ABERPORTH             52.08   -4.34   133    -29 KUES
99811   253 03503 ---- TRAWSCOED             52.20   -3.57    63    145 LAND
99812   182 03520 EGBS SHOBDON               52.15   -2.53    99     10 LAND
99801   256 03560 EGVW BEDFORD               52.13   -0.29    85    -17 LAND
99802   492 03590 EGUW WATTISHAM             52.07    0.58    87    -21 LAND
99803   179 03604 ---- MILFORD HAVEN         51.43   -5.03    44    -37 KUES
99804   266 03628 EGTG BRISTOL/FILTON        51.31   -2.35    59    -25 LAND
99805   123 03647 ---- LITTLE RISSINGTON     51.52   -1.41   215    -59 LAND
99806   490 03649 EGVN BRIZE NORTON          51.45   -1.35    88     -8 LAND
99807   431 03672 EGWU NORTHOLT              51.33   -0.25    38     31 LAND
99808   203 03707 EGDC CHIVENOR              51.05   -4.09     6     86 LAND
99809   234 03740 EGDL LYNEHAM               51.30   -1.59   145     -7 LAND
99810   360 03743 ---- LARKHILL              51.12   -1.49   132      0 LAND
99811   150 03768 ---- FARNBOROUGH           51.17    0.46    65     20 LAND
99812   275 03772 EGLL LONDON                51.29   -0.27    24      3 LAND
99801   256 03781 ---- KENLEY                51.18   -0.05   170    -49 LAND
99802   275 03797 EGMH MANSTON               51.21    1.21    44    -31 KUES
99803   203 03803 ---- SCILLY                49.55   -6.18    31    -30 MEER
99804   493 03808 ---- CAMBORNE              50.13   -5.20    87      2 KUES
99805   461 03809 EGDR CULDROSE              50.05   -5.15    78    -35 KUES
99806   203 03827 EGDB PLYMOUTH              50.21   -4.07    50      0 KUES
99807   493 03853 ---- YEOVILTON             51.01   -2.38    23     36 LAND
99808   275 03862 EGHH BOURNEMOUTH/HURN      50.47   -1.50    11     -5 KUES
99809    94 03866 ---- ST.CATHERINE'S POINT  50.35   -1.18    16     34 KUES
99810   285 03882 ---- HERSTMONCEUX          50.53    0.19    52     22 LAND
99811   421 03894 EGJB GUERNSEY              49.26   -2.36   101    -87 KUES
99812   234 03895 EGJJ JERSEY-AIRPORT        49.13   -2.12    84    -56 KUES
99801   298 03917 EGAA BELFAST               54.39   -6.13    81     -6 KUES
99802   282 03953 ---- VALENTIA              51.56  -10.14    25     58 KUES
99803   426 03955 EICK CORK AIRPORT          51.51   -8.29   153    -82 KUES
99804   243 03961 ---- CARLOW OAK PARK       52.51   -6.55    61     28 LAND
99805   426 03962 EINN SHANNON               52.42   -8.55    14      0 LAND
99806   426 03969 EIDW DUBLIN                53.26   -6.15    68    -32 KUES
99807   264 03971 ---- MULLINGAR             53.32   -7.22   100     21 LAND
99808   304 03976 ---- BELMULLET             54.14  -10.01     9     12 KUES
99809   312 03980 ---- MALIN HEAD            55.22   -7.20    20      9 KUES
99810   314 06030 EKYT ALBORG                57.06    9.52     3      1 LAND
99811   291 06041 ---- SKAGEN                57.46   10.39     3     -3 KUES
99812   260 06052 ---- THYBORON              56.43    8.13     2     13 KUES
99801   403 06060 EKKA KARUP                 56.18    9.07    52    -18 LAND
99802   434 06070 EKAH TIRSTRUP              56.18   10.37    25      4 KUES
99803   286 06104 EKBI BILLUND               55.44    9.09    70      5 LAND
99804   456 06110 EKSP SKRYDSTRUP            55.14    9.16    43      0 LAND
99805   352 06119 ---- KEGNAES               54.51    9.59    17     -2 KUES
99806   404 06120 EKOD ODENSE                55.28   10.20    17     -2 KUES
99807   204 06169 ---- GNIBEN                56.01   11.17    14    -13 MEER
99808   277 06170 EKRK KOEBENHAVN/ROSKILDE   55.35   12.08    44     -3 LAND
99809   393 06180 EKCH KOPENHAGEN            55.38   12.40     5      0 KUES
99810   320 06235 EHKD KOOY                  52.55    4.47     0      0 KUES
99811   320 06240 EHAM AMSTERDAM             52.18    4.46    -4      1 LAND
99812   276 06242 EHVL VLIELAND              53.15    4.55    11    -11 KUES
99801   412 06260 EHDB DE BILT               52.06    5.11     2      3 LAND
99802   320 06270 EHLW LEEUWARDEN            53.13    5.46     1     -1 LAND
99803   320 06275 EHDL DEELEN                52.04    5.53    48      9 LAND
99804   320 06279 EHHO HOOGEVEEN             52.44    6.31    12      1 LAND
99805   320 06280 EHGG GRONINGEN             53.08    6.35     4     -2 LAND
99806   412 06290 EHTW TWENTHE               52.16    6.54    35      0 LAND
99807   412 06310 ---- VLISSINGEN            51.26    3.36     8     -7 KUES
99808   224 06330 ---- HOEK V.HOLL.          51.59    4.07    12    -14 KUES
99809   323 06344 EHRD ROTTERDAM             51.57    4.27    -5      1 LAND
99810   320 06350 EHGR GILZE RIJEN           51.34    4.56    11     -2 LAND
99811   320 06370 EHEH EINDHOVEN             51.27    5.25    23     -9 LAND
99812   320 06375 EHVK VOLKEL                51.39    5.42    22     -3 LAND
99801   320 06380 EHBK MAASTRICHT            50.55    5.47   114     15 LAND
99802   475 06407 EBOS OOSTENDE              51.12    2.52     4     -3 KUES
99803   221 06431 ---- GENT                  51.11    3.49    10     -7 LAND
99804   475 06449 EBCI CHARLEROI             50.28    4.27   187    -37 LAND
99805   475 06450 EBAW ANTWERPEN             51.12    4.28    12     -5 LAND
99806   475 06451 EBBR BRUESSEL              50.54    4.32    55    -22 LAND
99807   471 06456 EBFS FLORENNES             50.14    4.40   279    -25 LAND
99808   471 06458 EBBE BEAUVECHAIN           50.45    4.46   105     17 LAND
99809   181 06476 EBSH ST.HUBERT             50.02    5.24   563   -120 LAND
99810   475 06478 EBLG BIERSET               50.39    5.27   178    -46 LAND
99811   470 06479 EBBL KLEINE BROGEL         51.10    5.28    55      1 LAND
99812   226 06490 EBSP SPA/LA SAUVENIERE     50.29    5.55   470     47 LAND
99801   461 06496 EBLB ELSENBORN             50.28    6.11   564     -5 LAND
99802   470 06590 ELLX LUXEMBURG             49.37    6.13   376    -46 LAND
99803   309 06601 ---- BASEL                 47.32    7.35   316    -12 LAND
99804   241 06604 LSGN NEUCHATEL             47.00    6.57   485    -12 LAND
99805   307 06605 ---- CHASSERAL             47.08    7.03  1599   -786 BERG
99806   177 06606 ---- CRESSIER              47.03    7.04   431     42 LAND
99807   307 06609 ---- MOLESON               46.33    7.01  1972   -885 BERG
99808   436 06610 ---- PAYERNE               46.49    6.56   490     17 LAND
99809   237 06612 LSGC LA CHAUX DE FONDS     47.05    6.48  1018     -3 LAND
99810   316 06616 ---- FAHY                  47.25    6.56   596     -1 LAND
99811   170 06619 ---- LA FRETAZ             46.50    6.35  1202   -365 BERG
99812   316 06620 LSPF SCHAFFHAUSEN          47.41    8.37   437     47 LAND
99801   178 06621 ---- GUETTINGEN            47.36    9.17   440     49 LAND
99802   217 06623 ---- SALEN-REUTENEN        47.39    9.01   718   -127 LAND
99803   226 06624 ---- HALLAU                47.42    8.28   419      7 LAND
99804   218 06625 ---- FRIBOURG POSIEUX      46.46    7.07   646      2 LAND
99805   178 06626 ---- GOESGEN (KKW)         47.22    7.58   380     36 LAND
99806   170 06628 ---- PLAFFEIEN-OBERSCH.    46.45    7.16  1042    -90 LAND
99807   230 06631 ---- BERN-LIEBEFELD        46.56    7.25   565     23 LAND
99808   177 06632 ---- GRENCHEN              47.11    7.25   430     66 LAND
99809   436 06633 ---- BUCHS-SUHR            47.23    8.05   387     42 LAND
99810   303 06635 ---- KOPPIGEN              47.07    7.37   484     12 LAND
99811   178 06636 ---- MUEHLEBERG (KKW)      46.58    7.17   480     51 LAND
99812   436 06637 ---- MEIRINGEN             46.44    8.07   589    493 LAND
99801   218 06638 ---- LANGNAU I.E.          46.56    7.49   745      6 LAND
99802   308 06639 ---- NAPF                  47.00    7.56  1406   -567 BERG
99803   177 06641 ---- MOEHLIN               47.34    7.53   344     72 LAND
99804   311 06643 ---- WYNAU                 47.16    7.47   422     74 LAND
99805   308 06645 ---- RUENENBERG            47.26    7.53   611    -76 BERG
99806   178 06646 ---- BEZNAU                47.34    8.14   326     91 LAND
99807   177 06648 ---- EGOLZWIL              47.11    8.00   521     -7 LAND
99808   178 06650 ---- LUZERN                47.01    8.18   456     69 LAND
99809   169 06651 ---- SCHUEPFHEIM           46.57    8.01   742    -12 LAND
99810   170 06655 ---- ENGELBERG             46.49    8.25  1036    716 BERG
99811   177 06657 ---- GISWIL                46.57    8.11   475     50 LAND
99812   307 06659 ---- PILATUS               46.59    8.15  2106  -1304 BERG
99801   294 06660 ---- ZUERICH (TOWN/VILLE)  47.23    8.34   556    -35 LAND
99802   178 06664 ---- RECKENHOLZ            47.26    8.31   444     10 LAND
99803   311 06666 ---- LEIBSTADT (KKW)       47.36    8.11   341     88 LAND
99804    79 06669 ---- LAEGERN               47.29    8.24   868   -378 BERG
99805   436 06670 LSZH ZUERICH               47.29    8.32   436     17 LAND
99806   436 06672 ---- ALTDORF               46.52    8.38   449    223 LAND
99807   178 06673 ---- WAEDENSwl             47.13    8.41   463     58 LAND
99808   177 06674 ---- CHAM                  47.11    8.28   443     82 LAND
99809   170 06675 ---- EINSIEDELN            47.08    8.46   910     67 LAND
99810    76 06676 ---- OBERAEGERI            47.08    8.37   724    -25 LAND
99811   178 06679 ---- TAENIKON              47.28    8.54   536     45 LAND
99812   387 06680 ---- SAENTIS               47.15    9.20  2502  -1405 BERG
99801   248 06681 ---- ST.GALLEN             47.26    9.24   779    -15 LAND
99802   280 06682 ---- ELM                   46.55    9.11   958     71 LAND
99803    76 06683 ---- SCHMERIKON            47.13    8.56   408    136 LAND
99804   178 06685 ---- GLARUS                47.02    9.04   515    223 LAND
99805    76 06687 ---- QUINTEN               47.08    9.13   419    539 LAND
99806   129 06688 ---- CRAP MASEGN           46.50    9.11  2480   -255 LAND
99807   308 06689 ---- HOERNLI               47.22    8.56  1144   -300 BERG
99808   177 06690 LSZR ALTENRHEIN            47.29    9.34   398     44 LAND
99809   170 06693 ---- EBNAT-KAPPEL          47.16    9.07   623     -3 LAND
99810   436 06700 LSGG GENF                  46.15    6.08   420      0 LAND
99811   181 06702 ---- LA DOLE               46.25    6.06  1670   -499 BERG
99812   169 06704 ---- BIERE                 46.32    6.20   684     21 LAND
99801   178 06705 ---- CHANGINS              46.24    6.14   430     24 LAND
99802   177 06711 ---- PULLY                 46.31    6.40   461    102 LAND
99803   374 06712 ---- AIGLE                 46.20    6.55   381    182 LAND
99804   291 06717 ---- GRAND-ST-BERNARD      45.52    7.10  2472    -92 BERG
99805   436 06720 LSGS SION                  46.13    7.20   482    476 LAND
99806   238 06722 ---- EVOLENE-VILLAZ        46.07    7.31  1825    373 BERG
99807   170 06724 ---- MONTANA               46.19    7.29  1508      2 LAND
99808   176 06727 ---- VISP                  46.18    7.50   639    932 LAND
99809   289 06730 ---- JUNGFRAUJOCH          46.29    8.02  3580   -566 BERG
99810   178 06734 LSMI INTERLAKEN            46.40    7.52   580    142 LAND
99811   233 06735 ---- ADELBODEN             46.30    7.34  1320     -4 LAND
99812   227 06744 ---- GRIMSEL-HOSPIZ        46.34    8.20  1980    163 BERG
99801   335 06745 ---- ULRICHEN              46.30    8.19  1346    798 BERG
99802   170 06748 LSEZ ZERMATT               46.02    7.45  1638    -66 LAND
99803   307 06750 ---- GUETSCH               46.39    8.37  2287   -296 BERG
99804   169 06751 ---- ROBIEI                46.27    8.31  1898    144 BERG
99805   303 06753 ---- PIOTTA                46.31    8.41  1007    560 LAND
99806   190 06756 ---- COMPROVASCO           46.28    8.56   575   1017 BERG
99807   307 06759 ---- CIMETTA               46.12    8.48  1672   -967 BERG
99808   352 06760 ---- LOCARNO-MONTI         46.10    8.47   367    339 BERG
99809   298 06762 LSZL LOCARNO               46.10    8.53   197    429 LAND
99810   361 06770 ---- LUGANO                46.00    8.58   273    204 LAND
99811   316 06771 ---- STABIO                45.50    8.56   353     17 LAND
99812   169 06778 ---- BUFFALORA             46.39   10.16  1968     53 LAND
99801   265 06780 ---- WEISSFLUHJOCH         46.50    9.49  2691   -771 BERG
99802   287 06782 ---- DISENTIS              46.42    8.51  1190    751 BERG
99803   308 06783 ---- SAN BERNARDINO        46.28    9.11  1639    479 BERG
99804   193 06784 ---- DAVOS                 46.49    9.51  1590    546 BERG
99805   436 06786 ---- CHUR                  46.52    9.32   556    405 LAND
99806   169 06787 ---- ANDEER                46.37    9.25   989    331 LAND
99807   169 06788 ---- HINTERRHEIN           46.31    9.11  1611    602 BERG
99808   307 06791 ---- CORVATSCH             46.25    9.49  3315   -963 BERG
99809   383 06792 LSXM SAMEDAN               46.32    9.53  1709    228 LAND
99810   169 06793 ---- VALBELLA              46.46    9.33  1569     55 LAND
99811   428 06794 ---- ROBBIA                46.21   10.04  1078   1154 BERG
99812   169 06795 ---- PIZ MARTEGNAS         46.35    9.32  2670   -264 LAND
99801   170 06796 ---- STA. MARIA VAL MUEST  46.36   10.26  1383    440 LAND
99802   170 06798 ---- SCOULS                46.48   10.16  1298    525 LAND
99803   262 06799 ---- NALUNS / SCHLIVERA    46.49   10.16  2400     57 BERG
99804   436 06990 ---- VADUZ FL.             47.08    9.31   460    371 LAND
99805   427 07002 ---- BOULOGNE              50.44    1.36    70    -47 KUES
99806   354 07005 LFOI ABBEVILLE             50.08    1.50    70    -16 LAND
99807   376 07015 LFQQ LILLE                 50.34    3.06    48    -12 LAND
99808   427 07020 ---- LA HAGUE              49.43   -1.56     3     47 KUES
99809   376 07024 LFRC CHERBOURG             49.39   -1.28   139    -73 LAND
99810   376 07027 LFRK CAEN                  49.11   -0.27    67    -14 LAND
99811   332 07028 LFOH LA HEVE               49.31    0.04   100      0 LAND
99812   363 07037 LFOP ROUEN                 49.23    1.11   157    -40 LAND
99801   363 07038 LFOE EVREUX                49.01    1.13   132    -23 LAND
99802   185 07040 ---- DIEPPE                49.56    1.06    33     49 KUES
99803   376 07055 LFOB BEAUVAIS              49.28    2.07   106     13 LAND
99804   320 07061 LFOW SAINT-QUENTIN         49.49    3.12    98    -11 LAND
99805   376 07075 LFQV CHARLEVILLE           49.47    4.38   149    -14 LAND
99806   427 07100 LFEC OUESSANT              48.28   -5.08    35    -35 MEER
99807   375 07110 LFRB BREST                 48.27   -4.25    99    -25 KUES
99808   375 07120 LFRT ST.BRIEUC             48.32   -2.51   136      3 KUES
99809   376 07125 LFRD DINARD APT            48.35   -2.04    58      0 KUES
99810   256 07130 LFRN RENNES                48.04   -1.44    37     -2 LAND
99811   346 07133 ---- POINTE DU ROC         48.50   -1.37    37     22 KUES
99812   376 07139 LFOF ALENCON               48.26    0.06   144      7 LAND
99801   376 07143 LFOR CHARTRES              48.28    1.31   155     -7 LAND
99802   486 07149 LFPO PARIS                 48.44    2.24    89    -11 LAND
99803   479 07157 LFPG PARIS CH.D.GAULLE     49.01    2.32   108    -33 LAND
99804   376 07168 LFQB TROYES                48.20    4.01   112     11 LAND
99805   256 07169 LFSI ST. DIZIER            48.38    4.54   139     19 LAND
99806   376 07180 LFSN NANCY                 48.41    6.13   229     46 LAND
99807   376 07190 LFST STRASSBURG            48.33    7.38   153     -4 LAND
99808   386 07200 ---- PENMARCH              47.48   -4.22     6     15 KUES
99809   375 07201 LFRQ QUIMPER               47.58   -4.10    92      3 LAND
99810   375 07205 LFRH LANN BIHOUE           47.46   -3.27    42    -26 LAND
99811   376 07222 LFRS NANTES                47.10   -1.36    27    -14 LAND
99812   376 07235 LFRM LE MANS               47.57    0.12    52     18 LAND
99801   376 07240 LFOT TOURS                 47.27    0.43   108    -15 LAND
99802   376 07249 LFOJ ORLEANS               47.59    1.47   125     -1 LAND
99803   448 07255 LFLD BOURGES               47.04    2.22   161    -13 LAND
99804   376 07260 LFQG NEVERS                47.00    3.06   175     37 LAND
99805   376 07280 LFSD DIJON                 47.16    5.05   219      7 LAND
99806   220 07288 LFSA BESANCON              47.15    5.59   307    -37 LAND
99807   246 07299 LFSB BASEL-MLH.            47.36    7.31   270     34 LAND
99808   256 07306 LFRI LA ROCHE-SUR-YON      46.42   -1.23    90     -4 LAND
99809   168 07315 ---- LA ROCHELLE           46.09   -1.09     4      4 KUES
99810   376 07335 LFBI POITIERS              46.35    0.18   120    -10 LAND
99811   376 07354 LFLX CHATEAUROUX           46.52    1.43   155     12 LAND
99812   342 07379 LFLN SAINT-YAN.            46.25    4.01   242      9 LAND
99801   320 07385 LFLM MACON                 46.18    4.48   216    -23 LAND
99802   376 07434 LFBL LIMOGES               45.52    1.11   402     10 LAND
99803   376 07460 LFLC CLERMONT              45.47    3.10   329     11 LAND
99804   376 07475 LFMH ST. ETIENNE           45.32    4.18   402    -12 LAND
99805   376 07480 LFLY LYON/BRON             45.43    4.57   200     11 LAND
99806   452 07481 LFLL LYON/SATOLAS          45.44    5.05   248     -4 LAND
99807   376 07486 LFLS GRENOBLE              45.22    5.20   384     82 LAND
99808   376 07491 LFLB CHAMBERY - AIX        45.39    5.53   235     99 LAND
99809   251 07497 ---- BOURG-ST-M            45.37    6.46   865    654 LAND
99810   376 07510 LFBD BORDEAUX              44.50   -0.42    49     -2 LAND
99811   302 07558 LFCM MILLAU                44.07    3.01   715     -3 LAND
99812   199 07577 LFLQ MONTELIMAR            44.35    4.44    73    128 LAND
99801   332 07579 LFMO ORANGE                44.08    4.50    53      1 LAND
99802   295 07588 LFMX ST.AUBAN              44.04    6.00   457     10 LAND
99803   453 07600 ---- SOCOA                 43.24   -1.41    24     28 KUES
99804   376 07602 LFBZ BIARRITZ              43.28   -1.32    69    -41 KUES
99805   376 07610 ---- PAU                   43.23   -0.25   185    -10 LAND
99806   376 07621 LFBT TARBES/OSSUN          43.11    0.00   364     32 LAND
99807   320 07622 LFDH AUCH                  43.41    0.36   121     59 LAND
99808   376 07630 LFBO TOULOUSE              43.38    1.22   152     -6 LAND
99809   347 07635 LFMK CARCASSONNE           43.13    2.19   126      7 LAND
99810   217 07638 ---- BEZIER-VIAS           43.18    3.24    16      1 KUES
99811   366 07643 LFMT MONTPELLIER           43.35    3.58     3      4 LAND
99812   272 07645 LFME NIMES/COURBESSAC      43.52    4.24    59     22 LAND
99801   290 07648 LFMY SALON                 43.36    5.06    59     -9 LAND
99802   334 07650 LFML MARSEILLE             43.27    5.13     5      8 KUES
99803   268 07667 LFTH HYERES/ALMANARRE      43.06    6.09     3     35 KUES
99804   436 07675 LFMC LE LUC                43.23    6.23    80     52 LAND
99805   185 07684 LFMD CANNES                43.33    6.57     3     90 KUES
99806   484 07690 LFMN NIZZA                 43.39    7.12     4     72 KUES
99807   334 07747 LFMP PERPIGNAN             42.44    2.52    43     -2 LAND
99808   319 07754 LFKC CALVI                 42.32    8.48    46    293 KUES
99809   479 07761 LFKJ AJACCIO               41.55    8.48     6     67 KUES
99810   446 07770 ---- PERTUSATO / CORSICA   41.22    9.11   105    -35 KUES
99811   291 07780 LFKF FIGARI                41.30    9.06    26     13 KUES
99812   391 07785 ---- CAP CORSE             43.00    9.22   111    222 KUES
99801   494 07790 LFKB BASTIA                42.33    9.29    10     30 LAND
99802   419 08001 LECO LA CORUNA             43.22   -8.25    58     47 KUES
99803   277 08014 ---- GIJON                 43.32   -5.38     3     56 KUES
99804   449 08015 LEOV OVIEDO                43.21   -5.52   335    -14 LAND
99805   341 08021 LEXJ SANTANDER/PARAYAS     43.26   -3.49     6     20 KUES
99806   419 08023 ---- SANTANDER             43.29   -3.48    52    -26 KUES
99807   367 08025 LEBB BILBAO                43.18   -2.56    42     34 LAND
99808   418 08027 ---- SAN SEBASTIAN/IGUEL.  43.18   -2.03   258    -83 KUES
99809   278 08029 LESO SAN SEBASTIAN/FUENT.  43.21   -1.48     5     47 KUES
99810   419 08042 LEST SANTIAGO              42.54   -8.26   370     -6 LAND
99811   419 08045 LEVX VIGO/PEINADOR         42.13   -8.38   264    -38 LAND
99812   332 08055 LELN LEON                  42.35   -5.39   926    -57 LAND
99801   326 08075 ---- BURGOS-VILLAFRIA      42.22   -3.38   894     52 LAND
99802   419 08080 ---- VITORIA OBSERVATORI   42.52   -2.44   513     15 LAND
99803   271 08140 LEVD VALLADOLID            41.43   -4.51   849    -33 LAND
99804   419 08141 ---- VALLADOLID            41.38   -4.45   735     -2 LAND
99805   419 08160 LEZG ZARAGOZA              41.40   -1.01   263    -31 LAND
99806   337 08171 ---- LERIDA                41.37    0.38   203    -42 LAND
99807   306 08175 LERS REUS                  41.09    1.10    71    -30 LAND
99808   414 08181 LEBL BARCELONA             41.17    2.04     4    177 KUES
99809   379 08184 LEGE GERONA/COST.BRAVA     41.54    2.46   143     28 LAND
99810   411 08202 LESA SALAMANCA/MATACAN     40.57   -5.30   793     15 LAND
99811   426 08221 LEMD MADRID/BARAJAS        40.27   -3.33   609    -18 LAND
99812   226 08272 ---- TOLEDO BUENAVISTA     39.53   -4.03   451     81 LAND
99801   417 08280 LEAB ALBACETE/LOS LLANOS   38.57   -1.51   702    -17 LAND
99802   357 08284 LEVC VALENCIA              39.30   -0.28    69    -20 KUES
99803   339 08286 LECN CASTELLON DE LA PLAN  39.57    0.04    36     24 KUES
99804   419 08306 LEPA PALMA                 39.33    2.44     4     17 KUES
99805   419 08314 LEMH MENORCA               39.52    4.14    87    -26 KUES
99806   419 08330 LEBZ BADAJOZ/TALAVERA      38.53   -6.49   185      5 LAND
99807   357 08360 LEAL ALICANTE              38.17   -0.33    43     26 KUES
99808   419 08373 LEIB IBIZA                 38.52    1.23    17     79 KUES
99809   272 08383 ---- HUELVA                37.17   -6.55    19      6 KUES
99810   421 08391 ---- SEVILLA/SAN PABLO     37.25   -5.53    34    -18 LAND
99811   418 08397 LEMO MORON DE LA FRONTERA  37.09   -5.37    87      3 LAND
99812   358 08410 LEBA CORDOBA               37.51   -4.51    90     66 LAND
99801   419 08419 LEGR GRANADA/AEROPUERTO    37.11   -3.47   567     55 LAND
99802   419 08430 ---- MURCIA                38.00   -1.10    61     35 LAND
99803   332 08433 LELC MURCIA/SAN JAVIER     37.47   -0.48     5     37 KUES
99804   420 08451 LEJR JEREZ DE LA FRONTERA  36.45   -6.04    27     12 LAND
99805   419 08482 LEMG MALAGA                36.40   -4.29    16    132 KUES
99806   419 08487 LEAM ALMERIA               36.51   -2.23    15    173 KUES
99807   415 08495 LXGB GIBRALTAR             36.09   -5.21     5     71 KUES
99801   412 08532 LPST SINTRA/GRANJA         38.50   -9.20   134     16 LAND
99802   455 08540 LPMR MONTE REAL            39.50   -8.53    52     11 LAND
99803   457 08541 ---- SINES (MONTES CHAOS)  37.57   -8.50    98    -23 KUES
99804   463 08545 LPPR PORTO                 41.14   -8.41    69     -8 KUES
99805   412 08548 LPCO COIMBRA/CERVACHE      40.09   -8.28   179     18 LAND
99806   446 08551 ---- VIANA DO CASTELO      41.38   -8.48    48      7 KUES
99807   474 08554 LPFR FARO                  37.01   -7.58     7     70 KUES
99808   237 08562 ---- BEJA                  38.01   -7.52   246      5 LAND
99809   475 08567 LPVR VILA REAL             41.16   -7.43   561      3 LAND
99810   206 08571 ---- PORTALEGRE            39.17   -7.25   467     -1 LAND
99811   469 08579 ---- LISBOA/GAGO COUTINHO  38.46   -9.08   104     23 KUES
99802   154 10004 ---- UFS TW EMS            54.10    6.21     0      0 MEER
99803   166 10007 ---- UFS DEUTSCHE BUCHT    54.10    7.27     0      0 MEER
99804   489 10015 ---- HELGOLAND             54.10    7.53     4     -4 MEER
99805   490 10020 ---- LIST/SYLT             55.01    8.25    26    -20 KUES
99806   490 10022 EDXK LECK                  54.48    8.57     7      1 LAND
99807   664 10028 ---- ST. PETER ORDING      54.20    8.36     5     -4 KUES
99808   454 10033 ETGG FLENSBURG             54.50    9.30    27      8 LAND
99809   668 10035 ---- SCHLESWIG             54.32    9.33    47    -26 LAND
99810   449 10037 ETNS SCHLESWIG-JAGEL       54.28    9.31    22     -7 LAND
99811   449 10038 ETNH HOHN                  54.19    9.32    10     -3 LAND
99812   476 10042 ---- OLPENITZ              54.40   10.02     4      8 KUES
99801   126 10044 ---- LEUCHTTURM KIEL       54.30   10.16     5     10 KUES
99802   476 10046 EDHK KIEL-H.               54.23   10.09    28    -13 KUES
99803   490 10055 ---- WESTERMARKELSDORF     54.32   11.04     3      6 KUES
99804   647 10091 ---- ARKONA                54.41   13.26    42    -42 KUES
99805   476 10093 ---- PUTBUS                54.22   13.29    40    -21 KUES
99806   476 10097 ---- GREIFSWALDER OIE      54.14   13.55    12    -11 KUES
99807   505 10113 ---- NORDERNEY             53.43    7.09    11    -11 KUES
99808   449 10126 ETNT WITTMUNDHAVEN         53.33    7.40     8     -5 KUES
99809   489 10129 ---- BREMERHAVEN           53.32    8.35     7     -2 KUES
99810   476 10130 ---- ELPERSBUETTEL         54.04    9.01     3      7 KUES
99811   489 10131 ---- CUXHAVEN              53.52    8.43     5     -2 KUES
99812   449 10136 ETMN NORDHOLZ              53.46    8.40    23    -16 KUES
99801   489 10139 ---- BREMERVOERDE          53.30    9.10     3      6 LAND
99802   452 10142 ETHI ITZEHOE               54.00    9.35    25    -12 LAND
99803   476 10146 ---- QUICKBORN             53.44    9.53    13     20 LAND
99804   668 10147 EDDH HAMBURG-FU.           53.38   10.00    16      3 LAND
99805   490 10150 ---- DOERNICK              54.10   10.21    26      9 LAND
99806   476 10152 ---- PELZERHAKEN           54.05   10.53     1     16 KUES
99807   490 10156 EDHL LUEBECK               53.49   10.42    14      5 KUES
99808   490 10161 ---- BOLTENHAGEN           54.00   11.11    15     29 KUES
99809   433 10162 ---- SCHWERIN              53.38   11.23    59     -8 LAND
99810   476 10168 ---- GOLDBERG              53.37   12.06    58      0 LAND
99811   506 10170 ---- WARNEMUENDE           54.11   12.05     4      7 KUES
99812   454 10172 ETNL LAAGE                 53.55   12.17    42     -9 LAND
99801   476 10180 ---- BARTH                 54.20   12.43     7     -4 KUES
99802   652 10184 ---- GREIFSWALD            54.06   13.25     2      1 KUES
99803   490 10193 ---- UECKERMUENDE          53.44   14.04     1      2 KUES
99804   489 10200 ---- EMDEN-FLUGPLATZ       53.23    7.14     0      1 LAND
99805   667 10224 EDDW BREMEN                53.03    8.48     3      3 LAND
99806   489 10235 ---- SOLTAU                52.58    9.47    76      2 LAND
99807   433 10238 ETGB BERGEN-HOHNE          52.49    9.56    70      8 LAND
99808   454 10246 ETHS FASSBERG              52.55   10.11    75      7 LAND
99809   490 10249 ---- BOIZENBURG            53.23   10.41    45    -22 LAND
99810   476 10253 ---- LUECHOW               52.58   11.08    17     17 LAND
99811   506 10261 ---- SEEHAUSEN             52.53   11.44    21      5 LAND
99812   490 10264 ---- MARNITZ               53.19   11.56    81     -9 LAND
99801   476 10267 ---- KYRITZ                52.56   12.25    40      5 LAND
99802   476 10268 ---- WAREN                 53.31   12.40    70     -3 LAND
99803   436 10270 ---- NEURUPPIN             52.54   12.49    38      6 LAND
99804   449 10281 ETNU TROLLENHAGEN          53.36   13.18    71    -30 LAND
99805   490 10282 ---- FELDBERG/MECKLENBURG  53.19   13.25   115    -18 LAND
99806   476 10289 ---- GRUENOW               53.19   13.56    56     -3 LAND
99807   652 10291 ---- ANGERMUENDE           53.02   14.00    56    -23 LAND
99808   367 10305 ---- LINGEN                52.31    7.19    22      1 LAND
99809   489 10309 ---- AHAUS                 52.05    6.56    46      7 LAND
99810   489 10312 ---- BELM                  52.19    8.10   103    -15 LAND
99811   651 10315 EDDG MUENSTER/OSNABR.      52.08    7.42    48     -2 LAND
99812   489 10321 ETND DIEPHOLZ              52.35    8.21    39      0 LAND
99801   476 10325 ---- BAD SALZUFLEN         52.06    8.45   135      8 LAND
99802   449 10334 ETNW WUNSTORF              52.27    9.26    57     -8 LAND
99803   454 10335 ETHB BUECKEBURG            52.17    9.05    70     -8 LAND
99804   651 10338 EDDV HANNOVER              52.28    9.41    56     -5 LAND
99805   449 10343 ETHC CELLE                 52.36   10.01    39     10 LAND
99806   505 10348 ---- BRAUNSCHWG.           52.17   10.27    81     -7 LAND
99807   476 10356 ---- UMMENDORF             52.10   11.11   162     -9 LAND
99808   490 10359 ---- GARDELEGEN            52.31   11.23    47     13 LAND
99809   489 10361 EDBM MAGDEBURG             52.07   11.35    79     11 LAND
99810   490 10365 ---- GENTHIN               52.23   12.10    35      2 LAND
99811   490 10368 ---- WIESENBURG            52.07   12.28   187    -46 LAND
99812   476 10376 ---- BARUTH                52.04   13.30    55      8 LAND
99801   668 10379 ---- POTSDAM               52.23   13.04    99    -58 LAND
99802   638 10381 ---- BERLIN-DAHLEM         52.28   13.18    58    -14 LAND
99803   651 10382 EDDT BERLIN-TEGEL          52.34   13.19    37      4 LAND
99804   652 10385 EDDB BERLIN-SCHOENEFELD    52.23   13.31    47     -9 LAND
99805   668 10393 ---- LINDENBERG            52.13   14.07   112    -57 LAND
99806   476 10396 ---- MANSCHNOW             52.33   14.33    12      8 LAND
99807   651 10400 EDDL DUESSELDORF           51.18    6.46    45    -10 LAND
99808   120 10404 ETGY KALKAR                51.44    6.16    27     -2 LAND
99809   476 10410 ---- ESSEN                 51.24    6.58   161    -40 LAND
99810   505 10418 ---- LUEDENSCHEID          51.15    7.38   387    -46 LAND
99811   489 10424 ---- WERL                  51.35    7.53    85     32 LAND
99812   481 10427 ---- K.ASTEN               51.11    8.29   839   -202 BERG
99801   505 10430 ---- BAD LIPPSPRINGE       51.47    8.50   157    -22 LAND
99802   489 10433 ---- LUEDGE                51.52    9.16   258    -48 LAND
99803   476 10435 ---- WARBURG               51.30    9.07   236    -16 LAND
99804   454 10439 ETHF FRITZLAR              51.07    9.17   172     34 LAND
99805   489 10442 ---- ALFELD                51.58    9.48   148     20 LAND
99806   489 10444 ---- GOETTINGEN            51.30    9.57   175      9 LAND
99807   400 10449 ---- LEINEFELDE            51.23   10.19   356     10 LAND
99808   400 10452 ---- BRAUNLAGE             51.43   10.36   607    -22 LAND
99809   494 10453 ---- BROCKEN               51.48   10.37  1142   -557 BERG
99810   476 10454 ---- WERNIGERODE           51.51   10.46   234     51 LAND
99811   400 10458 ---- HARZGERODE            51.39   11.08   404      8 LAND
99812   489 10460 ---- ARTERN                51.22   11.17   164     52 LAND
99801   638 10469 EDDP LEIPZIG/SCHKEUDITZ    51.25   12.14   141    -26 LAND
99802   506 10471 ---- LEIPZIG               51.19   12.25   141    -22 LAND
99803   490 10474 ---- WITTENBERG            51.53   12.38   105    -33 LAND
99804   454 10476 ETSH HOLZDORF              51.46   13.11    79      2 LAND
99805   489 10480 ---- OSCHATZ               51.18   13.05   150     -4 LAND
99806   667 10488 EDDC DRESDEN               51.08   13.45   230      5 LAND
99807   490 10490 ---- DOBERLUG-KIRCHHAIN    51.39   13.34    97      6 LAND
99808   476 10495 ---- HOYERSWERDA           51.27   14.15   116     -1 LAND
99809   490 10496 ETCO COTTBUS               51.47   14.19    69     -4 LAND
99810   668 10499 EDBX GOERLITZ              51.10   14.57   237     -1 LAND
99811   449 10500 ETNG GEILENKIRCHEN         50.58    6.03    90    -19 LAND
99812   208 10502 ETNN NOERVENICH            50.50    6.40   118     19 LAND
99801   489 10506 ---- NUERBURG-BARWEILER    50.22    6.52   485    -26 LAND
99802   651 10513 EDDK KOELN/BONN            50.52    7.10    91    -23 LAND
99803   476 10519 ---- BONN-ROLEBER          50.44    7.11   159    -48 LAND
99804   489 10526 EDKS B.MARIENBG.           50.40    7.58   547    -20 LAND
99805   489 10532 ---- GIESSEN               50.36    8.38   203     -1 LAND
99806   476 10534 ---- HOHERODSKOPF (VOGELS  50.31    9.13   743   -250 LAND
99807   476 10537 ---- NEU-ULRICHSTEIN       50.45    9.01   350      3 LAND
99808   400 10540 ---- EISENACH              51.00   10.22   312    -32 LAND
99809   400 10542 ---- BAD HERSFELD          50.51    9.44   272     12 LAND
99810   630 10544 ---- WASSERKUPPE           50.30    9.56   921   -285 BERG
99811   416 10548 ---- MEININGEN             50.34   10.23   450     -2 LAND
99812   468 10552 ---- SCHMUECKE             50.39   10.46   937   -271 BERG
99801   651 10554 EDDE ERFURT                50.59   10.58   315    -39 LAND
99802   568 10557 ---- NEUHAUS A.R.          50.30   11.08   845   -160 LAND
99803   387 10564 ---- SCHLEIZ               50.34   11.48   501    -47 LAND
99804   476 10565 ---- OSTERFELD             51.05   11.56   246      1 LAND
99805   489 10567 ---- GERA                  50.53   12.08   311    -29 LAND
99806   489 10569 ---- PLAUEN                50.29   12.08   386     19 LAND
99807   468 10574 ---- CARLSFELD             50.26   12.37   897    -26 LAND
99808   416 10577 ---- CHEMNITZ              50.47   12.52   418    -57 LAND
99809   523 10578 ---- FICHTELBERG           50.26   12.57  1213   -433 BERG
99810   420 10579 ---- MARIENBERG            50.39   13.09   639    -77 LAND
99811   482 10582 ---- ZINNWALD-G.           50.44   13.45   877   -217 LAND
99812   476 10591 ---- LICHTENHAIN           50.56   14.13   321    -33 LAND
99801   505 10609 ---- TRIER                 49.45    6.40   265      8 LAND
99802   449 10613 ETSB BUECHEL               50.10    7.04   478     21 LAND
99803   489 10615 ---- DEUSELBACH            49.46    7.03   481    -16 LAND
99804   540 10616 EDFH HAHN                  49.57    7.16   502     29 LAND
99805   449 10618 EDRG IDAR-OBERSTEIN        49.42    7.20   376     44 LAND
99806   387 10628 ---- GEISENHEIM            49.59    7.57   118     67 LAND
99807   481 10635 ---- KL.FELDBG./TS.        50.13    8.27   805   -408 BERG
99808   638 10637 EDDF FRANKFURT/M           50.03    8.36   111      0 LAND
99809   476 10641 ---- OFFENBACH-WETTERPARK  50.05    8.47   119     25 LAND
99810   476 10646 ---- NEUHUETTEN/SPESSART   50.01    9.25   340     22 LAND
99811   489 10648 ---- MICHELSTADT-V.        49.43    9.06   453    -41 LAND
99812   505 10655 ---- WUERZBURG             49.46    9.58   268     -4 LAND
99801   536 10658 ---- KISSINGEN             50.12   10.05   262     21 LAND
99802   489 10671 ---- COBURG                50.17   10.59   322     -1 LAND
99803   489 10675 ---- BAMBERG               49.53   10.55   243     31 LAND
99804   405 10685 ---- HOF                   50.19   11.53   567    -13 LAND
99805   476 10686 ---- WUNSIEDEL-SCHOENBRUN  50.02   11.58   622     -1 LAND
99806   489 10688 ---- WEIDEN                49.40   12.11   438    -14 LAND
99807   489 10704 ---- BERUS                 49.16    6.41   363    -15 LAND
99808   476 10706 ---- THOLEY                49.29    7.03   396    -48 LAND
99809   667 10708 EDDR SAARBRUECKEN          49.13    7.07   322    -52 LAND
99810   489 10724 ---- WEINBIET              49.23    8.07   553   -221 BERG
99811   505 10729 ---- MANNHEIM              49.31    8.33    96      0 LAND
99812   403 10731 ---- RHEINSTETTEN          48.58    8.19   118     -5 LAND
99801   489 10733 ---- WAIBSTADT             49.17    8.55   237    -22 LAND
99802   476 10736 ---- MUEHLACKER            48.58    8.52   244      9 LAND
99803   638 10738 EDDS STUTTGART-ECHT.       48.41    9.13   396    -36 LAND
99804   505 10739 ---- STUTTGART-SCHN.       48.50    9.12   314    -40 LAND
99805   489 10742 ---- OEHRINGEN             49.13    9.31   276    -20 LAND
99806   454 10743 ETHN NIEDERSTETTEN         49.24    9.58   468    -12 LAND
99807   489 10756 ---- FEUCHTWANGEN          49.10   10.22   475      2 LAND
99808   476 10761 ---- WEISSENBURG-EMETZH.   49.01   10.56   439     14 LAND
99809   667 10763 EDDN NUERNBERG             49.30   11.03   318      2 LAND
99810   575 10765 ETHR ROTH                  49.13   11.06   388    -10 LAND
99811   449 10771 ---- KUEMMERSBRUCK         49.26   11.54   419     35 LAND
99812   489 10776 ---- REGENSBURG            49.02   12.06   365     -7 LAND
99801   476 10777 ---- GELBELSEE             48.57   11.26   539    -62 LAND
99802   489 10782 ---- WALDMUENCHEN          49.23   12.41   499      3 LAND
99803   489 10788 ---- STRAUBING             48.50   12.34   350     19 LAND
99804   370 10791 ---- GR.ARBER              49.07   13.08  1446   -635 BERG
99805   387 10796 ---- ZWIESEL               49.02   13.14   612      4 LAND
99806   489 10803 ---- FREIBURG              48.01    7.50   236     18 LAND
99807   489 10805 EDTL LAHR                  48.22    7.50   156      1 LAND
99808   481 10815 ---- FREUDENST.            48.27    8.25   797    -36 LAND
99809   481 10818 ---- KLIPPENECK            48.07    8.45   973   -136 BERG
99810   481 10827 ETGZ MESSSTETTEN           48.11    9.00   920    -94 LAND
99811   489 10836 ---- STOETTEN              48.40    9.52   734      2 LAND
99812   449 10837 ETHL LAUPHEIM              48.13    9.55   538      7 LAND
99801   476 10850 ---- HARBURG               48.47   10.43   502    -30 LAND
99802   489 10852 EDMA AUGSBURG              48.26   10.56   463      5 LAND
99803   449 10853 ETSN NEUBURG/DONAU         48.43   11.13   380     34 LAND
99804   449 10856 ETSL LECHFELD              48.11   10.51   555     12 LAND
99805   449 10857 ETSA LANDSBERG             48.04   10.54   623    -21 LAND
99806   188 10860 ETSI INGOLSTADT            48.43   11.32   367      1 LAND
99807   505 10863 ---- WEIHENSTEPHAN         48.24   11.42   470    -12 LAND
99808   476 10865 ---- MUENCHEN STADT        48.08   11.33   520     32 LAND
99809   638 10870 EDDM MUENCHEN-FL.          48.22   11.48   453      5 LAND
99810   476 10872 ---- GOTTFRIEDING          48.40   12.32   350      6 LAND
99811   400 10875 ---- MUEHLDORF             48.17   12.30   406     43 LAND
99812   400 10895 ---- FUERSTENZELL          48.33   13.21   476      2 LAND
99801   568 10908 ---- FELDBERG/S.           47.53    8.00  1486   -524 BERG
99802   476 10945 ---- LEUTKIRCH-HERLAZHFN.  47.48   10.02   672     23 LAND
99803   489 10946 EDMK KEMPTEN               47.43   10.20   705     -5 LAND
99804   481 10948 ---- OBERSTDORF            47.24   10.17   810    221 LAND
99805   176 10954 ETHA ALTENSTADT            47.50   10.52   739     50 LAND
99806   493 10961 ---- ZUGSPITZE             47.25   10.59  2960  -1417 BERG
99807   659 10962 ---- HOHENPEISS.BG         47.48   11.01   977   -285 BERG
99808   489 10963 ---- GARMISCH              47.29   11.04   719    346 LAND
99809   489 10982 ---- CHIEMING              47.53   12.32   549      1 LAND
99810   179 11001 ---- WOLFSEGG              48.06   13.40   660   -202 LAND
99811   177 11008 ---- ROHRBACH              48.34   14.00   602     55 LAND
99812   476 11010 LOWL LINZ FL.              48.14   14.11   298     18 LAND
99801   326 11012 ---- KREMSMUENSTER         48.04   14.08   382    -23 LAND
99802   205 11018 ---- AMSTETTEN             48.07   14.54   266    109 LAND
99803   329 11019 ---- ALLENSTEIG            48.41   15.22   599    -20 LAND
99804   177 11020 ---- ZWETTL                48.37   15.12   505     47 LAND
99805   386 11021 ---- LITSCHAU              48.57   15.02   558     33 LAND
99806   282 11022 ---- RETZ                  48.46   15.56   320     14 LAND
99807   404 11030 LOXT TULLN                 48.19   16.07   175     30 LAND
99808   321 11032 ---- POYSDORF              48.40   16.38   202     55 LAND
99809   177 11034 ---- WIEN/CITY             48.12   16.22   171      9 LAND
99810   404 11035 ---- WIEN/HOHE WARTE       48.15   16.22   195    -15 LAND
99811   476 11036 LOWW WIEN FL.              48.07   16.34   183    -19 LAND
99812   177 11040 ---- WIEN/UNTERLAA         48.08   16.25   201    -36 LAND
99801   303 11053 ---- RIED IM INNKREIS      48.13   13.29   431    -15 LAND
99802   177 11055 ---- SCHAERDING            48.28   13.26   314     67 LAND
99803   177 11060 ---- LINZ                  48.18   14.17   262     11 LAND
99804   177 11070 ---- KREMS                 48.25   15.37   203     57 LAND
99805   177 11075 ---- LANGENLOIS            48.28   15.42   204     57 LAND
99806   322 11078 ---- LILIENFELD/TARSCHBER  48.02   15.35   681    -45 LAND
99807   177 11082 ---- GUMPOLDSKIRCHEN       48.02   16.17   219    -10 LAND
99808   329 11101 ---- BREGENZ               47.30    9.45   424     18 LAND
99809   235 11105 ---- FELDKIRCH             47.16    9.37   438    158 LAND
99810   159 11109 ---- ST.ANTON AM ARLBERG   47.08   10.16  1289    176 LAND
99811   256 11110 ---- GALZIG                47.08   10.14  2080   -137 LAND
99812   177 11112 ---- LANDECK               47.09   10.34   785    731 LAND
99801   476 11120 LOWI INNSBRUCK FL.         47.16   11.21   581    579 LAND
99802   142 11127 ---- OBERGURGL             46.52   11.01  1941    522 BERG
99803   311 11130 LOIK KUFSTEIN              47.35   12.10   493    330 LAND
99804   377 11138 ---- ALPINZENTRUM RUDOL.   47.08   12.38  2317   -236 BERG
99805   327 11140 ---- LOFER                 47.35   12.42   629    104 LAND
99806   281 11141 ---- BISCHOFSHOFEN         47.24   13.13   543    370 LAND
99807   168 11144 ---- ZELL A.SEE            47.20   12.48   766    351 LAND
99808   247 11146 ---- SONNBLICK             47.03   12.57  3106  -1027 BERG
99809   291 11148 ---- ST.MICHAEL/LUNGAU     47.06   13.39  1094    358 LAND
99810   168 11149 ---- OBERTAUERN            47.15   13.34  1743     93 LAND
99811   476 11150 LOWS SALZBURG FL.          47.48   13.00   430     48 LAND
99812   188 11155 ---- FEUERKOGEL            47.49   13.43  1618   -700 BERG
99801   410 11157 LOXA AIGEN/ENNS            47.32   14.08   638    447 LAND
99802   386 11165 LOXZ ZELTWEG               47.12   14.45   677    327 LAND
99803   326 11170 ---- LUNZ                  47.51   15.04   614    -30 LAND
99804   142 11173 ---- FISCHBACH             47.27   15.39  1034    -18 LAND
99805   328 11182 LOXN WIENER NEUSTADT       47.50   16.13   285    -42 LAND
99806   404 11190 ---- EISENSTADT            47.51   16.32   184     38 LAND
99807   293 11192 ---- KLEINZICKEN           47.12   16.20   267     37 LAND
99808   160 11201 ---- SILLIAN               46.45   12.25  1081    293 LAND
99809   223 11204 LOKL LIENZ                 46.50   12.48   659    695 LAND
99810   257 11212 ---- VILL.ALPE             46.36   13.40  2140  -1169 BERG
99811   265 11213 ---- VILLACH               46.37   13.52   495    253 LAND
99812   136 11221 ---- KOEFLACH              47.04   15.05   463    -14 LAND
99801   476 11231 LOWK KLAGENFURT FL.        46.39   14.20   448     83 LAND
99802   172 11232 ---- FEISTRITZ             46.34   14.46   532     16 LAND
99803   476 11240 LOWG GRAZ FL.              47.00   15.26   340     65 LAND
99804   122 11252 ---- VIRGEN (OSTTIROL)     47.00   12.27  1212    543 LAND
99805   126 11255 ---- KOETSCHACH            46.41   13.00   722     51 LAND
99806   177 11270 ---- DELLACH IM DRAUTAL    46.44   13.05   625    613 LAND
99807   144 11272 ---- SPITTAL/DRAU (TAWES)  46.47   13.29   542    309 LAND
99808   149 11280 ---- MURAU                 47.07   14.11   814    250 LAND
99809   148 11285 ---- DEUTSCHLANDSBERG      46.49   15.14   354    -11 LAND
99810   150 11290 ---- GRAZ (UNIVERSITAET)   47.05   15.27   367     38 LAND
99811   177 11292 ---- LASSNITZHOEHE         47.05   15.35   524      9 LAND
99812   169 11308 ---- WARTH                 47.15   10.11  1475    -10 LAND
99801   141 11310 ---- ISCHGL                46.59   10.19  2327   -133 BERG
99802   169 11312 ---- GALTUER               46.58   10.11  1584    185 LAND
99803   177 11314 ---- REUTTE AUTOM.         47.30   10.43   842     13 LAND
99804   141 11340 ---- SCHMITTENHOEHE        47.20   12.44  1956   -732 BERG
99805   177 11350 ---- SALZBURG              47.47   13.03   423     55 LAND
99806   177 11355 ---- WINDISCHGARSTEN       47.44   14.20   596     11 LAND
99807   177 11357 ---- ST. WOLFGANG          47.44   13.27   537    133 LAND
99808   177 11380 ---- REICHENAU/RAX         47.42   15.50   486    -34 LAND
99809   150 11390 ---- HARTBERG              47.17   15.59   330     50 LAND
99810   229 11406 ---- EGER                  50.04   12.23   483    -22 LAND
99811   468 11414 LKKV KARLSBAD              50.12   12.55   606    -11 LAND
99812   212 11423 ---- PRIMDA                49.40   12.41   743    -80 LAND
99801   230 11438 ---- TUSIMICE              50.23   13.20   322    -11 LAND
99802   208 11450 ---- PLZEN (AUT. STATION)  49.45   13.21   331     35 LAND
99803   222 11457 ---- CHURANOV              49.04   13.37  1122    -46 BERG
99804   220 11487 ---- KOCELOVICE            49.28   13.50   519      5 LAND
99805   208 11502 ---- AUSSIG                50.41   14.02   375    -65 LAND
99806   220 11509 ---- DOKSANY               50.28   14.10   158     39 LAND
99807   466 11518 LKPR PRAG FL.              50.06   14.15   380    -34 LAND
99808   229 11520 ---- PRAG                  50.01   14.27   304    -18 LAND
99809   219 11538 ---- TEMELIN               49.12   14.20   500    -61 LAND
99810   466 11567 ---- PRAHA (KBELI AIRP.)   50.07   14.32   285      0 LAND
99811   230 11603 LKLB LIBEREC               50.46   15.01   405     37 LAND
99812   466 11624 ---- CASLAV                49.56   15.23   242    -26 LAND
99801   219 11628 ---- KRAMOLIN-KOSETICE     49.35   15.05   534    -49 LAND
99802   200 11643 ---- PEC POD SNEZKOU       50.41   15.44   816     51 LAND
99803   466 11652 LKPD PARDUBICE             50.01   15.44   225      0 LAND
99804   220 11659 ---- PRIBYSLAW             49.35   15.46   533     20 LAND
99805   466 11679 ---- USTI NAD ORLICI       49.59   16.25   402     12 LAND
99806   190 11683 ---- SVRATOUCH             49.44   16.02   734    -74 LAND
99807   466 11692 ---- NAMEST NAD OSLAVOU    49.10   16.07   473    -34 LAND
99808   220 11693 ---- DUKOVANY              49.06   16.08   400     15 LAND
99809   198 11698 ---- KUCHAROVICE           48.53   16.05   334      0 LAND
99810   397 11710 ---- LUKA                  49.39   16.57   513      7 LAND
99811   466 11723 LKTB BRUENN                49.09   16.42   238      3 LAND
99812   230 11774 ---- HOLESOV               49.19   17.34   224     43 LAND
99801   466 11782 LKMT OSTRAVA/MOSNOV        49.41   18.07   257     24 LAND
99802   458 11787 ---- LYSA HORA/RIESENGEB.  49.33   18.27  1324   -608 LAND
99803   465 11816 LZIB BRATISLAVA            48.10   17.12   132      9 LAND
99804   165 11819 ---- JASLOVSKE BOHUNICE    48.29   17.40   176      5 LAND
99805   358 11826 LZPP PIESTANY              48.37   17.50   164     37 LAND
99806   346 11855 ---- NITRA                 48.17   18.08   135     -4 LAND
99807   135 11856 ---- MOCHOVCE              48.17   18.27   261     15 LAND
99808   374 11858 ---- HURBANOVO             47.52   18.12   115     -1 LAND
99809   391 11867 ---- PRIEVIDZA             48.46   18.35   260     -6 LAND
99810   354 11880 ---- DUDINCE               48.10   18.52   139     16 LAND
99811   471 11903 LZSL SLIAC                 48.39   19.09   314     42 LAND
99812   367 11927 ---- LUCENEC               48.20   19.44   214    -18 LAND
99801   372 11933 ---- STREBSKE PLESO        49.07   20.05  1354     77 LAND
99802   418 11934 LZTT POPRAD/T.             49.04   20.15   694     -4 LAND
99803   317 11938 ---- TELGART               48.51   20.11   901     49 LAND
99804   426 11968 LZKZ KOSICE                48.40   21.13   230    -19 LAND
99805   367 11976 ---- STROPKOV,TISINEC      49.13   21.39   216     81 LAND
99806   366 11978 ---- MILHOSTOV             48.40   21.43   105      9 LAND
99807   377 11993 LZKC KAMENICA NAD C.       48.56   22.00   176     36 LAND
99808   478 12105 ---- KOSZALIN              54.12   16.10    33    -10 KUES
99809   468 12120 ---- LEBA                  54.45   17.32     2     26 KUES
99810   478 12135 ---- HEL                   54.36   18.49     1     -1 MEER
99811   478 12160 EPEL ELBLAG                54.10   19.26    40    -12 LAND
99812   478 12185 ---- KETRZYN               54.04   21.22   107     24 LAND
99801   478 12195 EPSU SUWALKI               54.08   22.57   184     -2 LAND
99802   478 12200 ---- SWINEMUENDE           53.55   14.14     5     -1 KUES
99803   478 12205 ---- STETTIN               53.24   14.37     1     31 LAND
99804   234 12210 ---- RESKO                 53.46   15.25    52      2 LAND
99805   478 12230 EPPI PILA                  53.08   16.45    72    -11 LAND
99806   478 12235 ---- CHOJNICE              53.42   17.33   172    -11 LAND
99807   478 12250 EPTO TORUN                 53.02   18.35    69     14 LAND
99808   478 12270 ---- MLAWA                 53.06   20.22   147      5 LAND
99809   478 12280 EPMJ MIKOLAJKI             53.47   21.35   127     19 LAND
99810   478 12295 EPBK BIALYSTOK             53.06   23.10   148     18 LAND
99811   478 12300 ---- GORZOW WLKP           52.44   15.17    71     -9 LAND
99812   478 12310 ---- SLUBICE               52.21   14.35    21     23 LAND
99801   478 12330 EPPO POSEN                 52.25   16.50    86    -10 LAND
99802   322 12345 ---- KOLO                  52.12   18.40   115     -8 LAND
99803   316 12360 EPPL PLOCK                 52.35   19.44   106    -27 LAND
99804   478 12375 EPWA WARSCHAU              52.10   20.58   106    -15 LAND
99805   478 12385 ---- SIEDLCE               52.15   22.15   152      8 LAND
99806   478 12400 EPZG ZIELONA GORA          51.56   15.32   192    -93 LAND
99807   475 12415 ---- LEGNICA BARTOSZOW     51.11   16.13   122     -3 LAND
99808   260 12418 EPLS LESZNO                51.50   16.32    91     14 LAND
99809   478 12424 EPWR WROCLAW II            51.06   16.53   120     14 LAND
99810   478 12435 ---- KALISZ                51.47   18.05   137      1 LAND
99811   478 12455 ---- WIELUN                51.13   18.34   199    -28 LAND
99812   478 12465 EPLL LODZ                  51.44   19.24   187     28 LAND
99801   478 12469 ---- SULEJOW               51.21   19.52   188     -2 LAND
99802   478 12488 ---- KOZIENICE             51.34   21.32   123      3 LAND
99803   478 12495 EPLR LUBLIN RADAWIEC       51.13   22.24   238    -19 LAND
99804   478 12500 EPJG JELENIA GORA          50.54   15.48   342     60 LAND
99805   419 12510 ---- SNIEZKA               50.44   15.44  1604   -736 BERG
99806   478 12520 ---- KLODZKO               50.26   16.37   356     37 LAND
99807   478 12530 ---- OPOLE                 50.40   17.58   163     10 LAND
99808   478 12540 ---- RACIBORZ              50.04   18.11   206     16 LAND
99809   260 12550 EPCH CZESTOCHOWA           50.49   19.06   293    -32 LAND
99810   478 12560 EPKM KATOWICE              50.14   19.02   284     -1 LAND
99811   473 12566 EPKK KRAKOW                50.05   19.48   237     29 LAND
99812   478 12570 EPKA KIELCE                50.49   20.42   260      1 LAND
99801   473 12580 EPRZ RZESZOW-JASIONKA      50.06   22.03   200     11 LAND
99802   260 12585 ---- SANDOMIERZ            50.42   21.43   217    -54 LAND
99803   478 12600 EPBA BIELSKO-BIALA         49.48   19.00   398     66 LAND
99804   470 12625 ---- ZAKOPANE              49.18   19.58   857    110 LAND
99805   316 12660 EPNL NOWY SACZ             49.37   20.42   292     28 LAND
99806   478 12690 ---- LESKO                 49.28   22.20   420      2 LAND
99807   133 12766 ---- JOSVAFO               48.29   20.32   305     10 LAND
99808   465 12772 LHMC MISKOLC               48.05   20.46   232     48 LAND
99809   133 12805 ---- SOPRON                47.41   16.36   233    -45 LAND
99810   228 12815 ---- MOSONMAGYAROVAR       47.53   17.17   121      6 LAND
99811   258 12822 ---- GYOR                  47.43   17.41   116     -6 LAND
99812   162 12830 ---- VESZPREM              47.04   17.50   280     36 LAND
99801   465 12843 ---- BUDAPEST/LORINC       47.26   19.11   138     -7 LAND
99802   133 12846 ---- AGARD                 47.11   18.37   105     39 LAND
99803   465 12882 LHDC DEBRECEN              47.29   21.36   110      2 LAND
99804   202 12910 ---- SZENTGOTTHARD         46.55   16.19   312    -34 LAND
99805   460 12922 ---- SARMELLEK             46.41   17.10   124      8 LAND
99806   286 12925 ---- NAGYKANIZSA           46.27   16.58   139     26 LAND
99807   420 12935 ---- SIOFOK                46.55   18.03   108     26 LAND
99808   465 12942 LHPP PECS/POGANY           46.00   18.14   201    -34 LAND
99809   453 12970 LHKE KECSKEMET             46.55   19.45   113     -5 LAND
99810   465 12982 LHUD SZEGED                46.15   20.06    82     -3 LAND
99811   420 12992 LHBC BEKESCSABA            46.41   21.10    88      1 LAND
99812   465 13168 ---- NOVI SAD              45.20   19.51    86      5 LAND
99801   469 13262 ---- LOZNICA               44.33   19.14   121     35 LAND
99802   467 13269 ---- VALJEVO               44.19   19.55   176     12 LAND
99803   426 13272 ---- BEOGRAD/SURCIN        44.49   20.17    96     -8 LAND
99804   470 13274 LYBE BELGRAD               44.48   20.28   132    -36 LAND
99805   464 13278 ---- KRAGUJEVAC            44.02   20.56   185     26 LAND
99806   476 13295 ---- NEGOTIN               44.14   22.33    44     11 LAND
99807   468 13367 ---- ZLATIBOR              43.44   19.43  1029    -11 LAND
99808   474 13376 LYKT KRALJEVO              43.42   20.42   217     75 LAND
99809   468 13378 ---- KOPAONIK              43.17   20.48  1713   -418 LAND
99810   475 13388 LYNI NIS                   43.20   21.54   202     38 LAND
99811   468 13389 ---- LESKOVAC              42.59   21.57   232     27 LAND
99812   413 13462 LYTI PODGORICA/GOLUBOBCI   42.22   19.15    33    -20 LAND
99801   467 13489 ---- VRANJE                42.33   21.55   433     54 LAND
99802   412 13586 LWSK SKOPJE                41.58   21.39   238     81 LAND
99803    95 13615 LATI TIRANA                41.20   19.47    89     44 LAND
99804   467 14014 LJLJ LJUBLJANA/BRNIK       46.13   14.29   364    -15 LAND
99805   457 14026 LJMB MARIBOR/SLIVNICA      46.29   15.41   264     -5 LAND
99806   300 14236 ---- ZAGREB/GRIC           45.49   15.58   157    -31 LAND
99807   444 14241 LDZA ZAGREB/PLESO          45.44   16.04   106     20 LAND
99808   417 14256 ---- BILOGORA              45.53   17.12   262    -83 LAND
99809   429 14280 ---- OSIJEK-CEPIN          45.30   18.34    89      2 LAND
99810   447 14307 LDPL PULA                  44.54   13.55    63     52 KUES
99811   417 14317 LDRI RIJEKA                45.13   14.35    85      7 KUES
99812   414 14330 ---- GOSPIC                44.33   15.22   564     42 LAND
99801   444 14431 ---- ZADAR                 44.06   15.21    82    -37 KUES
99802   444 14444 LDSP SPLIT/RESNIK          43.32   16.18    21    195 KUES
99803   455 14445 ---- SPLIT/MARJAN          43.31   16.26   122     94 KUES
99804   416 14474 LDDU DUBROVNIK             42.34   18.16   164    173 KUES
99805   317 14528 LQBI BIHAC                 44.49   15.53   250     65 LAND
99806   216 14537 ---- SANSKI MOST           44.46   16.42   154     50 LAND
99807   419 14542 ---- BANJA LUKA            44.47   17.13   153     41 LAND
99808   180 14543 ---- JAJCE                 44.21   17.16   430    224 LAND
99809   228 14544 ---- BUGOJNO               44.04   17.28   562    177 LAND
99810   214 14549 ---- ZENICA                44.13   17.54   345     91 LAND
99811   217 14554 ---- GRADACAC              44.53   18.26   136     62 LAND
99812   420 14557 ---- TUZLA                 44.33   18.42   305     29 LAND
99801   222 14640 LQLV LIVNO                 43.50   17.01   724    120 LAND
99802   436 14648 LQMO MOSTAR                43.21   17.48    99     80 LAND
99803   228 14650 ---- IVAN SEDLO            43.46   18.02   970      0 LAND
99804   410 14652 ---- BJELASNICA            43.43   18.16  2067   -538 LAND
99805   451 14654 ---- SARAJEVO-BEJELAVE     43.52   18.26   630     -4 LAND
99806   478 15020 ---- BOTOSANI              47.44   26.39   161      1 LAND
99807   478 15080 LROD ORADEA                47.02   21.54   136      4 LAND
99808   508 15120 LRCL CLUJ-NAPOCA           46.47   23.34   410     38 LAND
99809   478 15145 LRTM TIRGU MURES           46.32   24.32   309     43 LAND
99810   478 15150 LRBC BACAU                 46.32   26.55   184      5 LAND
99811   478 15200 LRAR ARAD                  46.08   21.21   116     14 LAND
99812   435 15235 ---- FAGARAS               45.51   24.59   428     32 LAND
99801   508 15247 LRTR TIMISOARA             45.46   21.15    86     14 LAND
99802   478 15260 LRSB SIBIU                 45.48   24.09   443     18 LAND
99803   495 15302 ---- PREDEAL               45.31   25.35  1090    -79 LAND
99804   456 15338 ---- ORAVITA               45.02   21.41   200     -9 LAND
99805   508 15420 LRBS BUKAREST              44.30   26.08    90    -12 LAND
99806   485 15421 LROP BUKAREST/OTOPENI      44.33   26.06    95    -17 LAND
99807   478 15480 ---- CONSTANTA             44.13   28.39    13     16 KUES
99808   447 15552 LBWN VARNA                 43.12   27.55    41     87 KUES
99809   447 15614 LBSF SOFIA                 42.39   23.23   588    -33 LAND
99810   414 15655 LBBG BURGAS                42.29   27.29    16     19 KUES
99811   416 16008 LIVE RESCHENPASS           46.37   10.32  1459    215 LAND
99812   351 16020 LIPB BOZEN                 46.28   11.20   241    565 LAND
99801   408 16021 LIVR PASSO ROLLE           46.18   11.47  2004    -91 BERG
99802   431 16022 LIVP PAGANELLA             46.09   11.02  2125  -1064 BERG
99803   404 16033 LIVD DOBBIACO              46.44   12.13  1222    322 LAND
99804   400 16036 LIPA AVIANO                46.02   12.36   128    -50 LAND
99805   255 16040 LIVO TARVISIO              46.30   13.35   777    177 LAND
99806   263 16045 LIPI UDINE/RIVOLTO         45.59   13.02    51    -13 LAND
99807   430 16052 LIMH PIAN ROSA             45.56    7.42  3480   -906 BERG
99808   412 16059 LIMF TURIN                 45.13    7.39   301      0 LAND
99809   372 16066 LIMC MILANO/MALPENSA       45.37    8.44   234     14 LAND
99810   412 16076 LIME BERGAMO               45.40    9.42   238    -27 LAND
99811   412 16080 LIML MAILAND               45.26    9.17   107     22 LAND
99812   422 16084 LIMS PIACENZA              44.55    9.44   134     -8 LAND
99801   424 16088 LIPL BRESCIA/GHEDI         45.25   10.17   102      5 LAND
99802   372 16105 LIPZ VENEDIG               45.30   12.20     2      2 KUES
99803   443 16110 LIVT TRIEST                45.39   13.45     8     55 KUES
99804   412 16120 LIMJ GENUA                 44.25    8.51     2    141 KUES
99805   226 16125 ---- SARZANA/LUNI          44.05    9.59     9     75 KUES
99806   258 16138 LIPF FERRARA               44.50   11.37    10     -1 LAND
99807   413 16140 LIPE BOLOGNA               44.32   11.18    36     12 LAND
99808   416 16149 LIPR RIMINI                44.02   12.37    12     22 KUES
99809   426 16158 LIRP PISA-S.GIUSTO         43.41   10.23     2      0 LAND
99810   412 16170 LIRQ FLORENZ               43.48   11.12    40     64 LAND
99811   424 16206 LIRS GROSSETO              42.45   11.04     5     17 LAND
99812   173 16219 LIRK MONTE TERMINILLO      42.28   12.59  1874   -989 BERG
99801   372 16230 LIBP PESCARA               42.26   14.12    10     75 KUES
99802   412 16242 LIRF ROM                   41.48   12.14     2     24 KUES
99803   277 16244 ---- FROSINONE             41.38   13.18   180     27 LAND
99804   416 16245 LIRE PRATICA DI MARE       41.39   12.26     6     21 KUES
99805   421 16252 LIBS CAMPOBASSO            41.34   14.39   793     74 LAND
99806   425 16261 ---- AMENDOLA              41.32   15.43    57     -2 KUES
99807   372 16270 LIBD BARI                  41.08   16.47    34      9 KUES
99808   442 16280 LIQZ PONZA                 40.55   12.57   184   -178 KUES
99809   412 16289 LIRN NEAPEL                40.51   14.18    88    -21 KUES
99810   421 16294 LIQC CAPRI                 40.33   14.12   160     14 KUES
99811   388 16320 LIBR BRINDISI              40.39   17.57    15      9 KUES
99812   421 16325 ---- MARINA DI GINOSA      40.25   16.53     1     56 KUES
99801   412 16362 LICA LAMEZIA TERME         38.54   16.15    15    131 LAND
99802   412 16405 LICJ PALERMO               38.11   13.06    21    112 KUES
99803   454 16420 LICF MESSINA               38.12   15.33    59     23 KUES
99804   401 16429 LICT TRAPANI/BIRGI         37.55   12.30     7     18 KUES
99805   258 16434 LICX PRIZZI                37.43   13.26  1034   -230 LAND
99806   273 16453 ---- GELA                  37.05   14.13    18     87 KUES
99807   412 16460 LICC CATANIA               37.28   15.03    11     14 KUES
99808    97 16464 ---- SIRACUSA /SICI        37.04   15.17     1     23 KUES
99809   412 16531 LIEO OLBIA/COSTA SMERALDA  40.54    9.31    11     80 KUES
99810   444 16550 ---- CAPO BELLAVISTA       39.56    9.43   138    139 KUES
99811   412 16560 LIEE CAGLIARI              39.15    9.03     4     14 KUES
99812   449 16597 LMML MALTA                 35.51   14.29    91    -26 KUES
99801   357 16606 ---- SERRAI                41.04   23.34    33     -8 LAND
99802   445 16622 LGTS THESSALONIKI          40.31   22.58     8     17 KUES
99803   445 16624 ---- CHRYSOUPOLI           40.59   24.36     5      1 KUES
99804   445 16627 LGAL ALEXANDROUPOLI        40.51   25.55     7     23 KUES
99805   351 16632 LGKZ KOZANI                40.18   21.47   634    -12 LAND
99806   445 16641 LGKR KORFU                 39.37   19.55     2     70 KUES
99807   391 16642 LGID IOANNINA NATIONAL     39.42   20.49   483    111 LAND
99808   445 16648 LGLR LARISSA               39.38   22.25    74     20 LAND
99809   445 16650 LGLM LIMNOS                39.55   25.14     5      7 KUES
99810   443 16667 LGMT MYTILINI/AIRPORT      39.04   26.36     3     79 KUES
99811   212 16675 ---- STYLIS LAMIA          38.54   22.24   144      4 LAND
99812   445 16682 LGAD ANDRAVIDA             37.55   21.17    10      3 LAND
99801   445 16684 LGSY SKYROS                38.58   24.29    27     -8 KUES
99802   384 16685 LGKF KEFALHNIA             38.07   20.30    19    137 KUES
99803   445 16706 LGHI CHIOS                 38.20   26.08     5     96 KUES
99804   445 16710 LGTP TRIPOLIS/INTL         37.32   22.24   644    -13 LAND
99805   445 16716 LGAT ATHEN                 37.54   23.44    28     91 KUES
99806   443 16723 LGSM SAMOS                 37.42   26.55     2    258 KUES
99807   445 16726 LGKL KALAMATA              37.04   22.01     6     59 KUES
99808   442 16732 LGNX NAXOS                 37.06   25.23     9    132 KUES
99809   440 16741 LGPA PAROS                 37.01   25.08    76     64 KUES
99810   440 16742 LGKO KOS                   36.47   27.04   129    -85 KUES
99811   212 16743 LGKC KYTHIRA               36.17   23.01   167    -50 KUES
99812   445 16746 LGSA SOUDA/AIRPORT         35.29   24.07   146    -95 KUES
99801   445 16749 LGRP RHODOS                36.24   28.05     4     58 KUES
99802   445 16754 LGIR HERAKLION             35.20   25.11    37    196 KUES
99803   267 16759 ---- TYMBAKION             35.00   24.45     7    147 KUES
99804   386 16765 LGKP KARPATHOS             35.31   27.15     6      1 KUES
99805   455 17022 LTAS ZONGULDAK             41.27   31.48   137     78 KUES
99806   449 17024 ---- INEBOLU               41.59   33.46    64    116 KUES
99807   450 17026 LTCM SINOP                 42.02   35.10    32     15 KUES
99808   460 17030 ---- SAMSUN                41.17   36.18     4     13 KUES
99809   441 17031 ---- CARSAMBA/SAMSUN       41.15   36.34     5     12 KUES
99811   456 17050 ---- EDIRNE                41.40   26.34    48    -13 LAND
99812   454 17056 ---- TEKIRDAG              40.59   27.33     3     31 KUES
99801   446 17060 LTBA ISTANBUL              40.58   28.49    48    -15 KUES
99802   456 17070 ---- BOLU                  40.44   31.36   743    -33 LAND
99803   445 17090 LTAR SIVAS                 39.45   37.01  1285     63 LAND
99805   454 17116 LTBE BURSA                 40.11   29.04   100      9 LAND
99806   458 17128 LTAC ANKARA                40.07   32.59   953      6 LAND
99808   438 17195 LTAU KAYSERI/ERKILET       38.49   35.26  1055     44 LAND
99809   458 17219 LTBJ IZMIR/ADNAN MENDERE   38.16   27.09   125     16 KUES
99810   461 17240 LTBM ISPARTA               37.45   30.33   997     17 LAND
99811   432 17244 LTAN KONYA                 37.58   32.33  1032    -19 LAND
99812   446 17260 LTAJ GAZIANTEP             37.05   37.22   705     -1 LAND
99802   454 17290 LTBV BODRUM                37.02   27.26    26     49 KUES
99803   446 17295 LTBS MUGLA/DALAMAN         36.42   28.47     7    105 KUES
99804   450 17300 LTAI ANTALYA               36.42   30.44    50     22 KUES
99805   412 17350 LTAG ADANA                 37.00   35.25    73     -5 LAND
99806   448 17600 LCPH PAPHOS AIRPORT        34.43   32.29    11     53 KUES
99807   479 17601 LCRA AKROTIRI              34.35   32.59    23    163 KUES
99808   448 17609 LCLK LARNAKA               34.53   33.38     2     54 KUES
99804   446 26038 EETN TALLIN                59.25   24.48    44     -1 KUES
99805   428 26063 ULLI ST.PETERSBURG         59.58   30.18     4      0 KUES
99806   352 26115 ---- RISTNA                58.55   22.04     9     -9 KUES
99807   446 26242 EETU TARTU                 58.18   26.44    68     -4 LAND
99808   428 26298 ---- BOLOGOE               57.54   34.03   188    -18 LAND
99809   422 26314 ---- VENTSPILS             57.24   21.32     2     15 KUES
99810   427 26406 EVLA LIEPAJA               56.29   21.01     7      8 LAND
99811   427 26422 EVRA RIGA                  56.58   24.04     3      5 KUES
99812   427 26509 EYKL KLAIPEDA              55.42   21.09    10     14 KUES
99801   427 26524 EYSA SIAULIAI              55.56   23.19   106     24 LAND
99802   427 26554 ---- VERKHNEDVINSK         55.49   27.56   132     -3 LAND
99803   427 26629 ---- KAUNAS POCIUNAI       54.53   23.50    76     -2 LAND
99804   400 26659 ---- LEPEL                 54.53   28.42   174    -13 LAND
99805   422 26666 UMII VITEBSK               55.10   30.13   176      0 LAND
99806   428 26702 UMKK KOENIGSBERG           54.42   20.37    27     -2 LAND
99807   427 26730 EYVI VILNIUS               54.38   25.17   189    -35 LAND
99808   422 26825 UMMG GRODNO                53.36   24.03   134     -6 LAND
99809   427 26850 UMMM MINSK                 53.52   27.32   234     -1 LAND
99810   422 26863 UMOO MOGILEV YERM.         53.57   30.04   192    -10 LAND
99811   427 26887 ---- KOSTUCKOVICHI         53.22   32.04   168     -2 LAND
99810   427 33008 UMBB BREST                 52.07   23.41   142      1 LAND
99811   422 33027 ---- ZHITCKOVICHI          52.13   27.52   138    -12 LAND
99812   427 33041 UMGG GOMEL                 52.24   30.57   125     -1 LAND
99801   417 33261 ---- KONOTOP               51.14   33.12   144     12 LAND
99802   412 33345 UKKK KIEW                  50.24   30.27   179    -26 LAND
99803   388 33526 ---- IVANO-FRANKIVSK       48.56   24.42   275     -7 LAND
99804   393 33791 ---- KRYVYI RIH            48.03   33.13   123    -20 LAND
99805   421 33815 LUKK KISHINEV/KICHINAU     47.01   28.59   173    -69 LAND
99806   393 33837 UKOO ODESSA                46.29   30.38    64    -32 KUES
99809   393 34300 UKHH KHARKIV               49.58   36.08   154      3 LAND
99810   393 34504 UKDD DNIPROPETROVSK        48.36   34.58   141     -9 LAND
99810   412 40080 OSDI DAMASCUS              33.25   36.31   608     21 LAND
99811   428 40100 OLBA BEIRUT                33.49   35.29    29     79 KUES
99812   442 40180 LLBG TEL AVIV              32.00   34.54    40     12 KUES
99801   442 40199 LLET EILAT                 29.33   34.57    12     92 KUES
99802   413 40270 OJAM AMMAN                 31.59   35.59   778    -14 LAND
99803   413 40272 OJAI AMMAN/QUENN ALIA      31.40   35.58   721     -7 LAND
99809   412 60101 GMTT TANGER                35.44   -5.54    19     -9 KUES
99810   412 60115 GMFO OUJDA                 34.47   -1.56   468    -13 LAND
99811   417 60135 GMME RABAT                 34.03   -6.46    84     10 KUES
99812   412 60141 GMFF FES-SAIS              33.56   -4.59   579     22 LAND
99801   412 60150 GMFM MEKNES                33.53   -5.32   576    -23 LAND
99802   406 60155 GMMC CASABLANCA            33.34   -7.40    62    -36 KUES
99803   412 60156 GMMN CASABLANCA/MOHAMED    33.22   -7.35   200    -33 KUES
99804   412 60230 GMMX MARRAKECH             31.37   -8.02   468    -10 LAND
99805   412 60252 GMAD AGADIR/AL MASSIRA     30.20   -9.24    74     18 KUES
99806   384 60338 ---- MELILLA               35.17   -2.58    47     36 KUES
99807   412 60360 DABB ANNABA                36.50    7.49     3     -1 KUES
99808   412 60390 DAAG ALGIER                36.43    3.15    25    -16 KUES
99809   412 60419 DABC CONSTANTINE           36.17    6.37   694    -44 LAND
99810   404 60475 DABS TEBESSA               35.25    8.07   821     73 LAND
99811   412 60490 DAOO ORAN/ES SENIA         35.38   -0.36    90      1 LAND
99812   262 60535 DAFI DJELFA                34.20    3.23  1180    -42 LAND
99801   412 60566 DAUG GHARDAIA              32.24    3.48   468      3 LAND
99802   404 60571 DAOR BECHAR                31.30   -2.15   809      8 LAND
99803   412 60590 DAUE EL-GOLEA              30.34    2.52   397     26 LAND
99806   405 60710 DTKA TABARKA               36.57    8.45    21    154 KUES
99807   439 60715 DTTA TUNIS                 36.50   10.14     5     22 KUES
99808   422 60725 DTTN JENDOUBA              36.29    8.48   143      4 LAND
99809   439 60735 DTTK KAIROUAN              35.40   10.06    60    -14 LAND
99810   435 60740 DTMB MONASTIR/HABIB BOUR   35.45   10.45     2     49 KUES
99811   405 60750 DTTX SFAX EL-MAOU          34.43   10.41    21     -9 KUES
99812   441 60760 DTTZ TOZEUR                33.55    8.06    87    -38 LAND
99801   405 60769 DTTJ DJERBA                33.35   10.47     6     -2 KUES
99805   412 62305 ---- SALLUM PLATEAU        31.34   25.07     6    110 KUES
99806   412 62306 HEMM MERSA MATRUH          31.20   27.13    25     12 KUES
99807   412 62318 HEAX ALEXANDRIA/NOUZHA     31.12   29.57    -2      3 KUES
99808   412 62332 HEPS PORT SAID             31.17   32.14     1      0 KUES
99809   391 62366 HECA KAIRO                 30.08   31.24    64    -34 LAND
99806   176 A051  ---- WEESBY                54.50    9.09    22        LAND
99807   176 A112  ---- WRIXUM/FOEHR          54.41    8.32     8        LAND
99808   176 A138  ---- BORDELUM              54.38    8.56     8        LAND
99809   176 A159  ---- EGGEBEK               54.38    9.22    17        LAND
99810    76 A160  ---- FLENSBURG (SCHAEFERH  54.46    9.23    41        LAND
99811   176 A173  ---- SATRUP                54.41    9.38    35        LAND
99812   206 A191  ---- WAGERSROTT            54.40    9.49    40    -28 LAND
99801    76 A201  ---- HALLIG HOOGE          54.34    8.31     4        LAND
99802    76 A216  ---- STRUCKLAHNUNGSHOERN   54.30    8.49     7        KUES
99803   227 A226  ---- HATTSTEDT             54.32    9.02     5      5 LAND
99804   176 A345  ---- GROSS WITTENSEE       54.24    9.46    15        LAND
99805   206 A351  ---- ERFDE                 54.18    9.19    18    -12 LAND
99806   176 A397  ---- GROSSENBRODE          54.22   11.05     3        KUES
99807   176 A411  ---- KREMPEL               54.19    9.01     2        LAND
99808   227 A443  ---- OSTENFELD (RENDSBURG  54.19    9.49    14      2 LAND
99809   176 A473  ---- KOEHN                 54.20   10.28    40        LAND
99810    76 A480  ---- PUTLOS                54.19   10.48     5        KUES
99811   206 A481  ---- HOHWACHT              54.19   10.40    10     -1 KUES
99812    76 A505  ---- BUESUM                54.07    8.52     3        KUES
99801   176 A536  ---- HAALE                 54.10    9.34    26        LAND
99802   206 A653  ---- PADENSTEDT (PONY-PAR  54.01    9.56    17     16 LAND
99803    76 A699  ---- TRAVEMUENDE           53.58   10.53     2        KUES
99804   176 A752  ---- WEDDELBROOK           53.54    9.50    18        LAND
99805   206 A762  ---- WITTENBORN            53.55   10.14    38     -2 LAND
99806   176 A791  ---- SCHWARTAU,BAD -GROSS  53.56   10.42    26        LAND
99807   176 A940  ---- SPRENGE               53.41   10.22    55        LAND
99808   206 A981  ---- GRAMBEK               53.34   10.41    27      3 LAND
99809   206 B006  ---- HIDDENSEE-VITTE       54.34   13.06     1     -1 KUES
99810    76 B040  ---- DARSSER ORT (SWN)     54.28   12.30     4        KUES
99811   176 B085  ---- SAGARD                54.31   13.32     5        LAND
99812   206 B158  ---- STEINHAGEN-NEGAST     54.15   13.02    16    -15 LAND
99801    76 B203  ---- BASTORF-KAEGSDORF (S  54.08   11.40    51        KUES
99802   227 B258  ---- TRIBSEES              54.05   12.47     7      5 LAND
99803   206 B308  ---- KIRCHDORF/POEL        54.00   11.26    12     -5 KUES
99804   176 B320  ---- GERSDORF              54.05   11.44    52        LAND
99805   282 B334  ---- GROSS LUESEWITZ       54.04   12.20    40      0 LAND
99806   176 B365  ---- SUEDERHOLZ-NEUENDORF  54.06   13.09     5        LAND
99807   227 B382  ---- KARLSHAGEN            54.06   13.49     1      0 KUES
99808   176 B482  ---- GROSS KIESOW-SCHLAGT  54.01   13.30    34        LAND
99809   227 B488  ---- ANKLAM                53.50   13.41     9     -2 LAND
99810   176 B511  ---- GREVESMUEHLEN         53.50   11.10    25        LAND
99811   176 B525  ---- VENTSCHOW             53.47   11.34    43        LAND
99812   176 B531  ---- BAUMGARTEN            53.49   11.53    52        LAND
99801   176 B544  ---- PARUM                 53.49   12.07    10        LAND
99802   227 B556  ---- TETEROW               53.46   12.34    38      7 LAND
99803   176 B587  ---- RATHEBUR              53.44   13.47    10        LAND
99804   176 B629  ---- GOLDENBOW             53.32   11.46    52        LAND
99805   176 B670  ---- FRIEDLAND             53.40   13.32    22        LAND
99806   176 B687  ---- ROTHEMUEHL            53.36   13.49    23        LAND
99807   176 B710  ---- DODOW                 53.30   11.00    34        LAND
99808   176 B728  ---- NEUSTADT-GLEWE-FRIED  53.28   11.34    35        LAND
99809   176 B747  ---- PLAU AM SEE           53.28   12.14    66        LAND
99810   176 B766  ---- GROSS LUKOW           53.32   13.01    54        LAND
99811   176 B818  ---- REDEFIN               53.21   11.12    16        LAND
99812    76 B853  ---- RECHLIN               53.20   12.43    62        LAND
99801   227 B898  ---- GRAMBOW-SCHWENNENZ    53.23   14.22    50    -19 LAND
99802   176 B926  ---- MALK GOEHREN          53.13   11.22    31        LAND
99803   176 B951  ---- KRUEMMEL              53.16   12.43    64        LAND
99804   206 C720  ---- HAMBURG-NEUWIEDENTH.  53.29    9.54     3     43 LAND
99805    76 E006  ---- BORKUM-SUEDERSTRASSE  53.35    6.40    12        KUES
99806   227 E008  ---- BORKUM-FLUGPLATZ      53.36    6.42     3     -3 KUES
99807   176 E025  ---- DORNUM                53.39    7.26     1        LAND
99808    76 E031  ---- SPIEKEROOG (SWN)      53.46    7.40    14        MEER
99809   206 E043  ---- WANGERLAND-HOOKSIEL   53.38    8.05     8     -7 KUES
99810   176 E067  ---- LANGEN-HOLSSEL, KREI  53.42    8.38    13        LAND
99811   206 E078  ---- STEINAU,KR.CUXHAVEN   53.41    8.52     1      2 LAND
99812   206 E082  ---- FREIBURG/ELBE         53.50    9.15     2      0 LAND
99801   176 E087  ---- LAMSTEDT              53.38    9.06    25        LAND
99802   176 E091  ---- DROCHTERSEN           53.43    9.23     1        LAND
99803    76 E095  ---- RUTHENSTROM           53.43    9.25     7        LAND
99804   206 E099  ---- MITTELNKIRCHEN-HOHEN  53.33    9.37     1     26 LAND
99805   176 E103  ---- NORDEN-LEYBUCHTPOLDE  53.30    7.07     1        LAND
99806   176 E145  ---- BUTJADINGEN-INTE      53.29    8.23     1        LAND
99807   176 E158  ---- BEVERSTEDT            53.26    8.48     3        LAND
99808   168 E200  ---- BOCKHORN-GRABSTEDE    53.22    7.58    11        LAND
99809   176 E207  ---- DOLLART-KANALPOLDER   53.14    7.13     2        LAND
99810   176 E212  ---- MOORMERLAND-NEERMOOR  53.19    7.26     0        LAND
99811   176 E229  ---- WESTERSTEDE           53.15    7.56     7        LAND
99812   176 E232  ---- OVELGOENNE            53.23    8.27     2        LAND
99801   176 E234  ---- RASTEDE               53.14    8.13    16        LAND
99802    76 E235  ---- BRAKE                 53.21    8.30     1        LAND
99803   176 E246  ---- SCHWANEWEDE-NEUENKIR  53.13    8.31     1        LAND
99804   206 E254  ---- WORPSWEDE-HUETTENBUS  53.17    8.59     7     12 LAND
99805   176 E277  ---- KOENIGSMOOR           53.14    9.39    40        LAND
99806   176 E297  ---- BLECKEDE-WALMSBURG    53.14   10.51    12        LAND
99807   206 E298  ---- WENDISCH EVERN        53.13   10.28    62    -42 LAND
99808   176 E335  ---- HUDE/OLDENBURG        53.07    8.25     4        LAND
99809   176 E342  ---- OTTERSBERG-OTTERSTED  53.08    9.09    17        LAND
99810   227 E355  ---- ROTENBURG (W�MME)     53.08    9.20    32     -4 LAND
99811   176 E364  ---- HEESLINGEN-WIERSDORF  53.18    9.20    27        LAND
99812   176 E387  ---- ZERNIEN               53.04   10.53    83        LAND
99801   303 E402  ---- DOERPEN               52.57    7.19     8     -1 LAND
99802   227 E426  ---- GROSSENKNETEN-AHL.    52.55    8.13    42     -4 LAND
99803   227 E438  ---- BASSUM                52.52    8.42    40    -14 LAND
99804   176 E445  ---- SCHWARME              52.55    9.03    12        LAND
99805   176 E451  ---- VERDEN-DAUELSEN       52.58    9.14    21        LAND
99806   227 E475  ---- UELZEN                52.56   10.32    50      6 LAND
99807   176 E501  ---- TWIST-HEBELERMEER     52.44    7.05    19        LAND
99808   176 E513  ---- GROSS BERSSEN         52.46    7.29    27        LAND
99809   227 E525  ---- LOENINGEN             52.43    7.45    22      7 LAND
99810   176 E545  ---- BARNSTORF             52.42    8.29    37        LAND
99811   176 E564  ---- FRANKENFELD-HEDERN    52.46    9.24    18        LAND
99812   176 E571  ---- FALLINGBOSTEL, BAD    52.52    9.41    70        LAND
99801   176 E586  ---- SCHARNHORST-MARWEDE   52.44   10.20    72        LAND
99802   176 E601  ---- RINGE-GROSSRINGE      52.36    6.54    13        LAND
99803   206 E626  ---- ALFHAUSEN             52.29    7.55    65    -16 LAND
99804   176 E651  ---- KIRCHDORF, KREIS DIE  52.36    8.51    34        LAND
99805   227 E652  ---- NIENBURG              52.40    9.13    25      5 LAND
99806   176 E659  ---- REHBURG-LOCCUM        52.26    9.08    60        LAND
99807   176 E662  ---- ESSEL                 52.41    9.39    28        LAND
99808   176 E667  ---- NEUSTADT AM RUEBENBE  52.30    9.29    41        LAND
99809   176 E672  ---- WEDEMARK-ELZE         52.35    9.44    39        LAND
99810   176 E673  ---- CELLE (STADT)         52.37   10.04    38        LAND
99811   176 E688  ---- UETZE                 52.28   10.11    60        LAND
99812   227 E691  ---- WITTINGEN-VORHOP      52.38   10.40    72      0 LAND
99801   176 E704  ---- BENTHEIM, BAD         52.18    7.08    50        LAND
99802   176 E727  ---- ROTHENFELDE, BAD      52.06    8.11    95        LAND
99803    97 E732  ---- HAMELN                52.05    9.23    68        LAND
99804   176 E738  ---- RINTELN-VOLKSEN       52.08    9.07   212        LAND
99805   206 E739  ---- HAMELN-HASTENBECK     52.05    9.25    77     51 LAND
99806   206 E744  ---- BARSINGHAUSEN-HOHENB  52.19    9.26   110    -48 LAND
99807   176 E748  ---- SALZHEMMENDORF-LAUEN  52.05    9.33   175        LAND
99808   176 E755  ---- HANNOVER-HERRENHAUSE  52.24    9.40    50        LAND
99809   176 E756  ---- HANNOVER-KIRCHRODE    52.22    9.49    57        LAND
99810   176 E762  ---- LEHRTE-SIEVERSHAUSEN  52.22   10.08    66        LAND
99811   176 E764  ---- SPRINGE               52.13    9.34    98        LAND
99812   206 E790  ---- WOLFSBURG (SUEDWEST)  52.24   10.41    82    -18 LAND
99801    97 E792  ---- SUEPPLINGEN           52.14   10.55   129        LAND
99802   206 E798  ---- HELMSTEDT             52.15   10.58   110     26 LAND
99803   176 E799  ---- CREMLINGEN-DESTEDT    52.14   10.43   160        LAND
99804   176 E805  ---- OTTENSTEIN            51.57    9.24   295        LAND
99805   206 E818  ---- BEVERN                51.51    9.30   110     18 LAND
99806   176 E835  ---- EIMEN-VORWOHLE        51.53    9.44   265        LAND
99807   206 E839  ---- MORINGEN-LUTTERBECK   51.43    9.50   240      2 LAND
99808    76 E857  ---- NORTHEIM-STOECKHEIM   51.45    9.57   109        LAND
99809   176 E858  ---- NORTHEIM-IMBSHAUSEN   51.46   10.02   212        LAND
99810   206 E864  ---- SEESEN                51.54   10.11   186     -1 LAND
99811   227 E871  ---- LIEBENBURG-OTHFRESEN  52.01   10.24   187    -32 LAND
99812   176 E884  ---- LANGELSHEIM-ASTFELD   51.56   10.21   210        LAND
99801   206 E897  ---- BAD HARZBURG          51.54   10.34   201    -41 LAND
99802   176 E902  ---- BODENFELDE-AMELITH    51.42    9.31   258        LAND
99803   227 E944  ---- HERZBERG              51.38   10.22   238     18 LAND
99804   176 E950  ---- HERZBERG-LONAU        51.41   10.22   340        LAND
99805   176 E955  ---- LAUTERBERG,BAD-BARTO  51.36   10.28   305        LAND
99806   176 E970  ---- DRANSFELD-OSSENFELD   51.32    9.48   317        LAND
99807   176 F020  ---- MEYENBURG             53.19   12.17    98        LAND
99808   176 F050  ---- UCKERLAND-KARLSTEIN   53.26   13.49    40        LAND
99809   176 F069  ---- HOHENREINKENDORF      53.14   14.20    46        LAND
99810   227 F105  ---- LENZEN/ELBE           53.06   11.29    20      1 LAND
99811   176 F108  ---- KARSTAEDT/PRIGNITZ    53.10   11.45    32        LAND
99812   176 F125  ---- KUHBIER               53.09   12.05    63        LAND
99801   206 F143  ---- WITTSTOCK-ROTE M�HLE  53.11   12.29    66     11 LAND
99802   206 F151  ---- MENZ                  53.06   13.02    77    -12 LAND
99803   176 F172  ---- MITTENWALDE/UCKERMAR  53.11   13.39    72        LAND
99804   176 F178  ---- NEURUPPIN-GUEHLEN GL  53.03   12.46    89        LAND
99805   176 F191  ---- PASSOW                53.08   14.07    12        LAND
99806   176 F199  ---- BERKHOLZ-MEYENBURG    53.02   14.14    14        LAND
99807   176 F210  ---- PERLEBERG             53.06   11.52    40        LAND
99808   227 F263  ---- ZEHDENICK             52.58   13.20    51     -1 LAND
99809   176 F280  ---- FRIEDRICHSWALDE       53.01   13.43    75        LAND
99810   176 F305  ---- KLESSEN               52.44   12.30    38        LAND
99811   176 F325  ---- KREMMEN-GROSS ZIETHE  52.44   13.01    46        LAND
99812   176 F338  ---- MARWITZ (WASSERWERK)  52.40   13.11    33        LAND
99801   303 F361  ---- HECKELBERG            52.45   13.50    82    -29 LAND
99802   176 F385  ---- WUSTROW               52.46   14.13     6        LAND
99803   227 F419  ---- WUSTERWITZ            52.22   12.23    36     14 LAND
99804   303 F431  ---- BERGE                 52.37   12.47    40     -3 LAND
99805   176 F448  ---- STAAKEN               52.32   13.07    31        LAND
99806   176 F451  ---- AHRENSFELDE           52.35   13.34    60        LAND
99807   176 F470  ---- STRAUSBERG            52.35   13.56    81        LAND
99808   303 F475  ---- MUENCHEBERG           52.31   14.07    63      3 LAND
99809    76 F518  ---- BRANDENBURG/HAVEL     52.25   12.34    31        LAND
99810   176 F520  ---- GROSS KREUTZ          52.24   12.47    31        LAND
99811   176 F545  ---- THYROW                52.15   13.14    43        LAND
99812   176 F598  ---- POHLITZ               52.11   14.34    70        LAND
99801   176 F620  ---- BRUECK-GOEMNIGK       52.10   12.44    52        LAND
99802   176 F635  ---- FELGENTREU            52.06   13.00    48        LAND
99803   176 F660  ---- MUENCHEHOFE           52.09   13.50    44        LAND
99804   176 F681  ---- NEU MADLITZ           52.22   14.15    46        LAND
99805   206 F695  ---- COSCHEN               52.01   14.44    40     15 LAND
99806   282 F707  ---- LANGENLIPSDORF        51.55   13.05    91     -1 LAND
99807   176 F736  ---- HOHENBUCKO            51.46   13.28   131        LAND
99808   227 F742  ---- LUEBBEN-BLUMENFELDE   51.56   13.53    57     -2 LAND
99809   176 F757  ---- BISCHDORF, KREIS OBE  51.48   13.58    78        LAND
99810   176 F770  ---- LIEBEROSE             51.59   14.18    47        LAND
99811   176 F878  ---- GRAUSTEIN             51.34   14.29   139        LAND
99812   176 F925  ---- ELSTERWERDA           51.27   13.31    90        LAND
99801   227 F951  ---- KLETTWITZ             51.34   13.53   128    -25 LAND
99802   206 G002  ---- BERLIN-BUCH           52.38   13.30    60      8 LAND
99803   206 G005  ---- BERLIN-MARZAHN        52.32   13.34    60     -8 LAND
99804   227 G006  ---- BERLIN-KANISWALL      52.24   13.44    33      5 LAND
99805   176 H009  ---- WESTERKAPPELN         52.17    7.52    92        LAND
99806   227 H012  ---- RAHDEN-VARL           52.27    8.35    41      2 LAND
99807   176 H027  ---- PETERSHAGEN           52.23    9.01    43        LAND
99808   176 H058  ---- STEINFURT-BURGSTEINF  52.08    7.19    70    -14 LAND
99809   176 H061  ---- HOERSTEL              52.15    7.38    46        LAND
99810   176 H081  ---- ESPELKAMP-ISENSTEDT   52.21    8.39    65        LAND
99811   176 H119  ---- COESFELD              51.58    7.10    87        LAND
99812   176 H142  ---- LIENEN-KATTENVENNE    52.07    7.52    55        LAND
99801   176 H145  ---- OSTBEVERN-SCHIRLHEID  52.01    7.51    55        LAND
99802   176 H170  ---- ENGER                 52.09    8.31   128        LAND
99803   227 H174  ---- BIELEFELD-DEPPENDORF  52.04    8.28   105      7 LAND
99804   206 H203  ---- KLEVE                 51.46    6.06    46    -25 LAND
99805   176 H212  ---- DAHLEM-SCHMIDTHEIM    50.25    6.34   573        LAND
99806   176 H235  ---- REKEN-GROSS REKEN     51.49    7.05    59        LAND
99807   227 H247  ---- LUEDINGHAUSEN-BROCH.  51.46    7.31    59     10 LAND
99808   176 H257  ---- DRENSTEINFURT         51.46    7.45    72        LAND
99809   176 H261  ---- HARSEWINKEL           51.59    8.13    63        LAND
99810    76 H265  ---- GUETERSLOH/EMS        51.56    8.19    70        LAND
99811   176 H281  ---- LAGE, KREIS LIPPE-HO  51.56    8.46   154        LAND
99812   176 H311  ---- XANTEN                51.42    6.24    20        LAND
99801    76 H330  ---- HALTERN (WASSERWERK)  51.44    7.12    41        LAND
99802   176 H333  ---- OLFEN                 51.43    7.22    49        LAND
99803   227 H361  ---- BECKUM-UNTERBERG      51.43    8.03   120    -27 LAND
99804   176 H372  ---- DELBRUECK             51.47    8.34    88        LAND
99805   176 H376  ---- SALZKOTTEN            51.43    8.35    93        LAND
99806   227 H377  ---- LIPPSTADT-BOEKENFOER  51.38    8.23    92     -4 LAND
99807   176 H391  ---- BRAKEL                51.43    9.10   145        LAND
99808   227 H401  ---- GELDERN-WALBECK       51.30    6.14    40    -10 LAND
99809   206 H411  ---- BORKEN/WESTFALEN      51.52    6.53    48     17 LAND
99810   206 H419  ---- DUISBURG-BAERL        51.31    6.42    25      0 LAND
99811   176 H420  ---- DINSLAKEN             51.35    6.47    53        LAND
99812   227 H432  ---- BOCHUM                51.29    7.16   101      7 LAND
99801   206 H443  ---- WALTROP-ABDINGHOF     51.36    7.24    68      6 LAND
99802   176 H450  ---- FROENDENBERG-HOHENHE  51.29    7.47   240        LAND
99803   176 H460  ---- SASSENDORF, BAD-BEUS  51.32    8.11   171        LAND
99804   176 H475  ---- RUETHEN               51.30    8.26   361        LAND
99805   176 H477  ---- WUENNENBERG-EILERN    51.32    8.47   312        LAND
99806   176 H492  ---- BORGENTREICH          51.34    9.14   206        LAND
99807   176 H512  ---- NETTETAL-HUELST       51.18    6.12    45        LAND
99808   206 H522  ---- TOENISVORST           51.17    6.26    37     -1 LAND
99809   206 H542  ---- GEVELSBERG-OBERB.     51.20    7.20   205    -27 LAND
99810   176 H543  ---- BRECKERFELD-WENGEBER  51.15    7.28   440        LAND
99811   206 H547  ---- BUCHENHOFEN           51.13    7.07   130     -9 LAND
99812   176 H568  ---- NEUENRADE-BLINTROP    51.17    7.51   296        LAND
99801   227 H572  ---- ARNSBERG-NEHEIM       51.28    7.59   159    -10 LAND
99802    76 H573  ---- ARNSBERG-MUESCHEDE    51.25    8.01   278        LAND
99803   206 H579  ---- ESLOHE                51.16    8.10   325    -30 LAND
99804   176 H581  ---- WARSTEIN-HIRSCHBERG   51.26    8.16   331        LAND
99805   227 H591  ---- BRILON-TH�LEN         51.25    8.39   457      5 LAND
99806   206 H606  ---- HEINSBERG-SCHLEIDEN   51.02    6.06    57     14 LAND
99807   227 H612  ---- REICHSHOF-ECKENHAGEN  50.59    7.41   348     19 LAND
99808   176 H635  ---- DORMAGEN-ZONS         51.07    6.51    36        LAND
99809   176 H641  ---- SOLINGEN-HOHENSCHEID  51.08    7.05   154        LAND
99810   206 H642  ---- REMSCHEID-LENNEP      51.11    7.15   345     16 LAND
99811   176 H655  ---- WIPPERFUERTH-GARDEWE  51.10    7.25   360        LAND
99812   206 H658  ---- MEINERZHAGEN-REDLEND  51.05    7.38   380     37 LAND
99801   176 H669  ---- ATTENDORN-NEULISTERN  51.07    7.53   311        LAND
99802   227 H678  ---- LENNESTADT-THETEN     51.08    8.02   286     35 LAND
99803   176 H681  ---- SCHMALLENBERG-SELLIN  51.13    8.16   443        LAND
99804   176 H695  ---- MEDEBACH-BERGE        51.10    8.43   380        LAND
99805   176 H718  ---- JUELICH (KLAERANLAGE  50.56    6.20    76        LAND
99806   176 H721  ---- BEDBURG-WEILER HOHEN  51.01    6.31   101        LAND
99807   206 H744  ---- KOELN-STAMMHEIM       50.59    6.59    43      5 LAND
99808   176 H755  ---- OVERATH-BOEKE         50.58    7.17   221        LAND
99809   273 H768  ---- MOENCHENGLADBACH-HIL  51.08    6.22    77      5 LAND
99810   176 H777  ---- WENDEN-DOERNSCHEID    50.56    7.51   418        LAND
99811   176 H791  ---- BERLEBURG, BAD-ARFEL  51.01    8.26   436        LAND
99812   206 H795  ---- BAD BERLEBURG-ST�NZE  50.59    8.22   610   -107 LAND
99801   206 H827  ---- NIDEGGEN-SCHMIDT      50.40    6.25   370     -5 LAND
99802   227 H862  ---- NEUNKIRCHEN-SEELSCHE  50.50    7.22   195    -24 LAND
99803   206 H883  ---- SIEGEN (KL�RANLAGE)   50.51    8.00   263     65 LAND
99804    97 H884  ---- BIRKELBACH            51.01    8.16   541        LAND
99805   176 H889  ---- BURBACH-WUERGENDORF   50.46    8.08   413        LAND
99806   176 H908  ---- MONSCHAU-KALTERHERBE  50.31    6.13   535        LAND
99807   227 H932  ---- WEILERSWIST-LOMMERSU  50.43    6.47   146    -31 LAND
99808   303 H981  ---- KALL-SISTIG           50.30    6.32   505     -8 LAND
99809   227 J702  ---- PERL-NENNIG           49.32    6.23   152     39 LAND
99810   176 J709  ---- MERZIG                49.28    6.38   171        LAND
99811   227 J728  ---- WEISKIRCHEN/SAAR      49.33    6.49   380     -6 LAND
99812   176 J731  ---- NOHFELDEN-GONNESWEIL  49.34    7.04   403        LAND
99801   176 J812  ---- SCHMELZ-HUETTERSDORF  49.25    6.50   223        LAND
99802   206 J815  ---- NEUNKIRCHEN-WELLESW.  49.20    7.14   236     63 LAND
99803   176 J846  ---- HOMBURG/SAAR          49.20    7.22   235        LAND
99804   206 J908  ---- SAARBRUECKEN-BURBACH  49.14    6.56   190     87 LAND
99805   206 K017  ---- HILGENROTH            50.44    7.39   295      6 LAND
99806   176 K026  ---- WALLMENROTH           50.47    7.50   172        LAND
99807   227 K038  ---- BAD NEUENAHR-AHRWEIL  50.32    7.05   111     59 LAND
99808   206 K057  ---- HUEMMERICH            50.34    7.29   328    -70 LAND
99809   176 K081  ---- HACHENBURG/WESTERWAL  50.40    7.48   322        LAND
99810   176 K132  ---- SINZIG                50.33    7.16    60        LAND
99811   176 K170  ---- HOEHR-GRENZHAUSEN     50.26    7.40   241        LAND
99812   176 K172  ---- SELTERS, WESTERWALDK  50.31    7.44   239        LAND
99801   176 K191  ---- WESTERBURG/RHLPF.     50.33    7.58   355     31 LAND
99802   206 K210  ---- SCHNEIFELFORSTHAUS    50.17    6.25   657    -84 LAND
99803    76 K212  ---- ROTH BEI PRUEM        50.18    6.23   593        LAND
99804   176 K219  ---- LISSENDORF            50.19    6.37   407        LAND
99805   176 K230  ---- RODDER                50.24    6.52   512        LAND
99806   176 K240  ---- KALTENBORN, HOHE ACH  50.23    6.59   570        LAND
99807   176 K259  ---- POLCH, KR. MAYEN-KOB  50.18    7.19   235        LAND
99808   176 K272  ---- NASSAU (KLAERANLAGE)  50.19    7.47    80        LAND
99809   206 K282  ---- MONTABAUR             50.26    7.49   253     26 LAND
99810   176 K290  ---- EPPENROD/BORNBACH     50.25    7.56   300        LAND
99811   176 K295  ---- HOLZHEIM BEI DIEZ     50.22    8.03   155        LAND
99812   176 K300  ---- WINTERSPELT           50.14    6.13   426        LAND
99801   176 K308  ---- LAUPERATH-SCHEIDCHEN  50.05    6.19   517        LAND
99802   176 K310  ---- PRUEM-WATZERATH       50.11    6.22   386        LAND
99803   176 K317  ---- WEISSENSEIFEN         50.09    6.33   530        LAND
99804   176 K318  ---- DENSBORN              50.08    6.36   308        LAND
99805   176 K322  ---- KIRCHWEILER           50.14    6.45   570        LAND
99806   176 K326  ---- OBERSTADTFELD         50.10    6.46   421        LAND
99807   176 K339  ---- STROHN                50.07    6.55   390        LAND
99808   176 K354  ---- KAIL                  50.11    7.14   290        LAND
99809   176 K380  ---- OBERBACHHEIM          50.15    7.44   328        LAND
99810   176 K381  ---- SINGHOFEN (KLAERANLA  50.16    7.49   220        LAND
99811   206 K386  ---- NAST�TTEN             50.12    7.52   268     35 LAND
99812   206 K419  ---- OLSDORF               49.56    6.23   305     -1 LAND
99801   176 K428  ---- BITBURG               49.59    6.32   359        LAND
99802   176 K431  ---- MEISBURG              50.06    6.40   523        LAND
99803   227 K440  ---- MANDERSCHEID          50.06    6.48   413     21 LAND
99804   176 K446  ---- WITTLICH              49.58    6.56   147        LAND
99805   227 K463  ---- BLANKENRATH           50.02    7.18   417      9 LAND
99806   176 K475  ---- LINGERHAHN (WWV RLP)  50.05    7.34   482        LAND
99807   176 K501  ---- KIRCHBERG, RHEIN-HUN  49.56    7.23   393        LAND
99808   176 K509  ---- NEWEL                 49.49    6.35   365        LAND
99809   176 K511  ---- SPEICHER              49.56    6.38   325        LAND
99810   176 K515  ---- ZEMMER (FORSTHAUS MU  49.52    6.43   293        LAND
99811   176 K517  ---- BEUREN (HOCHWALD)     49.44    6.55   505        LAND
99812   176 K533  ---- KLEINICH, KR. BERNKA  49.53    7.11   438        LAND
99801   176 K539  ---- BRUCHWEILER, KR. BIR  49.48    7.14   545        LAND
99802   176 K557  ---- SEESBACH, KR. BAD KR  49.51    7.32   394        LAND
99803   227 K568  ---- BAD KREUZNACH         49.51    7.51   100     85 LAND
99804   206 K584  ---- MAINZ (ZDF)           49.58    8.13   195    -23 LAND
99805   176 K589  ---- HAHNHEIM              49.52    8.14   120        LAND
99806   206 K611  ---- TRIER-ZEWEN           49.44    6.37   132    141 LAND
99807   176 K612  ---- TRIER-IRSCH           49.44    6.42   228        LAND
99808   176 K633  ---- HUETTGESWASEN         49.44    7.08   650        LAND
99809   176 K650  ---- KIRN                  49.47    7.29   181        LAND
99810   176 K666  ---- BAYERFELD-STECKWEILE  49.42    7.50   310        LAND
99811   227 K685  ---- ALZEY                 49.44    8.07   215      4 LAND
99812   206 K699  ---- WORMS                 49.37    8.22    88      6 LAND
99801   176 K701  ---- KIRF-BEUREN           49.34    6.27   325        LAND
99802   176 K711  ---- OBERZERF              49.35    6.41   370        LAND
99803   176 K744  ---- KUSEL (KLAERANLAGE)   49.32    7.26   215        LAND
99804   176 K747  ---- HENSCHTAL             49.28    7.25   250        LAND
99805   176 K755  ---- EINOELLEN             49.37    7.38   303        LAND
99806    60 K761  ---- DOERRMOSCHEL-FELSBER  49.36    7.44   442        LAND
99807   206 K762  ---- RUPPERTSECKEN         49.39    7.53   461   -123 LAND
99808   176 K764  ---- HOMBERG-SCHOENBORNER  49.38    7.30   411        LAND
99809   176 K767  ---- ENKENBACH             49.32    7.53   300        LAND
99810   176 K784  ---- GRUENSTADT            49.34    8.11   160        LAND
99811   206 K863  ---- KAISERSLAUTERN        49.26    7.44   270     50 LAND
99812   176 K866  ---- TRIPPSTADT-NEUHOF     49.21    7.47   348        LAND
99801   206 K881  ---- BAD DUERKHEIM         49.28    8.11   107     29 LAND
99802   176 K918  ---- ZWEIBRUECKEN (KLAERA  49.15    7.20   225        LAND
99803   206 K925  ---- PIRMASENS             49.11    7.36   390    -43 LAND
99804   176 K969  ---- RUELZHEIM             49.10    8.18   105        LAND
99805   176 K984  ---- HIRSCHTHAL            49.03    7.46   205        LAND
99806   176 K986  ---- BUNDENTHAL            49.05    7.50   210        LAND
99807   227 K988  ---- BAD BERGZABERN        49.07    8.00   252    -38 LAND
99808   176 L021  ---- TRENDELBURG           51.35    9.26   133        LAND
99809   206 L031  ---- WAHLSBURG-LIPPOLDSB.  51.37    9.35   176     50 LAND
99810   176 L071  ---- LIEBENAU-HAUEDA       51.29    9.15   162        LAND
99811   176 L101  ---- WILLINGEN/HOCHSAUERL  51.17    8.35   588        LAND
99812   176 L113  ---- KORBACH-RHENA         51.17    8.47   458        LAND
99801   206 L121  ---- TWISTETAL-MUEHLHAUS.  51.20    8.55   295     50 LAND
99802   176 L125  ---- WALDECK-ALRAFT        51.14    8.58   300        LAND
99803   176 L130  ---- AROLSEN-LANDAU        51.20    9.05   265        LAND
99804    76 L131  ---- AROLSEN-VOLKHARDINGH  51.19    9.04   365        LAND
99805   176 L171  ---- WITZENHAUSEN-ZIEGENH  51.22    9.45   220        LAND
99806   176 L201  ---- BATTENBERG-HOF KARLS  51.04    8.32   590        LAND
99807    76 L215  ---- FRANKENBERG-GEISMAR   51.05    8.53   392        LAND
99808   206 L217  ---- BURGWALD-BOTTENDORF   51.02    8.49   293     -3 LAND
99809   176 L222  ---- VOEHL-BUCHENBERG      51.10    8.52   380        LAND
99810   176 L245  ---- WABERN-HEBEL          51.04    9.23   203        LAND
99811   176 L271  ---- HESSISCH LICHTENAU-F  51.13    9.41   340        LAND
99812   206 L286  ---- SONTRA                51.03    9.55   365    -62 LAND
99801   227 L291  ---- ESCHWEGE              51.11   10.04   170     91 LAND
99802    76 L292  ---- ESCHWEGE-ELTMANNSHAU  51.11    9.59   250        LAND
99803   176 L299  ---- HERLESHAUSEN-ARCHFEL  51.02   10.09   380        LAND
99804   176 L312  ---- WETTER/HESSEN-AMOENA  50.55    8.41   227        LAND
99805   206 L319  ---- COELBE                50.51    8.46   182     56 LAND
99806   206 L340  ---- GILSERBERG-MOISCHEID  50.58    9.03   340     -2 LAND
99807   206 L355  ---- NEUKIRCHEN-HAUPTSCHW  50.53    9.25   500    -95 LAND
99808   176 L409  ---- DRIEDORF              50.38    8.11   482        LAND
99809   227 L411  ---- DILLENBURG            50.44    8.16   314      5 LAND
99810   176 L442  ---- AMOENEBURG-RUEDIGHEI  50.47    8.57   210        LAND
99811    76 L463  ---- ALSFELD               50.46    9.16   305        LAND
99812   206 L464  ---- ALSFELD-EIFA          50.44    9.20   300     53 LAND
99801   176 L483  ---- HAUNETAL-WEHRDA       50.44    9.40   257        LAND
99802   176 L505  ---- WALDBRUNN-LAHR        50.31    8.08   280        LAND
99803   206 L511  ---- LOEHNBERG-OBERSH.     50.34    8.14   230     17 LAND
99804   176 L521  ---- ASSLAR KLEIN-ALTENST  50.35    8.28   200        LAND
99805   227 L555  ---- SCHOTTEN              50.29    9.07   265    -33 LAND
99806    76 L561  ---- LAUTERTAL-HOERGENAU   50.35    9.17   522        LAND
99807   176 L582  ---- PETERSBERG-MARBACH    50.37    9.43   305        LAND
99808   206 L592  ---- TANN/RHOEN            50.38   10.01   395     -6 LAND
99809   303 L602  ---- RUNKEL-ENNERICH       50.23    8.08   168     29 LAND
99810   176 L612  ---- WEILMUENSTER          50.26    8.23   183        LAND
99811   176 L617  ---- CAMBERG, BAD          50.17    8.17   244        LAND
99812   176 L631  ---- MUENZENBERG-GAMBACH   50.27    8.44   155        LAND
99801   206 L635  ---- BAD NAUHEIM           50.22    8.46   142     -1 LAND
99802   176 L652  ---- GEDERN-SCHOENHAUSEN   50.24    9.13   407        LAND
99803   206 L678  ---- SCHL�CHTERN-HEROLZ    50.20    9.33   230     66 LAND
99804   176 L685  ---- GREBENSTEIN           51.27    9.25   190        LAND
99805   176 L714  ---- HOHENSTEIN-BREITHARD  50.11    8.05   315        LAND
99806   206 L722  ---- WALDEMS-REINBORN      50.16    8.22   380     -2 LAND
99807   176 L732  ---- HOMBURG, BAD (FILTER  50.15    8.34   255        LAND
99808   176 L744  ---- VILBEL, BAD-DORTELWE  50.13    8.44   125        LAND
99809   176 L751  ---- NIDDERAU-ERBSTADT     50.16    8.52   162        LAND
99810   206 L771  ---- GRUENDAU-BREITENBORN  50.16    9.11   258      2 LAND
99811   176 L773  ---- WAECHTERSBACH         50.14    9.17   138        LAND
99812    97 L781  ---- SODEN,BAD-SALMUENSTE  50.16    9.22   145        LAND
99801   176 L803  ---- RUEDESHEIM-PRESBERG   50.03    7.53   403        LAND
99802   176 L819  ---- WIESBADEN-BIEBRICH    50.02    8.14    90        LAND
99803   206 L821  ---- WIESBADEN-AURINGEN    50.08    8.19   263    -54 LAND
99804   176 L829  ---- RAUNHEIM              50.01    8.26    89        LAND
99805   206 L841  ---- FRANKFURT WESTEND     50.08    8.40   124     12 LAND
99806   176 L850  ---- MUEHLHEIM/MAIN        50.08    8.49   102        LAND
99807   176 L865  ---- GROSS-GERAU-WALLERST  49.55    8.27    87        LAND
99808   206 L886  ---- DARMSTADT             49.53    8.41   162    -41 LAND
99809   176 L891  ---- ROEDERMARK-OBER-RODE  49.59    8.50   137        LAND
99810   176 L892  ---- REINHARDSHAGEN-VAAKE  51.29    9.37   115        LAND
99811   227 L894  ---- SCHAAFHEIM-SCHLIERB.  49.55    8.58   155     33 LAND
99812   176 L926  ---- LAUTERTAL/ODENWALD-R  49.43    8.41   208        LAND
99801   176 L930  ---- REINHEIM              49.49    8.49   165        LAND
99802   206 L947  ---- MICHELSTADT           49.41    9.01   204      9 LAND
99803   176 L979  ---- BIRKENAU              49.34    8.42   172        LAND
99804   206 L988  ---- BEERFELDEN            49.34    8.58   450    -43 LAND
99805   176 M031  ---- ELLRICH-WERNA         51.35   10.43   235        LAND
99806   176 M056  ---- REINHOLTERODE         51.25   10.11   336        LAND
99807   176 M146  ---- HELBEDUENDORF-KEULA   51.20   10.32   431        LAND
99808   206 M225  ---- M�HLHAUSEN-G�RMAR     51.13   10.29   190     28 LAND
99809   176 M259  ---- FREIENBESSINGEN       51.14   10.46   296        LAND
99810   176 M281  ---- ETZLEBEN              51.16   11.11   134        LAND
99811   206 M299  ---- OLBERSLEBEN           51.09   11.20   160      2 LAND
99812   176 M301  ---- SUEDEICHSFELD-WENDEH  51.10   10.15   290        LAND
99801   206 M348  ---- DACHWIG               51.04   10.52   173     -1 LAND
99802   176 M357  ---- ALPERSTEDT            51.06   11.03   158        LAND
99803   206 M405  ---- MOORGRUND-GRAEFENDOR  50.50   10.15   283      8 LAND
99804   176 M412  ---- HOERSELBERG-HAINICH-  51.01   10.31   290        LAND
99805   227 M448  ---- WEIMAR-SCHOENDORF     51.01   11.21   325    -46 LAND
99806   176 M473  ---- CROSSEN/ELSTER-NICKE  50.59   12.00   272        LAND
99807   176 M480  ---- MEUSELWITZ            51.03   12.18   173        LAND
99808   206 M488  ---- TEGKWITZ              50.59   12.20   193     27 LAND
99809   176 M500  ---- PONITZ                50.51   12.25   222        LAND
99810   206 M520  ---- WALTERSHAUSEN         50.54   10.33   353     21 LAND
99811   206 M552  ---- JENA (STERNWARTE)     50.56   11.35   155     43 LAND
99812   176 M557  ---- BUCHA                 50.52   11.30   310        LAND
99801   176 M565  ---- BOBECK                50.54   11.48   344        LAND
99802   206 M620  ---- KLEINER INSELBERG     50.51   10.29   732   -205 BERG
99803   176 M640  ---- DREI GLEICHEN-MUEHLB  50.52   10.49   286        LAND
99804   176 M651  ---- ILMTAL-DIENSTEDT      50.48   11.10   325        LAND
99805   176 M691  ---- HARTH-POELLNITZ NEUN  50.46   11.59   340        LAND
99806   176 M700  ---- GEISA                 50.43    9.57   280        LAND
99807   227 M732  ---- MARTINRODA            50.44   10.53   430     50 LAND
99808   206 M756  ---- SCHWARZBURG           50.38   11.11   277     90 LAND
99809   303 M765  ---- ROCKENDORF            50.41   11.31   280    -19 LAND
99810   206 M772  ---- SCHMIERITZ-WELTWITZ   50.44   11.50   340     43 LAND
99811   206 M799  ---- GOETTENDORF           50.40   12.05   390    -47 LAND
99812   206 M805  ---- BIRX                  50.32   10.03   745   -150 LAND
99801   176 M833  ---- FRAUENWALD            50.35   10.52   768        BERG
99802   176 M834  ---- SCHLEUSINGEN          50.31   10.46   399        LAND
99803   176 M846  ---- KATZHUETTE            50.33   11.02   450        LAND
99804   176 M909  ---- ROEMHILD-SUELZDORF    50.25   10.29   330        LAND
99805   206 M927  ---- VEILSDORF             50.25   10.49   397     45 LAND
99806   176 M938  ---- FRANKENBLICK-MENGERS  50.23   11.08   508        LAND
99807   176 M945  ---- JUDENBACH-NEUENBAU    50.26   11.14   738        LAND
99808   206 M965  ---- BAD LOBENSTEIN        50.27   11.38   500     39 LAND
99809   176 M978  ---- HIRSCHBERG            50.24   11.49   446        LAND
99810   176 M998  ---- NEUHAUS-SCHIERSCHNIT  50.20   11.14   383        LAND
99811   176 N104  ---- DIESDORF              52.45   10.53    65        LAND
99812   176 N135  ---- WINTERFELD-SALLENTHI  52.46   11.15    35        LAND
99801   176 N158  ---- BALLERSTEDT           52.44   11.43    35        LAND
99802   176 N182  ---- SCHWARZHOLZ           52.45   11.59    30        LAND
99803   176 N199  ---- SCHOLLENE             52.40   12.11    29        LAND
99804   176 N214  ---- KOECKTE               52.31   11.08    59        LAND
99805   176 N268  ---- GRIEBEN               52.25   11.58    38        LAND
99806   206 N272  ---- DEMKER                52.31   11.51    36      5 LAND
99807   176 N305  ---- BOESDORF              52.25   11.05    68        LAND
99808   176 N315  ---- BORN                  52.22   11.28    66        LAND
99809   176 N345  ---- ZIELITZ               52.18   11.40    52        LAND
99810   176 N366  ---- BURG-BLUMENTHAL       52.19   11.50    39        LAND
99811   206 N398  ---- DREWITZ BEI BURG      52.13   12.10    80     11 LAND
99812   176 N426  ---- WEISSENFELS-WENGELSD  51.16   12.03    92        LAND
99801   176 N435  ---- BOTTMERSDORF-KLEIN G  52.01   11.25    83        LAND
99802   176 N440  ---- SCHACKENSLEBEN        52.12   11.25    95        LAND
99803   176 N463  ---- KOENIGSBORN           52.08   11.47    52        LAND
99804   176 N500  ---- BUEHNE-RIMBECK        52.00   10.38   100        LAND
99805   176 N532  ---- HECKLINGEN-GROSS BOE  51.53   11.28   104        LAND
99806   176 N543  ---- WALTERNIENBURG-RONNE  51.58   11.55    52        LAND
99807   227 N548  ---- BERNBURG/SAALE        51.49   11.43    84    -17 LAND
99808   176 N553  ---- BADEWITZ BEI ZERBST   52.01   12.10    82        LAND
99809   176 N563  ---- DUEBEN                51.56   12.23    95        LAND
99810   206 N566  ---- JESSNITZ              51.41   12.18    74      5 LAND
99811   176 N587  ---- NAUNDORF BEI SEYDA    51.55   12.53   100        LAND
99812   206 N601  ---- SCHIERKE              51.46   10.39   609    -24 LAND
99801   303 N620  ---- QUEDLINBURG           51.48   11.08   142     -1 LAND
99802   206 N632  ---- MEHRINGEN/ASL         51.44   11.31   107     32 LAND
99803   206 N652  ---- KOETHEN (ANHALT)      51.45   12.01    76      5 LAND
99804   176 N671  ---- KEMBERG-RADIS         51.46   12.31    94        LAND
99805   176 N714  ---- SUEDHARZ-DIETERSDORF  51.32   11.03   440        LAND
99806   176 N731  ---- MANSFELD-ANNARODE     51.33   11.24   321        LAND
99807   282 N748  ---- QUERFURT-LODERSL.     51.23   11.32   204     -1 LAND
99808   176 N750  ---- SEEGEBIET MANSFELDER  51.32   11.41   154        LAND
99809   176 N815  ---- BIBRA, BAD-ALTENRODA  51.14   11.35   267        LAND
99810   176 N855  ---- FREYBURG/UNSTRUT-ZEU  51.14   11.50   140        LAND
99811   227 N924  ---- KREIPITZSCH           51.06   11.43   246    -26 LAND
99812   206 N977  ---- ZEITZ                 51.04   12.08   170      4 LAND
99801   227 O025  ---- BAD MUSKAU            51.34   14.42   125      4 LAND
99802   176 O039  ---- SCHOENWOELKAU-BRINNI  51.31   12.26   101        LAND
99803   206 O057  ---- KLITSCHEN BEI TORGAU  51.31   12.55    85     25 LAND
99804   176 O099  ---- HAEHNICHEN-TREBUS     51.20   14.50   163        LAND
99805   176 O141  ---- BELGERSHAIN           51.14   12.33   150        LAND
99806   176 O182  ---- BOXBERG               51.24   14.34   125        LAND
99807   176 O204  ---- MARKRANSTAEDT-GROSSL  51.19   12.10   118        LAND
99808   176 O248  ---- HEYDA BEI RIESA       51.16   13.22   132        LAND
99809   176 O251  ---- STRAUCH               51.22   13.35   128        LAND
99810   176 O268  ---- SCHOENTEICHEN-CUNNER  51.19   14.03   166        LAND
99811   176 O305  ---- PEGAU                 51.10   12.16   128        LAND
99812   176 O322  ---- GRIMMA-KLEINBOTHEN    51.11   12.46   134        LAND
99801   206 O348  ---- GARSEBACH BEI MEISSE  51.08   13.26   157     43 LAND
99802   206 O384  ---- KUBSCHUETZ,KR.BAUTZ.  51.10   14.30   232     -9 LAND
99803   206 O457  ---- DRESDEN-STREHLEN      51.01   13.46   119     80 LAND
99804   227 O458  ---- DRESDEN-HOSTERWITZ    51.01   13.51   114     85 LAND
99805   176 O461  ---- PULSNITZ              51.12   14.01   270        LAND
99806   206 O484  ---- SOHLAND/SPREE         51.04   14.26   290     -3 LAND
99807   176 O499  ---- OSTRITZ               51.02   14.56   213        LAND
99808   227 O510  ---- ALTGERINGSWALDE       51.05   12.56   296    -51 LAND
99809   303 O536  ---- NOSSEN                51.03   13.18   308    -59 LAND
99810   176 O543  ---- WILSDRUFF-MOHORN      51.01   13.28   288        LAND
99811   176 O566  ---- LOHMEN/SACHSEN        50.59   13.59   195        LAND
99812   176 O580  ---- DUERRHENNERSDORF      51.04   14.37   332        LAND
99801   303 O598  ---- BERTSDORF-HOERNITZ    50.54   14.45   270     52 LAND
99802   176 O625  ---- FRANKENBERG-ALTENHAI  50.53   13.02   326        LAND
99803   206 O660  ---- DIPPOLDISWALDE-REIN.  50.55   13.43   365     -2 LAND
99804   176 O708  ---- CRIMMITSCHAU-MANNICH  50.49   12.18   327        LAND
99805   176 O725  ---- SANKT EGIDIEN-KUHSCH  50.48   12.38   321        LAND
99806   176 O795  ---- ROSENTHAL-BIELATAL    50.50   14.04   460        LAND
99807   282 O805  ---- LICHTENTANNE          50.41   12.26   353      4 LAND
99808   206 O842  ---- DEUTSCHNEUDORF-BRUED  50.37   13.29   688    -19 LAND
99809   176 O846  ---- MARIENBERG-RUEBENAU   50.35   13.18   727        LAND
99810   206 O863  ---- AUE                   50.35   12.43   387    -34 LAND
99811   227 O868  ---- TREUEN                50.33   12.17   465    -45 LAND
99812   176 O877  ---- STUETZENGRUEN-HUNDSH  50.33   12.34   604        LAND
99801   176 O882  ---- TANNENBERG            50.37   12.56   532        LAND
99802   176 O888  ---- RASCHAU               50.31   12.50   507        LAND
99803   176 O950  ---- WEISCHLITZ-HEINERSGR  50.23   12.00   517        LAND
99804   176 O974  ---- KLINGENTHAL-KAMERUN   50.22   12.29   730        LAND
99805   206 O980  ---- ELSTER, BAD-SOHL      50.16   12.16   560     43 LAND
99806   176 O993  ---- ERLBACH-EUBABRUNN     50.18   12.23   565        LAND
99807   176 P004  ---- OBERLEICHTERSBACH-MO  50.16    9.46   470        LAND
99808   206 P013  ---- SANDBERG              50.21   10.00   510     15 LAND
99809   206 P022  ---- OSTHEIM V.D. RHOEN    50.27   10.13   312     39 LAND
99810   176 P025  ---- NEUSTADT, BAD         50.18   10.11   230        LAND
99811   176 P029  ---- MASSBACH              50.11   10.16   326        LAND
99812    76 P032  ---- AUBSTADT              50.20   10.27   304        LAND
99801   206 P033  ---- BAD KOENIGSHOFEN      50.17   10.27   288     37 LAND
99802   176 P038  ---- SULZDORF AN DER LEDE  50.14   10.34   332        LAND
99803   176 P041  ---- RODACH (KLAERANLAGE)  50.20   10.47   300        LAND
99804   176 P048  ---- PFARRWEISACH-LOHR (P  50.08   10.43   270        LAND
99805   176 P051  ---- MEEDER-OTTOWIND       50.22   10.53   450        LAND
99806   176 P052  ---- NEUSTADT BEI COBURG   50.19   11.07   330        LAND
99807   176 P058  ---- ITZGRUND-HERRETH      50.08   10.56   367        LAND
99808   176 P062  ---- LUDWIGSSTADT-LAUENST  50.31   11.22   520        LAND
99809   227 P066  ---- KRONACH               50.15   11.19   312      8 LAND
99810   176 P068  ---- BURGKUNSTADT          50.08   11.14   276        LAND
99811   206 P071  ---- TEUSCHNITZ            50.24   11.23   633    -16 LAND
99812   176 P073  ---- STEBEN, BAD           50.22   11.37   608        LAND
99801   176 P079  ---- LUDWIGSCHORGAST       50.07   11.34   336        LAND
99802   176 P086  ---- HELMBRECHTS           50.14   11.42   650        LAND
99803   176 P088  ---- STAMMBACH-QUERENBACH  50.09   11.44   598        LAND
99804   176 P095  ---- REHAU                 50.13   12.02   587        LAND
99805   206 P098  ---- SELB/OBERFRANKEN      50.12   12.08   609     18 LAND
99806    76 P099  ---- SELB-SPIELBERG        50.10   12.02   610        LAND
99807   206 P100  ---- KAHL (MAIN)           50.04    8.59   107     12 LAND
99808   176 P104  ---- HEINRICHSTHAL         50.04    9.21   450        LAND
99809   176 P106  ---- GROSSOSTHEIM          49.55    9.05   110        LAND
99810   206 P113  ---- LOHR/MAIN-HALSBACH    50.01    9.39   285      5 LAND
99811   176 P120  ---- GRAEFENDORF,KR.MAIN-  50.07    9.44   160        LAND
99812   176 P122  ---- HAMMELBURG            50.07    9.55   220        LAND
99801   206 P125  ---- ARNSTEIN-MUEDESHEIM   49.58    9.55   220     65 LAND
99802   227 P131  ---- SCHONUNGEN-MAINBERG   50.04   10.18   304     -2 LAND
99803   176 P137  ---- KOLITZHEIM            49.55   10.14   230        LAND
99804   176 P141  ---- KOENIGSBERG/BAYERN-H  50.05   10.29   259        LAND
99805   176 P147  ---- OBERAURACH-FATSCHENB  49.55   10.36   426        LAND
99806   206 P148  ---- EBRACH                49.51   10.30   346     -1 LAND
99807   176 P151  ---- RENTWEINSDORF-TREINF  50.04   10.49   258        LAND
99808   176 P158  ---- SCHESSLITZ-KOETTENSD  49.58   11.01   304        LAND
99809   176 P164  ---- THURNAU-TANNFELD      49.59   11.24   513        LAND
99810   176 P165  ---- STADELHOFEN           50.01   11.12   460        LAND
99811   176 P168  ---- AUFSESS-HOCHSTAHL     49.53   11.16   432        LAND
99812   176 P173  ---- PRESSECK              50.14   11.33   640        LAND
99801   227 P175  ---- HEINERSREUTH-VOLLHOF  49.58   11.31   350     52 LAND
99802   176 P179  ---- CREUSSEN-BUEHL        49.50   11.37   450        LAND
99803   282 P182  ---- FICHTELBERG/OBERFRA.  49.59   11.50   657     -4 LAND
99804   176 P185  ---- WALDERSHOF-SCHAFBRUC  49.56   12.05   723        LAND
99805   176 P188  ---- KEMNATH               49.52   11.53   460        LAND
99806   176 P189  ---- PRESSATH-MUEHLBERG    49.47   12.02   595        LAND
99807   176 P190  ---- HOHENBERG/EGER        50.05   12.13   517        LAND
99808   176 P197  ---- MAEHRING              49.55   12.32   676        LAND
99809   206 P198  ---- TIRSCHENREUTH-LODERM  49.52   12.21   500     27 LAND
99810   176 P208  ---- AMORBACH-NEUDORF      49.39    9.16   420        LAND
99811   176 P212  ---- HASLOCH/MAIN (SCHIRR  49.47    9.28   130        LAND
99812   176 P222  ---- ALTERTHEIM-OBERALTER  49.44    9.46   300        LAND
99801   176 P228  ---- BUETTHARD             49.37    9.53   263        LAND
99802   206 P232  ---- KITZINGEN             49.44   10.11   188     75 LAND
99803   176 P233  ---- SCHWARZACH/MAIN (KLA  49.48   10.13   188        LAND
99804   176 P236  ---- MARKT BIBART          49.40   10.23   317        LAND
99805   206 P238  ---- GOLLHOFEN             49.34   10.11   308    -10 LAND
99806   176 P243  ---- SCHLUESSELFELD (KLAE  49.44   10.38   290        LAND
99807   176 P249  ---- WILHELMSDORF/MITTELF  49.34   10.44   358        LAND
99808   176 P252  ---- ALTENDORF/OBERFRANKE  49.48   11.00   250        LAND
99809   227 P257  ---- MOEHRENDORF-KLSEE.    49.39   11.01   268     73 LAND
99810   176 P262  ---- GOESSWEINSTEIN        49.46   11.19   443        LAND
99811   206 P265  ---- GRAEFENBERG-KASBERG   49.40   11.13   506    -41 LAND
99812   176 P266  ---- LAUF/PEGNITZ (KLAERA  49.30   11.16   310        LAND
99801   176 P270  ---- PLECH                 49.39   11.28   443        LAND
99802   176 P271  ---- PEGNITZ (KLAERANLAGE  49.44   11.34   420        LAND
99803   227 P280  ---- NEUSTADT AM KULM      49.49   11.52   452     -3 LAND
99804   176 P287  ---- FREIHUNG-GROSSSCHOEN  49.34   11.53   493        LAND
99805   176 P292  ---- PLOESSBERG-LIEBENSTE  49.49   12.20   530        LAND
99806   176 P294  ---- FLOSSENBUERG          49.44   12.21   622        LAND
99807   176 P298  ---- WAIDHAUS-PFRENTSCH    49.37   12.29   499        LAND
99808   176 P299  ---- SCHOENSEE-DIETERSDOR  49.32   12.34   685        LAND
99809   176 P300  ---- SIMMERSHOFEN-ADELHOF  49.32   10.09   337        LAND
99810   176 P302  ---- BURGBERNHEIM          49.27   10.20   350        LAND
99811   206 P305  ---- ROTHENBURG OB DER TA  49.23   10.10   412      8 LAND
99812   176 P306  ---- COLMBERG-BINZWANGEN   49.23   10.22   434        LAND
99801   206 P308  ---- NEUBURG/KAMMEL-LANGE  48.19   10.23   495     24 LAND
99802   176 P310  ---- WINDSHEIM, BAD        49.31   10.25   310        LAND
99803   176 P317  ---- WEIHENZELL-GRUEB      49.20   10.37   474        LAND
99804   176 P318  ---- HERRIEDEN (KLAERANLA  49.14   10.30   420        LAND
99805   227 P319  ---- WEIDENBACH-WEIHERSCH  49.13   10.37   455     -8 LAND
99806   176 P321  ---- LANGENZENN            49.31   10.47   370        LAND
99807   176 P327  ---- ROHR/MITTELFRANKEN-D  49.19   10.55   402        LAND
99808   206 P333  ---- NUERNBERG-NETZSTALL   49.26   11.15   368    -17 LAND
99809   176 P337  ---- WENDELSTEIN-KLEINSCH  49.20   11.07   331        LAND
99810   227 P339  ---- FREYSTADT-OBERNDORF   49.11   11.22   436      2 LAND
99811   227 P343  ---- POMMELSBRUNN-MITTEL.  49.29   11.32   522      3 LAND
99812   176 P348  ---- NEUMARKT/OBERPFALZ    49.17   11.27   420        LAND
99801   176 P352  ---- EDELSFELD             49.35   11.42   535        LAND
99802   206 P354  ---- AMBERG-UNTERAMMERSR.  49.28   11.51   383     71 LAND
99803   206 P355  ---- ROELLBACH             49.46    9.15   239    -26 LAND
99804   176 P356  ---- KASTL, KREIS AMBERG-  49.22   11.41   424        LAND
99805   176 P359  ---- SCHMIDMUEHLEN         49.17   11.55   453        LAND
99806   176 P362  ---- NABBURG (FLUSSMEISTE  49.27   12.11   366        LAND
99807   176 P363  ---- SCHMIDGADEN           49.25   12.05   416        LAND
99808   227 P366  ---- SCHWANDORF            49.20   12.05   356     59 LAND
99809   176 P370  ---- TRAUSNITZ-REISACH     49.32   12.17   465        LAND
99810   206 P372  ---- OBERVIECHTACH         49.27   12.26   596    -27 LAND
99811   176 P374  ---- ALTENDORF             49.25   12.17   391        LAND
99812   176 P376  ---- NEUNBURG VORM WALD-E  49.22   12.27   420        LAND
99801   176 P379  ---- RODING-NEUBAEU        49.14   12.25   388        LAND
99802    76 P380  ---- RODING-WETTERFELD     49.13   12.32   373        LAND
99803   176 P382  ---- TREFFELSTEIN-WITZELS  49.24   12.37   470        LAND
99804   176 P389  ---- WEIDING, KREIS CHAM-  49.16   12.45   425        LAND
99805   176 P396  ---- NEUKIRCHEN BEI HEILI  49.16   12.58   460        LAND
99806   176 P405  ---- DINKELSBUEHL-OBERWIN  49.03   10.17   491        LAND
99807   176 P410  ---- BECHHOFEN/MITTELFRAN  49.10   10.35   425        LAND
99808   176 P411  ---- HAUNDORF-OBERERLBACH  49.11   10.49   449        LAND
99809   176 P417  ---- WASSERTRUEDINGEN (KL  49.02   10.36   420        LAND
99810   176 P418  ---- POLSINGEN-DOECKINGEN  48.56   10.46   510        LAND
99811   176 P420  ---- PLEINFELD-MANDLESMUE  49.07   10.58   380        LAND
99812   176 P422  ---- ROTHSEE BEI ALLERSBE  49.13   11.11   376        LAND
99801   176 P425  ---- THALMAESSING          49.05   11.13   417        LAND
99802   176 P433  ---- BERCHING              49.07   11.26   403        LAND
99803   227 P441  ---- PARSBERG/OBERPFALZ    49.09   11.41   549    -32 LAND
99804   176 P444  ---- BERATZHAUSEN          49.06   11.48   463        LAND
99805   176 P448  ---- RIEDENBURG            48.58   11.44   363        LAND
99806   176 P449  ---- KELHEIM (KANALSCHLEU  48.55   11.51   350        LAND
99807   176 P451  ---- TEUBLITZ (KLAERANLAG  49.13   12.05   350        LAND
99808   176 P453  ---- NITTENAU-HARTING      49.10   12.17   430        LAND
99809   176 P460  ---- HAGELSTADT            48.54   12.13   364        LAND
99810   206 P463  ---- SCHORNDORF-KNOEBLING  49.10   12.37   399     20 LAND
99811   176 P466  ---- STALLWANG             49.04   12.38   390        LAND
99812   176 P467  ---- WIESENFELDEN-UTZENZE  49.02   12.33   680        LAND
99801   176 P468  ---- AHOLFING              48.56   12.28   330        LAND
99802   206 P472  ---- PRACKENBACH           49.07   12.49   588     27 LAND
99803   176 P477  ---- SANKT ENGLMAR         49.00   12.49   810        BERG
99804   176 P481  ---- LAM-LAMBACH           49.13   13.04   692        LAND
99805   176 P485  ---- LINDBERG-BUCHENAU     49.02   13.20   740        LAND
99806   176 P486  ---- TEISNACH              49.02   12.59   400        LAND
99807   206 P501  ---- REIMLINGEN            48.50   10.31   435     54 LAND
99808   176 P505  ---- AURA IM SINNGRUND     50.11    9.34   287        LAND
99809   176 P517  ---- BISSINGEN (KLAERANLA  48.43   10.38   425        LAND
99810   176 P521  ---- TAGMERSHEIM-BLOSSENA  48.49   10.56   522        LAND
99811   206 P522  ---- EICHSTAETT-LANDERSH.  48.53   11.14   384      3 LAND
99812   227 P532  ---- KOESCHING             48.50   11.29   416     -5 LAND
99801   176 P535  ---- INGOLSTADT (FLUSSMEI  48.46   11.27   360        LAND
99802   227 P542  ---- MARKT ERLBACH-MOSBA.  49.32   10.38   362     -5 LAND
99803   176 P546  ---- SIEGENBURG (KLAERANL  48.46   11.50   380        LAND
99804   227 P548  ---- ELSENDORF-HORNECK     48.42   11.51   425      6 LAND
99805   176 P549  ---- GEISENFELD-EICHELBER  48.39   11.35   395        LAND
99806    76 P551  ---- LANGQUAID-OBERSCHNEI  48.52   12.02   378        LAND
99807   206 P555  ---- MALLERSDORF-PFB       48.47   12.11   404     17 LAND
99808   176 P557  ---- HOHENTHANN            48.40   12.05   470        LAND
99809   176 P568  ---- PILSTING-BAECKERMUEH  48.41   12.37   344        LAND
99810   176 P571  ---- BOGEN-PFELLING        48.53   12.45   345        LAND
99811   227 P572  ---- METTEN                48.51   12.55   313     13 LAND
99812   176 P576  ---- MOOS,KR. DEGGENDORF-  48.47   12.58   320        LAND
99801   176 P581  ---- KIRCHBERG/NIEDERBAYE  48.54   13.08   683        LAND
99802   176 P585  ---- OSTERHOFEN-THUNDORF   48.46   13.01   310        LAND
99803   227 P586  ---- SALDENBURG-ENTSCHENR  48.47   13.19   456     -6 LAND
99804   227 P594  ---- GRAINERT-REHBERG      48.47   13.38   628    -19 LAND
99805   176 P597  ---- BUECHLBERG-TANNOED    48.39   13.31   460        LAND
99806   176 P599  ---- SONNEN                48.41   13.44   847        BERG
99807   227 P602  ---- DILLINGEN-FRISTINGEN  48.34   10.34   419     10 LAND
99808   282 P606  ---- GUENZBURG             48.29   10.16   444     18 LAND
99809   176 P609  ---- ZUSMARSHAUSEN         48.25   10.35   443        LAND
99810   176 P611  ---- WERTINGEN             48.34   10.42   415        LAND
99811   176 P618  ---- DIEDORF/SCHWABEN-BIB  48.22   10.46   498        LAND
99812   176 P626  ---- DASING (KLAERANLAGE)  48.23   11.04   460        LAND
99801   176 P627  ---- SCHROBENHAUSEN        48.33   11.17   409        LAND
99802   206 P629  ---- ALTOMUENSTER-MAISBRU  48.25   11.19   510     -9 LAND
99803   176 P637  ---- SCHEYERN              48.30   11.27   481        LAND
99804   176 P639  ---- FAHRENZHAUSEN         48.22   11.34   458        LAND
99805   176 P642  ---- SCHWEITENKIRCHEN-SUE  48.31   11.39   499        LAND
99806   176 P645  ---- NANDLSTADT            48.31   11.50   475        LAND
99807   206 P655  ---- LANDSHUT-REITHOF      48.34   12.16   490    -60 LAND
99808   176 P656  ---- VILSHEIM-MUENCHSDORF  48.27   12.09   450        LAND
99809   176 P658  ---- STEINKIRCHEN-HOFSTAR  48.23   12.05   485        LAND
99810   176 P659  ---- OBERSCHLEISSHEIM      48.14   11.33   484        LAND
99811   176 P661  ---- LOICHING              48.37   12.25   416        LAND
99812   176 P663  ---- MAMMING-SCHNEIDERBER  48.37   12.37   447        LAND
99801   176 P664  ---- MARKLKOFEN (BETRIEBS  48.34   12.34   400        LAND
99802   176 P666  ---- VILSBIBURG            48.27   12.20   461        LAND
99803   176 P668  ---- GANGKOFEN (KLAERANLA  48.26   12.34   434        LAND
99804   176 P669  ---- NEUMARKT-SANKT VEIT   48.22   12.31   440        LAND
99805   176 P672  ---- EICHENDORF            48.38   12.51   350        LAND
99806   206 P674  ---- FALKENBERG,KR.ROTTAL  48.29   12.43   472    -21 LAND
99807   176 P677  ---- EGGENFELDEN           48.24   12.44   410        LAND
99808   176 P678  ---- WURMANNSQUICK-EGELSB  48.22   12.46   475        LAND
99809   227 P681  ---- ALDERSBACH-KRIESTORF  48.37   13.03   342     51 LAND
99810   176 P682  ---- EGING AM SEE-ROHRBAC  48.44   13.16   415        LAND
99811   176 P687  ---- PFARRKIRCHEN          48.26   12.59   378        LAND
99812    76 P688  ---- ROTTHALMUENSTER (LAN  48.22   13.11   387        LAND
99801   176 P689  ---- POCKING               48.24   13.19   323        LAND
99802   176 P697  ---- UNTERGRIESBACH-SCHAI  48.36   13.39   495        LAND
99803   176 P699  ---- UNTERGRIESBACH-GLOTZ  48.34   13.45   575        LAND
99804   176 P702  ---- WEISSENHORN-OBERREIC  48.19   10.12   500        LAND
99805   176 P718  ---- BREITENBRUNN-FUERBUC  48.08   10.22   610        LAND
99806   176 P724  ---- SCHWABMUENCHEN        48.12   10.44   538        LAND
99807   176 P732  ---- MERING (BAUHOF)       48.16   10.59   510        LAND
99808   206 P741  ---- MAISACH-GALGEN        48.13   11.12   530      2 LAND
99809   176 P760  ---- NASSENFELS            48.48   11.13   401        LAND
99810   176 P761  ---- ADELSDORF (KLAERANLA  49.43   10.55   260        LAND
99811   176 P764  ---- HAIMHAUSEN-OTTERSHAU  48.18   11.32   464        LAND
99812   176 P765  ---- ISEN-WESTACH          48.12   12.02   550        LAND
99801   206 P768  ---- EBERSBERG-HALBING     48.06   11.59   592     -2 LAND
99802   176 P769  ---- FINSING (KRAFTWERK)   48.13   11.48   498        LAND
99803   176 P771  ---- DORFEN (KLAERANLAGE)  48.16   12.10   430        LAND
99804   176 P777  ---- JETTENBACH            48.11   12.23   403        LAND
99805   176 P781  ---- AMPFING (KLAERANLAGE  48.16   12.26   400        LAND
99806   176 P785  ---- TUESSLING             48.13   12.38   417        LAND
99807   176 P788  ---- TACHERTING-SPREIT     48.05   12.31   508        LAND
99808   227 P794  ---- SIMBACH/INN           48.16   13.02   360     26 LAND
99809   303 P801  ---- MEMMINGEN             47.59   10.08   615    -28 LAND
99810   176 P803  ---- OTTOBEUREN            47.56   10.19   665        LAND
99811   227 P804  ---- ATTENKAM              47.53   11.22   672    -48 LAND
99812   176 P811  ---- OBERSTAUFEN-THALKIRC  47.34   10.05   748        LAND
99801   227 P817  ---- KAUFBEUREN            47.52   10.36   716    -16 LAND
99802   176 P818  ---- KRAFTISRIED           47.46   10.28   831        BERG
99803   176 P821  ---- BUCHLOE               48.02   10.44   626        LAND
99804   176 P824  ---- VILGERTSHOFEN-PFLUGD  47.58   10.55   685        LAND
99805   176 P825  ---- EBERFING              47.48   11.12   611        LAND
99806   176 P829  ---- STEINGADEN-LAUTERBAC  47.43   10.53   782        BERG
99807   206 P830  ---- OBERHACHING-LAUFZORN  48.01   11.33   604     -7 LAND
99808   238 P831  ---- WIELENBACH            47.53   11.10   550     13 LAND
99809   176 P833  ---- DIESSEN/AMMERSEE-DET  47.58   11.01   658        LAND
99810   176 P846  ---- SCHAEFTLARN-KLOSTER   47.59   11.28   557        LAND
99811   176 P850  ---- UTTING-ACHSELSCHWANG  48.02   11.03   591        LAND
99812   206 P856  ---- HOLZKIRCHEN           47.53   11.42   685    -33 LAND
99801   176 P860  ---- DEISENHOFEN, KREIS M  48.02   11.35   585        LAND
99802   176 P862  ---- FELDKIRCHEN-WESTERHA  47.56   11.54   517        LAND
99803   176 P870  ---- IRSCHENBERG-KASTHUB   47.49   11.52   715        LAND
99804    76 P873  ---- VOGTAREUTH (KLAERANL  47.57   12.10   464        LAND
99805   227 P874  ---- AMERANG-PFAFFING      48.01   12.17   515     14 LAND
99806   176 P875  ---- CHIEMSEE-HERRENCHIEM  47.52   12.23   536        LAND
99807   227 P877  ---- ROSENHEIM             47.53   12.08   444     42 LAND
99808   206 P881  ---- TROSTBERG             48.02   12.32   559     -9 LAND
99809   227 P887  ---- SIGMARSZELL-ZEISERTS  47.35    9.44   507     36 LAND
99810   176 P892  ---- WAGING AM SEE         47.55   12.46   475        LAND
99811   176 P893  ---- TEISENDORF            47.51   12.50   496        LAND
99812    76 P894  ---- WAGING AM SEE-SCHNOE  47.58   12.46   470        LAND
99801    76 P903  ---- LINDAU (SWN)          47.32    9.41   397        LAND
99802   206 P904  ---- SIEGSDORF-HOELL       47.50   12.39   721     12 LAND
99803   176 P905  ---- WEILER-SIMMERBERG (K  47.34    9.54   600        LAND
99804   176 P908  ---- OBERREUTE             47.33    9.56   903        BERG
99805   176 P914  ---- IMMENSTADT-REUTE      47.37   10.12   960        BERG
99806   176 P915  ---- OBERSTDORF-ROHRMOOS   47.25   10.10  1067        BERG
99807   176 P916  ---- BALDERSCHWANG         47.28   10.06  1037        BERG
99808   176 P917  ---- SONTHOFEN (FLUSSMEIS  47.31   10.16   730        LAND
99809   176 P919  ---- MINDELHEIM            48.04   10.29   590        LAND
99810   176 P923  ---- MARKTOBERDORF-SULZSC  47.43   10.38   790        BERG
99811   206 P924  ---- OY-MITTELBERG-PETERS  47.38   10.23   872     64 LAND
99812   176 P927  ---- HINDELANG-UNTERJOCH   47.34   10.26  1015        BERG
99801   176 P929  ---- SCHWANGAU-HORN (LFW)  47.35   10.43   796        BERG
99802   176 P931  ---- BERNBEUREN-PRACHTSRI  47.44   10.44   936        BERG
99803   176 P934  ---- HALBLECH-TRAUCHGAU    47.39   10.49   780        BERG
99804   176 P936  ---- SEEG (KLAERANLAGE)    47.40   10.38   802        BERG
99805   176 P937  ---- ETTAL-LINDERHOF       47.34   10.58   940        BERG
99806   227 P942  ---- BAD KOHLGRUB          47.40   11.05   750     85 LAND
99807   176 P944  ---- OBERAMMERGAU          47.36   11.04   835        BERG
99808   176 P945  ---- SCHLEHDORF            47.40   11.19   609        LAND
99809   176 P946  ---- MEHRING, KR. ALTOETT  48.11   12.49   411        LAND
99810   176 P947  ---- KOCHEL-EINSIEDL (KRA  47.34   11.18   805        BERG
99811   206 P948  ---- Mittenwald-B.wiesen   47.29   11.16   983    -13 LAND
99812    76 P949  ---- MITTENWALD/OBB.       47.26   11.16   923        BERG
99801   176 P950  ---- KRUEN                 47.30   11.17   873        BERG
99802   176 P956  ---- JACHENAU-TANNERN      47.38   11.31   720        LAND
99803   176 P957  ---- LENGGRIES (SYLVENSTE  47.35   11.33   737        LAND
99804   176 P958  ---- KREUTH-GLASHUETTE     47.37   11.39   897        BERG
99805   176 P960  ---- WAAKIRCHEN-DEMMELBER  47.46   11.41   815        BERG
99806   176 P962  ---- FEILNBACH, BAD        47.46   12.01   530        LAND
99807   176 P963  ---- ASSLING               47.59   11.59   500        LAND
99808   176 P965  ---- MIESBACH (KLAERANLAG  47.48   11.49   650        LAND
99809   176 P966  ---- OBERE FIRSTALM/SCHLI  47.40   11.51  1369        BERG
99810   176 P971  ---- BRANNENBURG-DEGERNDO  47.43   12.07   481        LAND
99811   176 P972  ---- TEISENDORF-BABING     47.50   12.49   590        LAND
99812   176 P973  ---- TEISENDORF-NEUKIRCHE  47.49   12.46   780        BERG
99801   176 P974  ---- ASCHAU-STEIN          47.44   12.18   680        LAND
99802   206 P975  ---- KIEFERSFELDEN         47.37   12.10   518    -32 LAND
99803   176 P979  ---- SAMERBERG-GEISENKAM   47.47   12.13   687        LAND
99804   176 P981  ---- UNTERWOESSEN-HINTERW  47.43   12.28   647        LAND
99805   206 P982  ---- REIT IM WINKEL 2      47.41   12.28   685     18 LAND
99806   176 P983  ---- RUHPOLDING (KLAERANL  47.46   12.38   650        LAND
99807   176 P986  ---- INZELL                47.46   12.45   690        LAND
99808   176 P987  ---- GRASSAU               47.47   12.29   540        LAND
99809   176 P988  ---- ALTUSRIED-MUTHMANNSH  47.47   10.06   730        LAND
99810   176 P989  ---- TITTMONING            48.04   12.46   382        LAND
99811   176 P990  ---- LAUFEN/OBB.-LEBENAU   47.57   12.54   430        LAND
99812   227 P991  ---- PIDING                47.46   12.55   458     11 LAND
99801   176 P994  ---- MARKTSCHELLENBERG     47.42   13.02   501        LAND
99802   176 P995  ---- RAMSAU-SCHWARZECK/SC  47.38   12.54  1088        BERG
99803   176 P996  ---- BERCHTESGADEN         47.38   13.01   600        LAND
99804   176 P997  ---- BERCHTESGADEN/JENNER  47.36   13.01   980        BERG
99805   176 Q027  ---- NECKARGEMUEND-KLEING  49.23    8.48   117        LAND
99806   176 Q033  ---- KOENIGHEIM            49.37    9.36   225        LAND
99807   176 Q047  ---- ELZTAL-RITTERSBACH    49.26    9.14   312        LAND
99808    76 Q053  ---- WALLDUERN             49.35    9.24   404        LAND
99809   227 Q055  ---- BUCHEN,KR.NECKAR-OD.  49.31    9.19   340     20 LAND
99810   176 Q056  ---- BETZWEILER-WAELDE     48.23    8.29   538        LAND
99811   176 Q059  ---- SECKACH               49.26    9.20   334        LAND
99812   176 Q060  ---- STOCKACH              47.52    9.01   532        LAND
99801   206 Q061  ---- NOTZINGEN             48.40    9.28   325      3 LAND
99802   206 Q062  ---- FREUDENBERG/MAIN-BOX  49.46    9.25   193     20 LAND
99803   176 Q066  ---- LAUDA-KOENIGSHOFEN-H  49.33    9.38   324        LAND
99804   176 Q067  ---- WIESENSTEIG           48.34    9.38   565        LAND
99805   206 Q076  ---- BAD MERGENTHEIM-NEUN  49.29    9.46   250     56 LAND
99806   176 Q077  ---- SAULGAU,BAD           48.02    9.29   576        LAND
99807   206 Q104  ---- WAGHAEUSEL-KIRRLACH   49.14    8.32   105     -4 LAND
99808   176 Q152  ---- MOECKMUEHL (LUBW)     49.19    9.22   170        LAND
99809   206 Q165  ---- INGELFINGEN-STACHEN.  49.20    9.42   385    -15 LAND
99810   176 Q171  ---- KUPFERZELL-RECHBACH   49.14    9.40   354        LAND
99811   176 Q218  ---- BRETTEN, KREIS KARLS  49.02    8.43   170        LAND
99812   227 Q221  ---- EPPINGEN-ELSENZ       49.10    8.51   220    -32 LAND
99801   176 Q222  ---- KOENIGSBACH-STEIN, E  48.58    8.35   160        LAND
99802   206 Q242  ---- OBERSULM-WILLSBACH    49.08    9.21   230    -14 LAND
99803   176 Q261  ---- WUESTENROT-OBERHEIMB  49.08    9.29   392        LAND
99804   206 Q292  ---- KIRCHBERG-JAGST       49.11    9.59   426      2 LAND
99805   176 Q293  ---- CRAILSHEIM (LUBW)     49.09   10.04   395        LAND
99806    76 Q295  ---- STIMPFACH-WEIPERTSHO  49.05   10.07   453        LAND
99807   176 Q318  ---- WILDBAD, BAD-CALMBAC  48.47    8.35   385        LAND
99808   176 Q327  ---- HERRENALB, BAD (LUBW  48.48    8.26   350        LAND
99809   282 Q332  ---- PFORZHEIM-ISPRINGEN   48.56    8.42   333      5 LAND
99810   176 Q333  ---- BRUCHSAL-HEIDELSHEIM  49.07    8.38   130        LAND
99811   176 Q334  ---- ABTSGMUEND-UNTERGROE  48.55    9.55   432        LAND
99812   176 Q340  ---- VAIHINGEN/ ENZ        48.55    8.57   200        LAND
99801   206 Q341  ---- SACHSENHEIM           48.57    9.04   250      9 LAND
99802   227 Q351  ---- GROSSENLACH MANNENW.  49.01    9.36   523    -75 LAND
99803   176 Q367  ---- WELZHEIM (LUBW)       48.52    9.38   470        LAND
99804    76 Q375  ---- WINTERBACH/REMSTAL    48.49    9.30   241        LAND
99805   206 Q378  ---- SCHWB.-GMND/WEILER    48.46    9.52   413      5 LAND
99806   227 Q382  ---- ELLWANGEN-RINDELBACH  48.59   10.08   460     16 LAND
99807   176 Q395  ---- LAUCHHEIM (BERGHOF)   48.53   10.14   503        LAND
99808   227 Q404  ---- RHEINAU-MEMPRECHTSH.  48.40    7.59   131     -2 LAND
99809   176 Q408  ---- KEHL-ODELSHOFEN       48.34    7.53   141        LAND
99810   176 Q409  ---- BAIERSBRONN-RUHESTEI  48.34    8.13   916        BERG
99811    76 Q410  ---- HORNISGRINDE          48.37    8.12  1119        BERG
99812   206 Q411  ---- BADEN-BADEN-GEROLDSA  48.44    8.15   240     18 LAND
99801   176 Q412  ---- IHRINGEN              48.02    7.38   193        LAND
99802   176 Q414  ---- FORBACH (LUBW)        48.40    8.21   304        LAND
99803   176 Q424  ---- ENZKLOESTERLE         48.40    8.28   600        LAND
99804   227 Q437  ---- NEUBULACH-OBERHAUGST  48.39    8.41   570    -37 LAND
99805   227 Q440  ---- RENNG. IHINGER-HOF    48.44    8.55   478    -44 LAND
99806   176 Q461  ---- BALTMANNSWEILER-HOHE  48.46    9.27   457        LAND
99807   176 Q481  ---- BLUMBERG-RANDEN       47.49    8.35   818        BERG
99808   227 Q485  ---- HERMARINGEN-ALLEWIND  48.37   10.16   468     -8 LAND
99809   176 Q491  ---- NATTHEIM-FLEINHEIM    48.43   10.18   530        LAND
99810   176 Q511  ---- DURBACH-EBERSWEIER    48.30    7.59   196        LAND
99811   206 Q518  ---- OHLSBACH              48.26    7.59   176    -14 LAND
99812   176 Q522  ---- BAIERSBRONN-MITTELTA  48.31    8.19   596        LAND
99801   176 Q529  ---- RIPPOLDSAU, BAD       48.25    8.20   493        LAND
99802   176 Q541  ---- NAGOLD                48.34    8.43   380        LAND
99803   176 Q554  ---- ROTTENBURG-KIEBINGEN  48.28    8.58   360        LAND
99804   227 Q561  ---- METZINGEN             48.32    9.16   362      7 LAND
99805   176 Q571  ---- URACH, BAD            48.30    9.24   471        LAND
99806   176 Q574  ---- WESTERHEIM            48.31    9.37   823        BERG
99807   206 Q579  ---- MERKLINGEN            48.31    9.46   685     51 LAND
99808   206 Q622  ---- WOLFACH               48.18    8.14   291     61 LAND
99809   176 Q625  ---- SCHILTACH (LUBW)      48.17    8.19   310        LAND
99810   176 Q637  ---- OBERNDORF/NECKAR      48.17    8.35   516        LAND
99811   176 Q642  ---- HAIGERLOCH-WEILDORF   48.22    8.46   524        LAND
99812   227 Q651  ---- HECHINGEN             48.23    8.59   522      8 LAND
99801   176 Q655  ---- BURLADINGEN-HAUSEN    48.18    9.04   682        LAND
99802   176 Q663  ---- HOHENSTEIN-BERNLOCH   48.22    9.20   740        LAND
99803   303 Q671  ---- M�NSINGEN-APFELSTETT  48.23    9.29   750    -13 LAND
99804   176 Q672  ---- BIRENBACH             48.44    9.39   348        LAND
99805   176 Q679  ---- EHINGEN-KIRCHEN       48.17    9.38   594        LAND
99806   206 Q702  ---- EMMENDINGEN-MUNDING.  48.08    7.50   203    -12 LAND
99807   176 Q703  ---- WEISWEIL-WALDECKHOF   48.11    7.42   173        LAND
99808   176 Q711  ---- WINDEN                48.08    8.01   303        LAND
99809   227 Q712  ---- ELZACH-FISNACHT       48.12    8.07   440     36 LAND
99810   176 Q713  ---- HERRENBERG            48.35    8.51   430        LAND
99811   176 Q715  ---- HASLACH IM KINZIGTAL  48.17    8.05   220        LAND
99812   176 Q716  ---- SIMONSWALD-OBERSIMON  48.05    8.05   419        LAND
99801   176 Q731  ---- ESCHBRONN-MARIAZELL   48.11    8.28   714        LAND
99802   227 Q733  ---- ROTTWEIL              48.11    8.38   588    -18 LAND
99803   206 Q738  ---- VILLINGEN-SCHWENNING  48.03    8.28   720     11 LAND
99804   176 Q739  ---- NEUHAUSEN OB ECK-UNT  47.57    8.59   663        LAND
99805   303 Q740  ---- BALINGEN-BRONNHPTN.   48.16    8.49   619     45 LAND
99806   227 Q751  ---- ALBSTADT-BADKAP       48.13    8.59   759    -43 LAND
99807   176 Q755  ---- SCHWENNINGEN, KREIS   48.06    9.00   835        BERG
99808   176 Q762  ---- LANGENENSLINGEN-ITTE  48.12    9.20   777        BERG
99809   176 Q763  ---- MENGEN-ENNETACH       48.04    9.19   567        LAND
99810   227 Q771  ---- RIEDLINGEN            48.09    9.28   533     31 LAND
99811   176 Q786  ---- BIBERACH AN DER RISS  48.06    9.49   604        LAND
99812   206 Q788  ---- SIGMARINGEN-LAIZ      48.04    9.11   580      9 LAND
99801   176 Q790  ---- DEGGENHAUSERTAL-AZEN  47.48    9.25   708        LAND
99802   227 Q811  ---- BUCHENBACH            47.58    8.00   445     99 LAND
99803   176 Q813  ---- BREITNAU              47.56    8.05  1001        BERG
99804   176 Q822  ---- EISENBACH             47.58    8.16   976        BERG
99805   227 Q823  ---- LENZKIRCH-RUHBUEHL    47.52    8.14   852      6 LAND
99806   206 Q848  ---- GEISINGEN             47.55    8.39   672     14 LAND
99807   206 Q864  ---- PFULLENDORF           47.56    9.17   630     40 LAND
99808    76 Q870  ---- DONAUESCHINGEN (LAND  47.58    8.31   680        LAND
99809   176 Q873  ---- ALTSHAUSEN            47.56    9.33   570        LAND
99810   303 Q879  ---- WEINGARTEN BEI RAVEN  47.49    9.37   440      2 LAND
99811    76 Q885  ---- WALDSEE, BAD-REUTE    47.55    9.43   576        LAND
99812   206 Q887  ---- MUELLHEIM             47.49    7.38   273    -20 LAND
99801   176 Q891  ---- ROT AN DER ROT-BUCH   47.58   10.01   690        LAND
99802   176 Q902  ---- MALSBURG-MARZELL      47.46    7.43   708        LAND
99803    76 Q903  ---- KANDERN-GUPF          47.42    7.35   362        LAND
99804   176 Q911  ---- TODTMOOS              47.44    8.00   781        BERG
99805    76 Q913  ---- DOGERN                47.36    8.10   309        LAND
99806   176 Q922  ---- UEHLINGEN-BIRKENDORF  47.45    8.19   760        BERG
99807    76 Q925  ---- WEILHEIM-BIERBRONNEN  47.41    8.12   771        BERG
99808   206 Q926  ---- WUTOESCHINGEN-OFTER.  47.41    8.23   398     55 LAND
99809   206 Q942  ---- SINGEN                47.46    8.49   445      5 LAND
99810    76 Q945  ---- GAILINGEN             47.42    8.44   450        LAND
99811   176 Q946  ---- GOTTMADINGEN          47.44    8.47   438        LAND
99812    76 Q951  ---- SIPPLINGEN (SWN)      47.49    9.06   705        LAND
99801    76 Q976  ---- FRIEDRICHSHAFEN       47.39    9.29   394        LAND
99802   227 Q978  ---- FRIEDRICHSHFN UNTER.  47.41    9.26   459     30 LAND
99803   176 Q999  ---- WANGEN/ALLGAEU-UNTER  47.43    9.52   666        LAND
99804   176 Z001  ---- GRAMAIS/OESTERREICH   47.16   10.32  1320        BERG
99805   176 Z002  ---- HINTERHORNBACH/OESTE  47.22   10.28  1100        BERG
99806   176 Z003  ---- UNTERGSCHWEND/OESTER  47.31   10.30  1040        BERG
99807   176 Z004  ---- ACHENKIRCH/OESTERREI  47.31   11.42   902        BERG
99803       01347 ENSG SOGNDAL               61.09    7.08   497    -20 LAND
99804       01368 ENFG FAGERNES              61.00    9.18   822    -21 LAND
99805       01475 ENSN SKIEN                 59.11    9.34    41     -4 LAND
99801       02378 ESNY SODERHAMN             61.16   17.06    26     -2 KUES
99802       02404 ESKV ARVIKA                59.40   12.35    77     30 LAND
99803       02435 ---- BORLANGE              60.26   15.30   145     -2 LAND
99804       02481 ---- SALA                  59.55   16.41    57     10 LAND
99805       02512 ESGP GOETEBORG             57.47   11.53    20     -9 KUES
99806       02527 ESGG GOTEBORG/LANDVETTER   57.40   12.30   164    -18 LAND
99807       02542 ---- HALLUM                58.19   13.02    70      7 LAND
99808       02566 ---- MALILLA               57.24   15.49    95     41 LAND
99809       02584 ---- GOTSKA SANDON         58.24   19.12    12    -12 MEER
99810       02586 ---- HARSTENA              58.15   17.01     5      2 KUES
99811       02595 ---- ROMA/GOTLAND          57.33   18.26    35     -2 LAND
99812       02603 ---- BROEN                 56.52   12.40    47     -8 KUES
99801       02604 ESMT HALMSTAD              56.41   12.50    31      5 KUES
99802       02620 ---- TORUP                 56.58   13.04    85     48 LAND
99803       02623 ---- HORBY                 55.52   13.40   114    -23 LAND
99804       02625 ---- SKILLINGE             55.29   14.19     4     34 KUES
99805       02641 ESMX VAXJO                 56.56   14.44   182      0 LAND
99806       02648 ---- VAEXJOE               56.51   14.50   199    -27 LAND
99807       02651 ESMK KRISTIANSTAD          55.55   14.05    23     14 LAND
99808       02680 ---- HOBURG                56.55   18.09    40    -39 KUES
99812       02952 EFPO PORI                  61.28   21.48    13     14 LAND
99801       02970 EFMA MARIEHAMN             60.07   19.54     5     -1 KUES
99802       02972 EFTU TURKU                 60.31   22.16    47    -17 LAND
99803       02975 EFHF HELSINKI              60.15   25.03    17     15 KUES
99804       03041 ---- AONACH MOR            56.49   -4.58  1130   -873 BERG
99805       03059 EGPE INVERNESS             57.32   -4.03     9     38 KUES
99806       03094 ---- ROSEHEARTY            57.42   -2.07     4     14 KUES
99807       03114 ---- OBAN                  56.25   -5.28     4    105 KUES
99808       03135 EGPK PRESTWICK             55.30   -4.36    20     31 KUES
99809       03140 EGPF GLASGOW               55.52   -4.26     8     70 LAND
99810       03154 ---- DUMFRIES              55.03   -3.39    16     14 LAND
99811       03160 EGPH EDINBURGH             55.57   -3.21    41     -9 LAND
99812       03235 ---- BOLTSHOPE PARK        54.49   -2.05   434     -4 LAND
99801       03245 EGNT NEWCASTLE/AIRPORT     55.02   -1.41    81    -21 LAND
99802       03246 ---- NEWCASTLE             55.02   -1.41    80    -20 LAND
99803       03261 ---- DISHFORTH AIRFIELD    54.08   -1.25    36     -1 LAND
99804       03262 ---- TYNEMOUTH             55.01   -1.25    30     30 KUES
99805       03334 EGCC MANCHESTER            53.21   -2.16    78     -6 LAND
99806       03347 EGRY LEEDS/MET             53.48   -1.33    47     43 LAND
99807       03453 EGXJ COTTESMORE            52.44   -0.39   138    -63 LAND
99808       03492 EGSH NORWICH-W.C.          52.38    1.18    14     -8 LAND
99809       03495 EGYC COLTISHALL            52.46    1.21    20    -14 LAND
99810       03496 ---- HEMSBY                52.41    1.41    13    -12 KUES
99811       03499 ---- SM.KNOLL              52.43    2.18     5     -5 MEER
99812       03534 EGBB BIRMINGHAM/AIRPORT    52.27   -1.45    93     25 LAND
99801       03683 EGSS STANSTED              51.53    0.14   106    -31 LAND
99802       03715 EGFF CARDIFF-WALES         51.24   -3.21    67    -48 KUES
99803       03726 EGRD BRISTOL/MET.          51.28   -2.36    11     60 LAND
99804       03776 EGKK LONDON/GATWICK        51.09   -0.11    62     30 LAND
99805       03779 EGRB LONDON WEATHER CENT.  51.31   -0.06    43    -11 LAND
99806       03817 EGDG ST. MAWGAN            50.26   -5.00   103    -22 LAND
99807       03839 ---- EXETER APT            50.44   -3.25    30     34 LAND
99808       03865 EGHI SOUTHAMPTON           50.54   -1.24     9      9 KUES
99809       03890 ---- OXFORD                51.45   -1.16    68      4 LAND
99810       03903 EGAB ST. ANGELO            54.24   -7.39    47    101 LAND
99811       03908 EGQB BALLYKELLY            55.04   -7.01     2     47 KUES
99812       03914 ---- PORTRUSH              55.12   -6.39     8     42 KUES
99801       03930 EGGP LIVERPOOL             53.20   -2.52    26    -20 KUES
99802       03957 ---- ROSSLARE              52.15   -6.20    23    -20 KUES
99803       03958 EGBE COVENTRY              52.22   -1.29    82      8 LAND
99804       03960 EIKL KILKENNY              52.40   -7.16    63     21 LAND
99809       06062 EKSV SKIVE                 56.33    9.10    23     -5 LAND
99810       06078 ---- ANHOLT                56.42   11.33     7     -6 KUES
99811       06080 EKEB ESBJERG               55.31    8.33    29    -16 KUES
99812       06141 ---- ABED                  54.50   11.20     8     -2 LAND
99801       06147 ---- VINDEBAEK KYST        54.53   12.11     3      4 KUES
99802       06160 EKVL VAERLOESE             55.46   12.20    18     10 LAND
99803       06174 ---- TESSEBOELLE           55.24   12.09    21      3 LAND
99804       06190 EKRN ROENNE/BORNH.         55.04   14.45    16     29 KUES
99805       06210 EHVB VALKENBURG            52.11    4.25     0     -1 KUES
99806       06250 EHTS TERSCHELLING          53.22    5.13    26    -25 KUES
99807       06629 ---- MUEHLEBERG / STOCKER  46.57    7.17   775     38 LAND
99808       06630 LSZB BERN                  46.55    7.30   510      6 LAND
99809       06710 LSGL LAUSANNE              46.33    6.37   616    -75 LAND
99810       06775 LSZA LUGANO                46.00    8.54   279     91 LAND
99811       06790 ---- ST.MORITZ             46.30    9.51  1850     87 LAND
99812       07017 LFQI CAMBRAI               50.13    3.09    77    -25 LAND
99801       07070 LFSR REIMS                 49.18    4.02    91     -2 LAND
99802       07090 LFSF METZ                  49.05    6.08   190     51 LAND
99803       07173 ---- EPINAL                48.12    6.26   317     50 LAND
99804       07197 LFSC COLMAR                47.55    7.24   211      2 LAND
99805       07265 LFLA AUXERRE               47.48    3.33   207    -42 LAND
99806       07593 ---- BRIANCON              44.55    6.39  1328    438 LAND
99807       07670 ---- PORQUEROLLES          43.00    6.14   143   -140 KUES
99808       07680 LFTU ST.RAPHAEL            43.25    6.45     2     45 KUES
99809       07695 ---- CAP FERRAT            43.41    7.20   138    -62 LAND
99810       08009 ---- RIBADEO               43.32   -7.01    25     41 KUES
99811       08013 ---- AVILES/DIV.PAST       43.33   -5.55    10     32 KUES
99812       08040 ---- FISTERRA              42.56   -9.17    98    -31 KUES
99801       08183 LELL SABADELL              41.31    2.07   148     23 LAND
99802       08227 LETO MADRID                40.29   -3.27   607     28 LAND
99803       08307 ---- POLLENSA              39.54    3.06     2     22 KUES
99804       08370 ---- JAVEA/YUNTAMIEN       38.47   -0.10    15    139 LAND
99805       08390 LEZL SEVILLA               37.22   -6.00     8      7 LAND
99806       08432 ---- AGUILAS               37.25   -1.35    33    114 KUES
99807       08485 ---- MOTRIL/CLUB NAUTICO   36.43   -3.32     3    281 KUES
99809       08536 LPPT LISSABON              38.47   -9.08   114     13 KUES
99810       08538 ---- SAGRES                37.00   -8.57    25     60 KUES
99811       08546 ---- PORTO/SERRA DO PILAR  41.08   -8.36    93    -37 KUES
99812       08547 ---- AVEIRO                40.39   -8.44     8      1 KUES
99801       10018 EDXW WESTERLAND            54.55    8.21    22    -21 KUES
99802       10026 ---- HUSUM                 54.31    9.09    28    -18 LAND
99803       10034 ETME EGGEBEK               54.38    9.21    20      0 LAND
99804       10063 ---- PUTTGARDEN            54.30   11.13     1      0 KUES
99805       10122 ETNJ JEVER                 53.32    7.53     7     -4 KUES
99806       10124 ---- LEUCHTTURM A. WESER   53.51    8.07    32    -32 MEER
99807       10125 EDWI WILHELMSHAVEN         53.30    8.03     5     -3 KUES
99808       10143 ---- NEUMUENSTER           54.05    9.56    20      6 LAND
99809       10177 ---- TETEROW               53.46   12.37    50     -5 LAND
99810       10181 EDCP PAROW                 54.22   13.05     4      0 KUES
99811       10203 ---- EMDEN                 53.21    7.12     5     -4 KUES
99812       10210 ---- FRIESOYTHE-ALTENOYTH  53.04    7.54     6     -1 LAND
99801       10215 EDWH OLDENBURG             53.11    8.10    11     -6 LAND
99802       10218 ETNA AHLHORN               52.53    8.14    49    -11 LAND
99803       10234 ETGQ ROTENBURG             53.08    9.21    34     -4 LAND
99804       10272 ETGW WITTSTOCK             53.11   12.31    72      5 LAND
99805       10273 EDCJ BASEPOHL              53.44   12.56    53    -14 LAND
99806       10277 ---- NEUGLOBSOW            53.09   13.02    62      4 LAND
99807       10280 ---- NEUBRANDENBURG        53.33   13.12    81    -33 LAND
99808       10306 ETHE RHEINE-BENTLAGE       52.18    7.23    40      0 LAND
99809       10314 ETNP HOPSTEN               52.20    7.33    39      1 LAND
99810       10317 ---- OSNABRUECK            52.15    8.03    95     -7 LAND
99811       10320 ETUO GUETERSLOH            51.55    8.18    72      6 LAND
99812       10324 ---- MINDEN                52.19    8.51    59      1 LAND
99801       10326 EDLI BIELEFELD             51.58    8.33   138      7 LAND
99802       10384 EDDI BERLIN-TEMPELHOF      52.28   13.24    50     -9 LAND
99803       10389 ---- BERLIN-ALEX.          52.31   13.25    37      4 LAND
99804       10401 ETUR BRUEGGEN              51.12    6.08    73    -23 LAND
99805       10403 EDLN MOENCHENGLADBACH      51.14    6.30    37      2 LAND
99806       10405 EDLV NIEDERRHEIN           51.36    6.09    32    -11 LAND
99807       10406 ---- BOCHOLT               51.50    6.32    21     13 LAND
99808       10416 EDLW DORTMUND              51.31    7.37   127    -46 LAND
99809       10426 EDLP PADERBORN             51.37    8.37   213    -45 LAND
99810       10432 ---- KOETERBERG            51.51    9.19   492   -282 LAND
99811       10438 ---- KASSEL                51.18    9.27   231    -20 LAND
99812       10441 ---- SCHAUENBURG-ELGERSH.  51.17    9.22   317     -6 LAND
99801       10457 ---- COCHSTEDT             51.51   11.25   162    -56 LAND
99802       10466 ---- HALLE                 51.31   11.57    96     13 LAND
99803       10487 ---- DRESDEN-STADT         51.03   13.44   113     61 LAND
99804       10492 ETHT COTTBUS/FLUGPLATZ     51.46   14.17    68     -3 LAND
99805       10493 JORG PRESCHEN              51.40   14.38   100     10 LAND
99806       10501 ---- AACHEN                50.47    6.06   202    -15 LAND
99807       10505 ---- AACHEN-ORSBACH        50.48    6.02   231    -44 LAND
99808       10510 ---- NUERBURG              50.20    6.57   627   -128 LAND
99809       10514 ETHM MENDIG                50.22    7.19   182    -45 LAND
99810       10515 ---- KOBLENZ-BEND.         50.25    7.35   127     10 LAND
99811       10516 ---- KO-FALKENST.KASERNE   50.22    7.35    84     53 LAND
99812       10517 ---- BONN-FRIESDORF        50.42    7.09    64     47 LAND
99801       10520 ---- ANDERNACH             50.26    7.26    75     62 LAND
99802       10521 ---- ROTHAARGEBIRGE        50.56    8.12   635    -88 LAND
99803       10535 ---- WAHLEN                50.49    9.08   349      4 LAND
99804       10536 EDEX FULDA                 50.33    9.39   305      5 LAND
99805       10546 ---- KALTENNORDHEIM        50.38   10.09   487      1 LAND
99806       10555 ---- WEIMAR                50.59   11.19   264     15 LAND
99807       10558 ---- SONNEBERG             50.23   11.11   626     36 LAND
99808       10575 ---- AUE                   50.36   12.43   391    -38 LAND
99809       10617 ETGX TRABEN-TRARBACH       49.58    7.07   257     -8 LAND
99810       10633 ETOU WIESBADEN             50.03    8.20   140      4 LAND
99811       10640 EDZW OFFENBACH             50.07    8.44    98     13 LAND
99812       10645 ---- BREITSOL              49.54    9.26   585   -224 LAND
99801       10677 EDQD BAYREUTH              49.59   11.38   488    -33 LAND
99802       10684 EDQM HOF/FLUGHAFEN         50.17   11.51   585    -31 LAND
99803       10714 EDRZ ZWEIBRUECKEN          49.13    7.24   345      2 LAND
99804       10722 EDSB KARLSR./BADEN-BADEN   48.47    8.05   124     -6 LAND
99805       10727 ---- KARLSRUHE             49.02    8.22   112     -4 LAND
99806       10735 ---- SINSHEIM              49.15    8.53   169     46 LAND
99807       10747 ---- KAISERSBACH-CRONHUET  48.55    9.41   489    -19 LAND
99808       10755 ETEB ANSBACH               49.19   10.38   467    -35 LAND
99809       10828 ---- SIGMARINGEN           48.06    9.15   645    -30 LAND
99810       10838 ---- ULM                   48.23    9.57   567    -40 LAND
99811       10840 ---- ULM-MAEHRINGEN        48.27    9.55   593     -9 LAND
99812       10858 ETSF FUERSTENFELDBRUCK     48.12   11.16   519    -11 LAND
99801       10893 ---- PASSAU                48.35   13.28   409    -28 LAND
99802       10929 EDTZ KONSTANZ              47.41    9.11   443      4 LAND
99803       10935 EDNY FRIEDRICHSHAFEN       47.40    9.31   416     26 LAND
99804       10947 ETSM MEMMINGEN             47.59   10.14   634      2 LAND
99805       10980 ---- WENDELSTEIN           47.42   12.01  1832   -720 BERG
99806       11015 ---- FREISTADT             48.30   14.30   548     10 LAND
99807       11028 ---- ST. POELTEN           48.12   15.37   282      1 LAND
99809       11128 ---- BRENNER               47.07   11.26  1450    -15 LAND
99810       11132 LOIJ ST.JOHANN/TIROL       47.31   12.27   670    231 LAND
99811       11134 ---- GERLOS                47.13   12.02  1250      9 LAND
99812       11143 LOWZ ZELL A.SEE FL.        47.18   12.47   753    364 LAND
99801       11145 ---- BAD GASTEIN           47.07   13.08  1100    125 LAND
99802       11154 ---- GMUNDEN               47.54   13.47   424     11 LAND
99803       11156 ---- BAD ISCHL             47.43   13.38   470    136 LAND
99804       11172 LOGM MARIAZELL             47.46   15.19   875     47 LAND
99805       11174 ---- ST.MICHAEL            47.20   15.00   580    219 LAND
99806       11176 LOGK KAPFENBERG            47.28   15.20   515    284 LAND
99807       11194 ---- NEUSIEDL AM SEE       47.57   16.51   135     -4 LAND
99808       11210 ---- MALLNITZ              46.59   13.11  1185     37 LAND
99809       11245 ---- GLEICHENBERG          46.52   15.54   303      6 LAND
99810       11248 ---- BAD RADKERSBURG       46.41   15.59   208      6 LAND
99811       11295 ---- LEIBNITZ              46.47   15.33   271     27 LAND
99812       11322 ---- MAYRHOFEN             47.10   11.51   647    461 LAND
99801       11354 ---- BAD GOISERN           47.38   13.37   502    306 LAND
99802       11448 ---- PILSEN                49.39   13.16   364     -4 LAND
99803       12150 EPGD DANZIG                54.23   18.28   135     10 KUES
99804       12555 EPKT KATOWICE/PYRZOWICE    50.29   19.05   303     18 LAND
99805       12825 LHPA PAPA                  47.12   17.30   145      4 LAND
99806       12839 LHBP BUDAPEST/FERIHEGY     47.26   19.16   151    -20 LAND
99807       12840 ---- BUDAPEST              47.31   19.02   118     38 LAND
99808       13455 ---- HERCEGNOVI            42.27   18.33    10    318 LAND
99809       13473 ---- PEC                   42.40   20.18   498      1 LAND
99810       13477 ---- PRIZREN               42.13   20.44   402    -15 LAND
99811       13481 LYPR PRISTINA              42.39   21.09   573     65 LAND
99812       13600 ---- SHKODRA               42.06   19.32    43     54 LAND
99801       13610 ---- KUKES                 42.02   20.25   354    197 LAND
99802       13611 ---- DURRES                41.18   19.27    15     25 LAND
99803       14301 ---- POREC                 45.14   13.36    15     47 KUES
99804       14442 ---- KNIN                  44.02   16.12   255      5 LAND
99805       14536 ---- PRIJEDOR              44.59   16.45   135      7 LAND
99806       14551 ---- DOBOJ                 44.44   18.06   146     39 LAND
99807       14653 LQSA SARAJEWO              43.49   18.20   510    116 LAND
99808       14655 ---- GACKO                 43.10   18.33   940     71 LAND
99809       14658 ---- SOKOLAC               43.57   18.49   872     80 LAND
99810       15481 LRCK KOGALNICEANU          44.20   28.26    97    -22 LAND
99811       15625 LBPD PLOVDIV               42.08   24.45   179      1 LAND
99812       16054 ---- AOSTA                 45.44    7.21   547    691 LAND
99801       16072 LIMO MONTE BISBINO         45.52    9.04  1319   -529 LAND
99802       16085 ---- PORTO TORRES          40.50    8.23     6     16 KUES
99803       16090 LIPX VERONA                45.23   10.52    67     20 LAND
99804       16094 LIPT VICENZA               45.34   11.31    39     26 LAND
99805       16117 ---- CUNEO LEVALDIGI       44.32    7.37   385     13 LAND
99806       16122 LIMG ALBENGA               44.03    8.07    45    310 LAND
99807       16130 ---- PARMA                 44.49   10.17    50     38 LAND
99808       16136 LIQD PASSO PORRETTA        44.01   11.00  1313   -225 LAND
99809       16146 LIVM PUNTA MARINA          44.27   12.18     2      0 KUES
99810       16147 LIPK FORLI                 44.12   12.04    27    -13 KUES
99811       16164 LIQV VOLTERRA              43.24   10.52   555   -219 LAND
99812       16181 LIRZ PERUGIA               43.05   12.30   208     11 LAND
99801       16191 LIPY FALCONARA             43.37   13.22    12     19 KUES
99802       16216 LIRV VITERBO               42.26   12.03   300     -6 LAND
99803       16226 ---- L'AQUILA              42.22   13.19   669    201 LAND
99804       16239 LIRA ROMA-CIAMPINO         41.47   12.35   130    -39 LAND
99805       16292 LIRI PONTECAGNANO          40.37   14.55    38     25 KUES
99806       16300 LIBZ POTENZA               40.38   15.48   843      2 LAND
99807       16350 LIBC CROTONE               39.00   17.04   155    -28 LAND
99808       16422 LICR REGGIO CALABRIA       38.04   15.39    11    160 KUES
99809       16538 LIEN FONNI                 40.07    9.15  1022     20 LAND
99810       16549 ---- CARLOFORTE / ISOLA    39.08    8.19    12      9 KUES
99811       16666 LGMK MYKONOS               37.26   25.21   123    -87 KUES
99812       16689 ---- PATRAS                38.15   21.44     1     98 KUES
99801       16699 LGTG ANAGRA                38.19   23.32   148    -51 LAND
99802       16740 LGSO SIROS                 37.25   24.57    72     92 KUES
99803       16744 LGSR SANTORINI             36.25   25.26    40    -20 KUES
99804       17117 LTBR BURSA/YENISEHIR       40.15   29.33   232     30 LAND
99805       17255 ---- KAHRAMANMARES         37.35   36.55   572     22 LAND
99806       17610 LCNC NICOSIA               35.09   33.17   224      2 LAND
99808       26058 ---- NARVA                 59.23   28.07    30     -6 LAND
99809       26231 ---- PARNU-SAUGA           58.25   24.28    12     -7 KUES
99810       26346 ---- ALUKSNE               57.26   27.02   197    -23 LAND
99811       26416 ---- SALDUS                56.41   22.30   112      4 LAND
99812       26424 ---- DOBELE                56.37   23.19    42     -9 LAND
99801       26429 ---- BAUSKA                56.25   24.11    30      0 LAND
99802       26502 EYPA PALANGA               55.58   21.06    10     15 KUES
99803       26529 EYPN PANEVEZYS             55.44   24.25    57     -1 LAND
99804       26603 ---- NIDA                  55.18   21.00     2      7 LAND
99805       26630 EYKA KAUNAS                54.58   24.05    78     -2 LAND
99806       26636 ---- SVECIONYS             55.08   26.10   222    -30 LAND
99807       26714 ---- MARIJAMPOLE           54.31   23.21    80     25 LAND
99808       26846 ---- STOLBTSY              53.28   26.44   172    -12 LAND
99809       26851 UMMS MINSK 2               53.52   27.32   231      2 LAND
99810       27613 UUEE MOSCOW/SHEREMETYEVO   55.58   37.25   191      2 LAND
99809       33347 UKBB KIEW/BORISPOL         50.20   30.58   121     -7 LAND
99810       33846 ---- NIKOLAYEV MATVEYEVKA  47.03   31.55    49    -36 LAND
99811       33983 ---- KERCH                 45.22   36.24    46     17 LAND
99812       33990 ---- JALTA                 44.30   34.10    14     73 KUES
99803       34712 ---- MARIUPOL WEST AIRP.   47.02   37.30    68     -7 LAND
99812       40007 OSAP ALEPPO                36.20   37.13   425     41 LAND
99802       40025 ---- LATAKIA               35.24   35.56    48    -25 LAND
99803       40030 ---- HAMA                  35.07   36.45   301     10 LAND
99807       40155 LLHA HAIFA                 32.48   35.02     8     41 KUES
99808       40184 LLJR JERUSALEM             31.47   35.13   757    -39 LAND
99810       40253 ---- BAQURA                32.38   35.37  -170      2 LAND
99811       40255 ---- IRBID                 32.33   35.51   619    -34 BERG
99812       40256 ---- WADI RAYAN            32.24   35.35  -200     32 LAND
99801       40257 ---- RAS MUNEEF            32.22   35.45  1150   -182 LAND
99802       40260 ---- H-5 SAFAWI            32.12   37.08   674      1 LAND
99803       40265 ---- MAFRAQ                32.22   36.15   683     -6 LAND
99804       40267 ---- WADI DHULAIL          32.09   36.17   580     18 LAND
99805       40268 ---- SALT                  32.02   35.44   915    -49 LAND
99806       40275 ---- QATRANEH              31.15   36.07   768     49 LAND
99807       40280 ---- JERICHO               31.52   35.30  -275     -3 LAND
99808       40285 ---- DEIR ALLA             32.13   35.37  -224    -11 LAND
99809       40288 ---- AL AZRAQ              31.50   36.49   527     -9 LAND
99810       40292 ---- ER RABBAH             31.16   35.45   920    -25 LAND
99811       40296 ---- GHOR EL SAFI          31.02   35.28  -350     44 LAND
99812       40298 ---- TAFILEH               30.47   35.43  1200    -42 LAND
99801       40300 ---- SHOUBAK               30.31   35.32  1365    -59 LAND
99802       40305 ---- JAFER                 30.17   36.09   853     21 LAND
99803       40310 ---- MA'AN                 30.10   35.47  1069      7 BERG
99804       40340 ---- AQABA AIRPORT         29.33   35.00    51     53 LAND
99805       40341 ---- AQABA (PORT)          29.29   34.59     2    102 KUES
99803       60250 GMAA AGADIR/INEZGANE       30.23   -9.34    27      7 KUES
99804       60765 DTTG GABES                 33.53   10.06     4      0 KUES
99801       62010 HLLT TRIPOLI               32.40   13.09    81     -1 KUES
99802       62019 HLRF SIRTE                 31.12   16.35    13      9 KUES
99803       62053 HLLB BENGHAZI              32.06   20.16   131    -51 KUES
99804       62450 ---- SUEZ                  29.52   32.28     3     10 LAND
99805       62456 HETB TABA/RAS              29.36   34.47   749    -21 LAND
99805       69679 KQUA RAJLOVAC              43.52   18.18   489    137 LAND
99805       F9400 OJ38 ZARQA AIRPORT         32.02   36.09   732     32 LAND
99806       F9401 ---- LOD IL                32.35   35.35   568   -120 LAND
99804       F9501 ---- BOCHUM UMSPWK.        51.28    7.11    82     26 LAND
99805       F9502 ---- EISERFELD UMSPWK.     50.51    7.59   226    102 LAND
99806       F9503 ---- GUNDELFINGEN UMSPWK.  48.31   10.23   436     12 LAND
99807       F9504 ---- HANEKENF�HR UMSPWK.   52.29    7.18    27      6 LAND
99808       F9505 ---- HOHENECK UMSPWK.      48.55    9.12   275     -1 LAND
99809       F9506 ---- K�HMOOS UMSPWK.       47.36    7.57   736    -24 LAND
99810       F9507 ---- LEUPOLZ UMSPWK.       47.44   10.22   721     47 LAND
99811       F9508 ---- MITTELBEXBACH UMSPWK  49.22    7.14   363      0 LAND
99812       F9509 ---- NIEDERSTEDEM UMSPWK.  49.55    6.29   233     59 LAND
99801       F9510 ---- RHEINAU UMSPWK.       49.26    8.33   106     -9 LAND
99802       F9511 ---- ROMMERSKIRCHEN UMSPW  51.01    6.42    87     -5 LAND
99803       F9512 ---- URBERACH UMSPWK.      49.59    8.46   177    -33 LAND
99804       F9513 ---- WEI�ENTURM UMSPWK.    50.24    7.27   141     -4 LAND
99805       F9514 ---- WESTERKAPPELN UMSPWK  52.17    7.53    80      2 LAND
99806       K1060 ---- AURICH                53.27    7.28     4      1 LAND
99807       K1083 ---- BORKUM                53.34    6.45     5     -4 KUES
99808       K1091 ---- DOERPEN               52.59    7.22     6      1 LAND
99809       K1115 ---- GELSENKIRCHEN         51.30    7.06    44     29 LAND
99810       K1140 ---- LOENINGEN             52.45    7.45    36     -6 LAND
99811       K1161 ---- BOCHUM                51.29    7.16   101      7 LAND
99812       K1170 ---- SOLINGEN              51.09    7.05   209    -15 LAND
99801       K1171 ---- LEVERKUSEN            51.01    6.59    44      4 LAND
99802       K1174 ---- HEINSBERG             51.03    6.06    57     14 LAND
99803       K1176 ---- KLEVE                 51.46    6.06    46    -25 LAND
99804       K1188 ---- DUISBURG              51.28    6.44    21     14 LAND
99805       K1407 ---- WYK/FOEHR             54.42    8.34     1      0 KUES
99806       K1445 ---- HEIDE/HOLSTEIN        54.13    9.06    12     -8 LAND
99807       K1481 ---- ELSFLETH              53.14    8.28     1      3 LAND
99808       K1484 ---- GLUECKSTADT           53.48    9.26     2     -1 LAND
99809       K1489 ---- BUCHHOLZ I.D. NORDH.  53.21    9.56    77    -13 LAND
99810       K1511 ---- CLOPPENBURG           52.51    8.04    42     -7 LAND
99811       K1514 ---- MELLE                 52.12    8.21    72     27 LAND
99812       K1520 ---- RAHDEN-VARL           52.27    8.34    42      2 LAND
99801       K1524 ---- HERFORD               52.08    8.41    77     25 LAND
99802       K1546 ---- HILDESHEIM            52.11    9.57    85     15 LAND
99803       K1547 ---- HAMELN                52.07    9.20    66     74 LAND
99804       K1550 ---- HOLZMINDEN            51.49    9.28   128     71 LAND
99805       K1579 ---- MELSUNGEN             51.08    9.33   190     16 LAND
99806       K1584 ---- AROLSEN               51.23    9.03   220     -1 LAND
99807       K1585 ---- ARNSBERG              51.23    8.04   218      6 LAND
99808       K1586 ---- WILLINGEN/UPLAND      51.18    8.36   580    -64 LAND
99809       K1596 ---- FRANKENBERG/EDER      51.03    8.49   290      0 LAND
99810       K1597 ---- LENNESTADT-ALTENHUND  51.07    8.05   300    116 LAND
99811       K1599 ---- BAD BERLEBURG         50.59    8.22   610   -107 LAND
99812       K1705 ---- OSTENFELD             54.19    9.48    15      1 LAND
99801       K2107 ---- VOELKLINGEN           49.16    6.52   220     16 LAND
99802       K2204 ---- JUELICH               50.55    6.25    91     -1 LAND
99803       K2221 ---- KOELN (BOTAN.GART.)   50.58    6.58    45      3 LAND
99804       K2226 ---- EUSKIRCHEN            50.39    6.47   176      9 LAND
99805       K2245 ---- BAD NEUENAHR-AHRWL.   50.32    7.05   111     59 LAND
99806       K2247 ---- NEUWIED-WOLLENDORF    50.27    7.26   121     16 LAND
99807       K2259 ---- MAYEN                 50.20    7.14   230     -8 LAND
99808       K2265 ---- MANDERSCHEID          50.06    6.48   403     31 LAND
99809       K2269 ---- BAD BERTRICH          50.04    7.01   160     59 LAND
99810       K2270 ---- DAUN                  50.12    6.50   430      4 LAND
99811       K2274 ---- BAD KREUZNACH         49.51    7.52   102     83 LAND
99812       K2286 ---- WOLFSTEIN/PFALZ       49.35    7.37   200     63 LAND
99801       K2288 ---- KAISERSLAUTERN        49.27    7.47   248     72 LAND
99802       K2290 ---- PIRMASENS             49.13    7.35   280      4 LAND
99803       K2301 ---- OFFENBURG             48.28    7.57   155      7 LAND
99804       K2309 ---- KEHL                  48.35    7.49   137     -2 LAND
99805       K2360 ---- SCHAUINSLAND          47.55    7.55  1205   -243 BERG
99806       K2507 ---- MICHELSTADT           49.41    9.00   204      9 LAND
99807       K2561 ---- FRANKFURT/PALMENGAR.  50.08    8.39   107     29 LAND
99808       K2588 ---- BAD SCHWALBACH        50.08    8.04   320     -4 LAND
99809       K2596 ---- DARMSTADT             49.53    8.41   162      3 LAND
99810       K2601 ---- SIEGEN                50.52    8.01   263     65 LAND
99811       K2611 ---- MARBURG               50.49    8.47   195     43 LAND
99812       K2613 ---- MAINZ                 49.59    8.16   125     47 LAND
99801       K2614 ---- ALZEY                 49.45    8.07   166     53 LAND
99802       K2630 ---- SCHLUECHTERN          50.21    9.31   212     84 LAND
99803       K2635 ---- WORMS                 49.38    8.23    91      3 LAND
99804       K2637 ---- GELNHAUSEN            50.12    9.11   155     25 LAND
99805       K2644 ---- WALDEMS               50.16    8.21   400     -3 LAND
99806       K2646 ---- LIMBURG               50.25    8.04   185     12 LAND
99807       K2649 ---- KOENIGSTEIN/TS.       50.11    8.29   388      9 LAND
99808       K2667 ---- BEERFELDEN            49.34    8.58   450    -43 LAND
99809       K2671 ---- LOHR                  50.01    9.37   161    129 LAND
99810       K2679 ---- BAD MERGENTHEIM       49.29    9.46   250     56 LAND
99811       K2688 ---- BAD BERGZABERN        49.07    8.00   252    -38 LAND
99812       K2689 ---- HEILBRONN             49.09    9.14   167     49 LAND
99801       K2693 ---- HEIDELBERG            49.25    8.40   110     29 LAND
99802       K2696 ---- PHILIPPSBURG (KKW)    49.15    8.27   100      1 LAND
99803       K2701 ---- BADEN BADEN           48.46    8.15   218     40 LAND
99804       K2706 ---- BAD HERRENALB         48.48    8.27   351     10 LAND
99805       K2711 ---- PFORZHEIM             48.54    8.44   245     20 LAND
99806       K2714 ---- LUDWIGSBURG           48.54    9.12   287    -13 LAND
99807       K2718 ---- KIRCHHEIM/TECK        48.40    9.25   289     47 LAND
99808       K2719 ---- WELZHEIM              48.53    9.38   510    -40 LAND
99809       K2721 ---- MURRHARDT             48.58    9.34   344      6 LAND
99810       K2724 ---- SCHWAEBISCH HALL      49.07    9.45   387     15 LAND
99811       K2727 ---- SCHWAEB.GMUEND        48.47    9.48   415      3 LAND
99812       K2729 ---- MERKLINGEN            48.30    9.42   747    -11 LAND
99801       K2735 ---- SCHONACH              48.08    8.12   904    -46 LAND
99802       K2736 ---- WOLFACH               48.18    8.14   265     87 LAND
99803       K2739 ---- VILLINGEN SCHWENN.    48.03    8.28   720     11 LAND
99804       K2753 ---- MUENSINGEN-APPELST.   48.23    9.29   750    -13 LAND
99805       K2757 ---- ROTTWEIL              48.11    8.38   588    -18 LAND
99806       K2760 ---- SIGMARINGEN           48.04    9.12   580      9 LAND
99807       K2761 ---- BONNDORF              47.49    8.21   876    -64 LAND
99808       K2765 ---- BIBERACH              48.07    9.48   534      8 LAND
99809       K2767 ---- TITISEE-NEUSTADT      47.54    8.10   860     -2 LAND
99810       K2778 ---- WALDSHUT              47.37    8.14   330     99 LAND
99811       K2780 ---- DONAUESCHINGEN        47.57    8.30   677     54 LAND
99812       K2786 ---- PFULLENDORF-BRUNNHS.  47.55    9.17   638     32 LAND
99801       K2787 ---- UEBERLINGEN/BODENSEE  47.46    9.10   440      7 LAND
99802       K2791 ---- RAVENSBURG            47.48    9.37   440      2 LAND
99803       K2796 ---- LINDENBERG/ALLGAEU    47.36    9.53   760    -38 LAND
99804       K2798 ---- STOCKACH              47.51    9.02   475      6 LAND
99805       K2832 ---- TAUBERBISCHOFSHEIM    49.37    9.41   179    113 LAND
99806       K2868 ---- REUTLINGEN-BETZING.   48.30    9.11   360     37 LAND
99807       K2890 ---- RASTATT               48.52    8.11   116      2 LAND
99808       K2913 ---- BOEBLINGEN            48.41    8.58   445      7 LAND
99809       K2920 ---- HERRENBERG            48.36    8.53   431     27 LAND
99810       K2923 ---- ROTTENBURG            48.29    8.57   342    106 LAND
99811       K2932 ---- TUTTLINGEN            48.01    8.49   648     -3 LAND
99812       K3018 ---- ZINNOWITZ             54.05   13.54     2     -1 KUES
99801       K3182 ---- BERNBURG/SAALE        51.50   11.43    81    -14 LAND
99802       K3187 ---- QUEDLINBURG           51.47   11.09   123     18 LAND
99803       K3362 ---- BITTERFELD            51.38   12.19    80     11 LAND
99804       K3382 ---- BAUTZEN               51.10   14.28   207     16 LAND
99805       K3384 ---- MEISSEN               51.09   13.27   225    -25 LAND
99806       K3404 ---- SONDERSHAUSEN         51.22   10.54   201     17 LAND
99807       K3406 ---- BAD FRANKENHAUSEN/KY  51.21   11.06   130     43 LAND
99808       K3414 ---- RASTENBERG            51.11   11.25   200     33 LAND
99809       K3822 ---- EUTIN                 54.08   10.35    50     -1 LAND
99810       K3854 ---- BAD SEGEBERG          53.56   10.18    49    -12 LAND
99811       K3869 ---- GRAMBECK              53.34   10.41    27      3 LAND
99812       K3883 ---- UELZEN                52.58   10.33    49      7 LAND
99801       K3891 ---- LUENEBURG             53.16   10.26    11      9 LAND
99802       K3910 ---- WOLFSBURG             52.27   10.46    56      8 LAND
99803       K3924 ---- SALZGITTER            52.02   10.19   130    -10 LAND
99804       K3973 ---- BAD LAUTERBERG        51.38   10.29   300    -16 LAND
99805       K3982 ---- CLAUSTHAL-ZELLERFLD.  51.48   10.20   590    -28 LAND
99806       K3997 ---- ESCHWEGE              51.11   10.04   170     91 LAND
99807       K4033 ---- OCHSENKOPF            50.02   11.48  1019   -434 BERG
99808       K4036 ---- KRONACH               50.14   11.20   305     49 LAND
99809       K4042 ---- KULMBACH              50.06   11.27   330     56 LAND
99810       K4054 ---- SCHWEINFURT           50.04   10.13   240     -5 LAND
99811       K4057 ---- KITZINGEN             49.44   10.12   230     33 LAND
99812       K4058 ---- EBRACH                49.51   10.29   360    -15 LAND
99801       K4069 ---- GUNZENHSN.            49.08   10.45   413     28 LAND
99802       K4071 ---- SCHWABACH             49.20   11.01   343     -2 LAND
99803       K4086 ---- FUERTH/BAYERN         49.29   10.58   313     -3 LAND
99804       K4087 ---- ERLANGEN              49.37   11.00   270     50 LAND
99805       K4091 ---- UFFENHEIM             49.32   10.14   340     27 LAND
99806       K4093 ---- ROTHENBURG ODT.       49.23   10.11   406     14 LAND
99807       K4100 ---- ELLWANGEN/JAGST       48.58   10.08   443     33 LAND
99808       K4102 ---- HEIDENHEIM            48.40   10.08   500     43 LAND
99809       K4105 ---- NOERDLINGEN           48.51   10.30   425     64 LAND
99810       K4108 ---- EICHSTAETT            48.54   11.10   397    -10 LAND
99811       K4116 ---- ALTOMUENSTER          48.23   11.15   502     -1 LAND
99812       K4130 ---- KRUMBACH-EDENHAUSEN   48.15   10.25   520     -1 LAND
99801       K4138 ---- ISNY                  47.41   10.03   712     51 LAND
99802       K4140 ---- OBERSTAUFEN           47.34   10.02   800    -78 LAND
99803       K4149 ---- KAUFBEUREN            47.53   10.36   720    -20 LAND
99804       K4157 ---- MITTENWALD            47.27   11.16   920     50 LAND
99805       K4169 ---- BAD TOELZ             47.47   11.33   640     -5 LAND
99806       K4171 ---- EBERSBERG             48.05   11.57   570    -15 LAND
99807       K4172 ---- HOLZKIRCHEN/OBB.      47.53   11.42   685    -33 LAND
99808       K4179 ---- KREUTH                47.39   11.45   793    -62 LAND
99809       K4181 ---- SCHLIERSEE            47.44   11.51   780     52 LAND
99810       K4185 ---- MAINBURG              48.39   11.48   413     18 LAND
99811       K4204 ---- JENA/STERNWARTE       50.56   11.35   155     43 LAND
99812       K4244 ---- LOBENSTEIN            50.27   11.38   500     39 LAND
99801       K4402 ---- FREIBERG              50.56   13.20   380     25 LAND
99802       K4408 ---- BAD GOTTLEUBA         50.51   13.56   380     15 LAND
99803       K4420 ---- GREIZ-DOELAU          50.37   12.10   270     50 LAND
99804       K4473 ---- SELB                  50.10   12.08   535     41 LAND
99805       K4476 ---- TIRSCHENREUTH         49.53   12.21   515     12 LAND
99806       K4484 ---- OBERVIECHTACH         49.27   12.25   498     15 LAND
99807       K4488 ---- CHAM                  49.13   12.40   396     33 LAND
99808       K4501 ---- MALLERSDORF/NDB.      48.47   12.15   410    -26 LAND
99809       K4503 ---- LANDSHUT              48.32   12.08   391     66 LAND
99810       K4514 ---- FREYUNG               48.48   13.33   645    -36 LAND
99811       K4529 ---- WASSERBURG/INN        48.03   12.13   443     31 LAND
99812       K4531 ---- TROSTBERG             48.01   12.33   487    -13 LAND
99801       K4533 ---- TRAUNSTEIN            47.52   12.39   596     13 LAND
99802       K4535 ---- BAD REICHENHALL       47.45   12.54   455     14 LAND
99803       K4536 ---- BERCHTESG.            47.38   13.01   550    183 LAND
99804       K4540 ---- REIT IM WINKL         47.40   12.29   675     28 LAND
99805       K4546 ---- BAYRISCHZELL          47.41   12.01   805     18 LAND
99806       K4570 ---- BROTJACKLRIEGEL       48.49   13.13  1016   -420 BERG
99807       K9097 ---- DETMOLD               51.57    8.54   194     13 LAND
99808       N0101 ---- BALDERSCHWANG         47.28   10.06  1050      2 BERG
99809       N0113 ---- LINDAU                47.33    9.44   400     42 LAND
99810       N0121 ---- MONSCHAU              50.32    6.15   542     17 LAND
99811       N0122 ---- WANGEN/ALLGAEU        47.41    9.52   588     62 LAND
99812       N0136 ---- BAD SCHUSSENRIED      48.00    9.40   576     14 LAND
99801       N0139 ---- BAD WALDSEE           47.55    9.45   620    -39 LAND
99802       N0149 ---- MARKTREDW.            50.00   12.07   508     42 LAND
99803       N0151 ---- SCHLEIDEN-SCHOENES.   50.31    6.24   572     -4 LAND
99804       N0153 ---- WARENDORF             51.57    8.01    53      7 LAND
99805       N0157 ---- RIEDLINGEN            48.09    9.28   538     26 LAND
99806       N0159 ---- SAULGAU-BOLSTERN      47.59    9.28   640    -51 LAND
99807       N0171 ---- EHINGEN/DONAU         48.17    9.43   520      3 LAND
99808       N0197 ---- GOTTMADINGEN          47.44    8.47   430     20 LAND
99809       N0214 ---- BLUMBERG              47.51    8.32   707      2 LAND
99810       N0224 ---- AHLEN                 51.47    7.52    70     -1 LAND
99811       N0226 ---- DUEREN                50.48    6.29   127     -5 LAND
99812       N0242 ---- HINDELANG/OSTRACHTAL  47.27   10.26   930      6 LAND
99801       N0253 ---- IMMENSTADT            47.33   10.13   731     -9 LAND
99802       N0258 ---- ZELL I.WIES.-PFAFFB.  47.44    7.52   730    -18 LAND
99803       N0267 ---- LOERRACH              47.38    7.39   309     37 LAND
99804       N0273 ---- LEUTKIRCH             47.50   10.01   655     39 LAND
99805       N0283 ---- HEITERSHEIM           47.53    7.39   231     22 LAND
99806       N0291 ---- BREISACH              48.02    7.35   192     13 LAND
99807       N0304 ---- ERKELENZ              51.05    6.19    99    -17 LAND
99808       N0311 ---- GUTACH/BR.            48.07    8.01   302    -24 LAND
99809       N0332 ---- MINDELHEIM            48.03   10.31   607     23 LAND
99810       N0352 ---- GERSTETTEN-DETTINGEN  48.36   10.07   582    -39 LAND
99811       N0359 ---- DISCHINGEN(EGAUWAS.)  48.41   10.22   460      0 LAND
99812       N0406 ---- DINKELSBUEHL          49.04   10.20   444     22 LAND
99801       N0411 ---- SCHRAMBERG            48.13    8.23   502     58 LAND
99802       N0429 ---- VIERSEN               51.15    6.22    60     -4 LAND
99803       N0432 ---- BOPFINGEN             48.51   10.21   497      3 LAND
99804       N0445 ---- DONAUWOERTH           48.43   10.47   405     44 LAND
99805       N0447 ---- STRAELEN              51.27    6.16    45    -15 LAND
99806       N0462 ---- VECHTA                52.45    8.18    41     -1 LAND
99807       N0469 ---- OBERKIRCH             48.31    8.05   190     19 LAND
99808       N0474 ---- WERTINGEN             48.34   10.41   430     -1 LAND
99809       N0477 ---- ACHERN                48.38    8.03   138     -3 LAND
99810       N0505 ---- FUESSEN-WEISSENSEE    47.35   10.38   790     65 LAND
99811       N0514 ---- ANKUM                 52.33    7.53    62     11 LAND
99812       N0527 ---- FORBACH-HERRENWIES    48.40    8.16   764     -3 LAND
99801       N0546 ---- HASELUENNE            52.40    7.29    17      4 LAND
99802       N0548 ---- SONTRA                51.04    9.56   365    -62 LAND
99803       N0554 ---- RINGGAU-RENDA         51.04   10.05   395    -55 LAND
99804       N0586 ---- SCHWABMUENCHEN        48.11   10.46   555     12 LAND
99805       N0602 ---- MEPPEN                52.42    7.18    14      4 LAND
99806       N0635 ---- WITZENHAUSEN-ZIEGH.   51.22    9.45   240     23 LAND
99807       N0645 ---- POETTMES-SCHORN       48.35   11.06   404     22 LAND
99808       N0674 ---- ABENSBERG-SANDHARL.   48.50   11.49   380      7 LAND
99809       N0677 ---- LANDAU/PFALZ          49.12    8.06   150    -13 LAND
99810       N0680 ---- GERMERSHEIM           49.13    8.23   106     -5 LAND
99811       N0717 ---- FRIESOYTHE            53.01    7.52     8      4 LAND
99812       N0738 ---- UPLENGEN-STAPELERM.   53.21    7.51    14     -4 LAND
99801       N0751 ---- THALMAESSING          49.05   11.14   417     21 LAND
99802       N0753 ---- GREDING               49.03   11.22   425     -6 LAND
99803       N0755 ---- SPEYER                49.21    8.25    99      1 LAND
99804       N0761 ---- KRAICHTAL-GOCHSHEIM   49.06    8.45   170     22 LAND
99805       N0763 ---- BEILNGRIES            49.02   11.28   370     40 LAND
99806       N0765 ---- LEER                  53.13    7.29     4     -2 LAND
99807       N0775 ---- RIEDENBURG            48.57   11.43   363     24 LAND
99808       N0778 ---- NEUSTADT/DONAU        48.52   11.46   360     45 LAND
99809       N0781 ---- KELHEIM               48.55   11.53   354     33 LAND
99810       N1012 ---- KALBACH               50.25    9.40   405    -35 LAND
99811       N1026 ---- LOSSBURG              48.23    8.29   601     14 LAND
99812       N1027 ---- GREBENHAIN            50.29    9.20   435     28 LAND
99801       N1033 ---- HORB                  48.27    8.41   389     59 LAND
99802       N1038 ---- ALBSTADT-BURGFELDEN   48.14    8.56   911    -74 LAND
99803       N1040 ---- HEMMOOR               53.42    9.09     5      2 LAND
99804       N1043 ---- BALINGEN              48.17    8.53   571     -1 LAND
99805       N1054 ---- HAIGERLOCH-HART       48.23    8.51   483    -35 LAND
99806       N1075 ---- TUEBINGEN             48.32    9.02   445     16 LAND
99807       N1101 ---- BAERNAU               49.49   12.26   610      0 LAND
99808       N1107 ---- NEUFFEN               48.33    9.24   480    -78 LAND
99809       N1120 ---- ZITTAU                50.54   14.49   235      1 LAND
99810       N1122 ---- NEUSTADT/WN-ALTENST.  49.43   12.10   400     70 LAND
99811       N1140 ---- GEISLINGEN            48.38    9.51   443      5 LAND
99812       N1147 ---- GOEPPINGEN            48.43    9.37   361     41 LAND
99801       N1150 ---- ROTENBURG/FULDA       50.59    9.44   200     94 LAND
99802       N1151 ---- KEMNATH               49.52   11.54   464      2 LAND
99803       N1156 ---- GUBEN                 51.56   14.42    46     15 LAND
99804       N1171 ---- SPANGENBERG           51.07    9.40   260     61 LAND
99805       N1201 ---- WALDMUENCHEN          49.23   12.43   510      3 LAND
99806       N1215 ---- WINTERBACH            48.48    9.29   280     48 LAND
99807       N1245 ---- BACKNANG              48.57    9.26   291      2 LAND
99808       N1265 ---- HOHENFELS             49.12   11.51   423     -8 LAND
99809       N1319 ---- ALTENSTEIG-WART       48.37    8.39   586     -9 LAND
99810       N1323 ---- FRANKFURT/ODER        52.22   14.32    49     -5 LAND
99811       N1325 ---- REGEN                 48.58   13.08   572     44 LAND
99812       N1333 ---- BISCHOFSMAIS          48.55   13.05   684    -18 LAND
99801       N1336 ---- BAD LIEBENZELL        48.46    8.44   319     19 LAND
99802       N1345 ---- VIECHTACH             49.05   12.54   455     26 LAND
99803       N1353 ---- LAM                   49.12   13.05   620     -1 LAND
99804       N1354 ---- RENNINGEN             48.46    8.57   405     29 LAND
99805       N1371 ---- FURTH IM WALD         49.18   12.50   392     37 LAND
99806       N1382 ---- FALKENSTEIN KR.CHAM   49.06   12.29   562     11 LAND
99807       N1401 ---- BOENNIGHEIM           49.02    9.05   228     15 LAND
99808       N1429 ---- NEUKIRCHEN-SEIGHS.    50.55    9.21   380    -11 LAND
99809       N1441 ---- SCHWALMSTADT          50.54    9.13   225     54 LAND
99810       N1461 ---- SANKT ENGLMAR         49.00   12.50   810   -195 LAND
99811       N1475 ---- DEGGENDORF            48.50   12.57   313     13 LAND
99812       N1503 ---- AALEN                 48.51   10.06   418      0 LAND
99801       N1528 ---- WUESTENROT            49.05    9.28   485    -37 LAND
99802       N1542 ---- EBERSWALDE            52.50   13.48    45      8 LAND
99803       N1551 ---- KUENZELSAU-MORSBACH   49.17    9.44   241     50 LAND
99804       N1613 ---- CRAILSHEIM            49.08   10.05   417     44 LAND
99805       N1622 ---- BLAUFELDEN            49.18    9.58   450      6 LAND
99806       N1648 ---- MOECKMUEHL            49.18    9.21   176     40 LAND
99807       N1712 ---- MOSBACH-DIEDESHEIM    49.21    9.06   140     71 LAND
99808       N2028 ---- FRIEDEBURG-HORSTEN    53.27    7.56     3      5 LAND
99809       N2032 ---- USLAR                 51.40    9.38   190     -6 LAND
99810       N2046 ---- MURNAU                47.40   11.14   622     13 LAND
99811       N2048 ---- KOCHEL                47.40   11.22   600     35 LAND
99812       N2076 ---- SAUERLACH             47.59   11.39   615    -25 LAND
99801       N2103 ---- OBERAMMERGAU          47.36   11.05   873    -38 LAND
99802       N2117 ---- WEILHEIM              47.51   11.09   568     59 LAND
99803       N2132 ---- GRUENSTADT            49.34    8.10   200    -67 LAND
99804       N2142 ---- DACHAU                48.15   11.27   483     21 LAND
99805       N2147 ---- STARNBERG             48.00   11.21   596     -4 LAND
99806       N2159 ---- KIRCHHEIMBOLANDEN     49.40    8.01   230      4 LAND
99807       N2171 ---- WOLFHAGEN             51.18    9.09   310     18 LAND
99808       N2173 ---- PASEWALK              53.30   14.00    10     40 LAND
99809       N2193 ---- LANDAU/ISAR           48.41   12.42   338     18 LAND
99810       N2202 ---- LALLING               48.50   13.06   353      1 LAND
99811       N2204 ---- HEPPENHEIM            49.39    8.38   101     -5 LAND
99812       N2216 ---- BIBLIS                49.41    8.25    88      2 LAND
99801       N2219 ---- SEEHEIM-JUGENHEIM     49.45    8.38   132    -10 LAND
99802       N2221 ---- GEISENHAUSEN          48.29   12.16   467      7 LAND
99803       N2222 ---- LAUTERTAL/ODW.        49.43    8.41   198     -6 LAND
99804       N2228 ---- FRIEDLAND             53.41   13.34    14     14 LAND
99805       N2235 ---- HOFGEISMAR            51.30    9.23   162     83 LAND
99806       N2249 ---- OPPENHEIM             49.51    8.22    85     38 LAND
99807       N2253 ---- EGING AM SEE          48.41   13.15   400     -4 LAND
99808       N2254 ---- RUESSELSHEIM          49.59    8.27    87     13 LAND
99809       N2271 ---- SCHOENBERG/NDB.       48.50   13.20   550     22 LAND
99810       N2274 ---- SANKT OSWALD          48.53   13.25   754     21 LAND
99811       N2284 ---- MAUTH                 48.53   13.35   810    -35 LAND
99812       N2311 ---- WILLEBADESSEN-BORL.   51.35    9.02   280    -50 LAND
99801       N2336 ---- HOEXTER               51.47    9.24    93    106 LAND
99802       N2361 ---- OTTENSTEIN            51.57    9.25   270    -51 LAND
99803       N2362 ---- GRIMMEN               54.07   13.04    15      0 LAND
99804       N2372 ---- DEMMIN                53.55   13.03    17      5 LAND
99805       N2375 ---- EMMERTHAL-GROHNDE     52.01    9.25    80     48 LAND
99806       N2386 ---- ANKLAM                53.51   13.41    12     -5 LAND
99807       N2388 ---- DORFEN KR.ERDING      48.16   12.10   439     41 LAND
99808       N2395 ---- WOLGAST               54.03   13.47     8     -7 KUES
99809       N2402 ---- NIEHEIM               51.48    9.07   230    -13 LAND
99810       N2412 ---- WUSTERHUSEN           54.07   13.37    31    -15 LAND
99811       N2431 ---- ASCHAU                47.46   12.20   620    -11 LAND
99812       N2433 ---- BAD MUENDER           52.11    9.28   110     31 LAND
99801       N2443 ---- RUHPOLDING-SEEHAUS    47.43   12.37   753    -18 LAND
99802       N2446 ---- SASSNITZ-STAPHEL      54.29   13.34     4     15 LAND
99803       N2457 ---- BERGEN/RUEGEN         54.25   13.26    75    -56 LAND
99804       N2475 ---- STRALSUND             54.18   13.04    13     -9 KUES
99805       N2571 ---- TEISENDORF            47.51   12.49   500      3 LAND
99806       N2575 ---- BAD SUELZE            54.07   12.40     5     16 LAND
99807       N2583 ---- BURGHAUSEN            48.11   12.51   413    -15 LAND
99808       N2603 ---- BODENKIRCHEN-AICH     48.26   12.24   464     10 LAND
99809       N2611 ---- EGGENFELDEN           48.24   12.47   400     44 LAND
99810       N2614 ---- PFARRKIRCHEN          48.26   12.56   410     18 LAND
99811       N2622 ---- PREROW A. DARSS       54.27   12.34     1      3 KUES
99812       N2626 ---- GRAAL-MUERITZ         54.15   12.16     6     11 LAND
99801       N2632 ---- POCKING               48.25   13.19   321     38 LAND
99802       N2704 ---- WALDKIRCHEN           48.43   13.36   625    -16 LAND
99803       N2781 ---- BUETZOW-WOLKEN        53.51   12.01    10     23 LAND
99804       N2813 ---- BAD DOBERAN           54.07   11.54    15     31 LAND
99805       N2822 ---- RERIK                 54.07   11.37    18    -11 KUES
99806       N2839 ---- WISMAR                53.53   11.26    26     22 LAND
99807       N3001 ---- SCHOEPPINGEN          52.06    7.15   100    -10 LAND
99808       N3002 ---- MUENCHBERG            50.12   11.48   545      9 LAND
99809       N3003 ---- GEFREES               50.05   11.43   475     48 LAND
99810       N3007 ---- SCHWARZENBACH/SAALE   50.12   11.55   532     22 LAND
99811       N3029 ---- OERLINGHAUSEN         51.58    8.39   180    -35 LAND
99812       N3035 ---- NAILA                 50.20   11.42   525     52 LAND
99801       N3041 ---- LICHTENFELS/OFR.      50.06   11.10   375     49 LAND
99802       N3047 ---- GEROLDSGRUEN-STEINB.  50.21   11.35   646    -52 LAND
99803       N3049 ---- EMLICHHEIM            52.37    6.51    14      5 LAND
99804       N3052 ---- PRESSECK              50.14   11.33   620    -26 LAND
99805       N3053 ---- STEINBACH AM WALD     50.27   11.23   616      1 LAND
99806       N3060 ---- BAD BENTHEIM          52.18    7.10    45     -9 LAND
99807       N3102 ---- AHAUS                 52.04    7.01    52      1 LAND
99808       N3114 ---- COESFELD              51.57    7.11    84     -6 LAND
99809       N3149 ---- EBERN-EYRICHSHOF      50.07   10.47   285     26 LAND
99810       N3206 ---- SULINGEN              52.41    8.49    48      3 LAND
99811       N3233 ---- NEUMARKT OPF.         49.17   11.26   426     -7 LAND
99812       N3240 ---- HOYA                  52.49    9.09    18     -3 LAND
99801       N3254 ---- OTTENDORF-OKRILLA     51.11   13.50   180     -2 LAND
99802       N3257 ---- PIRNA                 50.57   13.56   123     51 LAND
99803       N3264 ---- BISCHOFSWERDA         51.08   14.11   300     -8 LAND
99804       N3265 ---- AUERBACH/OPF.         49.42   11.38   418     35 LAND
99805       N3303 ---- HERSBRUCK             49.30   11.24   332    -12 LAND
99806       N3309 ---- LAUF/HEUCHLING        49.31   11.18   333    -13 LAND
99807       N3312 ---- ALTDORF/OFR.          49.23   11.22   428     -9 LAND
99808       N3334 ---- GRAEFENBERG           49.39   11.15   477    -12 LAND
99809       N3360 ---- STADELHOFEN           50.00   11.12   476    -17 LAND
99810       N3420 ---- FORCHHEIM/OFR.        49.43   11.03   257     41 LAND
99811       N3432 ---- NEUSTADT/AISCH-UNTN.  49.35   10.31   320     11 LAND
99812       N3462 ---- RIESA                 51.18   13.15   140      3 LAND
99801       N3504 ---- HASSFURT              50.02   10.31   239     -4 LAND
99802       N3533 ---- TORGAU                51.35   13.00    80      4 LAND
99803       N3608 ---- KAMENZ                51.17   14.07   157    -15 LAND
99804       N3619 ---- HOYERSWERDA           51.26   14.15   135    -20 LAND
99805       N3666 ---- ELSTERWERDA           51.28   13.32    91     10 LAND
99806       N3685 ---- GRAEFENTONNA          51.04   10.44   207     54 LAND
99807       N3727 ---- OBERWEISSENBRUNN      50.25    9.57   630    -13 LAND
99808       N3729 ---- BISCHOFSHEIM/RHOEN    50.24   10.00   465     10 LAND
99809       N3754 ---- HAMMELBURG            50.07    9.54   184    101 LAND
99810       N3778 ---- BURGSINN              50.09    9.39   235     15 LAND
99811       N3833 ---- WEIBERSBRUNN          49.54    9.24   470   -109 LAND
99812       N3924 ---- WEIKERSHEIM           49.28    9.57   370    -10 LAND
99801       N3951 ---- WERTHEIM-EICHEL       49.46    9.33   140     73 LAND
99802       N4002 ---- MUDAU-SCHLOSSAU       49.33    9.09   470    -50 LAND
99803       N4005 ---- AMORBACH              49.39    9.14   183     30 LAND
99804       N4032 ---- LUETZELBACH           49.46    9.05   274     51 LAND
99805       N4045 ---- ASCHAFFENBURG         49.59    9.07   110     44 LAND
99806       N4068 ---- GIFHORN               52.29   10.33    51     10 LAND
99807       N4070 ---- DIEBURG               49.54    8.51   145     47 LAND
99808       N4116 ---- HANAU                 50.06    8.57   102     17 LAND
99809       N4123 ---- EIBENSTOCK(TALSP.)    50.32   12.36   546     30 LAND
99810       N4161 ---- GOSLAR                51.55   10.26   266     19 LAND
99811       N4162 ---- ZWICKAU               50.41   12.28   347     10 LAND
99812       N4176 ---- ROTTACH-EGERN         47.41   11.46   747    -16 LAND
99801       N4191 ---- ZWOENITZ              50.39   12.49   500     15 LAND
99802       N4241 ---- NEU ANSPACH           50.18    8.30   375    -27 LAND
99803       N4242 ---- WOLFENBUETTEL         52.10   10.31    88     21 LAND
99804       N4248 ---- ROCHLITZ              51.03   12.49   185      0 LAND
99805       N4253 ---- FRIEDBERG             50.20    8.45   158     38 LAND
99806       N4277 ---- LEHRE                 52.20   10.40    90     24 LAND
99807       N4333 ---- BAD HOMBURG           50.15    8.34   255     95 LAND
99808       N4359 ---- LEHRTE                52.23    9.59    60      2 LAND
99809       N4365 ---- ADELHEIDSDORF         52.33   10.03    41      4 LAND
99810       N4377 ---- ANNABERG_BUCHHOLZ     50.35   13.00   630    -79 LAND
99811       N4414 ---- HALBERSTADT           51.54   11.03   110      1 LAND
99812       N4426 ---- DOERNTHAL             50.44   13.20   558    -51 LAND
99801       N4464 ---- BRAUNSDORF            50.53   13.01   300    -17 LAND
99802       N4513 ---- GRIMMA                51.14   12.43   150      5 LAND
99803       N4535 ---- BAD DUEBEN            51.36   12.35    89     42 LAND
99804       N4561 ---- HERZBERG              51.40   10.21   230    -27 LAND
99805       N4601 ---- OSTERODE/HARZ         51.43   10.16   285     -1 LAND
99806       N4623 ---- NORTHEIM              51.43    9.59   121     74 LAND
99807       N4639 ---- DESSAU                51.51   12.15    60      7 LAND
99808       N4655 ---- BAD GANDERSHEIM       51.52   10.02   154     58 LAND
99809       N4838 ---- ADENSTEDT             52.00    9.56   194      1 LAND
99810       N4854 ---- SCHOENINGEN           52.08   10.57   170    -25 LAND
99811       N5015 ---- BARSINGHAUSEN         52.18    9.28   114     55 LAND
99812       N5044 ---- INGELHEIM             49.59    8.04   135     42 LAND
99801       N5056 ---- RUEDESHEIM            49.59    7.56   126     59 LAND
99802       N5111 ---- FREISEN/SAAR          49.33    7.15   465     -5 LAND
99803       N5146 ---- SOHREN                49.56    7.18   430     -4 LAND
99804       N5149 ---- RHAUNEN               49.52    7.20   370      5 LAND
99806       N5184 ---- SAALFELD              50.39   11.23   235     26 LAND
99807       N5227 ---- KUSEL                 49.32    7.24   235     89 LAND
99808       N5245 ---- LAUTERECKEN           49.39    7.36   158    135 LAND
99809       N5250 ---- RUDOLSTADT            50.44   11.22   193     68 LAND
99810       N5344 ---- STROMBERG/HUNSRUECK   49.57    7.47   300     29 LAND
99811       N5346 ---- ILMENAU               50.41   10.54   498    -18 LAND
99812       N5374 ---- BINGEN-BUEDESHEIM     49.57    7.54    82    103 LAND
99801       N5417 ---- NAUMBURG/SAALE        51.09   11.48   135     63 LAND
99802       N5432 ---- MUEHLHAUSEN           51.12   10.30   190     28 LAND
99803       N5446 ---- OBERWESEL             50.07    7.43   110    155 LAND
99804       N5528 ---- ARNSTADT              50.51   10.58   267      9 LAND
99805       N5537 ---- TAMBACH-DIETHARZ      50.48   10.37   470    -43 LAND
99806       N5570 ---- BAD TENNSTEDT         51.09   10.50   175     40 LAND
99807       N5601 ---- SOEMMERDA             51.10   11.08   140     22 LAND
99808       N5755 ---- NORDHAUSEN            51.31   10.48   247     -5 LAND
99809       N5791 ---- SANGERHAUSEN          51.29   11.19   185     31 LAND
99810       N5872 ---- BAD DUERRENBERG       51.18   12.05   103     14 LAND
99811       N5939 ---- ADORF                 50.19   12.16   450     11 LAND
99812       N6016 ---- STEFFENBERG           50.51    8.28   338     45 LAND
99801       N6037 ---- ULRICHSTEIN           50.35    9.12   575    -82 LAND
99802       N6067 ---- DELMENHORST           53.03    8.38    10     -4 LAND
99803       N6160 ---- BUTZBACH              50.28    8.40   238    -29 LAND
99804       N6172 ---- WETZLAR               50.32    8.30   180     67 LAND
99805       N6197 ---- MEUSELWITZ            51.03   12.18   174     46 LAND
99806       N6208 ---- DIETZHOELZTAL         50.51    8.20   355    -10 LAND
99807       N6223 ---- HERBORN               50.41    8.18   238      5 LAND
99808       N6230 ---- OSTERHOLZ-SCHARMBECK  53.13    8.49     5     15 LAND
99809       N6241 ---- MENGERSKIRCHEN        50.34    8.09   412     22 LAND
99810       N6250 ---- SCHMITTEN-TREISBERG   50.18    8.26   535   -185 LAND
99811       N6257 ---- BORNA                 51.09   12.28   135      5 LAND
99812       N6259 ---- WEILMUENSTER          50.26    8.23   210     -8 LAND
99801       N6357 ---- QUERFURT              51.23   11.35   190    -31 LAND
99802       N6423 ---- BAD ZWISCHENAHN       53.12    8.00     7      2 LAND
99803       N6435 ---- HETTSTEDT             51.39   11.31   159     46 LAND
99804       N6553 ---- HASSELFELDE(WASSW.)   51.43   10.49   485    -22 LAND
99805       N6566 ---- ALTENBRAK             51.44   10.56   300     -8 LAND
99806       N6695 ---- OSCHERSLEBEN/BODE     52.01   11.14    80     27 LAND
99807       N6813 ---- LINDAU/SACHS.-ANHALT  52.02   12.06    75      9 LAND
99808       N6935 ---- HALDENSLEBEN          52.17   11.26    50     29 LAND
99809       N7012 ---- BAD OLDESLOE          53.49   10.24    15     21 LAND
99810       N7029 ---- RATZEBURG             53.42   10.46    10     23 LAND
99811       N7040 ---- PRUEM                 50.13    6.25   465     28 LAND
99812       N7060 ---- ARZFELD               50.05    6.16   497    -43 LAND
99801       N7075 ---- BITBURG               49.59    6.33   285     19 LAND
99802       N7113 ---- NEUSTRELITZ           53.23   13.03    64      7 LAND
99803       N7134 ---- TRIPPSTADT            49.22    7.49   430    -20 LAND
99804       N7135 ---- TEMPLIN               53.07   13.31    60      5 LAND
99805       N7142 ---- ZEHDENICK             52.59   13.21    46      4 LAND
99806       N7182 ---- LOEBAU                51.06   14.41   249     51 LAND
99807       N7239 ---- HERMESKEIL            49.39    6.56   530    -20 LAND
99808       N7244 ---- ECKERNFOERDE          54.27    9.51    25    -11 LAND
99809       N7314 ---- WEISSWASSER           51.30   14.37   155    -22 LAND
99810       N7316 ---- MERZIG                49.27    6.38   171     65 LAND
99811       N7332 ---- SAARBURG              49.37    6.33   180     93 LAND
99812       N7386 ---- FUERSTENWALDE/SPREE   52.21   14.04    38     21 LAND
99801       N7395 ---- STRAUSBERG            52.35   13.53    73     18 LAND
99802       N7411 ---- DAHME                 51.52   13.26    86     13 LAND
99803       N7417 ---- DAHLEM-KRONENBURG     50.22    6.29   480     39 LAND
99804       N7511 ---- TREUENBRIETZEN        52.06   12.53    59     -7 LAND
99805       N7539 ---- WITTLICH              49.59    6.54   177     42 LAND
99806       N7544 ---- LEHNIN                52.19   12.45    35     14 LAND
99807       N7608 ---- KASTELLAUN            50.04    7.27   425      1 LAND
99808       N7622 ---- BURG B.MAGDEBURG      52.17   11.49    40      7 LAND
99809       N7651 ---- ORANIENBURG           52.45   13.12    35      6 LAND
99810       N7659 ---- NAUEN                 52.37   12.52    35     -2 LAND
99811       N7740 ---- FRIESACK              52.46   12.35    29      3 LAND
99812       N7744 ---- ALTENKIRCHEN          50.41    7.39   260     46 LAND
99801       N7817 ---- PRITZWALK             53.09   12.10    70     12 LAND
99802       N7822 ---- BLANKENHEIM/AHRHUET.  50.24    6.44   400      4 LAND
99803       N7868 ---- STENDAL               52.34   11.53    34      7 LAND
99804       N8032 ---- KIRCHEN/SIEG          50.48    7.54   300      6 LAND
99805       N8044 ---- WEITERFELD            50.44    7.56   460    -26 LAND
99806       N8101 ---- WALDBROEL             50.52    7.37   295      6 LAND
99807       N8128 ---- SIEGBURG              50.48    7.12    63     48 LAND
99808       N8146 ---- GUMMERSBACH           51.01    7.35   250      7 LAND
99809       N8204 ---- BRUEHL                50.50    6.55    61     -3 LAND
99810       N8232 ---- SALZWEDEL             52.52   11.09    23      2 LAND
99811       N8261 ---- HITZACKER             53.09   11.02    28      5 LAND
99812       N8307 ---- RADEVORMWALD          51.13    7.23   397    -36 LAND
99801       N8322 ---- WUPPERTAL-BARMEN      51.16    7.11   197     46 LAND
99802       N8326 ---- HAGENOW               53.26   11.11    30     -1 LAND
99803       N8331 ---- LUDWIGSLUST           53.20   11.30    30      2 LAND
99804       N8334 ---- WUPPERTAL-VOHW.       51.14    7.04   176      2 LAND
99805       N8346 ---- REMSCHEID             51.12    7.12   235      8 LAND
99806       N8349 ---- WERMELSKIRCHEN        51.08    7.14   280     -6 LAND
99807       N8369 ---- BERG.NEUKIRCHEN       51.05    7.02   130    -65 LAND
99808       N8381 ---- DORMAGEN              51.07    6.51    40      2 LAND
99809       N8403 ---- BAD MUENSTEREIFEL     50.33    6.46   320     45 LAND
99810       N8408 ---- SUDERBURG             52.54   10.26    70    -14 LAND
99811       N8421 ---- BAD BEVENSEN          53.05   10.34    32     20 LAND
99812       N8424 ---- ERFTSTADT-BLIESHEIM   50.47    6.49   106     -1 LAND
99801       N8439 ---- ZUELPICH              50.42    6.39   170     50 LAND
99802       N8481 ---- NEUSS                 51.11    6.42    39     17 LAND
99803       N8524 ---- TRITTAU               53.37   10.24    40      1 LAND
99804       N8527 ---- KREFELD               51.18    6.32    40     -1 LAND
99805       N8566 ---- MESCHEDE/HENNE        51.20    8.16   348     33 LAND
99806       N8613 ---- SORPE                 51.22    7.58   294     27 LAND
99807       N8615 ---- HARSEFELD             53.27    9.30    32     -5 LAND
99808       N8623 ---- BRILON                51.25    8.39   457      5 LAND
99809       N8625 ---- STADERSAND            53.38    9.32     5     -1 LAND
99810       N8631 ---- RUETHEN               51.30    8.27   330     -7 LAND
99811       N8634 ---- WARSTEIN              51.27    8.21   330      8 LAND
99812       N8653 ---- MOEHNE                51.30    8.04   232     -8 LAND
99801       N8667 ---- BAD BRAMSTEDT         53.55    9.54    10      9 LAND
99802       N8686 ---- FROENDENBERG          51.28    7.44   121     28 LAND
99803       N8690 ---- BROKDORF              53.52    9.20     1      1 KUES
99804       N8716 ---- SCHWERTE              51.28    7.34   180    -28 LAND
99805       N8723 ---- WINTERBERG-ALTASTBG.  51.12    8.28   782   -145 LAND
99806       N8777 ---- OLPE                  51.02    7.51   305     -4 LAND
99807       N8790 ---- BIGGE                 51.07    7.53   311    105 LAND
99808       N8825 ---- VERSE                 51.12    7.41   392     19 LAND
99809       N8829 ---- LUEDENSCHEID          51.13    7.38   444    -27 LAND
99810       N8832 ---- ISERLOHN-RODEN        51.22    7.40   222     27 LAND
99811       N8864 ---- ENNEPETAL-MILSPE      51.18    7.19   280     -6 LAND
99812       N8867 ---- SPROCKHOEVEL-HASSL.   51.20    7.17   270      4 LAND
99801       N8884 ---- HAGEN                 51.21    7.27   113     39 LAND
99802       N8947 ---- VELBERT-LANGENBERG    51.22    7.07   220     23 LAND
99803       N9030 ---- HERNE                 51.32    7.13    63     10 LAND
99804       N9067 ---- BOTTROP               51.33    6.57    38     14 LAND
99805       N9079 ---- OBERHAUSEN            51.31    6.49    33     19 LAND
99806       N9109 ---- MOERS                 51.27    6.39    26      3 LAND
99807       N9117 ---- HILDBURGHAUSEN        50.26   10.43   370     21 LAND
99808       N9126 ---- SCHMIEDEFELD/RSTG.    50.37   10.49   720    -54 LAND
99809       N9154 ---- SUHL                  50.37   10.40   505     74 LAND
99810       N9227 ---- WUENNENBERG           51.31    8.45   345     12 LAND
99811       N9228 ---- BAD SALZUNGEN         50.48   10.13   290      1 LAND
99812       N9320 ---- DELBRUECK             51.46    8.33    97      8 LAND
99801       N9323 ---- WADERSLOH             51.46    8.16    92    -15 LAND
99802       N9328 ---- RUHLA                 50.54   10.22   470     57 LAND
99803       N9349 ---- GOTHA                 50.56   10.40   321     53 LAND
99804       N9350 ---- SOEST                 51.34    8.07   110      8 LAND
99805       N9357 ---- EISENACH              50.59   10.22   240     40 LAND
99806       N9401 ---- HAMM                  51.41    7.49    59     16 LAND
99807       N9413 ---- EILSLEBEN             52.09   11.13   140     13 LAND
99808       N9446 ---- WALTROP               51.38    7.24    73      1 LAND
99809       N9530 ---- HALTERN               51.44    7.12    40     22 LAND
99810       N9538 ---- DORSTEN               51.40    6.59    33     25 LAND
99811       N9607 ---- WESEL-FLUEREN         51.42    6.35    25     -5 LAND
99812       N9608 ---- RENA                  61.11   11.22   255    115 LAND
99802       C0014 ---- HARSEWINKEL           51.58    8.13   119    -47 LAND
99803       C0015 ---- STEINHAGEN            52.01    8.25   122      5 LAND
99804       C0073 ---- BIELEFELD/OLDENTRUP   52.01    8.37   100     45 LAND
99808       P0004 ---- EUPEN                 50.49    6.03   240    -53 LAND
99810       P0006 ---- BILLERBECK            51.58    7.17   127    -37 LAND
99811       P0007 ---- TAUS                  49.26   12.54   428      1 LAND
99812       P0008 ---- COMO                  45.47    9.05    62    202 LAND
99801       P0009 ---- ARNHEIM               51.59    5.54    10     13 LAND
99802       P0010 ---- LUETTICH              50.38    5.33    50     34 LAND
99803       P0011 ---- MERAN                 46.40   11.09   324    552 LAND
99804       P0012 ---- LEIBSTADT             47.36    8.11   340     89 LAND
99805       P0013 ---- NEUSS-WEHL            51.08    6.41    60     -4 LAND
99808       P0016 ---- GR.FELDBG./TS.        50.14    8.28   880   -530 BERG
99809       P0017 ---- GROSS UMSTADT         49.52    8.56   168     24 LAND
99810       P0018 ---- MELIBOCUS             49.44    8.39   517   -395 BERG
99811       P0019 ---- NIDDA                 50.25    9.01   190     -2 LAND
99812       P0020 ---- VOGELSBERG            50.32    9.14   774   -281 BERG
99801       P0021 ---- LAMBRECHT             49.22    8.04   176    -39 LAND
99802       P0022 ---- NEBELHORN             47.24   10.18  2224   -930 BERG
99803       P0023 ---- KITZBUEHEL            47.26   12.22   870      0 LAND
99804       P0024 ---- RIVA D. GARDA         45.56   10.59   130    698 LAND
99805       P0025 ---- GEESTHACHT            53.25   10.20     0     38 LAND
99806       P0026 EDHI FINKENWERDER          53.32    9.50     0     10 LAND
99807       P0027 ---- BRUNSBUETTEL/SWA      53.54    9.08     0      2 KUES
99808       P0028 ---- HOECHSTADT            49.41   10.50   272     19 LAND
99809       P0029 ---- ISSUM                 51.32    6.25    35     -8 LAND
99810       P0030 ---- OBERHAUSEN-STERKRADE  51.32    6.52    54     -2 LAND
99811       P0031 ---- MUELHEIM/RUHR         51.26    6.53    38     22 LAND
99812       P0032 ---- SCHWELM               51.17    7.18   165      5 LAND
99801       P0033 ---- UNNA                  51.32    7.41    86     -5 LAND
99802       P0034 ---- SCHWANDORF            49.20   12.07   372     21 LAND
99803       P0035 ---- WESTERBERG            47.46   12.37  1168   -291 BERG
99804       P0036 ---- MUENSTER ZENTRUM      51.58    7.38    60     -6 LAND
99805       P0037 ---- METALLEUROP           53.33    8.28    10     -8 LAND
99806       P0038 ---- COTTBUS/LUB           51.45   14.19    76    -11 LAND
99807       P0039 ---- KOENIGS WUSTERH./LUB  52.18   13.38    48    -10 LAND
99808       P0040 ---- POTSDAM-ZENTRUM/LUB   52.24   13.04    31     10 LAND
99809       P0041 ---- PREMNITZ/LUB          52.32   12.21    30      0 LAND
99810       P0042 ---- SCHWEDT/LUB           53.03   14.18     6     13 LAND
99811       P0043 ---- SENFTENBERG/LUB       51.31   14.00   103      5 LAND
99812       P0044 ---- SPREMBERG/LUB         51.34   14.23   100     12 LAND
99801       P0045 ---- WITTENBERGE/LUB       53.00   11.46    22      4 LAND
99806       P0050 ---- FALKENSTEIN/TAUNUS    50.11    8.28   550   -153 LAND
99807       P0051 ---- DUELMEN               51.50    7.14    70      4 LAND
99809       P0053 ---- ANEMOLTER             52.30    9.05    39     -6 LAND
99810       P0054 ---- BORNUM AM HARZ        51.55   10.10   170     15 LAND
99811       P0055 ---- ALTOETTING            48.16   12.38   372     42 LAND
99812       P0056 ---- LUPFEN                48.05    8.30   970   -124 LAND
99801       P0057 ---- GROSSER BEERBERG      50.40   10.45   980   -314 LAND
99802       P0058 ---- SANKT GALLENKIRCH     47.02    9.59   750    504 LAND
99803       P0059 ---- MITTAGSSPITZE         47.18    9.53  2097   -752 BERG
99804       P0060 ---- PATSCHERKOFEL         47.13   11.29  2248  -1062 BERG
99805       P0061 ---- HUNDSTEIN             47.22   12.54  2116   -999 BERG
99806       P0062 ---- TRAUNKIRCHEN          47.48   13.48   500    -26 LAND
99807       P0063 ---- ULRICHSBERG           48.41   13.55  1000   -113 LAND
99808       P0064 ---- PLOECKENSTEIN         48.47   13.52  1378   -512 BERG
99809       P0065 ---- GROSSER HOELLENGOGEL  47.45   13.40  2000  -1192 BERG
99810       P0066 ---- TUERNITZ              47.57   15.30   400    -31 LAND
99811       P0067 ---- HOELLENSTEIN/YBBS     47.45   14.45  1000    -35 LAND
99812       P0068 ---- HOCHSCHNEEBERG        47.45   15.50  2000  -1029 BERG
99801       P0069 ---- KAMMSPITZ             47.29   13.51  2141   -593 BERG
99802       P0070 ---- CHATILLON             45.45    7.37   500    738 LAND
99803       P0071 ---- MARGOZZO              45.58    8.27   700   -136 LAND
99804       P0072 ---- MASERA                46.08    8.19   800    110 LAND
99805       P0073 ---- M.ZEDA                46.03    8.32  2100   -403 LAND
99806       P0074 ---- SONDRIO               46.11    9.52   500    767 LAND
99807       P0075 ---- LECCO                 45.51    9.23   400    -25 LAND
99808       P0076 ---- BRIXEN                46.43   11.40   600    606 LAND
99809       P0077 ---- ROLLEPASS             46.18   11.48  1800      4 LAND
99810       P0078 ---- CORTINA D'AMPEZZO     46.33   12.08  1300     74 LAND
99811       P0079 ---- PASO DI FALZAREGO     46.32   12.02  1850    -13 LAND
99812       P0080 ---- ALBERTVILLE           45.40    6.24   500    315 LAND
99801       P0081 ---- LE ROIGNAIS           45.39    6.43  3001   -421 LAND
99802       P0082 ---- CHAMONIX              45.55    6.52  1000    284 LAND
99803       P0083 ---- ANNECY                45.54    6.07   500      1 LAND
99804       P0084 ---- MT. BUET              46.01    6.53  3100   -549 LAND
99805       P0085 ---- CHORGES               44.33    6.16   600    247 LAND
99806       P0086 ---- SERRE CHEVALIER       44.55    6.30  2700   -144 LAND
99807       P0087 ---- DIGNE                 44.05    6.14   700    -40 LAND
99808       P0088 ---- ANNOT                 43.58    6.42   600    422 LAND
99809       P0089 ---- CROIX DE L ALPE       44.24    6.40  2590   -334 LAND
99810       P0091 ---- SIMPLONPASS           46.15    8.03  2000    -38 LAND
99811       P0092 ---- MT. AUBERT            46.53    6.38  1339   -259 LAND
99812       P0093 ---- LILLEHAMMER           61.06   10.27   500    -56 LAND
99802       P0095 ---- TORPO                 60.30    8.15  1000     36 LAND
99803       P0096 ---- FINSE                 60.36    7.30  1500    -70 LAND
99804       P0097 ---- SELJORD               59.30    8.40   300      5 LAND
99805       P0098 ---- LIFJELL               59.15    8.30   800     -5 LAND
99806       P0099 ---- LJUBLJANA             46.04   14.39   400    -12 LAND
99807       P0100 ---- BLED                  46.22   14.07   900    -62 LAND
99808       P0101 ---- OF-POST D1            49.12    8.24   259    -71 LAND
99809       P0102 ---- OF-POST D2            47.54    9.54   576      5 LAND
99810       P0103 ---- OF-POST D3            48.42   12.30   462    -53 LAND
99811       P0104 ---- OF-POST D4            50.24   10.42   441      1 LAND
99812       P0105 ---- OF-POST D5            52.48    8.30    18     23 LAND
99801       P0106 ---- OF-POST D6            51.42    8.00   192     32 LAND
99802       P0107 ---- OF-POST D7            51.18    9.48   317     -2 LAND
99803       P0108 ---- OF-POST D8            53.12   12.12    60     22 LAND
99804       P0109 ---- OF-POST D9            51.36   13.30   115    -11 LAND
99805       P0110 ---- OF-POST H1            49.58    8.48   214    -70 LAND
99806       P0111 ---- OF-POST H2            50.21    8.22   281     10 LAND
99807       P0112 ---- OF-POST H3            50.57    9.06   356    -50 LAND
99808       P0113 ---- OF-POST H4            50.57    9.45   351      0 LAND
99809       P0114 ---- OF-POST H5            50.27    9.12   318     18 LAND
99810       P0115 ---- LOIBLPASS             46.25   14.17  1500   -369 LAND
99811       P0116 ---- NEUERN/NYRSKO         49.18   13.10   600     -4 LAND
99812       P0117 ---- MITTAGSBERG           49.04   13.25  1300   -224 LAND
99801       P0118 ---- PASO DI CAMPELLI      46.01   10.01  1890    -47 LAND
99802       P0119 ---- SCHMOELLN             53.18   14.05    20     25 LAND
99803       P0120 ---- HAMBURG-NEUENG.       53.25   10.14    10     -4 LAND
99804       P0121 ---- WENNIGSEN             52.16    9.39    30     47 LAND
99805       P0122 ---- WIELEN                52.32    6.45    20      9 LAND
99806       P0123 ---- LAUCHA                51.07   14.39   240     -4 LAND
99807       P0124 ---- TIMMENDORF/POEL       53.59   11.23    12     -5 KUES
99808       P0125 ---- KRAGELUND             54.41    9.49    20     -8 LAND
99809       P0126 ---- LINDEWITT             54.43    9.09    20      9 LAND
99810       P0127 ---- SOELLMNITZ            50.57   12.09   311    -29 LAND
99811       P0128 ---- PODELZIG              52.28   14.31    20     24 LAND
99812       P0129 ---- DELITZSCH-SELBEN      51.30   12.23   150    -58 LAND
99801       P0130 ---- KRUMMHOERN-LOQUARD    53.23    7.04    10    -10 LAND
99802       P0131 ---- KAISER-WILH.-KOOG     53.56    8.56     5     -3 LAND
99803       P0132 ---- MESSMAST WHV          53.37    8.03    10     -9 LAND
99804       P0133 ---- MESSMAST OL           53.09    8.03    10     -3 LAND
99805       P0134 ---- MESSMAST EMD          53.23    7.10    10     -9 LAND
99806       P0135 ---- HILKENBROOK, NT       52.59    7.42    15     -3 LAND
99807       P0136 ---- VIENENBURG, MG        51.57   10.36   100      9 LAND
99808       P0137 ---- SYKE-GESSEL, NTB      52.56    8.46    20      6 LAND
99809       P0138 ---- HOHEGING, NT          52.54    8.07    15     23 LAND
99810       P0139 ---- ALTENBEKEN, MG        51.44    8.56   300    -43 LAND
99811       P0140 ---- RAPSHAGEN, NT         53.13   12.14    70     21 LAND
99812       P0141 ---- BASSENS               53.42    7.56     2      0 LAND
99801       P0142 ---- TOSSENS               53.35    8.15     2     -1 KUES
99802       P0143 ---- WYBELSUMER POLDER     53.20    7.06     2     -2 LAND
99803       P0144 ---- SCHUELP               54.14    8.55    20    -16 LAND
99804       P0145 ---- HAMSWEHRUM            53.27    7.10    10     -9 LAND
99805       P0146 ---- PILSUM                53.29    7.20    10     -5 LAND
99806       P0147 ---- ASENDORF              52.45    9.00    40     11 LAND
99807       P0148 ---- MENSLAGE              52.35    7.43    25      6 LAND
99808       P0149 ---- GARLSTORF             53.14   10.00    80    -25 LAND
99809       P0150 ---- ST.PETER-ORDING       54.19    8.41     2     -1 KUES
99810       P0151 ---- HALLIG HOOGE          54.34    8.32     2     -2 KUES
99811       P0152 ---- PLOEN                 54.10   10.23    22     13 LAND
99812       P0153 ---- NORDW. FPN            55.00    6.27     0      0 MEER
99801       P0154 ---- WESTL. SYLT           55.00    7.18     0      0 MEER
99802       P0155 ---- BRUGGE                51.13    3.14     5     -1 LAND
99803       P0157 ---- DIESSEN               47.57   11.06   500    127 LAND
99804       P0158 ---- CHIEMSEE              47.50   12.20   500     46 LAND
99805       P0159 ---- GMUND/TEGERNSEE       47.45   11.45   500     -7 LAND
99806       P0160 ---- STEINBACH             47.50   13.15   500      8 LAND
99807       P0161 ---- HALLSTATT             47.34   13.39   500    308 LAND
99808       P0162 ---- SAN VIGILIO           46.42   11.56  1000    313 LAND
99809       P0163 ---- BELLAGIO              45.59    9.16   200    379 LAND
99810       P0164 ---- DOMASO                46.09    9.21   200    379 LAND
99811       P0165 ---- ISEO                  45.39   10.03   100     -2 LAND
99812       P0166 ---- LA SPEZIA             44.10    9.45     0     84 LAND
99801       P0167 ---- LIVORNO               43.33   10.18     0      2 KUES
99802       P0168 ---- SAN REMO              43.48    7.46     0    284 KUES
99803       P0169 ---- LEUCATE               42.50    3.05     0      8 KUES
99804       P0171 ---- TRIENT                46.06   11.09   194    449 LAND
99805       P0172 ---- MITROVICA             42.54   20.52   521     82 LAND
99806       P0173 ---- GNJILANE              42.28   21.29   500     36 LAND
99807       P0174 ---- LEISENWALD            50.19    9.10   371    -35 LAND
99808       P0175 ---- ROSTOCK-STADT         54.05   12.08     9     18 LAND
99809       P0176 ---- BUERSTADT             49.38    8.27    90      4 LAND
99810       P0177 ---- WALD-MICHELBACH       49.34    8.50   330     46 LAND
99811       P0178 ---- BIEBESHEIM            49.47    8.28    90      0 LAND
99812       P0179 ---- BRENSBACH             49.46    8.51   200     -8 LAND
99801       P0180 ---- GRUENBERG             50.37    8.58   273     23 LAND
99802       P0181 ---- STADTALLENDORF        50.50    9.01   300    -39 LAND
99803       P0182 ---- LAUTERBACH            50.38    9.24   296      9 LAND
99804       P0183 ---- BURGHAUN              50.43    9.43   245     65 LAND
99805       P0184 ---- SCHLENKLENGSFELD      50.50    9.49   310     41 LAND
99806       P0185 ---- BAD EMSTAL            51.15    9.14   370    -42 LAND
99807       P0186 ---- BAD BREISIG           50.31    7.18    53     84 LAND
99808       P0187 ---- BETZDORF              50.47    7.53   186     46 LAND
99809       P0188 ---- PUDERBACH             50.35    7.33   203     -1 LAND
99810       P0189 ---- ST.GOAR               50.09    7.43    80    105 LAND
99811       P0190 ---- NASSAU/RHL.-PFALZ     50.19    7.47    90    161 LAND
99812       P0191 ---- NASTAETTEN            50.12    7.52   268     35 LAND
99801       P0192 ---- GEROLSTEIN            50.13    6.40   358    -16 LAND
99802       P0193 ---- HINTERWEIDENTHAL      49.12    7.45   350     -3 LAND
99803       P0194 ---- FREINSHEIM            49.30    8.13   100     36 LAND
99804       P0195 ---- ROCKENHAUSEN          49.38    7.49   203    -11 LAND
99805       P0196 ---- EISENBERG             49.38    8.05   248    -14 LAND
99806       P0197 ---- WOERTH                49.48    9.09   105     49 LAND
99807       P0198 ---- MIESAU                49.24    7.26   236     46 LAND
99808       P0199 ---- UETERSEN              53.41    9.39     5      1 LAND
99809       P0200 ---- LABOE                 54.24   10.15    34    -19 LAND
99810       P0201 ---- SCHENEFELD            53.36    9.49    10      6 LAND
99811       P0202 ---- GLINDE                53.32   10.13    30     -9 LAND
99812       P0203 ---- WITTINGEN             52.43   10.44    78      3 LAND
99801       P0204 ---- HANNOV.MUENDEN        51.25    9.39   125     84 LAND
99802       P0205 ---- PEINE                 52.19   10.13    67      1 LAND
99803       P0206 ---- AMT NEUHAUS           53.17   10.55    20      3 LAND
99804       P0207 ---- HODENHAGEN            52.46    9.35    25      3 LAND
99805       P0208 ---- LANGWEDEL             52.58    9.12    20     22 LAND
99806       P0209 ---- GLANDORF              52.05    7.59    64     -8 LAND
99807       P0210 ---- DAMME                 52.30    8.08    63     -6 LAND
99808       P0211 ---- LANGWARDEN            53.36    8.19     8     -7 LAND
99809       P0212 ---- PULHEIM               51.00    6.28    46     50 LAND
99810       P0213 ---- KERPEN                50.52    6.40   100      5 LAND
99811       P0214 ---- TROISDORF             50.50    7.10    50      8 LAND
99812       P0215 ---- MECKENHEIM/RHEINB.    50.37    7.02   180     46 LAND
99801       P0216 ---- LINNICH               50.59    6.15    67     28 LAND
99802       P0217 ---- ALDENHOVEN            50.54    6.17    70     25 LAND
99803       P0218 ---- MECHERNICH            50.35    6.39   300    -26 LAND
99804       P0219 ---- WIESDORF              51.00    6.59    45      3 LAND
99805       P0220 ---- OPLADEN               51.01    7.00    57     -9 LAND
99806       P0221 ---- SCHLEBUSCH            51.02    7.04   100    -35 LAND
99807       P0222 ---- RHEINDORF             51.03    6.56    47     18 LAND
99808       P0223 ---- LEICHLINGEN           51.07    7.01   166     28 LAND
99809       P0224 ---- BAESWEILER            50.54    6.11   110     52 LAND
99810       P0225 ---- BERGHEIM              50.55    6.38    70     12 LAND
99811       P0226 ---- BERGISCH GLADBACH     50.59    7.07   162      6 LAND
99812       P0227 ---- KOENIGSWINTER         50.40    7.11    80    -22 LAND
99801       P0228 ---- EITORF                50.46    7.26    89     22 LAND
99802       P0229 ---- REKEN                 51.50    7.02    70     -5 LAND
99803       P0230 ---- ASCHEBERG             51.47    7.37    75     -6 LAND
99804       P0231 ---- HALLE/NORD.WESTFALEN  52.04    8.22   105      7 LAND
99805       P0232 ---- HOLTE-STUKENBROCK     51.54    8.39   130     15 LAND
99806       P0233 ---- BUENDE                52.12    8.35    61     41 LAND
99807       P0234 ---- ERWITTE               51.37    8.20   106    -17 LAND
99808       P0238 ---- LIMASSOL              34.40   33.03    40    146 KUES
99809       P0239 ---- MARBELLA              36.31   -4.53    30     80 KUES
99810       P0240 ---- SAN FELIU             41.45    3.05    10     81 MEER
99811       P0241 ---- SAINT TROPEZ          43.16    6.39    20     38 KUES
99812       P0242 ---- CERNOBBIO             45.50    9.05   400    -12 LAND
99801       P0243 ---- ISCHIA                40.44   13.57    80    -30 KUES
99802       P0244 ---- PORTOFINO             44.18    9.12     5    115 KUES
99803       P0245 ---- MADEIRA/FESTLAND      39.57   -8.02   500     10 LAND
99804       P0246 ---- KARTHAGO              36.54   10.16     3     24 KUES
99805       P0247 ---- WIESENSTEIG           48.32    9.37   756    -20 LAND
99806       P0248 ---- BESIGHEIM             49.00    9.09   202     41 LAND
99807       P0249 ---- SCHORNDORF            48.47    9.31   328      0 LAND
99808       P0250 ---- KRAUTHEIM             49.13    9.22   298    -42 LAND
99809       P0251 ---- SULZBACH-LAUFEN       48.34    9.30   360      9 LAND
99810       P0252 ---- BILLIGHEIM            49.21    9.16   290    -25 LAND
99811       P0253 ---- LOSSBURG              48.43    8.45   347      0 LAND
99812       P0254 ---- KIRCHZARTEN           47.58    7.57   388    156 LAND
99801       P0255 ---- ENDINGEN              48.08    7.42   186      3 LAND
99802       P0256 ---- OTTENHOEFEN           48.20    8.05   311      1 LAND
99803       P0257 ---- SINGEN                47.45    8.49   450      0 LAND
99804       P0258 ---- JESTETTEN             47.39    8.34   470     14 LAND
99805       P0259 ---- TRUCHTELFINGEN        48.14    9.01   475     55 LAND
99806       P0260 ---- ILLERIEDEN-DORNDORF   48.17   10.02   461     42 LAND
99807       P0261 ---- GAMMERTINGEN          48.08    9.07   659    -12 LAND
99808       P0262 ---- WOLFRATSHAUSEN        47.50   11.25   577     47 LAND
99809       P0263 ---- PFAFFENHOFEN          48.18   11.18   428     80 LAND
99810       P0264 ---- BRUCKMUEHL            47.53   11.55   512     -7 LAND
99811       P0265 ---- INNING AM AMMERSEE    48.02   11.05   550     17 LAND
99812       P0266 ---- KUENZING              48.23   13.03   309     34 LAND
99801       P0267 ---- OBERNZENN             49.17   10.16   400     20 LAND
99802       P0268 ---- FISCHACH              48.10   10.23   490      7 LAND
99803       P0269 ---- LAUINGEN              48.20   10.15   439     58 LAND
99804       P0273 ---- HELMBRECHTS           50.14   11.43   617    -40 LAND
99805       P0274 ---- BLIESRANDSBACH        49.10    7.05   250     20 LAND
99806       P0275 ---- HEUSWEILER            49.21    6.57   300     -4 LAND
99807       P0276 ---- PERL                  49.28    6.23   270     15 LAND
99808       P0277 ---- WADERN                49.32    6.53   300     -4 LAND
99809       P0278 ---- NEUNKIRCHEN/SAARLAND  49.12    7.06   224     46 LAND
99810       P0279 ---- SCHMELZ               49.26    6.51   230      6 LAND
99811       P0280 ---- NONNWEILER            49.36    6.39   420    -64 LAND
99812       P0281 ---- BERNAU/BRANDENBURG    52.40   13.34    67      1 LAND
99801       P0282 ---- HERZBERG/BRANDENBURG  51.42   13.14    81      0 LAND
99802       P0283 ---- TREBUS                52.25   14.04    15     51 LAND
99803       P0284 ---- LUEBBENAU             51.52   13.58    51      8 LAND
99804       P0285 ---- LUCKENWALDE           52.10   13.09    40      1 LAND
99805       P0286 ---- SATOW                 53.34   11.30    50     -3 LAND
99806       P0288 ---- MEERANE               50.51   12.27   250      5 LAND
99807       P0289 ---- LAMPERTSWALDE         51.10   13.23   150     50 LAND
99808       P0290 ---- OPPACH                51.04   14.31   350    -50 LAND
99809       P0291 ---- DOEBELN               51.04   13.04   210     35 LAND
99810       P0292 ---- WURZEN                51.22   12.44   124     12 LAND
99811       P0293 ---- POESSNECK             50.40   11.33   250     11 LAND
99812       P0295 ---- NIESKY                51.17   14.51   165     27 LAND
99801       P0297 ---- DINGOLFING            48.45   12.33   360      9 LAND
99802       P0298 ---- ARLBERG               47.08   10.11  1793    150 BERG
99803       P0299 ---- GROSSGLOCKNER         47.05   12.41  3797  -1247 BERG
99804       P0300 ---- DACHSTEIN             47.28   13.36  2995  -1505 BERG
99805       P0301 ---- LICHTENBERG           48.25   14.15   926   -193 BERG
99806       P0302 ---- ZINKEN                47.20   14.45  2331  -1094 BERG
99807       P0303 ---- WEINSBERG             48.24   15.06  1039   -186 BERG
99808       P0304 ---- KAISEREICHE           47.57   16.41   443   -259 LAND
99809       P0305 ---- SONNENBERG            47.53   16.29   484   -114 LAND
99810       P0306 ---- WANK                  47.30   11.08  1770   -593 BERG
99811       P0307 ---- HOERNLE               47.38   11.04  1538   -703 BERG
99812       P0308 ---- BRAUNECK              47.40   11.31  1545   -814 BERG
99801       P0309 ---- HOCHFELLN             47.45   12.33  1665   -788 BERG
99802       P0310 ---- PREDIGTSTUHL          47.42   12.52  1607   -874 BERG
99803       P0311 ---- ANDERMATT             46.38    8.36  1500     51 LAND
99804       P0312 ---- LINTHAL               46.55    9.00  1000    100 LAND
99805       P0314 ---- SAANEN-GSTAAD         46.30    7.16  1100    155 LAND
99804       P0325 ---- ANDORRA               42.33    1.36  1500    -97 LAND
99805       P0326 ---- WELVER                51.37    7.55   114    -37 LAND
99806       P0327 ---- ISERLOHN              51.25    7.41   279    -34 LAND
99807       P0328 ---- SIEDLINGSHAUSEN       51.15    8.28   364     49 LAND
99808       P0329 ---- MARSBERG-POSTWEG      51.26    8.47   445    -88 LAND
99809       P0330 ---- HORN                  51.53    8.57   210     -3 LAND
99810       P0331 ---- GOEHL                 54.17   10.56    19    -10 LAND
99811       P0332 ---- BISDORF               54.28   11.10     9      0 LAND
99812       P0333 ---- KHANIA                35.31   24.01    24     27 KUES
99809       P0346 ---- GETTORF               54.25    9.59    10      9 LAND
99810       P0347 ---- HARRISLEE             54.48    9.23    10     25 LAND
99811       P0348 ---- MALENTE               54.10   10.33    15     31 LAND
99812       P0349 ---- MARNE                 53.57    9.01     5     -3 LAND
99801       P0350 ---- REINFELD              53.50   10.29    15     21 LAND
99802       P0351 ---- SCHOENBERG            54.24   10.22     5     27 LAND
99803       P0352 ---- TRAPPENKAMP           54.02   10.13    70    -27 LAND
99804       P0353 ---- WESSELBUREN           54.13    8.55     5     -1 LAND
99805       P0354 ---- MEISSNER              51.14    9.53   754   -457 BERG
99806       P0355 ---- KLADRUM               53.33   11.47    50     10 LAND
99807       P0356 ---- RAKOW                 54.03   13.02    17     -8 LAND
99808       P0357 ---- RAVENSBERG            53.59   11.42    12     37 LAND
99809       P0358 ---- ABLASS                51.13   12.57   150     50 LAND
99810       P0359 ---- DORNA                 51.46   12.42   106    -27 LAND
99811       P0360 ---- WILLMERSDORF          52.40   13.41    67     11 LAND
99812       P0361 ---- HOCHHEIM              51.01   10.39   321    -17 LAND
99801       P0362 ---- IHLEWITZ              51.38   11.41   159     11 LAND
99802       P0363 ---- NEUENFELD             53.25   14.01    10     40 LAND
99803       P0364 ---- OBHAUSEN              51.23   11.39   190    -40 LAND
99804       P0365 ---- KLETTWITZ             51.32   13.53   103      0 LAND
99805       P0366 ---- REICHENBACH           51.08   14.48   249      8 LAND
99806       P0367 ---- ALPE D'HUEZ           45.05    6.04  1860     10 LAND
99807       P0368 ---- COURCHEVEL            45.24    6.38  1550    -19 LAND
99808       P0369 ---- FLAINE                46.01    6.39  1600     12 LAND
99809       P0370 ---- ISOLA 2000            44.08    7.12  2000    -31 LAND
99810       P0371 ---- MERIBEL               45.22    6.37  1400    -38 LAND
99811       P0372 ---- MORZINE               46.11    6.42  1000      6 LAND
99812       P0373 ---- VAL D'ISERE           45.27    6.59  1850    298 LAND
99801       P0374 ---- AHRNTAL               46.59   11.59   950    653 LAND
99802       P0375 ---- ARABBA                46.30   11.52  1602     57 LAND
99803       P0376 ---- BORMIO 2000           46.26   10.23  1225    411 LAND
99804       P0377 ---- CERVINIA              45.56    7.35  2050    148 LAND
99805       P0378 ---- COURMAYEUR            45.47    6.59  1224     14 LAND
99806       P0379 ---- FOLGARIA              45.55   11.10   900     -4 LAND
99807       P0380 ---- GOSSENSASS            46.56   11.26  1100    482 LAND
99808       P0381 ---- MADONNA DI CAMPIGLIO  46.14   10.49  1500    -43 LAND
99809       P0383 ---- SCHNALSTAL            46.44   10.54  2000     11 LAND
99810       P0384 ---- ST.WALBURG            46.33   11.02  1100    -92 LAND
99811       P0385 ---- DAMUELS               47.16    9.52  1428    -83 LAND
99812       P0386 ---- FILZMOOS              47.26   13.32  1055     -8 LAND
99801       P0387 ---- FULPMES               47.09   11.20   937    223 LAND
99802       P0388 ---- HINTERSEE             47.43   13.17   746     62 LAND
99803       P0389 ---- KAUNERTALER GLETSCH.  47.00   10.47  3000   -493 BERG
99804       P0390 ---- MATREI/OSTTIROL       47.00   12.32  1000    589 LAND
99805       P0391 ---- HOCHSOELDEN           47.04   10.54  1800    -52 LAND
99806       P0392 ---- ST.JAKOB/DEFEREGGEN.  46.54   12.22  1495     49 LAND
99807       P0393 ---- TURRACHER HOEHE       46.54   13.52  1783     -2 LAND
99808       P0394 ---- WAGRAIN               47.20   13.17   830    217 LAND
99809       P0395 ---- WOLFSBERG             46.47   14.59   463    -69 LAND
99811       P0397 ---- BRANAES               60.41   12.56   152    136 LAND
99801       P0399 ---- KLAEPPEN              61.10   13.13   350     81 LAND
99803       P0401 ---- SAEFSEN               60.09   14.25   300      1 LAND
99804       P0402 ---- GRINDELWALD           46.37    8.02  1034    269 LAND
99805       P0403 ---- LENZERHEIDE           46.43    9.33  1500    124 LAND
99806       P0405 ---- REJVIZ                50.13   17.18   770    -24 LAND
99807       P0406 ---- SPINDLERMUEHLE        50.43   15.37   700     30 LAND
99810       P0409 ---- MARSBERG-MEERHOF      51.32    8.50   371    -14 LAND
99811       P0410 ---- BICKENDORF            50.02    6.30   389    -13 LAND
99812       P0411 ---- FLOMBORN              49.42    8.10   180     39 LAND
99801       P0412 ---- SCHEID                50.29    6.30   334     31 LAND
99802       P0413 ---- NIEDER KOSTENZ        49.56    7.22   364      3 LAND
99803       P0414 ---- KEHRIG                50.14    7.13   370     -3 LAND
99804       P0415 ---- WILDPOLDSRIED         47.47   10.26   891      7 LAND
99805       P0416 ---- RIBNITZ-DAMGARTEN     54.16   12.28     7      7 KUES
99806       P0417 ---- KUESTE JASMUND BODD.  54.30   13.30     3     16 KUES
99808       P0422 ---- SPAIN_NEW_01          38.50   -6.31   319     12 LAND
99809       P0423 ---- SPAIN_NEW_02          43.15   -4.35   758     70 LAND
99810       P0424 ---- SPAIN_NEW_03          43.31   -5.53   178     14 LAND
99811       P0425 ---- SPAIN_NEW_04          40.30   -6.30   920     14 LAND
99812       P0426 ---- SPAIN_NEW_05          39.30   -5.25   698      6 LAND
99801       P0427 ---- SPAIN_NEW_06          42.50   -1.38   596     35 LAND
99802       P0428 ---- SPAIN_NEW_07          38.50   -2.00   853     12 LAND
99803       P0429 ---- SPAIN_NEW_08          42.41   -6.28   806     33 LAND
99804       P0430 ---- BLIESDORF             52.41   14.10     5     38 LAND
99805       P0431 ---- WERBIG                51.56   13.12   110     -4 LAND
99806       P0432 ---- ROSSAU                51.00   13.06   320     20 LAND
99807       P0433 ---- GROSSMACKENSTEDT      52.59    8.39    13     13 LAND
99808       P0434 ---- HASELUENNE KNN        52.43    7.32    26     -5 LAND
99809       P0435 ---- GRUEPPENBUEHREN       53.04    8.33    33    -26 LAND
99810       P0436 ---- ARRAS                 50.16    2.46    89    -10 LAND
99811       P0437 ---- CALAIS                50.57    1.49     3     -1 KUES
99812       P0439 ---- FINO1/PLATTFORM       54.05    6.35    10    -10 MEER
99801       P0441 ---- LENGERICH             52.11    7.52    80      0 LAND
99802       P0442 ---- TEGELBERG             47.34   10.47  1720   -865 BERG
99803       P0443 ---- PLATTERHOF            47.38   13.03   954    -41 LAND
99804       P0444 ---- SCHOTTMALHORN         47.37   12.50  2042   -943 BERG
99805       P0445 ---- FRANKFURT/ZEIL        50.06    8.41   100     11 LAND
99806       P0446 ---- ESSEN/BAHNHOF         51.27    7.01    72     49 LAND
99807       P0447 LFMQ LE CASTELLET          43.16    5.47   424    -21 LAND
99808       P0448 LTFJ SABIHA GOKCEN INTL.   40.54   29.19    95      3 KUES
99809       P0449 LIQS AMPUGNANO             43.15   11.15   194      7 LAND
99810       P0450 ---- KISA                  58.06   15.48   132     -1 LAND
99811       P0451 ---- GOETA KANAL           58.36   15.54    74    -41 LAND
99812       P0452 ---- VAETTERN              58.18   14.36   111     -6 LAND
99801       P0453 ---- HJAELMAREN            59.12   15.42    39     -1 LAND
99802       P0454 ---- KATRINEHOLM           59.06   16.30    61    -17 LAND
99803       P0455 ---- MALAEREN              59.24   17.12    35    -20 LAND
99804       P0456 ---- NORR MALAEREN         59.54   17.42    42    -21 LAND
99805       P0457 ---- DALAELVEN             60.24   17.00    69    -20 LAND
99806       P0458 ---- NORR HJAELMAREN       59.42   16.06    79     -6 LAND
99807       P0459 ---- SKYLLBERG             58.54   15.18   100     11 LAND
99808       P0460 ---- SMALAND               57.24   15.06   235    -22 LAND
99809       P0461 ---- BORAS                 57.30   13.36   219     -8 LAND
99810       P0462 ---- ALLEBERG              58.12   13.30   171     35 LAND
99811       P0463 ---- TOERREBODA            58.48   14.24   126    -12 LAND
99812       P0464 ---- VAENNERN              58.54   13.12    83    -27 LAND
99801       P0465 ---- DEGERFORS             59.36   14.30   196     20 LAND
99802       P0466 ---- BERGSLAGEN            60.00   15.12   217     44 LAND
99803       P0467 ---- TIOMILASKOGEN         60.18   13.24   336    -36 LAND
99804       P0468 ---- BORLAENGE             60.30   15.54   185     39 LAND
99805       P0469 ---- GAESTRIKLAND          61.00   16.00   290     -1 LAND
99806       P0470 ---- SILJAN                60.54   14.48   205    -17 LAND
99807       P0471 ---- DALARNA               60.54   14.06   382     -2 LAND
99808       P0472 ---- NORRA DALARNA         61.18   14.42   452     15 LAND
99809       P0473 ---- AESNEN                56.36   14.48   160    -20 LAND
99810       P0474 ---- BOLMEN                56.54   13.24   168      1 LAND
99811       P0475 ---- NORRA SKANE           56.06   13.36   131    -11 LAND
99812       P0476 ---- WITTIGHAUSEN          49.38    9.50   270     33 LAND
99801       P0477 ---- ENERTRAG              53.16   14.02   100    -55 LAND
99802       P0478 EGLC LONDON/CITY INTL      51.29   -0.03     5     27 LAND
99805       P0481 ---- WITTEN                51.26    7.20   104      4 LAND
99806       P0482 ---- OLBERNHAU             50.39   13.20   460     -1 LAND
99807       P0483 ---- ROSSKOPF              48.00    7.54   737   -193 BERG
99808       P0484 ---- HOLZSCHLAEGERMATTE    47.55    7.53  1000    -38 BERG
99811       P0487 ---- SDL.FLUSS LITANI      33.08   35.24   800    -65 LAND
99812       P0488 ---- BERGSTEDT             53.40   10.07    26     -5 LAND
99801       P0489 ---- HAMBURG INNENSTADT    53.33    9.59     8     13 LAND
99802       P0490 ---- HUERTH                50.53    6.52    60     18 LAND
99803       P0491 ---- HATTINGEN             51.24    7.11   150    -42 LAND
99804       P0492 ---- VILLARD DE LANS       45.04    5.33  1050    174 BERG
99805       P0493 ---- ALAGNA                45.50    7.56  1150    792 BERG
99806       P0494 ---- ZINAL                 46.07    7.38  1670   1125 BERG
99807       P0495 ---- CHAMPERY              46.11    6.53  1050    656 BERG
99808       P0496 ---- FIESCH                46.24    8.08  1050   1024 BERG
99809       P0497 ---- MELCHSEE-FRUTT        46.46    8.16  1920    347 BERG
99810       P0498 ---- MAURACH               47.25   11.45   930    270 BERG
99811       P0499 ---- SEDRUN                46.41    8.46  1400    784 BERG
99812       P0500 ---- BERTIKOW              53.18   14.01    74    -22 LAND
99801       P0501 ---- LANGEN-TRECHOW        53.54   11.56    25      2 LAND
99802       P0502 ---- HOHEN PRITZ           53.38   11.54    65     -9 LAND
99803       P0503 ---- WERDER                53.30   12.00    59     -1 LAND
99804       P0504 ---- BERSTELAND-NIEWITZ    51.56   13.47    53      2 LAND
99805       P0505 ---- MORBACH               49.49    7.07   428     -2 LAND
99806       P0506 ---- LUENNE                52.25    7.26    36     -3 LAND
99807       P0507 ---- HEIDEN                51.49    6.57    70     -8 LAND
99808       P0508 ---- BERGLICHT             49.47    6.58   401     63 LAND
99809       P0509 ---- SASSENBERG            51.59    8.03    60      0 LAND
99810       P0510 ---- SCHELKLINGEN          48.28    9.43   750    -14 LAND
99811       P0511 ---- SCHEID_2              50.20    6.25   560     13 LAND
99812       P0512 ---- HAARSTRANG            51.31    8.14   250    -45 LAND
99801       P0513 ---- NEUKIRCHEN            51.04   10.20   227     53 LAND
99802       P0514 ---- RAUSCHWITZ            51.00   11.46   318    -58 LAND
99803       P0515 ---- SCHILBACH             50.30   11.52   539      5 LAND
99804       P0516 ---- SCHOENEWALDE          52.01   12.49   148    -15 LAND
99806       P0518 ---- RAGUSA                36.55   14.43   507     17 LAND
99809       P0521 ---- LOVIISA               60.27   26.13     1      8 KUES
99811       P0523 LFBU BRIE-CHAMPNIERS       45.43    0.13   122    -15 LAND
99812       P0524 ---- TONNAY CHARENTE       45.56   -0.53    14     -6 KUES
99801       P0525 ---- GAETA                 41.12   13.34     1    186 KUES
99803       P0527 ---- SAN CARLOS D.RAPITA   40.37    0.35     1     37 KUES
99805       P0529 ---- TREGUIER              48.47   -3.14    41     -7 KUES
99807       P0531 ---- PORTO EMPEDOCLE       37.17   13.32     7    126 KUES
99808       P0532 ---- GARCHING              48.16   11.41   463     21 LAND
99809       P0533 ---- GUNDREMMINGEN         48.31   10.24   433     15 LAND
99810       P0534 ---- ESSENBACH             48.36   12.18   392     38 LAND
99811       P0535 ---- IMATRA                61.10   28.45    67      8 LAND
99812       P0536 ---- MALLAIG               57.00   -5.50    19     60 KUES
99801       P0537 ---- PORTREE               57.25   -6.11    14    126 KUES
99802       P0538 ---- ULLAPOOL              57.54   -5.10    14     49 KUES
99804       P0540 ---- GALLIPOLI             40.04   17.59    12     26 KUES
99805       P0541 ---- PORTO AZZURRO         42.46   10.24    12     58 KUES
99807       P0543 ---- UUSIKAUPUNKI          60.48   21.25    10     -4 KUES
99808       P0544 ---- BEAUVAIS              49.01   -1.11   111    -13 LAND
99809       P0545 ---- ASTI                  44.54    8.13   122     54 LAND
99810       P0546 ---- EGERSUND              58.27    6.01    27     87 KUES
99811       P0547 ---- ADRA                  36.45   -3.01     8    323 KUES
99812       P0548 ---- BANBURY               52.04   -1.20   107     16 LAND
99801       P0549 ---- BLACKBURN             53.45   -2.29   123     11 LAND
99802       P0550 ---- LA CIOTAT             43.10    5.36     3     35 KUES
99803       P0551 ---- LA PALMA              37.23   -6.33    95     15 LAND
99804       P0552 ---- MELILLI               37.11   15.08   278     63 LAND
99805       P0553 ---- VIVERO                42.53   -6.14  1389      8 LAND
99806       P0554 ---- COSENZA               39.18   16.15   243     74 LAND
99807       P0555 ---- SASSARI               40.44    8.34   203    -82 LAND
99808       P0556 ---- GUARDA                40.32   -7.16  1014   -139 LAND
99809       P0557 ---- LINARES               38.05   -3.38   411     -4 LAND
99811       P0559 ---- OBER-BEERBACH         49.46    8.41   340    -49 LAND
99812       P0560 ---- ERFURT-STADT          50.59   11.02   200     -2 LAND
99801       P0561 ---- HAMBACH               50.24    7.59   260    -56 LAND
99803       P0563 EGGW LONDON LUTON          51.52    0.22   160    -85 LAND
99804       P0564 EGNX EAST MIDLANDS         52.49   -1.20    93    -32 LAND
99807       P0567 UUWW MOSKVA/VNUKOVO        56.00   37.17   203    -10 LAND
99810       P0570 LFRV VANNES MEUCON         47.43   -2.44   134    -54 LAND
99811       P0571 LGAV ATHINAI-ELEFTHERIOS   37.56   23.56    94     25 KUES
99812       P0572 EEEI AMARI                 59.16   24.13    20      7 LAND
99801       P0573 EEKE KURESSAARE            58.14   22.31     2      2 KUES
99804       P0576 ---- BLANKENBURG / HARZ    51.49   10.57   220     72 LAND
99805       P0577 ---- BLEICHERODE           51.26   10.36   270    -14 LAND
99806       P0578 ---- HERMSDORF / THUER.    50.53   11.51   345    -51 LAND
99807       P0600 ---- VELBERT               51.20    7.03   249     -6 LAND
99808       P0601 ---- WEGBERG               51.09    6.17    68      3 LAND
99809       P0602 ---- GLADBECK              51.35    6.58    64    -12 LAND
99810       P0603 ---- CALW                  48.43    8.45   418     16 LAND
99811       P0604 ---- HAGEN-HOHENLIMBURG    51.21    7.34   131     18 LAND
99812       P0605 ---- ENNEPETALSPERRE       51.14    7.25   309     52 LAND
99801       P0606 ---- SCHMALLENBERG         51.09    8.17   381      0 LAND
99802       P0607 ---- MARSBERG              51.27    8.51   250    -31 LAND
99803       P0608 ---- LANGENAU              48.30   10.07   461      1 LAND
99804       P0609 ---- HARDHEIM              49.37    9.29   271     59 LAND
99805       P0610 ---- WRIEZEN               52.43   14.08    35     11 LAND
99811       P0616 ---- SUEDLOHN              51.57    6.54    52     -3 LAND
99812       P0617 ---- WETTRINGEN            52.13    7.21    48      8 LAND
99801       P0618 ---- HAFTENKAMP            52.32    6.55    17      2 LAND
99802       P0619 ---- ENNIGERLOH            51.51    8.02   104    -24 LAND
99803       P0620 ---- SCHWARTENBERG         52.50    7.06    13      0 LAND
99804       P0621 ---- BERDEL                51.57    7.47    60     -6 LAND
99805       P0622 ---- FREREN                52.29    7.32    37      2 LAND
99806       P0624 ---- SCHIRL                52.01    7.53    55      1 LAND
99807       P0625 ---- DOERENTHE             52.13    7.39    45      1 LAND
99808       P0626 ---- RIESENBECK            52.14    7.36    44      1 LAND
99809       P0627 ---- BEVERGERN             52.16    7.36    45     -5 LAND
99810       P0628 ---- MAEKEL                52.41    8.29    35      4 LAND
99811       P0629 ---- TEMMING               52.01    7.25    72     10 LAND
99812       P0630 ---- HOHENHOLTE            52.00    7.27    70     12 LAND
99801       P0631 ---- OSTBEVERN             52.03    7.51    55      1 LAND
99802       P0632 ---- OSTBEVERN/BROCK       52.04    7.54    55      1 LAND
99803       P0633 ---- OSTBEVERN/UEBERWAS.   52.01    7.51    55      1 LAND
99804       P0634 ---- BOHMTE                52.23    8.18    45      0 LAND
99805       P0635 ---- LEMFOERDE             52.29    8.23    40      7 LAND
99806       P0636 ---- LENGERICH             52.34    7.32    26     13 LAND
99807       P0637 ---- MERZEN                52.28    7.46    52     -5 LAND
99808       P0638 ---- NEUENKIRCHEN          52.23    7.52    54     16 LAND
99809       P0639 ---- TWIST                 52.38    7.07    20     -2 LAND
99810       P0640 ---- NORDHORN              52.29    7.03    20      1 LAND
99812       P0642 ---- BUTENDI1              55.01    7.46     0      0 LAND
99801       P0643 ---- GODEWIN1              54.03    7.02     0      0 MEER
99802       P0644 ---- GODEWIN2              54.03    7.02     0      0 MEER
99803       P0645 ---- NORDONE1              53.59    6.49     0      0 MEER
99804       P0646 ---- SANDBAN1              55.11    6.52     0      0 MEER
99805       P0647 ---- NORGRUE1              53.50    8.10     0      0 MEER
99806       P0648 ---- VEJAMAT1              54.19    5.52     0      0 MEER
99807       P0649 ---- WIKINGR1              54.50   14.04     0      0 MEER
99812       W3011 ---- WESTL.AGADIR          29.56  -11.27     0      0 MEER
99802       W3212 ---- CANARIS-E             32.00  -12.00     0      0 MEER
99803       W3409 ---- CANARIS-NE            34.00   -9.00     0      0 MEER
99805       W3602 ---- ALBORAN               36.02   -2.16     0      0 MEER
99806       W3604 ---- ALBORAN-W             35.45   -4.15     0      0 MEER
99807       W3607 ---- WESTL.GIBR.           36.00   -6.37     0      0 MEER
99808       W3609 ---- CABO S.VICENTE        36.29   -9.00     0      0 MEER
99809       W3701 ---- SDL.CARTAGENA         37.00   -1.15     0      0 MEER
99810       W3811 ---- WESTL.LISSABON        38.01  -11.20     0      0 MEER
99811       W4010 ---- WESTL.PORT.           39.33  -10.25     0      0 MEER
99812       W4211 ---- SDL.FINISTERRE        41.32  -10.52     0      0 MEER
99805       W4402 ---- GOLF BIARRITZ         44.00   -2.12     0      0 MEER
99806       W4410 ---- FINISTERRE            43.31   -9.49     0      0 MEER
99807       W4504 ---- SUDGASCOGNE           45.00   -3.31     0      0 MEER
99808       W4505 ---- NDL.GIJON             44.36   -5.08     0      0 MEER
99809       W4606 ---- BISKAYA               46.22   -5.41     0      0 MEER
99811       W4703 ---- NORDGASCOGNE          46.37   -3.24     0      0 MEER
99802       W4807 ---- SOLE                  48.00   -7.00     0      0 MEER
99805       W5001 ---- ENGL.KAN.-E           49.58   -1.13     0      0 MEER
99806       W5003 ---- LYME BAY              50.15   -3.00     0      0 MEER
99807       W5004 ---- ENGL.KAN.-W           49.34   -4.04     0      0 MEER
99808       W5011 ---- FASTNET               50.27  -10.33     0      0 MEER
99809       W5105 ---- LUNDY                 51.29   -4.31     0      0 MEER
99810       W5108 ---- SUEDL.IRL.            50.52   -7.44     0      0 MEER
99801       W5306 ---- IRISCHE SEE           53.15   -5.38     0      0 MEER
99806       W5501 ---- TYNE                  55.00   -0.45     0      0 MEER
99807       W5506 ---- NORTH CHANNEL         55.15   -5.31     0      0 MEER
99808       W5602 ---- FORTH                 56.29   -1.31     0      0 MEER
99809       W5607 ---- INISHTRAHULL          55.36   -7.00     0      0 MEER
99810       W5611 ---- NWL.IRLAND            55.56  -10.53     0      0 MEER
99812       W5708 ---- SDL.HEBRIDEN          56.31   -7.50     0      0 MEER
99805       W5802 ---- CROMARTY              58.12   -2.00     0      0 MEER
99806       W5808 ---- HEBRIDEN              57.56   -8.09     0      0 MEER
99810       W5906 ---- NDL.HEBRIDEN          58.44   -5.35     0      0 MEER
99812       W6003 ---- PENTLANDS             59.41   -3.07     0      0 MEER
99801       W6006 ---- FAROER                60.25   -5.34     0      0 MEER
99802       W6010 ---- 60NORD10WEST          59.53  -10.02     0      0 MEER
99806       W6102 ---- SHETLANDS             60.53   -1.35     0      0 MEER
99803       E2935 ---- GOLF AKABA-N          29.15   34.50     0      8 MEER
99804       E3231 ---- PORT-SAID             32.02   31.13     0      0 MEER
99805       E3234 ---- ISRAEL                31.51   34.16     0      0 MEER
99806       E3328 ---- SE-KRITIKO            33.00   27.31     0      0 MEER
99807       E3331 ---- DELTA                 33.07   31.21     0      0 MEER
99808       E3420 ---- SW-KRITIKO            34.10   20.20     0      0 MEER
99809       E3424 ---- SUEDL.KRETA           34.02   23.40     0      0 MEER
99810       E3512 ---- OESTL.DJERBA          35.00   11.30     0      0 MEER
99811       E3514 ---- MELITA-SE             35.00   13.30     0      0 MEER
99812       E3517 ---- SIDRA                 34.37   16.41     0      0 MEER
99801       E3519 ---- OESTL.TUNIS           34.51   18.41     0      0 MEER
99802       E3526 ---- KRETA-SE              34.35   26.10     0      0 MEER
99803       E3530 ---- RHODOS/ZYP.           34.58   30.25     0      0 MEER
99804       E3534 ---- CRUSADE-N             35.17   34.28     0      0 MEER
99805       E3613 ---- TUNIS                 36.11   12.34     0      0 MEER
99806       E3623 ---- KITHIRASEE            35.42   22.31     0      0 MEER
99807       E3624 ---- WEST CRETAN           36.00   24.29     0      0 MEER
99808       E3625 ---- AEGAEIS-S.            36.16   25.27     0     24 MEER
99809       E3627 ---- KARPATHIO             36.02   26.41     0      0 MEER
99810       E3629 ---- KASTELORIZO           35.34   28.30     0      0 MEER
99811       E3631 ---- TAURUS-W              36.29   30.56     0      0 MEER
99812       E3634 ---- TAURUS-E              36.00   34.00     0      0 MEER
99801       E3700 ---- PALOS                 37.00    0.00     0      0 MEER
99802       E3701 ---- CABRERA-W             37.28    1.14     0      0 MEER
99803       E3703 ---- ALGER-W               37.15    3.15     0      0 MEER
99804       E3712 ---- PANTELLERIA           37.00   12.00     0      0 MEER
99805       E3719 ---- ION.MEER              37.22   19.10     0      0 MEER
99806       E3721 ---- S-IONIANSEA           37.10   21.02     0      0 MEER
99807       E3724 ---- AEGAEIS-SW.           37.00   24.00     0      0 MEER
99808       E3727 ---- KOS                   37.00   27.00     0      0 MEER
99809       E3803 ---- CABRERA               38.29    3.00     0      0 MEER
99810       E3805 ---- ALGIER                37.47    4.59     0      0 MEER
99811       E3807 ---- ANNABA                37.57    7.10     0      0 MEER
99812       E3809 ---- SUEDL.SARD.           37.57    9.22     0      0 MEER
99801       E3811 ---- TUNISIE-E             38.00   11.10     0      0 MEER
99802       E3817 ---- BOOT-S                37.39   17.08     0      0 MEER
99803       E3825 ---- CENTRAL AEGEAN        38.00   25.00     0      0 MEER
99804       E3826 ---- SAMOSSEE              37.54   26.12     0      0 MEER
99805       E3901 ---- BALEARES-SW           39.01    0.56     0      0 MEER
99806       E3904 ---- BALEAREN              39.26    3.40     0      0 MEER
99807       E3905 ---- CABRERA-E             39.24    5.01     0      0 MEER
99808       E3915 ---- LIPARI-SE             38.31   15.00     0      3 MEER
99809       E3918 ---- BOOT                  38.48   18.00     0      0 MEER
99810       E3920 ---- ION.MEER-N.           39.00   19.31     0      0 MEER
99811       E3925 ---- AEGAEIS-N.            39.00   25.16     0      0 MEER
99812       E4007 ---- SARDAIGNE-S           39.31    7.29     0      0 MEER
99801       E4011 ---- CARBONARA             39.34   11.13     0      0 MEER
99802       E4013 ---- CIRCEO-S              40.15   13.00     0      0 MEER
99803       E4014 ---- LIPARI                39.31   14.00     0      0 MEER
99804       E4023 ---- AEGAEIS-NW.           39.45   23.00     0      0 MEER
99805       E4026 ---- THRAKICO              40.15   26.00     0      0 MEER
99806       E4028 ---- MARMARA               40.29   28.29     0      0 MEER
99807       E4103 ---- BALEARES-NE           40.48    2.43     0      0 MEER
99808       E4104 ---- MINORQUE              40.31    4.00     0      0 MEER
99809       E4107 ---- WESTL.KOR/S           41.25    6.57     0      0 MEER
99810       E4111 ---- TYRRH.MEER            41.28   10.31     0      0 MEER
99811       E4119 ---- STR.OTRANTO           40.45   19.00     0      0 MEER
99812       E4204 ---- GOLFE-LION            42.10    4.28     0      0 MEER
99801       E4208 ---- CORSE                 41.31    8.15     0      0 MEER
99802       E4212 ---- CIRCEO-N              41.31   12.00     0      0 MEER
99803       E4216 ---- NDL.BARI              42.00   16.29     0      0 MEER
99804       E4218 ---- ADRIA-SUED            41.58   17.46     0      0 MEER
99805       E4229 ---- SCHW.MEER1            41.52   28.51     0      0 MEER
99806       E4236 ---- SCHW.MEER7            42.00   36.00     0      0 MEER
99807       E4304 ---- LION                  42.31    3.45     0      0 MEER
99808       E4307 ---- SDL.PROVENCE          42.45    6.31     0      0 MEER
99809       E4309 ---- LIGUR.MEER            43.16    9.17     0      0 MEER
99810       E4310 ---- ELBA                  42.45   10.00     0      0 MEER
99811       E4316 ---- ZENTR.ADRIA           43.00   15.31     0      0 MEER
99812       E4329 ---- SCHW.MEER2            42.43   29.14     0      0 MEER
99801       E4413 ---- ADRIA-NORD            44.07   13.05     0      0 MEER
99802       E4414 ---- OESTL.ANCONA          43.30   14.12     0      0 MEER
99803       E4430 ---- SCHW.MEER3            43.34   29.39     0      0 MEER
99804       E4435 ---- SCHW.MEER6            43.51   35.15     0      0 MEER
99805       E4513 ---- GOLF-VENEDIG          45.00   13.00     0      0 MEER
99806       E4514 ---- SDL.PULA              44.31   14.00     0      0 MEER
99807       E4515 ---- RAB                   44.36   14.30     0      1 MEER
99808       E4531 ---- SCHW.MEER4            45.16   30.32     0      0 MEER
99809       E4637 ---- SCHW.MEER5            46.19   36.58     0      0 MEER
99810       E5000 ---- STR.DOVER             50.29    0.29     0      0 MEER
99811       E5101 ---- THEMSE                51.14    1.29     0      4 MEER
99812       E5203 ---- RHEINMUENDG.          52.00    3.00     0      0 MEER
99801       E5204 ---- IJMUIDEN              52.31    3.31     0      0 MEER
99802       E5303 ---- HUMBER                53.16    2.36     0      0 MEER
99803       E5304 ---- NORDSEE1              53.49    4.33     0      0 MEER
99804       E5305 ---- IJSSELMEER            52.42    5.24     0      0 MEER
99805       E5307 ---- OSTFR. KUESTE         53.45    7.00     0      0 MEER
99806       E5311 ---- LUEB. BUCHT           54.06   11.12     0      0 MEER
99807       E5312 ---- NDL.POEL              54.15   11.45     0      0 MEER
99808       E5344 ---- BALTRUM               53.44    7.23     0      0 MEER
99809       E5401 ---- HUMBER-W              53.31    1.00     0      0 MEER
99810       E5403 ---- DOGGER-SUED           54.00    3.00     0      0 MEER
99811       E5404 ---- NORDSEE2              54.35    4.18     0      0 MEER
99812       E5405 ---- WESTFR.KUESTE         53.50    5.15     0      0 MEER
99801       E5406 ---- DT.BUCHT              54.26    5.42     0      0 MEER
99802       E5407 ---- POS.FPN               54.29    7.22     0      0 MEER
99803       E5408 ---- WANGEROOGE            53.56    7.46     0      0 MEER
99804       E5409 ---- ELBEMUENDUNG          54.00    8.06     0      0 MEER
99805       E5411 ---- KIELER BUCHT          54.31   10.43     0      0 MEER
99806       E5412 ---- WESTL.OSTS.           54.29   12.23     0      0 MEER
99807       E5413 ---- WESTL.RUEGEN          54.34   13.00     0      0 MEER
99808       E5414 ---- BODDENGEW. OST        54.18   14.00     0      0 MEER
99809       E5416 ---- SUEDL.OSTS.           54.22   15.43     0      0 MEER
99810       E5502 ---- DOGGER                55.11    2.10     0      0 MEER
99811       E5504 ---- ENTENSCHN.            55.19    3.52     0      0 MEER
99812       E5506 ---- NORDSEE3              55.30    5.58     0      0 MEER
99801       E5507 ---- NORDW.SYLT            55.28    7.17     0      0 MEER
99802       E5508 ---- NORDFR.KUE.           54.42    8.00     0      0 MEER
99803       E5510 ---- FLENSB.FOER.          54.48   10.12     0      0 MEER
99804       E5511 ---- BELTE/SUND            55.30   10.44     0      0 MEER
99805       E5512 ---- FEHMARNBELT           54.36   11.18     0      0 MEER
99806       E5513 ---- NDL.RUEGEN            55.00   13.24     0      0 MEER
99807       E5517 ---- OESTL.BORNHOLM        55.29   16.31     0      0 MEER
99808       E5519 ---- NDL.DANZIG            55.12   19.00     0      0 MEER
99809       E5543 ---- ISET-MEER22           54.37   12.38     0      0 MEER
99810       E5606 ---- FISCHER-SUED          56.29    6.15     0      0 MEER
99811       E5611 ---- KATTEGAT              56.29   10.46     0      6 MEER
99812       E5612 ---- NDL.MOEN              55.12   12.45     0      0 MEER
99801       E5613 ---- KATTEGAT-S            56.00   11.42     0      0 MEER
99802       E5614 ---- HANOE-BUCHT-W         55.30   14.29     0      0 MEER
99803       E5615 ---- NDL.BORNHOLM          55.45   15.15     0      0 MEER
99804       E5616 ---- KALMAR-SUND-S         56.12   16.12     0      0 MEER
99805       E5618 ---- SE-OSTSEE             56.11   17.50     0      0 MEER
99806       E5620 ---- WESTL.KLAIPEDA        56.00   20.00     0      0 MEER
99807       E5702 ---- FORTIES               57.08    1.40     0      0 MEER
99808       E5705 ---- FISCHER               57.22    5.17     0      0 MEER
99809       E5709 ---- SKAGERRAK             57.28    8.57     0      0 MEER
99810       E5711 ---- KATTTEGAT-N           57.15   11.29     0      0 MEER
99811       E5805 ---- UTSIRA-SUED           58.21    5.08     0      0 MEER
99812       E5807 ---- KAP LINDESNES         58.00    6.42     0      5 MEER
99801       E5810 ---- NWL.SKAGEN            58.12   10.00     0      0 MEER
99802       E5811 ---- SKAGERRAK-E           58.00   11.00     0      0 MEER
99803       E5818 ---- WESTL.GOTLAND         57.31   17.31     0      0 MEER
99804       E5820 ---- ZENTR.OSTS.           57.58   20.11     0      0 MEER
99805       E5824 ---- RIGAI.MEERB.          57.45   23.30     0      0 MEER
99806       E5902 ---- VIKING-S              58.45    1.31     0      0 MEER
99807       E5910 ---- OSLOFJORD             58.45   10.29     0      0 MEER
99808       E5917 ---- SDL.STOCKHOLM         58.30   17.29     0      0 MEER
99809       E5919 ---- OESTL.STOCKHOLM       59.00   19.00     0      0 MEER
99810       E5922 ---- WESTL.OESEL           58.45   21.31     0      0 MEER
99811       E6001 ---- VIKING                60.05    0.47     0      0 MEER
99812       E6005 ---- UTSIRA-NORD           60.20    4.47     0      0 MEER
99801       E6019 ---- SDL.ALAND             59.42   17.18     0     25 MEER
99802       E6021 ---- NOERDL.OSTS.          59.56   20.54     0      1 MEER
99803       E6024 ---- FINN.MEERB.-W         59.36   24.00     0      0 MEER
99804       E6026 ---- FINN.MEERB.           60.00   26.00     0      0 MEER
99805       E6104 ---- UTVAR                 61.00    4.00     0      0 MEER
99806       E6118 ---- BOTTENSEE-SW          61.00   17.36     0      0 MEER
99807       E6120 ---- ALANDSEE              60.45   19.31     0      0 MEER
99808       E6131 ---- LADOGA SEE            61.00   31.30     0      1 MEER
99810       E7708 ---- GLOBAL1               54.30    6.22     0      0 MEER
99801       A338  ---- BREKENDORFER MOOR     54.25    9.36    25    -10 LAND
99802       A492  ---- OLDENBURG I.H.        54.16   10.53     0      9 LAND
99803       A512  ---- HEIDE                 54.10    9.04     9     -5 LAND
99804       A652  ---- PADENSTEDT            54.02    9.55    15     11 LAND
99805       B335  ---- KAVELSDORF            54.00   12.13    40    -16 LAND
99806       B742  ---- LINSTOW               53.37   12.23    62     -1 LAND
99807       C316  ---- MARMSTORF             53.26    9.56    75    -29 LAND
99808       E136  ---- ZETEL                 53.27    8.01     3     -1 LAND
99809       E267  ---- BOCKEL                53.12    9.18    26      4 LAND
99810       E427  ---- AHLHORN               52.54    8.10    40     -2 LAND
99811       E460  ---- VORM WITZENBRUCH      52.59    9.54    73      3 LAND
99812       E482  ---- HOHENZETHEN           53.03   10.50    79    -13 LAND
99801       E653  ---- WIETZEN               52.43    9.05    55    -21 LAND
99802       E726  ---- NEMDEN                52.13    8.12   130     -4 LAND
99803       E735  ---- HATTENDORF            52.14    9.16   200    -22 LAND
99804       E777  ---- WATENSTEDT            52.09   10.22   103    -11 LAND
99805       E877  ---- CLAUSTHAL-ZELLERFELD  51.47   10.21   585    -23 LAND
99806       E885  ---- WESTERODE             51.54   10.33   205    -45 LAND
99807       E923  ---- SCHLOCHAU             51.43    9.56   145     39 LAND
99808       E972  ---- MOLLENFELDE           51.25    9.51   265     -2 LAND
99809       F136  ---- KARSTEDTSHOF          53.06   12.29    70     -9 LAND
99810       F283  ---- JOACHIMSTHAL          52.57   13.49    70     -1 LAND
99811       F461  ---- RUEDERSDORF           52.28   13.46    50      7 LAND
99812       F537  ---- FAHLHORST             52.18   13.11    35      6 LAND
99801       F618  ---- FLAEMING              52.02   12.36   110     23 LAND
99802       F863  ---- HAENCHEN              51.43   14.16    69     22 LAND
99803       F945  ---- RUHLAND               51.28   13.52   110     -7 LAND
99804       H069  ---- LADBERGEN             52.07    7.42    55     -9 LAND
99805       H075  ---- HABICHTSWALD          52.14    7.52   130     -4 LAND
99806       H097  ---- STEINEGGE-EXTER       52.09    8.48   201      6 LAND
99807       H228  ---- KALTENBACH            51.47    6.58    64     -2 LAND
99808       H267  ---- BECKUMER BERG         51.47    8.03   142    -36 LAND
99809       H308  ---- SONSBECK              51.36    6.21    25      2 LAND
99810       H379  ---- LOHME-ALME            51.38    8.44   163     19 LAND
99811       H423  ---- ALTENESSEN            51.30    6.58    46     14 LAND
99812       H456  ---- OSTOENNER BACH        51.32    7.59   135    -17 LAND
99801       H483  ---- OTTENSGRUND           51.34    8.45   350    -47 LAND
99802       H528  ---- HOLZBUETTGEN          51.13    6.39    39      0 LAND
99803       H545  ---- OBERBARMEN            51.19    7.16   299    -25 LAND
99804       H554  ---- NAHMER                51.19    7.34   360      1 LAND
99805       H556  ---- ROELVEDER MUEHLE      51.17    7.36   410      1 LAND
99806       H605  ---- GUEDDERATH            51.08    6.26    50     32 LAND
99807       H663  ---- SICHTER               51.09    7.41   530   -119 LAND
99808       H746  ---- MOITZFELD             50.58    7.11   133     35 LAND
99809       H775  ---- ECKENHAGEN            50.58    7.43   445    -28 LAND
99810       H810  ---- KREUZ AACHEN          50.48    6.10   155      7 LAND
99811       H933  ---- WISSKIRCHEN           50.38    6.43   211      9 LAND
99812       H993  ---- BLANKENHEIM           50.28    6.42   550    -26 LAND
99801       J721  ---- LOESTERBACH SUED      49.37    6.56   482     28 LAND
99802       J907  ---- GOLDENE BREMM         49.13    6.58   224     53 LAND
99803       K040  ---- ESCH                  50.34    7.03   268    -42 LAND
99804       K100  ---- KLEIN-ALTENDORF       50.37    6.59   150     20 LAND
99805       K101  ---- STEINBORN             50.04    6.37   529    -36 LAND
99806       K130  ---- SINZIG                50.32    7.11   206     13 LAND
99807       K164  ---- KANNENBAECKER LAND    50.27    7.44   300      7 LAND
99808       K169  ---- GRENZAU               50.27    7.39   300      7 LAND
99809       K250  ---- MAYEN                 50.19    7.14   275     13 LAND
99810       K265  ---- OCHTENDUNG            50.20    7.25   314    -26 LAND
99811       K266  ---- MOSELTALBRUECKE       50.19    7.29   204      4 LAND
99812       K268  ---- MUENSTERMAIFELD       50.16    7.21   178     30 LAND
99801       K315  ---- STRICKSCHEID          50.09    6.19   470      6 LAND
99802       K341  ---- LAUBACHER HOEHE       50.14    7.04   564    -65 LAND
99803       K436  ---- WIERSDORF             50.00    6.27   296      8 LAND
99804       K442  ---- DREIS-BRUECK          50.16    6.47   470     10 LAND
99805       K445  ---- FLUSSBACH             50.01    6.56   331     -2 LAND
99806       K471  ---- SIMMERN-WAHLBACH      50.00    7.36   445     20 LAND
99807       K480  ---- LAUDERT               50.05    7.37   530    -65 LAND
99808       K481  ---- WAHLBACH              50.00    7.35   436     29 LAND
99809       K510  ---- MERZKIRCHEN           49.34    6.28   369    -84 LAND
99810       K531  ---- BERNKASTEL-KUES       49.55    7.04   120    129 LAND
99811       K560  ---- MEDDERSHEIM           49.47    7.37   150    142 LAND
99812       K562  ---- WIESWEILER            49.38    7.35   180    113 LAND
99801       K571  ---- BINGEN-GAULSHEIM      49.58    7.58    88     97 LAND
99802       K582  ---- MAINZ (DLR)           49.58    8.14   153     19 LAND
99803       K587  ---- WOERRSTADT            49.51    8.09   150     27 LAND
99804       K588  ---- ROMMERSHEIM           49.49    8.07   238    -46 LAND
99805       K597  ---- NIERSTEIN             49.52    8.20   169    -46 LAND
99806       K598  ---- DIEMHEIM              49.51    8.19   202     17 LAND
99807       K610  ---- AVELSBACH             49.45    6.42   248     -2 LAND
99808       K620  ---- KANZERN               49.40    6.35   216     57 LAND
99809       K621  ---- WITTLICH              49.58    6.52   197     22 LAND
99810       K623  ---- ZELTINGEN             49.57    7.02   212     37 LAND
99811       K630  ---- DIENSTWEILER          49.38    7.12   461     -1 LAND
99812       K642  ---- NIEDERWOERSSESBACH    49.46    7.20   302    -10 LAND
99801       K670  ---- PLEISWEILER-OBERHOFE  49.07    8.01   197     17 LAND
99802       K672  ---- SCHWEIGHOFEN          49.02    7.59   159      1 LAND
99803       K677  ---- FREIMERSHEIM          49.43    8.04   270    -51 LAND
99804       K695  ---- EICH                  49.45    8.23    89      1 LAND
99805       K732  ---- HAHNWEILER            49.35    7.14   536     22 LAND
99806       K768  ---- SCHORLENBERG          49.28    7.55   412     -2 LAND
99807       K787  ---- LEINIGER BERG         49.32    8.07   292      0 LAND
99808       K795  ---- FRANKENTHAL           49.33    8.21    95     38 LAND
99809       K862  ---- MORLAUTERN            49.28    7.46   320      0 LAND
99810       K880  ---- HERXHEIMWEYHER        49.10    8.15   144     -4 LAND
99811       K882  ---- STEINWEILER           49.07    8.07   132      8 LAND
99812       K886  ---- WEIERHOF              49.38    8.02   194     25 LAND
99801       K887  ---- NEUSTADT/WEINSTRASSE  49.22    8.12   141     -4 LAND
99802       K892  ---- SCHIFFERSTADT         49.25    8.21   102     -2 LAND
99803       K963  ---- LUSTADT               49.15    8.17   116     -7 LAND
99804       L112  ---- VASBECK               51.23    8.54   340      5 LAND
99805       L119  ---- HOF LAUTERBACH, VOEH  51.13    8.56   350    -13 LAND
99806       L160  ---- LUTTERBERG            51.22    9.38   395    -21 LAND
99807       L242  ---- AM SCHARFENSTEIN      51.11    9.24   245    -39 LAND
99808       L267  ---- ALHEIM                51.03    9.42   281     54 LAND
99809       L282  ---- OBERHONE              51.10   10.00   180    117 LAND
99810       L283  ---- DOMAENE VOGELSBURG    51.09   10.01   220     83 LAND
99811       L284  ---- HESSENRING            51.11   10.02   238     59 LAND
99812       L353  ---- ALSFELD               50.45    9.15   304    -21 LAND
99801       L379  ---- EICHHOF               50.50    9.41   200    110 LAND
99802       L414  ---- HAIGER                50.45    8.13   320     -1 LAND
99803       L474  ---- RIMBERG               50.48    9.29   490    -85 LAND
99804       L542  ---- HOMBERG-OHM           50.39    9.00   330    -34 LAND
99805       L585  ---- FULDA                 50.32    9.41   255     62 LAND
99806       L637  ---- T/R WETTERAU          50.21    8.42   250    -54 LAND
99807       L641  ---- ECHZELL SCHWALHEIM    50.24    8.54   130     58 LAND
99808       L648  ---- ALTENSTADT            50.19    8.56   184    -41 LAND
99809       L684  ---- THALAUBACH            50.26    9.45   370     19 LAND
99810       L687  ---- FORSTHAUS             50.23    9.44   475     50 LAND
99811       L716  ---- IDSTEIN               50.13    8.15   365    -38 LAND
99812       L838  ---- FRANKFURT             50.05    8.35    97     14 LAND
99801       L857  ---- WALDSCHNEISE HANAU    50.02    8.56   125     -6 LAND
99802       L858  ---- MARKOEBEL             50.14    8.57   156    -30 LAND
99803       L889  ---- ROSSDORF DARMSTADT    49.51    8.47   180    -15 LAND
99804       L912  ---- ALLMENDFELD           49.46    8.31    90     32 LAND
99805       L959  ---- RHEINBR.MANNHEIM      49.32    8.25   100     -6 LAND
99806       L962  ---- HEPPENHEIM            49.38    8.37    95      1 LAND
99807       L985  ---- BUCHHALDE             49.34    8.58   430    -23 LAND
99808       M403  ---- HOERSCHEL             51.01   10.13   300    -20 LAND
99809       M439  ---- BERKA, BAD (FLUGPLAT  50.54   11.16   303     23 LAND
99810       M524  ---- BOXBERG               50.53   10.39   348     26 LAND
99811       M575  ---- GERAER BERG           50.54   12.02   305    -36 LAND
99812       M721  ---- SCHMALKALDEN          50.44   10.28   330     54 LAND
99801       M774  ---- LEUBSDORF             50.42   11.51   420    -37 LAND
99802       M888  ---- SCHLEIZ               50.33   11.47   528     11 LAND
99803       N013  ---- ROSSLA                51.30   11.20   100     59 LAND
99804       N443  ---- IRXLEBEN              52.11   11.27   122    -53 LAND
99805       N520  ---- PABSTORF              52.02   10.58   112     21 LAND
99806       N567  ---- VOCKERODE             51.52   12.21    70     -5 LAND
99807       N616  ---- OBERHARZ AM BROCKEN   51.40   10.53   504    -31 LAND
99808       N642  ---- PLOETZKAU/SAALE       51.43   11.41    95    -19 LAND
99809       N769  ---- LAUCHSTAEDT, BAD      51.23   11.53   118    -16 LAND
99810       N793  ---- ZOERBIG               51.36   12.11    97      0 LAND
99811       N891  ---- ELSTER-SAALE-KANAL    51.21   12.11   115      0 LAND
99812       N992  ---- OSTERFELD             51.01   11.56   298    -51 LAND
99801       O013  ---- BERBERSDORF           50.40   12.50   300     40 LAND
99802       O215  ---- WALDSTEINBERG         51.18   12.35   136      5 LAND
99803       O252  ---- SCHOENBORN            51.19   13.43   174    -46 LAND
99804       O372  ---- BURKAUER BERG         51.10   14.07   328    -36 LAND
99805       O451  ---- DRESDEN-PILLNITZ      51.00   13.53   115     84 LAND
99806       O454  ---- DRESDEN/FLUGHAFEN     51.09   13.54   220      0 LAND
99807       O459  ---- ZELLWALD              51.02   13.16   301    -52 LAND
99808       O862  ---- MARIENHOEHE           50.36   12.23   486    -40 LAND
99809       O951  ---- HEINERSGRUEN          50.24   11.59   561     -4 LAND
99810       P017  ---- OBERTHULBA            50.12    9.56   320     49 LAND
99811       P082  ---- SAALEBRUECKE          50.21   11.52   464     35 LAND
99812       P101  ---- KAHL                  50.04    9.01   116      3 LAND
99801       P116  ---- HASELTAL              49.53    9.26   420    -59 LAND
99802       P134  ---- SCHWEINFURT           50.01   10.13   214     21 LAND
99803       P159  ---- HIRSCHAID             49.49   11.01   268      6 LAND
99804       P166  ---- THURNAU               50.01   11.21   498      1 LAND
99805       P235  ---- BUERGSTADT            49.42    9.17   210      3 LAND
99806       P254  ---- RANDERSACKER          49.45    9.59   185     79 LAND
99807       P264  ---- ROEDELSEE             49.43   10.15   240     23 LAND
99808       P267  ---- HIENBERG              49.36   11.22   539    -38 LAND
99809       P289  ---- NAABBRUECKE           49.35   12.08   391     33 LAND
99810       P291  ---- WALDNAAB              49.47   12.10   458     12 LAND
99811       P332  ---- ZOLLHAUS              49.24   11.07   346      5 LAND
99812       P353  ---- VILSTAL               49.24   11.54   397     40 LAND
99801       P401  ---- ZUMHAUS               49.13   10.15   462     10 LAND
99802       P438  ---- GELBELSEE             48.57   11.26   521    -44 LAND
99803       P452  ---- TB EICHELBERG         49.12   12.07   415    -23 LAND
99804       P515  ---- DONAUWOERTH-OSTERWE.  48.44   10.44   434     38 LAND
99805       P533  ---- KOESCHINGER FORST     48.51   11.27   450     27 LAND
99806       P547  ---- SIEGENBURG            48.42   11.48   400     31 LAND
99807       P573  ---- DEGGENAU              48.48   12.58   320     15 LAND
99808       P575  ---- NEUSLING              48.42   12.54   345    -10 LAND
99809       P589  ---- GALGENBERG            48.38   13.18   510    -60 LAND
99810       P621  ---- RAIN AM LECH-WALLERD  48.37   11.01   462    -36 LAND
99811       P632  ---- HOLLEDAU SUED         48.33   11.36   477    -11 LAND
99812       P738  ---- SCHOEFFELDING         48.04   10.58   650    -48 LAND
99801       P748  ---- OBERPFAFFENHOFEN      48.06   11.18   570     -7 LAND
99802       P755  ---- ASCHHEIM              48.13   11.41   495     10 LAND
99803       P805  ---- ALLGAEUER TOR         47.52   10.17   720    -20 LAND
99804       P866  ---- SEEHAMMER SEE         47.52   11.51   690    -44 LAND
99805       P869  ---- DETTENDORF            47.49   12.00   500     -7 LAND
99806       P878  ---- STREITHEIM            48.25   10.40   490    -16 LAND
99807       P910  ---- HELLENGERST           47.40   10.12   947    -49 LAND
99808       P912  ---- SULZBERG              47.41   10.19   730     38 LAND
99809       P941  ---- GROSSWEIL             47.40   11.15   680     12 LAND
99810       P977  ---- OBERAUDORF            47.40   12.11   470     16 LAND
99811       Q006  ---- SECKENHEIM            49.27    8.33   100     -3 LAND
99812       Q068  ---- HOLZSPITZE            49.27    9.33   370    -31 LAND
99801       Q208  ---- KARLSRUHE             49.00    8.27   170     49 LAND
99802       Q241  ---- SULMTAL               49.10    9.15   180     36 LAND
99803       Q247  ---- BESIGHEIM             48.59    9.11   300    -57 LAND
99804       Q290  ---- WOLFSKOPF             49.11   10.03   440    -12 LAND
99805       Q348  ---- ENGELBERG             48.48    9.02   450    -16 LAND
99806       Q358  ---- STUTTGART NECKARTAL   48.47    9.13   223     36 LAND
99807       Q441  ---- AK STUTTGART          48.43    9.05   500    -48 LAND
99808       Q444  ---- STUTTGART RWY4        48.40    9.11   363     -3 LAND
99809       Q585  ---- NW-HR09               48.31    9.45   710     26 LAND
99810       Q597  ---- NW-HR02               48.28   10.04   550    -33 LAND
99811       Q904  ---- DREIECK WEIL          47.37    7.35   240     13 LAND
99812       Q909  ---- RHEINFELDEN           47.34    7.47   282     22 LAND
99801       Q988  ---- GRUB                  47.39    9.45   540     -1 LAND
99802       X001  ---- SWIS-PUNKT            51.10    9.30   160     46 LAND
99803       X002  ---- SWIS-PUNKT            50.10    6.40   300     42 LAND
99804       X003  ---- SWIS-PUNKT            50.10    6.20   500     -7 LAND
99805       X004  ---- SWIS-PUNKT            51.20    7.40   700   -289 LAND
99806       X005  ---- SWIS-PUNKT            51.00    7.10   100     68 LAND
99807       X006  ---- SWIS-PUNKT            51.00    7.20   300     13 LAND
99808       X007  ---- SWIS-PUNKT            51.00    7.30   500    -83 LAND
99809       X008  ---- SWIS-PUNKT            48.31    9.45   900   -164 LAND
99810       X009  ---- SWIS-PUNKT            50.55    7.00   100    -32 LAND
99811       X010  ---- SWIS-PUNKT            50.50    6.10   100     -4 LAND
99812       X011  ---- SWIS-PUNKT            51.40   11.46   300   -130 LAND
99801       X012  ---- SWIS-PUNKT            50.40    6.40   100      5 LAND
99802       X013  ---- SWIS-PUNKT            50.45    7.50   500     27 LAND
99803       X014  ---- SWIS-PUNKT            50.25    9.45   700    -64 LAND
99804       X015  ---- SWIS-PUNKT            50.15    8.20   500   -103 LAND
99805       X016  ---- SWIS-PUNKT            49.27    8.34   300      2 LAND
99806       X017  ---- SWIS-PUNKT            49.10    9.15   300     -9 LAND
99807       X018  ---- SWIS-PUNKT            47.39    9.46   700    -61 LAND
99808       X019  ---- SWIS-PUNKT            48.30    8.08   300     12 LAND
99809       X020  ---- SWIS-PUNKT            48.30    8.09   500    -25 LAND
99810       X021  ---- SWIS-PUNKT            48.30    8.10   700     23 LAND
99811       X022  ---- SWIS-PUNKT            48.30    8.11   900   -139 LAND
99812       X023  ---- SWIS-PUNKT            48.30    8.12  1100   -514 BERG
99801       X024  ---- SWIS-PUNKT            50.20   10.00   700   -331 BERG
99802       X025  ---- SWIS-PUNKT            50.15   11.40   700   -106 LAND
99803       X026  ---- SWIS-PUNKT            53.20   13.40   100    -16 LAND
99804       X027  ---- SWIS-PUNKT            49.30   12.38   700    -88 LAND
99805       X028  ---- SWIS-PUNKT            51.15    9.50   700   -315 LAND
99806       X029  ---- SWIS-PUNKT            47.45   12.45   900    -23 LAND
99807       X030  ---- SWIS-PUNKT            47.45   12.30  1100     45 LAND
99808       X031  ---- SWIS-PUNKT            50.22   12.28   700     62 LAND
99809       X032  ---- SWIS-PUNKT            52.30   11.30   100    -46 LAND
99810       X033  ---- SWIS-PUNKT            51.15   11.00   100     62 LAND
99811       X034  ---- SWIS-PUNKT            51.40   12.40    90     41 LAND
99812       X035  ---- SWIS-PUNKT            51.20   13.15    70     45 LAND
99801       X036  ---- SWIS-PUNKT            51.40   10.31   900   -315 LAND
99802       X037  ---- SWIS-PUNKT            51.50   10.40   700   -115 LAND
99803       X038  ---- SWIS-PUNKT            49.50    7.10   700   -169 LAND
99804       X039  ---- SWIS-PUNKT            50.40   10.45   700    -34 LAND
99805       X040  ---- SWIS-PUNKT            50.30   11.00   900   -238 LAND
99806       X042  ---- SWIS-PUNKT            49.30    8.20   100     36 LAND
99807       X043  ---- SWIS-PUNKT            50.15    7.50   300      3 LAND
99808       X044  ---- SWIS-PUNKT            50.15    7.51   500   -117 LAND
99809       X045  ---- SWIS-PUNKT            52.30   13.20   100    -59 LAND
99810       X046  ---- SWIS-PUNKT            51.30   11.20   300      1 LAND
99811       X047  ---- SWIS-PUNKT            50.15    7.50   700   -317 LAND
99812       X048  ---- SWIS-PUNKT            50.40   10.22   275    109 LAND
99801       X049  ---- SWIS-PUNKT            50.28   10.45   475      5 LAND
99802       X050  ---- SWIS-PUNKT            53.50   13.30    50    -33 LAND
99803       X051  ---- SWIS-PUNKT            51.30   11.21   500   -171 LAND
99804       X052  ---- SWIS-PUNKT            50.05    8.00   700   -365 LAND
99805       X053  ---- SWIS-PUNKT            49.40    8.50   300    -15 LAND
99806       X054  ---- SWIS-PUNKT            50.20   10.00   900   -283 LAND
99807       X055  ---- SWIS-PUNKT            49.30   11.50   700   -246 LAND
99808       X056  ---- SWIS-PUNKT            50.00   12.00   900   -247 BERG
99809       X057  ---- SWIS-PUNKT            47.40   10.30  1000    -64 LAND
99810       X058  ---- SWIS-PUNKT            49.30   12.30   900   -331 BERG
99811       X059  ---- SWIS-PUNKT            49.00   13.09   900    -89 LAND
99812       X060  ---- SWIS-PUNKT            49.00   13.10  1000    -42 LAND
99801       X087  ---- SWIS-PUNKT            51.45   10.30   500    -51 LAND
99802       X088  ---- SWIS-PUNKT            51.40   10.30   700   -115 LAND
99803       X089  ---- SWIS-PUNKT            47.37    7.36   500     55 LAND
99804       X090  ---- SWIS-PUNKT            49.40   10.30   500   -109 LAND
99805       X091  ---- SWIS-PUNKT            50.10   11.40   300     86 LAND
99806       X093  ---- SWIS-PUNKT            49.02   13.18   700    -14 LAND
99807       X095  ---- SWIS-PUNKT            50.25   12.30   700     62 LAND
99808       X096  ---- SWIS-PUNKT            51.00   14.40   500    -64 LAND
99809       X097  ---- SWIS-PUNKT            51.47   10.40   900   -315 LAND
99810       X098  ---- SWIS-PUNKT            51.40   10.41  1100   -566 BERG
99811       X099  ---- SWIS-PUNKT            50.28   12.51   900    -28 LAND
99812       X100  ---- SWIS-PUNKT            51.40   12.40   100     31 LAND
99801       X101  ---- SWIS-PUNKT            48.21   11.47   450      8 LAND
99802       X102  ---- SWIS-PUNKT            49.30   11.05   320      0 LAND
99803       X103  ---- SWIS-PUNKT            52.23   13.31    50    -12 LAND
99804       X104  ---- SWIS-PUNKT            52.34   13.17    40     -5 LAND
99805       X105  ---- SWIS-PUNKT            52.28   13.24    53    -12 LAND
99806       X106  ---- SWIS-PUNKT            53.38    9.59    11      8 LAND
99807       X107  ---- SWIS-PUNKT            53.03    8.47     3      3 LAND
99808       X109  ---- SWIS-PUNKT            52.08    7.41    51     -5 LAND
99809       X110  ---- SWIS-PUNKT            51.17    6.45    39     -4 LAND
99810       X111  ---- SWIS-PUNKT            50.52    7.09    84    -16 LAND
99811       X112  ---- SWIS-PUNKT            49.13    7.07   351    -81 LAND
99812       X113  ---- SWIS-PUNKT            50.58   10.57   344    -68 LAND
99801       X114  ---- SWIS-PUNKT            50.02    8.34   109     -9 LAND
99802       X115  ---- SWIS-PUNKT            51.45    9.34   500   -172 BERG
99803       X116  ---- SWIS-PUNKT            50.31    2.37    28     38 LAND
99804       X117  EDAC SWIS-PUNKT            50.59   12.30   209     -8 LAND
99805       X118  EDMA SWIS-PUNKT            48.25   10.56   504    -36 LAND
99806       X119  EDQD SWIS-PUNKT            49.59   11.38   530     -7 LAND
99807       X120  EDVE SWIS-PUNKT            52.19   10.33    92    -14 LAND
99808       X121  EDWB SWIS-PUNKT            53.30    8.34     3      2 KUES
99809       X122  EDBC SWIS-PUNKT            51.51   11.25   198    -10 LAND
99810       X123  EDTD SWIS-PUNKT            47.58    8.31   742    -11 LAND
99811       X124  EDLW SWIS-PUNKT            51.31    7.37   135    -54 LAND
99812       X125  EDFE SWIS-PUNKT            49.58    8.39   128     16 LAND
99801       X126  EDWE SWIS-PUNKT            53.23    7.13     0      1 LAND
99802       X127  EDNY SWIS-PUNKT            47.40    9.31   449     -7 LAND
99803       X128  EDFH SWIS-PUNKT            49.57    7.16   548    -17 LAND
99804       X129  EDHI SWIS-PUNKT            53.32    9.50     3      7 LAND
99805       X130  EDAH SWIS-PUNKT            53.53   14.09    24    -19 KUES
99806       X131  EDQM SWIS-PUNKT            50.17   11.51   640    -13 LAND
99807       X132  EDSB SWIS-PUNKT            48.47    8.05   136    -18 LAND
99808       X133  EDVK SWIS-PUNKT            51.24    9.22   302    -57 LAND
99809       X134  EDHK SWIS-PUNKT            54.23   10.09    33    -18 KUES
99810       X135  EDTL SWIS-PUNKT            48.22    7.50   169     -5 LAND
99811       X136  EDWD SWIS-PUNKT            53.09    8.37    67    -60 LAND
99812       X137  EDHL SWIS-PUNKT            53.48   10.43    17     16 LAND
99801       X138  EDBM SWIS-PUNKT            52.04   11.38    89    -24 LAND
99802       X139  EDFM SWIS-PUNKT            49.28    8.31   103     -6 LAND
99803       X140  EDLN SWIS-PUNKT            51.14    6.30    41     -2 LAND
99804       X141  EDLV SWIS-PUNKT            51.36    6.08    35    -14 LAND
99805       X142  EDMO SWIS-PUNKT            48.05   11.17   635    -43 LAND
99806       X143  EDLP SWIS-PUNKT            51.37    8.37   232    -64 LAND
99807       X144  ETNL SWIS-PUNKT            53.55   12.17    46    -13 LAND
99808       X145  EDTY SWIS-PUNKT            49.07    9.47   436    -34 LAND
99809       X146  EDOP SWIS-PUNKT            53.25   11.47    50     10 LAND
99810       X147  EDGS SWIS-PUNKT            50.43    8.05   651   -124 LAND
99811       X148  EDMS SWIS-PUNKT            48.54   12.31   349    -17 LAND
99812       X149  EDXW SWIS-PUNKT            54.54    8.20     8     -8 KUES
99801       X150  EDWI SWIS-PUNKT            53.30    8.03     5     -3 KUES
99802       X151  EDRZ SWIS-PUNKT            49.13    7.24   377    -30 LAND
99803       X200  ---- SWIS-PUNKT            47.34    9.59   900     -2 LAND
99804       X201  ---- SWIS-PUNKT            47.21   10.20   900    152 LAND
99805       X202  ---- SWIS-PUNKT            47.40   10.52   900      8 LAND
99806       X203  ---- SWIS-PUNKT            47.33   10.22  1100    -48 LAND
99807       X204  ---- SWIS-PUNKT            47.35   10.53  1100     52 LAND
99808       X205  ---- SWIS-PUNKT            47.32   11.13  1100    -35 LAND
99809       X206  ---- SWIS-PUNKT            47.39   11.20   500    135 LAND
99810       X207  ---- SWIS-PUNKT            47.46   12.27   500    -14 LAND
99811       X208  ---- SWIS-PUNKT            47.35   11.20   900     70 LAND
99812       X209  ---- SWIS-PUNKT            47.46   12.22   900    -23 LAND
99801       X210  ---- SWIS-PUNKT            47.39   13.00   900     13 LAND
99802       X211  ---- SWIS-PUNKT            47.39   11.28  1100      0 LAND
99803       X212  ---- SWIS-PUNKT            47.45   12.21  1100   -111 LAND
99804       X213  ---- SWIS-PUNKT            47.32   13.00  1100     -1 LAND
99805       X214  ---- SWIS-PUNKT            47.54   11.22   700     -8 LAND
99806       X215  ---- SWIS-PUNKT            48.40   10.47   300    121 LAND
99807       X216  ---- SWIS-PUNKT            49.35   10.56   500   -117 LAND
99808       X217  ---- SWIS-PUNKT            48.50   11.08   500      6 LAND
99809       X218  ---- SWIS-PUNKT            48.55   11.31   500    -23 LAND
99810       X219  ---- SWIS-PUNKT            47.58   12.21   700      3 LAND
99811       X220  ---- SWIS-PUNKT            47.51   12.40   700      3 LAND
99812       X221  ---- SWIS-PUNKT            48.34   12.43   300     35 LAND
99801       X222  ---- SWIS-PUNKT            48.44   11.57   500    -69 LAND
99802       X223  ---- SWIS-PUNKT            48.34   12.43   500    -75 LAND
99803       X224  ---- SWIS-PUNKT            48.59   10.46   700   -191 LAND
99804       X225  ---- SWIS-PUNKT            49.02   11.04   700   -219 LAND
99805       X226  ---- SWIS-PUNKT            49.25   11.39   700   -207 LAND
99806       X227  ---- SWIS-PUNKT            49.29   12.01   700   -263 LAND
99807       X228  ---- SWIS-PUNKT            47.57    8.59   700    -73 LAND
99808       X229  ---- SWIS-PUNKT            48.44    9.57   700    -67 LAND
99809       X230  ---- SWIS-PUNKT            47.58    8.41   900    -54 LAND
99810       X231  ---- SWIS-PUNKT            48.15    9.05   900    -74 LAND
99811       X232  ---- SWIS-PUNKT            48.30    9.34   900   -164 LAND
99812       X233  ---- SWIS-PUNKT            48.06    9.23   500    115 LAND
99801       X234  ---- SWIS-PUNKT            49.32   10.43   300     57 LAND
99802       X235  ---- SWIS-PUNKT            49.15   10.53   500    -78 LAND
99803       X236  ---- SWIS-PUNKT            49.36   11.57   500    -50 LAND
99804       X237  ---- SWIS-PUNKT            49.44   12.05   500    -30 LAND
99805       X238  ---- SWIS-PUNKT            49.43    9.30   300     26 LAND
99806       X239  ---- SWIS-PUNKT            49.21    8.48   100     -3 LAND
99807       X240  ---- SWIS-PUNKT            49.21    8.56   300    -51 LAND
99808       X241  ---- SWIS-PUNKT            48.29    8.53   500    -52 LAND
99809       X242  ---- SWIS-PUNKT            48.55    9.46   500    -30 LAND
99810       X243  ---- SWIS-PUNKT            49.54    9.43   300    -10 LAND
99811       X244  ---- SWIS-PUNKT            50.14   10.26   500   -109 LAND
99812       X245  ---- SWIS-PUNKT            50.00   10.39   500   -176 LAND
99801       X246  ---- SWIS-PUNKT            49.52   10.29   500   -155 LAND
99802       X247  ---- SWIS-PUNKT            49.36   10.18   500   -133 LAND
99803       X248  ---- SWIS-PUNKT            49.59    9.02   100     54 LAND
99804       X249  ---- SWIS-PUNKT            50.00    9.15   100     19 LAND
99805       X250  ---- SWIS-PUNKT            49.52    9.14   300      6 LAND
99806       X251  ---- SWIS-PUNKT            50.23   10.11   300     53 LAND
99807       X252  ---- SWIS-PUNKT            50.28   10.14   300     51 LAND
99808       X253  ---- SWIS-PUNKT            49.37    9.05   500    -93 LAND
99809       X254  ---- SWIS-PUNKT            50.20    9.45   500     25 LAND
99810       X255  ---- SWIS-PUNKT            50.31   10.11   500    -12 LAND
99811       X256  ---- SWIS-PUNKT            50.21    9.49   700    -64 LAND
99812       X257  ---- SWIS-PUNKT            50.19    9.53   700    -64 LAND
99801       X258  ---- SWIS-PUNKT            50.29   10.04   700    -64 LAND
99802       X259  ---- SWIS-PUNKT            50.31   10.05   700   -105 LAND
99803       X260  ---- SWIS-PUNKT            50.19    9.54   900   -264 LAND
99804       X261  ---- SWIS-PUNKT            50.22    9.57   900   -283 LAND
99805       X262  ---- SWIS-PUNKT            50.30   10.03   900   -264 LAND
99806       X263  ---- SWIS-PUNKT            50.31   10.04   900   -305 LAND
99807       X264  ---- SWIS-PUNKT            49.49    8.44   300    -15 LAND
99808       X265  ---- SWIS-PUNKT            49.35    8.46   300      2 LAND
99809       X266  ---- SWIS-PUNKT            49.50    8.59   300    -15 LAND
99810       X267  ---- SWIS-PUNKT            49.42    8.47   500   -124 LAND
99811       X268  ---- SWIS-PUNKT            49.35    8.48   500   -124 LAND
99812       X269  ---- SWIS-PUNKT            49.39    9.04   500    -80 LAND
99801       X270  ---- SWIS-PUNKT            49.40    8.54   500    -80 LAND
99802       X271  ---- SWIS-PUNKT            48.48    8.28   500     64 LAND
99803       X272  ---- SWIS-PUNKT            48.12    8.04   500    -24 LAND
99804       X273  ---- SWIS-PUNKT            47.50    7.47   500     44 LAND
99805       X274  ---- SWIS-PUNKT            48.44    8.38   700    -17 LAND
99806       X275  ---- SWIS-PUNKT            48.14    8.26   700    -10 LAND
99807       X276  ---- SWIS-PUNKT            48.41    8.25   900   -161 LAND
99808       X277  ---- SWIS-PUNKT            47.48    7.48   900     62 LAND
99809       X278  ---- SWIS-PUNKT            47.47    7.46  1100    -62 LAND
99810       X279  ---- SWIS-PUNKT            47.47    8.09  1100    -62 LAND
99811       X280  ---- SWIS-PUNKT            48.05    8.09  1100   -127 LAND
99812       X281  ---- SWIS-PUNKT            47.34    7.44   300      4 LAND
99801       X282  ---- SWIS-PUNKT            47.37    8.19   300    153 LAND
99802       X283  ---- SWIS-PUNKT            47.37    7.50   500      2 LAND
99803       X284  ---- SWIS-PUNKT            49.07    7.56   300      3 LAND
99804       X285  ---- SWIS-PUNKT            49.17    8.02   500    -90 LAND
99805       X286  ---- SWIS-PUNKT            49.09    7.35   500    -90 LAND
99806       X287  ---- SWIS-PUNKT            49.28    6.32   300    -15 LAND
99807       X288  ---- SWIS-PUNKT            49.32    6.44   500     10 LAND
99808       X289  ---- SWIS-PUNKT            49.35    6.58   500     10 LAND
99809       X290  ---- SWIS-PUNKT            49.32    7.02   500    -40 LAND
99810       X291  ---- SWIS-PUNKT            49.53    8.04   300     29 LAND
99811       X292  ---- SWIS-PUNKT            49.44    7.39   300     -8 LAND
99812       X293  ---- SWIS-PUNKT            49.37    7.16   500    -80 LAND
99801       X294  ---- SWIS-PUNKT            49.39    7.27   500    -40 LAND
99802       X295  ---- SWIS-PUNKT            49.33    7.32   500    -80 LAND
99803       X296  ---- SWIS-PUNKT            49.37    7.55   500   -162 LAND
99804       X297  ---- SWIS-PUNKT            47.45    7.36   300    -47 LAND
99805       X298  ---- SWIS-PUNKT            50.10    7.34   500    -35 LAND
99806       X299  ---- SWIS-PUNKT            49.40    6.49   700   -190 LAND
99807       X300  ---- SWIS-PUNKT            49.40    7.01   700   -142 LAND
99808       X301  ---- SWIS-PUNKT            49.55    7.36   700   -235 LAND
99809       X302  ---- SWIS-PUNKT            49.43    7.08   700   -142 LAND
99810       X303  ---- SWIS-PUNKT            50.25    7.04   500     -1 LAND
99811       X304  ---- SWIS-PUNKT            50.42    6.29   300     65 LAND
99812       X305  ---- SWIS-PUNKT            50.38    6.33   300    -26 LAND
99801       X306  ---- SWIS-PUNKT            50.32    6.20   500      2 LAND
99802       X307  ---- SWIS-PUNKT            50.35    6.29   500     -3 LAND
99803       X308  ---- SWIS-PUNKT            50.34    7.12   100     11 LAND
99804       X309  ---- SWIS-PUNKT            50.17    7.41   300    -49 LAND
99805       X310  ---- SWIS-PUNKT            50.18    8.00   300     14 LAND
99806       X311  ---- SWIS-PUNKT            50.14    7.56   500   -122 LAND
99807       X312  ---- SWIS-PUNKT            50.08    7.50   500    -35 LAND
99808       X313  ---- SWIS-PUNKT            50.14    7.42   500   -113 LAND
99809       X314  ---- SWIS-PUNKT            50.12    7.46   500   -117 LAND
99810       X315  ---- SWIS-PUNKT            50.05    7.52   300     35 LAND
99811       X316  ---- SWIS-PUNKT            50.08    8.23   300     27 LAND
99812       X317  ---- SWIS-PUNKT            50.10    7.56   500    -35 LAND
99801       X318  ---- SWIS-PUNKT            50.06    8.02   500   -122 LAND
99802       X319  ---- SWIS-PUNKT            50.23    8.32   500   -152 LAND
99803       X320  ---- SWIS-PUNKT            50.30    8.10   300     14 LAND
99804       X321  ---- SWIS-PUNKT            50.50    8.39   300    -10 LAND
99805       X322  ---- SWIS-PUNKT            50.32    8.43   300     -4 LAND
99806       X323  ---- SWIS-PUNKT            50.35    7.20   300     -8 LAND
99807       X324  ---- SWIS-PUNKT            50.28    7.56   300    -21 LAND
99808       X325  ---- SWIS-PUNKT            50.26    7.44   500   -114 LAND
99809       X326  ---- SWIS-PUNKT            50.35    7.50   500     27 LAND
99810       X327  ---- SWIS-PUNKT            50.40    8.04   500     27 LAND
99811       X328  ---- SWIS-PUNKT            51.24    8.16   500     16 LAND
99812       X329  ---- SWIS-PUNKT            51.18    8.33   700    -63 LAND
99801       X330  ---- SWIS-PUNKT            51.04    8.28   700    -63 LAND
99802       X331  ---- SWIS-PUNKT            51.57    9.07   300    -37 LAND
99803       X333  ---- SWIS-PUNKT            50.45    7.16   100     11 LAND
99804       X334  ---- SWIS-PUNKT            50.56    7.25   300      1 LAND
99805       X335  ---- SWIS-PUNKT            51.17    7.27   500   -139 LAND
99806       X336  ---- SWIS-PUNKT            51.10    7.29   500   -139 LAND
99807       X337  ---- SWIS-PUNKT            51.04    7.34   500    -83 LAND
99808       X338  ---- SWIS-PUNKT            50.59    7.43   500     -4 LAND
99809       X339  ---- SWIS-PUNKT            51.32    9.28   300    -22 LAND
99810       X340  ---- SWIS-PUNKT            51.04    8.59   500    -38 LAND
99811       X341  ---- SWIS-PUNKT            50.54    9.25   500   -131 LAND
99812       X342  ---- SWIS-PUNKT            50.40    9.50   500    -25 LAND
99801       X343  ---- SWIS-PUNKT            51.17    8.34   700    -63 LAND
99802       X344  ---- SWIS-PUNKT            51.17    8.40   700   -153 LAND
99803       X345  ---- SWIS-PUNKT            51.00    9.04   700   -331 LAND
99804       X346  ---- SWIS-PUNKT            50.15    9.36   300     -4 LAND
99805       X347  ---- SWIS-PUNKT            50.26    9.24   500    -37 LAND
99806       X348  ---- SWIS-PUNKT            50.33    9.57   500    -12 LAND
99807       X349  ---- SWIS-PUNKT            50.08    9.25   500   -120 LAND
99808       X350  ---- SWIS-PUNKT            50.29    9.15   700   -237 LAND
99809       X351  ---- SWIS-PUNKT            50.30    9.54   700    -83 LAND
99810       X352  ---- SWIS-PUNKT            50.34   10.01   700   -105 LAND
99811       X353  ---- SWIS-PUNKT            51.52    9.08   100     28 LAND
99812       X354  ---- SWIS-PUNKT            51.38    9.22   100    136 LAND
99801       X355  ---- SWIS-PUNKT            51.32    9.11   100    130 LAND
99802       X356  ---- SWIS-PUNKT            51.35    9.15   300     -4 LAND
99803       X357  ---- SWIS-PUNKT            51.49    9.16   300     -4 LAND
99804       X358  ---- SWIS-PUNKT            51.48    9.50   100     84 LAND
99805       X359  ---- SWIS-PUNKT            51.52    9.38   300    -56 LAND
99806       X360  ---- SWIS-PUNKT            51.22    9.36   300    -22 LAND
99807       X361  ---- SWIS-PUNKT            51.31   10.03   300    -42 LAND
99808       X362  ---- SWIS-PUNKT            51.39   10.38   500     34 LAND
99809       X363  ---- SWIS-PUNKT            51.41   10.30   500    -48 LAND
99810       X364  ---- SWIS-PUNKT            51.46   10.17   500    -51 LAND
99811       X365  ---- SWIS-PUNKT            51.49   10.30   700   -115 LAND
99812       X366  ---- SWIS-PUNKT            51.51   10.22   700   -138 LAND
99801       X367  ---- SWIS-PUNKT            51.40   10.25   700   -115 LAND
99802       X368  ---- SWIS-PUNKT            51.47   10.33   900   -315 LAND
99803       X369  ---- SWIS-PUNKT            51.47   10.29   900   -338 LAND
99804       X370  ---- SWIS-PUNKT            51.44   10.25   900   -338 LAND
99805       X371  ---- SWIS-PUNKT            51.44   10.31   900   -315 LAND
99806       X372  ---- SWIS-PUNKT            51.56   10.47   100      8 LAND
99807       X373  ---- SWIS-PUNKT            51.52   11.11   100     11 LAND
99808       X374  ---- SWIS-PUNKT            51.27   11.04   100     73 LAND
99809       X375  ---- SWIS-PUNKT            51.42   11.13   300     -2 LAND
99810       X376  ---- SWIS-PUNKT            51.34   11.13   300     29 LAND
99811       X377  ---- SWIS-PUNKT            51.29   11.01   300      1 LAND
99812       X378  ---- SWIS-PUNKT            51.50   10.38   500    -22 LAND
99801       X379  ---- SWIS-PUNKT            51.34   11.01   500    -27 LAND
99802       X380  ---- SWIS-PUNKT            51.41   10.42   500     34 LAND
99803       X381  ---- SWIS-PUNKT            51.49   10.35   700   -115 LAND
99804       X382  ---- SWIS-PUNKT            51.47   10.42   700   -115 LAND
99805       X383  ---- SWIS-PUNKT            51.45   10.38   700   -115 LAND
99806       X384  ---- SWIS-PUNKT            51.47   10.39   700   -115 LAND
99807       X389  ---- SWIS-PUNKT            51.44   11.37   100     39 LAND
99808       X390  ---- SWIS-PUNKT            51.33   11.51   100     28 LAND
99809       X391  ---- SWIS-PUNKT            51.39   11.26   300     -2 LAND
99810       X392  ---- SWIS-PUNKT            51.32   11.20   300     -2 LAND
99811       X393  ---- SWIS-PUNKT            51.20   11.27   300   -113 LAND
99812       X394  ---- SWIS-PUNKT            51.15   11.44   300    -67 LAND
99801       X395  ---- SWIS-PUNKT            50.24   10.29   300     36 LAND
99802       X396  ---- SWIS-PUNKT            50.16   10.46   300     30 LAND
99803       X397  ---- SWIS-PUNKT            50.43   10.01   500    -25 LAND
99804       X398  ---- SWIS-PUNKT            50.23   11.06   500     -7 LAND
99805       X399  ---- SWIS-PUNKT            50.21   11.18   300     20 LAND
99806       X400  ---- SWIS-PUNKT            50.09   11.30   300     54 LAND
99807       X401  ---- SWIS-PUNKT            50.02   11.38   300    102 LAND
99808       X402  ---- SWIS-PUNKT            50.15   11.23   300     20 LAND
99809       X403  ---- SWIS-PUNKT            50.19   11.24   500     44 LAND
99810       X404  ---- SWIS-PUNKT            50.06   11.41   500     23 LAND
99811       X405  ---- SWIS-PUNKT            50.05   11.53   700    -79 LAND
99812       X406  ---- SWIS-PUNKT            49.55   12.07   700    -91 LAND
99801       X407  ---- SWIS-PUNKT            50.11   12.03   700    -47 LAND
99802       X408  ---- SWIS-PUNKT            49.53   12.02   900   -291 LAND
99803       X409  ---- SWIS-PUNKT            49.54   12.05   900   -291 LAND
99804       X410  ---- SWIS-PUNKT            50.01   11.52   900   -247 LAND
99805       X411  ---- SWIS-PUNKT            49.20   12.18   500    -16 LAND
99806       X412  ---- SWIS-PUNKT            49.44   12.22   700    -38 LAND
99807       X413  ---- SWIS-PUNKT            49.32   12.24   700    -38 LAND
99808       X414  ---- SWIS-PUNKT            49.29   12.36   700   -131 LAND
99809       X415  ---- SWIS-PUNKT            49.43   12.24   900   -238 LAND
99810       X416  ---- SWIS-PUNKT            49.30   12.37   900   -238 LAND
99811       X417  ---- SWIS-PUNKT            49.19   12.47   900   -281 LAND
99812       X418  ---- SWIS-PUNKT            49.30   12.34   900   -238 LAND
99801       X419  ---- SWIS-PUNKT            49.07   12.17   500    -56 LAND
99802       X420  ---- SWIS-PUNKT            48.40   13.31   500    -22 LAND
99803       X421  ---- SWIS-PUNKT            49.02   12.33   700   -127 LAND
99804       X422  ---- SWIS-PUNKT            48.58   12.50   700    -34 LAND
99805       X423  ---- SWIS-PUNKT            49.03   13.11   900    -89 LAND
99806       X424  ---- SWIS-PUNKT            48.48   13.45   900    -13 LAND
99807       X425  ---- SWIS-PUNKT            48.53   13.02  1100   -289 LAND
99808       X426  ---- SWIS-PUNKT            48.49   13.41  1100    -35 LAND
99809       X427  ---- SWIS-PUNKT            48.57   13.34  1100    -35 LAND
99810       X428  ---- SWIS-PUNKT            50.32   11.58   500    -22 LAND
99811       X429  ---- SWIS-PUNKT            50.20   12.06   700    -73 LAND
99812       X430  ---- SWIS-PUNKT            50.21   12.24   700    -55 LAND
99801       X431  ---- SWIS-PUNKT            50.28   12.26   700     62 LAND
99802       X432  ---- SWIS-PUNKT            50.29   12.45   700     -1 LAND
99803       X433  ---- SWIS-PUNKT            50.45   13.39   700    -53 LAND
99804       X434  ---- SWIS-PUNKT            50.27   12.45   900    -28 LAND
99805       X435  ---- SWIS-PUNKT            50.27   12.55   900    -28 LAND
99806       X436  ---- SWIS-PUNKT            50.32   13.10   900   -169 LAND
99807       X437  ---- SWIS-PUNKT            51.22   14.52   100     41 LAND
99808       X438  ---- SWIS-PUNKT            50.45   13.05   500    -41 LAND
99809       X439  ---- SWIS-PUNKT            50.50   10.24   700   -173 LAND
99810       X440  ---- SWIS-PUNKT            50.44   10.44   700    -31 LAND
99811       X441  ---- SWIS-PUNKT            50.44   10.35   900   -231 LAND
99812       X442  ---- SWIS-PUNKT            50.42   10.41   900   -231 LAND
99801       X443  ---- SWIS-PUNKT            50.55   12.22   300    -23 LAND
99802       X444  ---- SWIS-PUNKT            50.49   11.23   500   -134 LAND
99803       X445  ---- SWIS-PUNKT            50.44   11.10   500     -3 LAND
99804       X446  ---- SWIS-PUNKT            50.38   11.36   500     39 LAND
99805       X447  ---- SWIS-PUNKT            50.38   12.03   500    -15 LAND
99806       X448  ---- SWIS-PUNKT            51.14   11.33   300    -91 LAND
99807       X449  ---- SWIS-PUNKT            51.09   11.38   300    -67 LAND
99808       X450  ---- SWIS-PUNKT            51.00   12.09   300    -18 LAND
99809       X451  ---- SWIS-PUNKT            51.03   11.07   100     98 LAND
99810       X452  ---- SWIS-PUNKT            51.03   10.38   300      4 LAND
99811       X453  ---- SWIS-PUNKT            50.56   10.30   300      4 LAND
99812       X454  ---- SWIS-PUNKT            51.23   10.05   300     -3 LAND
99801       X455  ---- SWIS-PUNKT            51.58   12.22   100     26 LAND
99802       X456  ---- SWIS-PUNKT            51.55   12.10   100    -33 LAND
99803       X457  ---- SWIS-PUNKT            51.37   12.22   100     -9 LAND
99804       X458  ---- SWIS-PUNKT            51.14   11.55   100     48 LAND
99805       X459  ---- SWIS-PUNKT            51.09   12.07   100     43 LAND
99806       X460  ---- SWIS-PUNKT            52.20    7.43   100    -47 LAND
99807       X461  ---- SWIS-PUNKT            52.16    8.36   300   -220 LAND
99808       X462  ---- SWIS-PUNKT            50.53    6.07   100     -4 LAND
99809       X463  ---- SWIS-PUNKT            50.53    6.20   100     -4 LAND
99810       X464  ---- SWIS-PUNKT            50.46    6.26   100     -5 LAND
99811       X465  ---- SWIS-PUNKT            53.22    8.24   100    -98 LAND
99812       X466  ---- SWIS-PUNKT            52.22    8.00   100    -30 LAND
99801       X467  ---- SWIS-PUNKT            52.15   12.22   100    -50 LAND
99802       X468  ---- SWIS-PUNKT            51.59   12.57   100     -9 LAND
99803       X469  ---- SWIS-PUNKT            51.58   13.25   100      6 LAND
99804       X470  ---- SWIS-PUNKT            52.35   11.05   100    -38 LAND
99805       X471  ---- SWIS-PUNKT            51.20   12.56   100     25 LAND
99806       X472  ---- SWIS-PUNKT            50.59   14.13   500    -98 LAND
99807       X473  ---- SWIS-PUNKT            51.03   14.16   500   -113 LAND
99808       X474  ---- SWIS-PUNKT            51.04   14.32   500    -98 LAND
99809       X475  ---- SWIS-PUNKT            51.08   14.37   500    -98 LAND
99810       X476  ---- SWIS-PUNKT            51.44    9.28   500   -189 LAND
99811       X477  ---- SWIS-PUNKT            51.48    9.33   500   -189 LAND
99812       X478  ---- SWIS-PUNKT            51.47    9.36   500   -172 LAND
99801       X479  ---- MIDDELHAGEN           54.20   13.42    19    -17 LAND
99802       X480  ---- BLANDOW               54.34   13.35    48    -48 LAND
99803       X481  ---- BOHLENDORF            54.36   13.17     7     -7 LAND
99804       X482  ---- GNOIEN                53.58   12.42    19     -7 LAND
99805       X483  ---- HOEXTER               51.47    9.24    93    106 LAND
99806       X484  ---- HOGFGEISMAR           51.30    9.23   162     83 LAND
99807       X485  ---- BEVERN                51.52    9.30   110     18 LAND
99808       X486  ---- ORANIENBURG-STADT     52.45   13.15    35      6 LAND
99809       Z901  ---- HOERMOOS              47.30   10.00  1280   -315 BERG
99810       Z902  ---- HOCHGRATBAHN          47.30   10.04  1720   -755 BERG
99811       Z904  ---- KANZELWAND            47.20   10.12  1960   -666 BERG
99812       Z905  ---- FELLHORN              47.20   10.13  1610   -316 BERG
99801       Z907  ---- NEBELHORN             47.25   10.21  2200   -906 BERG
99802       Z908  ---- NEBELHORN-KOBLAT      47.25   10.21  2070   -776 BERG
99803       Z909  ---- SCHWARZENBERG         47.26   10.25  1355     73 BERG
99804       Z910  ---- TEGELBERG-RUECKEN     47.33   10.47  1680   -526 BERG
99805       Z911  ---- TEGELBERGBAHN         47.34   10.47  1720   -865 BERG
99806       Z912  ---- TEGELBERG             47.34   10.47  1710   -855 BERG
99807       Z914  ---- ZUGSPITZPLATT         47.24   10.59  2420   -877 BERG
99808       Z916  ---- PUERSCHLING           47.36   10.59  1370   -218 BERG
99809       Z917  ---- OSTERFELDER           47.26   11.04  1800   -257 BERG
99810       Z919  ---- KRANZBERG             47.27   11.14  1300   -123 BERG
99811       Z920  ---- MARCHKLAMM TAL        47.24   11.16   900    702 BERG
99812       Z921  ---- MARCHKLAMM            47.24   11.17  1600      2 BERG
99801       Z922  ---- BRUNNSTEINSPITZE      47.24   11.17  2030   -428 BERG
99802       Z923  ---- LINDERSPITZE-RINNE    47.26   11.18  2300   -698 BERG
99803       Z924  ---- LINDERSPITZE          47.26   11.18  2340   -738 BERG
99804       Z925  ---- FAHRENBERG            47.36   11.19  1575   -605 BERG
99806       Z926  ---- HERZOGSTANDBAHN       47.36   11.19  1625   -655 BERG
99806       Z928  ---- SCHROEDELSTEIN        47.40   11.31  1485   -754 BERG
99807       Z929  ---- BRAUNECK              47.40   11.31  1550   -819 BERG
99808       Z931  ---- BRECHERSPITZE         47.41   11.52  1600   -488 BERG
99809       Z932  ---- SPITZINGSEE           47.40   11.53  1100     12 BERG
99810       Z934  ---- WENDELSTEIN-SOIN      47.42   12.01  1580   -468 BERG
99811       Z936  ---- MOESLARNALM           47.45   12.21  1450   -747 BERG
99812       Z937  ---- KAMPENWAND            47.45   12.21  1520   -817 BERG
99801       Z939  ---- DUERRNBACHHORN        47.40   12.36  1580   -435 BERG
99802       Z940  ---- RAUSCHBERG            47.44   12.41  1635   -758 BERG
99803       Z942  ---- WARTSTEINKOPF         47.39   12.48  1755   -614 BERG
99804       Z943  ---- REITERALPE            47.39   12.48  1670   -529 BERG
99806       Z944  ---- WARTSTEINHUETTE       47.39   12.49  1615   -516 BERG
99806       Z946  ---- KUEHROINT             47.34   12.58  1420   -101 BERG
99807       Z947  ---- FUNTENSEETAUERN       47.29   12.58  2520   -800 BERG
99808       Z948  ---- HOELLGRABEN           47.37   13.00   660    659 BERG
99809       Z949  ---- JENNER                47.35   13.01  1200    119 BERG
99810       06678 ---- BISCHOFSZELL          47.30    9.14   470      8 LAND
99811       06647 ---- WUERENLINGEN          47.32    8.14   334     82 LAND
99808       10308 ---- NORDHORN              52.33    7.10    24     -1 LAND
99809       10619 ---- BAUMHOLDER            49.37    7.21   442    -44 LAND
99810       11113 ---- NAUDERS               46.53   10.30  1330    568 LAND
99809       F9600 ---- HEINERSCHEID          50.05    6.04   522    -64 LAND
99810       N9610 ---- WEI�ENFELS            51.12   11.58   100     17 LAND
99812       E273  ---- ROSENGARTEN-KLECKEN   53.22    9.57    82    -18 LAND
99801       H176  ---- KALLETAL NIEDERMEIEN  52.04    8.57   310    -88 LAND
99802       H250  ---- SENDENHORST_N         51.50    7.53    65      4 LAND
99803       H316  ---- RAESFELD KA           51.45    6.48    42      2 LAND
99804       H375  ---- LICHTENAU             51.37    8.54   304     -1 LAND
99805       H566  ---- MENDEN_LENDRINGSEN    51.24    7.50   170    -18 LAND
99806       H764  ---- ROTHE FURTH           51.05    7.19   230      1 LAND
99807       H789  ---- BREITENBACHTALSPERRE  50.59    8.05   410      6 LAND
99808       H813  ---- ESCHWEILER N          50.49    6.18   130      7 LAND
99809       H840  ---- BORNHEIM EICHENKAMP   50.47    7.01    57      1 LAND
99810       H910  ---- SIMMERATH N           50.38    6.18   460    -61 LAND
99811       J623  ---- DIFFERTEN             49.14    6.46   251    -10 LAND
99812       J736  ---- BALTERSWEILER         49.29    7.10   289      7 LAND
99801       J739  ---- BACHEM                49.30    6.42   220     16 LAND
99802       J927  ---- RIESWEILER            49.08    7.19   314    -23 LAND
99803       K060  ---- MAROTH                50.35    7.41   285     -6 LAND
99804       K082  ---- HERDORF               50.46    7.58   483     44 LAND
99807       K099  ---- LIEBENSCHEID          50.42    8.05   560    -33 LAND
99807       K242  ---- ADENAU                50.26    7.06   593    -94 LAND
99807       K376  ---- GONDERSHAUSEN         50.10    7.30   388     -1 LAND
99808       K399  ---- BERGHAUSEN            50.16    8.00   372      6 LAND
99809       K418  ---- K�RPERICH-GAYTALPARK  49.56    6.15   290     14 LAND
99810       K450  ---- NEEF                  50.05    7.08   133     86 LAND
99811       K550  ---- ENTENPFUHL            49.54    7.35   610   -145 LAND
99812       K552  ---- GAUCHSBERG            49.52    7.41   399      2 LAND
99801       K626  ---- HERMESKEIL            49.42    7.02   650    -92 LAND
99802       K748  ---- MARTINSH�HE           49.22    7.28   411     -1 LAND
99804       K756  ---- FRANKELBACH           49.31    7.39   417     -7 LAND
99804       K931  ---- HORTENKOPF            49.16    7.50   606   -233 LAND
99807       K996  ---- SCHAIDT               49.03    8.05   136      1 LAND
99807       L244  ---- GUDENSBERG            51.10    9.22   220    -14 LAND
99807       L314  ---- ANGELBURG-FRECHENHAU  50.49    8.26   435    -52 LAND
99808       L391  ---- BEBRA                 50.58    9.47   192    102 LAND
99809       L543  ---- GR�NBERG              50.35    8.59   314     -9 LAND
99811       L562  ---- FREIENSTEINAU         50.26    9.24   430     33 LAND
99811       L595  ---- GERSFELD_(RH�N)-DALH  50.25    9.50   667    -50 LAND
99801       L643  ---- NIDDA-KL�RANLAGE      50.24    8.59   132     56 LAND
99801       L731  ---- USINGEN               50.21    8.32   320     28 LAND
99802       L769  ---- FREIGERICHT-HORBACH   50.08    9.10   198    -18 LAND
99808       L918  ---- LORSCH-KL�RANLAGE     49.40    8.34    92     30 LAND
99808       Q824  ---- DACHSBERG-WOLPADINGE  47.42    8.07   880     21 LAND
99807       F9515 ---- GRONAU WEST           51.19    7.17    36     72 LAND
99808       F9516 ---- SOONWALD WEST 1       50.20    7.30   237    -29 LAND
99809       F9517 ---- SOONWALD WEST 2       49.59    7.47   294     35 LAND
99810       F9518 ---- SOONWALD WEST 3       50.19    7.30    73     64 LAND
99811       F9519 ---- SOONWALD WEST 4       49.56    7.49   262      1 LAND
99812       F9520 ---- WONNEGAU WEST 1       49.52    7.54   102     83 LAND
99801       F9521 ---- WONNEGAU WEST 2       47.54    8.20   811      1 LAND
99802       F9522 ---- WONNEGAU WEST 3       49.45    8.11   198     21 LAND
99803       F9523 ---- WONNEGAU WEST 4       49.47    8.08   181     38 LAND
99804       F9524 ---- WONNEGAU WEST 5       49.55    7.49   177      0 LAND
99805       F9525 ---- BRAUWEILER WEST 1     50.52    6.50    90     15 LAND
99806       F9526 ---- BRAUWEILER WEST 2     50.59    6.48    56     22 LAND
99807       F9527 ---- WALBERBERG WEST       50.51    6.53   116    -11 LAND
99808       F9528 ---- VILLE OST 1           50.53    6.54    57     21 LAND
99809       F9529 ---- VILLE OST 2           50.56    6.49    60     18 LAND
99810       F9530 ---- KUGELBERG O. / W. 1   49.13    8.50   240    -25 LAND
99811       F9531 ---- KUGELBERG O. / W. 2   48.58    9.10   258      1 LAND
99812       F9532 ---- KUGELBERG O. / W. 3   49.34    8.32   112    -16 LAND
99801       F9533 ---- KUGELBERG O. / W. 4   49.24    8.37   106     33 LAND
99802       F9534 ---- KUGELBERG O. / W. 5   49.04    9.02   190      2 LAND
99803       F9535 ---- KUGELBERG O. / W. 6   49.31    8.34   102     -6 LAND
99804       F9536 ---- KUGELBERG O. / W. 7   49.14    8.45   166     22 LAND
99805       F9537 ---- KUGELBERG O. / W. 8   49.00    9.07   271    -28 LAND
99808       10271 ---- NEURUPPIN-ALT RUPPIN  52.57   12.51    50     -6 LAND
99801       34615 ---- VOLNOVAKHA            47.37   37.29   267    -43 LAND
99801       12399 ---- TERESPOL              52.05   23.37   136      7 LAND
99802       13457 ---- TIVAT                 42.24   18.44   139    132 KUES
99803       13459 ---- NIKSIC                42.46   18.57   143    422 LAND
99804       13461 ---- BAR                   42.06   19.05   142    -29 MEER
99805       13463 ---- PODGORICA             42.26   19.17   154    -44 LAND
99810       26144 ---- LOGEVA                58.45   26.25   130    -46 LAND
99811       26215 EEKE ARENSBURG             58.13   22.31     3      1 MEER
99812       26258 ---- PSKOV                 57.49   28.20   132    -92 LAND
99801       26425 ---- JELGAVA               56.33   23.58   134   -122 LAND
99802       26544 ---- DAUGAVPILS            55.52   26.37   134     16 LAND
99803       26657 ---- DOKSICY               54.53   27.45   135     74 LAND
99804       26695 ---- LEPEL                 55.10   34.24   135     90 LAND
99805       26759 ---- BORISOV               54.16   28.30   135     42 LAND
99806       26763 ---- ORSHA                 54.30   30.27   133     54 LAND
99807       26774 ---- OGORKI                54.18   30.57   132     55 LAND
99808       26781 ---- SMOLENSK              54.45   32.04   132     63 LAND
99809       26832 ---- LIDA                  53.54   25.19   131     16 LAND
99810       26898 ---- BRYANSK               53.15   34.19   132     40 LAND
99811       26941 ---- BARANOVICHI           53.08   25.58   139     40 LAND
99812       26951 ---- SLUTSK                53.03   27.33   132     14 LAND
99801       26961 ---- BOBRUISK              53.13   29.08   135      6 LAND
99802       26966 ---- ZHLOBIN               52.54   30.03   134     -8 LAND
99805       27402 ---- TVER                  56.53   35.52   130      2 LAND
99810       33019 ---- PINSK                 52.07   26.07   133      7 LAND
99811       33036 ---- MOZYR                 52.02   29.12   133     14 LAND
99812       33088 ---- SARNY                 51.19   26.37   131     21 LAND
99801       33124 ---- BRAGIN                51.48   30.15   133     -1 LAND
99802       33135 ---- CHERNIGOV             51.27   31.12   136    -19 LAND
99803       33177 ---- VLADIMIR-VOLYNSKIJ    50.50   24.21   145     54 LAND
99804       33187 ---- LUTSK                 50.43   25.24   133     63 LAND
99805       33275 ---- SUMY                  50.52   34.45   130     34 LAND
99806       33301 ---- ROVNO                 50.36   26.09   131     78 LAND
99807       33317 ---- SHEPETIVKA            50.10   27.02   137    101 LAND
99808       33325 ---- ZHYTOMYR              50.17   28.40   136     92 LAND
99809       33393 ---- LIVIV                 49.48   23.58   143     80 LAND
99810       33415 ---- TERNOPOL              49.32   25.41   148    178 LAND
99811       33466 ---- MIRONOVKA             49.39   31.05   136      7 LAND
99812       33506 ---- POLTAVA               49.37   34.33   135    -13 LAND
99801       33562 ---- VINNITSA              49.15   28.36   148    131 LAND
99802       33614 ---- SVETLOVODSK           49.04   33.15   137    -61 KUES
99803       33631 ---- UZHGOROD              48.38   22.16   134     16 LAND
99804       33658 ---- CHERNOVTSY            48.16   25.58   136     84 LAND
99805       33664 ---- BRICENI               48.21   27.05   131     78 LAND
99806       33745 ---- BALTI                 47.47   27.57   129     15 LAND
99807       33749 ---- BRAVICEA              47.22   28.26   134     17 LAND
99808       33761 ---- LYUBASHEVKA           47.51   30.16   139     16 LAND
99809       33821 ---- DUBASARI              47.17   29.08   135     -3 LAND
99810       33829 ---- TIRASPOL              46.52   29.36   128     -9 LAND
99811       33883 ---- KOMRAT                46.18   28.38   129    -37 LAND
99812       33885 ---- CAHUL                 45.53   28.14   132    -10 LAND
99802       33889 ---- IZMAIL                45.22   28.51   133   -103 LAND
99802       33896 ---- SARATA                46.01   29.40   129    -97 LAND
99803       33902 ---- KHERSON               46.44   32.43   133   -107 LAND
99804       33934 ---- DZHANKOI              45.43   34.23    13      0 LAND
99805       33946 ---- SIMFEROPOL            45.02   33.58   142     18 KUES
99806       33994 ---- AYVOVE                44.44   33.39    41      5 KUES
99809       34415 ---- IZYUM                 49.11   37.17   131    -26 LAND
99811       G201  ---- BIRKENMOOR            50.19   10.53   320     10 LAND
99812       G202  ---- HOHENROTH             50.19   10.10   300     15 LAND
99801       G205  ---- MARKERSREUTH          50.13   11.49   556     -2 LAND
99802       G210  ---- BAD STAFFELSTEIN      50.07   11.00   258     62 LAND
99803       G213  ---- BRAUNERSGRUEN         50.05   12.06   590    -14 LAND
99804       G214  ---- KOESLAU               50.04   10.40   400    -76 LAND
99805       G220  ---- STEINFELD             49.57    9.40   300    -10 LAND
99806       G222  ---- GROSSOSTHEIM          49.56    9.03   129     59 LAND
99807       G225  ---- MISTELBACH            49.54   11.30   410     51 LAND
99808       G237  ---- SCHWARZENAU           49.48   10.13   200     47 LAND
99809       G250  ---- DIETZHOF              49.42   11.10   363    -22 LAND
99810       G255  ---- HEPPDIEL              49.40    9.22   335     -9 LAND
99811       G258  ---- EDELSFELD             49.35   11.42   528    -54 LAND
99812       G262  ---- NEUHERBERG            49.31   10.17   380    -13 LAND
99801       G271  ---- WULLNHOF              49.23   12.36   510      3 LAND
99802       G273  ---- IRRENLOHE             49.23   12.06   363     74 LAND
99803       G298  ---- SARCHING              49.01   12.14   330     29 LAND
99804       G303  ---- KIRCHBERG IM WALD     48.54   13.11   624    -28 LAND
99805       G306  ---- WALLERSTEIN           48.53   10.30   420     31 LAND
99806       G313  ---- UTTENKOFEN            48.49   12.51   323      3 LAND
99807       G321  ---- FEISTENAICH           48.42   12.20   460    -43 LAND
99808       G324  ---- KRINGELL              48.41   13.30   450    -30 LAND
99809       G330  ---- STEINBEISSEN          48.36   12.44   380     45 LAND
99810       G340  ---- AINERTSHOFEN          48.31   11.05   470    -44 LAND
99806       G342  ---- WEISSINGEN            48.27   10.09   455      7 LAND
99806       G352  ---- BAERNAU               48.23   13.23   310     33 LAND
99807       G357  ---- FRIEDING              48.20   12.50   480    -37 LAND
99807       G372  ---- KIRCHHEIM             48.11   10.28   536     40 LAND
99808       G378  ---- OSTERSEEON            48.04   11.55   560     -5 LAND
99808       G384  ---- NILLING               48.02   12.49   390      8 LAND
99808       G385  ---- ROTHENFELD            47.58   11.13   690      2 LAND
99808       F9435 ---- HALLE DIESELSTR. HKW  51.28   12.00   105     -3 LAND
99702       F9434 ---- RUKLA                 55.03   24.24    80      7 LAND

TABLE St 99999 99991 gmos 99792 ecmgl 99791 gmegl
clu   CofX  id    ICAO name                 nb.    el.     elev  Hmod-H type
===== ----- ===== ---- -------------------- ------ ------- ----- ------ ----
99702   371 01001 ENJA JAN MAYEN             70.56   -8.40    10     29 KUES
99703   431 01008 ENSB SVALBARD              78.15   15.28    29    342 KUES
99704   414 01025 ---- TROMSOE               69.41   18.55    10    152 KUES
99701   422 01028 ENBJ BJORNOYA              74.31   19.01    16     14 KUES
99702   221 01049 ENAT ALTA LUFTHAVN         69.59   23.22     3    202 KUES
99703   135 01052 ENHF HAMMERFEST            70.40   23.40    81     24 KUES
99704   159 01089 ENKR KIRKENES              69.44   29.54    91    -24 KUES
99701    91 01092 ---- MAKKAUR FYR           70.43   30.04     9    191 KUES
99702   422 01152 ENBO BODOE                 67.16   14.22    13     42 KUES
99703   216 01180 ---- HARSTAD               68.48   16.32    45    112 KUES
99704   321 01210 ENAL ALESUND AIRP          62.34    6.07    22     91 KUES
99701   389 01238 ---- FOKSTUA 2             62.07    9.17   973    -72 LAND
99702   462 01241 ENOL ORLAND                63.42    9.36     7     54 KUES
99703   331 01271 ENVA TRONDHEIM             63.28   10.55    17     65 LAND
99702   135 01366 ---- SOGNEFJELL            61.34    8.00  1415    -34 LAND
99703   303 01380 ---- VENABU                61.39   10.07   940      2 LAND
99702   254 02049 ESNG GALLIVARE APT         67.09   20.39   359    -12 LAND
99703   463 02186 ESPA LULEA                 65.33   22.08    17     -1 KUES
99704   164 02226 ESPC FROSON                63.12   14.30   376    -39 LAND
99701   164 02267 ---- ORNSKOLDSVIK          63.18   18.41    24     28 KUES
99702   365 02284 ---- JAERNAESKLUBB         63.26   19.41     6      8 KUES
99703   164 02286 ESNU UMEA                  63.48   20.17     7     44 KUES
99704   310 02355 ---- KUGGOEREN AMOS        61.42   17.31     9      7 KUES
99701   164 02366 ESNN TIMRA/MIDLANDA        62.31   17.27     3     27 LAND
99703    61 02752 ---- KRISTIINANKAUPUNGIN   62.12   21.10     2      8 MEER
99704   230 02807 EFIV IVALO                 68.37   27.25   147     46 LAND
99701    37 02830 EFKT KITTILA               67.42   24.51   196     12 LAND
99702   262 02836 EFSO SODANKYLA             67.22   26.39   179     25 LAND
99703   230 02847 ---- ROVANIEMI             66.30   25.43    85     43 LAND
99704   230 02869 EFKS KUUSAMO               65.58   29.11   262     16 LAND
99701   174 02876 ---- OULU                  65.01   25.23     3     14 KUES
99702   230 02897 EFKI KAJAANI               64.17   27.41   143     11 LAND
99703   247 02915 ---- VIITASAARI            63.05   25.52   132    -14 LAND
99704   230 02917 EFKU KUOPIO                63.01   27.48    98     -6 LAND
99701   230 02929 EFJO JOENSUU APT           62.40   29.38   119    -27 LAND
99702   258 02935 EFJY JYVASKYLA             62.24   25.41   141     14 LAND
99704   247 02947 ---- MIKKELI               61.44   27.18   138    -23 LAND
99701   230 02948 EFSA SAVONLINNA            61.57   28.57    95      0 LAND
99702   372 04018 BIKF KEFLAVIK              63.58  -22.36    52    -27 LAND
99703   372 04030 BIRK REYKJAVIK             64.08  -21.54    54    -36 KUES
99704   372 04063 BIAR AKUREYRI              65.41  -18.05    23    142 KUES
99701   372 04097 ---- DALATANGI             65.16  -13.35     9    172 KUES
99702   425 04231 BGSF SONDRESTROMFJORD      67.01  -50.42    50     26 LAND
99703   293 04250 ---- GODTHAB NUUK          64.10  -51.45    80    -80 KUES
99704   408 04270 BGBW NARSARSUAQ            61.09  -45.26     4    160 KUES
99701   290 04320 BGDH DANMARKSHAVN          76.46  -18.40    11    135 KUES
99702    66 04330 BGDB DANEBORG              74.18  -20.13    44     77 KUES
99703   433 04360 BGAM TASIILAQ              65.36  -37.38    50     12 KUES
99704   219 04361 BGKK KULUSUK               65.34  -37.08    35     10 KUES
99701   410 06011 ---- FAROEER               62.01   -6.46    54     74 KUES
99704   461 08501 LPFL FLORES/AZOREN         39.27  -31.08    28    -11 KUES
99701   398 08505 LPHR AZOREN                38.31  -28.43    40    129 KUES
99702   449 08509 LPLA LAJES/AZOREN          38.46  -27.06    52    118 KUES
99703   455 08515 LPAZ SANTA MARIA           36.58  -25.10   100    -49 KUES
99704   453 08521 LPFU FUNCHAL               32.41  -16.46    58    233 KUES
99704   256 08589 ---- CAP VERDEN/PRAIA      14.54  -23.31    27     11 MEER
99701   412 08594 GVAC SAL                   16.44  -22.57    54    -42 KUES
99702   440 17038 LTCG TRABZON               41.00   39.43    35    233 KUES
99704   438 17096 LTCE ERZURUM               39.55   41.16  1756     59 LAND
99703   432 17170 LTCI VAN                   38.27   43.19  1669    123 LAND
99701   446 17280 LTCC DIYARBAKIR            37.53   40.12   687    -32 LAND
99701   405 20087 ---- OSTROV GOLOMJANNYJ    79.33   90.37     8     -8 KUES
99702   405 20674 ---- OSTROV DIKSON         73.30   80.24    47    -35 KUES
99703   405 21824 UEST TIKSI                 71.35  128.55     7     55 KUES
99704   428 22113 ULMM MURMANSK              68.58   33.03    51     11 LAND
99701   410 22550 ULAA ARCHANGELSK           64.35   40.30    13     -6 KUES
99702   411 22583 ---- KOJNAS                64.45   47.39    63     67 LAND
99703   428 22802 ---- SORTAVALA             61.43   30.43    19     -3 LAND
99704   428 22820 ULPP PETROSK               61.49   34.16   110      9 LAND
99701   405 23256 USDT TAZOVSKOE             67.28   78.44     8     -2 LAND
99702   410 23330 USDD SALEHARD              66.32   66.40    16     -6 LAND
99703   411 23472 UOTT TURUHANSK             65.47   87.56    38    -20 LAND
99704   411 23631 USHB BEREZOVO              63.56   65.03    32    -26 LAND
99701   423 23734 ---- OKTJABRSKOE           62.27   66.03    72    -32 LAND
99702   411 23804 UUYY SYKTYVKAR             61.40   50.51   116     -8 LAND
99703   398 23849 ---- SURGUT                61.15   73.30    55    -21 LAND
99704   406 24125 ---- OLENEK                68.30  112.26   220    -31 LAND
99701   410 24266 ---- VERHOJANSK            67.33  133.23   137     91 LAND
99702   410 24688 ---- OJMJAKON              63.15  143.09   741     52 LAND
99703   411 24959 UEEE JAKUTSK               62.01  129.43   101     51 LAND
99704   411 27051 ULWT TOTMA                 59.53   42.45   134      5 LAND
99701   422 27113 ---- CEREPOVEC             59.15   37.58   114     -3 LAND
99702   423 27459 UWGG NIZHNY NOVGOROD       56.14   43.47    78     35 LAND
99703   404 27595 UWKD KAZAN                 55.36   49.17   116     -1 LAND
99704   421 27612 UUUU MOSKAU                55.45   37.34   156      6 LAND
99701   428 27719 ---- TULA                  54.14   37.37   165     32 LAND
99702   410 27730 ---- RYAZAN                54.38   39.42   158    -28 LAND
99703   411 27962 ---- PENZA                 53.07   45.01   174     12 LAND
99704   421 28076 ---- DEMJANSKOE            59.36   69.17    57    -24 LAND
99701   405 28382 ---- UST-ISIM              57.41   71.11    62      2 LAND
99702   410 28440 USSS EKATERINBURG          56.48   60.38   237     28 LAND
99703   411 28698 UNOO OMSK                  55.01   73.23   122    -15 LAND
99704   410 28722 UWUU UFA                   54.43   55.50   104     21 LAND
99701   389 28952 UAUU KUSTANAI              53.13   63.37   156     17 LAND
99702   406 29122 ---- KARGASOK              59.03   80.57    59     -9 LAND
99703   406 29430 ---- TOMSK                 56.28   84.58   130    -20 LAND
99704   411 29838 UNBB BARNAUL               53.26   83.31   184    -51 LAND
99701   405 30054 UERT VITIM                 59.27  112.35   190    134 LAND
99702   411 30309 UIBB BRATSK                56.17  101.45   416    -30 LAND
99703   411 30433 ---- NIZHNEANGARSK         55.47  109.33   487    -26 LAND
99704   407 30521 ---- ZHIGALOVO             54.48  105.13   426    130 LAND
99701   411 30710 UIII IRKUTSK               52.16  104.21   485    -24 LAND
99702   406 30731 ---- GORJACINSK            52.59  108.17   488     40 LAND
99703   411 30758 UIAA CHITA                 52.05  113.29   671     24 LAND
99704   404 31088 UHOO OKHOTSK               59.22  143.12     6     43 KUES
99701   406 31300 ---- ZEJA                  53.42  127.18   229     32 LAND
99702   406 31478 ---- SOFIJSKIJ PRIISK      52.16  133.59   902     65 LAND
99703   406 31735 UHHH HABAROVSK             48.31  135.10    76    -15 LAND
99704   404 31960 UHWW VLADIVOSTOK           43.07  131.54   138    -79 KUES
99701   406 32053 ---- NOGLIKI               51.55  143.08    34    -15 LAND
99702   410 32150 UHSS JUZHNO-SAKHALINSK     46.57  142.43    24     54 LAND
99703   410 32215 ---- SEVERO-KURILSK        50.41  156.08    23     35 KUES
99704   411 32389 ---- KLJUCHI               56.19  160.50    29      2 LAND
99701   405 32408 UHPK UST'KAMCHATSK         56.13  162.43    27    -25 KUES
99703   406 34123 UUOO VORONEZ               51.42   39.13   149    -41 LAND
99704   405 34152 ---- BALASHOV              51.33   43.09   154    -10 LAND
99703   400 34560 URWW VOLGOGRAD             48.47   44.22   134    -11 LAND
99704   406 34880 URWA ASTRAHAN              46.17   48.03   -23      7 LAND
99701   427 35108 UARR URALSK                51.15   51.17    37     10 LAND
99702   422 35121 UWOO ORENBURG              51.41   55.06   117     -6 LAND
99703   412 35188 ---- TSELINOGRAD           51.07   71.22   342     -4 LAND
99704   419 35229 UATT AKTJUBINSK            50.17   57.09   219     18 LAND
99701   384 35358 ---- TORGAI                49.38   63.30   123    -31 LAND
99702   427 35394 UAKK KARAGANDA             49.48   73.09   553    -21 LAND
99703   419 35746 ---- ARAL'SK               46.47   61.39    62    -16 LAND
99704   399 36870 UAAA ALMA-ATA              43.14   76.56   847    107 LAND
99701   418 37171 ---- SOTSCHI               43.27   39.54    16     37 KUES
99702   411 37228 ---- WLADIKAVKAZ           43.03   44.39   703    -17 LAND
99703   416 37788 UDYZ YEREVAN ZVARTNOTS     40.09   44.23   854     -2 LAND
99704   388 37864 UBBB BAKU/BINA             40.27   50.04    -6     28 KUES
99701   421 38353 ---- BISHKEK               42.51   74.32   756    -16 LAND
99702   393 38457 UTTT TASCHKENT             41.16   69.16   428     -7 LAND
99703   393 38507 ---- KRASNOVODSK           40.03   53.00    89     -8 LAND
99704   429 38545 ---- DARGANATA             40.28   62.17   143     10 LAND
99701   389 38696 UTSS SAMARKAND             39.34   66.57   724    -11 LAND
99702   409 38836 UTDD DUSHANBE              38.33   68.47   800     32 LAND
99703   388 38880 UTAA ASHKHABAD             37.58   58.20   228    -32 LAND
99704   393 38927 UTST TERMEZ                37.14   67.16   310    -12 LAND
99701   381 38954 ---- KHOROG                37.30   71.31  2077    811 LAND
99704   372 40362 OERF RAFHA                 29.37   43.29   449     -2 LAND
99701   304 40375 OETB TABUK                 28.23   36.36   778     -5 LAND
99702   267 40416 OEDR DHAHRAN INTL          26.16   50.09    26      8 KUES
99703   288 40430 OEMA AL MADINAH            24.33   39.42   654     26 LAND
99704   372 40437 OERK RIAD INT.AIRPORT      24.56   46.43   614     28 LAND
99701   450 40582 OKBK KUWAIT                29.13   47.59    55     -1 KUES
99702   419 40704 OITQ AHAR                  38.26   47.04  1390     66 LAND
99703   419 40719 OIGG RASHT                 37.12   49.38    37     61 LAND
99704   411 40745 OIMM MASHHAD               36.16   59.38   989     -9 LAND
99701   411 40747 OICS SANANDAJ              35.20   47.00  1373    217 LAND
99702   408 40754 OIII TEHERAN               35.41   51.21  1204   -106 LAND
99703   411 40762 DIMH TORBAT-HEYDARIEH      35.16   59.13  1333     -5 LAND
99704   411 40766 OICC KERMANSHAH            34.16   47.07  1320     -7 LAND
99701   419 40768 ---- HAMEDAN               34.52   48.32  1749    -23 LAND
99702   419 40794 OIAS SAFI-ABAD DEZFUL      32.16   48.26    82     -3 LAND
99703   411 40800 OIFM ESFAHAN               32.28   51.43  1550    -11 LAND
99704   419 40835 OIAH GACH SARAN DU GUNBA.  30.26   50.46   699     14 LAND
99701   411 40848 OISS SHIRAZ                29.32   52.35  1486     15 LAND
99702   411 40854 OIKM BAM                   29.06   58.24  1067    -31 LAND
99703   419 40875 OIKB BANDARABBASS          27.13   56.22    10     35 LAND
99704   220 41024 OEJN JEDDAH/KING ABDUL     21.42   39.11    15      9 KUES
99701   188 41030 ---- MAKKAH                21.26   39.46   240     27 LAND
99702   357 41170 OTBD DOHA-INT.AIRPORT      25.15   51.34    11     -5 KUES
99703   372 41184 OMRK RAS AL KHAIMAH        25.37   55.56    31      7 KUES
99704   416 41194 OMDB DUBAI                 25.15   55.20     8      0 KUES
99701   385 41196 OMSJ SHARJAH               25.20   55.31    35      8 KUES
99702   373 41217 OMAA ABU DHABI/INTL.       24.26   54.39    27    -11 KUES
99703   373 41218 OMAL AL AIN AIRPORT        24.16   55.36   265    -23 LAND
99704   126 41242 ---- DIBBA                 25.37   56.15    20    158 KUES
99701   126 41244 OOBR BURAIMI               24.14   55.47   299     11 LAND
99702   384 41246 OOSH SOHAR MAJIS           24.28   56.38     4      3 KUES
99703   117 41253 ---- RUSTAQ                23.25   57.26   322     43 LAND
99704   141 41254 OOSQ SAIQ                  23.04   57.39  1755    -22 LAND
99701   358 41255 ---- NIZWA                 22.51   57.32   492     43 LAND
99702   384 41256 OOMS SEEB-INT.AIRPORT      23.35   58.17    15      6 KUES
99703    97 41257 ---- SAMAIL                23.18   57.56   414    -10 LAND
99704   105 41258 ---- QABOOS PORT           23.38   58.34     4     39 KUES
99701    79 41262 OOFD FAHUD                 22.21   56.29   170      9 LAND
99702   126 41263 ---- BAHLA                 22.59   57.18   589    -25 LAND
99703   130 41264 ---- ADAM                  22.23   57.31   285     35 LAND
99704   310 41265 ---- IBRA                  22.44   58.31   469     42 LAND
99701   117 41267 ---- QALHAT                22.40   59.24    11    216 KUES
99702   370 41268 OOSR SUR                   22.32   59.29    14    214 KUES
99703   370 41288 OOMA MASIRAH               20.40   58.54    19     -9 KUES
99704   104 41304 OONR MARMUL                18.08   55.11   269     33 LAND
99701   165 41312 ---- RAYSUT PORT           16.55   53.55    33    110 KUES
99702   381 41314 OOTH THUMRAIT              17.40   54.02   467    -26 LAND
99703   121 41315 ---- QAIROON HAIRITI       17.15   54.05   878    -19 LAND
99704   416 41316 OOSA SALALAH               17.02   54.05    20     18 KUES
99701   379 41571 OPRN ISLAMABAD             33.37   73.06   507     -5 LAND
99702   383 41620 OPZB ZHOB                  31.21   69.28  1405    -27 LAND
99703   385 41640 OPLH LAHORE CITY           31.33   74.20   214    -10 LAND
99704   383 41696 OPKL KALAT                 29.02   66.35  2015     -2 LAND
99701   391 41749 OPNH NAWABSHAH             26.15   68.22    37    -16 LAND
99702   385 41780 OPKC KARACHI               24.54   67.08    21     13 KUES
99703   415 41923 VGTJ DHAKA                 23.46   90.23     8     -4 LAND
99704   415 41950 ---- BARISAL               22.45   90.22     4     -2 LAND
99701   415 41978 VGEG CHITTAGONG            22.16   91.49     4      3 KUES
99702   383 42182 VIDD NEW DELHI/SAFDARJUNG  28.35   77.12   211      8 LAND
99703   211 42260 VIAG AGRA                  27.09   77.58   168     -2 LAND
99704   383 42348 VIJP JAIPUR/SANGANER       26.49   75.48   385    -46 LAND
99701   383 42369 VILK LUCKNOW               26.45   80.53   122      1 LAND
99702   389 42809 VECC CALCUTTA              22.39   88.27     4      7 LAND
99703   383 42867 ---- NAGPUR SONEGAON       21.06   79.03   308    -16 LAND
99704   383 43003 VABB BOMBAY AIRPORT        19.07   72.51     8     11 KUES
99701   383 43128 VOHY HYDERABAD AIRPORT     17.27   78.28   530      9 LAND
99702   383 43279 VOMM MADRAS                13.00   80.11    10      5 LAND
99703   383 43371 ---- THIRUVANANTHAPURAM     8.29   76.57    60    -55 KUES
99704   391 43450 ---- KATUNAYAKE             7.10   79.53     8      7 KUES
99701   379 43466 VCBI COLOMBO                6.54   79.52     7     37 KUES
99702   383 43467 VCCC RATMALANA              6.49   79.53     5     24 KUES
99703   391 43555 VRMM MALE                   4.12   73.32     2     -2 KUES
99704   391 43599 VRGN GAN                   -0.41   73.09     2     -2 KUES
99701   422 44275 ---- BAYANBULAG            46.50   98.05  2255      6 LAND
99702   423 44292 ZMUB ULAAN-BAATOR          47.55  106.52  1307     14 LAND
99703   244 44434 ---- POKHARA               28.12   83.59   827    -65 LAND
99704   224 44438 ---- BHAIRAWA AIRPORT      27.31   83.27   109    -20 LAND
99701   371 44454 VNKT KATHMANDU             27.42   85.22  1337     19 LAND
99702   396 45007 VHHH HONGKONG              22.20  114.11     5     66 KUES
99703   221 45011 VMMC MACAO                 22.12  113.32    57    -25 KUES
99704   385 47008 ---- CHONGJIN              41.47  129.49    42    -29 KUES
99701   385 47016 ---- HYESAN                41.24  128.10   715    191 LAND
99702   385 47041 ---- HAMHEUNG              39.56  127.33    15     60 KUES
99703   385 47050 ---- ANJU                  39.37  125.39    34    -19 KUES
99704   385 47055 ---- WONSAN                39.11  127.26    35     -7 KUES
99701   385 47058 ZKPY PYONGYANG             39.02  125.47    36    -19 LAND
99702   341 47101 ---- CHUNCHON              37.54  127.44    74    113 LAND
99703   243 47105 ---- KANGNUNG              37.45  128.53    27     76 KUES
99704   328 47106 RKSB TONGHAE/RADAR         37.30  129.08    40      5 LAND
99701   397 47108 RKSL SEOUL                 37.34  126.58    86    -15 LAND
99702   328 47114 ---- WONJU                 37.20  127.57   149      9 LAND
99703   328 47127 ---- CHUNGJU               36.58  127.57   113     94 LAND
99704   397 47133 RKTD TAEJON                36.18  127.24    77     -4 LAND
99701   397 47136 ---- ANDONG                36.34  128.43   140      8 LAND
99702   397 47138 ---- POHANG                36.02  129.23     6     43 KUES
99703   397 47143 RKTT TAEGU                 35.53  128.37    58     26 LAND
99704   397 47146 RKTC CHONJU                35.49  127.09    54     18 LAND
99701   397 47152 ---- ULSAN                 35.33  129.19    32      3 KUES
99702   397 47156 ---- KWANGJU               35.10  126.53    70     41 LAND
99703   395 47189 ---- SOGWIPO               33.14  126.34    52     89 KUES
99704   360 47407 ---- ASAHIKAWA             43.46  142.22   116    -19 LAND
99701   360 47412 RJCO SAPPORO               43.03  141.20    17      0 KUES
99702   360 47430 ---- HAKODATE              41.49  140.45    43    -16 KUES
99703   361 47575 ---- AOMORI / HONSHU       40.49  140.46     3     11 KUES
99704   360 47584 ---- MORIOKA               39.42  141.10   155     43 LAND
99701   360 47590 ---- SENDAI                38.16  140.54    39     -5 KUES
99702   359 47604 ---- NIIGATA               37.55  139.03     2      0 KUES
99703   247 47610 ---- NAGANO                36.40  138.11   418     49 LAND
99704   360 47662 RJTD TOKYO NARITA          35.41  139.46     5      8 LAND
99701   360 47746 ---- TOTTORI / HONSHU      35.29  134.14    15     61 KUES
99702   359 47765 ---- HIROSHIMA             34.24  132.28    53     46 KUES
99703   360 47772 ---- OSAKA                 34.41  135.31    23    -19 KUES
99704   360 47807 ---- FUKUOKA               33.35  130.23     3     12 KUES
99701   360 47815 RJFO OITA                  33.14  131.37     5     18 KUES
99702   360 47827 ---- KAGOSHIMA             31.34  130.33     4     52 KUES
99703   360 47830 ---- MIYAZAKI              31.55  131.25     6     18 KUES
99704   245 47893 ---- KOCHI                 33.34  133.33     1    117 KUES
99701   245 47895 ---- TOKUSHIMA / SHIKOKU   34.04  134.35     6     20 KUES
99702   307 48042 ---- MANDALAY              21.59   96.06    74      1 LAND
99703   313 48062 VYSW SITTWE                20.08   92.53     4      1 KUES
99704   388 48097 ---- YANGON                16.46   96.10    14     -8 LAND
99701   400 48327 VTCC CHIANG MAI            18.47   98.59   312      2 LAND
99702   400 48429 VTBS BANGKOK/SUVARNABHUMI  13.41  100.46     2      0 KUES
99703   400 48455 ---- BANGKOK               13.44  100.34     3      0 KUES
99704   400 48456 VTBD BANGKOK/DON MUANG     13.55  100.36     4      2 KUES
99701   400 48461 ---- PHATTHAYA             12.55  100.52    59    -47 KUES
99702   400 48475 ---- HUA HIN               12.35   99.57     5     26 KUES
99703   400 48550 ---- KOH SAMUI              9.27  100.02     4    113 KUES
99704   400 48564 VTSP PHUKET                 7.53   98.24     2     36 KUES
99701   400 48569 ---- HAT YAI                6.55  100.26    27     48 LAND
99702   404 48601 WMKP PENANG-BAYANLEPAS      5.18  100.15     3     57 KUES
99703   404 48620 ---- SITIAWAN               4.13  100.42     7      2 KUES
99704   404 48647 WMKK KUALA LUMPUR           3.07  101.33    27     47 LAND
99701   404 48657 ---- KUANTAN                3.37  103.13    18     11 KUES
99702   417 48698 WSSS SINGAPUR               1.22  103.59     5      6 KUES
99703   392 48855 VVDN DA NANG               16.02  108.11     7      5 KUES
99704   287 48930 ---- LUANG-PRABANG         19.53  102.08   305    109 LAND
99701   293 48940 ---- VIENTIANE             17.57  102.34   171     -7 LAND
99702    41 48991 VDPP PHNOM-PENH/POCHENT.   11.33  104.51    10     11 LAND
99703   450 50774 ---- YICHUN (NORTH)        47.43  128.54   232     54 LAND
99704   404 50854 ---- ANDA                  46.23  125.19   150     -4 LAND
99701   453 50953 ZYHB HARBIN                45.45  126.46   143      8 LAND
99702   462 51463 ZWWW URUMQI                43.47   87.37   919     46 LAND
99703   465 51709 ZWSH KASHI                 39.28   75.59  1291      3 LAND
99704   409 51730 ---- ALAR                  40.30   81.03  1013     -6 LAND
99701   462 51765 ---- TIKANLIK              40.38   87.42   847     -8 LAND
99702   409 51818 ---- PISHAN                37.37   78.17  1376      9 LAND
99703   407 52436 ---- YUMENZHEN             40.16   97.02  1527     16 LAND
99704   465 52495 ---- BAYAN MOD             40.45  104.30  1329     44 LAND
99701   426 52866 ---- XINING                36.37  101.46  2262    103 LAND
99702   414 53487 ZBDT DATONG                40.06  113.20  1069     -3 LAND
99703   465 53513 ---- LINHE                 40.46  107.24  1041     10 LAND
99704   416 53698 ---- SHIJIAZHUANG          38.15  114.25    81      4 LAND
99701   450 53959 ---- YUNCHENG              35.02  111.01   376      3 LAND
99702   461 54102 ZBXH XILINHOT              43.57  116.04   991     23 LAND
99703   450 54161 ---- CHANGCHUNG            43.54  125.13   231    -20 LAND
99704   465 54218 ZBCF CHIFENG               42.16  118.58   572     31 LAND
99701   410 54324 ---- CHAOYANG              41.33  120.27   167     99 LAND
99702   454 54342 ---- SHENYANG              41.46  123.26    43     -3 LAND
99703   462 54423 ---- CHENGDE               40.58  117.55   374     74 LAND
99704   462 54471 ---- YINGKOU               40.40  122.12     4      1 KUES
99701   453 54497 ---- DANDONG               40.05  124.20    14     -8 KUES
99702   458 54511 ZBAA PEKING                39.56  116.17    55      6 LAND
99703   410 54527 ---- TIANJIN               39.06  117.10     5     -1 LAND
99704   465 54662 ZYTL DALIAN                38.54  121.38    97    -79 KUES
99701   465 54753 ---- LONGKOU               37.37  120.19     5     16 KUES
99702   461 54823 ZSTN JINAN                 36.36  117.03   169    -35 LAND
99703   464 54843 ---- WEIFANG               36.42  119.05    31     42 LAND
99704   461 54857 ZSQD QUINGDAO              36.04  120.20    77    -62 KUES
99701   400 55472 ---- XAINZA                30.57   88.38  4670    139 LAND
99702   444 55578 ---- XIGAZE                29.15   88.53  3837    136 LAND
99703   436 55591 ---- LHASA                 29.40   91.08  3650    143 LAND
99704   431 56187 ---- WENJIANG              30.42  103.50   541    -16 LAND
99701   404 56196 ---- MIANYANG              31.28  104.41   472     63 LAND
99702   441 56571 ---- XICHANG               27.54  102.16  1599    -25 LAND
99703   441 56778 ZPPP KUNMING/WUJIABA       25.01  102.41  1892     17 LAND
99704   408 57025 ---- FENGXIANG             34.31  107.25   781    -26 LAND
99701   450 57083 ZHCC ZHENGZHOU             34.43  113.39   111     -3 LAND
99702   447 57245 ---- ANKANG                32.43  109.02   291    127 LAND
99703   453 57411 ---- NANCHONG              30.48  106.05   310     12 LAND
99704   437 57461 ---- YICHANG               30.42  111.18   134     13 LAND
99701   452 57494 ---- WUHAN                 30.37  114.08    23     -5 LAND
99702   437 57516 ---- CHONGQING             29.31  106.29   351     -9 LAND
99703   408 57598 ---- YINING                29.02  114.35   147     58 LAND
99704   450 57662 ---- CHANGDE               29.03  111.41    35      2 LAND
99701   453 57687 ---- CHANGSHA              28.14  112.52    68      6 LAND
99702   395 57793 ---- YICHUN                27.48  114.23   129    -18 LAND
99703   449 57816 ZUGY GUIYANG               26.29  106.39  1222     -4 LAND
99704   438 57957 ---- GUILIN                25.20  110.18   166     -6 LAND
99701   450 57972 ---- CHENZHOU              25.48  113.02   185     50 LAND
99702   449 58027 ZSXZ XUZHOU                34.17  117.09    42     12 LAND
99703   452 58040 ---- GANYU                 34.51  119.08    10     13 KUES
99704   450 58221 ZSBB BENGBU                32.57  117.22    22      5 LAND
99701   450 58238 ZSNJ NANJING               31.44  118.51    12     -9 LAND
99702   453 58362 ZSPD SHANGHAI PUDONG       31.24  121.28     8      0 LAND
99703   453 58424 ---- ANQING                30.32  117.03    20     25 LAND
99704   449 58457 ZSHC HANGZHOU              30.14  120.10    43    -30 KUES
99701   453 58477 ---- DINGHAI               30.02  122.07    37     37 KUES
99702   453 58527 ZSJD JINGDEZHEN            29.18  117.12    60      1 LAND
99703   453 58752 ---- RUI'AN                27.47  120.39    38     -4 KUES
99704   450 58847 ---- FUZHOU                26.05  119.17     9     71 KUES
99701   402 58968 RCTP TAIBEI                25.02  121.31     9     39 LAND
99702   393 59046 ---- LIUZHOU               24.21  109.24    97     15 LAND
99703   447 59134 ZSAM XIAMEN                24.29  118.05   139   -111 KUES
99704   438 59211 ---- BAISE                 23.54  106.36   175     89 LAND
99701   450 59287 ZGGG GUANGZHOU             23.08  113.19     8      3 LAND
99702   450 59316 ---- SHANTOU               23.21  116.40     4     17 KUES
99703   449 59431 ZGNN NANNING               22.49  108.21   126    -41 LAND
99704   442 59493 ZGSZ SHENZHEN HUANGTIAN    22.38  113.49     4     39 LAND
99701   453 59644 ---- BEIHAI                21.29  109.06    16     -3 KUES
99702   442 59658 ZGZJ ZHANJIANG             21.13  110.24    28    -21 KUES
99703   450 59663 ---- YANGJIANG             21.52  111.58    22     -8 LAND
99704   447 59758 ZGHK HAIKOU                20.02  110.21    24    -14 KUES
99701   444 59948 ---- YA XIAN               18.14  109.31     7     51 KUES
99702   339 60005 GCLA LA PALMA              28.37  -17.45    29    -15 KUES
99703   326 60015 GCXO TENERIFE NORTE        28.28  -16.19   632     -6 KUES
99704   418 60020 ---- SANTA CRUZ DE TENE.   28.28  -16.16    35    286 KUES
99701   418 60025 GCTS TENERIFE SUR          28.03  -16.34    64    111 KUES
99702   418 60030 GCLP LAS PALMAS            27.56  -15.23    24    111 KUES
99703   367 60035 GCFV FUERTEVENTURA         28.27  -13.52    22     87 KUES
99704   385 60040 GCRR LANZAROTE             28.57  -13.36    14    107 KUES
99704   412 60630 DAUI IN-SALAH              27.14    2.30   268     27 LAND
99701   404 60680 DAAT TAMANRASSET           22.47    5.31  1378    -37 LAND
99702   391 61024 DRZA AGADEZ                16.58    7.59   501      9 LAND
99703   417 61052 DRRN NIAMEY/DIORI HAMANI   13.29    2.10   223    -19 LAND
99704   417 61291 GABS BAMAKO                12.32   -7.57   380    -26 LAND
99701   417 61415 GQPP NOUADHIBOU            20.56  -17.02     5     13 KUES
99702   417 61442 GQNN NOUAKCHOTT            18.06  -15.57     2      4 KUES
99703   417 61641 GOOY DAKAR                 14.44  -17.30    27    -18 LAND
99704   417 61701 GBYD BANJUL/YUNDUM         13.21  -16.48    36    -15 KUES
99701   198 61766 GGOV BISSAU                11.53  -15.39    39    -22 KUES
99702   412 61832 GUCY CONAKRY/GBESSIA        9.34  -13.37    26     74 KUES
99703   290 61901 ---- ST. HELENA           -15.56   -5.04   435   -435 KUES
99704   440 61902 FHAW ASCENSION             -7.58  -14.24    86    -57 KUES
99701   484 61980 FMEE SAINT-DENIS          -20.53   55.31    21      8 KUES
99702   410 61988 FIMR RODRIGUES            -19.41   63.25    58    -12 KUES
99703   422 61990 FIMP PLAISANCE            -20.26   57.40    55     40 KUES
99704   321 62259 ---- TAZERBO               25.48   21.08   260      8 LAND
99702   412 62405 HELX LUXOR                 25.40   32.42    93     -6 LAND
99703   412 62414 HESN ASSUAN                23.58   32.47   192    -12 LAND
99704   412 62423 ---- FARAFRA               27.04   27.59    82    -19 LAND
99701   412 62463 HEGN HURGHADA              27.09   33.43    16     11 KUES
99702   413 62641 HSPN PORT SUDAN            19.35   37.13     3     82 KUES
99703   413 62721 HSSS KHARTOUM              15.36   32.33   382      1 LAND
99704   410 62730 HSKA KASSALA               15.28   36.24   500     38 LAND
99701   305 63125 HDAM DJIBOUTI              11.33   43.09    13     24 KUES
99702   368 63450 HAAB ADDIS ABABA            8.59   38.48  2324     22 LAND
99703   368 63471 HADR DIREDAWA               9.36   41.51  1260     66 LAND
99704   178 63658 HUSO SOROTI                 1.43   33.37  1123    -44 LAND
99701   404 63705 HUEN ENTEBBE                0.03   32.27  1155    -15 LAND
99702   417 63733 HIMU MUSOMA                -1.30   33.48  1147     46 LAND
99703   404 63740 HKJK NAIROBI               -1.19   36.55  1624    -22 LAND
99704   417 63791 HTKJ KILIMANJARO AIRPORT   -3.25   37.04   891     13 LAND
99701   412 63820 HKMO MOMBASA               -4.02   39.37    57     38 KUES
99702   425 63870 HTZA ZANZIBAR/KISAUNI      -6.13   39.13    15     43 KUES
99703   425 63894 HTDA DAR ES SALAAM AIRP.   -6.52   39.12    55      6 KUES
99704   421 63980 FSIA SEYCHELLES INT.       -4.40   55.31     3     14 KUES
99701   412 64210 FZAA KINSHASA/NDJILI       -4.23   15.26   309    -37 LAND
99702    40 64220 ---- KINSHASA              -4.22   15.15   445      5 LAND
99703   297 64387 HRYR KIGALI                -1.58   30.07  1491    -15 LAND
99704   208 64390 HBBA BUJUMBURA             -3.19   29.19   782     45 LAND
99701   417 64400 FCPP POINTE-NOIRE          -4.49   11.54    17    -12 KUES
99702   417 64450 FCBB BRAZZAVILLE           -4.15   15.15   319      2 LAND
99703   417 64500 FOOL LIBREVILLE             0.27    9.25    12     90 KUES
99704   304 64650 FEFF BANGUI                 4.24   18.31   365    -22 LAND
99701   417 64700 FTTJ NDJAMENA              12.08   15.02   295     -8 LAND
99702   178 64756 FTTC ABECHE                13.51   20.51   549    -10 LAND
99703   417 64910 FKKD DOUALA                 4.00    9.44    10     -9 KUES
99704   378 65046 DNKN KANO                  12.03    8.32   476    -24 LAND
99701   410 65125 DNAA ABUJA                  9.15    7.00   344     36 LAND
99702   440 65201 DNMM LAGOS/IKEJA            6.35    3.20    40     -1 KUES
99703   417 65344 DBBB COTONOU                6.21    2.23     5     52 KUES
99704   259 65387 DXXX LOME                   6.10    1.15    20     30 KUES
99701   410 65401 DGLN NAVRONGO              10.54   -1.06   203     -4 KUES
99702   412 65472 DGAA ACCRA                  5.36   -0.10    68     -3 KUES
99703   417 65503 DFFD OUAGADOUGOU           12.21   -1.31   316    -11 LAND
99704   412 65545 DIBU BONDOUKOU              8.03   -2.47   369     10 LAND
99701   412 65557 ---- GAGNOA                 6.08   -5.57   205      1 LAND
99702   386 65562 DIDK DIMBOKRO               6.39   -4.42    92    -16 LAND
99703   412 65578 DIAP ABIDJAN                5.15   -3.56     7     72 KUES
99704   227 66160 FNLU LUANDA                -8.51   13.14    74     -1 KUES
99701   418 67002 ---- HAHAYA AIRPORT       -11.32   43.16    29    368 KUES
99702   418 67009 ---- DIEGO-SUAREZ         -12.21   49.18   114     14 KUES
99703   418 67027 FMNM MAJUNGA              -15.40   46.21    26      4 KUES
99704   410 67083 FMMI ANTANANARIVO         -18.48   47.29  1279     13 LAND
99701   371 67137 FMSF FIANARANTSOA         -21.27   47.06  1115     75 LAND
99702   418 67237 FQNP NAMPULA              -15.06   39.17   438    -61 LAND
99703   410 67295 FQCH CHIMOIO              -19.07   33.28   731    -77 LAND
99704   292 67315 FQVL VILANCULOS           -22.06   35.19    20      6 KUES
99701   418 67323 FQIN INHAMBANE            -23.52   35.23    14    -13 KUES
99702   413 67341 FQMA MAPUT0/MAVALANE      -25.55   32.34    39    -22 KUES
99703   155 67586 ---- LILONGWE             -13.47   33.46  1229    -17 LAND
99704   152 67693 FWCL CHILEKA              -15.41   34.58   766      5 LAND
99701   325 67761 ---- KARIBA               -16.31   28.53   518     36 LAND
99702   368 67775 ---- HARARE-KUTSAGA       -17.55   31.08  1479      4 LAND
99703   250 67843 FVFA VICTORIA FALLS       -18.06   25.51  1061      3 LAND
99704   309 67853 ---- HWANGE NATIONAL PARK -18.38   27.00  1079     -5 LAND
99701   333 67975 ---- MASVINGO             -20.04   30.52  1094    -27 LAND
99702   119 68010 ---- OKAUKUEJO            -19.11   15.55  1102    -13 LAND
99703   266 68029 ---- KASANE               -17.49   25.09   968    -81 LAND
99704   344 68032 FBMN MAUN                 -19.59   23.25   945    -17 LAND
99701   324 68110 ---- WINDHUK              -22.34   17.06  1728     49 LAND
99702   415 68112 FYWH WINDHUK STRIJDOM     -22.29   17.28  1715     15 LAND
99703   390 68174 FAPI PIETERSBURG          -23.50   29.25  1228     36 LAND
99704   119 68212 ---- HARDAP               -24.32   17.56  1108     36 LAND
99701   369 68240 FBSK GABORONE AIRPORT     -24.13   25.55  1005      4 LAND
99702   207 68296 ---- SKUKUZA              -24.59   31.36   263      4 LAND
99703   166 68300 FYLZ LUDERITZ/DIAZ POINT  -26.38   15.06    23    104 KUES
99704   316 68312 FYKT KEETMANSHOOP         -26.32   18.07  1067     22 LAND
99701   405 68368 FAOR JOHANNESBURG         -26.08   28.14  1694    -72 LAND
99702   346 68438 FAKM KIMBERLEY            -28.48   24.46  1204    -12 LAND
99703   407 68442 FABL BLOEMFONTEIN         -29.06   26.18  1354     10 LAND
99704   385 68461 FABM BETHLEHEM AIRPORT    -28.15   28.20  1686     -3 LAND
99701   111 68513 ---- KOINGNAAS            -30.12   17.17    99    -29 LAND
99702    95 68523 ---- BRANDVLEI            -30.28   20.29   922     15 LAND
99703    95 68558 ---- BARKLY EAST          -30.56   27.36  1816    -39 LAND
99704   172 68588 FADN DURBAN               -29.58   30.57     8     37 KUES
99701   116 68647 FAQT QUEENSTOWN           -31.55   26.53  1098     -9 LAND
99702   137 68727 ---- BEAUFORT WEST        -32.21   22.33   902    -53 LAND
99703   420 68816 FACT KAPSTADT             -33.59   18.36    42     29 KUES
99704   413 68842 FAPE PORT ELIZABETH       -33.59   25.36    60     46 KUES
99701   404 68858 FAEL EAST LONDON          -33.02   27.50   125     23 KUES
99702   423 68906 FAGE GOUGH ISLAND         -40.21   -9.53    54     58 KUES
99703   166 68916 ---- CAPE POINT           -34.21   18.30   208   -122 KUES
99704   158 68928 FAMO MOSSEL BAY           -34.11   22.09    59     74 KUES
99701   417 68994 FAME MARION ISLAND        -46.53   37.52    22    -22 KUES
99702   219 70200 PAOM NOME                  64.30 -165.26     6     20 KUES
99703   225 70219 PABE BETHEL AK             60.47 -161.48    40    -35 LAND
99704   211 70261 PAFA FAIRBANKS/INT.        64.49 -147.52   132      0 LAND
99701   221 70273 PANC ANCHORAGE INT.        61.10 -150.01    37     51 LAND
99702   221 70361 PAYA YAKUTAT               59.31 -139.40    11      6 KUES
99703   219 70381 PAJN JUNEAU                58.22 -134.35     5    135 LAND
99704   179 71060 CWOA CAMSELL RIVER N.W.T.  65.37 -118.07   230     11 LAND
99701   283 71066 ---- HIGH LEVEL,ALTA.      58.37 -117.10   338      8 LAND
99702   267 71078 CYYL LYNN LAKE MAN.        56.52 -101.05   357    -30 LAND
99703   281 71090 CYCY CLYDE N.W.T.          70.29  -68.31    25     38 KUES
99704   195 71122 ---- BANFF,ALTA.           51.11 -115.33  1397    232 LAND
99701   394 71123 CYEG EDMONTON INT.         53.18 -113.35   715     21 LAND
99702   286 71260 CYAM SAULT STE.MARIE ONT.  46.29  -84.30   187     14 LAND
99703   430 71395 CYHZ HALIFAX INT.          44.53  -63.31   145      6 KUES
99704   190 71474 ---- CLINTON,B.C.          51.08 -121.30  1057    -11 LAND
99701   195 71515 CYHD DRYDEN                49.50  -92.45   413    -23 LAND
99702   386 71621 CYTR TRENTON               44.07  -77.32    85     11 LAND
99703   169 71622 CYFD BRANTFORD             43.02  -81.09   278     -3 LAND
99704   386 71624 CYYZ TORONTO               43.40  -79.38   173    -41 LAND
99701   386 71627 CYUL MONTREAL DORVAL       45.28  -73.45    31     -1 LAND
99702   394 71628 CYOW OTTAWA                45.19  -75.40   116    -24 KUES
99703   279 71700 CYFC FREDERICTON           45.52  -66.32    17     15 LAND
99704   387 71707 CYQY SYDNEY,N.S.           46.10  -60.03    56    -32 LAND
99701   195 71714 CYQB QUEBEC,QUE.           46.48  -71.23    70      4 LAND
99702   390 71727 CYBG BAGOTVILLE            48.20  -71.00   159    -48 LAND
99703   280 71731 CYYB NORTH BAY             46.21  -79.26   358     -5 LAND
99704   395 71801 CYYT ST.JOHNS NEUFUNDL.    47.37  -52.44   134    -12 KUES
99701   395 71803 CYQX GANDER                48.57  -54.34   151    -15 LAND
99702   389 71809 CYDF DEER LAKE NF.         49.13  -57.24    17     58 LAND
99703   386 71815 CYJT STEPHENVILLE NFLD.    48.32  -58.33     8      7 KUES
99704   394 71816 CYYR GOOSE BAY NF.         53.19  -60.25    46    -19 LAND
99701   391 71827 CYGL LA GRANDE RIVIERE     53.38  -77.42   195    -45 LAND
99702   167 71828 CYKL SCHEFFERVILLE QUE.    54.48  -66.49   522     75 LAND
99703   195 71849 CYVZ DEER LAKE             49.55  -97.14   239     -1 LAND
99704   386 71869 CYPA PRINCE ALBERT SASK.   53.13 -105.40   428     17 LAND
99701   392 71877 CYYC CALGARY               51.07 -114.01  1077     -1 LAND
99702   145 71888 ---- JASPER,ALTA.          52.53 -118.04  1061    374 LAND
99703   382 71892 CYVR VANCOUVER             49.11 -123.10     3      9 KUES
99704   390 71893 CYQQ COMOX B.C.            49.43 -124.54    24     85 LAND
99701   390 71917 CWEU EUREKA UA N.W.T.      79.59  -85.56    10     81 KUES
99702   391 71924 CYRB RESOLUTE              74.43  -94.59    40      2 LAND
99703   394 71925 CYCB CAMBRIDGE BAY N.W.T.  69.06 -105.08    25     -8 KUES
99704   387 71926 CYBK BAKER LAKE N.W.T.     64.18  -96.05    18    -12 LAND
99701   180 71932 ---- UXBRIDGE WEST ON      44.06  -79.10   325    -55 LAND
99702   394 71934 CYSM FORT SMITH            60.01 -111.57   203      9 LAND
99703   195 71966 ---- DAWSON,Y.T.           64.03 -139.08   370    222 LAND
99704   246 72201 KEYW KEY WEST              24.33  -81.45     2     -2 MEER
99701   286 72202 KMIA MIAMI                 25.49  -80.17     3      0 KUES
99702   184 72203 KPBI WEST PALM BEACH       26.41  -80.07     6     -2 KUES
99703   180 72205 KMCO ORLANDO /JETPORT      28.26  -81.19    29      0 LAND
99704   288 72206 KJAX JACKSONVILLE          30.30  -81.42     9      0 LAND
99701   295 72208 KCHS CHARLESTON            32.54  -80.02    14     -7 KUES
99702   279 72211 KTPA TAMPA                 27.58  -82.32     8     -5 LAND
99703   180 72214 KTLH TALLAHASSEE           30.23  -84.22    25      0 LAND
99704   183 72218 KAGS AUGUSTA BUSH FLD.     33.22  -81.58    44     27 LAND
99701   206 72219 KATL ATLANTA GA.           33.39  -84.25   312    -22 LAND
99702   178 72223 KMOB MOBILE/BATES F. AL.   30.41  -88.15    66    -22 KUES
99703   285 72226 KMXF MONTGOMERY            32.18  -86.24    67    -10 LAND
99704   177 72231 KMSY NEW ORLEANS           29.59  -90.15     1      1 KUES
99701   173 72243 KIAH HOUSTON TX.           29.58  -95.21    30     -2 LAND
99702   162 72250 KBRO BROWNSVILLE/TX.       25.55  -97.25     7      0 LAND
99703   295 72253 KSAT SAN ANTONIO INT.      29.32  -98.28   247     23 LAND
99704   120 72254 KAUS AUSTIN                30.18  -97.42   193     40 LAND
99701   277 72259 KDFW DALLAS                32.54  -97.02   182    -27 LAND
99702   119 72261 KDLF DEL RIO               29.22 -100.55   310     -8 LAND
99703   158 72266 KABI ABILENE/MUN. 18.      32.25  -99.41   542     12 LAND
99704   159 72267 KLBB LUBBOCK 18.           33.39 -101.49   996      0 LAND
99701   255 72270 KELP EL PASO INT.          31.48 -106.24  1206     26 LAND
99702   147 72274 KTUS TUCSON INT.           32.07 -110.56   802     11 LAND
99703   139 72278 KPHX PHOENIX AZ.           33.26 -112.01   344    -21 LAND
99704   157 72290 KSAN SAN DIEGO/LINGBERG    32.44 -117.10     5     45 KUES
99701   156 72295 KLAX LOS ANGELES           33.56 -118.24    38      8 KUES
99702   204 72306 KRDU RALEIGH/DURHAM NC.    35.52  -78.47   132    -12 LAND
99703   302 72308 KORF NORFOLK/INT.,VA.      36.54  -76.12     8     -5 KUES
99704   305 72314 KCLT CHARLOTTE/DOUG. NC    35.13  -80.56   228    -18 LAND
99701   202 72315 ---- ASHEVILLE/MUN.,NC.    35.26  -82.32   659     21 LAND
99702   305 72327 KBNA NASHVILLE INT.        36.07  -86.41   180    -27 LAND
99703   301 72334 KMEM MEMPHIS               35.03  -90.00   101     -4 LAND
99704   148 72351 KSPS WICHITA FALLS 18.     33.58  -98.29   309    -12 LAND
99701   277 72353 KOKC OKLAHOMA CITY         35.23  -97.36   395    -17 LAND
99702   257 72365 KABQ ALBUQUERQUE INT.      35.03 -106.37  1631    -13 LAND
99703   114 72370 ---- KINGMAN/MOHAVE,AZ.    35.16 -113.56  1050     -5 LAND
99704   114 72374 ---- WINSLOW               35.02 -110.43  1505     -5 LAND
99701   249 72376 ---- FLAGSTAFF AZ.         35.14 -111.49  2192     36 LAND
99702   139 72386 KLAS LAS VEGAS/MCCARRAN    36.05 -115.10   662      7 LAND
99703   158 72389 KFAT FRESNO/AIR TERM.      36.46 -119.43   100      3 LAND
99704   206 72403 KIAD WASHINGTON/DULLES     38.57  -77.27    95      3 LAND
99701   311 72405 KDCA WASHINGTON            38.51  -77.02     5     30 LAND
99702   207 72406 KBWI BALTIMORE             39.11  -76.40    48    -26 KUES
99703   185 72407 KACY ATLANTIC CITY INT.    39.27  -74.34    21    -13 KUES
99704   206 72408 KPHL PHILADELPHIA INT.     39.53  -75.15     4     36 LAND
99701   205 72411 KROA ROANOKE/MUN. VA.      37.19  -79.58   358    -24 LAND
99702   209 72421 KCVG CINCINNATI OH.        39.03  -84.40   271    -24 LAND
99703   313 72423 KSDF LOUISVILLE/STAND.KY.  38.11  -85.44   151     -6 LAND
99704   209 72434 KSTL ST. LOUIS             38.45  -90.22   174     -3 LAND
99701   318 72438 KIND INDIANAPOLIS IN/W.C.  39.44  -86.16   246      1 LAND
99702   299 72446 KMCI KANSAS CITY           39.17  -94.45   316    -42 LAND
99703   201 72451 KDDC DODGE CITY/MUN.KS.    37.46  -99.58   791    -24 LAND
99704   154 72476 ---- GRAND JUNCTION,CO.    39.07 -108.31  1481     -6 LAND
99701   162 72488 KRNO RENO                  39.30 -119.47  1344    133 LAND
99702   156 72492 KSCK STOCKTON METRO. CA.   37.54 -121.15     8     -8 LAND
99703   167 72494 KSFO SAN FRANCISCO         37.37 -122.23     6     12 KUES
99704   206 72502 KEWR NEWARK                40.42  -74.10     5     21 LAND
99701   312 72503 KLGA NEW YORK              40.46  -73.54     7      6 KUES
99702   318 72509 KBOS BOSTON MA.            42.22  -71.02     6     16 LAND
99703   338 72519 KSYR SYRACUSE/HANCOCK NY.  43.07  -76.07   124      0 LAND
99704   338 72520 KPIT PITTSBURGH INT.       40.30  -80.13   367    -48 LAND
99701   333 72524 KCLE CLEVELAND             41.25  -81.52   241     -9 LAND
99702   338 72528 KBUF BUFFALO INT.,NY.      42.56  -78.44   220    -19 LAND
99703   210 72530 KORD CHICAGO               41.59  -87.54   203     -4 LAND
99704   325 72537 KDTW DETROIT               42.14  -83.20   195      7 LAND
99701   199 72546 KDSM DES MOINES/MUN. IA.   41.32  -93.39   294    -16 LAND
99702   173 72547 KDBQ DUBUQUE/MUN. IA.      42.24  -90.42   328    -54 LAND
99703   170 72564 KCYS CHEYENNE WY.          41.09 -104.49  1876     -5 LAND
99704   283 72565 KDEN DENVER INT.           39.52 -104.40  1656    -36 LAND
99701   195 72570 ---- CRAIG-MOFFAT,CO.      40.30 -107.31  1915     39 LAND
99702   295 72572 KSLC SALT LAKE CITY        40.47 -111.58  1288     11 LAND
99703   151 72594 KEKA EUREKA CA.            40.48 -124.10    13      8 KUES
99704   314 72606 KPWM PORTLAND INT.         43.39  -70.19    23     12 KUES
99701   330 72617 KBTV BURLINGTON/INT. VT.   44.28  -73.09   104     14 LAND
99702   207 72640 KMKE MILWAUKEE             42.57  -87.54   220     -3 LAND
99703   200 72658 KMSP MINNEAPOLIS           44.53  -93.13   256      3 LAND
99704   271 72662 KRAP RAPID CITY            44.03 -103.04   970      5 LAND
99701   168 72681 KBOI BOISE/MUN. ID.        43.34 -116.13   871    -30 LAND
99702   206 72698 KPDX PORTLAND/INT. OR.     45.36 -122.36    12     15 LAND
99703   105 72734 KCIU SAULT STE.MARIE MI.   46.28  -84.22   218     -7 LAND
99704   218 72745 KDLH DULUTH INT.           46.50  -92.11   436    -36 LAND
99701   298 72753 KFAR FARGO/HECTOR F. ND.   46.54  -96.48   274      4 LAND
99702   189 72764 KBIS BISMARCK/MUN. ND.     46.46 -100.45   511     12 LAND
99703   158 72781 KYKM YAKIMA WA.            46.34 -120.32   332      7 LAND
99704   320 72785 KGEG SPOKANE/INT. WA.      47.38 -117.32   721    -23 LAND
99701   206 72793 KSEA SEATTLE               47.27 -122.18   130    -15 LAND
99702   293 74486 KJFK NEW YORK JOHN F.K.    40.39  -73.47     4     -1 KUES
99703   401 76225 MMCU CHIHUAHUA             28.38 -106.05  1435    -20 LAND
99704   395 76405 MMLP LA PAZ (MEX.)         24.16 -110.25    18     11 KUES
99701   336 76548 MMTM TAMPICO               22.13  -97.51     9      0 KUES
99702   272 76612 MMGL GUADALAJARA           20.40 -103.23  1551      7 LAND
99703   442 76644 MMMD AEROP.INT. MERIDA     20.59  -89.39     9     -2 LAND
99704   301 76654 MMZO MANZANILLO,COL.       19.03 -104.19     3     52 KUES
99701   310 76680 ---- MEXICO CITY           19.24  -99.11  2309      8 LAND
99702   364 76692 ---- VERACRUZ              19.09  -96.07    16     -8 LAND
99703   418 76743 MMVA VILLAHERMOSA          17.59  -92.56    16     -2 LAND
99704   419 76805 MMAA ACAPULCO              16.50  -99.56     3     93 KUES
99701   430 78016 TXKF BERMUDA NAVAL         32.22  -64.41     6     -5 KUES
99702   430 78073 MYNN NASSAU                25.03  -77.28     3      1 KUES
99703   360 78224 MUHA HAVANNA               22.59  -82.24    75     22 KUES
99704   382 78229 MUVR VARADERO              23.08  -81.17     3      6 KUES
99701   246 78264 MUCU SANTIAGO DE CUBA      19.58  -75.51    55     16 KUES
99702   430 78388 MKJS MONT.BAY-SANGSTER     18.30  -77.55     1    124 KUES
99703   422 78397 MKJP KINGSTON              17.56  -76.47     3    110 KUES
99704   386 78458 MDPP PUERTO PLATA          19.45  -70.34     5    132 KUES
99701   275 78460 MDST SANTIAGO INT.         19.28  -70.42   183     61 LAND
99702   386 78479 MDPC PUNTA CANA            18.34  -68.22    12     23 KUES
99703   386 78485 MDSD LAS AMERICAS          18.26  -69.40    18     -4 KUES
99704   272 78486 MDSO SANTO DOMINGO         18.26  -69.53    14      3 KUES
99701   199 78526 TJSJ SAN JUAN              18.26  -66.00     3      2 KUES
99702   426 78583 MZBZ BELIZE AIRPORT        17.32  -88.18     5      2 KUES
99703   265 78641 MGGT GUATEMALA AEROPUERTO  14.35  -90.31  1489     48 LAND
99704   319 78720 MHTG TEGUCIGALPA           14.03  -87.13  1007     66 LAND
99701   408 78762 MROC JUAN SANTAMARIA       10.00  -84.13   920     30 LAND
99702   271 78767 MRLM PUERTO LIMON          10.00  -83.03     5     34 KUES
99703   367 78774 ---- LIBERIA               10.37  -85.26    80     24 LAND
99704   422 78866 TNCM ST. MAARTEN           18.03  -63.07     4     -4 KUES
99701   280 78897 TFFR LE RAIZET,GUADELOUPE  16.16  -61.31    11     -5 KUES
99702   323 78925 TFFF LE LAMENTIN           14.36  -61.00     5     49 KUES
99703   430 78948 TLPL HEWANORRA AIRPORT     13.45  -60.57     3    110 KUES
99704   430 78958 TGPY GRENADA               12.00  -61.47     6    253 KUES
99701   422 78962 TTCP CROWN POINT           11.09  -60.50     3      9 KUES
99702   422 78970 TTPP TRINIDAD PIARCO INT.  10.36  -61.21    17     19 KUES
99703   422 78982 TNCA QUEEN BEATRIX-AIRP.   12.30  -70.01     3     29 KUES
99704   422 78988 TNCC HATO-AIRPORT          12.12  -68.58     9     22 KUES
99701   409 80022 SKCG CARTAGENA/RAFAEL NU.  10.27  -75.31     1     26 KUES
99702   409 80028 SKBQ BARRANQUILLA/ER.COR.  10.53  -74.47    14     23 KUES
99703   224 80110 SKMD MEDELLIN/OLAYA         6.13  -75.36  1490    351 LAND
99704   401 80112 SKRG RIO NEGRO/J.M.CORDO.   6.08  -75.26  2140      1 LAND
99701   396 80222 SKBO BOGOTA                 4.43  -74.09  2547    -12 LAND
99702   401 80259 SKCL CALI/ALFONSO B.        3.33  -76.23   961    -82 LAND
99703   220 81001 ---- GEORGETOWN             6.48  -58.09     1      0 KUES
99704   421 81002 SYTM TIMEHRI/GUYANA         6.30  -58.15    28    -23 LAND
99701   343 81405 SOCA CAYENNE/FR.GUYANA      4.50  -52.22     8     20 LAND
99702    67 81408 SOOG GEORGES DE L'OYAPOCK   3.53  -51.48     6     24 LAND
99703   404 82022 SBBV BOA VISTA              2.50  -60.42   140    -61 LAND
99704   404 82193 SBBE BELEM/INTL.           -1.23  -48.29    16    -12 KUES
99701   404 82332 SBEG MANAUS                -3.09  -59.59    84    -58 LAND
99702   404 82579 SBTE TERESINA/INTL.        -5.03  -42.49    86     -9 LAND
99703   404 82599 SBNT NATAL AEROPORTO       -5.55  -35.15    52    -35 KUES
99704   404 82824 SBPV PORTO VELHO           -8.46  -63.55   102    -17 LAND
99701   404 82899 SBRF RECIFE/INTL.          -8.08  -34.55    19    -17 KUES
99702   404 82993 SBMO MACEIO                -9.31  -35.47   117    -21 KUES
99703   201 83096 ---- ARACAJU              -10.55  -37.03     9     -5 KUES
99704   404 83248 SBSV SALVADOR BAHIA       -12.54  -38.20     6     12 KUES
99701   404 83362 SBCY CUIABA/INTL.         -15.39  -56.06   187    -39 LAND
99702   396 83378 SBBR BRASILIA/INTL.       -15.52  -47.56  1061     31 LAND
99703   211 83423 ---- GOIANIA              -16.41  -49.17   747     63 LAND
99704   210 83437 SBMK MONTES CLAROS        -16.43  -43.52   646     24 LAND
99701   197 83483 ---- PIRAPORA             -17.21  -44.57   505     54 LAND
99702   191 83579 SBAX ARAXA                -19.34  -46.56  1004    -13 LAND
99703   174 83698 SBCP CAMPOS               -21.45  -41.20    11     -9 LAND
99704   404 83746 SBGL GALEAO (RIO/INTL.)   -22.49  -43.15     6     45 KUES
99701   185 83766 ---- LONDRINA             -23.23  -51.11   566    -17 LAND
99702   387 83780 SBSP SAO PAULO            -23.37  -46.39   802     45 LAND
99703   404 83827 SBFI FOZ DO IGUACU AERP.  -25.31  -54.35   180     13 LAND
99704   404 83899 SBFL FLORIANOPOLIS AERP.  -27.40  -48.33     5    103 KUES
99701   404 83971 SBPA PORTO ALEGRE/INTL.   -30.00  -51.11     3      1 LAND
99702   266 84008 ---- SAN CRISTOBAL         -0.54  -89.36     6     -6 LAND
99703   223 84071 SEQU QUITO                 -0.08  -78.29  2794      5 LAND
99704   268 84203 SEGU GUAYAQUIL             -2.09  -79.53     4      4 LAND
99701   404 84377 ---- IQUITOS               -3.45  -73.15   125    -18 LAND
99702   404 84401 SPUR PIURA                 -5.11  -80.36    49     -6 LAND
99703   179 84628 SPJC LIMA                 -12.00  -77.07    12     22 KUES
99704   396 84686 SPZO CUZCO                -13.33  -71.59  3248    364 LAND
99701   244 84735 ---- JULIACA              -15.28  -70.10  3826      8 LAND
99702   407 85201 SLLP LA PAZ/ALTO          -16.31  -68.11  4058     19 LAND
99703   401 85223 SLCB COCHABAMBA           -17.25  -66.11  2548     96 LAND
99704   218 85242 SLOR ORURO                -17.58  -67.04  3072    659 LAND
99701   246 85245 SLCZ SANTA CRUZ/EL TROMP. -17.48  -63.11   418     12 LAND
99702   421 85442 SCFA ANTOFAGASTA          -23.26  -70.26   135      5 KUES
99703   372 85469 SCIP OSTERINSEL           -27.09 -109.25    51    -10 KUES
99704   416 85574 ---- PUDAHUEL             -33.23  -70.47   474    -16 LAND
99701   421 85577 SCEL SANTIAGO             -33.26  -70.41   520    -35 LAND
99702   421 85682 SCIE CONCEPCION           -36.46  -73.04    12      3 KUES
99703   421 85799 SCTE PUERT0 MONTT         -41.26  -73.06    90    -51 KUES
99704   413 85874 SCBA BALMACEDA            -45.55  -71.42   522    124 LAND
99701   421 85934 SCCI PUNTA ARENAS         -53.00  -70.51    37     21 KUES
99702   409 86218 SGAS ASUNCION             -25.16  -57.38   101    -41 LAND
99703   419 86580 SUMU MONTEVID. CARRASCO   -34.50  -56.00    33    -11 KUES
99704   398 87046 SASJ JUJUY AERO           -24.23  -65.05   921     80 LAND
99701   406 87222 SANC CATAMARCA AERO       -28.36  -65.46   454      7 LAND
99702   406 87289 SARL PASO DE LOS LIBRES   -29.41  -57.09    69    -24 LAND
99703   430 87344 SACO CORDOBA/ARGENTINIEN  -31.19  -64.13   484    -59 LAND
99704   406 87418 SAME MENDOZA AERO         -32.50  -68.47   705     52 LAND
99701   398 87506 SAMM MALARGUE AERO        -35.30  -69.35  1426    -38 LAND
99702   406 87509 SAMR SAN RAFAEL AERO      -34.35  -68.24   745      1 LAND
99703   406 87576 SAEZ BUENOS AIRES AERO    -34.49  -58.32    20    -10 KUES
99704   406 87623 SAZR SANTA ROSA           -36.34  -64.16   190    -11 LAND
99701   406 87692 SAZM MAR DEL PLATA        -37.56  -57.35    18      2 KUES
99702   406 87750 SAZB BAHIA BLANCA         -38.44  -62.10    75     -2 KUES
99703   398 87765 SAZS BARILOCHE AERO       -41.09  -71.10   845    -41 LAND
99704   406 87803 SAVE ESQUEL AERO          -42.56  -71.09   789     41 LAND
99701   406 87860 SAVC COMODORO RINADAVIA   -45.47  -67.30    58    -19 KUES
99702   406 87938 SAWH USHUAIA              -54.48  -68.19    16     79 KUES
99703   427 88889 SFAL FALKLANDS            -51.49  -58.27    74     19 KUES
99704   117 88903 ---- GRYTVIKEN            -54.17  -36.30     3     52 KUES
99701   357 89002 ---- NEUMAYER             -70.40   -8.15    50    -50 KUES
99702   308 89004 ---- SANAE-AWS            -71.40   -2.50   815     -5 KUES
99701   400 89055 SAWB MARAMBIO             -64.14  -56.43   198    -72 LAND
99702   287 89059 SCBO BERNARDO O'HIGGINS   -63.19  -57.54    10    343 KUES
99704   241 89512 ---- NOVOLAZAREVSKAJA     -70.46   11.50   119     15 LAND
99701   379 89532 ---- SYOWA                -69.01   39.35    18    311 KUES
99702   271 89564 ---- MAWSON               -67.36   62.53    10     21 KUES
99703   252 89574 ---- PROGRESS             -69.23   76.23    14     18 KUES
99704   232 89592 ---- MIRNYJ               -66.33   93.01    40     62 LAND
99701   359 89611 ---- CASEY                -66.17  110.31    40     41 LAND
99702   317 89642 AFDU DUMONT D'URVILLE     -66.40  140.01    41    198 LAND
99703   188 91165 PHLI LIHUE,KAUAI           21.59 -159.21    45     35 KUES
99704   172 91182 PHNL HONOLULU              21.21 -157.56     2     57 KUES
99701   156 91190 PHOG KAHULUI,MAUI          20.54 -156.26    18    225 KUES
99702   208 91285 PHTO HILO/GEN.,LYMAN.      19.43 -155.04     9     13 KUES
99703   280 91334 ---- TRUK,CAROLINE IS.      7.28  151.50     2     -1 KUES
99704   274 91348 PTPN PONAPE                 6.58  158.13    37     10 KUES
99701   404 91517 YGGG HONIARA               -9.25  159.58    55    -15 KUES
99702   404 91568 ---- ANEITYUM             -20.14  169.46     6     -2 KUES
99703   416 91680 NFFN NANDI (FIDSCHI)      -17.45  177.27    13     46 KUES
99704   407 91753 NLWW HIHIFO               -13.14 -176.10    23    -12 KUES
99701   274 91765 ---- PAGO PAGO/INT.AIRP.  -14.20 -170.43     3     -3 KUES
99702   416 91843 ---- RAROTONGA            -21.12 -159.49     7     44 KUES
99703   331 91925 NTMN ATUONA                -9.48 -139.02    51    -23 KUES
99704   453 91938 NTAA TAHITI               -17.33 -149.37     2     35 KUES
99701   251 92004 AYWK WEWAK W.O.            -3.35  143.40     4     25 KUES
99702   102 93110 ---- AUCKLAND AERO        -37.01  174.49     7     20 KUES
99703    96 93245 ---- TAUPO                -38.44  176.05   407     37 LAND
99704    96 93439 ---- WELLINGTON           -41.20  174.49    13    118 KUES
99701   102 93615 ---- HOKITIKA             -42.43  170.59    45    -34 KUES
99702    96 93781 ---- CHRISTCHURCH AERO    -43.29  172.32    38     -9 KUES
99703    96 93831 NZQN QUEENSTOWN/INTL.     -45.01  168.44   358    259 LAND
99704    96 93845 ---- INVERCARGILL         -46.25  168.19     2     10 KUES
99701   141 94120 YPDN DARWIN               -12.24  130.52    31    -30 KUES
99702    83 94131 ---- TINDAL               -14.31  132.23   135     87 LAND
99703   204 94203 YBRM BROOME AIRPORT       -17.57  122.13    17     17 KUES
99704    86 94238 ---- TENNANT CREEK AIRPOR -19.38  134.11   375            
99701    79 94287 YBCS CAIRNS AIRPORT       -16.53  145.45     3    223 KUES
99702   111 94294 YBTL TOWNSVILLE           -19.15  146.46     5     14 KUES
99703   234 94300 YCAR CARNARVON AIRPORT    -24.52  113.40     4      7 LAND
99704   179 94312 YPPD PORT HEDLAND         -20.22  118.38     9     -6 KUES
99701    79 94326 YBAS ALICE SPRINGS        -23.48  133.54   537     15 LAND
99702   101 94346 ---- LONGREACH AIRPORT    -23.26  144.17   192            
99703   112 94374 YBRK ROCKHAMPTON          -23.23  150.29    14     29 LAND
99704   207 94403 YGEL GERALDTON            -28.48  114.42    35      9 KUES
99701   118 94461 ---- GILES (M.O.)         -25.02  128.18   580            
99702   139 94578 YBBN BRISBANE             -27.23  153.06     4      0 LAND
99703   124 94604 ---- BUNBURY              -33.22  115.38     3      3 KUES
99704   127 94608 YPPH PERTH                -31.57  115.52    19     57 KUES
99701   193 94637 YPKG KALGOORLIE BOULDER   -30.47  121.27   367    111 LAND
99702   102 94653 ---- CEDUNA (AIRPORT M.O. -32.08  133.42    15            
99703   134 94672 YPAD ADELAIDE             -34.56  138.31     6      5 KUES
99704    68 94691 YBHI BROKEN HILL/INTL.    -32.00  141.28   292      9 LAND
99701    49 94743 ---- MOUNT BOYCE AWS.     -33.37  150.16  1080   -178 LAND
99702   146 94767 YSSY SYDNEY AIRPORT       -33.57  151.11     6     -4 KUES
99703    47 94768 ---- SYDNEY               -33.52  151.13    39    -36 KUES
99704    72 94774 ---- NEWCASTLE            -32.55  151.48    33    -32 KUES
99701   213 94802 YABA ALBANY AIRPORT       -34.56  117.48    71     37 KUES
99702    49 94828 YPOD PORTLAND             -38.19  141.28    82    -43 KUES
99703   152 94866 YMML MELBOURNE AIRPORT    -37.40  144.50   132     15 KUES
99704   119 94926 YSCB CANBERRA             -35.18  149.11   575     34 LAND
99701    42 94969 ---- LAUNCESTON           -41.25  147.07     5    131 LAND
99702   143 94975 ---- HOBART               -42.50  147.29     4     23 KUES
99703   159 94995 YLHI LORD HOWE ISLAND     -31.32  159.04     5     -4 KUES
99704   200 94998 ---- MACQUARIE ISLAND     -54.30  158.56     6     -6 KUES
99701   124 95448 YLST LEINSTER             -27.51  120.42   497     59 LAND
99702    58 95492 ---- THAGOMINDAH          -27.59  143.49   132    -26 LAND
99703   409 96001 WIAA SABANG                 5.52   95.19   126     16 KUES
99704   409 96011 WITT BANDA ACEH/BL.BINTG.   5.31   95.25    21     39 KUES
99701   409 96035 ---- MEDAN                  3.34   98.41    25      3 LAND
99702   409 96163 ---- PADANG/TABING         -0.53  100.21     3    122 KUES
99703   415 96315 ---- BRUNEI AIRPORT         4.56  114.56    22    -21 KUES
99704   404 96413 ---- KUCHING                1.29  110.20    27     18 KUES
99701   404 96471 ---- KOTA KINABALU          5.56  116.03     3     50 KUES
99702   404 96491 ---- SANDAKAN               5.54  118.04    12    -11 KUES
99703   409 96741 ---- JAKARTA               -6.07  106.52     2      4 KUES
99704   409 96749 WIII JAKARTA SOEKARNO      -6.07  106.39     8      0 KUES
99701   409 96933 WRSP SURABAYA/PERAK        -7.13  112.43     3     -2 KUES
99702    50 96995 ---- CHRISTMAS ISLAND     -10.27  105.41   279   -261 KUES
99703   281 96996 ---- COCOS ISLAND AIRP.   -12.11   96.50     3     -3 KUES
99704   409 97014 ---- MENADO/DR.SAM RATU.    1.32  124.55    80     21 KUES
99701   409 97180 ---- UJUNG PANDANG/HASAN.  -5.04  119.33    14     21 KUES
99702   409 97230 WRRR DENPASAR-NGURAHRAI    -8.45  115.10     1     10 KUES
99703   409 97240 ---- AMPENAN               -8.32  116.04     3     60 KUES
99704   409 97260 ---- SUMBAWA BESAR         -8.26  117.25     3     55 KUES
99701   344 98328 ---- BAGUIO                16.24  120.36  1500   -154 LAND
99702   313 98425 RPLL MANILA                14.35  120.59    13      7 KUES
99703   313 98429 ---- NINOY AQUINO/INTL.    14.31  121.00    14      6 KUES
99704   316 98431 ---- CALAPAN               13.25  121.11    39    -28 KUES
99701   300 98536 ---- ROMBLON               12.35  122.17    46    -10 KUES
99702   404 98618 ---- PUERTO PRINCESA        9.45  118.44    14     50 KUES
99703   304 98644 ---- TAGBILARAN             9.36  123.51     7      9 KUES
99704   404 98646 ---- MACTAN                10.19  123.59    23    197 KUES
99701   329 98753 ---- DAVAO                  7.08  125.39    17      5 KUES
99704       01059 ENNA BANAK/LAKSELV (AFB)   70.04   24.59     8     94 KUES
99701       01112 ENBN BRONNOYSUND/BRONNOY   65.27   12.13     8    129 KUES
99702       01149 ---- BASMOEN               66.20   14.06    34    140 KUES
99703       01194 ---- NARVIK                68.28   17.30    17    172 KUES
99704       01215 ---- HJELVIG (MYRBO)       62.37    7.14    35    177 KUES
99701       01223 ENKB KRISTIANSUND          63.07    7.50    44     -1 KUES
99702       01290 ENNM NAMSOS                64.28   11.35     2     72 KUES
99702       02086 ---- LAINIO                67.46   22.21   315     10 LAND
99703       02096 ---- PAJALA                67.12   23.23   165     17 LAND
99704       02120 ---- KVIKKJOKK             66.57   17.44   320    168 LAND
99701       02128 ESPD GUNNARN               64.58   17.42   278     46 LAND
99702       02196 ---- HAPARANDA             65.50   24.09     5      3 KUES
99703       02293 ESNS SKELLEFTEHAMN         64.38   21.05    46     -3 KUES
99704       02324 ESND SVEG                  62.02   14.22   360     28 LAND
99701       02810 EFET ENONTEKIO             68.22   23.36   306     21 LAND
99702       02911 EFVA VAASA                 63.03   21.46     5     11 KUES
99703       02912 ---- VAASA                 63.06   21.35     4      9 KUES
99701       04048 BIVM VESTMANNAEYJAR        63.24  -20.17   118    -83 KUES
99702       04072 ---- FAGURHOLSMYRI         63.53  -16.39    46    -33 KUES
99703       04094 ---- NUPUR                 64.42  -14.06    25    111 KUES
99704       04339 BGSC SCORESBYSUND          70.29  -21.58    65     64 KUES
99704       08513 ---- PONTA DELGADA         37.45  -25.40    35    125 KUES
99703       23074 ---- DUDINKA               69.24   86.10    19     26 LAND
99703       27615 UUDD MOSKAU/DOMODEDOVO     55.25   37.46   200    -36 LAND
99704       28225 USPP PERM                  57.57   56.12   170    -45 LAND
99701       28429 ---- OKTJABRSKI            56.31   57.12   229      6 LAND
99702       28642 USCC CELJABINSK-BLANDINO   55.18   61.32   230    -20 LAND
99703       28807 UWWW SAMARA                53.15   50.27    40     34 LAND
99704       28900 ---- SAMARA/KURUMOCH       53.30   50.09   145    -40 LAND
99701       29570 UNKL KRASNOJARSK           56.02   92.45   276      8 LAND
99702       29634 UNNT NOVOSIBIRSK           55.02   82.54   162    -57 LAND
99703       29846 UNWW NOVOKUZNETSK          53.49   86.53   308    -17 LAND
99704       30253 UIKB BODAJBO               57.51  114.14   275    198 LAND
99701       34267 ---- DANILOVKA             50.22   44.07   102     17 LAND
99702       34519 UKCC DONETSK               48.04   37.46   224    -12 LAND
99704       34731 URRR ROSTOV-NA-DONU        47.15   39.49    78      8 LAND
99701       34929 URKK KRASNODAR             45.01   39.09    29      9 LAND
99702       35138 UWOR ORSK (SOUTH APT)      51.04   58.36   285    -51 LAND
99703       37235 ---- GROZNYJ               43.21   45.41   163     40 LAND
99704       37260 ---- SUHUMI                42.52   41.08    13     32 KUES
99701       37549 UGTB TBILISI               41.41   44.57   490     27 LAND
99702       37789 UGEE YEREVAN               40.09   44.24   865     42 LAND
99703       40001 ---- KAMISHLI              37.03   41.13   455    -22 LAND
99701       40016 ---- HASSAKAH              36.30   40.45   307      5 LAND
99704       40039 ---- RAQQA                 35.56   39.01   245      1 LAND
99701       40045 ---- DEIR AZ ZAWR          35.19   40.09   215    -14 LAND
99702       40061 OSPR PALMYRA               34.33   38.18   408     12 LAND
99701       40250 ---- H-4 IRWAISHED         32.30   38.12   683     10 LAND
99702       40438 OERY RIYADH                24.42   46.44   635    -18 LAND
99703       40608 ORBM MOSUL                 36.19   43.09   223     41 LAND
99704       40616 ---- ERBIL                 36.09   44.00   414     16 LAND
99701       40623 ---- SULAIMANIYA           35.33   45.27   853     -4 LAND
99702       40650 ORBS BAGHDAD               33.14   44.14    34     -5 LAND
99703       40689 ORMM BASRAH                30.34   47.47     2      4 LAND
99704       40904 OAFZ FAIZABAD              37.07   70.31  1200    331 LAND
99701       40911 OAMS MAZAR-I-SHARIF        36.42   67.12   378     20 LAND
99702       40913 OAUZ KUNDUZ                36.40   68.55   433      1 LAND
99703       40914 ---- BAGHLAN               36.05   68.39   550     18 LAND
99704       40922 OAMN MIMANA                35.56   64.46   815     30 LAND
99701       40938 ---- HERAT                 34.13   62.13   964     -7 LAND
99702       40948 OAKB KABUL/AIRPORT         34.33   69.13  1791     12 LAND
99703       40990 ---- KANDAHAR              31.30   65.51  1010      8 LAND
99704       41020 ---- JEDDAH (PORT)         21.24   39.12    10      3 KUES
99701       41150 OBBI BAHREIN-INT.AIRP.     26.16   50.39     2      4 KUES
99702       41216 ---- ABU DHABI             24.26   54.28     5     -3 KUES
99703       41240 OOKB KHASAB                26.13   56.14     3    180 KUES
99704       41275 ---- QARN ALAM             21.22   57.03   139    -25 LAND
99701       41404 OYSN SANA'A                15.31   44.11  2206     74 LAND
99702       41431 OYHD HODEIDAH              14.45   42.59   115   -106 KUES
99703       41466 OYTZ TAIZ                  13.41   44.08  1402     -9 LAND
99704       41480 OYAA ADEN                  12.40   45.02     3     -3 KUES
99701       41494 OYSQ SOCOTRA               12.38   53.54    47      2 KUES
99702       41641 OPLA LAHORE AIRPORT        31.31   74.24   216     -7 LAND
99703       41947 ---- KHULNA                22.47   89.32     4      3 LAND
99704       42042 VISR SRINAGAR              33.59   74.47  1664    -18 LAND
99701       42181 VIDP NEU DELHI             28.34   77.07   220     17 LAND
99702       42295 ---- DARJEELING            27.03   88.16  2127   -332 LAND
99703       42475 VIAL ALLAHABAD/BAMHRAULI   25.27   81.44    97    -19 LAND
99704       42647 VAAH AHMEDABAD INTL        23.04   72.37    58      1 LAND
99701       43057 ---- BOMBAY                18.54   72.49    10     33 KUES
99702       43194 VAGO GOA-DABOLIM           15.23   73.49    42    -19 KUES
99703       43296 VOBG BANGALORE             12.57   77.38   888     -5 LAND
99704       43372 VOTV TRIVANDRUM AIRPORT     8.28   76.57     4      1 KUES
99701       47110 RKSS SEOUL AIRPORT         37.33  126.48    18      9 LAND
99702       47113 RKSI INCHEON/INTL.         37.28  126.26     7      6 KUES
99703       47153 RKPK PUSAN                 35.11  128.56     4     68 KUES
99704       47166 RKJM MOKPO                 34.45  126.23     4      3 KUES
99701       47182 RKPC CHEJU INT'L AIRPORT   33.31  126.30    36    269 KUES
99702       47545 RJSK AKITA AIRPORT         39.37  140.13    93    -45 LAND
99703       47569 RJSS SENDAI AIRPORT        38.08  140.55     1     12 KUES
99704       47588 ---- YAMAGATA              38.15  140.21   153     68 LAND
99701       47595 ---- FUKUSHIMA             37.45  140.28    69     52 LAND
99702       47598 ---- ONAHAMA               36.57  140.54     3     22 LAND
99703       47607 RJNT TOYAMA                36.42  137.12    17    -11 KUES
99704       47616 ---- FUKUI                 36.03  136.14     7      0 LAND
99701       47618 ---- MATSUMOTO             36.15  137.58   610    139 LAND
99702       47635 RJNN NAGOYA AIRPORT        35.15  136.56    14     -2 KUES
99703       47670 ---- YOKOHAMA              35.26  139.39    39      2 KUES
99704       47671 RJTT TOKYO INTERNATIONAL   35.33  139.46     6     -4 LAND
99701       47686 RJAA TOKYO AIRPORT         35.46  140.23    41    -13 LAND
99702       47687 ---- TOKIO                 35.38  139.51     5     -3 KUES
99703       47721 ---- FUJI AB               35.19  138.52   680    -32 LAND
99704       47759 ---- KYOTO                 35.01  135.44    41     63 LAND
99701       47768 ---- OKAYAMA / HONSHU      34.39  133.55    18      2 KUES
99702       47771 RJBB OSAKA AIRPORT         34.47  135.27    12     -8 KUES
99703       47789 RJOA HIROSHIMA AIRPORT     34.26  132.55   331    -60 KUES
99704       47819 ---- KUMAMOTO              32.49  130.43    39     53 LAND
99701       47836 RJFC YAKUSHIMA             30.22  130.40    37     20 KUES
99702       47855 RJFU NAGASAKI AIRPORT      32.55  129.55     2     57 KUES
99703       47930 ---- NAHA                  26.11  127.39     3      5 KUES
99704       48070 ---- MONGHSAT              20.33   99.16   572    217 LAND
99701       48600 ---- LANGKAWI               6.20   99.44     8    103 KUES
99702       48618 ---- KUALA TRENGGANU        5.23  103.06     6     28 KUES
99703       48625 ---- IPOH                   4.34  101.06    39     15 LAND
99704       48632 ---- CAMERON HIGHLANDS      4.28  101.22  1545   -195 LAND
99701       48694 WSAP PAYA LEBAR             1.21  103.54    20     -9 LAND
99702       48820 VVNB HANOI                 21.01  105.48     6     10 LAND
99703       48900 VVTS SAIGON                10.49  106.40     5     -1 LAND
99704       48966 ---- SIEMREAP              13.22  103.51    15     -3 LAND
99701       52889 ZLLL LANZHOU               36.03  103.53  1518    142 LAND
99702       54543 ---- SHANHAIGUAN           39.58  119.48    12     59 KUES
99703       54774 ---- WEIHAI                37.30  122.07    61    -26 KUES
99704       57036 ---- XI'AN                 34.18  108.56   398     12 LAND
99701       58259 ---- NANTONG               32.06  120.52     1      6 LAND
99702       58334 ---- WUHU                  31.20  118.21    16     -6 LAND
99703       58343 ---- CHANGZHOU             31.46  119.57    15     -2 LAND
99704       58367 ZSSS SHANGHAI              31.24  121.28     8      0 LAND
99701       59368 ---- XINGANG               23.06  121.22    37    306 KUES
99702       59554 RCKH GAOXIONG              22.37  120.16    33    -12 KUES
99701       61202 GATS TESSALIT              20.15    0.59   494    -26 LAND
99702       61214 GAKL KIDAL                 18.26    1.21   458     25 LAND
99703       61223 GATB TOMBOUCTOU            16.43   -3.00   263     -8 LAND
99704       61226 GAGO GAO                   16.16   -0.03   265     -6 LAND
99701       61265 GAMB MOPTI                 14.31   -4.05   276      1 LAND
99702       61856 GFLL FREETOWN               8.37  -13.12    25    -11 KUES
99703       61967 FJDG DIEGO GARCIA          -7.18   72.24     1     -1 KUES
99704       61984 ---- SAINT-PIERRE         -21.20   55.29    52     -7 KUES
99702       62460 HESH SHARM EL SHEIKH       27.58   34.23    49     12 KUES
99703       62760 HSFS EL FASHER             13.37   25.20   730     27 LAND
99704       62771 ---- EL OBEID              13.10   30.14   574     34 LAND
99701       62790 HSNL NYALA                 12.03   24.53   655     31 LAND
99702       62810 ---- KADUGLI               11.00   29.43   499     18 LAND
99703       62840 HSSM MALAKAL                9.33   31.39   387    -22 LAND
99704       62941 HSSJ JUBA                   4.52   31.36   460     -5 LAND
99701       63021 HHAS ASMARA                15.17   38.55  2325    -12 KUES
99702       63023 HHMS MASSAWA               15.37   39.27    10     -1 KUES
99703       63170 HCMH HARGEISA               9.30   44.05  1326      5 LAND
99704       63175 HCMV BURAO                  9.31   45.34  1032      7 LAND
99701       63270 HCMK KISIMAYU              -0.22   42.26    10      6 KUES
99702       63451 HAHM HARAR MEDA             8.44   38.57  1900     35 LAND
99703       63710 HKKR KERICHO               -0.22   35.21  2184     33 LAND
99704       63789 HTAR ARUSHA                -3.24   36.37  1387      4 LAND
99701       64005 FZEA MBANDAKA               0.03   18.16   345    -19 LAND
99702       64008 FZEN BASANKUSU              1.13   19.48   360     11 LAND
99703       64810 ---- MALABO / BIOKO ISL.    3.45    8.46    50     20 LAND
99704       64950 FKYS YAOUNDE/NSIMALEN       3.50   11.31   751     11 LAND
99701       65082 DNMA MAIDUGURI             11.51   13.05   354    -39 LAND
99702       65510 DFOO BOBO DIOULASSO        11.10   -4.20   461    -10 LAND
99703       65528 DIOD ODIENNE                9.30   -7.34   434     34 LAND
99704       65548 DIMN MAN                    7.23   -7.31   339    -13 LAND
99701       65660 GLRB MONROVIA/ROBERTS       6.15  -10.21     8     93 KUES
99702       67113 FMMH MAHANORO             -19.50   48.48     5     45 KUES
99703       67561 FLND NDOLA                -13.00   28.39  1269     23 LAND
99704       67665 FLLS LUSAKA               -15.19   28.27  1152     16 LAND
99701       67743 FLLI LIVINGSTONE          -17.49   25.49   985    -33 LAND
99702       67964 ---- BULAWAYO             -20.09   28.37  1343      8 LAND
99703       68104 FYRK WALVIS BAY           -22.53   14.26     7     32 KUES
99704       68190 ---- PHALABORWA           -23.56   31.09   427    -29 LAND
99701       68239 ---- POMFRET              -25.50   23.32  1182    -19 LAND
99702       68262 ---- PRETORIA EENDRACHT   -25.45   28.11  1308     20 LAND
99703       68476 ---- LADYSMITH            -28.34   29.46  1100    -37 LAND
99704       68992 ---- BOUVET ISLAND        -54.24    3.18    28     -5 KUES
99702       70026 PABR BARROW/W.POST W.ROG.  71.18 -156.47    13     -4 KUES
99703       70272 PAED ANCHORAGE ELMENDORF   61.15 -149.48    65      4 KUES
99704       70308 PASN ST.PAUL               57.09 -170.13    10      0 LAND
99701       71601 CYAW HALIFAX               44.38  -63.30    51     13 KUES
99702       71620 CYGK KINGSTON              44.13  -76.36    93      3 KUES
99703       71716 CZBF BATHURST              46.54  -71.30   168      1 LAND
99704       71749 CYQT THUNDER BAY ONT.      48.22  -89.19   199     50 LAND
99701       71811 CYZV SEPT-ILES QUE.        50.13  -66.16    55    -36 KUES
99702       71852 CYWG WINNIPEG INT.AIRPORT  49.54  -97.14   239     -1 LAND
99703       71863 CYQR REGINA SASK.          50.26 -104.40   577     -5 LAND
99704       71909 CYFB IQALUIT               63.45  -68.33    34     -9 LAND
99701       71911 CYUS SHEPHERD BAY          68.49  -93.26    51    -17 KUES
99702       71913 CYYQ CHURCHILL             58.44  -94.04    28    -27 KUES
99703       71957 CYEV INUVIK                68.18 -133.29    59     37 LAND
99704       72216 ---- ALBANY                31.32  -84.11    60     -2 LAND
99701       72228 KBHM BIRMINGHAM-SHUTTLESW  33.33  -86.46   198     -8 LAND
99702       72237 KRSW FORT MYERS            26.32  -81.45     9     -2 KUES
99703       72242 KGLS GALVESTON             29.18  -94.48     2      0 KUES
99704       72287 KONT ONTARIO INT.          34.03 -117.36   287    -20 LAND
99701       72304 ---- CAPE HATTERAS, NC.    35.16  -75.33     2     -2 KUES
99702       72340 KLIT NORTH LITTLE ROCK     34.50  -92.15   165    -49 LAND
99703       72388 KSJC SAN JOSE INT.         37.22 -121.56    18     40 LAND
99704       72466 KCOS COLORADO SPRINGS      38.49 -104.43  1873     44 LAND
99701       72467 KASE ASPEN                 39.13 -106.52  2382    264 LAND
99702       72469 ---- DENVER                39.45 -104.52  1625    -22 LAND
99703       72482 KSMF SACRAMENTO INT.       38.42 -121.35     7      0 LAND
99704       72487 ---- CALIENTE,NV.          37.37 -114.31  1335    101 LAND
99701       72493 KOAK OAKLAND INT.          37.45 -122.13     4     14 LAND
99702       72512 KIAG NIAGARA FALLS         43.06  -78.57   180     -4 LAND
99703       72522 KMDT HARRISBURG INT.       40.12  -76.46    94     39 LAND
99704       72527 KAGC PITTSBURGH/ALLEGH.    40.21  -79.56   382    -66 LAND
99701       72554 KOFF OMAHA/OFFUTT AFB.     41.07  -95.54   315     14 LAND
99702       72568 KJAC JACKSON HOLE          43.36 -110.44  1964     21 LAND
99703       72610 KBGR BANGOR INT.           44.48  -68.50    59     -6 LAND
99704       72613 ---- MOUNT WASHINGTON NH.  44.16  -71.18  1909  -1134 BERG
99701       72670 ---- CODY/MUN.WY.          44.31 -109.01  1551     44 LAND
99702       72775 KGTF GREAT FALLS MT.       47.29 -111.22  1118      0 LAND
99703       72779 KFCA KALISPELL,MT.         48.18 -114.16   906     12 LAND
99704       74783 KFLL FORT LAUDERDALE       26.04  -80.09    35    -31 LAND
99701       76394 MMMY MONTERREY             25.52 -100.14   448     22 LAND
99702       76595 MMUN CANCUN                21.01  -86.51    10     -7 KUES
99703       76679 MMMX MEXICO INT.           19.26  -99.05  2243    -11 LAND
99704       78118 MBJT TURKS ISLAND          21.27  -71.09    10    -10 KUES
99701       78119 MBSC SOUTH CAICOS          21.31  -71.32     4     -4 KUES
99702       78258 MUHG HOLGUIN               20.48  -76.19   106      8 LAND
99703       78315 MUPR PINAR DEL RIO         22.25  -83.41    41      9 LAND
99704       78325 ---- CASA BLANCA           23.10  -82.21    50    -10 KUES
99701       78337 MUTD TRINIDAD              21.47  -79.59    54    -10 KUES
99702       78339 MUOC CIEGO DE AVILA        22.31  -78.27     2      0 LAND
99703       78344 ---- CIENFUEGOS            22.08  -80.27    42    -28 KUES
99704       78373 ---- CIUDAD HABANA         22.58  -82.23    78     19 KUES
99701       78409 MTCH CAP-HAITIEN           19.45  -72.11     2     38 KUES
99702       78439 MTPP PORT AU PRINCE        18.34  -72.18    31     23 KUES
99703       78447 MTCA LES CAYES             18.11  -73.44     1     61 KUES
99704       78470 MDSJ SAN JUAN D.L. MAGUA.  18.49  -71.18   415     33 LAND
99701       78475 MDLR LA ROMANA             18.25  -68.56     8     37 KUES
99702       78547 TISX ST. CROIX             17.42  -64.48    17     31 KUES
99703       78550 TUPJ BEEF ISLAND,TORTOLA   18.27  -64.32     4      5 KUES
99704       78555 TIST ST. THOMAS            18.20  -64.58     3     16 KUES
99701       78662 ---- SAN SALVADOR          13.43  -89.12   698     38 LAND
99702       78666 MSLP SAN SALVADOR AIRPORT  13.26  -89.03    25     22 LAND
99703       78741 MNMG MANAGUA SANDINO APT   12.09  -86.10    56      6 KUES
99704       78760 ---- PUNTARENAS             9.58  -84.50     5     68 KUES
99701       78792 MPTO PANAMA TOCUMEN APT     9.03  -79.22    45     -7 KUES
99702       78861 TAPA COOLIDGE FIELD        17.07  -61.47    10     -9 KUES
99703       78899 TFFM MARIE GALANTE         15.52  -61.16     5     -4 KUES
99704       78946 ---- CASTRIES              14.02  -61.01    55     53 KUES
99701       78954 TBPB GRANTLEY ADAMS        13.04  -59.29    50     -1 KUES
99702       78990 TNCB FLAMINGO,BONAIRE      12.09  -68.17     6     -1 KUES
99703       80407 SVMC MARACAIBO             10.43  -71.44    66      0 KUES
99704       80415 SVMI CARACAS AEROPUERTO    10.36  -66.59    43    269 KUES
99701       80416 ---- CARACAS               10.30  -66.53   835     34 LAND
99702       80421 SVMG MARGARITA INTL.       10.55  -63.58    24     99 KUES
99703       80438 ---- MERIDA/VENEZUELA       8.36  -71.11  1479    176 LAND
99704       80472 SVVA VALENCIA              10.10  -67.56   430    136 LAND
99701       82099 SBMQ MACAPA                 0.03  -51.04    17    -14 LAND
99702       82191 ---- BELEM                 -1.27  -48.28    10     -6 KUES
99703       82240 SWPI PARINTINS             -2.37  -56.44    29    -15 LAND
99704       82244 SBSN SANTAR�M              -2.25  -54.48    72    -44 LAND
99701       82280 SBSL S�O LUIZ              -2.32  -44.18    51    -46 KUES
99702       82288 SBPB PARNA�BA              -2.54  -41.44     5     16 LAND
99703       82317 SBTF TEF�                  -3.22  -64.42    47     -3 LAND
99704       82353 SBHT ALTAMIRA              -3.13  -52.13    74    -21 LAND
99701       82397 SBFZ FORTALEZA             -3.46  -38.36    26     15 KUES
99702       82400 SBFN FERNANDO DE NORONHA   -3.51  -32.25    56    -56 KUES
99703       82411 SBTT TABATINGA             -4.15  -69.56    85     -1 LAND
99704       82425 SWKO COARI                 -4.05  -63.09    46    -13 LAND
99701       82444 SBIH ITAITUBA              -4.15  -56.00    33      0 LAND
99702       82562 SBMA MARAB�                -5.22  -49.08    95    -51 LAND
99703       82564 SBIZ IMPERATRIZ            -5.32  -47.29   123     -3 LAND
99704       82567 SBCJ CARAJAS               -6.07  -50.00   621   -379 BERG
99701       82598 SBSG NATAL                 -5.46  -35.12    45    -40 KUES
99702       82610 SWEI EIRUNEP�              -6.40  -69.52   104     29 LAND
99703       82640 SBEK JACAREACANGA          -6.14  -57.47    98     36 LAND
99704       82659 SWGN ARAGUA�NA             -7.06  -48.12   229    -19 LAND
99701       82795 SBKG CAMPINA GRANDE        -7.14  -35.54   548   -124 BERG
99702       82798 SBJP JO�O PESSOA           -7.06  -34.51     7      1 KUES
99703       82900 ---- RECIFE CURADO         -8.03  -34.55     7     -5 KUES
99704       82915 SBRB RIO BRANCO            -9.58  -67.48   143     24 LAND
99701       82965 SBAT ALTA FLORESTA         -9.52  -56.06   288     -6 LAND
99702       82984 SBPL PETROLINA             -9.22  -40.34   375      1 LAND
99703       82986 SBUF PAULO AFONSO          -9.24  -38.13   253    -12 LAND
99704       83065 SBPJ PALMAS               -10.17  -48.22   236    -36 LAND
99701       83095 SBAR ARACAJ�              -10.59  -37.04     8     -6 KUES
99702       83208 SBVH VILHENA              -12.42  -60.06   612    -30 BERG
99703       83221 SDIY FEIRA DE SANTANA     -12.12  -38.58   232    -36 LAND
99704       83242 SBLE LEN��IS              -12.33  -41.23   439     83 BERG
99701       83344 SBQV VIT�RIA DA CONQUISTA -14.53  -40.48   875     31 BERG
99702       83349 SBIL ILHEUS               -14.49  -39.02     4      4 KUES
99703       83359 SBBW BARRA DO GAR�AS      -15.52  -52.23   350    -22 LAND
99704       83377 ---- BRASILIA             -15.47  -47.56  1158    -13 LAND
99701       83410 SBRD RONDON�POLIS         -16.28  -54.35   284    -39 LAND
99702       83424 SBGO GOI�NIA              -16.38  -49.13   747     52 BERG
99703       83460 SBPS PORTO SEGURO         -16.26  -39.05    51    -42 KUES
99704       83470 SWLC RIO VERDE            -17.55  -50.55   727    -42 BERG
99701       83525 SBUL UBERL�NDIA           -18.53  -48.14   945   -264 BERG
99702       83531 SNPD PATOS DE MINAS       -18.31  -46.26   940    -30 BERG
99703       83543 SBGV GOVERNADOR VALADARES -18.51  -41.56   263     35 LAND
99704       83552 SBCR CORUMB�              -19.01  -57.40   130     49 LAND
99701       83576 SBUR UBERABA              -19.46  -47.58   808    -95 BERG
99702       83583 SBBH BELO HORIZONTE       -19.51  -43.57   785     91 LAND
99703       83611 SBCG CAMPO GRANDE/INTL.   -20.27  -54.37   583    -19 LAND
99704       83618 SBTG TR�S LAGOAS          -20.47  -51.42   313    -29 LAND
99701       83635 SNDV DIVIN�POLIS          -20.10  -44.52   789     15 BERG
99702       83648 ---- VITORIA              -20.19  -40.20     8      8 KUES
99703       83649 SBVT VIT�RIA              -20.15  -40.17     3     13 KUES
99704       83652 SBRP RIBEIR�O PRETO       -21.08  -47.46   549     39 BERG
99701       83659 SBDO DOURADOS             -22.14  -54.49   452    -63 LAND
99702       83672 SBAU ARA�ATUBA            -21.12  -50.26   397      4 LAND
99703       83692 SBJF JUIZ DE FORA         -21.46  -43.22   939   -200 BERG
99704       83716 SBDN PRESIDENTE PRUDENTE  -22.07  -51.23   436    -30 LAND
99701       83719 SBCB CABO FRIO            -22.59  -42.02     7      2 KUES
99702       83721 SBKP CAMPINAS-VIRACOPOS   -23.01  -47.09   661      7 LAND
99703       83722 SBBU BAURU/AREALVA        -22.21  -49.03   615    -68 BERG
99704       83726 SDSC SAO CARLOS           -21.59  -47.53   856    -78 BERG
99701       83743 ---- RIO DE JANEIRO       -22.55  -43.10     5     35 KUES
99702       83755 SBRJ SANTOS DUMONT        -22.55  -43.10     3     37 KUES
99703       83767 SBMG MARING�              -23.25  -51.57   542   -123 BERG
99704       83768 SBLO LONDRINA             -23.20  -51.08   569    -20 BERG
99701       83773 ---- AVARE                -23.06  -48.55   793     39 LAND
99702       83779 SBGR SAO PAULO/INTL.      -23.26  -46.28   750    -23 LAND
99703       83782 ---- SANTOS               -23.56  -46.20    14     -2 KUES
99704       83809 SBSJ S�O JOS� DOS CAMPOS  -23.14  -45.52   646    -33 BERG
99701       83837 SSZW PONTA GROSSA         -25.06  -50.10   868     38 BERG
99702       83840 SBCT CURITIBA             -25.32  -49.11   911      0 BERG
99703       83842 ---- CURITIBA             -25.26  -49.16   923     -5 LAND
99704       83920 ---- SAO JOAQUIM          -28.17  -49.55  1402      0 LAND
99701       83968 SBCO PORTO ALEGRE CANOAS  -29.57  -51.09     8     18 LAND
99702       83883 SBCH CHAPECO              -27.05  -52.38   687    -40 BERG
99703       83891 SBLJ LAGES                -27.48  -50.20   937     -4 BERG
99704       83905 SBJV JOINVILLE            -26.13  -48.48     5     -2 LAND
99701       83914 SBPF PASSO FUNDO          -28.15  -52.24   684    -34 BERG
99702       83926 SBNF NAVEGANTES           -26.53  -48.39     5     41 KUES
99703       83928 SBUG URUGUAIANA           -29.47  -57.02    74    -31 LAND
99704       83937 SBSM SANTA MARIA          -29.43  -53.42    85      8 LAND
99701       83942 SBCX CAXIAS DO SUL        -29.12  -51.12   751   -233 BERG
99702       83985 SBPK PELOTAS              -31.47  -52.25    13      3 LAND
99703       85244 SLVR SANTA CRUZ- VIRU     -17.39  -63.08   373     24 LAND
99704       85445 SCLE LA ESCONDIDA         -24.17  -69.08  3136    -30 LAND
99701       85972 SCDR KAP HOORN            -56.36  -68.43    42    -42 KUES
99702       86570 SUPE PUNTA DEL ESTE       -34.55  -54.55    20     -9 KUES
99703       86622 SSKW CACOAL               -11.27  -61.26   210     -8 LAND
99704       86626 SBSI SINOP                -11.59  -55.34   371    -69 KUES
99701       86645 SBSO SORRISO              -12.33  -55.43   380    -83 LAND
99702       86652 SNBR BARREIRAS            -12.07  -45.02   470    124 BERG
99703       86676 SNVB VALEN�A              -13.21  -39.08   105    -37 LAND
99704       87480 SAAR ROSARIO              -32.55  -60.47    25    -12 LAND
99701       87585 SABE BUENOS AIRES         -34.35  -58.29    24     -2 KUES
99702       87839 ---- FARO PUNTA DELGADA   -42.46  -63.38    56    -12 KUES
99703       87903 ---- LAGO ARGENTINO AERO  -50.20  -72.18   223     40 LAND
99704       89042 ---- SIGNY ISLAND         -60.43  -45.36     6    133 KUES
99702       89542 ---- MOLODEZNAYA          -67.40   45.51    40    146 LAND
99704       91217 PGUM GUAM MARIANA IS.      13.33  144.50   110    -67 KUES
99701       91366 PKWA KWAJALEIN/BUCHOLZ      8.44  167.44     2     -2 KUES
99702       91530 ANAU NAURU INT.            -0.32  166.55     6     -5 KUES
99703       91574 ---- CHESTERFIELD         -19.58  158.31     3     -3 KUES
99704       91592 ---- NOUMEA               -22.16  166.27    69    -35 KUES
99701       91663 ---- SAVUSAVU AIRPORT     -16.48  179.20     3     51 KUES
99702       91930 NTTB BORA-BORA            -16.27 -151.45     4     -4 KUES
99703       91961 ---- PITCAIRN ISLAND      -25.04 -130.06   264   -263 KUES
99704       93119 NZAA AUCKLAND             -37.01  174.48     7     20 KUES
99701       93308 NZNP NEW PLYMOUTH         -39.01  174.11    28     26 KUES
99702       93436 NZWN WELLINGTON AIRPORT   -41.20  174.48    12    118 KUES
99703       93780 NZCH CHRISTCHURCH         -43.29  172.33    38    -10 KUES
99704       93890 ---- DUNEDIN              -45.56  170.12     1     39 KUES
99701       94035 AYPY PORT MORESBY          -9.26  147.13    42     -9 KUES
99702       94387 YBUD BUNDABERG (BINGERA)  -24.54  152.19    27    -13 KUES
99703       94463 ---- CURTIN SPRINGS       -25.19  131.45   488     11 LAND
99704       94564 ---- RAINBOW BEACH        -25.55  153.06    10      0 KUES
99701       94587 ---- TABULAM              -28.45  152.27   555    -11 LAND
99702       94669 ---- PORT PIRIE           -33.11  138.01     3     -2 KUES
99703       94791 YSCH COFFS HARBOUR        -30.19  153.07     6     46 KUES
99704       94868 ---- MELBOURNE            -37.49  144.58    31      5 KUES
99701       95367 YBMK MACKAY               -21.10  149.11     6      4 KUES
99702       96059 ---- PRAPAT-SIBISAMONT.     2.10   98.56  1200    -22 LAND
99703       96747 WIIH JAKARTA HALIM P.      -6.15  106.54    30      4 KUES
99704       96853 ---- JOGYAKARTA/ADISUC.    -7.47  110.26   107     49 LAND
99701       97290 ---- ENDEH                 -8.48  121.36     3    156 KUES
99702       97390 WPXL DILLI/AIRPORT         -8.34  125.34     6     98 KUES
99703       98748 ---- CAGAYAN DE ORO         8.29  124.38     5    114 KUES
99704       99953 ---- LONGBOAT KEY          27.23  -82.38     8     -1 KUES
99703       F9402 SBCA CASCAVEL             -25.00  -53.30   754    -61 LAND
99704       F9403 SBCD CACADOR              -26.47  -50.56  1014     67 BERG
99701       F9404 SBCM CRICI�MA             -28.44  -49.26    28      5 LAND
99702       F9405 SBCN CALDAS NOVAS         -17.44  -48.37   685      0 BERG
99703       F9406 SBDB BONITO               -21.23  -56.46   360    -11 LAND
99704       F9407 SBGU GUARAPUAVA           -25.23  -51.13  1065    -36 BERG
99701       F9408 SBIP IPATINGA             -19.28  -42.29   239    -20 LAND
99702       F9409 SBJA JAGUARUNA            -28.41  -48.04    37    -37 KUES
99703       F9410 SBJI JI-PARAN�            -10.52  -61.51   182     16 LAND
99704       F9411 SBJU JUAZEIRO DO NORTE     -7.13  -39.16   409     -4 LAND
99701       F9412 SBML MARILIA              -22.12  -49.56   647    -93 BERG
99702       F9413 SBNM SANTO �NGELO         -28.17  -54.10   322     -4 LAND
99703       F9414 SBSR S�O JOS� D. R. PRETO -20.49  -49.24   544    -87 BERG
99704       F9415 SBTB PORTO DE TROMBETAS    -1.29  -56.24    88      1 LAND
99701       F9416 SBTC UNA                  -15.21  -39.00     6     -5 KUES
99702       F9417 SBVG VAG                  -21.35  -45.28   923    -28 BERG
99703       F9418 SNTF TEIXEIRA DE FREITAS  -17.32  -39.41   105    -28 LAND
99704       F9419 SSVV POLO TURISTICO        -2.54  -40.22     8     18 KUES
99701       F9420 SULS MALDONADO            -34.51  -55.06    29     20 KUES
99702       F9421 SBCF BELO HORIZONTE AIRP. -19.20  -43.58   828   -154 BERG
99703       F9422 SBZM JUIZ DE FORA         -21.31  -43.10   411     54 LAND
99701       N9609 ---- ABYEI                  9.36   28.26   400     -7 LAND
99701       P0001 ---- INSEL BORACAY         11.59  121.55     4    103 MEER
99702       P0002 ---- CHITWAN-PARK          27.35   84.10   150      9 LAND
99703       P0003 ---- MAURITIUS STRAND     -20.18   57.30     0     89 KUES
99701       P0005 ---- STR.V.MOZAMBIQUE     -16.00   42.00     0      0 MEER
99702       P0014 ---- PALM SPRINGS (CF.)    33.45 -116.24   125    123 LAND
99703       P0015 ---- PUERTO VALLARTA       20.30 -105.15     5    187 KUES
99702       P0046 ---- TORAJA-LAND           -2.59  119.54  1200     -1 LAND
99703       P0047 ---- BANAUE/NORD-LUZON     17.01  121.00  1800    -51 LAND
99704       P0048 ---- TONGARIO NATIONALP.  -39.15  175.30  1500    -33 LAND
99701       P0049 ---- MOUNT COOK NAT.PARK  -43.35  170.15  2000    -50 LAND
99704       P0052 ---- ARBIL                 36.12   44.01   400      9 LAND
99701       P0094 ---- RONDESLOTTET          61.56    9.52  2178   -796 LAND
99702       P0315 ---- ARGUINEGUIN           27.45  -15.39    15    174 LAND
99703       P0316 ---- OGDEN                 41.14 -111.59   902    380 LAND
99704       P0317 ---- PARK CITY             40.39 -111.30  2117     78 LAND
99701       P0318 ---- HEBER CITY            40.31 -111.25  1670    319 LAND
99702       P0319 ---- PROVO                 40.15 -111.40  1388     19 LAND
99703       P0320 ---- SUEDL. ISLAS MARIAS   21.00 -107.00     0      0 MEER
99704       P0321 ---- WESTL. LOS ANGELES    32.00 -119.00     0      0 MEER
99701       P0322 ---- WESTL. DAVENPORT      37.00 -123.00     0      0 MEER
99702       P0323 ---- WESTL. ENSENADA       48.00 -130.00     0      0 MEER
99703       P0324 ---- OBERER SEE            47.13  -86.23     0    183 MEER
99701       P0337 ---- SAN PEDRO DE MACORIS  18.30  -69.18     5     11 KUES
99702       P0338 ---- S.FRANCI. DE MACORIS  19.19  -70.15   116    -19 LAND
99703       P0339 ---- CONCEPCION D.L. VEGA  19.13  -70.31    71     43 LAND
99704       P0340 ---- GONAIVES              19.27  -72.41     6     -4 KUES
99701       P0342 ---- NATIONALPARK JARAGUA  17.37  -71.25     0     98 KUES
99702       P0343 ---- NAT.PK. MTE. CHRISTI  19.52  -71.39     0      1 KUES
99703       P0344 ---- NAT.PK. LOS HAITISES  19.05  -69.36     0     52 KUES
99704       P0345 ---- NT.P.SIERRA BAHORUCO  18.15  -71.40     0     83 KUES
99702       P0396 ---- ARE                   63.23   13.12   371     72 LAND
99704       P0398 ---- FUNAESDALEN           62.30   12.36   582    156 LAND
99702       P0400 ---- RIKSGRAENSEN          68.26   18.09   400    129 LAND
99704       P0407 ---- BEAR MOUNTAIN         35.11 -118.37  2000   -529 LAND
99701       P0408 ---- VAIL                  39.38 -106.22  2400    207 LAND
99703       P0418 ---- SULEJA                 9.02    7.27   480    -38 LAND
99703       P0479 OIIE TEHERAN/IMAM KHOMEI.  35.25   51.09  1008      3 LAND
99704       P0480 RJGG CHUBU CENTRAIR        34.51  136.48     4     14 LAND
99701       P0485 ---- LOLENGI                0.09   21.00   380     38 LAND
99702       P0486 ---- OHARA                 35.14  140.23    20     40 LAND
99701       P0517 ---- USINSK                66.00   57.33    78     14 LAND
99703       P0519 ---- JINING / SHANDONG     35.24  116.34    44    -17 LAND
99704       P0520 ---- SAO SEBASTIAO         -9.56  -36.33   228    -40 LAND
99702       P0522 ---- RAAHE                 64.41   24.29     5     38 KUES
99702       P0526 ---- KOGALYM               62.14   74.32    77      2 LAND
99704       P0528 ---- SAO LUIZ             -24.06  -53.14   360     -5 LAND
99702       P0530 ---- KOKKOLA               63.50   23.08    13     -5 KUES
99703       P0539 ---- VARKAUS               62.19   27.52    77     22 LAND
99702       P0542 ---- QUANZHOU              25.56  111.04   158     54 LAND
99702       P0558 ---- SUBIC                 14.52  120.14    20     45 KUES
99702       P0562 ZYTX SHENYANG / TAOXIAN    41.34  123.28    60    -16 LAND
99701       P0565 ZBTJ TIANJIN               39.06  117.10     5     -1 LAND
99702       P0566 UACC ASTANA                51.07   71.22   347     -9 LAND
99704       P0568 MMTO TOLUCA, MEX.          19.16  -99.41  2720     -2 LAND
99701       P0569 KSFB ORLANDO / SANFORD A.  28.46  -81.15    17     -8 LAND
99702       P0574 UKCW LUHANSK               48.25   39.23   194    -54 LAND
99703       P0575 CYMM FORT MCMURRAY ALTA.   56.39 -111.13   369    -19 LAND
99702       P0611 VGHS DHAKA ZIA INTL.       23.50   90.24     9     -5 LAND
99703       P0612 VOBL BANGALURU             13.11   77.42   889     10 LAND
99704       P0613 VOCI COCHIN                10.09   76.24     9     12 LAND
99701       P0614 VOCL CALICUT               11.08   75.57   104    -43 LAND
99702       P0615 VOHS HYDERABAD             17.15   78.25   500     48 LAND
99703       P0641 HAGM GAMBELLA               9.51   34.35   526    393 LAND
99704       W1164 ---- ISLA MARGARITA        11.00  -64.00     0      8 MEER
99701       W1261 ---- LEEW.ISLANDS-S        12.00  -61.00     0      0 MEER
99702       W1560 ---- LEEW.ISLANDS-N        15.00  -60.00     0      0 MEER
99703       W1655 ---- 16N55W                16.00  -55.00     0      0 MEER
99704       W1724 ---- KAP VERDEN            17.24  -24.29     0      0 MEER
99701       W1843 ---- 18N43W                18.00  -43.00     0      0 MEER
99702       W1862 ---- WINDW.INSELN-E        18.00  -62.00     0      0 MEER
99703       W1965 ---- WINDW.INSELN-W        19.00  -65.00     0      0 MEER
99704       W2030 ---- 20N30W                20.00  -30.00     0      0 MEER
99701       W2180 ---- TRINIDAD/KUBA         21.00  -80.00     0      0 MEER
99702       W2476 ---- BAHAMAS               24.00  -76.00     0      0 MEER
99703       W2520 ---- SWL.KANAREN           25.00  -20.00     0      0 MEER
99704       W2617 ---- SDL.TENERIFFA         26.18  -16.44     0      0 MEER
99701       W2778 ---- GRAND BAHAMA          27.00  -78.00     0      0 MEER
99702       W2814 ---- SDL.FUERTEVENTURA     27.31  -13.52     0      0 MEER
99703       W2918 ---- NDL.LA PALMA          29.00  -18.00     0      0 MEER
99701       W3015 ---- CANARIS-SUED          30.00  -15.00     0      0 MEER
99704       W3417 ---- NDL.MADEIRA           34.00  -17.00     0      0 MEER
99701       W4215 ---- GEBIET 41             41.47  -15.28     0      0 MEER
99702       W4235 ---- GEBIET 43             42.21  -35.19     0      0 MEER
99703       W4325 ---- GEBIET 42             42.58  -24.49     0      0 MEER
99704       W4346 ---- GEBIET 44             42.52  -45.49     0      0 MEER
99702       W4652 ---- GEBIET 50             45.41  -52.22     0      0 MEER
99704       W4715 ---- GEBIET 46             47.04  -14.42     0      0 MEER
99701       W4726 ---- GEBIET 47             47.00  -25.42     0      0 MEER
99703       W4835 ---- GEBIET 48             47.31  -35.22     0      0 MEER
99704       W4845 ---- GEBIET 49             48.13  -45.21     0      0 MEER
99703       W5215 ---- GEBIET 51             52.08  -15.08     0      0 MEER
99704       W5244 ---- GEBIET 54             52.25  -44.22     0      0 MEER
99702       W5325 ---- GEBIET 52             53.03  -25.10     0      0 MEER
99703       W5335 ---- GEBIET 53             52.53  -35.25     0      0 MEER
99704       W5353 ---- GEBIET 55             53.17  -52.50     0      0 MEER
99701       W5413 ---- WESTL.IRLAND          53.39  -12.37     0      0 MEER
99703       W5646 ---- GEBIET 59             56.28  -45.35     0      0 MEER
99701       W5716 ---- GEBIET 56             57.22  -15.42     0      0 MEER
99702       W5720 ---- POSITION L            57.00  -20.00     0      0 MEER
99703       W5735 ---- GEBIET 58             57.01  -35.29     0      0 MEER
99704       W5755 ---- GEBIET 60             57.11  -55.12     0      0 MEER
99703       W5812 ---- WESTL.HEBRIDEN        57.34  -12.03     0      0 MEER
99704       W5825 ---- GEBIET 57             57.56  -24.53     0      0 MEER
99701       W5843 ---- KAP FARVELL           58.05  -43.28     0      0 MEER
99703       W5922 ---- PENTL-FARV2           59.02  -21.43     0      0 MEER
99703       W6015 ---- PENTL-FARV1           60.00  -15.00     0      0 MEER
99704       W6031 ---- PENTL-FARV3           60.28  -31.13     0      0 MEER
99701       W6050 ---- SW-GROENLAND          60.16  -49.59     0      0 MEER
99703       W6138 ---- SE-GROENLAND          61.11  -38.30     0      0 MEER
99704       W6458 ---- DAVISSTR1             64.00  -58.00     0      0 MEER
99701       W6531 ---- DOHRNBANK             64.45  -30.33     0      0 MEER
99702       W7041 ---- SUEDL.NANTUCKET IS.   41.00  -70.00     0      0 MEER
99703       W7060 ---- DAVISSTR2             70.00  -60.00     0      0 MEER
99704       W9853 ---- WINNIPEG-SEE          53.00  -98.00     0    217 MEER
99701       E2834 ---- ROTES MEER            27.32   34.04     0      0 MEER
99702       E2835 ---- GOLF AKABA-S          28.25   34.35     0      0 MEER
99701       E6204 ---- SVINOY                62.20    4.23     0      0 MEER
99702       E6220 ---- BOTTENSEE             62.00   19.31     0      0 MEER
99703       E6300 ---- 63NORD00OST           63.04    0.07     0      0 MEER
99704       E6319 ---- BOTTENSEE-NW          62.48   18.48     0      0 MEER
99701       E6407 ---- FROYABANKEN           64.00    7.00     0      0 MEER
99702       E6421 ---- QUARK                 63.30   21.00     0      0 MEER
99703       E6524 ---- BOTTENWIEK            65.00   23.31     0      0 MEER
99704       E6602 ---- POSITION M            66.00    2.00     0      0 MEER
99701       E6609 ---- HALTENBANK            65.31    8.35     0      0 MEER
99702       E6914 ---- LOFOTEN               68.33   14.03     0      0 MEER
99703       E7225 ---- NORDKAP               72.09   25.17     0      0 MEER
99704       E7520 ---- BAERENINSEL           74.39   19.43     0      0 MEER
99701       E7707 ---- SPITZBERGEN           76.58    7.19     0      0 MEER
99703       S4450 ---- ATLANTIK SUED1       -44.00  -50.00     0      0 MEER
99701       S4659 ---- ATLANTIK SUED2       -46.00  -59.00     0      0 MEER
99703       40415 OEDF DAMMAM (KING FAHD IN  26.26   49.48    13      1 LAND
99704       47642 RJTY YOKOTA AIR BASE       35.45  139.21   141     25 LAND
99701       47808 RJFF FUKUOKA AIRPORT       33.35  130.27     9      6 LAND
99702       72356 KTUL TULSA (INT. AIRP.)    36.12  -95.53   207     -8 LAND
99703       72401 KRIC RICHMOND (BYRD AIRPO  37.31  -77.19    51     -8 LAND
99704       72508 KBDL HARTFORD/BRADLEY INT  41.56  -72.41    53      0 LAND
99701       72543 KRFD ROCKFORD GREATER ROC  42.12  -89.06   224     12 LAND
99702       72677 KBIL BILLINGS (LOGAN INT.  45.48 -108.33  1092    -46 LAND
99703       F9423 KAFW FORT WORTH-ALLIANCE,  32.59  -97.19   220     -3 LAND
99701       F9424 SBAE BAURU/AREALVA APT.    22.09  -49.04   594   -594 BERG
99701       P0650 GOBD DIASS-THIES AIRPORT   14.40  -17.04    88    -32 LAND
99702       82591 SBMS MOSSORO/DIX SEPT R.   -5.12  -37.22    23     42 LAND
99703       83703 SBPP PONTA PORA AEROPORTO -22.33  -55.42   660    -57 LAND
99704       83818 SBST SANTOS AEROPORTO     -23.56  -46.18     3      1 LAND
99701       83828 SBTD TOLEDO               -24.41  -53.42   562    -54 LAND
99702       83981 SBBG BAGE/GUSTAVO KRAEMER -31.23  -54.07   180      3 LAND
99703       86816 SBBT BARRETOS/CHAFEI AMS. -20.35  -48.36   578     42 LAND
99704       F9425 SBAC ARACATI               -4.34  -37.48    36    -24 LAND
99701       F9426 SBJE CRUZ/ARISTON PESSOA   -2.54  -40.21    73    -47 LAND
99702       F9427 SBME MACAE                -22.20  -41.46     3     68 LAND
99703       F9428 SBPG PONTA GROSSA         -25.11  -50.09   789    109 LAND
99704       F9429 SBPO PATO BRANCO          -26.13  -52.42   822     -4 LAND
99701       F9430 SBAQ ARARAQUARA           -21.48  -48.08   711    -67 LAND
99702       F9431 SSUM UMUARAMA             -23.48  -53.19   475    -95 LAND
99703       F9432 SSPB PATO BRANCO AIRPORT  -26.13  -52.42   822     -4 LAND
99701       72204 KMLB ORLANDO MELBOURNE I.  28.06  -80.39    11     -4 LAND
99702       87155 SARE RESISTENCIA AIRPORT  -27.27  -59.03    52     -7 LAND
99703       F9433 SBVC GLAUBER DE ANDRADE   -15.54  -40.55   894    -85 LAND
99702       23073 ---- NORILSK               69.24   88.04   126     16 LAND
99703       23205 ---- NAR?JAN-MAR           67.38   53.01   139   -125 LAND
99704       23226 ---- VORKUTA               67.30   63.58   133     35 LAND
99701       25913 ---- MAGADAN               59.33  150.47   132     74 KUES
99703       27199 ---- KIROV                 58.34   49.34   134     24 LAND
99704       27333 ---- KOSTROMA              57.44   40.47   136     -8 LAND
99702       28224 ---- PERM                  57.60   56.20   131     48 LAND
99703       28411 ---- IZHEVSK               56.50   53.27   131     16 LAND
99704       28506 ---- YELABUGA              55.46   52.03   135    -11 LAND
99701       28676 ---- PETROPAVLOVSK         54.48   69.07   139     -7 LAND
99703       34122 ---- VORONEZ               51.39   39.15   149    -40 LAND
99704       34172 ---- SARATOW               51.33   46.02   111     37 LAND
99702       34467 ---- VOLGOGRAD             48.47   44.20   133    -10 LAND
99703       34691 ---- NOVYY USHTOGAN        47.54   48.48   137   -142 LAND
99704       34949 ---- STAVROPOL             45.07   42.05   451    -79 LAND
99701       35078 ---- ATBASAR               51.49   68.22   134    163 LAND
99702       35671 ---- ZHEZKAZGAN            47.48   67.43   133    199 LAND
99703       35700 ---- GUR?YEV               47.07   51.50   147   -172 KUES
99704       35796 ---- BALKHASH              46.53   75.00   129    253 LAND
99701       36003 ---- PAVLODAR              52.18   76.56   131    -17 LAND
99702       36428 ---- ULKEN NARYN           49.12   84.31   133    339 LAND
99703       36639 ---- URZHAR                47.07   81.37   132    285 LAND
99704       36821 ---- BAKANAS               44.50   76.16   134    259 LAND
99701       36859 ---- PANFILOV              44.10   80.04   136    381 LAND
99702       36927 ---- BALYKTSCHY (RYBACHE)  42.28   76.11   137   1493 KUES
99703       36974 ---- NARYN                 41.26   76.00   129   2135 BERG
99704       36985 UCFP KARAKOLKA             41.29   77.24  3080    678 BERG
99701       37006 ---- NOVOROSSIJSK          44.43   37.51   136     -2 KUES
99702       37177 ---- GAGRY                 43.15   40.16     7     22 KUES
99703       37272 ---- TKVARCHELI            42.50   41.40   266     -2 BERG
99704       37279 ---- ZUGDIDI               42.31   41.53   134    -16 LAND
99701       37308 ---- AMBROLAURI            42.32   43.08   136    943 LAND
99702       37395 ---- KUTAISI               42.15   42.38   135     -2 LAND
99703       37416 ---- CHINVALY              42.14   43.59   871     91 LAND
99704       37437 ---- DUSHETI               42.05   44.42   128    500 LAND
99701       37514 ---- AKHALTSIKHE           41.39   43.00   139   1111 LAND
99702       37531 ---- GORI                  41.60   44.07   132    563 LAND
99703       37545 ---- TBILISI (TIFLIS)      41.45   44.46   140    377 LAND
99704       37566 ---- SAGAREDZO             41.44   45.20   806   -104 LAND
99701       37575 ---- ZAKATALY              41.34   46.40   132     81 LAND
99702       37609 ---- ASHOTSK               41.02   43.53   136   2033 BERG
99703       37621 ---- BOLNISI               41.27   44.34   134    321 LAND
99704       37651 UDSG SHIRAKI               41.25   46.15   801   -165 LAND
99701       37673 ---- KHACHMAZ              41.25   48.53   142     -4 LAND
99702       37675 ---- KUBA                  41.22   48.31   131     32 LAND
99703       37686 ---- GYUMRI                40.46   43.51   145   1366 LAND
99704       37693 ---- STEPANAVAN            41.00   44.24   140   1246 LAND
99701       37699 ---- APARAN                40.32   44.23   136   2008 BERG
99702       37704 ---- VANADZOR              40.50   44.26   148   1238 LAND
99703       37711 ---- IDZHEVAN              40.52   45.09   136    656 LAND
99704       37717 ---- SEVAN LAKE            40.34   45.00   138   1788 MEER
99701       37735 ---- GYANDJA               40.43   46.25   147     10 LAND
99702       37747 ---- YEVLAKH               40.38   47.09   133    -23 LAND
99703       37749 ---- GEOKCHAY              40.39   47.45   127     -2 LAND
99704       37756 ---- MARAZA                40.32   48.56   134    318 LAND
99701       37759 ---- SUMGAIT               40.38   48.38   134    329 LAND
99702       37785 ---- ASHTARAK              40.17   44.21   137    702 LAND
99703       37787 ---- ARMAVIR               40.08   43.54   149    708 LAND
99704       37871 ---- ARTASHAT              39.56   44.31   135    714 LAND
99701       37893 ---- AGDAM                 39.59   46.56   131     73 LAND
99702       37895 ---- STEPANAKERT           39.49   46.45   131    563 LAND
99703       37897 ---- SISIAN                39.30   46.02   134   1686 LAND
99704       37905 ---- ZHDANOVSK             39.46   47.45   149    -18 LAND
99701       37959 ---- KAFAN                 39.12   46.27   133    982 BERG
99702       37972 ---- BILASUVAR             39.28   48.33   131    -16 LAND
99703       37985 ---- LENKORAN?             38.44   48.50   142   -121 KUES
99704       38062 ---- KYZYL-ORDA            44.51   65.30   129      5 LAND
99701       38111 ---- AKTAU                 43.38   51.11   138   -153 KUES
99702       38141 ---- ZHASLYK               43.53   57.53   133    -14 LAND
99703       38178 ---- AKBAYTAL              43.09   64.20   132     70 LAND
99704       38232 ---- AK-KUDUK              42.58   54.06   129    -17 LAND
99701       38264 ---- NUKUS CITY            42.29   59.37    77     -5 LAND
99702       38328 ---- SHYMKENT (CHIMKENT)   42.19   69.42   131    310 LAND
99703       38343 ---- KULAN                 42.57   72.45   125    503 LAND
99704       38345 ---- TALAS                 42.31   72.13   133   1096 LAND
99701       38388 ---- EKEZHE                41.02   57.46   133    -75 LAND
99702       38392 ---- DASHOGUZ (TASHAUZ)    41.45   59.49   130    -52 LAND
99703       38396 ---- URGENCH               41.35   60.39   131    -47 LAND
99704       38413 ---- TAMDYBULAK            41.44   64.37   137    186 BERG
99701       38462 ---- PSKEM                 41.54   70.22   128   1612 LAND
99702       38511 ---- CHAGYL                40.47   55.20   134    -32 BERG
99703       38567 ---- NAVOI                 40.08   65.21   128    192 LAND
99704       38579 ---- DZHIZAK               40.07   67.50   134    145 LAND
99701       38583 ---- SYRDAR?YA             40.49   68.41   142     99 LAND
99702       38599 ---- KHUDJAND              40.13   69.42   152    195 LAND
99703       38611 ---- NAMANGAN              40.59   71.35   474      6 LAND
99704       38613 ---- DZHALAL-ABAD          40.55   72.57   136    602 LAND
99701       38616 ---- KARA-SUU              40.42   72.54   126    541 LAND
99702       38618 ---- FERGANA               40.23   71.45   130    287 LAND
99703       38656 ---- YERBENT               39.19   58.36   129    -35 LAND
99704       38683 ---- BUHARA (BUKHARA)      39.47   64.29   130     79 LAND
99701       38687 ---- CHARDZHOU             39.05   63.36   132     50 LAND
99702       38705 ---- PENDZHIKENT           39.30   67.36   130    703 LAND
99703       38713 ---- URA-TYUBE             39.54   68.59   132    411 LAND
99704       38750 ---- ESENGULY              37.28   53.58   159   -172 KUES
99701       38763 ---- SERDAR                38.59   56.17   159    -56 LAND
99702       38812 ---- KARSHI                38.48   65.46   127    230 LAND
99703       38851 ---- RASHT                 39.00   70.18   139   1380 LAND
99704       38856 ---- DARVAZ                38.28   70.47   129   2126 BERG
99701       38869 ---- IRHT                  38.10   72.38   132   4235 BERG
99702       38875 ---- KARAKUL?              39.01   73.33   138   3775 MEER
99704       38895 ---- MARY (BAYRAM-ALI)     37.36   62.11   133     94 LAND
99704       38911 ---- KERKI                 37.50   65.12   128    118 LAND
99701       38933 ---- KURGAN-TYUBE          37.49   68.47   139    248 LAND
99702       38947 ---- PYANDZH               37.15   69.05   134    228 LAND
99701       38974 ---- SERAKHS               36.32   61.13   135    156 LAND
99701       38987 ---- KUSHKA                35.17   62.21   130    589 BERG
99701       69777 KQTI TAJI (BAGDAD AIRPT.)  37.16   42.24   300    125 LAND

TABLE St 99999 99991 gmos 99791 gmegl gme_polar no_ecmwf
clu   CofX  id    ICAO name                 nb.    el.     elev  Hmod-H type
===== ----- ===== ---- -------------------- ------ ------- ----- ------ ----
99703    59 89014 ---- NORDENSKIOLD BASE    -73.03  -13.23   495   -129 KUES
99704   380 89022 ---- HALLEY               -75.27  -26.13    30    -30 KUES
99703   185 89504 ---- TROLL                -72.01    2.32  1277     -2 KUES
99701       89507 ---- KOHNEN               -75.00    0.00  2892     27 KUES

TABLE St 99999 polar outside_gitter
clu   CofX  id    ICAO name                 nb.    el.     elev  Hmod-H type
===== ----- ===== ---- -------------------- ------ ------- ----- ------ ----
-9950       89606 ---- VOSTOK               -78.27  106.52  3420     36 LAND
"""