# Diff Details

Date : 2023-05-01 13:43:02

Directory y:\\研究生\\跨越网关\\代码\\Gateway_System

Total : 205 files,  1184 codes, -18 comments, -22 blanks, all 1144 lines

[Summary](results.md) / [Details](details.md) / [Diff Summary](diff.md) / Diff Details

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [control/src/config.py](/control/src/config.py) | Python | 2 | 1 | 0 | 3 |
| [control/src/core_scheduling.py](/control/src/core_scheduling.py) | Python | 73 | -11 | 5 | 67 |
| [control/src/device_manager.py](/control/src/device_manager.py) | Python | 5 | 0 | 1 | 6 |
| [control/src/driver/bsp_underwater_acoustic_comm.py](/control/src/driver/bsp_underwater_acoustic_comm.py) | Python | -2 | -5 | -2 | -9 |
| [control/src/task_queue.py](/control/src/task_queue.py) | Python | 31 | 5 | 6 | 42 |
| [db/gateway.db](/db/gateway.db) | Database | 2 | 0 | 0 | 2 |
| [logs/device/2023_04_30 13_22_36.log](/logs/device/2023_04_30%2013_22_36.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 13_23_21.log](/logs/device/2023_04_30%2013_23_21.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 13_23_23.log](/logs/device/2023_04_30%2013_23_23.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 13_24_21.log](/logs/device/2023_04_30%2013_24_21.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 13_27_59.log](/logs/device/2023_04_30%2013_27_59.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 14_04_18.log](/logs/device/2023_04_30%2014_04_18.log) | Log | -1 | 0 | -1 | -2 |
| [logs/device/2023_04_30 14_05_18.log](/logs/device/2023_04_30%2014_05_18.log) | Log | -1 | 0 | -1 | -2 |
| [logs/device/2023_04_30 14_05_49.log](/logs/device/2023_04_30%2014_05_49.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 14_07_02.log](/logs/device/2023_04_30%2014_07_02.log) | Log | -6 | 0 | -1 | -7 |
| [logs/device/2023_04_30 14_07_24.log](/logs/device/2023_04_30%2014_07_24.log) | Log | -6 | 0 | -1 | -7 |
| [logs/device/2023_04_30 14_15_19.log](/logs/device/2023_04_30%2014_15_19.log) | Log | -6 | 0 | -1 | -7 |
| [logs/device/2023_04_30 14_15_35.log](/logs/device/2023_04_30%2014_15_35.log) | Log | -6 | 0 | -1 | -7 |
| [logs/device/2023_04_30 14_16_32.log](/logs/device/2023_04_30%2014_16_32.log) | Log | -6 | 0 | -1 | -7 |
| [logs/device/2023_04_30 14_18_33.log](/logs/device/2023_04_30%2014_18_33.log) | Log | -1 | 0 | -1 | -2 |
| [logs/device/2023_04_30 14_21_10.log](/logs/device/2023_04_30%2014_21_10.log) | Log | -1 | 0 | -1 | -2 |
| [logs/device/2023_04_30 14_26_35.log](/logs/device/2023_04_30%2014_26_35.log) | Log | -1 | 0 | -1 | -2 |
| [logs/device/2023_04_30 14_29_47.log](/logs/device/2023_04_30%2014_29_47.log) | Log | -4 | 0 | -1 | -5 |
| [logs/device/2023_04_30 14_29_59.log](/logs/device/2023_04_30%2014_29_59.log) | Log | -1 | 0 | -1 | -2 |
| [logs/device/2023_04_30 14_32_59.log](/logs/device/2023_04_30%2014_32_59.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 14_33_49.log](/logs/device/2023_04_30%2014_33_49.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 14_34_01.log](/logs/device/2023_04_30%2014_34_01.log) | Log | -2 | 0 | -1 | -3 |
| [logs/device/2023_04_30 14_34_43.log](/logs/device/2023_04_30%2014_34_43.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 14_35_24.log](/logs/device/2023_04_30%2014_35_24.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 14_37_06.log](/logs/device/2023_04_30%2014_37_06.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 14_38_46.log](/logs/device/2023_04_30%2014_38_46.log) | Log | -40 | 0 | -1 | -41 |
| [logs/device/2023_04_30 14_40_38.log](/logs/device/2023_04_30%2014_40_38.log) | Log | -40 | 0 | -1 | -41 |
| [logs/device/2023_04_30 14_47_32.log](/logs/device/2023_04_30%2014_47_32.log) | Log | -41 | 0 | -1 | -42 |
| [logs/device/2023_04_30 14_48_22.log](/logs/device/2023_04_30%2014_48_22.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 14_50_52.log](/logs/device/2023_04_30%2014_50_52.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 14_56_52.log](/logs/device/2023_04_30%2014_56_52.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 14_59_12.log](/logs/device/2023_04_30%2014_59_12.log) | Log | -15 | 0 | -1 | -16 |
| [logs/device/2023_04_30 14_59_32.log](/logs/device/2023_04_30%2014_59_32.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 15_02_47.log](/logs/device/2023_04_30%2015_02_47.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 15_03_09.log](/logs/device/2023_04_30%2015_03_09.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 15_03_43.log](/logs/device/2023_04_30%2015_03_43.log) | Log | -4 | 0 | -1 | -5 |
| [logs/device/2023_04_30 15_04_30.log](/logs/device/2023_04_30%2015_04_30.log) | Log | -4 | 0 | -1 | -5 |
| [logs/device/2023_04_30 15_21_41.log](/logs/device/2023_04_30%2015_21_41.log) | Log | -19 | 0 | -1 | -20 |
| [logs/device/2023_04_30 15_31_59.log](/logs/device/2023_04_30%2015_31_59.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 15_35_51.log](/logs/device/2023_04_30%2015_35_51.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 15_41_20.log](/logs/device/2023_04_30%2015_41_20.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 15_47_05.log](/logs/device/2023_04_30%2015_47_05.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 15_55_27.log](/logs/device/2023_04_30%2015_55_27.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_03_33.log](/logs/device/2023_04_30%2016_03_33.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 16_03_51.log](/logs/device/2023_04_30%2016_03_51.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 16_05_49.log](/logs/device/2023_04_30%2016_05_49.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 16_06_44.log](/logs/device/2023_04_30%2016_06_44.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 16_07_18.log](/logs/device/2023_04_30%2016_07_18.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 16_08_22.log](/logs/device/2023_04_30%2016_08_22.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_10_08.log](/logs/device/2023_04_30%2016_10_08.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_10_27.log](/logs/device/2023_04_30%2016_10_27.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_11_25.log](/logs/device/2023_04_30%2016_11_25.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 16_11_50.log](/logs/device/2023_04_30%2016_11_50.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_12_00.log](/logs/device/2023_04_30%2016_12_00.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 16_14_26.log](/logs/device/2023_04_30%2016_14_26.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 16_16_51.log](/logs/device/2023_04_30%2016_16_51.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 16_18_37.log](/logs/device/2023_04_30%2016_18_37.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 16_20_10.log](/logs/device/2023_04_30%2016_20_10.log) | Log | -14 | 0 | -1 | -15 |
| [logs/device/2023_04_30 16_21_13.log](/logs/device/2023_04_30%2016_21_13.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_21_31.log](/logs/device/2023_04_30%2016_21_31.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 16_27_54.log](/logs/device/2023_04_30%2016_27_54.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_29_43.log](/logs/device/2023_04_30%2016_29_43.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_32_43.log](/logs/device/2023_04_30%2016_32_43.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_32_54.log](/logs/device/2023_04_30%2016_32_54.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_34_30.log](/logs/device/2023_04_30%2016_34_30.log) | Log | -10 | 0 | -1 | -11 |
| [logs/device/2023_04_30 16_35_33.log](/logs/device/2023_04_30%2016_35_33.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 16_37_03.log](/logs/device/2023_04_30%2016_37_03.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 16_39_21.log](/logs/device/2023_04_30%2016_39_21.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 16_41_22.log](/logs/device/2023_04_30%2016_41_22.log) | Log | -40 | 0 | -1 | -41 |
| [logs/device/2023_04_30 16_50_43.log](/logs/device/2023_04_30%2016_50_43.log) | Log | -13 | 0 | -1 | -14 |
| [logs/device/2023_04_30 16_59_14.log](/logs/device/2023_04_30%2016_59_14.log) | Log | -13 | 0 | -1 | -14 |
| [logs/device/2023_04_30 17_01_11.log](/logs/device/2023_04_30%2017_01_11.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 17_01_37.log](/logs/device/2023_04_30%2017_01_37.log) | Log | -38 | 0 | -5 | -43 |
| [logs/device/2023_04_30 17_05_17.log](/logs/device/2023_04_30%2017_05_17.log) | Log | -65 | 0 | -9 | -74 |
| [logs/device/2023_04_30 17_06_44.log](/logs/device/2023_04_30%2017_06_44.log) | Log | -13 | 0 | -1 | -14 |
| [logs/device/2023_04_30 17_07_20.log](/logs/device/2023_04_30%2017_07_20.log) | Log | -11 | 0 | -1 | -12 |
| [logs/device/2023_04_30 17_09_13.log](/logs/device/2023_04_30%2017_09_13.log) | Log | -3 | 0 | -1 | -4 |
| [logs/device/2023_04_30 17_09_41.log](/logs/device/2023_04_30%2017_09_41.log) | Log | -38 | 0 | -5 | -43 |
| [logs/device/2023_04_30 17_10_14.log](/logs/device/2023_04_30%2017_10_14.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 17_11_13.log](/logs/device/2023_04_30%2017_11_13.log) | Log | -38 | 0 | -5 | -43 |
| [logs/device/2023_04_30 17_13_28.log](/logs/device/2023_04_30%2017_13_28.log) | Log | -38 | 0 | -5 | -43 |
| [logs/device/2023_04_30 17_14_20.log](/logs/device/2023_04_30%2017_14_20.log) | Log | -38 | 0 | -5 | -43 |
| [logs/device/2023_04_30 17_15_34.log](/logs/device/2023_04_30%2017_15_34.log) | Log | -65 | 0 | -9 | -74 |
| [logs/device/2023_04_30 17_16_26.log](/logs/device/2023_04_30%2017_16_26.log) | Log | -38 | 0 | -5 | -43 |
| [logs/device/2023_04_30 17_18_16.log](/logs/device/2023_04_30%2017_18_16.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 17_19_39.log](/logs/device/2023_04_30%2017_19_39.log) | Log | -37 | 0 | -3 | -40 |
| [logs/device/2023_04_30 17_20_26.log](/logs/device/2023_04_30%2017_20_26.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 17_21_31.log](/logs/device/2023_04_30%2017_21_31.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 17_22_40.log](/logs/device/2023_04_30%2017_22_40.log) | Log | -33 | 0 | -3 | -36 |
| [logs/device/2023_04_30 17_23_54.log](/logs/device/2023_04_30%2017_23_54.log) | Log | -12 | 0 | -1 | -13 |
| [logs/device/2023_04_30 17_25_17.log](/logs/device/2023_04_30%2017_25_17.log) | Log | -13 | 0 | -1 | -14 |
| [logs/device/2023_04_30 17_26_13.log](/logs/device/2023_04_30%2017_26_13.log) | Log | -13 | 0 | -1 | -14 |
| [logs/device/2023_04_30 17_26_42.log](/logs/device/2023_04_30%2017_26_42.log) | Log | -13 | 0 | -1 | -14 |
| [logs/device/2023_04_30 17_27_56.log](/logs/device/2023_04_30%2017_27_56.log) | Log | -13 | 0 | -1 | -14 |
| [logs/device/2023_04_30 17_32_30.log](/logs/device/2023_04_30%2017_32_30.log) | Log | -14 | 0 | -1 | -15 |
| [logs/device/2023_04_30 17_32_52.log](/logs/device/2023_04_30%2017_32_52.log) | Log | -14 | 0 | -1 | -15 |
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
| [main.py](/main.py) | Python | 17 | 3 | 2 | 22 |
| [pika_trans.py](/pika_trans.py) | Python | -10 | -9 | -2 | -21 |
| [requirements.txt](/requirements.txt) | pip requirements | 2 | 0 | 0 | 2 |
| [test.py](/test.py) | Python | -13 | -4 | -5 | -22 |
| [utils/get_time.py](/utils/get_time.py) | Python | 13 | 2 | 9 | 24 |
| [web/app/views/device/views.py](/web/app/views/device/views.py) | Python | 5 | 0 | 3 | 8 |

[Summary](results.md) / [Details](details.md) / [Diff Summary](diff.md) / Diff Details