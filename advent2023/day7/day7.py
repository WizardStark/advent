from functools import cmp_to_key

test = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]

input = [
    "3J4KT 513",
    "Q3K42 147",
    "29JQK 187",
    "AAKA9 821",
    "555J5 571",
    "64JQ2 388",
    "A29J2 877",
    "33399 59",
    "AJ7A8 312",
    "3AA83 474",
    "9J979 218",
    "78478 432",
    "96644 502",
    "JKK8T 647",
    "33924 127",
    "56J42 864",
    "28J66 208",
    "44494 469",
    "93939 167",
    "62224 191",
    "4T3TT 447",
    "69J99 217",
    "7ATJ7 99",
    "8325T 792",
    "T3444 545",
    "99J9A 968",
    "5J474 724",
    "Q89K2 739",
    "7KJJK 565",
    "53A33 716",
    "TQ5QA 573",
    "TQJK5 109",
    "JQ4QQ 436",
    "TQ683 219",
    "QKA6A 711",
    "2T456 365",
    "TKT7K 292",
    "Q96AJ 936",
    "TTTT8 22",
    "9999A 306",
    "6KA94 376",
    "Q4A44 928",
    "3QKKQ 29",
    "Q33Q3 185",
    "83333 318",
    "3Q4AJ 668",
    "84T8A 696",
    "9T444 108",
    "K3A83 245",
    "8TTJ6 421",
    "Q5442 482",
    "K64K6 785",
    "969K6 685",
    "KQ333 779",
    "Q8277 606",
    "A5Q9A 605",
    "7K22K 631",
    "T459Q 786",
    "7KT35 856",
    "AJ6J6 444",
    "888KK 297",
    "5AA55 723",
    "667AK 838",
    "44447 834",
    "Q2K77 238",
    "K54AT 977",
    "787QA 755",
    "K87QK 54",
    "72AAQ 278",
    "92279 356",
    "993Q7 310",
    "98488 676",
    "55584 835",
    "KKK98 9",
    "6T666 603",
    "4A27T 772",
    "2789J 954",
    "7T77T 212",
    "T49J2 102",
    "TT97T 425",
    "4666K 900",
    "QQ38Q 885",
    "TT44J 89",
    "77A66 740",
    "5867T 517",
    "2TTT2 349",
    "Q443Q 338",
    "J5995 980",
    "2A3K7 350",
    "JKK23 214",
    "J38T4 481",
    "255Q2 228",
    "98898 922",
    "7Q74Q 915",
    "54544 976",
    "99349 73",
    "TATJA 382",
    "335J3 107",
    "25222 950",
    "TJ7T8 554",
    "J999J 960",
    "AAA35 475",
    "39964 301",
    "A7Q96 288",
    "4TT48 851",
    "K7567 514",
    "5TT78 398",
    "48568 41",
    "5J885 848",
    "54582 787",
    "JQATQ 309",
    "6646T 746",
    "9A855 235",
    "3333A 79",
    "45494 560",
    "88833 100",
    "8838T 781",
    "K69T4 1",
    "8A84A 234",
    "3JQ84 587",
    "KJ446 173",
    "82A2T 472",
    "Q385K 7",
    "K44KK 97",
    "8QKJ4 570",
    "37J33 634",
    "8T559 898",
    "JA55A 984",
    "A682T 616",
    "K3782 503",
    "77737 777",
    "TTT99 506",
    "66Q9Q 653",
    "Q2277 784",
    "3T3TT 859",
    "8365J 203",
    "JJ555 855",
    "83338 296",
    "A2Q99 884",
    "Q8J84 830",
    "A3467 158",
    "J6525 329",
    "J5838 196",
    "T3J29 454",
    "45K29 72",
    "77752 797",
    "28674 60",
    "25575 197",
    "24QQA 42",
    "9T352 283",
    "354Q9 46",
    "TJK24 717",
    "9J2AQ 580",
    "AKAAA 690",
    "999TT 811",
    "77277 651",
    "2626J 96",
    "A8Q3J 253",
    "88676 595",
    "QQ7TJ 624",
    "22T9T 239",
    "47474 170",
    "44548 180",
    "72JJ2 626",
    "365Q6 667",
    "22424 20",
    "K62KK 277",
    "7373Q 644",
    "QAJ26 806",
    "5AA99 768",
    "82228 895",
    "J3KK5 822",
    "A6T2J 540",
    "KKKK4 523",
    "62TTT 155",
    "33QJQ 295",
    "98999 812",
    "22JK4 719",
    "86886 518",
    "9A4JJ 262",
    "77974 563",
    "66366 515",
    "KKTJA 192",
    "J6445 488",
    "7T9QT 468",
    "J9A9A 734",
    "QAAAQ 664",
    "69966 143",
    "83348 531",
    "J45JQ 133",
    "TQK4A 679",
    "TTQTT 557",
    "566K4 677",
    "77747 504",
    "44K44 135",
    "JTTTT 8",
    "5Q5Q5 207",
    "4T2A5 63",
    "JK2K7 901",
    "52KT4 586",
    "35496 674",
    "4466J 216",
    "J7477 162",
    "77979 25",
    "JKQ8K 714",
    "9J3KJ 524",
    "3333J 271",
    "KK792 420",
    "4646A 182",
    "75745 151",
    "JAT5A 413",
    "2223J 439",
    "57577 569",
    "T9T44 423",
    "J48Q4 769",
    "8A888 48",
    "6Q6Q5 308",
    "3J3AJ 894",
    "JJJ8J 910",
    "5T637 584",
    "TTJ7Q 845",
    "88J3J 854",
    "K2238 736",
    "QAQJQ 607",
    "J272Q 286",
    "7QKKJ 426",
    "7399J 298",
    "7JTQJ 67",
    "4KAT9 989",
    "KK88J 236",
    "T267Q 126",
    "T2T7J 50",
    "5JK85 839",
    "8552K 640",
    "K6TQT 336",
    "93KQ4 371",
    "7J777 867",
    "KTKKJ 886",
    "55568 707",
    "J76QK 860",
    "T6683 30",
    "3929K 499",
    "22727 378",
    "J667A 604",
    "2292A 429",
    "K9324 443",
    "J7555 123",
    "A3T33 14",
    "A3AA3 478",
    "K4TJ4 58",
    "25379 470",
    "JJA62 291",
    "9K8AQ 729",
    "55455 98",
    "642T9 341",
    "J95Q2 94",
    "3Q925 279",
    "97TQ6 122",
    "K6KAK 198",
    "J6TKJ 944",
    "5945Q 463",
    "KT9A3 969",
    "2588K 742",
    "AJ933 817",
    "48644 450",
    "63336 27",
    "47593 509",
    "43TT3 275",
    "8858T 92",
    "4Q486 327",
    "AJ9T7 862",
    "33525 391",
    "TK5TT 56",
    "79777 12",
    "8TQQ3 215",
    "2TQK6 305",
    "4KK37 243",
    "66776 487",
    "AAJA6 507",
    "662K6 799",
    "55999 803",
    "555AT 611",
    "9479J 497",
    "77957 302",
    "6A333 691",
    "744K4 101",
    "95999 863",
    "6QQQQ 904",
    "7K57K 818",
    "67K6K 282",
    "29T2J 810",
    "2T5KJ 548",
    "58K94 355",
    "J2TK9 244",
    "99J22 671",
    "9989K 730",
    "2K9T4 138",
    "72872 222",
    "K37TQ 912",
    "634T7 939",
    "444JT 783",
    "QQ66A 715",
    "KJ755 709",
    "K5588 876",
    "33536 567",
    "Q6J58 722",
    "544A4 501",
    "7KQ7K 720",
    "4J2J3 117",
    "Q72J7 88",
    "4K4AK 103",
    "692A4 809",
    "22223 705",
    "22Q2J 385",
    "K6KK4 623",
    "25A7Q 998",
    "777Q7 702",
    "99898 399",
    "5A857 335",
    "54K94 267",
    "5J5Q5 280",
    "88288 635",
    "29922 204",
    "KKKT8 183",
    "9J5AA 141",
    "TTT6J 249",
    "8K88J 251",
    "AAAAJ 130",
    "62262 659",
    "2A626 113",
    "22J2T 654",
    "K2788 648",
    "Q838Q 935",
    "6T8TT 428",
    "TK4KK 572",
    "AKQAA 28",
    "3K78J 320",
    "TKK33 363",
    "27JAJ 324",
    "JK3TT 965",
    "4K3TQ 422",
    "36494 551",
    "58328 166",
    "5676J 16",
    "K4279 313",
    "66656 883",
    "4634A 104",
    "48A4A 220",
    "TTT6T 979",
    "K4678 770",
    "226QQ 948",
    "99J5Q 795",
    "9KJ99 596",
    "TT5T8 807",
    "965K7 268",
    "38334 255",
    "6J66Q 511",
    "9AA63 240",
    "JA742 699",
    "J5KKJ 159",
    "53A2T 921",
    "43J55 908",
    "2A2A9 790",
    "A8899 695",
    "8J333 78",
    "AQ282 756",
    "JKQ7Q 525",
    "95539 642",
    "93TT9 2",
    "7Q87J 10",
    "44TQ6 972",
    "63333 5",
    "AA8QQ 990",
    "AJAJJ 200",
    "66446 461",
    "T8T9T 442",
    "4A7TQ 789",
    "35J74 247",
    "J3399 849",
    "373J8 128",
    "55368 281",
    "J9KTA 776",
    "52555 601",
    "77272 520",
    "24T42 311",
    "KK4KJ 157",
    "KQJ95 112",
    "8J88J 466",
    "TQ384 537",
    "J9QQT 390",
    "44228 655",
    "KK52K 917",
    "4742Q 788",
    "346T3 869",
    "33339 796",
    "4AJ6K 242",
    "93Q27 713",
    "A2222 449",
    "Q2229 638",
    "A5355 430",
    "34333 77",
    "K9K94 250",
    "A59K8 210",
    "6T4AA 248",
    "JJJ99 542",
    "KAK3K 693",
    "JA2A2 550",
    "4KA9Q 933",
    "25666 516",
    "8T4T7 193",
    "7KK26 744",
    "666Q4 873",
    "4A99A 703",
    "7TQJ8 435",
    "8482J 688",
    "JJ848 55",
    "33K33 791",
    "234T4 731",
    "AK57T 406",
    "AJQ49 87",
    "A864A 160",
    "33T3T 163",
    "9AJK6 617",
    "64645 307",
    "6Q347 1000",
    "T65K3 315",
    "5J6J5 368",
    "4545Q 66",
    "Q5888 574",
    "9QQT9 500",
    "6QAJ4 178",
    "666AK 660",
    "4827K 195",
    "7847A 246",
    "T66KT 348",
    "49A4T 270",
    "22272 753",
    "4TT68 725",
    "Q7K3A 146",
    "226Q6 759",
    "JK7K7 3",
    "QQ727 85",
    "646JQ 828",
    "5T729 946",
    "3K383 585",
    "989T9 966",
    "3J336 124",
    "563TA 878",
    "KK2AA 747",
    "J6K3T 150",
    "K999K 985",
    "A288A 408",
    "3T5J8 396",
    "J3J68 75",
    "7KT77 986",
    "336QQ 612",
    "3478K 592",
    "2K22K 962",
    "J4Q33 844",
    "876J2 637",
    "T5552 650",
    "TT2TT 353",
    "A2A25 903",
    "Q6J6Q 417",
    "AA3TA 687",
    "Q2T3Q 816",
    "9JK22 575",
    "QQQ8Q 752",
    "9J3Q5 957",
    "J6363 625",
    "77283 964",
    "9K962 538",
    "68787 871",
    "7A72A 24",
    "79KA8 90",
    "95965 344",
    "35596 139",
    "49997 258",
    "833J8 602",
    "444TT 924",
    "4646Q 549",
    "3QAJQ 342",
    "8T548 889",
    "348Q7 893",
    "55K5K 993",
    "A8A8A 264",
    "A88J8 451",
    "33AKQ 213",
    "48886 136",
    "54T45 303",
    "QJTTQ 229",
    "AAQA3 942",
    "4Q565 533",
    "Q56JK 636",
    "5QQQ5 343",
    "4AKJ8 322",
    "4AQQ5 987",
    "JTTJ5 492",
    "QQ5KQ 866",
    "2T537 34",
    "3QQQQ 448",
    "43K77 347",
    "T93JJ 762",
    "85525 657",
    "44448 370",
    "55474 325",
    "9965T 961",
    "33QQQ 940",
    "6A3Q5 369",
    "944J4 483",
    "99K92 384",
    "75557 773",
    "A4444 801",
    "T2TTK 263",
    "6A882 952",
    "QQ7QQ 751",
    "AK3K3 875",
    "5J5JJ 618",
    "K9KK6 564",
    "A3K33 345",
    "75J77 71",
    "288K2 820",
    "97JQJ 333",
    "8J357 741",
    "42Q5T 153",
    "75JA5 26",
    "9QQ9Q 465",
    "34322 874",
    "5KJK5 953",
    "666JA 257",
    "K99KK 409",
    "33T3J 23",
    "A3434 832",
    "QJQQJ 847",
    "5J22J 610",
    "3A377 256",
    "3T388 361",
    "436AA 373",
    "88889 556",
    "575A7 467",
    "K5KKJ 858",
    "5682J 74",
    "95AJ8 358",
    "8AA66 186",
    "QQQ77 608",
    "9989J 620",
    "888K8 366",
    "T4JJ9 566",
    "JK988 970",
    "58988 47",
    "J9929 452",
    "KAA7J 206",
    "TTTJJ 145",
    "7T7J7 645",
    "6T372 902",
    "276A3 121",
    "34AQK 116",
    "T9Q32 154",
    "4A4J5 224",
    "333KK 857",
    "QQJQQ 775",
    "KKK3K 633",
    "Q8Q88 476",
    "5K2AA 205",
    "K6666 184",
    "97335 18",
    "KAK4K 590",
    "42442 831",
    "T2A92 694",
    "7KKKK 598",
    "2KK2K 528",
    "24992 505",
    "24QK4 958",
    "664J3 782",
    "T55QQ 708",
    "343Q3 678",
    "T8A55 491",
    "58JQ5 780",
    "3843T 314",
    "3AQ96 735",
    "T69KT 938",
    "545K8 673",
    "28Q66 460",
    "44777 332",
    "T22Q8 622",
    "22J22 252",
    "96599 897",
    "KKQ7Q 393",
    "64Q7K 911",
    "Q3JQ8 231",
    "33373 536",
    "55QA5 559",
    "7J266 930",
    "9982A 774",
    "9TK6Q 615",
    "KK2JJ 484",
    "9Q9JQ 6",
    "AAAQA 819",
    "J5K4Q 480",
    "JK69K 843",
    "499A9 757",
    "2Q456 473",
    "4KAK7 152",
    "QQQKK 290",
    "AAAJ5 852",
    "67K23 749",
    "337J7 261",
    "T55T5 861",
    "AATT5 802",
    "T9TTT 86",
    "33387 826",
    "T57AQ 583",
    "652J2 899",
    "27788 681",
    "77JTT 555",
    "8826Q 718",
    "J7JKJ 805",
    "8J228 745",
    "23932 907",
    "3TJJ3 532",
    "7557K 364",
    "95JJ4 273",
    "6T6TA 629",
    "QQQTQ 870",
    "88228 276",
    "JT3T2 738",
    "66744 49",
    "33A3A 241",
    "77AA7 658",
    "337Q5 700",
    "88887 357",
    "8QQA7 351",
    "56622 32",
    "AJQKK 937",
    "TAJ7T 132",
    "66466 490",
    "78A8Q 689",
    "88A83 665",
    "72J5T 137",
    "2A534 149",
    "J33KT 841",
    "63223 981",
    "35552 57",
    "33JAA 853",
    "5A7A7 913",
    "J33J3 339",
    "TT93T 680",
    "JJJJJ 287",
    "T8TJQ 582",
    "7T9TJ 433",
    "944TJ 733",
    "43774 743",
    "592K9 69",
    "6J666 971",
    "JJ666 882",
    "9J668 129",
    "Q643K 967",
    "2Q2A2 415",
    "2936T 414",
    "A5A52 704",
    "3A4KJ 813",
    "8KAQ5 323",
    "38889 931",
    "TQ4QK 156",
    "AQK32 920",
    "79KK9 266",
    "J44J4 119",
    "568A8 561",
    "JA8J2 553",
    "A2386 37",
    "29374 374",
    "2Q2QJ 562",
    "5KKK5 434",
    "7QQ77 15",
    "723J7 697",
    "JTKK3 19",
    "85947 402",
    "666Q9 441",
    "9A847 669",
    "44JQA 945",
    "59Q8Q 670",
    "7QT64 652",
    "73J7T 534",
    "ATAAA 161",
    "7JJAQ 202",
    "KKKAK 232",
    "T659T 403",
    "Q9J99 649",
    "6J878 974",
    "JA5JA 367",
    "77769 880",
    "48J5J 701",
    "88787 427",
    "68K79 597",
    "A44T4 496",
    "T9JJK 823",
    "8A639 641",
    "K856Q 416",
    "26336 546",
    "22292 169",
    "2J268 165",
    "2A277 609",
    "J8288 825",
    "TQQQT 956",
    "22AAA 387",
    "52749 106",
    "AJA7A 379",
    "9Q999 527",
    "K2727 360",
    "J9A92 44",
    "2336J 134",
    "88T68 778",
    "55TTT 947",
    "7A5Q6 223",
    "QJT34 890",
    "77655 93",
    "79K5Q 269",
    "AQJQ8 362",
    "7T22T 62",
    "J554K 793",
    "A5AAT 800",
    "Q5K74 579",
    "QQJ3Q 179",
    "TKQ66 951",
    "377Q7 923",
    "3A4A3 464",
    "9J999 189",
    "93522 672",
    "5JQK7 949",
    "QQT66 914",
    "93K35 400",
    "7QQJJ 544",
    "AAT4J 471",
    "JT8TT 254",
    "528KQ 43",
    "AAJAJ 576",
    "QQ9Q7 992",
    "TTJ33 639",
    "39KJ7 814",
    "77J37 386",
    "5K555 114",
    "7TA4A 211",
    "5847J 999",
    "K527T 453",
    "TQ6Q9 168",
    "J6QJT 526",
    "TTJ88 289",
    "8A8A7 682",
    "A32T8 383",
    "769T3 692",
    "QK653 510",
    "666J3 80",
    "55Q55 340",
    "49286 896",
    "J4334 529",
    "97JA8 837",
    "25J79 991",
    "42JA5 140",
    "T3TJT 35",
    "97TKA 588",
    "QQ2QT 411",
    "86666 21",
    "5Q3JK 118",
    "3T333 621",
    "36693 761",
    "QKAAK 684",
    "778J8 354",
    "TQJ65 836",
    "2J228 172",
    "9869J 84",
    "A6QQ9 326",
    "746A6 446",
    "Q5678 494",
    "J2J83 177",
    "KKAK8 943",
    "J8TTJ 995",
    "T4333 175",
    "996Q7 916",
    "99696 51",
    "57J2J 683",
    "T269T 926",
    "89827 906",
    "QQ76Q 95",
    "4Q884 225",
    "5K43J 346",
    "99292 530",
    "Q53K3 765",
    "J8888 627",
    "39462 405",
    "JA43T 988",
    "AJ678 352",
    "676J7 996",
    "J9J89 321",
    "38AA8 199",
    "77J78 70",
    "9J944 438",
    "K2A22 767",
    "5QKJA 401",
    "J32J7 698",
    "5AA5A 458",
    "38647 237",
    "2AA32 131",
    "K9843 594",
    "JQ5A4 754",
    "6Q667 824",
    "5KA78 418",
    "62J5T 498",
    "4444J 840",
    "99QQ7 375",
    "4AAJA 221",
    "J9939 304",
    "93259 918",
    "85A55 377",
    "4JQ4Q 827",
    "66626 881",
    "34453 656",
    "AA8TT 927",
    "33555 982",
    "T3J63 293",
    "6J3T6 850",
    "7K7KK 285",
    "8QQ8Q 983",
    "79Q99 111",
    "Q5TQ8 661",
    "Q58QJ 808",
    "2224J 599",
    "67669 727",
    "83Q49 65",
    "J8834 865",
    "2Q2T6 489",
    "8TQQA 485",
    "TT9TA 558",
    "46436 479",
    "299T9 404",
    "72429 675",
    "A3695 372",
    "46468 737",
    "8K642 978",
    "ATQAQ 909",
    "QTJQQ 833",
    "9QQQQ 334",
    "4Q445 233",
    "22J26 316",
    "TATAT 395",
    "TTT44 144",
    "AK45Q 174",
    "545Q2 300",
    "5KJJ5 380",
    "63636 419",
    "K989K 227",
    "4644J 728",
    "6TJA6 115",
    "38KK8 260",
    "55J95 389",
    "Q3332 265",
    "Q5Q2J 959",
    "J7547 613",
    "A8753 666",
    "24525 359",
    "T5J5T 91",
    "AA565 272",
    "J3433 763",
    "K288T 68",
    "777T7 381",
    "TTJ22 593",
    "8TJ72 905",
    "8JA8A 171",
    "A55A3 299",
    "Q6247 82",
    "AAK2A 994",
    "A6886 600",
    "T6K8T 105",
    "66766 552",
    "KQQQQ 81",
    "JJ229 394",
    "J9AA3 40",
    "79J79 83",
    "695JK 11",
    "Q6Q6Q 522",
    "JA3QA 804",
    "27424 284",
    "65555 632",
    "99AAA 493",
    "KKKKQ 294",
    "QJ9QQ 630",
    "J2AAA 319",
    "29772 331",
    "48488 424",
    "5A7AA 794",
    "57773 190",
    "888J7 328",
    "5JJ45 226",
    "A3658 766",
    "42444 431",
    "77757 887",
    "Q8463 259",
    "99529 643",
    "KQK99 397",
    "86222 410",
    "66J86 125",
    "88666 38",
    "48838 181",
    "8QAJ5 495",
    "K555T 748",
    "KTKTK 392",
    "93693 535",
    "6AJJA 52",
    "9JT92 486",
    "KJJKK 13",
    "4AAQQ 581",
    "63553 437",
    "77878 577",
    "AJK8A 39",
    "77847 462",
    "64389 76",
    "KJ46K 892",
    "QQQQ2 925",
    "9TQQQ 412",
    "5JJ4J 710",
    "52JAQ 209",
    "22AJJ 477",
    "K3882 750",
    "65J65 459",
    "5A556 17",
    "K4445 317",
    "7J77J 829",
    "82922 36",
    "89K88 726",
    "J5666 33",
    "99T99 591",
    "46565 543",
    "63K6K 706",
    "Q8T9K 764",
    "88Q99 619",
    "QQ68Q 142",
    "KKKKJ 457",
    "QQQAA 164",
    "54T68 521",
    "T7382 440",
    "8J464 512",
    "6Q443 712",
    "4TJJQ 568",
    "4JJ4A 589",
    "4J49A 798",
    "TJA4T 879",
    "9Q99Q 188",
    "TJJ7T 578",
    "775AJ 868",
    "T82A8 963",
    "2Q55Q 407",
    "K3KJA 955",
    "666KK 120",
    "TA665 975",
    "68AKK 662",
    "95994 760",
    "34733 31",
    "KKK5K 721",
    "7KT7T 732",
    "K44J8 973",
    "Q7A9A 815",
    "JT3A3 455",
    "TJ938 888",
    "67677 541",
    "74T93 53",
    "Q6366 330",
    "78772 663",
    "KK22J 201",
    "55599 686",
    "9TAAA 64",
    "KQKKQ 547",
    "8KK87 919",
    "38J88 176",
    "57AQ9 194",
    "8793K 846",
    "377A2 614",
    "8487J 771",
    "J4JA2 45",
    "4T444 456",
    "9Q228 539",
    "68468 872",
    "8J8TK 274",
    "2K222 758",
    "9999K 337",
    "77T32 934",
    "8T88Q 891",
    "QQ5QQ 628",
    "J974T 148",
    "58575 646",
    "65JJJ 230",
    "4A92A 110",
    "3888K 445",
    "TJ5JA 61",
    "K5K65 929",
    "34433 508",
    "AA9AA 997",
    "A3323 4",
    "62AK3 519",
    "5542K 932",
    "76K27 842",
    "7T33T 941",
]


hand_types = {
    51: 6,
    42: 5,
    32: 4,
    33: 3,
    23: 2,
    24: 1,
    15: 0,
}

cards1 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

cards2 = cards1.copy()
cards2["J"] = 1


def identify1(string):
    syms = {}

    for c in string:
        syms[c] = 1 + syms.get(c, 0)

    return 10 * max(syms.values()) + len(syms.values())


def identify2(string):
    syms = {}

    for c in string:
        syms[c] = 1 + syms.get(c, 0)

    jcount = syms.pop("J", 0)
    vals = list(syms.values())
    maxval = max(vals) + jcount if vals else jcount

    return 10 * maxval + max(len(vals), 1)


def compare1(x, y):
    xtype = identify1(x[0])
    ytype = identify1(y[0])
    if not xtype == ytype:
        return hand_types[xtype] - hand_types[ytype]
    for i, c in enumerate(x[0]):
        if c != y[0][i]:
            return cards1[c] - cards1[y[0][i]]
    return 0


def compare2(x, y):
    xtype = identify2(x[0])
    ytype = identify2(y[0])
    if not xtype == ytype:
        return hand_types[xtype] - hand_types[ytype]
    for i, c in enumerate(x[0]):
        if c != y[0][i]:
            return cards2[c] - cards2[y[0][i]]
    return 0


def part1(input):
    hands = [el.split() for el in input]
    sorted_hands = sorted(hands, key=cmp_to_key(compare1))
    total = sum(int(x[1]) * (i + 1) for i, x in enumerate(sorted_hands))
    print(total)


def part2(input):
    hands = [el.split() for el in input]
    sorted_hands = sorted(hands, key=cmp_to_key(compare2))
    total = sum(int(x[1]) * (i + 1) for i, x in enumerate(sorted_hands))
    print(total)


part1(input)
part1(test)
part2(input)
part2(test)
