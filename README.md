[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">PySpark Action Operations</h3>

  <p align="center">
    PySpark all action operation functions.
    <br />
    <br />
    <a href="https://github.com/BankNatchapol/PySpark-Action-Operations/issues">Report Bug</a>
    ·
    <a href="https://github.com/BankNatchapol/PySpark-Action-Operations/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
        <a href="#dataset">Dataset</a>
    </li>

<li>
      <a href="#submitting">Submitting</a>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- INSTALLATION -->
## Installation
you can install spark follow this link [Spark](https://spark.apache.org/downloads.html)

<!-- DATASET -->
## Dataset
prime_nums.text file is file that contains prime numbers from 2 to 541

<!-- SUBMITTING -->
## Submitting 
there are 5 action operation function files.<br>
### Collect 
retrieve all the elements of the dataset (from all nodes) to the driver node.
> spark-submit collect.py

### Take 
returns the first num rows of dataset as a list of row.
> spark-submit take.py

### Count 
return the number of elements in this RDD.
> spark-submit count.py

### CountByValue 
return the count of each unique value in this RDD as a dictionary of (value, count) pairs.
> spark-submit countByValue.py

### Reduce 
aggregate action function is used to calculate min, max, and total of elements in a dataset.
> spark-submit reduce.py

<!-- CONTACT -->
## Contact

Facebook - [@Natchapol Patamawisut](https://www.facebook.com/natchapol.patamawisut/)

Project Link: [https://github.com/BankNatchapol/PySpark-Action-Operations](https://github.com/BankNatchapol/PySpark-Action-Operations)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/natchapol-patamawisut
