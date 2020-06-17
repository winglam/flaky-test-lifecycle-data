# Data for A Study on the Lifecycle of Flaky Tests

The contents of this directory are the following.
- ```Table2-Flaky-Tests-anon.csv``` contains the data that we used to obtain Table 2.
- ```Tables3and4-Reproducibility-Runtime-anon.csv``` contains the data that we used to obtain Tables 3 and 4.
- ```Tables5and7-Categories-anon.csv``` contains the data that we used to obtain Tables 5 and 7.
- ```generate-plots.py``` contains the python script that we used to generate the plots in Figures 2 and 3 and the data in Tables 3 and 4.

All data are from proprietary projects within Microsoft and are, therefore, anonymized for confidentiality reasons.

Project names (e.g., ```ProjC```) in ```Table2-Flaky-Tests-anon.csv``` will match the project names in the paper and the ones in ```Tables3and4-Reproducibility-Runtime-anon.csv``` and ```Tables5and7-Categories-anon.csv```.

Test names (e.g., ```TEST-793```) in ```Table2-Flaky-Tests-anon.csv``` will match the test names in ```Tables5and7-Categories-anon.csv```. Note that only test names that are ```FixedWithPR``` in ```Table2-Flaky-Tests-anon.csv``` will appear in ```Tables5and7-Categories-anon.csv```.

Flaky tests in ```Tables5and7-Categories-anon.csv``` may be linked to multiple pull requests (e.g., the developer fixed the flakiness of the test through multiple pull requests).

# Cite

If you use any of this data, please cite our corresponding [ICSE paper](http://mir.cs.illinois.edu/winglam/publications/2020/LamETAL20FaTB.pdf):
```
@inproceedings{LamETAL2020FaTB,
    author      = "Wing Lam and K{\i}van{\c{c}} Mu{\c{s}}lu and Hitesh Sajnani and Suresh Thummalapenta",
    title       = "A Study on the Lifecycle of Flaky Tests",
    booktitle   = "ICSE 2020, Proceedings of the 42nd International Conference on Software Engineering",
    month       = "may",
    year = 	 2020,
    address = 	 "Seoul, South Korea",
    pages       = "pages-to-appear"
}
```
