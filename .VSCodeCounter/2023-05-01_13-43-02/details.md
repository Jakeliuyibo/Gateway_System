# Details

Date : 2023-05-01 13:43:02

Directory y:\\研究生\\跨越网关\\代码\\Gateway_System

Total : 321 files,  1098343 codes, 41993 comments, 241997 blanks, all 1382333 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [README.md](/README.md) | Markdown | 9 | 0 | 4 | 13 |
| [control/config/device.conf](/control/config/device.conf) | Properties | 1 | 2 | 1 | 4 |
| [control/src/__init__.py](/control/src/__init__.py) | Python | 13 | 2 | 7 | 22 |
| [control/src/backup/core_scheduling backup.py](/control/src/backup/core_scheduling%20backup.py) | Python | 102 | 50 | 33 | 185 |
| [control/src/backup/forwarding_rule.conf](/control/src/backup/forwarding_rule.conf) | Properties | 3 | 0 | 0 | 3 |
| [control/src/backup/forwarding_rule.py](/control/src/backup/forwarding_rule.py) | Python | 53 | 21 | 18 | 92 |
| [control/src/config.py](/control/src/config.py) | Python | 23 | 3 | 4 | 30 |
| [control/src/core_scheduling.py](/control/src/core_scheduling.py) | Python | 169 | 49 | 44 | 262 |
| [control/src/device_manager.py](/control/src/device_manager.py) | Python | 140 | 31 | 34 | 205 |
| [control/src/driver/bsp_underwater_acoustic_comm.py](/control/src/driver/bsp_underwater_acoustic_comm.py) | Python | 161 | 33 | 30 | 224 |
| [control/src/driver/msatellite.py](/control/src/driver/msatellite.py) | Python | 85 | 18 | 15 | 118 |
| [control/src/driver/mserial.py](/control/src/driver/mserial.py) | Python | 77 | 20 | 12 | 109 |
| [control/src/task_queue.py](/control/src/task_queue.py) | Python | 78 | 30 | 20 | 128 |
| [control/src/test_for_pika.py](/control/src/test_for_pika.py) | Python | 20 | 11 | 8 | 39 |
| [control/src/tool/mformatconv.py](/control/src/tool/mformatconv.py) | Python | 6 | 1 | 3 | 10 |
| [control/src/tool/mlocaltime.py](/control/src/tool/mlocaltime.py) | Python | 9 | 4 | 8 | 21 |
| [db/gateway.db](/db/gateway.db) | Database | 101 | 0 | 2 | 103 |
| [logs/device/2023_04_30 20_24_45.log](/logs/device/2023_04_30%2020_24_45.log) | Log | 32 | 0 | 1 | 33 |
| [logs/device/2023_04_30 20_35_01.log](/logs/device/2023_04_30%2020_35_01.log) | Log | 47 | 0 | 1 | 48 |
| [logs/device/2023_04_30 21_05_56.log](/logs/device/2023_04_30%2021_05_56.log) | Log | 11 | 0 | 1 | 12 |
| [logs/device/2023_04_30 21_06_44.log](/logs/device/2023_04_30%2021_06_44.log) | Log | 90 | 0 | 1 | 91 |
| [logs/device/2023_04_30 21_10_35.log](/logs/device/2023_04_30%2021_10_35.log) | Log | 20 | 0 | 1 | 21 |
| [logs/device/2023_04_30 21_14_41.log](/logs/device/2023_04_30%2021_14_41.log) | Log | 27 | 0 | 1 | 28 |
| [logs/device/2023_04_30 21_20_02.log](/logs/device/2023_04_30%2021_20_02.log) | Log | 19 | 0 | 1 | 20 |
| [logs/device/2023_04_30 21_26_02.log](/logs/device/2023_04_30%2021_26_02.log) | Log | 19 | 0 | 1 | 20 |
| [logs/device/2023_04_30 21_27_07.log](/logs/device/2023_04_30%2021_27_07.log) | Log | 11 | 0 | 1 | 12 |
| [logs/device/2023_04_30 21_28_43.log](/logs/device/2023_04_30%2021_28_43.log) | Log | 11 | 0 | 1 | 12 |
| [logs/device/2023_04_30 21_29_30.log](/logs/device/2023_04_30%2021_29_30.log) | Log | 11 | 0 | 1 | 12 |
| [logs/device/2023_04_30 21_31_01.log](/logs/device/2023_04_30%2021_31_01.log) | Log | 11 | 0 | 1 | 12 |
| [logs/device/2023_04_30 21_32_14.log](/logs/device/2023_04_30%2021_32_14.log) | Log | 13 | 0 | 1 | 14 |
| [logs/device/2023_04_30 21_32_42.log](/logs/device/2023_04_30%2021_32_42.log) | Log | 21 | 0 | 1 | 22 |
| [logs/device/2023_04_30 21_36_31.log](/logs/device/2023_04_30%2021_36_31.log) | Log | 21 | 0 | 1 | 22 |
| [logs/device/2023_04_30 21_37_14.log](/logs/device/2023_04_30%2021_37_14.log) | Log | 20 | 0 | 1 | 21 |
| [logs/device/2023_04_30 22_16_21.log](/logs/device/2023_04_30%2022_16_21.log) | Log | 13 | 0 | 1 | 14 |
| [logs/device/2023_04_30 22_17_02.log](/logs/device/2023_04_30%2022_17_02.log) | Log | 12 | 0 | 1 | 13 |
| [logs/device/2023_04_30 22_18_32.log](/logs/device/2023_04_30%2022_18_32.log) | Log | 14 | 0 | 1 | 15 |
| [logs/device/2023_04_30 22_21_09.log](/logs/device/2023_04_30%2022_21_09.log) | Log | 28 | 0 | 1 | 29 |
| [logs/device/2023_04_30 22_51_06.log](/logs/device/2023_04_30%2022_51_06.log) | Log | 48 | 0 | 3 | 51 |
| [logs/device/2023_04_30 22_53_25.log](/logs/device/2023_04_30%2022_53_25.log) | Log | 28 | 0 | 1 | 29 |
| [logs/device/2023_04_30 22_55_21.log](/logs/device/2023_04_30%2022_55_21.log) | Log | 28 | 0 | 1 | 29 |
| [logs/device/2023_04_30 22_58_10.log](/logs/device/2023_04_30%2022_58_10.log) | Log | 31 | 0 | 1 | 32 |
| [logs/device/2023_04_30 22_58_58.log](/logs/device/2023_04_30%2022_58_58.log) | Log | 34 | 0 | 1 | 35 |
| [logs/device/2023_04_30 22_59_43.log](/logs/device/2023_04_30%2022_59_43.log) | Log | 11 | 0 | 1 | 12 |
| [logs/device/2023_04_30 22_59_47.log](/logs/device/2023_04_30%2022_59_47.log) | Log | 28 | 0 | 1 | 29 |
| [logs/device/2023_04_30 23_03_24.log](/logs/device/2023_04_30%2023_03_24.log) | Log | 44 | 0 | 1 | 45 |
| [logs/device/2023_04_30 23_06_11.log](/logs/device/2023_04_30%2023_06_11.log) | Log | 32 | 0 | 1 | 33 |
| [logs/device/2023_04_30 23_07_22.log](/logs/device/2023_04_30%2023_07_22.log) | Log | 27 | 0 | 1 | 28 |
| [logs/device/2023_04_30 23_13_38.log](/logs/device/2023_04_30%2023_13_38.log) | Log | 20 | 0 | 1 | 21 |
| [logs/device/2023_05_01 12_53_31.log](/logs/device/2023_05_01%2012_53_31.log) | Log | 67 | 0 | 1 | 68 |
| [logs/device/2023_05_01 12_59_43.log](/logs/device/2023_05_01%2012_59_43.log) | Log | 20 | 0 | 1 | 21 |
| [logs/device/2023_05_01 13_02_10.log](/logs/device/2023_05_01%2013_02_10.log) | Log | 31 | 0 | 1 | 32 |
| [logs/device/2023_05_01 13_07_56.log](/logs/device/2023_05_01%2013_07_56.log) | Log | 22 | 0 | 1 | 23 |
| [logs/device/2023_05_01 13_20_35.log](/logs/device/2023_05_01%2013_20_35.log) | Log | 32 | 0 | 1 | 33 |
| [logs/device/2023_05_01 13_22_31.log](/logs/device/2023_05_01%2013_22_31.log) | Log | 13 | 0 | 1 | 14 |
| [logs/device/2023_05_01 13_23_17.log](/logs/device/2023_05_01%2013_23_17.log) | Log | 27 | 0 | 1 | 28 |
| [logs/device/2023_05_01 13_31_09.log](/logs/device/2023_05_01%2013_31_09.log) | Log | 22 | 0 | 1 | 23 |
| [logs/web/2023_04_30 13_22_34.log](/logs/web/2023_04_30%2013_22_34.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 13_22_36.log](/logs/web/2023_04_30%2013_22_36.log) | Log | 21 | 0 | 1 | 22 |
| [logs/web/2023_04_30 13_23_21.log](/logs/web/2023_04_30%2013_23_21.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 13_23_22.log](/logs/web/2023_04_30%2013_23_22.log) | Log | 10 | 0 | 1 | 11 |
| [logs/web/2023_04_30 13_24_21.log](/logs/web/2023_04_30%2013_24_21.log) | Log | 18 | 0 | 1 | 19 |
| [logs/web/2023_04_30 13_27_59.log](/logs/web/2023_04_30%2013_27_59.log) | Log | 15 | 0 | 1 | 16 |
| [logs/web/2023_04_30 14_04_18.log](/logs/web/2023_04_30%2014_04_18.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_05_18.log](/logs/web/2023_04_30%2014_05_18.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_05_49.log](/logs/web/2023_04_30%2014_05_49.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_07_02.log](/logs/web/2023_04_30%2014_07_02.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_07_24.log](/logs/web/2023_04_30%2014_07_24.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_15_19.log](/logs/web/2023_04_30%2014_15_19.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_15_34.log](/logs/web/2023_04_30%2014_15_34.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_16_31.log](/logs/web/2023_04_30%2014_16_31.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_18_33.log](/logs/web/2023_04_30%2014_18_33.log) | Log | 25 | 0 | 1 | 26 |
| [logs/web/2023_04_30 14_21_10.log](/logs/web/2023_04_30%2014_21_10.log) | Log | 11 | 0 | 1 | 12 |
| [logs/web/2023_04_30 14_26_35.log](/logs/web/2023_04_30%2014_26_35.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 14_29_47.log](/logs/web/2023_04_30%2014_29_47.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_29_59.log](/logs/web/2023_04_30%2014_29_59.log) | Log | 13 | 0 | 1 | 14 |
| [logs/web/2023_04_30 14_32_58.log](/logs/web/2023_04_30%2014_32_58.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_33_48.log](/logs/web/2023_04_30%2014_33_48.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_34_01.log](/logs/web/2023_04_30%2014_34_01.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_34_43.log](/logs/web/2023_04_30%2014_34_43.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_35_23.log](/logs/web/2023_04_30%2014_35_23.log) | Log | 13 | 0 | 1 | 14 |
| [logs/web/2023_04_30 14_37_06.log](/logs/web/2023_04_30%2014_37_06.log) | Log | 13 | 0 | 1 | 14 |
| [logs/web/2023_04_30 14_38_46.log](/logs/web/2023_04_30%2014_38_46.log) | Log | 13 | 0 | 1 | 14 |
| [logs/web/2023_04_30 14_40_38.log](/logs/web/2023_04_30%2014_40_38.log) | Log | 18 | 0 | 1 | 19 |
| [logs/web/2023_04_30 14_47_31.log](/logs/web/2023_04_30%2014_47_31.log) | Log | 21 | 0 | 1 | 22 |
| [logs/web/2023_04_30 14_48_22.log](/logs/web/2023_04_30%2014_48_22.log) | Log | 13 | 0 | 1 | 14 |
| [logs/web/2023_04_30 14_50_52.log](/logs/web/2023_04_30%2014_50_52.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 14_56_52.log](/logs/web/2023_04_30%2014_56_52.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 14_59_11.log](/logs/web/2023_04_30%2014_59_11.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 14_59_32.log](/logs/web/2023_04_30%2014_59_32.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 15_02_47.log](/logs/web/2023_04_30%2015_02_47.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 15_03_08.log](/logs/web/2023_04_30%2015_03_08.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 15_03_43.log](/logs/web/2023_04_30%2015_03_43.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 15_04_30.log](/logs/web/2023_04_30%2015_04_30.log) | Log | 14 | 0 | 1 | 15 |
| [logs/web/2023_04_30 15_21_41.log](/logs/web/2023_04_30%2015_21_41.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 15_31_59.log](/logs/web/2023_04_30%2015_31_59.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 15_35_51.log](/logs/web/2023_04_30%2015_35_51.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 15_41_20.log](/logs/web/2023_04_30%2015_41_20.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 15_47_05.log](/logs/web/2023_04_30%2015_47_05.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 16_14_26.log](/logs/web/2023_04_30%2016_14_26.log) | Log | 51 | 0 | 1 | 52 |
| [logs/web/2023_04_30 16_16_51.log](/logs/web/2023_04_30%2016_16_51.log) | Log | 53 | 0 | 1 | 54 |
| [logs/web/2023_04_30 16_18_37.log](/logs/web/2023_04_30%2016_18_37.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 16_20_10.log](/logs/web/2023_04_30%2016_20_10.log) | Log | 50 | 0 | 1 | 51 |
| [logs/web/2023_04_30 16_21_13.log](/logs/web/2023_04_30%2016_21_13.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 16_21_31.log](/logs/web/2023_04_30%2016_21_31.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 16_27_53.log](/logs/web/2023_04_30%2016_27_53.log) | Log | 19 | 0 | 1 | 20 |
| [logs/web/2023_04_30 16_29_42.log](/logs/web/2023_04_30%2016_29_42.log) | Log | 19 | 0 | 1 | 20 |
| [logs/web/2023_04_30 16_32_43.log](/logs/web/2023_04_30%2016_32_43.log) | Log | 0 | 0 | 1 | 1 |
| [logs/web/2023_04_30 16_32_54.log](/logs/web/2023_04_30%2016_32_54.log) | Log | 19 | 0 | 1 | 20 |
| [logs/web/2023_04_30 16_34_30.log](/logs/web/2023_04_30%2016_34_30.log) | Log | 19 | 0 | 1 | 20 |
| [logs/web/2023_04_30 16_35_32.log](/logs/web/2023_04_30%2016_35_32.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 16_37_03.log](/logs/web/2023_04_30%2016_37_03.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 16_39_21.log](/logs/web/2023_04_30%2016_39_21.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 16_41_22.log](/logs/web/2023_04_30%2016_41_22.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 16_50_43.log](/logs/web/2023_04_30%2016_50_43.log) | Log | 73 | 0 | 1 | 74 |
| [logs/web/2023_04_30 16_59_14.log](/logs/web/2023_04_30%2016_59_14.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 17_01_11.log](/logs/web/2023_04_30%2017_01_11.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_01_36.log](/logs/web/2023_04_30%2017_01_36.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_05_17.log](/logs/web/2023_04_30%2017_05_17.log) | Log | 54 | 0 | 1 | 55 |
| [logs/web/2023_04_30 17_06_43.log](/logs/web/2023_04_30%2017_06_43.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_07_20.log](/logs/web/2023_04_30%2017_07_20.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_09_13.log](/logs/web/2023_04_30%2017_09_13.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_09_41.log](/logs/web/2023_04_30%2017_09_41.log) | Log | 3 | 0 | 1 | 4 |
| [logs/web/2023_04_30 17_10_14.log](/logs/web/2023_04_30%2017_10_14.log) | Log | 31 | 0 | 1 | 32 |
| [logs/web/2023_04_30 17_11_12.log](/logs/web/2023_04_30%2017_11_12.log) | Log | 37 | 0 | 1 | 38 |
| [logs/web/2023_04_30 17_13_28.log](/logs/web/2023_04_30%2017_13_28.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_14_20.log](/logs/web/2023_04_30%2017_14_20.log) | Log | 31 | 0 | 1 | 32 |
| [logs/web/2023_04_30 17_15_34.log](/logs/web/2023_04_30%2017_15_34.log) | Log | 52 | 0 | 1 | 53 |
| [logs/web/2023_04_30 17_16_26.log](/logs/web/2023_04_30%2017_16_26.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_18_16.log](/logs/web/2023_04_30%2017_18_16.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_19_39.log](/logs/web/2023_04_30%2017_19_39.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_20_26.log](/logs/web/2023_04_30%2017_20_26.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_21_31.log](/logs/web/2023_04_30%2017_21_31.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_22_39.log](/logs/web/2023_04_30%2017_22_39.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_23_53.log](/logs/web/2023_04_30%2017_23_53.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_25_17.log](/logs/web/2023_04_30%2017_25_17.log) | Log | 28 | 0 | 1 | 29 |
| [logs/web/2023_04_30 17_26_13.log](/logs/web/2023_04_30%2017_26_13.log) | Log | 31 | 0 | 1 | 32 |
| [logs/web/2023_04_30 17_26_42.log](/logs/web/2023_04_30%2017_26_42.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_27_56.log](/logs/web/2023_04_30%2017_27_56.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_32_30.log](/logs/web/2023_04_30%2017_32_30.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_32_51.log](/logs/web/2023_04_30%2017_32_51.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_48_42.log](/logs/web/2023_04_30%2017_48_42.log) | Log | 28 | 0 | 1 | 29 |
| [logs/web/2023_04_30 17_49_36.log](/logs/web/2023_04_30%2017_49_36.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 17_50_04.log](/logs/web/2023_04_30%2017_50_04.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 17_50_54.log](/logs/web/2023_04_30%2017_50_54.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_54_09.log](/logs/web/2023_04_30%2017_54_09.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_57_37.log](/logs/web/2023_04_30%2017_57_37.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 17_59_36.log](/logs/web/2023_04_30%2017_59_36.log) | Log | 31 | 0 | 1 | 32 |
| [logs/web/2023_04_30 18_00_15.log](/logs/web/2023_04_30%2018_00_15.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 18_00_43.log](/logs/web/2023_04_30%2018_00_43.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 18_03_39.log](/logs/web/2023_04_30%2018_03_39.log) | Log | 41 | 0 | 1 | 42 |
| [logs/web/2023_04_30 18_12_50.log](/logs/web/2023_04_30%2018_12_50.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 18_14_07.log](/logs/web/2023_04_30%2018_14_07.log) | Log | 32 | 0 | 1 | 33 |
| [logs/web/2023_04_30 18_20_06.log](/logs/web/2023_04_30%2018_20_06.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 18_21_14.log](/logs/web/2023_04_30%2018_21_14.log) | Log | 71 | 0 | 1 | 72 |
| [logs/web/2023_04_30 18_22_42.log](/logs/web/2023_04_30%2018_22_42.log) | Log | 35 | 0 | 1 | 36 |
| [logs/web/2023_04_30 18_26_53.log](/logs/web/2023_04_30%2018_26_53.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 18_28_56.log](/logs/web/2023_04_30%2018_28_56.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 18_34_52.log](/logs/web/2023_04_30%2018_34_52.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 20_14_23.log](/logs/web/2023_04_30%2020_14_23.log) | Log | 6 | 0 | 1 | 7 |
| [logs/web/2023_04_30 20_19_52.log](/logs/web/2023_04_30%2020_19_52.log) | Log | 30 | 0 | 1 | 31 |
| [logs/web/2023_04_30 20_23_09.log](/logs/web/2023_04_30%2020_23_09.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 20_24_45.log](/logs/web/2023_04_30%2020_24_45.log) | Log | 53 | 0 | 1 | 54 |
| [logs/web/2023_04_30 20_35_01.log](/logs/web/2023_04_30%2020_35_01.log) | Log | 35 | 0 | 1 | 36 |
| [logs/web/2023_04_30 21_06_43.log](/logs/web/2023_04_30%2021_06_43.log) | Log | 50 | 0 | 1 | 51 |
| [logs/web/2023_04_30 21_10_35.log](/logs/web/2023_04_30%2021_10_35.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 21_14_41.log](/logs/web/2023_04_30%2021_14_41.log) | Log | 59 | 0 | 1 | 60 |
| [logs/web/2023_04_30 21_20_02.log](/logs/web/2023_04_30%2021_20_02.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 21_26_02.log](/logs/web/2023_04_30%2021_26_02.log) | Log | 14 | 0 | 1 | 15 |
| [logs/web/2023_04_30 21_27_07.log](/logs/web/2023_04_30%2021_27_07.log) | Log | 11 | 0 | 1 | 12 |
| [logs/web/2023_04_30 21_28_43.log](/logs/web/2023_04_30%2021_28_43.log) | Log | 11 | 0 | 1 | 12 |
| [logs/web/2023_04_30 21_29_30.log](/logs/web/2023_04_30%2021_29_30.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 21_31_00.log](/logs/web/2023_04_30%2021_31_00.log) | Log | 12 | 0 | 1 | 13 |
| [logs/web/2023_04_30 21_32_14.log](/logs/web/2023_04_30%2021_32_14.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 21_32_41.log](/logs/web/2023_04_30%2021_32_41.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 21_36_31.log](/logs/web/2023_04_30%2021_36_31.log) | Log | 31 | 0 | 1 | 32 |
| [logs/web/2023_04_30 21_37_14.log](/logs/web/2023_04_30%2021_37_14.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 22_16_20.log](/logs/web/2023_04_30%2022_16_20.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 22_17_01.log](/logs/web/2023_04_30%2022_17_01.log) | Log | 10 | 0 | 1 | 11 |
| [logs/web/2023_04_30 22_18_32.log](/logs/web/2023_04_30%2022_18_32.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 22_21_09.log](/logs/web/2023_04_30%2022_21_09.log) | Log | 9 | 0 | 1 | 10 |
| [logs/web/2023_04_30 22_51_06.log](/logs/web/2023_04_30%2022_51_06.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 22_53_25.log](/logs/web/2023_04_30%2022_53_25.log) | Log | 8 | 0 | 1 | 9 |
| [logs/web/2023_04_30 22_55_21.log](/logs/web/2023_04_30%2022_55_21.log) | Log | 8 | 0 | 1 | 9 |
| [logs/web/2023_04_30 22_58_10.log](/logs/web/2023_04_30%2022_58_10.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 22_58_57.log](/logs/web/2023_04_30%2022_58_57.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 22_59_42.log](/logs/web/2023_04_30%2022_59_42.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 22_59_47.log](/logs/web/2023_04_30%2022_59_47.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_04_30 23_03_24.log](/logs/web/2023_04_30%2023_03_24.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 23_06_11.log](/logs/web/2023_04_30%2023_06_11.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_04_30 23_07_22.log](/logs/web/2023_04_30%2023_07_22.log) | Log | 6 | 0 | 1 | 7 |
| [logs/web/2023_04_30 23_13_38.log](/logs/web/2023_04_30%2023_13_38.log) | Log | 9 | 0 | 1 | 10 |
| [logs/web/2023_05_01 12_53_31.log](/logs/web/2023_05_01%2012_53_31.log) | Log | 40 | 0 | 1 | 41 |
| [logs/web/2023_05_01 12_59_43.log](/logs/web/2023_05_01%2012_59_43.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_05_01 13_02_10.log](/logs/web/2023_05_01%2013_02_10.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_05_01 13_07_56.log](/logs/web/2023_05_01%2013_07_56.log) | Log | 29 | 0 | 1 | 30 |
| [logs/web/2023_05_01 13_20_35.log](/logs/web/2023_05_01%2013_20_35.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_05_01 13_22_31.log](/logs/web/2023_05_01%2013_22_31.log) | Log | 1 | 0 | 1 | 2 |
| [logs/web/2023_05_01 13_23_17.log](/logs/web/2023_05_01%2013_23_17.log) | Log | 22 | 0 | 1 | 23 |
| [logs/web/2023_05_01 13_31_09.log](/logs/web/2023_05_01%2013_31_09.log) | Log | 22 | 0 | 1 | 23 |
| [main.py](/main.py) | Python | 29 | 6 | 8 | 43 |
| [requirements.txt](/requirements.txt) | pip requirements | 8 | 0 | 1 | 9 |
| [utils/get_time.py](/utils/get_time.py) | Python | 24 | 4 | 11 | 39 |
| [utils/mlogging.py](/utils/mlogging.py) | Python | 24 | 5 | 6 | 35 |
| [web/app/__init__.py](/web/app/__init__.py) | Python | 37 | 9 | 11 | 57 |
| [web/app/config.py](/web/app/config.py) | Python | 52 | 10 | 9 | 71 |
| [web/app/models/models.py](/web/app/models/models.py) | Python | 115 | 14 | 25 | 154 |
| [web/app/public.py](/web/app/public.py) | Python | 30 | 3 | 6 | 39 |
| [web/app/static/device/amis/ang-ie11.css](/web/app/static/device/amis/ang-ie11.css) | CSS | 87,921 | 3,173 | 22,989 | 114,083 |
| [web/app/static/device/amis/ang.css](/web/app/static/device/amis/ang.css) | CSS | 90,214 | 3,173 | 22,995 | 116,382 |
| [web/app/static/device/amis/antd-ie11.css](/web/app/static/device/amis/antd-ie11.css) | CSS | 87,920 | 3,173 | 22,989 | 114,082 |
| [web/app/static/device/amis/antd.css](/web/app/static/device/amis/antd.css) | CSS | 90,193 | 3,173 | 22,994 | 116,360 |
| [web/app/static/device/amis/barcode.js](/web/app/static/device/amis/barcode.js) | JavaScript | 100 | 0 | 0 | 100 |
| [web/app/static/device/amis/charts.js](/web/app/static/device/amis/charts.js) | JavaScript | 32 | 45 | 0 | 77 |
| [web/app/static/device/amis/codemirror.js](/web/app/static/device/amis/codemirror.js) | JavaScript | 14 | 0 | 0 | 14 |
| [web/app/static/device/amis/color-picker.js](/web/app/static/device/amis/color-picker.js) | JavaScript | 130 | 0 | 0 | 130 |
| [web/app/static/device/amis/cropperjs.js](/web/app/static/device/amis/cropperjs.js) | JavaScript | 5 | 9 | 0 | 14 |
| [web/app/static/device/amis/cxd-ie11.css](/web/app/static/device/amis/cxd-ie11.css) | CSS | 87,920 | 3,173 | 22,989 | 114,082 |
| [web/app/static/device/amis/cxd.css](/web/app/static/device/amis/cxd.css) | CSS | 90,189 | 3,173 | 22,994 | 116,356 |
| [web/app/static/device/amis/dark-ie11.css](/web/app/static/device/amis/dark-ie11.css) | CSS | 87,920 | 3,173 | 22,989 | 114,082 |
| [web/app/static/device/amis/dark.css](/web/app/static/device/amis/dark.css) | CSS | 90,195 | 3,173 | 22,994 | 116,362 |
| [web/app/static/device/amis/exceljs.js](/web/app/static/device/amis/exceljs.js) | JavaScript | 10 | 30 | 4 | 44 |
| [web/app/static/device/amis/helper.css](/web/app/static/device/amis/helper.css) | CSS | 44,655 | 2,930 | 0 | 47,585 |
| [web/app/static/device/amis/iconfont.css](/web/app/static/device/amis/iconfont.css) | CSS | 2,404 | 0 | 1 | 2,405 |
| [web/app/static/device/amis/iconfont.svg](/web/app/static/device/amis/iconfont.svg) | XML | 848 | 3 | 1,663 | 2,514 |
| [web/app/static/device/amis/ie11-patch.css](/web/app/static/device/amis/ie11-patch.css) | CSS | 1 | 0 | 1 | 2 |
| [web/app/static/device/amis/locale/de-DE.js](/web/app/static/device/amis/locale/de-DE.js) | JavaScript | 405 | 0 | 3 | 408 |
| [web/app/static/device/amis/markdown.js](/web/app/static/device/amis/markdown.js) | JavaScript | 136 | 0 | 0 | 136 |
| [web/app/static/device/amis/papaparse.js](/web/app/static/device/amis/papaparse.js) | JavaScript | 4 | 6 | 3 | 13 |
| [web/app/static/device/amis/rest.js](/web/app/static/device/amis/rest.js) | JavaScript | 32 | 0 | 0 | 32 |
| [web/app/static/device/amis/rich-text.js](/web/app/static/device/amis/rich-text.js) | JavaScript | 123 | 158 | 118 | 399 |
| [web/app/static/device/amis/sdk-ie11.css](/web/app/static/device/amis/sdk-ie11.css) | CSS | 87,920 | 3,173 | 22,989 | 114,082 |
| [web/app/static/device/amis/sdk.css](/web/app/static/device/amis/sdk.css) | CSS | 90,189 | 3,173 | 22,994 | 116,356 |
| [web/app/static/device/amis/sdk.js](/web/app/static/device/amis/sdk.js) | JavaScript | 3,439 | 236 | 114 | 3,789 |
| [web/app/static/device/amis/thirds/hls.js/hls.js](/web/app/static/device/amis/thirds/hls.js/hls.js) | JavaScript | 92 | 273 | 0 | 365 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/base/worker/workerMain.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/base/worker/workerMain.js) | JavaScript | 8 | 8 | 2 | 18 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/apex/apex.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/apex/apex.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/azcli/azcli.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/azcli/azcli.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/bat/bat.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/bat/bat.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/clojure/clojure.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/clojure/clojure.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/coffee/coffee.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/coffee/coffee.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/cpp/cpp.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/cpp/cpp.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/csharp/csharp.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/csharp/csharp.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/css/css.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/css/css.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/dockerfile/dockerfile.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/dockerfile/dockerfile.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/fsharp/fsharp.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/fsharp/fsharp.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/go/go.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/go/go.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/handlebars/handlebars.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/handlebars/handlebars.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/html/html.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/html/html.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/ini/ini.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/ini/ini.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/java/java.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/java/java.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/javascript/javascript.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/javascript/javascript.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/less/less.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/less/less.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/lua/lua.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/lua/lua.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/markdown/markdown.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/markdown/markdown.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/msdax/msdax.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/msdax/msdax.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/objective-c/objective-c.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/objective-c/objective-c.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/php/php.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/php/php.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/postiats/postiats.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/postiats/postiats.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/powershell/powershell.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/powershell/powershell.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/pug/pug.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/pug/pug.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/python/python.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/python/python.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/r/r.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/r/r.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/razor/razor.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/razor/razor.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/redis/redis.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/redis/redis.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/redshift/redshift.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/redshift/redshift.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/ruby/ruby.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/ruby/ruby.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/rust/rust.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/rust/rust.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/sb/sb.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/sb/sb.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/scheme/scheme.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/scheme/scheme.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/scss/scss.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/scss/scss.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/shell/shell.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/shell/shell.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/solidity/solidity.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/solidity/solidity.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/sql/sql.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/sql/sql.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/st/st.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/st/st.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/swift/swift.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/swift/swift.js) | JavaScript | 1 | 9 | 0 | 10 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/typescript/typescript.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/typescript/typescript.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/vb/vb.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/vb/vb.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/xml/xml.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/xml/xml.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/yaml/yaml.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/basic-languages/yaml/yaml.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/editor/editor.main.css](/web/app/static/device/amis/thirds/monaco-editor/min/vs/editor/editor.main.css) | CSS | 1 | 5 | 0 | 6 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/editor/editor.main.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/editor/editor.main.js) | JavaScript | 661 | 58 | 90 | 809 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/editor/editor.main.nls.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/editor/editor.main.nls.js) | JavaScript | 4 | 6 | 1 | 11 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/editor/editor.main.nls.zh-cn.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/editor/editor.main.nls.zh-cn.js) | JavaScript | 6 | 6 | 1 | 13 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/language/css/cssMode.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/language/css/cssMode.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/language/css/cssWorker.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/language/css/cssWorker.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/language/html/htmlMode.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/language/html/htmlMode.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/language/html/htmlWorker.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/language/html/htmlWorker.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/language/json/jsonMode.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/language/json/jsonMode.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/language/json/jsonWorker.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/language/json/jsonWorker.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/language/typescript/tsMode.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/language/typescript/tsMode.js) | JavaScript | 1 | 6 | 0 | 7 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/language/typescript/tsWorker.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/language/typescript/tsWorker.js) | JavaScript | 1 | 20 | 0 | 21 |
| [web/app/static/device/amis/thirds/monaco-editor/min/vs/loader.js](/web/app/static/device/amis/thirds/monaco-editor/min/vs/loader.js) | JavaScript | 4 | 6 | 1 | 11 |
| [web/app/static/device/amis/thirds/mpegts.js/mpegts.js](/web/app/static/device/amis/thirds/mpegts.js/mpegts.js) | JavaScript | 2 | 7 | 0 | 9 |
| [web/app/static/device/amis/tinymce.js](/web/app/static/device/amis/tinymce.js) | JavaScript | 109 | 1 | 0 | 110 |
| [web/app/static/device/css/fonts/fontawesome-webfont.svg](/web/app/static/device/css/fonts/fontawesome-webfont.svg) | XML | 2,671 | 0 | 1 | 2,672 |
| [web/app/static/device/css/icons/backkeys.svg](/web/app/static/device/css/icons/backkeys.svg) | XML | 7 | 0 | 1 | 8 |
| [web/app/static/device/css/icons/close.svg](/web/app/static/device/css/icons/close.svg) | XML | 3 | 0 | 0 | 3 |
| [web/app/static/device/css/icons/file.svg](/web/app/static/device/css/icons/file.svg) | XML | 3 | 0 | 0 | 3 |
| [web/app/static/device/css/icons/forwardkeys.svg](/web/app/static/device/css/icons/forwardkeys.svg) | XML | 10 | 0 | 1 | 11 |
| [web/app/static/device/css/icons/more.svg](/web/app/static/device/css/icons/more.svg) | XML | 3 | 0 | 0 | 3 |
| [web/app/static/device/css/icons/nav.svg](/web/app/static/device/css/icons/nav.svg) | XML | 3 | 0 | 1 | 4 |
| [web/app/static/device/css/icons/notes.svg](/web/app/static/device/css/icons/notes.svg) | XML | 3 | 0 | 1 | 4 |
| [web/app/static/device/css/icons/search.svg](/web/app/static/device/css/icons/search.svg) | XML | 6 | 0 | 1 | 7 |
| [web/app/static/device/css/style.css](/web/app/static/device/css/style.css) | CSS | 19,982 | 334 | 2,749 | 23,065 |
| [web/app/static/device/js/app.js](/web/app/static/device/js/app.js) | JavaScript | 61,878 | 2,669 | 3,345 | 67,892 |
| [web/app/static/device/js/data.js](/web/app/static/device/js/data.js) | JavaScript | 799 | 0 | 1 | 800 |
| [web/app/static/device/scripts/app.js](/web/app/static/device/scripts/app.js) | JavaScript | 61,878 | 2,669 | 3,345 | 67,892 |
| [web/app/static/device/scripts/data.js](/web/app/static/device/scripts/data.js) | JavaScript | 1 | 0 | 0 | 1 |
| [web/app/static/login/css/style.css](/web/app/static/login/css/style.css) | CSS | 287 | 15 | 1 | 303 |
| [web/app/static/login/js/jquery-2.2.3.min.js](/web/app/static/login/js/jquery-2.2.3.min.js) | JavaScript | 3 | 1 | 1 | 5 |
| [web/app/templates/device/base.html](/web/app/templates/device/base.html) | HTML | 122 | 6 | 10 | 138 |
| [web/app/templates/device/data.html](/web/app/templates/device/data.html) | HTML | 442 | 2 | 8 | 452 |
| [web/app/templates/device/index.html](/web/app/templates/device/index.html) | HTML | 536 | 2 | 12 | 550 |
| [web/app/templates/login/login.html](/web/app/templates/login/login.html) | HTML | 73 | 20 | 10 | 103 |
| [web/app/utils/get_time.py](/web/app/utils/get_time.py) | Python | 23 | 16 | 5 | 44 |
| [web/app/views/device/__init__.py](/web/app/views/device/__init__.py) | Python | 15 | 4 | 3 | 22 |
| [web/app/views/device/views.py](/web/app/views/device/views.py) | Python | 390 | 68 | 63 | 521 |
| [web/app/views/index/__init__.py](/web/app/views/index/__init__.py) | Python | 12 | 2 | 2 | 16 |
| [web/app/views/index/views.py](/web/app/views/index/views.py) | Python | 25 | 5 | 6 | 36 |
| [web/app/views/login/__init__.py](/web/app/views/login/__init__.py) | Python | 14 | 3 | 3 | 20 |
| [web/app/views/login/views.py](/web/app/views/login/views.py) | Python | 33 | 5 | 5 | 43 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)