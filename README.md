三位一体招生信息爬虫
====

**三位一体招生信息爬虫**用于爬取[中国教育在线](http://www.eol.cn/html/g/zjswyt/)中的浙江高校三位一体报考简章中的信息，并写入Excel
表，以供学生及生涯规划咨询师查阅。

## Version
- 0.0.0
    - ADD:使用requests下载网页
    - ADD:使用BeautifulSoap爬取表格中的学校名称，报考时间，网址，并存入一个`list`
    
- 0.0.1
    - CHANGE: The format of docstrings
    - CHANGE: Some variable and arguments names
    - ADD: A bunch of printings lines for debugging and tracing the running of the program
    
- v0.0.2
    - ADD: Update README.md
    - CHANGE: Delete some useless files

- v1.0.0
    - Fixed: Exclude 中国美术学院 to write to the excel
    - ADD: Function get_link(school_name)
    - ADD: Function get_admission_guide(link)
    - ADD: Function parse_admission_guide(html)
    - ADD: Function write_admission_guide_to_cvs()

- v1.1.0
    - CHANGE: The name of the file "三位一体招生信息爬虫.py" to "admission_info_crawler"
    - Add: File test_admission_info_crawler.py
    
- v1.1.1
    - UPDATE: The version in README.md

## Contact
**Fan Zhang**
- Homepage: https://github.com/fanzhangg
- e-mail: vanadium-zhang@outlook.com